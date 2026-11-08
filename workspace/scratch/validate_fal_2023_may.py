# -*- coding: utf-8 -*-
"""
Validation script for DBE English FAL Grade 12 P1 May/June 2023 JSONL files.
"""

import json
import os
import re

REQUIRED_KEYS = [
    "item_id", "source_id", "pair_source_id", "subject", "grade",
    "language", "track", "kind", "question_ref", "marks", "topic",
    "passage", "question", "memo", "final_answer", "needs_review",
    "licence", "attribution"
]

def check_katex(text: str) -> bool:
    tokens = re.findall(r'(?<!\\)\$', text)
    return len(tokens) % 2 == 0

def validate_file(filepath: str):
    print(f"\n--- Validating {filepath} ---")
    assert os.path.exists(filepath), f"File {filepath} does not exist!"

    lines = []
    with open(filepath, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            line_str = line.strip()
            if not line_str:
                continue
            try:
                data = json.loads(line_str)
            except Exception as e:
                raise ValueError(f"Line {idx} is invalid JSON: {e}")
            lines.append(data)

    print(f"Total items parsed: {len(lines)}")
    assert len(lines) == 48, f"Expected 48 items, got {len(lines)}"

    seen_ids = set()
    total_marks = 0
    section_a_marks = 0
    section_b_marks = 0
    section_c_marks = 0

    for idx, item in enumerate(lines, start=1):
        # 1. Check all required keys
        for key in REQUIRED_KEYS:
            assert key in item, f"Item {idx} missing key '{key}'"

        # 2. Key types and values
        assert item["item_id"] not in seen_ids, f"Duplicate item_id: {item['item_id']}"
        seen_ids.add(item["item_id"])

        assert item["source_id"] == "dbe-english_fal-g12-p1-2023-may"
        assert item["pair_source_id"] == "dbe-english_fal-g12-p1-2023-may-memo"
        assert item["subject"] == "english_fal"
        assert item["grade"] == 12
        assert item["language"] == "en"
        assert item["track"] == "languages_fal"
        assert item["kind"] in ["multiple_choice", "passage_questions", "question"]
        assert isinstance(item["marks"], int) and item["marks"] > 0
        assert item["needs_review"] is False
        assert item["licence"] == "DBE copyright - check terms"
        assert item["attribution"] == "Department of Basic Education"

        ref = item["question_ref"]
        marks = item["marks"]
        total_marks += marks

        if ref.startswith("1."):
            section_a_marks += marks
        elif ref == "2":
            section_b_marks += marks
        elif ref.startswith("3.") or ref.startswith("4.") or ref.startswith("5."):
            section_c_marks += marks
        else:
            raise ValueError(f"Unexpected question_ref: {ref}")

        # 3. KaTeX balance check
        for field in ["passage", "question", "memo", "final_answer"]:
            val = item[field]
            assert isinstance(val, str) and len(val.strip()) > 0, f"Empty {field} in {item['item_id']}"
            assert check_katex(val), f"Unbalanced KaTeX in {item['item_id']}, field {field}"

    print(f"Section A marks: {section_a_marks} (Expected: 30)")
    print(f"Section B marks: {section_b_marks} (Expected: 10)")
    print(f"Section C marks: {section_c_marks} (Expected: 40)")
    print(f"Total marks: {total_marks} (Expected: 80)")

    assert section_a_marks == 30, f"Section A marks mismatch: {section_a_marks} != 30"
    assert section_b_marks == 10, f"Section B marks mismatch: {section_b_marks} != 10"
    assert section_c_marks == 40, f"Section C marks mismatch: {section_c_marks} != 40"
    assert total_marks == 80, f"Total marks mismatch: {total_marks} != 80"

    print("ALL VALIDATION CHECKS PASSED!")

def main():
    f1 = "workspace/items/english_fal/dbe-english_fal-g12-p1-2023-may.jsonl"
    f2 = "workspace/items/dbe-english_fal-g12-p1-2023-may.jsonl"

    validate_file(f1)
    validate_file(f2)

    with open(f1, "rb") as a, open(f2, "rb") as b:
        assert a.read() == b.read(), "Mirror files are not byte-for-byte identical!"
    print("\nMirror files are byte-for-byte IDENTICAL!")

if __name__ == "__main__":
    main()
