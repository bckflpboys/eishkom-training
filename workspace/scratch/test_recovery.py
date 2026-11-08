import json
import re
import sys
import subprocess
from pathlib import Path

def normalize_text(s):
    # Convert South African decimal commas like 13{,}32 or 13,32 to 13.32
    s = re.sub(r'(\d+)\{?,\}?(\d+)', r'\1.\2', s)
    # Strip LaTeX units like \text{ m/s}
    s = re.sub(r'\\text\{[^}]*\}', '', s)
    return s

def extract_numbers(s):
    s = normalize_text(s)
    return set(re.findall(r'-?\d+(?:\.\d+)?', s))

# Test on lane 7 (Physics EN)
p = 'dbe-physical_sciences-g12-p1-2022-nov'
items = {json.loads(l)['item_id']: json.loads(l) for l in open(f'workspace/items/{p}.jsonl', encoding='utf-8')}
gen_lines = [json.loads(l) for l in open(f'workspace/gen/wave2/{p}.jsonl', encoding='utf-8')]

passed_orig = 9
can_recover = 0
reasons = []

for d in gen_lines:
    iid = d['item_id']
    item = items.get(iid, {})
    memo_ans = item.get('final_answer') or item.get('memo', '')
    raw = d['raw']
    try:
        obj = json.loads(raw)
        code = obj.get('meta', {}).get('verify_code', '')
        if code:
            r = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True, timeout=5)
            out = r.stdout.strip()
            nums_out = extract_numbers(out)
            nums_memo = extract_numbers(memo_ans)
            if nums_out and nums_memo and (nums_out.issubset(nums_memo) or nums_memo.issubset(nums_out) or bool(nums_out & nums_memo)):
                can_recover += 1
                reasons.append((iid, out, memo_ans[:40]))
    except Exception as e:
        pass

print(f"Original verified in Physics EN: {passed_orig} / {len(gen_lines)}")
print(f"With comma & unit normalization: {can_recover} / {len(gen_lines)} ({(can_recover/len(gen_lines)*100):.1f}%)")
print("\nSample recovered items:")
for iid, out, memo in reasons[:6]:
    print(f"  {iid}: SymPy='{out}' vs Memo='{memo}'")

