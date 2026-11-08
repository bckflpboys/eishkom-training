import urllib.request
import json
import ssl

ctx = ssl.create_default_context()

def test_chat(base_url, api_key, model, provider_name):
    url = f"{base_url}/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": "Hello! Reply with exactly: READY"}],
        "max_tokens": 30
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            msg = data["choices"][0]["message"]["content"]
            print(f"[{provider_name}] {model}: SUCCESS -> {msg.strip()[:60]}")
            return True
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='ignore')[:150]
        print(f"[{provider_name}] {model}: HTTP {e.code} -> {body}")
        return False
    except Exception as e:
        print(f"[{provider_name}] {model}: ERROR -> {e}")
        return False

print("--- Testing OpenAI ---")
openai_key = "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"
test_chat("https://api.openai.com/v1", openai_key, "gpt-6-luna", "OpenAI")

print("\n--- Testing Intern-AI ---")
intern_key = "sk-7394079193455baf4de2616444aa1523f92883ca8e3720815d7022d3bb4abe90"
intern_models = ["deepseek-v4.1-flash-1017", "glm-5.3", "Agents-A1", "Atria-Dawn", "Sage-A1.5"]
for m in intern_models:
    test_chat("https://discovery-api.intern-ai.org.cn/v1", intern_key, m, "Intern-AI")

print("\n--- Testing OpenRouter Models ---")
openrouter_key = "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"
openrouter_models = [
    "nvidia/nemotron-3-ultra-550b-a55b:free",
    "nvidia/nemotron-3.5-super-vl:free",
    "dots-studio/dots-3-note-preview:free"
]
for m in openrouter_models:
    test_chat("https://openrouter.ai/api/v1", openrouter_key, m, "OpenRouter")

