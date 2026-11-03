#!/usr/bin/env python3
"""
analyze_failures.py - ask the teacher model WHY your model fails, and what data would fix it.

    python eval/analyze_failures.py --name r1-sft [--max-cases 30]

WHY
  A pass rate tells you THAT it fails. Reading 40 failures tells you WHY, but that is slow. A big model reads
  them all, groups them ("sign errors in factorising", "answers in English when asked in Afrikaans", "gives
  the answer away when the learner begs"), guesses a root cause, and proposes new data to write. You still
  decide: it is a colleague's opinion, not an order.

OUTPUT  workspace/eval_runs/<name>/analysis.md  and  suggested_plan.json (rows you can paste into plan_config.json)
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tutor_data as td  # noqa: E402
from llm import Client  # noqa: E402
from wspaths import p, read_jsonl  # noqa: E402

PROMPT = """A small AI tutor model (for South African school learners, Grades 7-12) was tested on an exam of tutoring situations.
These are some of the tests it FAILED. For each: the learner's message, the model's reply, and which checks failed.

{cases}

Tasks:
1. Group the failures into categories (3-8). For each give: name, count, example_ids, root_cause (your best guess about WHY the model fails, e.g. missing training data, wrong policy habit, language drift), fix (concrete data to add: what situations, how many, which teaching strategy/answer policy/language).
2. Suggest rows for a data-generation plan: {{"subject","grade","topic","strategy","count"}}.
3. Add short notes: anything suspicious about the TESTS themselves (a check that may be wrong, an ambiguous question).
Return JSON: {{"categories": [{{"name": "...", "count": 0, "example_ids": [], "root_cause": "...", "fix": "..."}}], "suggested_plan_rows": [], "notes": "..."}}"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", required=True)
    ap.add_argument("--items", default=str(p("eval", "eval_items.jsonl")))
    ap.add_argument("--max-cases", type=int, default=30)
    a = ap.parse_args()

    items = {i["id"]: i for i in read_jsonl(a.items)}
    outs = {(o["id"], o["sample"]): o for o in read_jsonl(p("eval_runs", a.name, "outputs.jsonl"))}
    cases, seen = [], set()
    for r in read_jsonl(p("eval_runs", a.name, "scores.jsonl")):
        if r["passed"] or r["id"] in seen:
            continue
        seen.add(r["id"])
        it, o = items[r["id"]], outs[(r["id"], r["sample"])]
        cases.append({"id": r["id"], "subject": it["control"]["subject"], "grade": it["control"]["grade"],
                      "answer_policy": it["control"]["answer_policy"],
                      "learner": " ".join(td.text_of(m["content"]) for m in it["messages"] if m["role"] == "user")[:400],
                      "model_reply": (o.get("text") or "")[:600], "tool_calls": o.get("tool_calls", []),
                      "failed_checks": [f"{c['type']}: {c['detail']}" for c in r["checks"] if c["passed"] is False]})
    if not cases:
        print("No failures to analyse. (Either great news, or the exam is too easy: add harder items.)")
        return
    cases = cases[: a.max_cases]
    client = Client("TEACHER")
    obj, res = client.chat_json([{"role": "system", "content": "You are an expert in teaching and in training small language models. Reply with one JSON object only."},
                                 {"role": "user", "content": PROMPT.format(cases=json.dumps(cases, ensure_ascii=False, indent=1))}],
                                temperature=0.2, max_tokens=3000, tag="analyze")
    out_dir = p("eval_runs", a.name)
    (out_dir / "suggested_plan.json").write_text(json.dumps(obj.get("suggested_plan_rows", []), indent=2, ensure_ascii=False), encoding="utf-8")
    md = [f"# Failure analysis: {a.name}  ({len(cases)} failing items looked at; cost ${res['cost']:.4f})\n"]
    for c in obj.get("categories", []):
        md += [f"## {c.get('name')}  (x{c.get('count')})", f"examples: {', '.join(map(str, c.get('example_ids', [])))}",
               f"**why:** {c.get('root_cause')}", f"**fix:** {c.get('fix')}\n"]
    md += ["## Notes on the tests", str(obj.get("notes", ""))]
    (out_dir / "analysis.md").write_text("\n".join(md), encoding="utf-8")
    print("\n".join(md))
    print(f"\nwrote {out_dir / 'analysis.md'} and suggested_plan.json. YOU decide what to act on.")


if __name__ == "__main__":
    main()
