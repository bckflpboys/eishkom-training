import json
import os

paths = [
    "workspace/items/english_fal/dbe-english_fal-g12-p1-2022-nov.jsonl",
    "workspace/items/dbe-english_fal-g12-p1-2022-nov.jsonl",
]

required_keys = [
    "item_id", "source_id", "pair_source_id", "subject", "grade",
    "language", "track", "kind", "question_ref", "marks", "topic",
    "passage", "question", "memo", "final_answer", "needs_review",
    "licence", "attribution"
]

for p in paths:
    assert os.path.exists(p), f"File missing: {p}"
    print(f"Checking {p}...")
    with open(p, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"  Line count: {len(lines)}")
    items = []
    seen_ids = set()
    total_marks = 0
    section_marks = {"A": 0, "B": 0, "C_Q3": 0, "C_Q4": 0, "C_Q5": 0}

    for idx, line in enumerate(lines):
        line = line.strip()
        assert line, f"Empty line at {idx+1}"
        data = json.loads(line)
        for k in required_keys:
            assert k in data, f"Missing key {k} in item {data.get('item_id', idx)}"
        assert data["item_id"] not in seen_ids, f"Duplicate item_id {data['item_id']}"
        seen_ids.add(data["item_id"])

        marks = data["marks"]
        assert isinstance(marks, int) and marks > 0, f"Invalid marks: {marks} in {data['item_id']}"
        total_marks += marks

        ref = data["question_ref"]
        if ref.startswith("1."):
            section_marks["A"] += marks
        elif ref == "2":
            section_marks["B"] += marks
        elif ref.startswith("3."):
            section_marks["C_Q3"] += marks
        elif ref.startswith("4."):
            section_marks["C_Q4"] += marks
        elif ref.startswith("5."):
            section_marks["C_Q5"] += marks

        # KaTeX checks
        for field in ["passage", "question", "memo", "final_answer"]:
            val = data[field]
            dollars = val.count("$")
            assert dollars % 2 == 0, f"Unbalanced dollars in {data['item_id']} ({field})"

    assert total_marks == 80, f"Total marks {total_marks} != 80"
    assert section_marks["A"] == 30, f"Section A marks {section_marks['A']} != 30"
    assert section_marks["B"] == 10, f"Section B marks {section_marks['B']} != 10"
    assert section_marks["C_Q3"] == 10, f"Question 3 marks {section_marks['C_Q3']} != 10"
    assert section_marks["C_Q4"] == 10, f"Question 4 marks {section_marks['C_Q4']} != 10"
    assert section_marks["C_Q5"] == 20, f"Question 5 marks {section_marks['C_Q5']} != 20"

    print("  ALL CHECKS PASSED!")
    print(f"  Total marks: {total_marks}")
    print(f"  Section breakdown: {section_marks}")
