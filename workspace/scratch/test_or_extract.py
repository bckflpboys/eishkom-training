import os
import json
import urllib.request
import urllib.error
from pathlib import Path

env = {}
for line in Path('.env').read_text(encoding='utf-8').splitlines():
    if line and not line.startswith('#') and '=' in line:
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip().strip('"\'')

or_key = env.get('OPENROUTER_API_KEY')

prompt = """You are an educational assistant. Output only a JSON array with one object:
[{"item_id": "test-1", "question": "What is $2+2$?", "final_answer": "4", "marks": 1}]
"""

m = "nvidia/nemotron-3.5-super-vl:free"
url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {or_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://eishkom.ai",
    "X-Title": "Eishkom AI"
}
data = json.dumps({
    "model": m,
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.1,
    "max_tokens": 1000
}).encode('utf-8')

req = urllib.request.Request(url, data=data, headers=headers)
with urllib.request.urlopen(req, timeout=30) as r:
    res = json.loads(r.read().decode('utf-8'))
    print("RESPONSE:")
    print(res['choices'][0]['message'].get('content'))

