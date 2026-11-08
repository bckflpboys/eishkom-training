import urllib.request
import json

api_key = "AQ.Ab8RN6KWottlmFmKypg9atadZdfk9IVDF02wuF0hzsrZ1l6CmQ"

models_to_test = [
    "models/gemma-4-26b-a4b-it",
    "models/gemma-4-31b-it",
    "models/gemini-2.5-flash",
    "models/gemini-2.5-flash-lite",
    "models/gemini-flash-latest"
]

for m in models_to_test:
    url = f"https://generativelanguage.googleapis.com/v1beta/{m}:generateContent?key={api_key}"
    payload = {"contents": [{"parts": [{"text": "Say hello in one word"}]}]}
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            ans = res["candidates"][0]["content"]["parts"][0]["text"].strip()
            print(f"[OK] {m} -> {ans}")
    except Exception as e:
        status = getattr(e, 'code', 'error')
        print(f"[FAIL] {m} -> HTTP {status}: {e}")

