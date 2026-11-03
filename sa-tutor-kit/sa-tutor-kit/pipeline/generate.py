#!/usr/bin/env python3
"""
generate.py - ask the teacher model to write one tutoring record per plan row.

    python pipeline/generate.py --round r1 --dry-run          # show one prompt + the projected cost
    python pipeline/generate.py --round r1 --limit 10         # ALWAYS test on 10 first, then READ them
    python pipeline/generate.py --round r1 --workers 4        # the real run (safe to stop and restart)

WHAT THE TEACHER DOES vs WHAT THE PIPELINE DOES
  The teacher writes only the CONVERSATION (the learner's messages, the tutor's private reasoning, the
  tutor's replies, tool calls) and a few meta notes. The pipeline fills in everything it can know for sure:
  the control settings (from the plan), thinking on/off, ids, licence/attribution (from the item), and the
  REAL tool results (tools_sim.py). A model that is allowed to write labels will sometimes write wrong ones.

  Faithful mode : the teacher teaches the real exam question. We keep the memo's final answer as the
                  truth and later check the teacher's own answer against it.
  Original mode : the teacher invents a NEW question of the same type (this avoids copying exam papers)
                  and must also return a tiny Python snippet that prints the final answer. verify.py runs
                  it and compares. Code is better at arithmetic than a language model is.

OUTPUT   workspace/gen/<round>/
  raw_outputs.jsonl   every reply (so you can debug the prompt without paying again)
  candidates.jsonl    records that passed the schema check (still UNVERIFIED)
  failed.jsonl        plan rows that never produced a valid record, with the reasons
"""
import argparse
import json
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import retrieval  # noqa: E402
import tools_sim  # noqa: E402
import tutor_data as td  # noqa: E402
from llm import BudgetExceeded, Client, extract_json  # noqa: E402
from wspaths import KIT_ROOT, append_jsonl, p, read_jsonl  # noqa: E402

LOCK = threading.Lock()
SYSTEM = ("You are an expert South African teacher and a careful data writer. You write ONE training record for a "
          "school tutor AI. Follow the TUTOR SPEC exactly. Reply with a single JSON object and nothing else.")

LANG_DESC = {"en": "English", "af": "Afrikaans", "mixed": "a mix of Afrikaans and English (code-switching), the way many South African learners type"}
STYLE_DESC = {
    "plain": "clear, short sentences",
    "informal": "informal and short, like a message to a friend (lower-case, maybe a typo or two, no formal maths layout)",
    "with_attempt": "includes their own (possibly wrong) attempt at the problem",
}

TEMPLATE = """=== TUTOR SPEC (follow it exactly) ===
{spec}

=== THIS RECORD ===
control (the settings the tutor must obey): {control}
thinking: {thinking}   (on = EVERY assistant message has a private "reasoning" string; off = none do)
mode: {mode}

SOURCE ITEM
subject: {subject}   grade: {grade}   topic: {topic}
{passage}question: {question}
memo / worked solution: {memo}
final answer from the memo: {final}

LEARNER SIMULATION
- the learner writes in: {lang}
- the learner's state: {state}
- writing style: {style}
- include this common misunderstanding (the tutor should notice it and deal with it kindly): {mis}
- the learner sends {turns} message(s) in total; the first one presents the question

{mode_rules}

OUTPUT: one JSON object:
{{"messages": [ {{"role": "user", "content": "..."}}, {{"role": "assistant", {reasoning_hint}"content": "..."}}, ... ],
  "meta": {{"strategy_used": "...", "topic": "...", "techniques": ["..."], "misconception_targeted": "...",
           "final_answer": "...", "verify_code": "..."}}}}

RULES
1. Messages alternate user / assistant, start with a user message, and END with a plain assistant reply. No system message.
2. {reasoning_rule}
3. Reply language follows control.response_language ("mirror" = the language the learner wrote in). Use correct CAPS terms. Afrikaans must read naturally, like a good Afrikaans teacher wrote it.
4. Obey control.answer_policy. Under hint_only never state the final answer in any assistant reply (the private reasoning may contain it).
5. Obey control.strategy (if it is "auto", choose the best one and put it in meta.strategy_used), control.tone, control.response_length (per assistant message) and control.math_format.
6. Tools: use only tools listed in control.tools. A tool call is an assistant message with "tool_calls" (content may be empty) followed by a "tool" message whose content is exactly "placeholder": the pipeline replaces it with the real result. {tool_rules}
7. The tutor must react to what the learner actually wrote. The learner must behave like a real learner (short, sometimes wrong, sometimes vague).
8. Use a decimal POINT (2.5). Do not invent CAPS references, paper numbers or marks. No personal data. Do not use <think> tags.
9. meta.techniques: choose from {techniques}. Leave "verify_code" empty in faithful mode."""

FAITHFUL = ("HOW TO USE THE SOURCE ITEM (faithful mode): the learner's first message must present THIS question with the same "
            "numbers and meaning (phrase it like a learner would, or paste it). Teach THIS question. meta.final_answer must be YOUR "
            "final answer to it.")
ORIGINAL = ("HOW TO USE THE SOURCE ITEM (original mode): do NOT copy the question. Invent a NEW question of the same type, topic and "
            "difficulty with different numbers and context (an everyday South African context is welcome). Teach the NEW question. "
            "meta.final_answer is the final answer to YOUR new question. meta.verify_code is a short Python script (standard library "
            "or sympy only) that PRINTS only that final answer, e.g. print(6) or print('x = 2 or x = 3').")


def spec_sections(numbers):
    text = (KIT_ROOT / "tutor_spec.md").read_text(encoding="utf-8")
    parts = re.split(r"^(?=## \d+\.)", text, flags=re.M)
    keep = [s.strip() for s in parts if re.match(r"## (\d+)\.", s) and int(re.match(r"## (\d+)\.", s).group(1)) in numbers]
    if not keep:
        raise SystemExit("could not find the spec sections in tutor_spec.md")
    return "\n\n".join(keep)


def build_prompt(plan, item, spec_text):
    c, lr = plan["control"], plan["learner"]
    passage = f"passage: {item['passage']}\n" if item.get("passage") else ""
    tools = c.get("tools", [])
    tool_rules = []
    if "calculator" in tools:
        tool_rules.append("Use calculator for any arithmetic beyond easy sums.")
    if "board" in tools:
        tool_rules.append("Use board when drawing helps (always when strategy is visual_board): commands follow the blackboard grammar in the spec; "
                          "never write board commands in the reply text; after the tool message, refer to what is on the board.")
    if "plot_function" in tools:
        tool_rules.append("Use plot_function to show a graph.")
    if "search_curriculum" in tools:
        tool_rules.append("Use search_curriculum when a curriculum detail should be looked up instead of guessed.")
    thinking_on = plan["thinking"] == "on"
    return TEMPLATE.format(
        spec=spec_text, control=json.dumps(c, ensure_ascii=False), thinking=plan["thinking"], mode=plan["mode"],
        subject=item["subject"], grade=item["grade"], topic=item.get("topic") or "(see question)", passage=passage,
        question=item["question"], memo=item.get("memo") or "(none)", final=item.get("final_answer") or "(none)",
        lang=LANG_DESC.get(lr["student_language"], "English"), state=lr["state"], style=STYLE_DESC[lr["style"]],
        mis=(f"{lr['misconception']['misconception']} (correct idea: {lr['misconception']['correct_idea']})" if lr.get("misconception") else "none"),
        turns=lr["turns"], mode_rules=FAITHFUL if plan["mode"] == "faithful" else ORIGINAL,
        reasoning_hint='"reasoning": "...", ' if thinking_on else "",
        reasoning_rule=('thinking is ON: EVERY assistant message (also ones that only make a tool call) has a "reasoning" string in English, '
                        "about 60-150 words, following spec section 7: solve and verify, diagnose, choose the strategy, plan the reply."
                        if thinking_on else 'thinking is OFF: no assistant message may have a "reasoning" key.'),
        tool_rules=" ".join(tool_rules), techniques=", ".join(sorted(td.TECHNIQUES)))


def normalize_messages(msgs, thinking):
    out = []
    for m in msgs if isinstance(msgs, list) else []:
        if not isinstance(m, dict) or m.get("role") not in ("user", "assistant", "tool"):
            continue
        n = {"role": m["role"]}
        c = m.get("content", "")
        n["content"] = c if isinstance(c, (str, list)) else ("" if c is None else str(c))
        if isinstance(n["content"], str):
            n["content"] = re.sub(r"</?think>", "", n["content"]).strip()
        if m["role"] == "assistant":
            if thinking == "on" and isinstance(m.get("reasoning"), str):
                n["reasoning"] = re.sub(r"</?think>", "", m["reasoning"]).strip()
            tcs = m.get("tool_calls")
            if isinstance(tcs, list) and tcs:
                fixed = []
                for k, tc in enumerate(tcs, 1):
                    fn = (tc or {}).get("function") or {}
                    fixed.append({"id": tc.get("id") or f"call_{len(out)}_{k}", "type": "function",
                                  "function": {"name": fn.get("name"), "arguments": fn.get("arguments", {})}})
                n["tool_calls"] = fixed
        if m["role"] == "tool":
            for k in ("name", "tool_call_id"):
                if m.get(k):
                    n[k] = m[k]
            n["content"] = n["content"] or "placeholder"
        out.append(n)
    return out


def task_type_for(plan, item):
    c, lr = plan["control"], plan["learner"]
    if lr["state"] == "asking_for_answer":
        return "do_my_work"
    if c["strategy"] == "exam_technique":
        return "exam_technique"
    if lr["style"] == "with_attempt":
        return "check_my_work"
    if item["kind"] == "passage_questions":
        return "comprehension"
    if c["subject"] in td.LANGUAGE_SUBJECTS:
        return "language_help"
    return "solve_problem" if item.get("final_answer") or c["subject"] in td.CHECKABLE else "explain_concept"


def assemble(plan, item, obj, model, index):
    tmeta = obj.get("meta") if isinstance(obj.get("meta"), dict) else {}
    c = plan["control"]
    msgs = normalize_messages(obj.get("messages"), plan["thinking"])
    used = c["strategy"] if c["strategy"] != "auto" else str(tmeta.get("strategy_used", "")).strip()
    faithful = plan["mode"] == "faithful"
    techniques = [t for t in (tmeta.get("techniques") or []) if isinstance(t, str) and t in td.TECHNIQUES]
    meta = {
        "topic": (item.get("topic") or str(tmeta.get("topic") or "")).strip() or "unknown",
        "task_type": task_type_for(plan, item), "student_language": plan["learner"]["student_language"],
        "student_state": plan["learner"]["state"], "strategy_used": used,
        "source_type": "synthetic_from_source" if not faithful else ("past_paper_adapted" if item.get("pair_source_id") else "textbook_adapted"),
        "source_ref": f"{item['source_id']} {item.get('question_ref', '')}".strip(), "source_licence": item.get("licence") or "unknown",
        "attribution": item.get("attribution", ""), "generator": model, "answer_verified": False, "verification_method": "none",
        # unverified maths/science stays out of training ("exclude") until verify.py proves the answer and sets "auto"
        "split": "exclude" if c["subject"] in td.CHECKABLE else "auto",
        "created": time.strftime("%Y-%m-%d"), "item_id": item["item_id"], "mode": plan["mode"],
        "final_answer": (item.get("final_answer") if faithful else str(tmeta.get("final_answer", "")).strip()),
    }
    if faithful:
        meta["teacher_final_answer"] = str(tmeta.get("final_answer", "")).strip()
    else:
        meta["verify_code"] = str(tmeta.get("verify_code", "")).strip()
    if not meta["final_answer"]:
        meta.pop("final_answer")
    if techniques:
        meta["techniques"] = techniques
    if plan["learner"].get("misconception"):
        meta["misconception_targeted"] = plan["learner"]["misconception"]["misconception"]
    rec = {"schema_version": td.SCHEMA_VERSION, "id": plan["plan_id"], "group_id": plan["group_id"], "control": plan["control"],
           "thinking": plan["thinking"], "messages": msgs, "meta": meta}
    rec, unverified = tools_sim.fill_tool_results(rec, index)
    if unverified:
        rec["meta"]["tool_results_unverified"] = unverified
    return rec


def errors_of(rec):
    iss = td.Issues()
    td.check_record(rec, iss)
    return [m for lv, m in iss.items if lv == "ERROR"]


def work(plan, item, client, spec_text, index, temperature, retries, round_dir):
    prompt = build_prompt(plan, item, spec_text)
    messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}]
    last_errors, last_text = [], ""
    for attempt in range(retries + 1):
        res = client.chat(messages, temperature=temperature, max_tokens=6000, tag=f"gen:{plan['plan_id']}")
        last_text = res["text"]
        with LOCK:
            append_jsonl(round_dir / "raw_outputs.jsonl", {"plan_id": plan["plan_id"], "attempt": attempt, "reply": last_text,
                                                           "cost": round(res["cost"], 6)})
        try:
            obj = extract_json(last_text)
            rec = assemble(plan, item, obj, client.model, index)
            last_errors = errors_of(rec)
        except (ValueError, KeyError, TypeError) as e:
            rec, last_errors = None, [f"could not read your reply as the JSON object ({e})"]
        if rec is not None and not last_errors:
            return rec, []
        messages = messages[:2] + [{"role": "assistant", "content": last_text},
                                   {"role": "user", "content": "Your record had these problems:\n- " + "\n- ".join(last_errors[:8]) +
                                    "\nReturn the corrected JSON object only."}]
    return None, last_errors


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--round", required=True)
    ap.add_argument("--plan", help="default: workspace/plans/<round>.jsonl")
    ap.add_argument("--limit", type=int, default=0, help="only the next N undone plan rows")
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--temperature", type=float, default=0.8)
    ap.add_argument("--retries", type=int, default=2, help="extra tries per row when the record is invalid")
    ap.add_argument("--dry-run", action="store_true", help="print one prompt and the projected cost; call nothing")
    a = ap.parse_args()

    plans = read_jsonl(a.plan or p("plans", f"{a.round}.jsonl"))
    items = {}
    for f in p("items").glob("*.jsonl"):
        for it in read_jsonl(f):
            items[it["item_id"]] = it
    round_dir = p("gen", a.round)
    round_dir.mkdir(parents=True, exist_ok=True)
    done = set()
    for name in ("candidates.jsonl", "failed.jsonl"):
        fp = round_dir / name
        if fp.exists():
            done |= {r.get("id") or r.get("plan_id") for r in read_jsonl(fp)}
    todo = [pl for pl in plans if pl["plan_id"] not in done and pl["item_id"] in items]
    if a.limit:
        todo = todo[: a.limit]
    spec_text = spec_sections({2, 3, 4, 5, 7})
    index = retrieval.load_index(p("index", "bm25.json")) if p("index", "bm25.json").exists() else None
    client = Client("TEACHER")

    if a.dry_run:
        pl = todo[0] if todo else plans[0]
        prompt = build_prompt(pl, items[pl["item_id"]], spec_text)
        toks = len(prompt) / 3.5
        out_toks = 1400
        per = toks * client.price_in / 1e6 + out_toks * client.price_out / 1e6
        print(prompt, "\n" + "=" * 80)
        print(f"prompt ~{toks:,.0f} tokens (the spec part is identical every time, so providers with caching charge much less).")
        print(f"estimated cost per record: ${per:.4f}  ->  {len(todo)} rows to do = ${per * len(todo):.2f} (+ retries)")
        return

    print(f"{len(todo)} rows to do ({len(done)} already done). model={client.model}")
    ok = bad = 0
    t0 = time.time()
    stop = False
    with ThreadPoolExecutor(max_workers=max(1, a.workers)) as ex:
        futs = {ex.submit(work, pl, items[pl["item_id"]], client, spec_text, index, a.temperature, a.retries, round_dir): pl for pl in todo}
        for fut in as_completed(futs):
            pl = futs[fut]
            try:
                rec, errs = fut.result()
            except BudgetExceeded as e:
                print("STOPPED:", e)
                stop = True
                for f in futs:
                    f.cancel()
                break
            except Exception as e:                                       # noqa: BLE001
                rec, errs = None, [f"crashed: {type(e).__name__}: {e}"]
            with LOCK:
                if rec is not None:
                    append_jsonl(round_dir / "candidates.jsonl", rec)
                    ok += 1
                else:
                    append_jsonl(round_dir / "failed.jsonl", {"plan_id": pl["plan_id"], "errors": errs})
                    bad += 1
            if (ok + bad) % 10 == 0:
                print(f"  {ok + bad}/{len(todo)} done  (ok {ok}, failed {bad})  {time.time() - t0:.0f}s")
    print(f"\nfinished: {ok} candidates, {bad} failed. Spend so far: run `python llm.py spend`.")
    if not stop:
        print("NEXT: READ some candidates (open workspace/gen/%s/candidates.jsonl) before verifying. Then: "
              "python pipeline/verify.py --round %s" % (a.round, a.round))


if __name__ == "__main__":
    main()
