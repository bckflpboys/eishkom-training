#!/usr/bin/env python3
"""
extract_items.py - cut questions and memo answers out of the extracted text, using the teacher model.

    python pipeline/extract_items.py --source dbe-maths-g12-p1-2024-nov            # paper + memo
    python pipeline/extract_items.py --source siyavula-maths-g10-unbranded --kind textbook
    add --dry-run first to see the size and estimated cost without spending anything

WHY THE TEACHER DOES THIS
  PDF text is messy: the question paper and the memo are separate files, question numbers are buried
  in the text, maths is garbled. A big model is good at "find question 2.1.3 and the matching memo
  answer". We still do not trust it blindly:
    - it must copy the question faithfully (we will compare numbers later),
    - items with no clear final answer are flagged needs_review,
    - YOU read a sample of the items before anything else is built on them (GUIDE.md phase 2).

OUTPUT   workspace/items/<source_id>.jsonl   one item per line:
  item_id, source_id, subject, grade, language, track, kind, question_ref, marks, topic,
  passage, question, memo, final_answer, needs_review, licence, attribution
"""
import argparse
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tutor_data as td  # noqa: E402
from llm import BudgetExceeded, Client  # noqa: E402
from wspaths import p, write_jsonl  # noqa: E402

SYSTEM = ("You convert South African school exam papers, marking guidelines (memoranda) and textbook pages into "
          "clean structured data. Be FAITHFUL: copy question wording and numbers exactly, never invent numbers or "
          "answers. Write maths in LaTeX inside $...$. Reply with one JSON object only.")

PAPER_LIST = """Here is a question paper. List its top-level question numbers.

QUESTION PAPER TEXT:
<<<
{paper}
>>>

Return JSON: {{"questions": ["1", "2", "3"]}}"""

PAPER_ITEMS = """QUESTION PAPER TEXT:
<<<
{paper}
>>>

MEMORANDUM (marking guideline) TEXT:
<<<
{memo}
>>>

Task: extract every sub-question of QUESTION {n} (for example {n}.1, {n}.1.1, {n}.2) and match each with its memo answer.
Return JSON:
{{"items": [{{
  "question_ref": "{n}.1.1",
  "marks": 3,
  "topic": "short topic name, e.g. quadratic equations",
  "passage": "text the question depends on (a reading passage, a table, a diagram described in words), or empty",
  "question": "the question text, copied faithfully, maths in LaTeX",
  "memo": "the memo's working and answer, copied faithfully (steps, method marks)",
  "final_answer": "the short final answer(s), e.g. x = 2 or x = 3. Use a decimal POINT. Empty if the memo has none",
  "needs_review": false
}}]}}
Rules:
- If a part has no clear memo answer, set final_answer to "" and needs_review to true.
- If the question or memo text is garbled and you are not sure, set needs_review to true. Do not guess.
- Skip parts that need a diagram you cannot describe from the text.
- Include only parts that belong to question {n}."""

BOOK_ITEMS = """TEXTBOOK TEXT (pages {a}-{b}):
<<<
{text}
>>>

Task: extract (1) WORKED EXAMPLES (a question with a full worked solution) and (2) EXERCISE QUESTIONS whose answers
are given in this text. Return JSON:
{{"items": [{{
  "question_ref": "p{a}-ex1",
  "kind": "worked_example",
  "marks": 0,
  "topic": "short topic name",
  "passage": "",
  "question": "the question, copied faithfully, maths in LaTeX",
  "memo": "the full worked solution or the given answer, copied faithfully",
  "final_answer": "short final answer(s), decimal POINT; empty if none",
  "needs_review": false
}}]}}
Rules: copy faithfully, never invent. If unsure, needs_review = true. Skip anything that depends on a picture."""


def slug(s):
    return re.sub(r"[^A-Za-z0-9._-]+", "-", str(s)).strip("-").lower()


def pages_of(text):
    parts = re.split(r"^=== page (\d+) ===\s*$", text, flags=re.M)
    return [(int(parts[i]), parts[i + 1]) for i in range(1, len(parts), 2)] if len(parts) > 1 else [(1, text)]


def finish_item(raw, src, memo_id):
    item = {
        "item_id": f"{src['source_id']}-{slug(raw.get('question_ref', 'x'))}",
        "source_id": src["source_id"], "pair_source_id": memo_id,
        "subject": src["subject"], "grade": int(src["grade"]) if str(src.get("grade", "")).isdigit() else src.get("grade"),
        "language": src.get("language") or "en", "track": (src.get("track") or "").strip(),
        "kind": raw.get("kind") or ("passage_questions" if (raw.get("passage") or "").strip() else "question"),
        "question_ref": str(raw.get("question_ref", "")), "marks": raw.get("marks") or 0,
        "topic": str(raw.get("topic", "")).strip(), "passage": str(raw.get("passage", "") or "").strip(),
        "question": str(raw.get("question", "")).strip(), "memo": str(raw.get("memo", "")).strip(),
        "final_answer": str(raw.get("final_answer", "") or "").strip(),
        "needs_review": bool(raw.get("needs_review", False)),
        "licence": src.get("licence", ""), "attribution": src.get("attribution", ""),
    }
    problems = []
    if not item["question"]:
        problems.append("empty question")
    if not item["memo"] and item["kind"] != "question":
        problems.append("empty memo")
    if src["subject"] in td.CHECKABLE and not item["final_answer"]:
        item["needs_review"] = True
    return item, problems


def est_cost(client, text):
    toks = len(text) / 3.5
    return toks, toks * client.price_in / 1e6


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", required=True, help="source_id of the paper (or textbook) in sources.csv")
    ap.add_argument("--kind", choices=["paper", "textbook"], default="paper")
    ap.add_argument("--sources", default=str(p("sources", "sources.csv")))
    ap.add_argument("--max-questions", type=int, default=0, help="only the first N top-level questions (for a cheap test)")
    ap.add_argument("--pages-per-chunk", type=int, default=6, help="textbook mode: pages per call")
    ap.add_argument("--max-chunks", type=int, default=0, help="textbook mode: only the first N chunks")
    ap.add_argument("--dry-run", action="store_true", help="show sizes and estimated cost, call nothing")
    a = ap.parse_args()

    rows = {r["source_id"]: r for r in csv.DictReader(open(a.sources, encoding="utf-8-sig", newline=""))}
    if a.source not in rows:
        sys.exit(f"source_id {a.source!r} is not in {a.sources}")
    src = rows[a.source]
    client = Client("TEACHER")
    items, problems_total = [], 0

    try:
        if a.kind == "paper":
            memo_id = (src.get("pair_with") or "").strip()
            if not memo_id:
                sys.exit("this source has no pair_with (memo source_id) in sources.csv")
            paper = p("text", f"{a.source}.txt").read_text(encoding="utf-8")
            memo = p("text", f"{memo_id}.txt").read_text(encoding="utf-8")
            toks, cost = est_cost(client, paper + memo)
            print(f"paper+memo is about {toks:,.0f} tokens; each question call re-sends it (~${cost:.4f} per call before caching)")
            if a.dry_run:
                return
            lst, _ = client.chat_json([{"role": "system", "content": SYSTEM},
                                       {"role": "user", "content": PAPER_LIST.format(paper=paper)}], temperature=0, tag="extract:list")
            qs = [str(q) for q in lst.get("questions", [])]
            if a.max_questions:
                qs = qs[: a.max_questions]
            print("questions found:", qs)
            for n in qs:
                obj, _ = client.chat_json([{"role": "system", "content": SYSTEM},
                                           {"role": "user", "content": PAPER_ITEMS.format(paper=paper, memo=memo, n=n)}],
                                          temperature=0, max_tokens=8000, tag=f"extract:q{n}")
                got = 0
                for raw in obj.get("items", []):
                    item, probs = finish_item(raw, src, memo_id)
                    if probs:
                        problems_total += 1
                        print(f"  skipped {item['item_id']}: {', '.join(probs)}")
                        continue
                    items.append(item)
                    got += 1
                print(f"  question {n}: {got} items")
        else:
            text = p("text", f"{a.source}.txt").read_text(encoding="utf-8")
            pgs = pages_of(text)
            chunks = [pgs[i:i + a.pages_per_chunk] for i in range(0, len(pgs), a.pages_per_chunk)]
            if a.max_chunks:
                chunks = chunks[: a.max_chunks]
            toks, cost = est_cost(client, text)
            print(f"{len(pgs)} pages in {len(chunks)} chunks; whole text is about {toks:,.0f} tokens (~${cost:.4f} input)")
            if a.dry_run:
                return
            for ch in chunks:
                a1, b1 = ch[0][0], ch[-1][0]
                body = "\n".join(f"[page {n}]\n{t}" for n, t in ch)
                obj, _ = client.chat_json([{"role": "system", "content": SYSTEM},
                                           {"role": "user", "content": BOOK_ITEMS.format(a=a1, b=b1, text=body)}],
                                          temperature=0, max_tokens=8000, tag=f"extract:p{a1}")
                got = 0
                for raw in obj.get("items", []):
                    item, probs = finish_item(raw, src, "")
                    if probs:
                        problems_total += 1
                        continue
                    items.append(item)
                    got += 1
                print(f"  pages {a1}-{b1}: {got} items")
    except BudgetExceeded as e:
        print("STOPPED:", e)

    seen, uniq = set(), []
    for it in items:
        if it["item_id"] in seen:
            it["item_id"] += f"-{len(seen)}"
        seen.add(it["item_id"])
        uniq.append(it)
    out = p("items", f"{a.source}.jsonl")
    write_jsonl(out, uniq)
    review = sum(1 for i in uniq if i["needs_review"])
    print(f"\nwrote {len(uniq)} items to {out}  ({review} flagged needs_review, {problems_total} skipped)")
    print("NEXT: open the file and READ 20 random items against the PDF. Fix or delete bad ones by hand.")


if __name__ == "__main__":
    main()
