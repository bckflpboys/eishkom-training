#!/usr/bin/env python3
"""
make_variants.py - ask the same question in different ways (to test that the model understood, not memorised).

    python eval/make_variants.py --per-item 2 [--tags core] [--out workspace/eval/eval_items_variants.jsonl]
    then:  python eval/run_eval.py --items workspace/eval/eval_items_variants.jsonl ...

WHY
  A model can learn the exact wording of your 40 exam questions and still be useless on the 41st. Real
  learners write "pls help i dont get this", add typos, switch language, leave out the word "solve".
  This asks the teacher to REWORD each learner message (same maths, same numbers, same meaning) in
  different styles, and keeps the same checks. If the model passes the original but fails the reworded
  version, it is memorising wording. The score on variants is your ROBUSTNESS score.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tutor_data as td  # noqa: E402
from llm import Client  # noqa: E402
from wspaths import p, read_jsonl, write_jsonl  # noqa: E402

PROMPT = """Here is a message a South African school learner (Grade {grade}, {subject}) sent to an AI tutor:

\"\"\"{text}\"\"\"

Write {k} DIFFERENT versions of this message. Rules:
- Same question, same numbers, same meaning, same language as the original. Do not solve anything.
- Make each version sound like a real learner: one casual with a typo or two, one short and blunt, one polite and wordy (use {k} styles in total).
- Keep any maths exactly correct.
Return JSON: {{"variants": ["...", "..."]}} (a paraphrase of the original, {k} items)."""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--items", default=str(p("eval", "eval_items.jsonl")))
    ap.add_argument("--out", default=str(p("eval", "eval_items_variants.jsonl")))
    ap.add_argument("--per-item", type=int, default=2)
    ap.add_argument("--tags", nargs="*")
    a = ap.parse_args()
    items = read_jsonl(a.items)
    if a.tags:
        items = [i for i in items if set(i.get("tags", [])) & set(a.tags)]
    client, out = Client("TEACHER"), []
    for it in items:
        if len(it["messages"]) != 1 or not isinstance(it["messages"][0]["content"], str):
            continue                                                      # only simple single-message items
        text = it["messages"][0]["content"]
        try:
            obj, _ = client.chat_json([{"role": "user", "content": PROMPT.format(grade=it["control"]["grade"], subject=it["control"]["subject"],
                                                                                  text=text, k=a.per_item)}], temperature=0.8, max_tokens=600, tag="variants")
        except Exception as e:                                           # noqa: BLE001
            print(f"  {it['id']}: failed ({type(e).__name__})")
            continue
        for n, v in enumerate([v for v in obj.get("variants", []) if isinstance(v, str) and v.strip()][: a.per_item], 1):
            new = dict(it)
            new["id"] = f"{it['id']}~v{n}"
            new["tags"] = sorted(set(it.get("tags", [])) | {"variant"})
            new["variant_of"] = it["id"]
            new["messages"] = [{"role": "user", "content": v.strip()}]
            out.append(new)
    write_jsonl(a.out, out)
    print(f"wrote {len(out)} variant items to {a.out}.  READ a few: if a variant changed the maths, delete it.")


if __name__ == "__main__":
    main()
