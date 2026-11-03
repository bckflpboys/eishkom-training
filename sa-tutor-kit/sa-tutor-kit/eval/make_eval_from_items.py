#!/usr/bin/env python3
"""
make_eval_from_items.py - turn the questions you extracted from HELD-OUT past papers into exam items.

    python eval/make_eval_from_items.py --source dbe-maths-g12-p1-2024-nov            # appends to workspace/eval/eval_items.jsonl
    python eval/make_eval_from_items.py --source dbe-eng-g10-p1-2024 --max 30

WHY
  Your own 42 starter questions test behaviours (policy, language, tools). Real past-paper questions test whether the
  tutor is right on the REAL exam. Both are needed. Rules:
    * only use papers you will NEVER train on (put their source_id in plan_config.json -> holdout_sources)
    * maths/science items get a final_answer check (SymPy compares); language items get a rubric check judged
      by a model against the memo (needs score_eval.py --judge)
    * read 10 of the generated items against the paper before trusting them; fix or delete bad ones
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tutor_data as td  # noqa: E402
from wspaths import p, read_jsonl, write_jsonl  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", required=True)
    ap.add_argument("--out", default=str(p("eval", "eval_items.jsonl")))
    ap.add_argument("--max", type=int, default=0)
    ap.add_argument("--policy", default="full_solution", choices=["full_solution", "guided", "hint_only"])
    ap.add_argument("--keep-review", action="store_true", help="also use items flagged needs_review")
    a = ap.parse_args()

    items = [i for i in read_jsonl(p("items", f"{a.source}.jsonl")) if a.keep_review or not i.get("needs_review")]
    if a.max:
        items = items[: a.max]
    existing = read_jsonl(a.out) if Path(a.out).exists() else []
    have = {e["id"] for e in existing}
    new = []
    for it in items:
        if it["item_id"] in have:
            continue
        subj, grade = it["subject"], int(it["grade"])
        lang = it.get("language") or "en"
        control = {"subject": subj, "grade": grade, "subject_language": lang, "response_language": lang, "strategy": "auto",
                   "answer_policy": a.policy, "student_level": "on_track", "tone": "encouraging",
                   "response_length": "long" if (it.get("marks") or 0) >= 4 else "medium", "tools": ["calculator"] if subj in td.CHECKABLE else []}
        if subj in td.NEEDS_MATH_FORMAT:
            control["math_format"] = "latex"
        if subj in td.LANGUAGE_SUBJECTS:
            control["language_track"] = it.get("track") or ("HL" if subj == "english" else "FAL")
        text = (it["passage"] + "\n\n" if it.get("passage") else "") + it["question"]
        checks = []
        if it.get("final_answer") and subj in td.CHECKABLE:
            checks.append({"type": "final_answer", "expected": it["final_answer"]})
        else:
            checks.append({"type": "rubric", "text": "The reply answers the question correctly and covers the key points of the official memo: " + it["memo"][:600]})
        checks.append({"type": "language", "expected": lang})
        new.append({"id": it["item_id"], "tags": ["paper", subj, f"gr{grade}"], "task_type": "solve_problem" if subj in td.CHECKABLE else "comprehension",
                    "control": control, "thinking": "on" if subj in td.CHECKABLE else "off",
                    "messages": [{"role": "user", "content": text}], "checks": checks})
    write_jsonl(a.out, existing + new)
    print(f"added {len(new)} items from {a.source} ({len(existing) + len(new)} in the exam now) -> {a.out}")
    print("READ 10 of them against the paper. Never train on this source.")


if __name__ == "__main__":
    main()
