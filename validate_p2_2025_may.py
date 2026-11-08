import json
import os
import re

file_paths = [
    "sa-tutor-kit/sa-tutor-kit/workspace/items/physical_sciences/dbe-physical_sciences-g12-p2-2025-may.jsonl",
    "sa-tutor-kit/sa-tutor-kit/workspace/items/dbe-physical_sciences-g12-p2-2025-may.jsonl"
]

required_keys = [
    "item_id", "source_id", "pair_source_id", "subject", "grade",
    "language", "track", "kind", "question_ref", "marks", "topic",
    "passage", "question", "memo", "final_answer", "needs_review",
    "licence", "attribution"
]

for fpath in file_paths:
    print(f"\n--- VALIDATING {fpath} ---")
    assert os.path.exists(fpath), f"File not found: {fpath}"
    
    total_marks = 0
    items_count = 0
    needs_review_count = 0
    
    with open(fpath, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            
            try:
                data = json.loads(line)
            except Exception as e:
                raise ValueError(f"Line {line_num}: Invalid JSON: {e}")
            
            # Check keys
            for k in required_keys:
                if k not in data:
                    raise KeyError(f"Line {line_num}: Missing required key '{k}'")
            
            # Check types
            assert isinstance(data["item_id"], str) and data["item_id"], f"Line {line_num}: item_id must be non-empty string"
            assert data["source_id"] == "dbe-physical_sciences-g12-p2-2025-may", f"Line {line_num}: source_id mismatch"
            assert data["pair_source_id"] == "dbe-physical_sciences-g12-p2-2025-may-memo", f"Line {line_num}: pair_source_id mismatch"
            assert data["subject"] == "physical_sciences", f"Line {line_num}: subject mismatch"
            assert data["grade"] == 12, f"Line {line_num}: grade mismatch"
            assert data["language"] == "en", f"Line {line_num}: language mismatch"
            assert data["track"] == "sciences", f"Line {line_num}: track mismatch"
            assert data["kind"] in ["question", "passage_questions"], f"Line {line_num}: invalid kind"
            assert isinstance(data["marks"], int) and data["marks"] > 0, f"Line {line_num}: marks must be positive int"
            assert isinstance(data["topic"], str) and data["topic"], f"Line {line_num}: topic empty"
            assert isinstance(data["passage"], str), f"Line {line_num}: passage not string"
            assert isinstance(data["question"], str) and data["question"], f"Line {line_num}: question empty"
            assert isinstance(data["memo"], str) and data["memo"], f"Line {line_num}: memo empty"
            assert isinstance(data["final_answer"], str), f"Line {line_num}: final_answer not string"
            assert isinstance(data["needs_review"], bool), f"Line {line_num}: needs_review not bool"
            assert data["licence"] == "DBE copyright - check terms", f"Line {line_num}: licence mismatch"
            assert data["attribution"] == "Department of Basic Education", f"Line {line_num}: attribution mismatch"
            
            total_marks += data["marks"]
            items_count += 1
            if data["needs_review"]:
                needs_review_count += 1
            
            # Check KaTeX balance
            for text_field in ["passage", "question", "memo"]:
                text_val = data[text_field]
                # remove display math $$ first
                cleaned = text_val.replace("$$", "")
                if cleaned.count("$") % 2 != 0:
                    raise ValueError(f"Line {line_num} ({data['item_id']}): Unbalanced $ in field '{text_field}'")
                
                # Check for bare °C (must be inside KaTeX with ^\circ\text{C} or ^\circ)
                # If bare °C outside of $...$ or without \circ
                for m in re.finditer(r'°C', text_val):
                    idx = m.start()
                    context = text_val[max(0, idx-10):min(len(text_val), idx+10)]
                    if "\\circ" not in context:
                        raise ValueError(f"Line {line_num} ({data['item_id']}): Bare °C in field '{text_field}': {context}")
                
                # Check for bare decimal comma in math mode e.g. $0,15$ instead of $0{,}15$
                # find math mode spans
                # inline math
                inline_matches = re.findall(r'\$([^\$]+)\$', cleaned)
                for math_str in inline_matches:
                    bare_comma = re.search(r'\d,\d', math_str)
                    if bare_comma:
                        raise ValueError(f"Line {line_num} ({data['item_id']}): Bare decimal comma '{bare_comma.group()}' in math mode: ${math_str}$")

    print(f"PASS: Items count = {items_count}")
    print(f"PASS: Total marks = {total_marks} (Expected: 150)")
    print(f"PASS: Needs review = {needs_review_count}")
    assert total_marks == 150, f"Expected 150 marks, got {total_marks}"
    assert items_count == 69, f"Expected 69 items, got {items_count}"

print("\nALL VALIDATIONS PASSED PERFECTLY!")
