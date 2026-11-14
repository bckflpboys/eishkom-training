import json
import time
import urllib.request
import urllib.error
from pathlib import Path
from google.oauth2 import service_account
import google.auth.transport.requests

ROOT = Path(__file__).resolve().parent.parent
sa_path = str(ROOT / "vertex_service_account.json")

def test_vertex_model(token, project_id, location, model, prompt="Say 'ready' and nothing else."):
    url = f"https://{location}-aiplatform.googleapis.com/v1/projects/{project_id}/locations/{location}/publishers/google/models/{model}:generateContent"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": 30, "temperature": 0.2}
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers)
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            elapsed = time.time() - t0
            res = json.loads(resp.read().decode("utf-8"))
            parts = res.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])
            content = parts[0].get("text", "").strip() if parts else ""
            return True, content, elapsed, None
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="ignore")
        return False, None, time.time() - t0, f"HTTP {e.code}: {err_body[:200]}"
    except Exception as e:
        return False, None, time.time() - t0, str(e)

def main():
    print("Testing Vertex AI service account...")
    creds = service_account.Credentials.from_service_account_file(
        sa_path,
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    auth_req = google.auth.transport.requests.Request()
    creds.refresh(auth_req)
    token = creds.token
    print(f"Auth Success! Token acquired (first 10 chars: {token[:10]}...)")

    models_to_test = [
        "gemini-2.5-flash",
        "gemini-2.5-pro",
        "gemini-2.0-flash",
        "gemini-2.0-flash-exp",
        "gemini-1.5-flash",
        "gemini-1.5-flash-002",
        "gemini-1.5-pro",
        "gemini-1.5-pro-002",
    ]

    for m in models_to_test:
        ok, res, el, err = test_vertex_model(token, "eishkom", "us-central1", m)
        if ok:
            print(f"  [PASS] Vertex AI / {m} ({el:.2f}s): {res}")
        else:
            print(f"  [FAIL] Vertex AI / {m} ({el:.2f}s): {err}")

if __name__ == "__main__":
    main()

