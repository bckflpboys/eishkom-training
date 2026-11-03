#!/usr/bin/env python3
"""
review_sample.py - let a HUMAN check a random sample of the verified records.

    python pipeline/review_sample.py export --round r1 --n 40            # makes a readable file + a CSV
    (open review/r1_sample.md, read, then fill the 'verdict' column in review/r1_sample.csv)
    python pipeline/review_sample.py apply  --round r1                   # applies your verdicts

WHY
  Machines check answers and formats. They cannot tell you "this explanation is confusing", "this
  Afrikaans sounds like a translation", or "a real Grade 8 would never write that". A sample of 40-100
  records, read by you / a maths teacher / an Afrikaans speaker, is the cheapest quality control there is.
  The share of bad records in the sample tells you whether to trust the rest, or to fix the teacher
  prompt and regenerate.

VERDICTS (type one in the 'verdict' column)
  ok       good record
  af_ok    good, and the Afrikaans was checked by someone who speaks it  (sets language_reviewed_by_speaker)
  bad      remove it (explain in 'notes' so you can fix the prompt)
  af_bad   remove it: the Afrikaans is wrong or unnatural
  (blank)  skipped
"""
import argparse
import csv
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tutor_data as td  # noqa: E402
from wspaths import p, read_jsonl, write_jsonl  # noqa: E402


def one_liner(rec):
    c = rec["control"]
    return (f"{c['subject']} Gr{c['grade']} | reply:{c['response_language']} | {c['strategy']} | policy:{c['answer_policy']} | "
            f"level:{c['student_level']} | thinking:{rec['thinking']} | tools:{','.join(c['tools']) or '-'}")


def to_markdown(rec):
    out = [f"## {rec['id']}", f"`{one_liner(rec)}`", ""]
    if rec["meta"].get("source_ref"):
        out.append(f"source: {rec['meta']['source_ref']}   mode: {rec['meta'].get('mode')}   final answer: {rec['meta'].get('final_answer', '-')}")
        out.append("")
    for m in rec["messages"]:
        if m["role"] == "user":
            out.append("**Learner:** " + td.text_of(m["content"]) + (" *(image)*" if td.has_image(m["content"]) else ""))
        elif m["role"] == "assistant":
            if m.get("reasoning"):
                out.append("> *private reasoning:* " + m["reasoning"])
            if m.get("tool_calls"):
                out.append("*tool call:* `" + json.dumps([tc["function"] for tc in m["tool_calls"]], ensure_ascii=False) + "`")
            if m.get("content"):
                out.append("**Tutor:** " + m["content"])
        else:
            out.append("*tool result:* `" + str(m["content"]) + "`")
        out.append("")
    out.append("---\n")
    return "\n".join(out)


def cmd_export(a):
    recs = read_jsonl(p("verified", a.round, "accepted.jsonl"))
    if a.subject:
        recs = [r for r in recs if r["control"]["subject"] == a.subject]
    if a.lang:
        recs = [r for r in recs if r["control"]["response_language"] == a.lang or r["meta"]["student_language"] == a.lang]
    recs = [r for r in recs if not r["meta"].get("human_reviewed")]
    rng = random.Random(a.seed)
    cells = defaultdict(list)
    for r in recs:
        cells[(r["control"]["subject"], r["control"]["response_language"])].append(r)
    for v in cells.values():
        rng.shuffle(v)
    sample, keys = [], sorted(cells)
    while len(sample) < min(a.n, len(recs)):
        for k in keys:
            if cells[k] and len(sample) < a.n:
                sample.append(cells[k].pop())
    base = p("review", f"{a.round}_sample")
    base.parent.mkdir(parents=True, exist_ok=True)
    Path(f"{base}.md").write_text("\n".join(to_markdown(r) for r in sample), encoding="utf-8")
    with open(f"{base}.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "summary", "verdict", "notes"])
        for r in sample:
            w.writerow([r["id"], one_liner(r), "", ""])
    print(f"exported {len(sample)} records:\n  read   {base}.md\n  fill   {base}.csv  (verdict: ok / af_ok / bad / af_bad)")


def cmd_apply(a):
    csv_path = a.csv or f"{p('review', a.round + '_sample')}.csv"
    verdicts = {}
    with open(csv_path, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            v = (row.get("verdict") or "").strip().lower()
            if v:
                verdicts[row["id"]] = (v, (row.get("notes") or "").strip())
    acc_path, rej_path = p("verified", a.round, "accepted.jsonl"), p("verified", a.round, "rejected.jsonl")
    accepted = read_jsonl(acc_path)
    rejected = read_jsonl(rej_path) if rej_path.exists() else []
    keep, counts = [], Counter()
    for r in accepted:
        v = verdicts.get(r["id"])
        if not v:
            keep.append(r)
            continue
        verdict, notes = v
        counts[verdict] += 1
        if verdict in ("ok", "af_ok"):
            r["meta"]["human_reviewed"] = True
            if verdict == "af_ok":
                r["meta"]["language_reviewed_by_speaker"] = True
            if notes:
                r["meta"]["review_notes"] = notes
            keep.append(r)
        elif verdict in ("bad", "af_bad"):
            rejected.append({"id": r["id"], "reasons": [f"human: {verdict} {notes}".strip()], "record": r})
        else:
            print(f"  unknown verdict {verdict!r} for {r['id']} (kept, not marked)")
            keep.append(r)
    write_jsonl(acc_path, keep)
    write_jsonl(rej_path, rejected)
    total = sum(counts.values())
    bad = counts["bad"] + counts["af_bad"]
    print(f"applied {total} verdicts: {dict(counts)}; accepted now {len(keep)}")
    if total:
        print(f"BAD RATE in your sample: {100 * bad / total:.0f}%")
        if bad / total > 0.10:
            print("  -> above 10%: do NOT trust the unreviewed rest. Read your notes, fix the teacher prompt/spec, regenerate.")
        else:
            print("  -> low enough to go on, but keep sampling every round.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("export")
    e.add_argument("--round", required=True)
    e.add_argument("--n", type=int, default=40)
    e.add_argument("--seed", type=int, default=1)
    e.add_argument("--subject")
    e.add_argument("--lang", help="only records with this reply/student language (e.g. af, for the Afrikaans speaker)")
    e.set_defaults(fn=cmd_export)
    x = sub.add_parser("apply")
    x.add_argument("--round", required=True)
    x.add_argument("--csv")
    x.set_defaults(fn=cmd_apply)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
