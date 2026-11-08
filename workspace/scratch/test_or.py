import os
import json
import time
import urllib.request
import urllib.error
from pathlib import Path

env = {}
for line in Path('.env').read_text(encoding='utf-8').splitlines():
    if line and not line.startswith('#') and '=' in line:
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip().strip('"\'')

or_key = env.get('OPENROUTER_API_KEY')

models = [
    "nvidia/nemotron-3.5-super-vl:free",
    "nvidia/nemotron-3-ultra-550b-a55b:free",
    "nvidia/nemotron-3.5-lightning:free",
    "dots-studio/dots-3-note-preview:free",
    "cohere/north-mini-code:free",
    "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
    "xingchen-agi/xing4.0-29b-a4b:free",
    "recursive/flint-v1.0:free",
    "google/gemma-4-26b-a4b-it:free",
    "google/gemma-4-31b-it:free"
]

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {or_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://eishkom.ai",
    "X-Title": "Eishkom AI"
}

for m in models:
    data = json.dumps({
        "model": m,
        "messages": [{"role": "user", "content": "Respond only with: OK"}],
        "max_tokens": 100
    }).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            res = json.loads(r.read().decode('utf-8'))
            msg = res['choices'][0]['message'].get('content') or ""
            print(f"[{m}] SUCCESS: {msg.strip()[:30]}")
    except urllib.error.HTTPError as e:
        err = e.read().decode('utf-8')
        try:
            err_j = json.loads(err)
            msg = err_j.get('error', {}).get('message', '')
        except:
            msg = err[:100]
        print(f"[{m}] HTTP {e.code}: {msg}")
    except Exception as e:
        print(f"[{m}] Exception: {e}")
    time.sleep(1.0)
