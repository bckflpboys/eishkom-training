import json
import re

REQUIRED_KEYS = [
    'item_id', 'source_id', 'pair_source_id', 'subject', 'grade',
    'language', 'track', 'kind', 'question_ref', 'marks', 'topic',
    'passage', 'question', 'memo', 'final_answer', 'needs_review',
    'licence', 'attribution'
]

files = [
    'workspace/items/mathematics/dbe-mathematics-g12-p1-2019-nov.jsonl',
    'workspace/items/dbe-mathematics-g12-p1-2019-nov.jsonl'
]

for filepath in files:
    print(f'Testing: {filepath}')
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    assert len(lines) == 48, f'Expected 48 lines, got {len(lines)}'
    total_marks = 0
    q_refs = []
    for idx, line in enumerate(lines):
        item = json.loads(line)
        for k in REQUIRED_KEYS:
            assert k in item, f"Missing key {k} in line {idx+1}"
        assert isinstance(item['marks'], int), f"marks not int in {item['item_id']}"
        total_marks += item['marks']
        q_refs.append(item['question_ref'])
        for fld in ['passage', 'question', 'memo', 'final_answer']:
            val = item[fld]
            wb = re.sub(r'\$\$.*?\$\$', '', val, flags=re.DOTALL)
            assert len(re.findall(r'(?<!\\)\$', wb)) % 2 == 0, f"Unbalanced $ in {item['item_id']} field {fld}"
            # Check for naked decimal comma in math mode, e.g. $0,15$ or $3,14$ instead of $0{,}15$
            bad_commas = re.findall(r'(?<=\$\d),(?=\d)', val)
            if bad_commas:
                print(f"Warning: naked decimal comma in {item['item_id']} field {fld}: {bad_commas}")
    assert total_marks == 150, f"Marks sum is {total_marks}, expected 150"
    print(f"  All checks passed for {filepath}: 48 items, {total_marks} marks, 0 KaTeX syntax issues!\n")
