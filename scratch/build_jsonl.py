import json
import os
import sys
import re

sys.path.append(os.path.dirname(__file__))

from section_a import items_a
from section_b import items_b
from section_c import items_c

all_items = items_a + items_b + items_c
print(f"Total items assembled: {len(all_items)}")

# Verification checks
REQUIRED_KEYS = [
    "item_id", "source_id", "pair_source_id", "subject", "grade",
    "language", "track", "kind", "question_ref", "marks", "topic",
    "passage", "question", "memo", "final_answer", "needs_review",
    "licence", "attribution"
]

katex_errors = 0
for idx, item in enumerate(all_items):
    # Check keys
    for k in REQUIRED_KEYS:
        assert k in item, f"Item {idx} missing key {k}"
    
    assert item["source_id"] == "dbe-english_hl-g12-p2-2025-nov"
    assert item["pair_source_id"] == "dbe-english_hl-g12-p2-2025-nov-memo"
    assert item["subject"] == "english_hl"
    assert item["grade"] == 12
    assert item["language"] == "en"
    assert item["track"] == "languages_hl"
    assert isinstance(item["marks"], int) and item["marks"] > 0
    assert isinstance(item["needs_review"], bool)

    # Check KaTeX balance in question and memo
    for field in ["question", "memo"]:
        text = item[field]
        # Count unescaped dollar signs
        dollars = re.findall(r'(?<!\\)\$', text)
        if len(dollars) % 2 != 0:
            print(f"ERROR: Unbalanced dollar signs in item {item['item_id']} field {field}")
            katex_errors += 1
        
        # Check invalid celsius notation
        if r"\text{^\circ C}" in text or r"\text{^∘ C}" in text:
            print(f"ERROR: Invalid degree Celsius in item {item['item_id']} field {field}")
            katex_errors += 1

assert katex_errors == 0, f"Found {katex_errors} KaTeX formatting errors!"
print("All items passed schema and KaTeX validation checks!")

# Paths to write
paths = [
    "sa-tutor-kit/sa-tutor-kit/workspace/items/english_hl/dbe-english_hl-g12-p2-2025-nov.jsonl",
    "sa-tutor-kit/sa-tutor-kit/workspace/items/dbe-english_hl-g12-p2-2025-nov.jsonl",
    "workspace/items/english_hl/dbe-english_hl-g12-p2-2025-nov.jsonl",
    "workspace/items/dbe-english_hl-g12-p2-2025-nov.jsonl"
]

for p in paths:
    abs_p = os.path.abspath(p)
    os.makedirs(os.path.dirname(abs_p), exist_ok=True)
    with open(abs_p, "w", encoding="utf-8") as f:
        for item in all_items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"Wrote {len(all_items)} lines to {abs_p} (size: {os.path.getsize(abs_p)} bytes)")

print("\n--- Summary ---")
print(f"Total items extracted: {len(all_items)}")
print(f"Total marks accounted: {sum(it['marks'] for it in all_items)}")
print(f"Candidate exam requirement marks: 80 (Section A: 30, Section B: 25, Section C: 25)")
print(f"Items with needs_review: true -> {sum(1 for it in all_items if it['needs_review'])}")
print(f"KaTeX errors: {katex_errors}")
