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

sys.path.insert(0, str(ROOT_DIR / "stage-2"))
from run_stage2_fleet import extract_json_safely, auto_repair_record

SYSTEM_PROMPT = (
    "You are an expert South African CAPS physics teacher. "
    "Output raw JSON starting with { and ending with } immediately. "
    "Do NOT write any text before or after the JSON. "
    "All your reasoning must go inside the 'reasoning' fields of assistant messages."
)

def call_intern_deepseek_optimized(prompt):
    url = f"{INTERN_BASE_URL}/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {INTERN_KEY}",
        "User-Agent": "curl/8.4.0"
    }
    payload = {
        "model": "deepseek-v4.1-flash-1017",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 3000
    }
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                choice = data["choices"][0]["message"]
                content = choice.get("content") or choice.get("reasoning_content") or ""
                if content:
                    return content
        except urllib.error.HTTPError as he:
            if he.code == 429:
                wait_sec = 5.0 * (attempt + 1)
                print(f"[Intern-AI DeepSeek] 429 rate limit hit. Sleeping {wait_sec}s (attempt {attempt+1}/4)...")
                time.sleep(wait_sec)
            else:
                time.sleep(2.0)
        except Exception as e:
            print(f"[Intern-AI DeepSeek] Error: {e}. Retrying...")
            time.sleep(3.0)
    raise RuntimeError("Intern-AI DeepSeek failed after 4 attempts")

test_prompt = """CRITICAL: START YOUR RESPONSE WITH { IMMEDIATELY. NO PREAMBLE TEXT.
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

print("Testing call_intern_deepseek_optimized...")
t0 = time.time()
resp = call_intern_deepseek_optimized(test_prompt)
dt = time.time() - t0
print(f"Success in {dt:.2f}s! ({len(resp)} chars)")
parsed = extract_json_safely(resp)
print("Parsed JSON successfully! Keys:", list(parsed.keys()))
print("Done!")

