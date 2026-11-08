import os
import json
import re
import urllib.request
import urllib.error
from pathlib import Path

env = {}
for line in Path('.env').read_text(encoding='utf-8').splitlines():
    if line and not line.startswith('#') and '=' in line:
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip().strip('"\'')

or_key = env.get('OPENROUTER_API_KEY')

qp_text = """
QUESTION 1 / VRAAG 1
1.1 Which ONE of the following is a vector quantity?
A Mass
B Time
C Velocity
D Temperature (2)
1.2 An object moves at constant velocity. Which ONE of the following is TRUE?
A The net force acting on the object is zero.
B The object is accelerating. (2)
"""

memo_text = """
QUESTION 1 / VRAAG 1
1.1 C $\\checkmark\\checkmark$ (2)
1.2 A $\\checkmark\\checkmark$ (2)
"""

prompt = f"""You are an expert South African educational data editor. You are editing the file dbe-test-p1.jsonl.
Extract all atomic subquestions for Question 1 into valid JSON objects, one object per line (JSONL format).

RULES:
1. Each line MUST be a single valid JSON object with keys:
   "item_id", "source_id", "subject", "grade", "question_ref", "marks", "question", "memo", "final_answer"
2. Standardize math into KaTeX LaTeX ($...$).
3. Output ONLY the raw JSON lines to append. Do not include markdown blocks or commentary.

QUESTION:
{qp_text}

MEMO:
{memo_text}
"""

models_to_test = [
    "nvidia/nemotron-3.5-super-vl:free",
    "cohere/north-mini-code:free",
    "recursive/flint-v1.0:free"
]

for m in models_to_test:
    print(f"\n--- Testing Model: {m} ---")
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {or_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://eishkom.ai",
        "X-Title": "Eishkom AI"
    }
    data = json.dumps({
        "model": m,
        "messages": [
            {"role": "system", "content": "You are a code and JSON data editor. You output strictly raw JSONL lines."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1,
        "max_tokens": 1500
    }).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            res = json.loads(r.read().decode('utf-8'))
            msg = res['choices'][0]['message']
            content = msg.get('content') or msg.get('reasoning') or ""
            print("RECEIVED CONTENT:")
            print(content[:500])
    except urllib.error.HTTPError as e:
        print(f"HTTP ERROR {e.code}: {e.read().decode('utf-8')[:200]}")
    except Exception as e:
        print(f"EXCEPTION: {e}")

