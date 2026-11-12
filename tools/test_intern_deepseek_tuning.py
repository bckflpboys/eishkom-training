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

print(f"INTERN_BASE_URL: {INTERN_BASE_URL}")
print(f"INTERN_KEY present: {bool(INTERN_KEY)}")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

prompt = """CRITICAL: START YOUR RESPONSE WITH { IMMEDIATELY. NO PREAMBLE TEXT.
Generate a valid JSON object:
{
  "messages": [
    {"role": "user", "content": "How do I calculate kinetic energy of a 2kg mass moving at 3m/s?"},
    {"role": "assistant", "reasoning": "Identify the standard formula E_k = 0.5 * m * v^2 and substitute values.", "content": "The kinetic energy is $E_k = \\frac{1}{2}mv^2 = \\frac{1}{2}(2)(3)^2 = 9\\text{ J}$."}
  ],
  "meta": {
    "strategy_used": "direct_explanation",
    "final_answer": "9 J"
  }
}"""

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {INTERN_KEY}",
    "User-Agent": "curl/8.4.0"
}

payload = {
    "model": "deepseek-v4.1-flash-1017",
    "messages": [
        {"role": "system", "content": "You are an expert CAPS physics teacher. Output raw JSON starting with {"},
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.2,
    "max_tokens": 3000
}

url = f"{INTERN_BASE_URL}/chat/completions"

for i in range(3):
    t0 = time.time()
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=40) as resp:
            raw = resp.read().decode("utf-8")
            dt = time.time() - t0
            data = json.loads(raw)
            choice = data["choices"][0]["message"]
            content = choice.get("content") or ""
            reasoning = choice.get("reasoning_content") or ""
            print(f"Attempt {i+1}: Success in {dt:.2f}s | content_len={len(content)} | reasoning_len={len(reasoning)}")
            if content:
                print("Content preview:", content[:150].replace('\n', ' '))
            elif reasoning:
                print("Reasoning preview:", reasoning[:150].replace('\n', ' '))
    except Exception as e:
        dt = time.time() - t0
        print(f"Attempt {i+1}: Failed in {dt:.2f}s | Error: {e}")
    time.sleep(1)

