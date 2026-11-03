#!/usr/bin/env python3
"""
verify.py - decide which teacher-written records are good enough to train on.

    python pipeline/verify.py --round r1                      # free checks only
    python pipeline/verify.py --round r1 --judge              # + a second model grades each record (costs a little)

THE LAYERS (a record must pass all of them)
  1. real tool results   tool messages are recomputed in code (calculator, plot, board, search)
  2. schema              tutor_data.py validation (structure, enums, thinking/reasoning, board syntax ...)
  3. correctness         maths/science only:
                           faithful: the teacher's final answer must match the MEMO (SymPy)
                           original: the teacher's verify_code is RUN and its output must match the answer
                         full_solution replies must actually state that answer
  4. leaks & language    hint_only/guided replies must not give the answer away; the reply must be in the
                         language the settings ask for (rough heuristic)
  5. judge (optional)    a model grades correctness/policy/pedagogy/language/fit/honesty 1-5 using the
                         spec's rubric; accept only if every score >= --judge-min and correctness == 5
  6. duplicates          near-identical records are dropped
  Then YOU read a random sample (pipeline/review_sample.py). Machines catch the obvious; people catch
  "technically correct but a bad way to teach".

SAFETY NOTE ABOUT verify_code
  The teacher's snippet is run on YOUR computer. We only allow a few imports (sympy, math, fractions...)
  and block file/network/system calls, with a time limit. Run this in Colab or a throw-away folder if you
  are cautious. Never run unreviewed code from a model with access to anything you care about.

OUTPUT   workspace/verified/<round>/accepted.jsonl, rejected.jsonl (with reasons), report.json
"""
import argparse
import json
import re
import subprocess
import sys
import threading
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import retrieval  # noqa: E402
import tools_sim  # noqa: E402
import tutor_data as td  # noqa: E402
from answers import answers_match, contains_final_answer  # noqa: E402
from llm import BudgetExceeded, Client  # noqa: E402
from wspaths import KIT_ROOT, p, read_jsonl, write_jsonl  # noqa: E402

ALLOWED_IMPORTS = {"sympy", "math", "fractions", "decimal", "itertools", "statistics", "cmath", "numbers"}
BLOCKED = re.compile(r"\b(open|exec|eval|compile|__import__|input|globals|locals|getattr|setattr|breakpoint)\s*\(|"
                     r"\b(os|sys|subprocess|socket|shutil|pathlib|requests|urllib|ctypes|pickle)\b", re.I)
LOCK = threading.Lock()


def run_snippet(code, timeout=10):
    """Run the teacher's verification snippet. Returns (last_stdout_line, error)."""
    if not code or not code.strip():
        return None, "verify_code is empty"
    for m in re.finditer(r"^\s*(?:from|import)\s+([A-Za-z_][\w]*)", code, flags=re.M):
        if m.group(1) not in ALLOWED_IMPORTS:
            return None, f"import of '{m.group(1)}' is not allowed"
    if BLOCKED.search(code):
        return None, "code uses a blocked name (file/network/system access)"
    try:
        r = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None, "verify_code timed out"
    if r.returncode != 0:
        return None, "verify_code crashed: " + (r.stderr.strip().splitlines() or ["?"])[-1][:120]
    lines = [ln for ln in r.stdout.strip().splitlines() if ln.strip()]
    return (lines[-1].strip(), None) if lines else (None, "verify_code printed nothing")


def spec_rubric():
    text = (KIT_ROOT / "tutor_spec.md").read_text(encoding="utf-8")
    m = re.search(r"^## 8\..*?(?=^## \d+\.)", text, flags=re.S | re.M)
    return m.group(0).strip() if m else ""


JUDGE_SYSTEM = ("You are a strict, fair examiner of AI tutoring conversations for South African school learners. "
                "Reply with one JSON object only.")
JUDGE_TEMPLATE = """{rubric}

The conversation below was written to follow these settings: {control}
{memo}
CONVERSATION (the tutor's "reasoning" is its PRIVATE notes; the learner never sees it):
{convo}

Score each dimension from 1 to 5 using the rubric. Check the maths and the facts yourself.
Return JSON: {{"correctness": 5, "policy": 5, "pedagogy": 4, "language": 5, "fit": 5, "honesty": 5, "notes": "one or two sentences"}}"""


def convo_text(rec):
    lines = []
    for m in rec["messages"]:
        if m["role"] == "user":
            lines.append("LEARNER: " + td.text_of(m["content"]) + (" [image attached]" if td.has_image(m["content"]) else ""))
        elif m["role"] == "assistant":
            if m.get("reasoning"):
                lines.append("TUTOR (private reasoning): " + m["reasoning"])
            if m.get("tool_calls"):
                lines.append("TUTOR tool call: " + json.dumps([tc["function"] for tc in m["tool_calls"]], ensure_ascii=False))
            if m.get("content"):
                lines.append("TUTOR: " + m["content"])
        else:
            lines.append("TOOL RESULT: " + str(m.get("content")))
    return "\n".join(lines)


def judge(client, rec, item, rubric):
    memo = ""
    if item and item.get("memo"):
        memo = f"Official memo for the source question: {item['memo']}\nFinal answer in the memo: {item.get('final_answer', '')}\n"
    prompt = JUDGE_TEMPLATE.format(rubric=rubric, control=json.dumps(rec["control"], ensure_ascii=False), memo=memo, convo=convo_text(rec))
    obj, _ = client.chat_json([{"role": "system", "content": JUDGE_SYSTEM}, {"role": "user", "content": prompt}],
                              temperature=0, max_tokens=500, tag=f"judge:{rec['id']}")
    keys = ["correctness", "policy", "pedagogy", "language", "fit", "honesty"]
    scores = {k: int(obj[k]) for k in keys}
    return scores, str(obj.get("notes", ""))[:300]


def verify_record(rec, items, index, a):
    """Returns (record_or_None, reasons). Reasons are short strings."""
    rec, unverified = tools_sim.fill_tool_results(rec, index)
    if unverified:
        rec["meta"]["tool_results_unverified"] = unverified
        if a.reject_unverified_tools:
            return None, [f"tool results not verifiable: {','.join(unverified)}"]
    iss = td.Issues()
    td.check_record(rec, iss)
    errs = [m for lv, m in iss.items if lv == "ERROR"]
    warns = [m for lv, m in iss.items if lv == "WARN"]
    if errs:
        return None, ["validation: " + e for e in errs[:4]]
    c, m = rec["control"], rec["meta"]
    reasons = []
    subj = c["subject"]
    replies = [x for x in rec["messages"] if x["role"] == "assistant" and x.get("content")]
    last = replies[-1]["content"] if replies else ""
    if subj in td.CHECKABLE:
        final = m.get("final_answer", "")
        if m.get("mode") == "faithful":
            item = items.get(m.get("item_id"))
            memo_ans = (item or {}).get("final_answer", "")
            if not memo_ans:
                reasons.append("no memo final answer to check against")
            elif not answers_match(m.get("teacher_final_answer", ""), memo_ans):
                reasons.append(f"teacher answer {m.get('teacher_final_answer', '')!r} != memo {memo_ans!r}")
            method = "sympy_vs_memo"
        else:
            out, err = run_snippet(m.get("verify_code", ""))
            if err:
                reasons.append(err)
            elif not answers_match(out, final):
                reasons.append(f"verify_code printed {out!r} but final_answer is {final!r}")
            method = "code_exec"
        if not reasons:
            if c["answer_policy"] == "full_solution" and final and not contains_final_answer(last, final):
                reasons.append("full_solution reply does not state the final answer")
            if rec["thinking"] == "on" and final and a.check_reasoning:
                reasoning_all = " ".join(x.get("reasoning", "") for x in rec["messages"] if x["role"] == "assistant")
                if not contains_final_answer(reasoning_all, final):
                    reasons.append("private reasoning never reaches the final answer")
        if not reasons:
            m["answer_verified"], m["verification_method"] = True, method
            m["split"] = "auto"                      # proven: it may now be used for training
    else:
        m["verification_method"] = "none"
    if any("possible answer leak" in w for w in warns) and a.reject_leaks:
        reasons.append("answer leaked under hint_only/guided")
    if any("reply looks" in w and "expected reply language" in w for w in warns) and a.reject_language:
        reasons.append("reply language does not match the settings")
    if any("last reply is" in w and "words" in w for w in warns) and a.reject_length:
        reasons.append("reply longer than response_length allows")
    return (None, reasons) if reasons else (rec, [])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--round", required=True)
    ap.add_argument("--in", dest="inp", help="default: workspace/gen/<round>/candidates.jsonl")
    ap.add_argument("--judge", action="store_true", help="grade every record with the judge model (costs money)")
    ap.add_argument("--judge-min", type=int, default=4)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--no-reject-leaks", dest="reject_leaks", action="store_false")
    ap.add_argument("--no-reject-language", dest="reject_language", action="store_false")
    ap.add_argument("--reject-length", action="store_true", help="also reject replies that exceed response_length")
    ap.add_argument("--no-check-reasoning", dest="check_reasoning", action="store_false")
    ap.add_argument("--reject-unverified-tools", action="store_true")
    a = ap.parse_args()

    cands = read_jsonl(a.inp or p("gen", a.round, "candidates.jsonl"))
    items = {}
    for f in p("items").glob("*.jsonl"):
        for it in read_jsonl(f):
            items[it["item_id"]] = it
    index = retrieval.load_index(p("index", "bm25.json")) if p("index", "bm25.json").exists() else None

    accepted, rejected = [], []
    for rec in cands:
        out, reasons = verify_record(rec, items, index, a)
        (accepted if out else rejected).append(out or {"id": rec.get("id"), "reasons": reasons, "record": rec})
    print(f"free checks: {len(accepted)} passed, {len(rejected)} rejected (of {len(cands)})")

    if a.judge and accepted:
        client, rubric = Client("JUDGE"), spec_rubric()
        print(f"judging {len(accepted)} records with {client.model} ...")
        keep = []

        def one(rec):
            try:
                scores, notes = judge(client, rec, items.get(rec["meta"].get("item_id")), rubric)
            except BudgetExceeded:
                raise
            except Exception as e:                                       # noqa: BLE001
                return rec, None, f"judge failed: {type(e).__name__}"
            return rec, scores, notes

        try:
            with ThreadPoolExecutor(max_workers=max(1, a.workers)) as ex:
                for rec, scores, notes in ex.map(one, accepted):
                    if scores is None:
                        rejected.append({"id": rec["id"], "reasons": [notes], "record": rec})
                        continue
                    rec["meta"]["judge_scores"], rec["meta"]["judge_notes"] = scores, notes
                    if min(scores.values()) >= a.judge_min and scores["correctness"] == 5:
                        keep.append(rec)
                    else:
                        low = ", ".join(f"{k}={v}" for k, v in scores.items() if v < a.judge_min or (k == "correctness" and v < 5))
                        rejected.append({"id": rec["id"], "reasons": [f"judge: {low}. {notes}"], "record": rec})
        except BudgetExceeded as e:
            print("STOPPED judging:", e)
            keep = []
        accepted = keep
        print(f"after judge: {len(accepted)} accepted")

    seen, final = set(), []
    for rec in accepted:
        first = next((td.text_of(x["content"]) for x in rec["messages"] if x["role"] == "user"), "")
        key = (re.sub(r"\W+", " ", first.lower()).strip(), rec["meta"].get("final_answer", ""), rec["control"]["strategy"])
        if key in seen:
            rejected.append({"id": rec["id"], "reasons": ["near-duplicate"], "record": rec})
            continue
        seen.add(key)
        final.append(rec)

    out_dir = p("verified", a.round)
    write_jsonl(out_dir / "accepted.jsonl", final)
    write_jsonl(out_dir / "rejected.jsonl", rejected)
    reasons = Counter(r["reasons"][0].split(":")[0] if r["reasons"][0].startswith(("validation", "judge")) else r["reasons"][0][:50]
                      for r in rejected)
    unverified_lang = sum(1 for r in final if r["control"]["subject"] in td.LANGUAGE_SUBJECTS and not r["meta"].get("judge_scores"))
    report = {"candidates": len(cands), "accepted": len(final), "rejected": len(rejected),
              "accept_rate": round(len(final) / max(1, len(cands)), 3), "top_reasons": reasons.most_common(12),
              "accepted_by_subject": dict(Counter(r["control"]["subject"] for r in final))}
    (out_dir / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"\nACCEPTED {len(final)} / {len(cands)}  ({100 * report['accept_rate']:.0f}%)  -> {out_dir / 'accepted.jsonl'}")
    for reason, n in reasons.most_common(8):
        print(f"  rejected x{n}: {reason}")
    if unverified_lang:
        print(f"\nNOTE: {unverified_lang} language-subject records have no machine check beyond the schema. "
              f"Use --judge and READ a sample (pipeline/review_sample.py).")
    print("NEXT: python pipeline/review_sample.py export --round", a.round)


if __name__ == "__main__":
    main()
