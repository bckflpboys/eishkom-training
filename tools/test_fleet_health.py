import functools
import json
import os
import pathlib
import sys
import time
import urllib.request
import urllib.error

print = functools.partial(print, flush=True)

# Load .env keys
env_file = pathlib.Path(".env")
keys = {}
if env_file.exists():
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            keys[k.strip()] = v.strip().strip("'\"")

def check_endpoint(provider_name, model_name, url, headers, payload):
    t0 = time.time()
    headers = dict(headers)
    headers["User-Agent"] = "curl/8.4.0"
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            elapsed = time.time() - t0
            content = ""
            if "choices" in data and len(data["choices"]) > 0:
                c0 = data["choices"][0]
                if isinstance(c0, dict):
                    msg = c0.get("message", {})
                    content = msg.get("content") or msg.get("reasoning_content") or ""
            elif "message" in data and "content" in data["message"]:
                c_list = data["message"]["content"]
                if isinstance(c_list, list) and len(c_list) > 0:
                    content = c_list[0].get("text") or c_list[0].get("thinking") or ""
            status_desc = f"OK ({elapsed:.2f}s) -> '{content[:40].strip()}...'" if content else f"OK ({elapsed:.2f}s)"
            return True, status_desc
    except urllib.error.HTTPError as he:
        elapsed = time.time() - t0
        err_body = he.read().decode("utf-8", errors="replace")[:120]
        return False, f"HTTP {he.code} ({elapsed:.2f}s): {err_body}"
    except Exception as e:
        elapsed = time.time() - t0
        return False, f"ERR ({elapsed:.2f}s): {e}"

print("=" * 80)
print("EISHKOM AI FLEET HEALTH & API PROVIDER LIVE AUDIT (CORRECT .ENV KEYS)")
print("=" * 80)

# 1. Alibaba DashScope
ali_key = keys.get("DASHSCOPE_API_KEY")
print("\n[1] Alibaba DashScope (Sampling 4/14):")
for m in ["qwen3.8-flash", "deepseek-v4.1-flash", "kimi-k3", "deepseek-v4-pro-0813"]:
    payload = {"model": m, "messages": [{"role": "user", "content": "Say 'OK'"}]}
    if "kimi" not in m:
        payload["temperature"] = 0.2
    ok, msg = check_endpoint("Alibaba", m, "https://ws-kvneg1w4j01n4v80.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1/chat/completions",
                             {"Content-Type": "application/json", "Authorization": f"Bearer {ali_key}"}, payload)
    print(f"  * {m:<30}: {'PASS' if ok else 'FAIL'} -> {msg}")
    time.sleep(0.05)

# 2. Vercel AI Gateway
vrc_key = keys.get("VERCEL_GATEWAY_API_KEY")
vrc_models = [
    "nvidia/nemotron-3-ultra-550b-a55b", "openai/gpt-oss-120b", "nvidia/nemotron-3.5-super-vl",
    "nvidia/nemotron-3.5-lightning-free", "xiaomi/mimo-v2.6-flash", "meta/muse-ember",
    "thinkingmachines/inkling-2-small", "minimax/minimax-m3.1-flash"
]
print("\n[2] Vercel AI Gateway:")
for m in vrc_models:
    payload = {"model": m, "messages": [{"role": "user", "content": "Say 'OK'"}]}
    ok, msg = check_endpoint("Vercel", m, "https://ai-gateway.vercel.sh/v1/chat/completions",
                             {"Content-Type": "application/json", "Authorization": f"Bearer {vrc_key}"}, payload)
    print(f"  * {m:<35}: {'PASS' if ok else 'FAIL'} -> {msg}")
    time.sleep(0.05)

# 3. Token Lab AMD
amd_key = keys.get("TOKENLAB_API_KEY")
print("\n[3] Token Lab AMD:")
for m in ["Gemma-4-31B-IT", "Qwen3.8-27B", "DeepSeek-V4-Flash"]:
    payload = {"model": m, "messages": [{"role": "user", "content": "Say 'OK'"}]}
    ok, msg = check_endpoint("AMD", m, "https://api.tokenlab.amd.com/v1/chat/completions",
                             {"Content-Type": "application/json", "Authorization": f"Bearer {amd_key}"}, payload)
    print(f"  * {m:<30}: {'PASS' if ok else 'FAIL'} -> {msg}")
    time.sleep(0.05)

# 4. TokenHarbor
thb_key = keys.get("TOKENHARBOUR_API_KEY")
print("\n[4] TokenHarbor:")
for m in ["deepseek-v4.1-flash:free", "mimo-v2.6-flash:free", "deepseek-v4-flash:free", "mimo-v2.5:free"]:
    payload = {"model": m, "messages": [{"role": "user", "content": "Say 'OK'"}]}
    ok, msg = check_endpoint("TokenHarbor", m, "https://tokenharbor.ai/v1/chat/completions",
                             {"Content-Type": "application/json", "Authorization": f"Bearer {thb_key}"}, payload)
    print(f"  * {m:<30}: {'PASS' if ok else 'FAIL'} -> {msg}")
    time.sleep(0.1)

# 5. APMix
apm_key = keys.get("APMIX_API_KEY")
print("\n[5] APMix:")
for m in ["deepseek-v4.1-flash-1017-free", "nemotron-3.5-super-vl-free"]:
    payload = {"model": m, "messages": [{"role": "user", "content": "Say 'OK'"}]}
    ok, msg = check_endpoint("APMix", m, "https://api.apmix.ai/v1/chat/completions",
                             {"Content-Type": "application/json", "Authorization": f"Bearer {apm_key}"}, payload)
    print(f"  * {m:<32}: {'PASS' if ok else 'FAIL'} -> {msg}")
    time.sleep(0.1)

# 6. APInex
apn_key = keys.get("APINEX_API_KEY")
print("\n[6] APInex:")
for m in ["free/gemini-3.8-flash", "free/mimo-v2.6-pro", "free/qwen-3.8-max", "free/kimi-k3", "free/deepseek-v4.1-flash"]:
    payload = {"model": m, "messages": [{"role": "user", "content": "Say 'OK'"}]}
    ok, msg = check_endpoint("APInex", m, "https://api.apinex.bond/v1/chat/completions",
                             {"Content-Type": "application/json", "Authorization": f"Bearer {apn_key}"}, payload)
    print(f"  * {m:<32}: {'PASS' if ok else 'FAIL'} -> {msg}")
    time.sleep(0.4)

# 7. Kilo Gateway
klo_key = keys.get("KILO_API_KEY")
print("\n[7] Kilo Gateway:")
for m in ["kilo-auto/free", "nvidia/nemotron-3.5-super-vl:free"]:
    payload = {"model": m, "messages": [{"role": "user", "content": "Say 'OK'"}]}
    ok, msg = check_endpoint("Kilo", m, "https://kilo.ai/api/gateway/v1/chat/completions",
                             {"Content-Type": "application/json", "Authorization": f"Bearer {klo_key}"}, payload)
    print(f"  * {m:<38}: {'PASS' if ok else 'FAIL'} -> {msg}")
    time.sleep(0.4)

# 8. Refuseless
ref_key = keys.get("REFUSELESS_API_KEY")
print("\n[8] Refuseless:")
for m in ["deepseek-v4.1-flash-abliterated-free"]:
    payload = {"model": m, "messages": [{"role": "user", "content": "Say 'OK'"}]}
    ok, msg = check_endpoint("Refuseless", m, "https://api.refuseless.com/v1/chat/completions",
                             {"Content-Type": "application/json", "Authorization": f"Bearer {ref_key}"}, payload)
    print(f"  * {m:<40}: {'PASS' if ok else 'FAIL'} -> {msg}")

# 9. Groq
grq_key = keys.get("GROQ_API_KEY")
print("\n[9] Groq:")
for m in ["qwen/qwen3.8-27b", "openai/gpt-oss-120b"]:
    payload = {"model": m, "messages": [{"role": "user", "content": "Say 'OK'"}]}
    ok, msg = check_endpoint("Groq", m, "https://api.groq.com/openai/v1/chat/completions",
                             {"Content-Type": "application/json", "Authorization": f"Bearer {grq_key}"}, payload)
    print(f"  * {m:<25}: {'PASS' if ok else 'FAIL'} -> {msg}")

# 10. Cohere
coh_key = keys.get("COHERE_API_KEY")
print("\n[10] Cohere:")
for m in ["command-a-03-2025"]:
    payload = {"model": m, "messages": [{"role": "user", "content": "Say 'OK'"}]}
    ok, msg = check_endpoint("Cohere", m, "https://api.cohere.com/v2/chat",
                             {"Content-Type": "application/json", "Authorization": f"Bearer {coh_key}"}, payload)
    print(f"  * {m:<25}: {'PASS' if ok else 'FAIL'} -> {msg}")
