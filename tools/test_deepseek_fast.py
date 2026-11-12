import os
import sys
import json
import time
import ssl
import urllib.request
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

def load_env():
    keys = {}
    for env_path in [ROOT_DIR / ".env", ROOT_DIR / "sa-tutor-kit" / "sa-tutor-kit" / ".env"]:
        if env_path.exists():
            for line in env_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if "=" in line and not line.startswith("#"):
                    k, v = line.split("=", 1)
                    keys[k.strip()] = v.strip().strip("'\"")
    return keys

ENV_KEYS = load_env()
OPENROUTER_KEY = ENV_KEYS.get("OPENROUTER_API_KEY", "")
INTERN_KEY = ENV_KEYS.get("INTERN_API_KEY", "")
INTERN_BASE_URL = ENV_KEYS.get("INTERN_BASE_URL", "https://discovery-api.intern-ai.org.cn/v1")

print(f"OpenRouter Key present: {bool(OPENROUTER_KEY)}")
print(f"Intern Key present: {bool(INTERN_KEY)}")

# Test OpenRouter DeepSeek
if OPENROUTER_KEY:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "HTTP-Referer": "https://eishkom.ai",
        "X-Title": "Eishkom AI Tutor Stage 2"
    }
    payload = {
        "model": "deepseek/deepseek-chat",
        "messages": [
            {"role": "user", "content": "Respond with a single raw JSON object: {\"status\": \"ok\", \"model\": \"deepseek-chat\"}"}
        ],
        "temperature": 0.1,
        "max_tokens": 150
    }
    t0 = time.time()
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            elapsed = time.time() - t0
            choice = data["choices"][0]["message"]
            print(f"[OpenRouter DeepSeek] SUCCESS in {elapsed:.2f}s! Reply:\n{choice.get('content')}")
    except Exception as e:
        print(f"[OpenRouter DeepSeek] ERROR: {e}")

# Test Intern-AI DeepSeek
if INTERN_KEY:
    _ssl_ctx = ssl.create_default_context()
    _ssl_ctx.check_hostname = False
    _ssl_ctx.verify_mode = ssl.CERT_NONE
    url = f"{INTERN_BASE_URL}/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {INTERN_KEY}",
        "User-Agent": "curl/8.4.0"
    }
    payload = {
        "model": "deepseek-v4.1-flash-1017",
        "messages": [
            {"role": "user", "content": "Respond with a single raw JSON object: {\"status\": \"ok\", \"model\": \"deepseek-v4.1-flash-1017\"}"}
        ],
        "temperature": 0.1,
        "max_tokens": 150
    }
    t0 = time.time()
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req, context=_ssl_ctx, timeout=35) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            elapsed = time.time() - t0
            choice = data["choices"][0]["message"]
            content = choice.get("content") or choice.get("reasoning_content") or ""
            print(f"[Intern-AI DeepSeek] SUCCESS in {elapsed:.2f}s! Reply:\n{content}")
    except Exception as e:
        print(f"[Intern-AI DeepSeek] ERROR: {e}")

