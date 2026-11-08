import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

filepath = "workspace/items/physical_sciences/dbe-physical_sciences-g12-p1-2021-nov.jsonl"

with open(filepath, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

print(f"Total lines read: {len(lines)}")
assert len(lines) == 56, f"Expected 56 lines, got {len(lines)}"

items = [json.loads(line) for line in lines]

question_marks = {}
total_marks = 0

for i, it in enumerate(items):
    ref = it["question_ref"]
    marks = it["marks"]
    total_marks += marks
    
    # Track question main number
    q_main = ref.split(".")[0]
    question_marks[q_main] = question_marks.get(q_main, 0) + marks
    
    # Assertions
    assert it["item_id"] == f"dbe-physical_sciences-g12-p1-2021-nov-{ref}"
    assert it["source_id"] == "dbe-physical_sciences-g12-p1-2021-nov"
    assert it["pair_source_id"] == "dbe-physical_sciences-g12-p1-2021-nov-memo"
    assert it["subject"] == "physical_sciences"
    assert it["grade"] == 12
    assert it["language"] == "en"
    assert it["track"] == "physical_sciences"
    assert it["kind"] in ["question", "multiple_choice"]
    if q_main == "1":
        assert it["kind"] == "multiple_choice"
    else:
        assert it["kind"] == "question"
    assert it["marks"] > 0
    assert len(it["topic"]) > 0
    assert len(it["question"]) > 0
    assert len(it["memo"]) > 0
    assert len(it["final_answer"]) > 0
    assert it["needs_review"] is False
    assert it["licence"] == "DBE copyright - check terms"
    assert it["attribution"] == "Department of Basic Education"
    
    # KaTeX check
    for fld in ["passage", "question", "memo", "final_answer"]:
        text = it[fld]
        if text.count("$$") % 2 != 0:
            raise ValueError(f"Line {i+1} ({ref}) field {fld} has unclosed $$")
        t = re.sub(r"\$\$.*?\$\$", "", text, flags=re.DOTALL)
        t = re.sub(r"\\\$", "", t)
        if t.count("$") % 2 != 0:
            raise ValueError(f"Line {i+1} ({ref}) field {fld} has unclosed single $")
            
        # Check for malformed celsius
        if "\\text{^\\circ C}" in text or "^\\circ C" in text:
            raise ValueError(f"Line {i+1} ({ref}) field {fld} has incorrect celsius formatting")

print("\n--- QUESTION MARK BREAKDOWN ---")
expected_totals = {
    "1": 20,
    "2": 16,
    "3": 18,
    "4": 10,
    "5": 14,
    "6": 12,
    "7": 14,
    "8": 19,
    "9": 15,
    "10": 12
}

for q, m in sorted(question_marks.items(), key=lambda x: int(x[0])):
    exp = expected_totals.get(q)
    print(f"Question {q}: {m} marks (Expected: {exp}) {'[MATCH]' if m == exp else '[MISMATCH]'}")
    assert m == exp, f"Mismatch in Question {q}: got {m}, expected {exp}"

print(f"\nGRAND TOTAL MARKS: {total_marks} / 150 [PERFECT MATCH]")
print("ALL 56 ITEMS FULLY VALIDATED AND PASSED ALL QUALITY CHECKS!")
