import json
import urllib.request
import urllib.error
from pathlib import Path
from google.oauth2 import service_account
import google.auth.transport.requests

ROOT = Path(__file__).resolve().parent.parent
sa_path = str(ROOT / "vertex_service_account.json")

def get_token():
    creds = service_account.Credentials.from_service_account_file(
        sa_path,
        scopes=["https://www.googleapis.com/auth/cloud-platform", "https://www.googleapis.com/auth/generative-language"]
    )
    auth_req = google.auth.transport.requests.Request()
    creds.refresh(auth_req)
    return creds.token

def test_url(name, url, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(f"[PASS] {name}: {str(data)[:200]}")
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="ignore")
        print(f"[FAIL] {name}: HTTP {e.code}: {err[:200]}")
    except Exception as e:
        print(f"[FAIL] {name}: {e}")

def main():
    token = get_token()
    print("Testing APIs with acquired token...")

    # 1. Test Generative Language API (Gemini developer API via Google Cloud OAuth)
    test_url("Generative Language Models List", "https://generativelanguage.googleapis.com/v1beta/models", token)

    # 2. Test Cloud Resource Manager (to check project access)
    test_url("Project Get", "https://cloudresourcemanager.googleapis.com/v1/projects/eishkom", token)

    # 3. Test Service Usage (to see enabled services)
    test_url("Enabled Services", "https://serviceusage.googleapis.com/v1/projects/eishkom/services?filter=state:ENABLED", token)

    # 4. Test Vertex AI endpoints across locations
    for loc in ["us-central1", "us-east4", "europe-west1", "asia-southeast1"]:
        test_url(f"Vertex AI Endpoints ({loc})", f"https://{loc}-aiplatform.googleapis.com/v1/projects/eishkom/locations/{loc}/endpoints", token)

if __name__ == "__main__":
    main()

