import urllib.request
import json
import time
import ssl

def load_env():
    env = {}
    with open('.env', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                env[k.strip()] = v.strip().strip('\'"')
    return env

env = load_env()
print("=" * 70)
print("       EISHKOM AI — COMPREHENSIVE PROVIDER & QUOTA HEALTH CHECK")
print("=" * 70)

# 1. Cerebras (New Key)
crb_key = env.get('CEREBRAS_API_KEY')
try:
    url = 'https://api.cerebras.ai/v1/chat/completions'
    headers = {'Authorization': f'Bearer {crb_key}', 'Content-Type': 'application/json', 'User-Agent': 'curl/8.4.0'}
    payload = {'model': 'qwen-3.8-27b', 'messages': [{'role': 'user', 'content': '1+1'}], 'max_tokens': 10}
    t0 = time.time()
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        dt = time.time() - t0
        print(f"[CEREBRAS (NEW KEY)]  PASS | qwen-3.8-27b | {dt:.2f}s latency | Quota FRESH")
except Exception as e:
    print(f"[CEREBRAS (NEW KEY)]  FAIL | {e}")

# 2. Google AI Studio Key 1
k1 = env.get('GEMINI_API_KEY')
try:
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key={k1}'
    t0 = time.time()
    req = urllib.request.Request(url, data=json.dumps({'contents': [{'parts': [{'text': '1+1'}]}]}).encode('utf-8'), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=10) as r:
        dt = time.time() - t0
        print(f"[AI STUDIO KEY 1]     PASS | gemini-3.5-flash-lite | {dt:.2f}s latency | Active")
except Exception as e:
    print(f"[AI STUDIO KEY 1]     FAIL | {e}")

# 3. Google AI Studio Key 2
k2 = env.get('GEMINI_API_KEY_2')
try:
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key={k2}'
    t0 = time.time()
    req = urllib.request.Request(url, data=json.dumps({'contents': [{'parts': [{'text': '1+1'}]}]}).encode('utf-8'), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=10) as r:
        dt = time.time() - t0
        print(f"[AI STUDIO KEY 2]     PASS | gemini-3.5-flash-lite | {dt:.2f}s latency | Active")
except Exception as e:
    print(f"[AI STUDIO KEY 2]     FAIL | {e}")

# 4. Google AI Studio Key 3 (Paid check)
k3 = env.get('GEMINI_API_KEY_3')
try:
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key={k3}'
    req = urllib.request.Request(url, data=json.dumps({'contents': [{'parts': [{'text': '1+1'}]}]}).encode('utf-8'), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=10) as r:
        print("[AI STUDIO KEY 3]     PASS | Credits active!")
except urllib.error.HTTPError as he:
    body = he.read().decode('utf-8', errors='replace')[:80]
    print(f"[AI STUDIO KEY 3]     WARN | HTTP {he.code}: {body}")
except Exception as e:
    print(f"[AI STUDIO KEY 3]     FAIL | {e}")

# 5. Groq
grq_key = env.get('GROQ_API_KEY')
try:
    url = 'https://api.groq.com/openai/v1/chat/completions'
    headers = {'Authorization': f'Bearer {grq_key}', 'Content-Type': 'application/json', 'User-Agent': 'curl/8.4.0'}
    payload = {'model': 'qwen/qwen3.8-27b', 'messages': [{'role': 'user', 'content': '1+1'}], 'max_tokens': 10}
    t0 = time.time()
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        dt = time.time() - t0
        print(f"[GROQ LPU]            PASS | qwen3.8-27b | {dt:.2f}s latency | Active")
except Exception as e:
    print(f"[GROQ LPU]            FAIL | {e}")

# 6. NVIDIA NIM
nvd_key = env.get('NVIDIA_API_KEY')
try:
    url = 'https://integrate.api.nvidia.com/v1/chat/completions'
    headers = {'Authorization': f'Bearer {nvd_key}', 'Content-Type': 'application/json', 'User-Agent': 'curl/8.4.0'}
    payload = {'model': 'nvidia/nemotron-3.5-lightning-30b-a3b', 'messages': [{'role': 'user', 'content': '1+1'}], 'max_tokens': 10}
    t0 = time.time()
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        dt = time.time() - t0
        print(f"[NVIDIA NIM]          PASS | nemotron-3.5-lightning | {dt:.2f}s latency | Active")
except Exception as e:
    print(f"[NVIDIA NIM]          FAIL | {e}")

# 7. Cohere
coh_key = env.get('COHERE_API_KEY')
try:
    url = 'https://api.cohere.com/v2/chat'
    headers = {'Authorization': f'Bearer {coh_key}', 'Content-Type': 'application/json', 'User-Agent': 'curl/8.4.0'}
    payload = {'model': 'command-a-03-2025', 'messages': [{'role': 'user', 'content': '1+1'}]}
    t0 = time.time()
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        dt = time.time() - t0
        print(f"[COHERE]              PASS | command-a-03-2025 | {dt:.2f}s latency | Active")
except Exception as e:
    print(f"[COHERE]              FAIL | {e}")

# 8. Intern-AI
int_key = env.get('INTERN_API_KEY')
int_base = env.get('INTERN_BASE_URL', 'https://discovery-api.intern-ai.org.cn/v1')
try:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url = f'{int_base}/chat/completions'
    headers = {'Authorization': f'Bearer {int_key}', 'Content-Type': 'application/json', 'User-Agent': 'curl/8.4.0'}
    payload = {'model': 'deepseek-v4-flash-0731', 'messages': [{'role': 'user', 'content': '1+1'}], 'max_tokens': 10}
    t0 = time.time()
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
        dt = time.time() - t0
        print(f"[INTERN-AI]           PASS | deepseek-v4-flash | {dt:.2f}s latency | Active")
except Exception as e:
    print(f"[INTERN-AI]           FAIL | {e}")

# 9. OpenRouter
orp_key = env.get('OPENROUTER_API_KEY')
try:
    url = 'https://openrouter.ai/api/v1/chat/completions'
    headers = {'Authorization': f'Bearer {orp_key}', 'Content-Type': 'application/json', 'User-Agent': 'curl/8.4.0'}
    payload = {'model': 'nvidia/nemotron-3-ultra-550b-a55b:free', 'messages': [{'role': 'user', 'content': '1+1'}], 'max_tokens': 10}
    t0 = time.time()
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        dt = time.time() - t0
        print(f"[OPENROUTER]          PASS | nemotron-3-ultra-550b:free | {dt:.2f}s latency | Active")
except Exception as e:
    print(f"[OPENROUTER]          FAIL | {e}")

print("=" * 70)

