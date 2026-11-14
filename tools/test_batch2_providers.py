"""Test Batch 2 of newly provided LLM Providers:
1. Google Gemini Platform API (AQ.Ab8RN6KKtJQ-...)
2. Alibaba Model Studio (DashScope MaaS)
3. TokenHarbour (tokenharbour.ai)
4. llm7.io
5. Vercel API Gateway
6. Ollama.com Cloud
7. KiloCode (kilo.ai)
8. Token Lab AMD (api.tokenlab.amd.com)
"""

import os
import json
import time
import urllib.request
import urllib.error
from pathlib import Path

def test_chat_completion(base_url, api_key, model, extra_headers=None, extra_body=None, prompt="Say 'ready' and nothing else."):
    url = f"{base_url.rstrip('/')}/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    if extra_headers:
        headers.update(extra_headers)

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 40,
        "temperature": 0.2
    }
    if extra_body:
        payload.update(extra_body)

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers)
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            elapsed = time.time() - t0
            res = json.loads(resp.read().decode("utf-8"))
            content = res.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
            return True, content, elapsed, None
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="ignore")
        return False, None, time.time() - t0, f"HTTP {e.code}: {err_body[:200]}"
    except Exception as e:
        return False, None, time.time() - t0, str(e)

def list_models(base_url, api_key, extra_headers=None):
    url = f"{base_url.rstrip('/')}/models"
    headers = {"Authorization": f"Bearer {api_key}"}
    if extra_headers:
        headers.update(extra_headers)
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if "data" in data:
                return [m.get("id") for m in data["data"]]
            elif isinstance(data, list):
                return [m.get("id") or m.get("name") for m in data]
            return list(data.keys())
    except Exception as e:
        return f"Error: {e}"

def test_gemini_platform(api_key, model="gemini-1.5-flash", prompt="Say 'ready' and nothing else."):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": 30, "temperature": 0.2}
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers)
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            elapsed = time.time() - t0
            res = json.loads(resp.read().decode("utf-8"))
            text = res.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "").strip()
            return True, text, elapsed, None
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="ignore")
        return False, None, time.time() - t0, f"HTTP {e.code}: {err_body[:200]}"
    except Exception as e:
        return False, None, time.time() - t0, str(e)


def main():
    print("=" * 70)
    print("TESTING BATCH 2 PROVIDERS & MODELS")
    print("=" * 70)

    # 1. Gemini Platform API Key
    print("\n--- 1. GOOGLE GEMINI PLATFORM API ---")
    gemini_plat_key = "AQ.Ab8RN6KKtJQ-FGWyqeVyhaIzCVJZJo6q0-pd8L8-u3LgEGF9Cw"
    # List models available to this key:
    try:
        req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models?key={gemini_plat_key}")
        with urllib.request.urlopen(req, timeout=15) as resp:
            m_data = json.loads(resp.read().decode("utf-8"))
            plat_models = [m["name"].replace("models/", "") for m in m_data.get("models", [])]
            print(f"Total available models: {len(plat_models)}")
            sample_models = [m for m in plat_models if any(k in m for k in ["flash", "pro", "gemini-2", "hydrogen"])]
            print(f"Sample matching models: {sample_models[:10]}")
    except Exception as e:
        plat_models = []
        print(f"Error listing Gemini models: {e}")

    test_models_gem = ["gemini-1.5-flash", "gemini-2.0-flash-exp", "gemini-1.5-pro", "gemini-2.5-flash", "gemini-4-hydrogen", "gemini-3.8-flash"]
    for m in test_models_gem:
        ok, res, el, err = test_gemini_platform(gemini_plat_key, m)
        if ok:
            print(f"  [PASS] {m} ({el:.2f}s): {res}")
        else:
            print(f"  [FAIL] {m} ({el:.2f}s): {err}")

    # 2. Alibaba Model Studio
    print("\n--- 2. ALIBABA MODEL STUDIO (DASHSCOPE) ---")
    ali_key = "sk-ws-H.DIEIEIL.hoB5.MEYCIQCfe21U-TRiPWNDVnLdSBcycVdTOZLdSN7JBHzYC_ZBowIhAIrvSY-_6p6QnNqB8RoX67dqzHk6SfIEnd2vlpKNn4Bj"
    ali_base = "https://ws-kvneg1w4j01n4v80.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1"
    ali_models = list_models(ali_base, ali_key)
    print(f"Listed models from API: {ali_models}")
    for m in ["kimi-k3.1-pro", "qwen3.8-max", "qwen-max"]:
        ok, res, el, err = test_chat_completion(ali_base, ali_key, m)
        if ok:
            print(f"  [PASS] {m} ({el:.2f}s): {res[:60]}")
        else:
            print(f"  [FAIL] {m} ({el:.2f}s): {err}")

    # 3. TokenHarbour
    print("\n--- 3. TOKENHARBOUR (tokenharbour.ai) ---")
    th_key = "thk_live_nhOh6evR6RDNPUZ3lpqL08wS8fsQv_SiVbPkKNbfsa-p0qCk9qPNV2V6n3UG2Y1R"
    for th_base in ["https://api.tokenharbour.ai/v1", "https://api.tokenharbour.com/v1"]:
        th_models = list_models(th_base, th_key)
        print(f"Endpoint {th_base} models: {th_models}")
        if isinstance(th_models, list):
            for m in th_models[:5]:
                ok, res, el, err = test_chat_completion(th_base, th_key, m)
                if ok:
                    print(f"  [PASS] {m} ({el:.2f}s): {res[:60]}")
                else:
                    print(f"  [FAIL] {m} ({el:.2f}s): {err}")
            break

    # 4. LLM7.io
    print("\n--- 4. LLM7.IO ---")
    llm7_key = "I9jr5jLACtJ18Iue3kV/sI1H7srYtAEGVqJZYAM97vIq3sAr0YRxQ3Zn6YPR5SYz6zXHDc2HGBLyHqLLF/T2cYCIFnopb3bLntHqYBkgAvfzBq1w9D3ireYkOTlxDpozvhJurDjmFiO4WSOJ"
    llm7_base = "https://api.llm7.io/v1"
    llm7_models = list_models(llm7_base, llm7_key)
    print(f"Listed models: {llm7_models}")
    for m in ["default", "gpt-4o-mini", "claude-3-haiku", "gemini-flash"]:
        ok, res, el, err = test_chat_completion(llm7_base, llm7_key, m)
        if ok:
            print(f"  [PASS] {m} ({el:.2f}s): {res[:60]}")
        else:
            print(f"  [FAIL] {m} ({el:.2f}s): {err}")

    # 5. Token Lab AMD
    print("\n--- 5. TOKEN LAB AMD (api.tokenlab.amd.com) ---")
    tl_key = "tl-d83428d3bc8ce667bf6203ece678de835bca878409de6211"
    tl_base = "https://api.tokenlab.amd.com/v1"
    tl_models = list_models(tl_base, tl_key)
    print(f"Listed models: {tl_models}")
    for m in ["DeepSeek-V4-Flash", "DeepSeek-V4.1-Flash", "Clef"]:
        ok, res, el, err = test_chat_completion(tl_base, tl_key, m)
        if ok:
            print(f"  [PASS] {m} ({el:.2f}s): {res[:60]}")
        else:
            print(f"  [FAIL] {m} ({el:.2f}s): {err}")

    # 6. Ollama Cloud
    print("\n--- 6. OLLAMA.COM CLOUD ---")
    ollama_key = "d475f087e8e8496fb388c8e0bacb17aa.LkarbmW-pfn-_DVvU6yKIQSF"
    ollama_base = "https://ollama.com/v1"
    ollama_models = list_models(ollama_base, ollama_key)
    print(f"Listed models: {ollama_models}")
    for m in ["gemma4:31b", "gemma4:31b-cloud", "glm-5.3-flash:cloud", "deepseek-v4.1-flash:1017-cloud", "deepseek-v4.1-flash"]:
        ok, res, el, err = test_chat_completion(ollama_base, ollama_key, m)
        if ok:
            print(f"  [PASS] {m} ({el:.2f}s): {res[:60]}")
        else:
            print(f"  [FAIL] {m} ({el:.2f}s): {err}")

    # 7. Vercel Gateway
    print("\n--- 7. VERCEL API GATEWAY ---")
    vercel_key = "vck_7WpGr9GxO4bGXatlrUv4GFZjYWMMXPOmWcFe1QQPyMqJSxEyhd4I83HZ"
    for v_base in ["https://api.gateway.vercel.com/v1", "https://gateway.ai.cloudflare.com/v1", "https://ai-gateway.vercel.sh/v1", "https://api.vercel.com/v1"]:
        print(f"Testing endpoint {v_base}...")
        v_models = list_models(v_base, vercel_key)
        print(f"  Result: {v_models}")

    # 8. KiloCode
    print("\n--- 8. KILOCODE (kilo.ai) ---")
    kilo_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbnYiOiJwcm9kdWN0aW9uIiwia2lsb1VzZXJJZCI6IjIyOGFkZjc2LTE4NDQtNDE3OC1iODIwLTFlNjZiYTYyYTM5YSIsImFwaVRva2VuUGVwcGVyIjpudWxsLCJ2ZXJzaW9uIjozLCJpYXQiOjE3OTQ2MDUxNzQsImV4cCI6MTk1MjI4NTE3NH0.ljNBD8bJH2O5hOasmTTdExy4OYcbnkkjxCYCMSJrmEU"
    for k_base in ["https://api.kilo.ai/v1", "https://gateway.kilo.ai/v1", "https://kilo.ai/api/v1"]:
        print(f"Testing endpoint {k_base}...")
        k_models = list_models(k_base, kilo_key)
        print(f"  Result: {k_models}")

if __name__ == "__main__":
    main()

