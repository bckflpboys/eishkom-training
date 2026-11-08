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

ai_key2 = env.get('GEMINI_API_KEY_2')
or_key = env.get('OPENROUTER_API_KEY')

print("--- TESTING AI STUDIO 2 ---")
for m in ['gemini-3.1-flash-lite', 'gemini-3.5-flash-lite', 'gemma-4-26b-a4b-it', 'gemma-4-31b-it']:
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={ai_key2}'
    data = json.dumps({'contents': [{'parts': [{'text': 'Say hello'}]}]}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            res = json.loads(r.read().decode('utf-8'))
            ans = res['candidates'][0]['content']['parts'][0]['text'].strip()
            print(f'[{m}] OK: {ans[:25]}')
    except Exception as e:
        print(f'[{m}] FAIL: {e}')

print("\n--- TESTING OPENROUTER FREE MODELS ---")
or_models = [
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

for m in or_models:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {or_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://eishkom.ai",
        "X-Title": "Eishkom AI"
    }
    data = json.dumps({
        "model": m,
        "messages": [{"role": "user", "content": "Say hello"}],
        "max_tokens": 10
    }).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            res = json.loads(r.read().decode('utf-8'))
            msg = res['choices'][0]['message']['content'].strip()
            print(f'[{m}] OK: {msg[:25]}')
    except Exception as e:
        print(f'[{m}] FAIL: {e}')

