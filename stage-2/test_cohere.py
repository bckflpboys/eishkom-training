import urllib.request
import json
import urllib.error

key = "iNTzE94EZk0t0ZGlgAudCE3eOHgqVHsL4KKX05Kh"

# 1. List models
print("=== 1. LISTING COHERE MODELS ===")
url_m = "https://api.cohere.com/v1/models"
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json",
    "User-Agent": "curl/8.4.0"
}

try:
    req = urllib.request.Request(url_m, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as r:
        data = json.loads(r.read().decode())
        models = data.get("models", [])
        print(f"Total models available on Cohere: {len(models)}")
        for m in sorted([m.get("name") for m in models if m.get("name")]):
            print(f"  - {m}")
except urllib.error.HTTPError as he:
    print(f"HTTP Error {he.code}: {he.read().decode()[:300]}")
except Exception as e:
    print(f"Error: {e}")

