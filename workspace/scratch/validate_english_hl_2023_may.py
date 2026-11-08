import json
import re

REQUIRED_KEYS = [
    'item_id', 'source_id', 'pair_source_id', 'subject', 'grade',
    'language', 'track', 'kind', 'question_ref', 'marks', 'topic',
    'passage', 'question', 'memo', 'final_answer', 'needs_review',
    'licence', 'attribution'
]

files = [
    'workspace/items/english_hl/dbe-english_hl-g12-p1-2023-may.jsonl',
    'workspace/items/dbe-english_hl-g12-p1-2023-may.jsonl'
]

for filepath in files:
    print(f'Testing: {filepath}')
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    assert len(lines) == 31, f'Expected 31 lines, got {len(lines)}'
    total_marks = 0
    sec_a_marks = 0
    sec_b_marks = 0
    sec_c_marks = 0
    q_refs = []
    for idx, line in enumerate(lines):
        item = json.loads(line)
        for k in REQUIRED_KEYS:
            assert k in item, f"Missing key {k} in line {idx+1}"
        assert isinstance(item['marks'], int), f"marks not int in {item['item_id']}"
        total_marks += item['marks']
        ref = item['question_ref']
        q_refs.append(ref)
        if ref.startswith('1.'):
            sec_a_marks += item['marks']
        elif ref == '2':
            sec_b_marks += item['marks']
        else:
            sec_c_marks += item['marks']

        for fld in ['passage', 'question', 'memo', 'final_answer']:
            val = item[fld]
            wb = re.sub(r'\$\$.*?\$\$', '', val, flags=re.DOTALL)
            unbalanced = len(re.findall(r'(?<!\\)\$', wb)) % 2 != 0
            assert not unbalanced, f"Unbalanced $ in {item['item_id']} field {fld}"

    assert sec_a_marks == 30, f"Section A marks: {sec_a_marks}, expected 30"
    assert sec_b_marks == 10, f"Section B marks: {sec_b_marks}, expected 10"
    assert sec_c_marks == 30, f"Section C marks: {sec_c_marks}, expected 30"
    assert total_marks == 70, f"Marks sum is {total_marks}, expected 70"
    print(f"  All checks passed for {filepath}:")
    print(f"    Items: {len(lines)}")
    print(f"    Section A marks: {sec_a_marks}/30")
    print(f"    Section B marks: {sec_b_marks}/10")
    print(f"    Section C marks: {sec_c_marks}/30")
    print(f"    Total Marks: {total_marks}/70")
    print(f"    0 KaTeX syntax issues!\n")
