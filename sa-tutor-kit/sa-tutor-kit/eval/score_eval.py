#!/usr/bin/env python3
"""
score_eval.py - mark the model's answers.

    python eval/score_eval.py --name r1-sft                 # free automatic checks
    python eval/score_eval.py --name r1-sft --judge         # + a judge model marks the "rubric" checks (costs a little)

CHECK TYPES (in each eval item's "checks")
  final_answer   {"expected": "x=2 or x=3"}      the reply states this answer (SymPy compares, "x = 3" == "3,0")
  no_leak        {"answers": ["x = 2"]}          the reply must NOT give these away (hint_only / guided tests)
  language       {"expected": "af"}              the reply is in this language (or a list of acceptable ones)
  asks_question  {}                              a guided reply ends with a question
  tool_call      {"name": "board"}               the model called this tool (optionally "args_contains": {...})
  no_tool_call   {}                              the model did NOT call a tool (easy sums need no calculator)
  contains_any / contains_all / not_contains     {"words": [...]}  simple keyword checks
  rubric         {"text": "..."}                 a judge model decides (needs --judge; skipped otherwise)
  ... plus checks applied to EVERY reply: no <think> tags leaked, balanced LaTeX, within response_length,
  non-empty, no raw JSON/tool syntax in the text.

WHY AUTOMATIC CHECKS FIRST
  They are free, instant, and consistent: you can run them after every training round and compare.
  They are blunt (a correct answer in an odd form can fail), so READ failures.md before believing a number.

OUTPUT   workspace/eval_runs/<name>/scores.jsonl, summary.json, failures.md
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tutor_data as td  # noqa: E402
from answers import contains_final_answer  # noqa: E402
from llm import Client  # noqa: E402
from wspaths import p, read_jsonl, write_jsonl  # noqa: E402


def _norm(s):
    return re.sub(r"\s+", " ", str(s).lower().replace("\u2019", "'")).strip()


def judge_rubric(client, item, text, rubric):
    user = "\n".join(m["content"] if isinstance(m["content"], str) else td.text_of(m["content"]) for m in item["messages"] if m["role"] == "user")
    prompt = (f"RUBRIC: {rubric}\n\nLEARNER (grade {item['control']['grade']}, {item['control']['subject']}) wrote:\n{user}\n\n"
              f"TUTOR REPLY:\n{text}\n\nDoes the reply satisfy the rubric? Score 1-5 (5 = fully, 1 = not at all). "
              'Return JSON: {"score": 5, "notes": "one sentence"}')
    obj, _ = client.chat_json([{"role": "system", "content": "You are a strict, fair examiner of AI tutoring replies. Reply with one JSON object only."},
                               {"role": "user", "content": prompt}], temperature=0, max_tokens=200, tag="eval:judge")
    return int(obj["score"]), str(obj.get("notes", ""))[:200]


def run_checks(item, out, judge_client):
    text = out.get("text", "") or ""
    c = item["control"]
    res = []

    def add(kind, ok, detail=""):
        res.append({"type": kind, "passed": bool(ok), "detail": detail})

    # --- applied to every reply
    add("auto:non_empty", text.strip() != "", "empty reply" if not text.strip() else "")
    add("auto:no_think_leak", "<think>" not in text and "</think>" not in text)
    add("auto:no_raw_tool_syntax", "<tool_call>" not in text and '"tool_calls"' not in text and not text.lstrip().startswith('{"'))
    cap = td.LENGTH_WORDS.get(c.get("response_length"))
    if cap:
        n = td.words(text)
        add("auto:length", n <= cap * 1.15, f"{n} words, limit {cap}")          # 15% slack: counting words is approximate
    if c.get("math_format") == "latex":
        add("auto:latex_balanced", text.count("$") % 2 == 0, "unbalanced $")
    # --- item checks
    for ch in item.get("checks", []):
        t = ch["type"]
        if t == "final_answer":
            ok = contains_final_answer(text, ch["expected"])
            add(t, ok, f"expected {ch['expected']!r}")
        elif t == "no_leak":
            answers = ch.get("answers") or [ch.get("answer")]
            leaked = [a for a in answers if a and (contains_final_answer(text, a) or (len(re.sub(r'\W', '', a)) >= 4 and _norm(re.sub(r'\W', '', a)) in _norm(re.sub(r'\W', '', text))))]
            add(t, not leaked, f"leaked: {leaked}" if leaked else "")
        elif t == "language":
            exp = ch["expected"] if isinstance(ch["expected"], list) else [ch["expected"]]
            g = td.guess_lang(text)
            add(t, g in exp or g == "unknown", f"looks {g}, expected {exp}")
        elif t == "asks_question":
            add(t, "?" in text[-250:], "no question near the end")
        elif t == "tool_call":
            calls = [x for x in out.get("tool_calls", []) if x["name"] == ch["name"]]
            ok = bool(calls)
            for k, v in (ch.get("args_contains") or {}).items():
                ok = ok and any(_norm(v) in _norm(json.dumps(x["arguments"])) for x in calls)
            add(t, ok, f"called: {[x['name'] for x in out.get('tool_calls', [])]}")
        elif t == "no_tool_call":
            add(t, not out.get("tool_calls"), f"called: {[x['name'] for x in out.get('tool_calls', [])]}")
        elif t == "contains_any":
            add(t, any(_norm(w) in _norm(text) for w in ch["words"]), f"none of {ch['words']}")
        elif t == "contains_all":
            missing = [w for w in ch["words"] if _norm(w) not in _norm(text)]
            add(t, not missing, f"missing {missing}")
        elif t == "not_contains":
            found = [w for w in ch["words"] if _norm(w) in _norm(text)]
            add(t, not found, f"found {found}")
        elif t == "rubric":
            if judge_client is None:
                res.append({"type": t, "passed": None, "detail": "skipped (no --judge)"})
            else:
                try:
                    score, notes = judge_rubric(judge_client, item, text, ch["text"])
                    add(t, score >= 4, f"judge {score}/5: {notes}")
                except Exception as e:                                           # noqa: BLE001
                    res.append({"type": t, "passed": None, "detail": f"judge failed: {type(e).__name__}"})
        else:
            add(t, False, "unknown check type")
    return res


def rate(rows):
    return round(sum(rows) / len(rows), 4) if rows else None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", required=True)
    ap.add_argument("--items", default=str(p("eval", "eval_items.jsonl")))
    ap.add_argument("--judge", action="store_true")
    a = ap.parse_args()

    items = {i["id"]: i for i in read_jsonl(a.items)}
    outs = read_jsonl(p("eval_runs", a.name, "outputs.jsonl"))
    judge_client = Client("JUDGE") if a.judge else None
    rows = []
    for o in outs:
        item = items.get(o["id"])
        if not item:
            continue
        checks = run_checks(item, o, judge_client)
        graded = [c for c in checks if c["passed"] is not None]
        rows.append({"id": o["id"], "sample": o["sample"], "passed": all(c["passed"] for c in graded), "checks": checks,
                     "tokens": o.get("tokens", 0), "latency_s": o.get("latency_s", 0), "words": td.words(o.get("text", "")),
                     "error": o.get("error")})
    out_dir = p("eval_runs", a.name)
    write_jsonl(out_dir / "scores.jsonl", rows)

    by_item = defaultdict(list)
    for r in rows:
        by_item[r["id"]].append(r["passed"])
    slices = defaultdict(lambda: defaultdict(list))
    for r in rows:
        it = items[r["id"]]
        c = it["control"]
        slices["subject"][c["subject"]].append(r["passed"])
        slices["grade"][f"Gr{c['grade']}"].append(r["passed"])
        lang_checks = [ch for ch in it.get("checks", []) if ch["type"] == "language"]
        lang = lang_checks[0]["expected"] if lang_checks else c["response_language"]
        slices["language"]["/".join(lang) if isinstance(lang, list) else lang].append(r["passed"])
        for tag in it.get("tags", []):
            slices["tag"][tag].append(r["passed"])
        slices["task_type"][it.get("task_type", "?")].append(r["passed"])
    by_check = defaultdict(list)
    for r in rows:
        for ch in r["checks"]:
            if ch["passed"] is not None:
                by_check[ch["type"]].append(ch["passed"])
    summary = {
        "run": a.name, "items": len(by_item), "samples": len(rows),
        "overall_sample_pass": rate([r["passed"] for r in rows]),
        "items_all_samples_pass": rate([all(v) for v in by_item.values()]),
        "items_any_sample_pass": rate([any(v) for v in by_item.values()]),
        "avg_tokens": round(sum(r["tokens"] for r in rows) / max(1, len(rows)), 1),
        "avg_latency_s": round(sum(r["latency_s"] for r in rows) / max(1, len(rows)), 2),
        "avg_words": round(sum(r["words"] for r in rows) / max(1, len(rows)), 1),
        "errors": sum(1 for r in rows if r["error"]),
        "slices": {k: {name: {"pass": rate(v), "n": len(v)} for name, v in sorted(d.items())} for k, d in slices.items()},
        "checks": {k: {"pass": rate(v), "n": len(v)} for k, v in sorted(by_check.items())},
        "failed_items": sorted({r["id"] for r in rows if not r["passed"]}),
    }
    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    lines = [f"# Failures for {a.name}\n"]
    out_by_key = {(o["id"], o["sample"]): o for o in outs}
    for r in rows:
        if r["passed"]:
            continue
        o = out_by_key[(r["id"], r["sample"])]
        bad = [c for c in r["checks"] if c["passed"] is False]
        lines.append(f"## {r['id']} (sample {r['sample']})\nfailed: " + "; ".join(f"**{c['type']}** {c['detail']}" for c in bad))
        lines.append("\nreply:\n> " + (o.get("text", "")[:900].replace("\n", "\n> ") or "(empty)") + "\n")
        if o.get("tool_calls"):
            lines.append("tool calls: `" + json.dumps(o["tool_calls"], ensure_ascii=False)[:400] + "`\n")
    (out_dir / "failures.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"\n{a.name}: {summary['overall_sample_pass']:.0%} of {len(rows)} answers pass all checks "
          f"({summary['items_all_samples_pass']:.0%} of items right every time, {summary['items_any_sample_pass']:.0%} right at least once)")
    for kind in ("tag", "subject", "grade", "language"):
        print(f"\nby {kind}:")
        for name, d in summary["slices"].get(kind, {}).items():
            print(f"  {name:<22} {d['pass']:.0%}  (n={d['n']})")
    print("\nby check type:")
    for name, d in summary["checks"].items():
        print(f"  {name:<24} {d['pass']:.0%}  (n={d['n']})")
    print(f"\nREAD {out_dir / 'failures.md'} before trusting these numbers.")


if __name__ == "__main__":
    main()
