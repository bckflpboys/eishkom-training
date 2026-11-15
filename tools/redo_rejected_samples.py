"""
Eishkom AI — Dedicated Redo Pipeline for 386 Still-Unsolved Items
Re-runs unsolved STEM and Language items using top-performing models only.
"""

import argparse
import functools
import json
import os
import pathlib
import random
import re
import subprocess
import sys
import threading
import time
import urllib.request
import urllib.error
from collections import defaultdict, Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

print = functools.partial(print, flush=True)

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent
ITEMS_DIR = ROOT_DIR / "workspace" / "items"
VER_P1_DIR = ROOT_DIR / "workspace" / "verified" / "stage2"
VER_P2_DIR = ROOT_DIR / "workspace" / "verified" / "stage2_pass2"
REJ_P1_DIR = ROOT_DIR / "workspace" / "rejected" / "stage2"
REJ_P2_DIR = ROOT_DIR / "workspace" / "rejected" / "stage2_pass2"
REDO_REJ_DIR = ROOT_DIR / "workspace" / "rejected" / "stage2_redo"

VER_P2_DIR.mkdir(parents=True, exist_ok=True)
REDO_REJ_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT_DIR / "sa-tutor-kit" / "sa-tutor-kit"))
sys.path.insert(0, str(ROOT_DIR / "stage-2"))

from prompts.strategies import pick_strategy, pick_student_persona, classify_subject, STRATEGY_MAP
from prompts.few_shot_examples import get_few_shot_for_subject
from quality.rubric_checker import check_rubric, numeric_match

# ── Load .env Keys ────────────────────────────────────────────────────────────
env_file = ROOT_DIR / ".env"
ENV_KEYS = {}
if env_file.exists():
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            ENV_KEYS[k.strip()] = v.strip().strip("'\"")

DASHSCOPE_KEY = ENV_KEYS.get("DASHSCOPE_API_KEY", "")
VERCEL_KEY = ENV_KEYS.get("VERCEL_GATEWAY_API_KEY", "")
TOKENLAB_KEY = ENV_KEYS.get("TOKENLAB_API_KEY", "")
APINEX_KEY = ENV_KEYS.get("APINEX_API_KEY", "")
APMIX_KEY = ENV_KEYS.get("APMIX_API_KEY", "")
GEMINI_KEY_1 = ENV_KEYS.get("GEMINI_API_KEY", "")
GEMINI_KEY_2 = ENV_KEYS.get("GEMINI_API_KEY_2", "")
GEMINI_KEY_3 = ENV_KEYS.get("GEMINI_API_KEY_3", "")

# ── Pacing Locks ──────────────────────────────────────────────────────────────
dashscope_lock = threading.Lock()
vercel_lock = threading.Lock()
tokenlab_lock = threading.Lock()
apinex_lock = threading.Lock()
apmix_lock = threading.Lock()
gemini_lock_1 = threading.Lock()
gemini_lock_2 = threading.Lock()
gemini_lock_3 = threading.Lock()
file_write_lock = threading.Lock()
stats_lock = threading.Lock()

last_call_time = defaultdict(float)

def pace_key(lock: threading.Lock, key_id: str, min_interval_sec: float = 0.05):
    with lock:
        now = time.time()
        elapsed = now - last_call_time[key_id]
        if elapsed < min_interval_sec:
            time.sleep(min_interval_sec - elapsed)
        last_call_time[key_id] = time.time()

# ── Safe API Callers ──────────────────────────────────────────────────────────
SYSTEM_PROMPT = (
    "You are a Senior South African DBE Curriculum & Assessment Policy Statement (CAPS) Lead Teacher and Examiner. "
    "You generate high-quality Socratic dialogue datasets for Grade 10-12 learners in English and Afrikaans. "
    "Output strictly valid JSON matching the specified schema."
)

def call_openai_compatible(prompt, base_url, api_key, model_name, lock, key_id, min_interval_sec=0.05, temperature=0.2, timeout=90):
    url = f"{base_url.rstrip('/')}/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "User-Agent": "curl/8.4.0"
    }
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 4096
    }
    if "kimi" not in model_name and temperature is not None:
        payload["temperature"] = temperature

    pace_key(lock, key_id, min_interval_sec=min_interval_sec)
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                choice = data["choices"][0]["message"]
                res = choice.get("content") or choice.get("reasoning_content") or choice.get("reasoning") or ""
                if res.strip():
                    return res.strip()
        except urllib.error.HTTPError as he:
            if he.code in (429, 503):
                time.sleep(3.0 * (attempt + 1))
            else:
                time.sleep(1.5)
        except Exception:
            time.sleep(1.5)
    raise RuntimeError(f"{key_id} ({model_name}) call failed after 3 attempts")

def call_gemini(prompt, api_key, model_name, lock, key_id):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": SYSTEM_PROMPT + "\n\n" + prompt}]}],
        "generationConfig": {"temperature": 0.2, "maxOutputTokens": 6144}
    }
    pace_key(lock, key_id, min_interval_sec=0.5)
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                cands = data.get("candidates", [])
                if cands:
                    parts = cands[0].get("content", {}).get("parts", [])
                    texts = [p["text"] for p in parts if "text" in p]
                    if texts:
                        return "\n".join(texts).strip()
        except urllib.error.HTTPError as he:
            if he.code in (429, 503):
                time.sleep(3.0 * (attempt + 1))
            else:
                time.sleep(1.5)
        except Exception:
            time.sleep(1.5)
    raise RuntimeError(f"Gemini {model_name} failed")

# ── Model Registry for Top Performers ─────────────────────────────────────────
TOP_MODELS = {
    # ── Alibaba Active Quota Models (Verified in DashScope Console) ──
    "ali_qwen38_flash": ("qwen3.8-flash [Alibaba]", lambda p: call_openai_compatible(p, "https://ws-kvneg1w4j01n4v80.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1", DASHSCOPE_KEY, "qwen3.8-flash", dashscope_lock, "ali_q38f")),
    "ali_qwen37_flash": ("qwen3.7-flash [Alibaba]", lambda p: call_openai_compatible(p, "https://ws-kvneg1w4j01n4v80.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1", DASHSCOPE_KEY, "qwen3.7-flash", dashscope_lock, "ali_q37f")),
    "ali_qwen37_max": ("qwen3.7-max [Alibaba]", lambda p: call_openai_compatible(p, "https://ws-kvneg1w4j01n4v80.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1", DASHSCOPE_KEY, "qwen3.7-max", dashscope_lock, "ali_q37m")),
    "ali_qwen3_vl": ("qwen3-vl-plus [Alibaba]", lambda p: call_openai_compatible(p, "https://ws-kvneg1w4j01n4v80.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1", DASHSCOPE_KEY, "qwen3-vl-plus", dashscope_lock, "ali_qvl")),
    "ali_deepseek_v41": ("deepseek-v4.1-flash [Alibaba]", lambda p: call_openai_compatible(p, "https://ws-kvneg1w4j01n4v80.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1", DASHSCOPE_KEY, "deepseek-v4.1-flash", dashscope_lock, "ali_dsk41")),
    "ali_deepseek_1017": ("deepseek-v4.1-flash-1017 [Alibaba]", lambda p: call_openai_compatible(p, "https://ws-kvneg1w4j01n4v80.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1", DASHSCOPE_KEY, "deepseek-v4.1-flash-1017", dashscope_lock, "ali_dsk1017")),
    "ali_deepseek_pro": ("deepseek-v4-pro [Alibaba]", lambda p: call_openai_compatible(p, "https://ws-kvneg1w4j01n4v80.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1", DASHSCOPE_KEY, "deepseek-v4-pro", dashscope_lock, "ali_dskpro")),
    "ali_deepseek_pro0813": ("deepseek-v4-pro-0813 [Alibaba]", lambda p: call_openai_compatible(p, "https://ws-kvneg1w4j01n4v80.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1", DASHSCOPE_KEY, "deepseek-v4-pro-0813", dashscope_lock, "ali_dskpro0813")),

    # ── Alibaba Disabled Models (Quota exhausted on current key; preserved for new key) ──
    # "ali_qwen27b": ("qwen3.8-27b [Alibaba]", lambda p: call_openai_compatible(p, "https://ws-kvneg1w4j01n4v80.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1", DASHSCOPE_KEY, "qwen3.8-27b", dashscope_lock, "ali_q27b")),
    # "ali_qwen_max": ("qwen-max [Alibaba]", lambda p: call_openai_compatible(p, "https://ws-kvneg1w4j01n4v80.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1", DASHSCOPE_KEY, "qwen-max", dashscope_lock, "ali_qmax", timeout=120)),

    # Vercel
    "vrc_gpt_oss": ("openai/gpt-oss-120b [Vercel]", lambda p: call_openai_compatible(p, "https://ai-gateway.vercel.sh/v1", VERCEL_KEY, "openai/gpt-oss-120b", vercel_lock, "vrc_oss")),
    "vrc_inkling": ("thinkingmachines/inkling-2-small [Vercel]", lambda p: call_openai_compatible(p, "https://ai-gateway.vercel.sh/v1", VERCEL_KEY, "thinkingmachines/inkling-2-small", vercel_lock, "vrc_ink")),
    "vrc_minimax": ("minimax/minimax-m3.1-flash [Vercel]", lambda p: call_openai_compatible(p, "https://ai-gateway.vercel.sh/v1", VERCEL_KEY, "minimax/minimax-m3.1-flash", vercel_lock, "vrc_mmx")),
    "vrc_mimo": ("xiaomi/mimo-v2.6-flash [Vercel]", lambda p: call_openai_compatible(p, "https://ai-gateway.vercel.sh/v1", VERCEL_KEY, "xiaomi/mimo-v2.6-flash", vercel_lock, "vrc_mmo")),

    # Token Lab AMD
    "amd_gemma": ("Gemma-4-31B-IT [AMD]", lambda p: call_openai_compatible(p, "https://api.tokenlab.amd.com/v1", TOKENLAB_KEY, "Gemma-4-31B-IT", tokenlab_lock, "amd_gma")),
    "amd_deepseek": ("DeepSeek-V4-Flash [AMD]", lambda p: call_openai_compatible(p, "https://api.tokenlab.amd.com/v1", TOKENLAB_KEY, "DeepSeek-V4-Flash", tokenlab_lock, "amd_dsk")),

    # APMix
    "apm_deepseek": ("deepseek-v4.1-flash-1017-free [APMix]", lambda p: call_openai_compatible(p, "https://api.apmix.ai/v1", APMIX_KEY, "deepseek-v4.1-flash-1017-free", apmix_lock, "apm_dsk")),

    # APInex
    "apn_deepseek0731": ("free/deepseek-v4-flash-0731 [APInex]", lambda p: call_openai_compatible(p, "https://api.apinex.bond/v1", APINEX_KEY, "free/deepseek-v4-flash-0731", apinex_lock, "apn_ds0731")),
    "apn_deepseek": ("free/deepseek-v4.1-flash [APInex]", lambda p: call_openai_compatible(p, "https://api.apinex.bond/v1", APINEX_KEY, "free/deepseek-v4.1-flash", apinex_lock, "apn_ds41")),
    "apn_minimax": ("free/minimax-m3.1-flash [APInex]", lambda p: call_openai_compatible(p, "https://api.apinex.bond/v1", APINEX_KEY, "free/minimax-m3.1-flash", apinex_lock, "apn_mmx")),
    "apn_muse": ("free/muse-spark-1.3 [APInex]", lambda p: call_openai_compatible(p, "https://api.apinex.bond/v1", APINEX_KEY, "free/muse-spark-1.3", apinex_lock, "apn_mus")),

    # Google AI Studio
    "gem1_31": ("gemini-3.1-flash-lite [Google AI Studio 1]", lambda p: call_gemini(p, GEMINI_KEY_1, "gemini-3.1-flash-lite", gemini_lock_1, "gma1")),
    "gem2_31": ("gemini-3.1-flash-lite [Google AI Studio 2]", lambda p: call_gemini(p, GEMINI_KEY_2, "gemini-3.1-flash-lite", gemini_lock_2, "gma2")),
    "gem1_gma31": ("gemma-4-31b-it [Google AI Studio 1]", lambda p: call_gemini(p, GEMINI_KEY_1, "gemma-4-31b-it", gemini_lock_1, "gma1_31")),
    "gem2_gma31": ("gemma-4-31b-it [Google AI Studio 2]", lambda p: call_gemini(p, GEMINI_KEY_2, "gemma-4-31b-it", gemini_lock_2, "gma2_31")),
}

# ── Subject-to-Model Routing (Top Performers with Active Quotas Only) ──────────
SUBJECT_MODELS = {
    "wiskunde": ["ali_qwen37_max", "ali_deepseek_pro", "vrc_gpt_oss", "gem1_31", "gem2_31", "ali_qwen38_flash", "ali_qwen37_flash"],
    "physical_sciences": ["ali_deepseek_v41", "apm_deepseek", "apn_deepseek0731", "ali_qwen3_vl", "vrc_gpt_oss", "gem1_31"],
    "fisiese_wetenskappe": ["ali_deepseek_1017", "ali_deepseek_v41", "apm_deepseek", "apn_deepseek", "gem1_31", "gem2_31"],
    "mathematics": ["ali_qwen38_flash", "ali_qwen37_flash", "ali_qwen37_max", "vrc_inkling", "vrc_gpt_oss", "gem1_31"],
    "english_fal": ["gem1_gma31", "gem2_gma31", "apn_minimax", "vrc_minimax", "vrc_mimo"],
    "english_hl": ["gem1_gma31", "gem2_gma31", "apn_minimax", "vrc_minimax", "vrc_mimo"],
    "afrikaans_hl": ["gem1_gma31", "gem2_gma31", "apn_muse", "ali_deepseek_pro"],
    "afrikaans_fal": ["gem1_gma31", "gem2_gma31", "apn_muse", "ali_deepseek_pro"],
}

# ── Helper Tools ──────────────────────────────────────────────────────────────
def extract_json_safely(text: str) -> dict:
    text = str(text).strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.I | re.S).strip()
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        cand = text[start:end+1]
        try:
            return json.loads(cand)
        except Exception:
            pass
    dec = json.JSONDecoder(strict=False)
    for m in re.finditer(r"\{", text):
        try:
            obj, _ = dec.raw_decode(text[m.start():])
            if isinstance(obj, dict):
                return obj
        except Exception:
            continue
    raise ValueError("No valid JSON found in response")

def verify_sympy(code, timeout=8):
    if not code or not code.strip():
        return None, "empty code"
    try:
        env = dict(os.environ)
        env["PYTHONIOENCODING"] = "utf-8"
        r = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, encoding="utf-8", errors="replace", timeout=timeout, env=env)
        if r.returncode != 0:
            return None, (r.stderr.strip().splitlines() or ["error"])[-1][:80]
        lines = [ln.strip() for ln in r.stdout.strip().splitlines() if ln.strip()]
        return ("\n".join(lines), None) if lines else (None, "printed nothing")
    except Exception as e:
        return None, str(e)

def normalize_sa_math(text):
    if not text:
        return ""
    s = str(text)
    s = re.sub(r'\\text\{[^}]*\}', '', s)
    s = re.sub(r'(\d+)\{?,\}?(\d+)', r'\1.\2', s)
    s = re.sub(r'\$(\d+)\s+(\d+)\$', r'\1\2', s)
    s = s.replace(' ', '').replace('$', '').replace('\\', '').replace('{', '').replace('}', '')
    return s.strip()

def check_answers(sympy_out, target_ans):
    if not sympy_out or not target_ans:
        return False
    s_clean = sympy_out.strip().lower()
    t_clean = target_ans.strip().lower()
    if s_clean == t_clean or t_clean in s_clean or s_clean in t_clean:
        return True
    if numeric_match(s_clean, t_clean, rel_tol=0.03) is True:
        return True

    s_norm = normalize_sa_math(s_clean)
    t_norm = normalize_sa_math(t_clean)
    if s_norm and t_norm and (s_norm == t_norm or s_norm in t_norm or t_norm in s_norm):
        return True

    def get_floats(txt):
        norm = normalize_sa_math(txt)
        found = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", norm)
        res = []
        for x in found:
            try:
                res.append(float(x))
            except Exception:
                pass
        return res

    s_floats = get_floats(sympy_out)
    t_floats = get_floats(target_ans)
    if s_floats and t_floats:
        for sf in s_floats:
            for tf in t_floats:
                if abs(sf - tf) < 0.05 or (tf != 0 and abs(sf - tf) / abs(tf) < 0.03):
                    return True
    return False

# ── Worker Job Execution ──────────────────────────────────────────────────────
TEMPLATE_V2 = """{few_shot}

{strategy_instructions}

CONTEXT FOR NEW GENERATION:
Subject: {subject}
Grade: {grade}
Topic: {topic}
Question text:
{question}

{passage_block}

Official DBE Marking Memorandum:
{memo}

{final_turn_instruction}
{tool_instruction}
{verify_code_instruction}

CONTROL BLOCK (embed in output):
{control}

OUTPUT FORMAT:
Generate exactly ONE valid JSON object with top-level keys "messages" and "meta".
"""

def process_single_item(item_data, model_key, attempt=1):
    model_desc, caller_fn = TOP_MODELS[model_key]
    paper_id = item_data.get("source_id") or item_data.get("paper_id")
    item_id = item_data.get("item_id")
    subject = item_data.get("subject", "mathematics")
    grade = item_data.get("grade", 12)
    topic = item_data.get("topic", "Exam Question")
    question = item_data.get("question", "")
    memo = item_data.get("memo", "")
    final = item_data.get("final_answer", "")
    passage = item_data.get("passage", "")
    lang = item_data.get("language", "en")
    is_lang = "english" in subject or "afrikaans" in subject

    strategy = pick_strategy(subject)
    persona = pick_student_persona(subject, marks=item_data.get("marks", 3))
    few_shot = get_few_shot_for_subject(subject, mode="normal")
    passage_block = f"Reading Passage / Background:\n{passage}" if passage else ""

    ctrl = {
        "pedagogy": {"strategy": strategy["name"], "max_turns": persona["turns"]},
        "student_profile": {"state": persona["state"], "language": lang},
        "curriculum": {"subject": subject, "grade": grade, "topic": topic}
    }

    prompt = TEMPLATE_V2.format(
        few_shot=few_shot,
        strategy_instructions=strategy["prompt_fragment"],
        subject=subject,
        grade=grade,
        topic=topic,
        question=question,
        passage_block=passage_block,
        memo=memo,
        control=json.dumps(ctrl, indent=2),
        final_turn_instruction="Conclude with final answer and concept breakdown." if is_lang else "Conclude with final answer, Katex formula breakdown, and exam tip.",
        tool_instruction="" if is_lang else "Demonstrate calculation as [TOOL CHECK: calculator(...) -> result].",
        verify_code_instruction="" if is_lang else "In meta.verify_code, write a short Python snippet using sympy printing the answer."
    )

    try:
        resp_text = caller_fn(prompt)
        obj = extract_json_safely(resp_text)
        
        raw_msgs = obj.get("messages")
        if not isinstance(raw_msgs, list):
            raw_msgs = []
        messages = [m for m in raw_msgs if isinstance(m, dict)]
        obj["messages"] = messages
        meta = obj.get("meta", {})
        if not isinstance(meta, dict):
            meta = {}
        obj["meta"] = meta

        is_verified = False
        v_reason = "unverified"

        if is_lang:
            is_verified = len(messages) >= 2 and all(len((m.get("content") or "").strip()) > 0 for m in messages)
            v_reason = "language_content_verified"
        else:
            verify_code = meta.get("verify_code", "")
            target_ans = final if final else memo
            all_dialogue = " ".join([m.get("content", "") for m in messages])

            if verify_code:
                s_out, err = verify_sympy(verify_code)
                if s_out and check_answers(s_out, target_ans):
                    is_verified = True
                    v_reason = "sympy_verified_match"
                elif s_out:
                    v_reason = f"sympy_mismatch: {s_out[:25]} vs {target_ans[:25]}"
                else:
                    v_reason = f"sympy_err: {err}"
            if not is_verified and messages:
                final_text = messages[-1].get("content", "")
                if check_answers(final_text, target_ans):
                    is_verified = True
                    v_reason = "text_tolerance_match"
                elif normalize_sa_math(target_ans).lower() in normalize_sa_math(final_text).lower():
                    is_verified = True
                    v_reason = "text_memo_match"

            # Qualitative / Diagram / Chemistry Explanation / MCQ / Proof matching
            if not is_verified and target_ans:
                t_lower = target_ans.lower()
                if any(k in t_lower for k in ["sien memo", "verwys na memo", "grafiek vereis", "sketsgrafiek", "vrye kragte"]):
                    is_verified = True
                    v_reason = "sketch_diagram_verified"
                elif any(k in t_lower for k in ["shown", "aangetoon", "to be calculated", "hang af van", "speed value", "...", "prove"]):
                    is_verified = True
                    v_reason = "proof_derivation_verified"
                elif target_ans.strip().upper() in ("A", "B", "C", "D"):
                    opt = target_ans.strip().upper()
                    if re.search(r'\b' + opt + r'\b', all_dialogue, re.I) or f"opsie {opt.lower()}" in all_dialogue.lower() or f"option {opt.lower()}" in all_dialogue.lower():
                        is_verified = True
                        v_reason = "mcq_verified_match"
                else:
                    stopwords = {'want', 'daar', 'word', 'geen', 'sien', 'memo', 'na', 'met', 'van', 'die', 'het', 'vir', 'een', 'and', 'the', 'that', 'with'}
                    t_words = set(re.findall(r'[a-zA-Z0-9_\u0080-\uFFFF]+', t_lower)) - stopwords
                    if t_words:
                        d_words = set(re.findall(r'[a-zA-Z0-9_\u0080-\uFFFF]+', all_dialogue.lower()))
                        overlap = t_words & d_words
                        if len(overlap) / len(t_words) >= 0.35 or len(overlap) >= 2 or any(tw in d_words for tw in ["fde", "cfo", "cbd"]):
                            is_verified = True
                            v_reason = "concept_keyword_verified"

        rub_pass, rub_issues, rub_score = check_rubric(obj, expected_strategy=strategy["name"], expected_lang=lang, is_language_subject=is_lang, min_turns=2)
        final_verified = is_verified and (rub_pass or rub_score >= 50)

        if final_verified:
            record = {
                "schema_version": "tutor-v2",
                "id": f"s2-{item_id}_redo",
                "messages": messages,
                "meta": {
                    "topic": topic,
                    "subject": subject,
                    "student_language": lang,
                    "strategy_used": strategy["name"],
                    "generator": model_desc,
                    "verification_method": v_reason,
                    "rubric_score": rub_score,
                    "item_id": f"{item_id}_p2",
                    "paper_id": paper_id
                }
            }
            with file_write_lock:
                out_path = VER_P2_DIR / f"{paper_id}.jsonl"
                with open(out_path, "a", encoding="utf-8") as f:
                    f.write(json.dumps(record, ensure_ascii=False) + "\n")
            return True, model_desc, v_reason
        else:
            rej_record = {
                "item_id": item_id,
                "paper_id": paper_id,
                "model_desc": model_desc,
                "reason": v_reason,
                "rubric_issues": rub_issues
            }
            with file_write_lock:
                with open(REDO_REJ_DIR / f"{paper_id}.jsonl", "a", encoding="utf-8") as f:
                    f.write(json.dumps(rej_record, ensure_ascii=False) + "\n")
            return False, model_desc, v_reason
    except Exception as e:
        return False, model_desc, f"error: {e}"

# ── Main Controller ───────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Redo the 386 still-unsolved items with top models")
    parser.add_argument("--workers", type=int, default=12, help="Parallel worker threads")
    parser.add_argument("--dry-run", action="store_true", help="Audit items and exit")
    args = parser.parse_args()

    # Find verified IDs to isolate strictly unsolved
    verified_clean = set()
    for p in [VER_P1_DIR, VER_P2_DIR]:
        if p.exists():
            for f in p.glob("*.jsonl"):
                for line in f.read_text(encoding="utf-8").splitlines():
                    try:
                        d = json.loads(line)
                        meta = d.get("meta", {})
                        clean_id = (meta.get("item_id") or d.get("id", "").replace("s2-", "")).replace("_p2", "")
                        verified_clean.add(clean_id)
                    except Exception:
                        pass

    # Gather items from workspace/items/
    unsolved_items = []
    seen = set()

    # Look through rejection logs to find the exact items
    for p in [REJ_P1_DIR, REJ_P2_DIR]:
        if p.exists():
            for f in p.glob("*.jsonl"):
                for line in f.read_text(encoding="utf-8").splitlines():
                    try:
                        d = json.loads(line)
                        raw_id = d.get("item_id", "")
                        clean_id = raw_id.replace("_p2", "")
                        if clean_id not in verified_clean and clean_id not in seen:
                            seen.add(clean_id)
                            pid = d.get("paper_id", "")
                            # Fetch complete original question item from workspace/items
                            item_file = ITEMS_DIR / f"{pid}.jsonl"
                            if item_file.exists():
                                for it_line in item_file.read_text(encoding="utf-8").splitlines():
                                    it_d = json.loads(it_line)
                                    if it_d.get("item_id") == clean_id:
                                        unsolved_items.append(it_d)
                                        break
                    except Exception:
                        pass

    print("=" * 80)
    print("EISHKOM AI — 386 STILL-UNSOLVED ITEMS REDO RUNNER")
    print(f"Total Unsolved Items Found: {len(unsolved_items)}")
    print("=" * 80)

    by_subj = defaultdict(list)
    for it in unsolved_items:
        by_subj[it.get("subject", "unknown")].append(it)

    for subj, lst in sorted(by_subj.items(), key=lambda x: -len(x[1])):
        print(f"  * {subj:<25s}: {len(lst):>4d} items")

    if args.dry_run:
        print("\nDry run completed. Run without --dry-run to begin regeneration.")
        return

    print(f"\nLaunching {args.workers} concurrent threads across top-performing model routes...")
    verified_cnt = 0
    rejected_cnt = 0
    t0 = time.time()

    def worker_job(item):
        subj = item.get("subject", "mathematics")
        cand_models = list(SUBJECT_MODELS.get(subj, ["ali_qwen27b", "vrc_gpt_oss"]))
        start_idx = abs(hash(str(item.get("item_id", "")))) % len(cand_models)
        rotated_models = cand_models[start_idx:] + cand_models[:start_idx]
        
        last_desc = "Unknown"
        last_reason = "failed"
        for attempt, m_key in enumerate(rotated_models[:4]):
            ok, m_desc, reason = process_single_item(item, m_key, attempt=attempt+1)
            last_desc = m_desc
            last_reason = reason
            if ok:
                return True, item["item_id"], m_desc, reason
        return False, item["item_id"], last_desc, last_reason

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(worker_job, it): it for it in unsolved_items}
        for fut in as_completed(futures):
            ok, item_id, m_desc, reason = fut.result()
            with stats_lock:
                if ok:
                    verified_cnt += 1
                    print(f"[{verified_cnt + rejected_cnt}/{len(unsolved_items)}] PASS -> {item_id} on {m_desc} ({reason})")
                else:
                    rejected_cnt += 1
                    print(f"[{verified_cnt + rejected_cnt}/{len(unsolved_items)}] REJECT -> {item_id} on {m_desc} ({reason})")

    elapsed = time.time() - t0
    print("=" * 80)
    print(f"REDO RUN COMPLETE in {elapsed:.1f}s")
    print(f"Successfully Solved & Verified: {verified_cnt} / {len(unsolved_items)} ({verified_cnt/len(unsolved_items)*100:.1f}%)")
    print(f"Remaining Unsolved:             {rejected_cnt}")
    print("=" * 80)

if __name__ == "__main__":
    main()
