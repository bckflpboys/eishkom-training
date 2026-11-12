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
INTERN_KEY = ENV_KEYS.get("INTERN_API_KEY", "")
INTERN_BASE_URL = ENV_KEYS.get("INTERN_BASE_URL", "https://discovery-api.intern-ai.org.cn/v1")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = f"{INTERN_BASE_URL}/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {INTERN_KEY}",
    "User-Agent": "curl/8.4.0"
}

# Test 1: Standard with concise prompt
payload1 = {
    "model": "deepseek-v4.1-flash-1017",
    "messages": [
        {"role": "system", "content": "You are a CAPS physics teacher. Output ONLY valid JSON immediately. Keep internal reasoning concise."},
        {"role": "user", "content": "Return JSON with final_answer for: What is Newton's second law formula?"}
    ],
    "temperature": 0.1,
    "max_tokens": 1500
}

# Test 2: Checking if 429 clears after 3 seconds
time.sleep(3)
t0 = time.time()
try:
    req = urllib.request.Request(url, data=json.dumps(payload1).encode("utf-8"), headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
        dt = time.time() - t0
        data = json.loads(resp.read().decode("utf-8"))
        msg = data["choices"][0]["message"]
        print(f"Test 1: Success in {dt:.2f}s! content: {len(msg.get('content') or '')} chars, reasoning: {len(msg.get('reasoning_content') or '')} chars")
        print("Output:", (msg.get("content") or msg.get("reasoning_content"))[:120])
except Exception as e:
    print(f"Test 1: Error: {e}")

