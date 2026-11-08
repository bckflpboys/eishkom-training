#!/usr/bin/env python3
"""
Eishkom AI - Extraction Queue Scanner.

Answers one question: for each subject lane, which paper should the next
agent extract?

It reads workspace/sources/sources.csv, inspects workspace/items/ for
existing JSONL output, validates the mark total against the printed exam
total, and prints the next actionable paper per lane.

Status vocabulary
-----------------
LOCKED_EVAL : 2024 paper, quarantined in workspace/eval/ - never extract
NO_TEXT     : no workspace/text/<id>.txt - run PDF extraction first
TODO        : text ready, nothing extracted yet
DONE_OK     : extracted and mark total matches the printed total
DONE_BAD    : extracted but mark total does not match (needs repair)
BLOCKED     : text ready but the paired memo text is missing
"""

import csv
import json
import re
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
SOURCES_CSV = WORKSPACE / "sources" / "sources.csv"
ITEMS_DIR = WORKSPACE / "items"
TEXT_DIR = WORKSPACE / "text"

# Lane -> (display name, subject-id prefixes)
LANES = {
    "mathematics": ("Mathematics", ("dbe-mathematics-", "dbe-wiskunde-", "dbe-maths-")),
    "physical_sciences": ("Physical Sciences", ("dbe-physical_sciences-", "dbe-fisiese_wetenskappe-")),
    "english": ("English", ("dbe-english_hl-", "dbe-english_fal-")),
    "afrikaans": ("Afrikaans", ("dbe-afrikaans_hl-", "dbe-afrikaans_fal-")),
}

# The `subject` column is the authoritative lane key: it covers every row in
# sources.csv, including ids that do not follow the usual prefix convention
# (e.g. `dbe-maths-g12-p1-2024-nov`).
SUBJECT_TO_LANE = {
    "mathematics": "mathematics",
    "wiskunde": "mathematics",
    "physical": "physical_sciences",
    "fisiese": "physical_sciences",
    "english": "english",
    "afrikaans": "afrikaans",
}

LANE_ORDER = ["mathematics", "physical_sciences", "english", "afrikaans"]


def expected_marks(source_id: str) -> int:
    """Printed exam total for a paper.

    Language subject ids are shaped `dbe-english_hl-...` / `dbe-english_fal-...`,
    so the track token sits before the grade, separated by underscores.
    """
    m = re.search(r"_(hl|fal)-g\d+", source_id)
    if m:
        return 70 if m.group(1) == "hl" else 80
    return 150


def lane_of(row):
    """Resolve a source row to its lane, preferring the subject column."""
    lane = SUBJECT_TO_LANE.get((row.get("subject") or "").strip().lower())
    if lane:
        return lane
    sid = row.get("source_id", "")
    for lane_name, (_name, prefixes) in LANES.items():
        if sid.startswith(prefixes):
            return lane_name
    return None


def is_locked(row) -> bool:
    if "EVAL" in (row.get("notes") or ""):
        return True
    return row.get("year") == "2024"


def find_items_file(source_id: str):
    """Prefer the subject folder, fall back to the root mirror."""
    subj = list(ITEMS_DIR.glob(f"*/{source_id}.jsonl"))
    if subj:
        return subj[0]
    root = ITEMS_DIR / f"{source_id}.jsonl"
    return root if root.exists() else None


def inspect(source_id: str) -> dict:
    path = find_items_file(source_id)
    if path is None:
        return {"items": 0, "marks": 0, "katex": 0, "review": 0, "path": None}

    items, katex, review = [], 0, 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            it = json.loads(line)
        except json.JSONDecodeError:
            katex += 1
            continue
        items.append(it)
        if it.get("needs_review") is True:
            review += 1
        for field in ("question", "memo", "passage", "final_answer"):
            txt = it.get(field, "")
            if isinstance(txt, str) and len(re.findall(r"(?<!\\)\$", txt)) % 2:
                katex += 1

    return {
        "items": len(items),
        "marks": sum(int(it.get("marks") or 0) for it in items),
        "katex": katex,
        "review": review,
        "path": path,
    }


def status_of(row) -> str:
    sid = row["source_id"]
    if is_locked(row):
        return "LOCKED_EVAL"

    if not (TEXT_DIR / f"{sid}.txt").exists():
        return "NO_TEXT"

    info = inspect(sid)
    if info["items"]:
        return "DONE_OK" if info["marks"] == expected_marks(sid) else "DONE_BAD"

    pair = row.get("pair_with") or ""
    if pair and not (TEXT_DIR / f"{pair}.txt").exists():
        return "BLOCKED"

    return "TODO"


def load_rows():
    with open(SOURCES_CSV, encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r.get("kind") == "past_paper"]


def main() -> int:
    if not SOURCES_CSV.exists():
        print(f"error: {SOURCES_CSV} not found", file=sys.stderr)
        return 1

    rows = load_rows()
    buckets = {lane: {"TODO": [], "DONE_OK": [], "DONE_BAD": [],
                      "NO_TEXT": [], "BLOCKED": [], "LOCKED_EVAL": []}
               for lane in LANES}

    unmapped = []
    for row in rows:
        lane = lane_of(row)
        if lane is None:
            unmapped.append(row["source_id"])
            continue
        buckets[lane][status_of(row)].append(row)

    print("=" * 78)
    print("EISHKOM AI - EXTRACTION QUEUE")
    print("=" * 78)

    for lane in LANE_ORDER:
        name = LANES[lane][0]
        b = buckets[lane]
        done = len(b["DONE_OK"])
        total = sum(len(v) for v in b.values() if True)
        print()
        print(f"[{name}]  {done} verified / {len(b['TODO']) + done + len(b['DONE_BAD'])} text-ready papers")
        print(f"  DONE_OK {len(b['DONE_OK']):>3}   DONE_BAD {len(b['DONE_BAD']):>2}   "
              f"TODO {len(b['TODO']):>2}   NO_TEXT {len(b['NO_TEXT']):>2}   "
              f"LOCKED {len(b['LOCKED_EVAL']):>2}")

        if b["DONE_BAD"]:
            print("  ! repair needed:")
            for r in b["DONE_BAD"]:
                info = inspect(r["source_id"])
                print(f"      {r['source_id']}  {info['marks']}/{expected_marks(r['source_id'])} marks")

        next_batch = b["TODO"][:3]
        if next_batch:
            print("  next up:")
            for r in next_batch:
                sid = r["source_id"]
                print(f"      {sid}  -> {r.get('pair_with')}  [{expected_marks(sid)} marks]")
        elif b["DONE_BAD"]:
            print("  next up: repair the DONE_BAD paper above")
        else:
            print("  next up: nothing pending (new text extracts may be needed)")

    pending = sum(len(buckets[l]["TODO"]) + len(buckets[l]["DONE_BAD"]) for l in LANES)
    accounted = sum(len(v) for b in buckets.values() for v in b.values())
    print()
    print("=" * 78)
    print(f"TOTAL ACTIONABLE PAPERS: {pending}")
    print(f"ROWS ACCOUNTED: {accounted}/{len(rows)}")
    if unmapped:
        print(f"WARNING: {len(unmapped)} row(s) matched no lane:")
        for sid in unmapped:
            print(f"  {sid}")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
