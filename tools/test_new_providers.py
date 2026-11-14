"""Test all newly provided API providers and models:
1. Vertex AI (eishkom project with service account)
2. Refuseless.com
3. APInex.bond
4. APMix.ai
"""

import os
import json
import time
import urllib.request
import urllib.error
from pathlib import Path
from google.oauth2 import service_account
import google.auth.transport.requests

ROOT = Path(__file__).resolve().parent.parent

def test_openai_endpoint(base_url, api_key, model, prompt="Say 'ready' and nothing else."):
    """Test an OpenAI-compatible /v1/chat/completions endpoint."""
    url = f"{base_url.rstrip('/')}/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 50,
        "temperature": 0.3
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers)
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            elapsed = time.time() - t0
            res = json.loads(resp.read().decode("utf-8"))
            content = res.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
            return True, content, elapsed, None
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="ignore")
        return False, None, time.time() - t0, f"HTTP {e.code}: {err_body[:200]}"
    except Exception as e:
        return False, None, time.time() - t0, str(e)

def list_openai_models(base_url, api_key):
    """Query /v1/models."""
    url = f"{base_url.rstrip('/')}/models"
    headers = {"Authorization": f"Bearer {api_key}"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if "data" in data:
                return [m.get("id") for m in data["data"]]
            return []
    except Exception as e:
        return f"Error listing models: {e}"

def test_vertex(sa_path, project_id, location, model, prompt="Say 'ready' and nothing else."):
    """Test Vertex AI generateContent."""
    creds = service_account.Credentials.from_service_account_file(
        sa_path,
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    auth_req = google.auth.transport.requests.Request()
    creds.refresh(auth_req)
    token = creds.token
    
    url = f"https://{location}-aiplatform.googleapis.com/v1/projects/{project_id}/locations/{location}/publishers/google/models/{model}:generateContent"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": 50, "temperature": 0.2}
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
    print("=" * 70)
    print("TESTING NEW PROVIDERS & MODELS")
    print("=" * 70)

    # 1. REFUSELESS
    print("\n--- 1. REFUSELESS (https://api.refuseless.com/v1) ---")
    refuseless_key = os.environ.get("REFUSELESS_API_KEY", "abl_7c474ce1e1327274b559c38e569a4628b318c052ee5ab478")
    refuseless_models = list_openai_models("https://api.refuseless.com/v1", refuseless_key)
    print(f"Listed models from API: {refuseless_models}")
    models_to_test = ["deepseek-v4.1-flash-abliterated-free", "glm-5.3-abliterated"]
    if isinstance(refuseless_models, list):
        for m in refuseless_models:
            if m not in models_to_test:
                models_to_test.append(m)
    for m in models_to_test:
        ok, res, el, err = test_openai_endpoint("https://api.refuseless.com/v1", refuseless_key, m)
        if ok:
            print(f"  [PASS] {m} ({el:.2f}s): {res[:60]}")
        else:
            print(f"  [FAIL] {m} ({el:.2f}s): {err}")

    # 2. APINEX
    print("\n--- 2. APINEX (https://api.apinex.bond/v1) ---")
    apinex_key = os.environ.get("APINEX_API_KEY", "sk-apxa989180905641e7065d9d54287436797ae6a8cab8b890be")
    apinex_listed = list_openai_models("https://api.apinex.bond/v1", apinex_key)
    print(f"Listed models from API: {apinex_listed}")
    user_apinex_models = [
        "free/mimo-v2.6-pro",
        "free/qwen-3.8-max",
        "free/kimi-k3",
        "free/deepseek-v4.1-flash",
        "free/glm-5.3-flash",
        "free/deepseek-v4-pro-0813",
        "free/deepseek-v4-flash-0731",
        "free/muse-spark-1.3",
        "free/minimax-m3.1-flash",
        "free/gpt-6-luna",
    ]
    models_to_test_apx = list(user_apinex_models)
    if isinstance(apinex_listed, list):
        for m in apinex_listed:
            if m not in models_to_test_apx:
                models_to_test_apx.append(m)
    for m in models_to_test_apx:
        ok, res, el, err = test_openai_endpoint("https://api.apinex.bond/v1", apinex_key, m)
        if ok:
            print(f"  [PASS] {m} ({el:.2f}s): {res[:60]}")
        else:
            print(f"  [FAIL] {m} ({el:.2f}s): {err}")

    # 3. APMIX
    print("\n--- 3. APMIX (https://api.apmix.ai/v1) ---")
    apmix_key = os.environ.get("APMIX_API_KEY", "apx_live_FXywyzcZdig3imjqxQIJT5QJgeTCz1Y0YUK3uZSJ")
    apmix_listed = list_openai_models("https://api.apmix.ai/v1", apmix_key)
    print(f"Listed models from API: {apmix_listed}")
    user_apmix_models = [
        "deepseek-v4.1-flash-1017-free",
        "nemotron-3.5-super-vl-free",
        "gpt-5.6-luna",
    ]
    models_to_test_apmix = list(user_apmix_models)
    if isinstance(apmix_listed, list):
        for m in apmix_listed:
            if m not in models_to_test_apmix:
                models_to_test_apmix.append(m)
    for m in models_to_test_apmix:
        ok, res, el, err = test_openai_endpoint("https://api.apmix.ai/v1", apmix_key, m)
        if ok:
            print(f"  [PASS] {m} ({el:.2f}s): {res[:60]}")
        else:
            print(f"  [FAIL] {m} ({el:.2f}s): {err}")

    # 4. VERTEX AI
    print("\n--- 4. VERTEX AI (Google Cloud Project: eishkom) ---")
    sa_path = str(ROOT / "vertex_service_account.json")
    if not os.path.exists(sa_path):
        print(f"Error: {sa_path} not found!")
        return
    
    vertex_models = [
        "gemini-2.5-flash",
        "gemini-2.0-flash",
        "gemini-2.0-flash-exp",
        "gemini-1.5-flash",
        "gemini-1.5-flash-002",
        "gemini-1.5-pro",
        "gemini-1.5-pro-002",
    ]
    for m in vertex_models:
        ok, res, el, err = test_vertex(sa_path, "eishkom", "us-central1", m)
        if ok:
            print(f"  [PASS] {m} ({el:.2f}s): {res[:60]}")
        else:
            print(f"  [FAIL] {m} ({el:.2f}s): {err}")

if __name__ == "__main__":
    main()

