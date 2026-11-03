#!/usr/bin/env python3
"""
merge.py - combine the verified records of several rounds into ONE training file.

    python pipeline/merge.py --rounds r1 r2 --out workspace/verified/all_r2.jsonl

WHY
  Each training round starts again from the BASE model and trains on EVERYTHING so far (old + new data).
  If you trained round 2 on the new subject only, the model would forget round 1 ("catastrophic
  forgetting"). So the file you build and train from is always the merge of all rounds up to now.
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tutor_data as td  # noqa: E402
from wspaths import p, read_jsonl, write_jsonl  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--rounds", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    seen_ids, seen_keys, out, dropped = set(), set(), [], 0
    for r in a.rounds:
        for rec in read_jsonl(p("verified", r, "accepted.jsonl")):
            first = next((td.text_of(x["content"]) for x in rec["messages"] if x["role"] == "user"), "")
            key = (re.sub(r"\W+", " ", first.lower()).strip(), rec["meta"].get("final_answer", ""), rec["control"]["strategy"])
            if rec["id"] in seen_ids or key in seen_keys:
                dropped += 1
                continue
            seen_ids.add(rec["id"])
            seen_keys.add(key)
            out.append(rec)
    write_jsonl(a.out, out)
    print(f"merged {len(out)} records from {a.rounds} ({dropped} duplicates dropped) -> {a.out}")
    print(f"NEXT: python tutor_data.py report {a.out}   then   python tutor_data.py build {a.out} --out workspace/build/<name>")


if __name__ == "__main__":
    main()
