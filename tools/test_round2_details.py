import urllib.request
import urllib.error
import json
import time

def call_chat(url, key, model, payload_extra=None):
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": "Say 'ready' and nothing else."}],
        "max_tokens": 40
    }
    if payload_extra:
        payload.update(payload_extra)
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
            return True, content.strip(), time.time() - t0, None
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="ignore")
        return False, None, time.time() - t0, f"HTTP {e.code}: {err[:200]}"
    except Exception as e:
        return False, None, time.time() - t0, str(e)

def main():
    print("=" * 70)
    print("DETAILED VERIFICATION FOR NEW MODELS")
    print("=" * 70)

    # 1. VERCEL AI GATEWAY
    print("\n--- VERCEL AI GATEWAY (https://ai-gateway.vercel.sh/v1) ---")
    v_key = "vck_7WpGr9GxO4bGXatlrUv4GFZjYWMMXPOmWcFe1QQPyMqJSxEyhd4I83HZ"
    v_url = "https://ai-gateway.vercel.sh/v1/chat/completions"
    v_models = [
        "baseten/mammoth-1",
        "baseten/elephant-1",
        "nvidia/nemotron-3.5-super-vl",
        "openai/gpt-oss-120b",
        "nvidia/nemotron-3-ultra-550b-a55b",
    ]
    for m in v_models:
        ok, res, el, err = call_chat(v_url, v_key, m)
        if ok:
            print(f"  [PASS] Vercel / {m} ({el:.2f}s): {res[:60]}")
        else:
            print(f"  [FAIL] Vercel / {m} ({el:.2f}s): {err}")

    # 2. ALIBABA MODEL STUDIO
    print("\n--- ALIBABA MODEL STUDIO (DASHSCOPE) ---")
    ali_key = "sk-ws-H.DIEIEIL.hoB5.MEYCIQCfe21U-TRiPWNDVnLdSBcycVdTOZLdSN7JBHzYC_ZBowIhAIrvSY-_6p6QnNqB8RoX67dqzHk6SfIEnd2vlpKNn4Bj"
    ali_url = "https://ws-kvneg1w4j01n4v80.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1/chat/completions"
    
    # Test kimi-k3.1-pro without temperature
    ok, res, el, err = call_chat(ali_url, ali_key, "kimi-k3.1-pro")
    if ok:
        print(f"  [PASS] DashScope / kimi-k3.1-pro ({el:.2f}s): {res[:60]}")
    else:
        print(f"  [FAIL] DashScope / kimi-k3.1-pro ({el:.2f}s): {err}")

    # Test qwen3.8-max with extra_body enable_thinking
    ok, res, el, err = call_chat(ali_url, ali_key, "qwen3.8-max", payload_extra={"extra_body": {"enable_thinking": True}})
    if ok:
        print(f"  [PASS] DashScope / qwen3.8-max ({el:.2f}s): {res[:60]}")
    else:
        print(f"  [FAIL] DashScope / qwen3.8-max ({el:.2f}s): {err}")

    # 3. TOKEN LAB AMD
    print("\n--- TOKEN LAB AMD (https://api.tokenlab.amd.com/v1) ---")
    tl_key = "tl-d83428d3bc8ce667bf6203ece678de835bca878409de6211"
    tl_url = "https://api.tokenlab.amd.com/v1/chat/completions"
    tl_models = ["DeepSeek-V4-Flash", "DeepSeek-V4.1-Flash", "Gemma-4-31B-IT", "Qwen3.8-27B"]
    for m in tl_models:
        ok, res, el, err = call_chat(tl_url, tl_key, m)
        if ok:
            print(f"  [PASS] Token Lab / {m} ({el:.2f}s): {res[:60]}")
        else:
            print(f"  [FAIL] Token Lab / {m} ({el:.2f}s): {err}")
        time.sleep(1)

    # 4. LLM7.IO
    print("\n--- LLM7.IO (https://api.llm7.io/v1) ---")
    llm7_key = "I9jr5jLACtJ18Iue3kV/sI1H7srYtAEGVqJZYAM97vIq3sAr0YRxQ3Zn6YPR5SYz6zXHDc2HGBLyHqLLF/T2cYCIFnopb3bLntHqYBkgAvfzBq1w9D3ireYkOTlxDpozvhJurDjmFiO4WSOJ"
    llm7_url = "https://api.llm7.io/v1/chat/completions"
    for m in ["default", "deepseek-v4.1-flash", "glm-5.3-flash", "mimo-v2.6-flash", "gpt-6-luna", "kimi-k3.1-pro"]:
        ok, res, el, err = call_chat(llm7_url, llm7_key, m)
        if ok:
            print(f"  [PASS] LLM7 / {m} ({el:.2f}s): {res[:60]}")
        else:
            print(f"  [FAIL] LLM7 / {m} ({el:.2f}s): {err}")
        time.sleep(1)

if __name__ == "__main__":
    main()

