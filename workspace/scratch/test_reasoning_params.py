import os
import json
import urllib.request
from pathlib import Path

# Load .env
env_file = Path(".env")
keys = {}
if env_file.exists():
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            keys[k.strip()] = v.strip().strip("'\"")

openai_key = keys.get("OPENAI_API_KEY", "")
gemini_key1 = keys.get("GEMINI_API_KEY", "")
gemini_key2 = keys.get("GEMINI_API_KEY_2", "")
openrouter_key = keys.get("OPENROUTER_API_KEY", "")

# 1. Test OpenAI gpt-6-luna with reasoning_effort
print("=== Testing OpenAI gpt-6-luna reasoning_effort ===")
for effort in ["high", "xhigh"]:
    try:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {openai_key}", "Content-Type": "application/json"}
        payload = {
            "model": "gpt-6-luna",
            "messages": [{"role": "user", "content": "Respond with OK"}],
            "max_completion_tokens": 50,
            "reasoning_effort": effort
        }
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(f"OpenAI reasoning_effort={effort} SUCCESS:", data["choices"][0]["message"].get("content"))
    except Exception as e:
        print(f"OpenAI reasoning_effort={effort} FAILED:", e)

# 2. Test Google AI Studio max thinking budget
print("\n=== Testing Google AI Studio Gemini 3.5 / 3.1 Thinking ===")
for model in ["gemini-3.5-flash-lite", "gemini-3.1-flash-lite"]:
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={gemini_key1}"
        payload = {
            "contents": [{"parts": [{"text": "Respond with OK"}]}],
            "generationConfig": {
                "temperature": 0.4,
                "maxOutputTokens": 100,
                "thinkingConfig": {
                    "thinkingBudget": 24576
                }
            }
        }
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(f"Gemini {model} with thinkingBudget=24576 SUCCESS:", data["candidates"][0]["content"]["parts"][0]["text"])
    except Exception as e:
        print(f"Gemini {model} with thinkingBudget=24576 FAILED:", e)

# 3. Test OpenRouter reasoning parameter
print("\n=== Testing OpenRouter reasoning ===")
try:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {openrouter_key}", "Content-Type": "application/json"}
    payload = {
        "model": "nvidia/nemotron-3-ultra-550b-a55b:free",
        "messages": [{"role": "user", "content": "Respond with OK"}],
        "max_tokens": 100,
        "reasoning": {"effort": "high"}
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        print("OpenRouter with reasoning={'effort': 'high'} SUCCESS:", data["choices"][0]["message"].get("content"))
except Exception as e:
    print("OpenRouter with reasoning failed:", e)
