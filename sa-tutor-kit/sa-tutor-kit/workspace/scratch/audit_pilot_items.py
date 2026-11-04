import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

targets = [
    ("Mathematics P1 (2023 Nov)", "mathematics/dbe-mathematics-g12-p1-2023-nov.jsonl", 150),
    ("Physical Sciences P2 (2025 Nov)", "physical_sciences/dbe-physical_sciences-g12-p2-2025-nov.jsonl", 150),
    ("English HL P1 (2023 Nov)", "english_hl/dbe-english_hl-g12-p1-2023-nov.jsonl", 70),
    ("Afrikaans HL P1 (2023 Nov)", "afrikaans_hl/dbe-afrikaans_hl-g12-p1-2023-nov.jsonl", 70),
]

base = Path("sa-tutor-kit/sa-tutor-kit/workspace/items")

print("=== PHASE 2.5 PILOT EXTRACTION AUDIT ===")
all_pass = True

for title, rel_path, expected_marks in targets:
    fpath = base / rel_path
    if not fpath.exists():
        print(f"[FAIL] {title}: File not found at {fpath}")
        all_pass = False
        continue
    
    lines = fpath.read_text(encoding="utf-8").splitlines()
    items = []
    syntax_errors = 0
    katex_unclosed = 0
    
    for idx, l in enumerate(lines, 1):
        if not l.strip():
            continue
        try:
            it = json.loads(l)
            items.append(it)
        except Exception as e:
            syntax_errors += 1
            print(f"  Line {idx} JSON parse error: {e}")
            
    calc_marks = sum(it.get("marks", 0) for it in items)
    
    # Check katex unclosed dollars
    for it in items:
        for field in ["question", "memo", "passage", "final_answer"]:
            txt = it.get(field, "")
            if isinstance(txt, str):
                dollars = len(re.findall(r"(?<!\\)\$", txt))
                if dollars % 2 != 0:
                    katex_unclosed += 1
                    
    mark_status = "[OK]" if calc_marks == expected_marks else f"[WARN: got {calc_marks}, expected {expected_marks}]"
    print(f"\n{title}:")
    print(f"  File: {rel_path} ({len(lines)} lines)")
    print(f"  Items: {len(items)}")
    print(f"  Marks: {calc_marks} / {expected_marks} {mark_status}")
    print(f"  Syntax Errors: {syntax_errors}")
    print(f"  Unclosed KaTeX $: {katex_unclosed}")
    
    if items:
        first = items[0]
        item_id = first.get("item_id")
        qref = first.get("question_ref")
        q_snip = str(first.get("question", ""))[:80].replace("\n", " ")
        m_snip = str(first.get("memo", ""))[:80].replace("\n", " ")
        print(f"  Sample Item ID: {item_id}")
        print(f"  Question Ref: {qref}")
        print(f"  Question snippet: {q_snip}...")
        print(f"  Memo snippet: {m_snip}...")

print("\n=== MIRROR VERIFICATION ===")
for title, rel_path, expected_marks in targets:
    filename = Path(rel_path).name
    root_mirror = base / filename
    if root_mirror.exists():
        print(f"[OK] Root mirror exists: workspace/items/{filename} ({root_mirror.stat().st_size} bytes)")
    else:
        print(f"[FAIL] Missing root mirror: workspace/items/{filename}")
