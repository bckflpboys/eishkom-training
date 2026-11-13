import urllib.request
import json
import ssl
import time

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

tests = []

# AI Studio Key 1
k1 = env.get('GEMINI_API_KEY')
for m in ['gemini-3.5-flash-lite', 'gemini-3.1-flash-lite', 'gemini-4-hydrogen', 'gemma-4-31b-it', 'gemma-4-26b-a4b-it']:
    tests.append(('AI Studio 1', m, f'https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={k1}', {'Content-Type': 'application/json'}, {'contents': [{'parts': [{'text': 'hi'}]}]}))

# AI Studio Key 2
k2 = env.get('GEMINI_API_KEY_2')
for m in ['gemini-3.5-flash-lite', 'gemini-3.1-flash-lite', 'gemini-4-hydrogen', 'gemma-4-31b-it', 'gemma-4-26b-a4b-it']:
    tests.append(('AI Studio 2', m, f'https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={k2}', {'Content-Type': 'application/json'}, {'contents': [{'parts': [{'text': 'hi'}]}]}))

# Groq
grq = env.get('GROQ_API_KEY')
for m in ['qwen/qwen3.8-27b', 'openai/gpt-oss-120b']:
    tests.append(('Groq LPU', m, 'https://api.groq.com/openai/v1/chat/completions', {'Authorization': f'Bearer {grq}', 'Content-Type': 'application/json', 'User-Agent': 'curl/8.4.0'}, {'model': m, 'messages': [{'role': 'user', 'content': 'hi'}], 'max_tokens': 10}))

# NVIDIA
nvd = env.get('NVIDIA_API_KEY')
for m in ['nvidia/nemotron-3.5-lightning-30b-a3b', 'nvidia/nemotron-3.5-super-vl-120b-a12b', 'minimaxai/minimax-m3.1-flash', 'mistralai/mistral-large-4-1t-a52b']:
    tests.append(('NVIDIA NIM', m, 'https://integrate.api.nvidia.com/v1/chat/completions', {'Authorization': f'Bearer {nvd}', 'Content-Type': 'application/json', 'User-Agent': 'curl/8.4.0'}, {'model': m, 'messages': [{'role': 'user', 'content': 'hi'}], 'max_tokens': 10}))

# Cohere
coh = env.get('COHERE_API_KEY')
for m in ['command-a-03-2025', 'command-r-plus-08-2024', 'command-r-08-2024', 'command-a-reasoning-08-2025', 'command-a-plus-05-2026', 'north-mini-code']:
    tests.append(('Cohere API', m, 'https://api.cohere.com/v2/chat', {'Authorization': f'Bearer {coh}', 'Content-Type': 'application/json', 'User-Agent': 'curl/8.4.0'}, {'model': m, 'messages': [{'role': 'user', 'content': 'hi'}]}))

# Intern-AI
int_k = env.get('INTERN_API_KEY')
tests.append(('Intern-AI', 'deepseek-v4.1-flash-1017', 'https://discovery-api.intern-ai.org.cn/v1/chat/completions', {'Authorization': f'Bearer {int_k}', 'Content-Type': 'application/json', 'User-Agent': 'curl/8.4.0'}, {'model': 'deepseek-v4.1-flash-1017', 'messages': [{'role': 'user', 'content': 'hi'}], 'max_tokens': 10}))

# OpenRouter
orp = env.get('OPENROUTER_API_KEY')
tests.append(('OpenRouter', 'nemotron-3-ultra-550b:free', 'https://openrouter.ai/api/v1/chat/completions', {'Authorization': f'Bearer {orp}', 'Content-Type': 'application/json', 'User-Agent': 'curl/8.4.0'}, {'model': 'nvidia/nemotron-3-ultra-550b-a55b:free', 'messages': [{'role': 'user', 'content': 'hi'}], 'max_tokens': 10}))

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print(f"Checking {len(tests)} models across all remaining active providers...\n")
pass_count = 0
fail_count = 0
for prov, m, url, hdrs, payload in tests:
    t0 = time.time()
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=hdrs)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
            dt = time.time() - t0
            print(f"PASS | {prov:<15s} | {m:<38s} | {dt:.2f}s")
            pass_count += 1
    except Exception as e:
        dt = time.time() - t0
        print(f"FAIL | {prov:<15s} | {m:<38s} | {dt:.2f}s | {e}")
        fail_count += 1

print(f"\nAudit complete: {pass_count} passed, {fail_count} failed out of {len(tests)} tested.")

