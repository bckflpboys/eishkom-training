# -*- coding: utf-8 -*-
import json
import re

paths = [
    "workspace/items/afrikaans_fal/dbe-afrikaans_fal-g12-p1-2020-nov.jsonl",
    "workspace/items/dbe-afrikaans_fal-g12-p1-2020-nov.jsonl",
    "sa-tutor-kit/sa-tutor-kit/workspace/items/afrikaans_fal/dbe-afrikaans_fal-g12-p1-2020-nov.jsonl",
    "sa-tutor-kit/sa-tutor-kit/workspace/items/dbe-afrikaans_fal-g12-p1-2020-nov.jsonl"
]

required_keys = [
    "item_id", "source_id", "pair_source_id", "subject", "grade",
    "language", "track", "kind", "question_ref", "marks", "topic",
    "passage", "question", "memo", "final_answer", "needs_review",
    "licence", "attribution"
]

expected_q_refs = [
    "1.1", "1.2", "1.3", "1.4", "1.5", "1.6.1", "1.6.2",
    "1.7.1", "1.7.2", "1.7.3", "1.8", "1.9", "1.10", "1.11",
    "1.12", "1.13", "1.14", "1.15", "1.16", "1.17",
    "1.18", "1.19", "1.20", "1.21.1", "1.21.2", "1.22",
    "2",
    "3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "3.8", "3.9", "3.10",
    "4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7", "4.8.1", "4.8.2", "4.9",
    "5.1.1", "5.1.2", "5.1.3", "5.1.4", "5.1.5", "5.1.6", "5.1.7",
    "5.1.8", "5.1.9", "5.1.10", "5.1.11", "5.1.12", "5.1.13", "5.1.14",
    "5.2.1", "5.2.2", "5.2.3", "5.2.4", "5.2.5", "5.2.6"
]

for p in paths:
    print("Checking:", p)
    with open(p, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"  Item count: {len(lines)}")
    assert len(lines) == len(expected_q_refs), f"Item count mismatch: {len(lines)} != {len(expected_q_refs)}"
    
    total_marks = 0
    actual_refs = []
    
    for idx, line in enumerate(lines):
        obj = json.loads(line)
        for k in required_keys:
            assert k in obj, f"Missing key {k} in item {idx+1}"
            assert obj[k] is not None, f"Key {k} is None in item {idx+1}"
        
        actual_refs.append(obj["question_ref"])
        total_marks += obj["marks"]
        
        for field in ["question", "memo", "final_answer", "passage"]:
            val = obj.get(field, "")
            dollars = re.findall(r"(?<!\\)\$", val)
            assert len(dollars) % 2 == 0, f"Unclosed dollar sign in {obj['item_id']} field {field}"

    assert actual_refs == expected_q_refs, f"Question ref mismatch: {actual_refs} vs {expected_q_refs}"
    assert total_marks == 80, f"Total marks mismatch: {total_marks} != 80"
    print(f"  Verified marks: {total_marks} / 80")
    print(f"  KaTeX balance: OK (0 unclosed dollars)")

print("\nALL 4 FILES FULLY VALIDATED AND PASS ALL CAPS/UDVES INTEGRITY CHECKS!")
