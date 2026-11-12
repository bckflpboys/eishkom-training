import urllib.request, json, os
from pathlib import Path

env = dict(l.strip().split('=', 1) for l in Path('.env').read_text().splitlines() if '=' in l and not l.startswith('#'))
k = env.get('OPENROUTER_API_KEY')
url = 'https://openrouter.ai/api/v1/chat/completions'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {k}',
    'HTTP-Referer': 'https://eishkom.ai',
    'X-Title': 'Eishkom AI Tutor Stage 2'
}

models_to_test = [
    'nvidia/nemotron-3-ultra-550b-a55b:free',
    'nvidia/nemotron-3.5-lightning:free',
    'google/gemma-4-31b-it:free'
]

for m in models_to_test:
    payload = {
        'model': m,
        'messages': [{'role': 'user', 'content': 'Respond with raw JSON: {"status": "ok"}'}],
        'max_tokens': 50
    }
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers)
        with urllib.request.urlopen(req, timeout=15) as r:
            res = json.loads(r.read().decode())
            print(f'Model {m}: SUCCESS! Reply: {res["choices"][0]["message"]["content"][:60]}')
    except Exception as e:
        print(f'Model {m}: Error -> {e}')

