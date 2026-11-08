# validate_items.py
import json
import re

def validate_katex(text, item_id, field_name):
    errors = []
    # Count unescaped $
    dollar_count = 0
    escaped = False
    for ch in text:
        if ch == '\\':
            escaped = not escaped
        elif ch == '$' and not escaped:
            dollar_count += 1
            escaped = False
        else:
            escaped = False
    if dollar_count % 2 != 0:
        errors.append(f"{item_id} {field_name}: Unbalanced dollar delimiters (count={dollar_count})")
    
    # Check for forbidden degree celsius
    if r"\text{^" in text or r"\text{^{\circ" in text:
        errors.append(f"{item_id} {field_name}: Invalid degree celsius formatting \\text{{^")
        
    # Check for bare decimal commas in math mode
    math_segments = re.findall(r"\$\$(.*?)\$\$|\$(.*?)\$", text, flags=re.DOTALL)
    for m1, m2 in math_segments:
        m_content = m1 if m1 else m2
        bare_comma = re.search(r"\d,\d", m_content)
        if bare_comma:
            errors.append(f"{item_id} {field_name}: Bare decimal comma in math mode: {bare_comma.group(0)}")

    return errors

all_errors = []
total_marks = 0

with open("sa-tutor-kit/sa-tutor-kit/workspace/items/mathematics/dbe-mathematics-g12-p2-2025-may.jsonl", "r", encoding="utf-8") as f:
    items = [json.loads(line) for line in f]

expected_keys = [
    "item_id", "source_id", "pair_source_id", "subject", "grade",
    "language", "track", "kind", "question_ref", "marks", "topic",
    "passage", "question", "memo", "final_answer", "needs_review",
    "licence", "attribution"
]

for item in items:
    for k in expected_keys:
        if k not in item:
            all_errors.append(f"{item.get('item_id')}: Missing key {k}")
    
    if not isinstance(item["marks"], int):
        all_errors.append(f"{item['item_id']}: marks is not integer")
    if not isinstance(item["needs_review"], bool):
        all_errors.append(f"{item['item_id']}: needs_review is not boolean")
    if item["grade"] != 12:
        all_errors.append(f"{item['item_id']}: grade != 12")
    if item["language"] != "en":
        all_errors.append(f"{item['item_id']}: language != en")
    if item["track"] != "core_maths":
        all_errors.append(f"{item['item_id']}: track != core_maths")
        
    total_marks += item["marks"]
    
    for f in ["passage", "question", "memo"]:
        errs = validate_katex(item[f], item["item_id"], f)
        all_errors.extend(errs)

print(f"Total items checked: {len(items)}")
print(f"Total marks accounted for: {total_marks} / 150")
print(f"Total errors: {len(all_errors)}")
if all_errors:
    for e in all_errors[:20]:
        print("  ERROR:", e)
else:
    print("ALL CHECKS PASSED PERFECTLY (0 ERRORS)!")
