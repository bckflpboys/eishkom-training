# -*- coding: utf-8 -*-
import json
import re

required_fields = [
    'item_id', 'source_id', 'pair_source_id', 'subject', 'grade',
    'language', 'track', 'kind', 'question_ref', 'marks', 'topic',
    'passage', 'question', 'memo', 'final_answer', 'needs_review',
    'licence', 'attribution'
]

file_path = 'workspace/items/dbe-mathematics-g12-p2-2020-nov.jsonl'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f'Total lines: {len(lines)}')

total_marks = 0
question_marks = {}
qref_list = []

for i, line in enumerate(lines):
    line_num = i + 1
    d = json.loads(line)
    
    # Check fields
    for field in required_fields:
        if field not in d:
            raise ValueError(f'Line {line_num} missing field {field}')
    
    # Check fixed values
    assert d['source_id'] == 'dbe-mathematics-g12-p2-2020-nov'
    assert d['pair_source_id'] == 'dbe-mathematics-g12-p2-2020-nov-memo'
    assert d['subject'] == 'mathematics'
    assert d['grade'] == 12
    assert d['language'] == 'en'
    assert d['track'] == 'core_maths'
    assert isinstance(d['marks'], int) and d['marks'] > 0
    assert isinstance(d['needs_review'], bool)
    
    q_ref = d['question_ref']
    qref_list.append(q_ref)
    q_num = q_ref.split('.')[0]
    question_marks[q_num] = question_marks.get(q_num, 0) + d['marks']
    total_marks += d['marks']
    
    # Check KaTeX balance in string fields
    for field in ['passage', 'question', 'memo', 'final_answer']:
        val = d[field]
        # Check even dollar signs
        cnt = val.count('$')
        if cnt % 2 != 0:
            raise ValueError(f'Line {line_num} field {field} has unbalanced dollar signs ({cnt})')
        # Check for unclosed display math
        parts = val.split('$$')
        for part_idx, part in enumerate(parts):
            if part_idx % 2 == 0 and part.count('$') % 2 != 0:
                raise ValueError(f'Line {line_num} field {field} has unbalanced inline math inside block')

print('Question Marks Breakdown:')
for q, m in sorted(question_marks.items(), key=lambda x: int(x[0])):
    print(f'  Question {q}: {m} marks')

print(f'Total Marks: {total_marks}')
print(f'Question Refs ({len(qref_list)} items):')
print(', '.join(qref_list))
print('ALL VERIFICATIONS PASSED!')
