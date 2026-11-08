import json
import urllib.request
from pathlib import Path

# Load .env
env_file = Path(".env")
keys = {}
for line in env_file.read_text(encoding="utf-8").splitlines():
    if "=" in line and not line.startswith("#"):
        k, v = line.split("=", 1)
        keys[k.strip()] = v.strip().strip("'\"")

gemini_key = keys.get("GEMINI_API_KEY", "")

# Query models
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={gemini_key}"
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        models = [m["name"].replace("models/", "") for m in data.get("models", [])]
        print(f"Total available models: {len(models)}")
        # Look for 3.6, 3.8, flash, etc.
        matching = [m for m in models if any(x in m for x in ["3.6", "3.8", "3.5", "3.1", "flash", "gemini-3"])]
        print("Matching models:", matching[:30])
except Exception as e:
    print("Error listing models:", e)

# Test specific model IDs:
for test_id in ["gemini-3.8-flash", "gemini-3.6-flash", "gemini-3.5-flash-lite", "gemini-3.1-flash-lite"]:
    try:
        url2 = f"https://generativelanguage.googleapis.com/v1beta/models/{test_id}:generateContent?key={gemini_key}"
        payload = {"contents": [{"parts": [{"text": "Hello"}]}]}
        req2 = urllib.request.Request(url2, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req2, timeout=10) as resp2:
            print(f"Test model '{test_id}': SUCCESS")
    except Exception as e:
        print(f"Test model '{test_id}': FAILED ({e})")

