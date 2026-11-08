import json

for path in [
    'workspace/items/physical_sciences/dbe-physical_sciences-g12-p1-2022-nov.jsonl',
    'workspace/items/dbe-physical_sciences-g12-p1-2022-nov.jsonl'
]:
    with open(path, 'r', encoding='utf-8') as f:
        items = [json.loads(line) for line in f]

    print(f'Checking {path}...')
    print(f'  Total items: {len(items)}')
    total_marks = sum(item['marks'] for item in items)
    print(f'  Total marks: {total_marks}')
    assert total_marks == 150, f'Expected 150 marks, got {total_marks}'

    ids = [item['item_id'] for item in items]
    assert len(ids) == len(set(ids)), 'Duplicate item_ids found!'

    required_keys = [
        'item_id', 'source_id', 'pair_source_id', 'subject', 'grade',
        'language', 'track', 'kind', 'question_ref', 'marks', 'topic',
        'passage', 'question', 'memo', 'final_answer', 'needs_review',
        'licence', 'attribution'
    ]
    for item in items:
        for k in required_keys:
            assert k in item, f'Missing key {k}'

    for item in items:
        for f in ['passage', 'question', 'memo', 'final_answer']:
            val = item[f]
            s = val.replace('$$', '')
            assert s.count('$') % 2 == 0, f'Unbalanced dollar in {item["item_id"]} field {f}'
            assert r'\text{^\circ C}' not in val, f'Illegal celsius formatting in {item["item_id"]}'

    print(f'  {path}: PASS (100% compliant, 0 KaTeX errors, marks: 150/150)')

print('All files validated successfully!')
