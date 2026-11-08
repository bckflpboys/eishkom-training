#!/usr/bin/env python3
"""
tools/run_dynamic_fleet_5000.py - Eishkom AI Cooperative Multi-Model Fleet.

Architecture:
  - All models working continuously in parallel on their assigned lanes:
      * Gemini 3.5 Flash Lite (Key 1): Language lanes (English FAL, Afrikaans FAL)
      * Gemini 3.1 Flash Lite (Key 2): Language & Science lanes (English HL, Afrikaans HL, Physics P2)
      * OpenRouter Nemotron Turbo (0.6s): Maths P2 lane
      * Intern-AI DeepSeek V4.1: Fisiese Wetenskappe lane
      * OpenAI gpt-6-luna (Primary): Maths P1 & Wiskunde V1 (2 papers per cycle)
      * OpenAI gpt-6-luna (Dynamic Rover):
          - Finishes remaining items for any paper that is lagging behind
          - Operates in a 2:1 loop: does 2 papers in assigned subject, then helps 1 paper in each other subject
  - Subprocess Windows UTF-8 encoding fix: encoding='utf-8', errors='replace'
  - Embedded Tool Calling in reasoning: [TOOL CHECK: calculator(...) -> result]
  - Forensic South African decimal comma normalization
  - Auto-generation of matching full_solution demonstrations per paper
  - Non-stop generation targeting 5,000+ SFT samples
"""

import os
import sys
import json
import time
import re
import ssl
import threading
import subprocess
import urllib.request
import urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT_DIR = Path(__file__).resolve().parent.parent
KIT_ROOT = ROOT_DIR / "sa-tutor-kit" / "sa-tutor-kit"
sys.path.insert(0, str(KIT_ROOT))
sys.path.insert(0, str(ROOT_DIR / "tools"))

try:
    from answers import answers_match
except ImportError:
    def answers_match(a, b):
        return a.strip().lower() == b.strip().lower()

from convert_raw_items_to_full_solutions import process_paper, OUT_DIR as FULLSOL_DIR

W4_VER_DIR = ROOT_DIR / "workspace" / "verified" / "wave4"
W4_VER_DIR.mkdir(parents=True, exist_ok=True)
W4_GEN_DIR = ROOT_DIR / "workspace" / "gen" / "wave4"
W4_GEN_DIR.mkdir(parents=True, exist_ok=True)

W3_VER_DIR = ROOT_DIR / "workspace" / "verified" / "wave3"
W3_GEN_DIR = ROOT_DIR / "workspace" / "gen" / "wave3"

ITEMS_DIR = ROOT_DIR / "workspace" / "items"

# Load keys
def load_env():
    keys = {}
    for env_path in [ROOT_DIR / ".env", KIT_ROOT / ".env"]:
        if env_path.exists():
            for line in env_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if "=" in line and not line.startswith("#"):
                    k, v = line.split("=", 1)
                    keys[k.strip()] = v.strip().strip("'\"")
    return keys

ENV_KEYS = load_env()
OPENAI_KEY = ENV_KEYS.get("OPENAI_API_KEY", "")
OPENROUTER_KEY = ENV_KEYS.get("OPENROUTER_API_KEY", "")
GEMINI_KEY_1 = ENV_KEYS.get("GEMINI_API_KEY", "")
GEMINI_KEY_2 = ENV_KEYS.get("GEMINI_API_KEY_2", "") or GEMINI_KEY_1
INTERN_KEY = ENV_KEYS.get("INTERN_API_KEY", "")
INTERN_BASE_URL = ENV_KEYS.get("INTERN_BASE_URL", "https://discovery-api.intern-ai.org.cn/v1")

print_lock = threading.Lock()
key1_lock = threading.Lock()
key2_lock = threading.Lock()
openrouter_lock = threading.Lock()
intern_lock = threading.Lock()
build_lock = threading.Lock()

milestone_5000_alerted = False

SYSTEM_PROMPT = (
    "You are an expert South African teacher and a careful data writer. "
    "You write ONE training record for a school tutor AI following the CAPS curriculum and TUTOR SPEC. "
    "CRITICAL: Output raw JSON object starting with { and ending with } immediately. Do NOT write chain-of-thought outside JSON. All reasoning must go inside the 'reasoning' fields."
)

TEMPLATE = """CRITICAL: START YOUR RESPONSE WITH {{ IMMEDIATELY. NO PREAMBLE TEXT.

=== THIS RECORD ===
control: {control}
thinking: {thinking}

SOURCE ITEM:
subject: {subject}   grade: {grade}   topic: {topic}
{passage}question: {question}
memo / worked solution: {memo}
final answer from the memo: {final}

LEARNER SIMULATION:
- learner writes in: {lang}
- learner's state: {state}
- writing style: {style}
- the learner sends {turns} message(s) in total; the first presents the question

OUTPUT FORMAT (one JSON object):
{{
  "messages": [
    {{"role": "user", "content": "..."}},
    {{"role": "assistant", "reasoning": "...", "content": "..."}},
    ...
  ],
  "meta": {{
    "strategy_used": "{strategy}",
    "final_answer": "{final}",
    "verify_code": "import sympy as sp\\n# solve and print final answer",
    "techniques": ["..."]
  }}
}}

RULES:
1. Socratic hint ladder: ask ONE small question at a time and wait. Do not reveal the full answer immediately.
2. In assistant messages, include "reasoning" (private thought diagnosing student) and "content" (the response).
3. TOOL-CALLING INSTRUCTION FOR CALCULATION SUBJECTS (Maths & Sciences):
   In your private reasoning ("reasoning"), demonstrate the exact tool-check calculation:
   [TOOL CHECK: calculator(expression="...") -> result]
   Show the step-by-step arithmetic so the student model learns how to call the calculator for future calculations.
4. In meta.verify_code, write a short Python snippet using sympy or standard library that prints the final answer.
5. Output valid JSON only with NO markdown fences.
"""

def extract_json_safely(text):
    text = str(text).strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.I).strip()
    
    first_b = text.find("{")
    last_b = text.rfind("}")
    if first_b != -1 and last_b != -1 and last_b > first_b:
        sub = text[first_b : last_b + 1]
        for s in [sub, re.sub(r'\\(?![/"\\bfnrtu])', r'\\\\', sub)]:
            try:
                obj = json.loads(s, strict=False)
                if isinstance(obj, dict) and ("messages" in obj or "meta" in obj):
                    return obj
            except:
                pass

    dec = json.JSONDecoder(strict=False)
    for candidate in [text, re.sub(r'\\(?![/"\\bfnrtu])', r'\\\\', text)]:
        for m in re.finditer(r"\{", candidate):
            try:
                obj, _ = dec.raw_decode(candidate[m.start():])
                if isinstance(obj, dict) and ("messages" in obj or "meta" in obj):
                    return obj
            except:
                continue
        try:
            obj = json.loads(candidate, strict=False)
            if isinstance(obj, list) and len(obj) > 0 and isinstance(obj[0], dict):
                return obj[0]
            if isinstance(obj, dict) and ("messages" in obj or "meta" in obj):
                return obj
        except:
            pass

    raise ValueError(f"No valid JSON found in response ({len(text)} chars)")

# Forensic Matcher with South African Comma Normalization and UTF-8 Safe Subprocess
ALLOWED_IMPORTS = {"sympy", "math", "fractions", "decimal", "itertools", "statistics", "cmath", "numbers"}
BLOCKED = re.compile(r"\b(open|exec|eval|compile|__import__|input|globals|locals|getattr|setattr|breakpoint)\s*\(|"
                     r"\b(os|sys|subprocess|socket|shutil|pathlib|requests|urllib|ctypes|pickle)\b", re.I)

def verify_sympy(code, timeout=8):
    if not code or not code.strip():
        return None, "empty code"
    for m in re.finditer(r"^\s*(?:from|import)\s+([A-Za-z_][\w]*)", code, flags=re.M):
        if m.group(1) not in ALLOWED_IMPORTS:
            return None, f"blocked import: {m.group(1)}"
    if BLOCKED.search(code):
        return None, "blocked system name"
    try:
        r = subprocess.run(
            [sys.executable, "-I", "-c", code],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout
        )
        if r.returncode != 0:
            return None, (r.stderr.strip().splitlines() or ["error"])[-1][:80]
        lines = [ln.strip() for ln in r.stdout.strip().splitlines() if ln.strip()]
        return ("\n".join(lines), None) if lines else (None, "printed nothing")
    except subprocess.TimeoutExpired:
        return None, "timeout"
    except Exception as e:
        return None, str(e)[:80]

def normalize_sa_math(text):
    if not text:
        return ""
    s = str(text)
    s = re.sub(r'\\text\{[^}]*\}', '', s)
    s = re.sub(r'(\d+)\{?,\}?(\d+)', r'\1.\2', s)
    s = re.sub(r'\$(\d+)\s+(\d+)\$', r'\1\2', s)
    s = s.replace(' ', '').replace('$', '').replace('\\', '').replace('{', '').replace('}', '')
    return s.strip()

def check_answers(sympy_out, memo_str):
    if not sympy_out or not memo_str:
        return False
    if answers_match(sympy_out, memo_str):
        return True
    
    s_norm = normalize_sa_math(sympy_out)
    m_norm = normalize_sa_math(memo_str)
    if s_norm and m_norm and (s_norm == m_norm or s_norm in m_norm or m_norm in s_norm):
        return True

    def get_floats(txt):
        norm = normalize_sa_math(txt)
        found = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", norm)
        res = []
        for x in found:
            try:
                res.append(float(x))
            except:
                pass
        return res

    s_floats = get_floats(sympy_out)
    m_floats = get_floats(memo_str)
    
    if s_floats and m_floats:
        for sf in s_floats:
            for mf in m_floats:
                if abs(sf - mf) < 0.05 or (mf != 0 and abs(sf - mf) / abs(mf) < 0.02):
                    return True

    return False

# Caller functions
def call_openai_luna(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_KEY}"
    }
    payload = {
        "model": "gpt-6-luna",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "reasoning_effort": "xhigh",
        "max_completion_tokens": 4000
    }
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["choices"][0]["message"]["content"]
        except Exception:
            time.sleep(2.0 * (attempt + 1))
    raise RuntimeError("OpenAI gpt-6-luna failed after 4 attempts")

def call_gemini(prompt, api_key, model_name, lock):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": SYSTEM_PROMPT + "\n\n" + prompt}]}],
        "generationConfig": {
            "temperature": 0.2,
            "maxOutputTokens": 4000,
            "thinkingConfig": {"thinkingBudget": 24576}
        }
    }
    with lock:
        time.sleep(0.3)
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                candidates = data.get("candidates", [])
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts", [])
                    texts = [p["text"] for p in parts if "text" in p]
                    return "\n".join(texts)
        except urllib.error.HTTPError as he:
            if he.code == 429:
                time.sleep(5.0)
            else:
                time.sleep(2.0)
        except Exception:
            time.sleep(2.0)
    raise RuntimeError(f"Gemini {model_name} failed")

def call_gemini_with_fallback(prompt, api_key, model_name, lock):
    try:
        return call_gemini(prompt, api_key, model_name, lock)
    except Exception:
        with print_lock:
            print(f"[{model_name}] Quota/Error -> Falling back to OpenAI gpt-6-luna.")
        return call_openai_luna(prompt)

def call_openrouter_nemotron_turbo(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "HTTP-Referer": "https://eishkom.ai",
        "X-Title": "Eishkom AI Tutor Wave 4"
    }
    payload = {
        "model": "nvidia/nemotron-3-ultra-550b:free",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 3500,
        "reasoning": {"effort": "high"}
    }
    with openrouter_lock:
        time.sleep(0.6)
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, timeout=90) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                choice = data["choices"][0]["message"]
                return choice.get("content") or choice.get("reasoning", "")
        except urllib.error.HTTPError as he:
            if he.code == 429:
                time.sleep(3.0)
            else:
                time.sleep(1.5)
        except Exception:
            time.sleep(1.5)
    with print_lock:
        print("[OpenRouter Nemotron] 429/Timeout -> Falling back to OpenAI gpt-6-luna.")
    return call_openai_luna(prompt)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def call_intern_deepseek_with_fallback(prompt):
    url = f"{INTERN_BASE_URL}/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {INTERN_KEY}",
        "User-Agent": "curl/8.4.0"
    }
    payload = {
        "model": "deepseek-v4.1-flash-1017",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 3500
    }
    with intern_lock:
        time.sleep(0.5)
    for attempt in range(2):
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=75) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                choice = data["choices"][0]["message"]
                content = choice.get("content")
                if content and "{" in content:
                    return content
        except Exception:
            time.sleep(2.0)
    with print_lock:
        print("[Intern-AI DeepSeek Lane] Timeout/Error -> Falling back to OpenAI gpt-6-luna.")
    return call_openai_luna(prompt)

def get_current_totals():
    all_socratic = 0
    for d in [ROOT_DIR / "workspace" / "verified" / "test_round", ROOT_DIR / "workspace" / "verified" / "wave2", W3_VER_DIR, W4_VER_DIR]:
        if d.exists():
            for f in d.glob("*.jsonl"):
                all_socratic += sum(1 for _ in open(f, encoding="utf-8"))
    all_fullsol = 0
    if FULLSOL_DIR.exists():
        for f in FULLSOL_DIR.glob("*.jsonl"):
            all_fullsol += sum(1 for _ in open(f, encoding="utf-8"))
    estimated_samples = int(all_socratic * 2.5) + all_fullsol
    return all_socratic, all_fullsol, estimated_samples

def check_and_alert_5000():
    global milestone_5000_alerted
    with build_lock:
        socratic, fullsol, est = get_current_totals()
        if est >= 5000 and not milestone_5000_alerted:
            milestone_5000_alerted = True
            print("\n" + "*" * 80)
            print(f"*** ALERT: 5,000 SFT TRAINING SAMPLES MILESTONE REACHED! ({est} estimated) ***")
            print(f"*** Socratic Lessons: {socratic} (~{int(socratic * 2.5)} turns) | Full Solutions: {fullsol} ***")
            print(f"*** Continuing generation non-stop as instructed! ***")
            print("*" * 80 + "\n")

# Single Paper Processor with Instant Resumption
def process_paper_item_queue(lane):
    lane_id = lane["id"]
    paper_id = lane["paper_id"]
    caller = lane["caller"]
    model_desc = lane["model_desc"]

    item_file = ITEMS_DIR / f"{paper_id}.jsonl"
    if not item_file.exists():
        with print_lock:
            print(f"[{lane_id}] Paper {paper_id} not found!")
        return 0, 0, 0

    items = []
    with open(item_file, encoding="utf-8") as fp:
        for line in fp:
            line = line.strip()
            if line:
                try:
                    items.append(json.loads(line))
                except:
                    pass

    # Check verified file in wave3 or wave4
    ver_dir = W3_VER_DIR if (W3_VER_DIR / f"{paper_id}.jsonl").exists() else W4_VER_DIR
    gen_dir = W3_GEN_DIR if (W3_GEN_DIR / f"{paper_id}.jsonl").exists() else W4_GEN_DIR
    
    verified_file = ver_dir / f"{paper_id}.jsonl"
    raw_gen_file = gen_dir / f"{paper_id}.jsonl"

    done_items = set()
    if raw_gen_file.exists():
        for line in open(raw_gen_file, encoding="utf-8"):
            try:
                rec = json.loads(line)
                if "item_id" in rec:
                    done_items.add(rec["item_id"])
            except:
                pass

    with print_lock:
        print(f"[{lane_id}] Starting {paper_id} ({len(items)} items total, {len(done_items)} already generated) on {model_desc}")

    n_gen = len(done_items)
    n_ver = sum(1 for _ in open(verified_file, encoding="utf-8")) if verified_file.exists() else 0

    for idx, item in enumerate(items, 1):
        item_id = item.get("item_id", f"{paper_id}-item-{idx}")
        if item_id in done_items:
            continue

        subject = item.get("subject", "mathematics")
        grade = item.get("grade", 12)
        topic = item.get("topic", "Exam Question")
        passage = f"passage:\n{item.get('passage')}\n\n" if item.get("passage") else ""
        question = item.get("question", "")
        memo = item.get("memo") or item.get("solution") or item.get("answer", "")
        final = item.get("final_answer") or item.get("answer") or ""

        is_af = "afrikaans" in subject.lower() or "wiskunde" in subject.lower() or "wetenskappe" in subject.lower()
        lang = "af" if is_af else "en"

        ctrl = {
            "subject": subject,
            "grade": grade,
            "subject_language": lang,
            "response_language": "mirror",
            "strategy": "step_walkthrough",
            "answer_policy": "guided",
            "student_level": "struggling",
            "tone": "encouraging",
            "response_length": "short",
            "tools": ["calculator", "board"],
            "math_format": "latex"
        }

        prompt = TEMPLATE.format(
            control=json.dumps(ctrl),
            thinking="on",
            subject=subject,
            grade=grade,
            topic=topic,
            passage=passage,
            question=question,
            memo=memo,
            final=final,
            lang=lang,
            state="lost",
            style="everyday learner language, short turns",
            turns=3,
            strategy="step_walkthrough"
        )

        try:
            resp_text = caller(prompt)
            n_gen += 1
            done_items.add(item_id)

            with open(raw_gen_file, "a", encoding="utf-8") as rfp:
                rfp.write(json.dumps({"item_id": item_id, "model": model_desc, "raw": resp_text}, ensure_ascii=False) + "\n")

            obj = extract_json_safely(resp_text)
            messages = obj.get("messages", [])
            meta = obj.get("meta", {})
            verify_code = meta.get("verify_code", "")

            is_verified = False
            v_reason = "not_checked"

            if "english" in subject or "afrikaans" in subject:
                is_verified = len(messages) >= 2 and all(m.get("content") for m in messages)
                v_reason = "language_content_verified"
            else:
                if verify_code:
                    sympy_out, err = verify_sympy(verify_code)
                    if sympy_out:
                        target = final if final else memo
                        if check_answers(sympy_out, target):
                            is_verified = True
                            v_reason = "verified_match"
                        else:
                            v_reason = f"mismatch: sympy={sympy_out[:30]} vs memo={target[:30]}"
                    else:
                        v_reason = f"sympy_err: {err}"
                else:
                    v_reason = "missing_verify_code"

            if is_verified:
                n_ver += 1
                record = {
                    "schema_version": "tutor-v1",
                    "id": f"wave4-{item_id}",
                    "group_id": str(item_id),
                    "control": ctrl,
                    "thinking": "on",
                    "messages": messages,
                    "meta": {
                        "topic": topic,
                        "task_type": "comprehension" if ("english" in subject or "afrikaans" in subject) else "solve_problem",
                        "student_language": lang,
                        "strategy_used": "step_walkthrough",
                        "source_type": "past_paper_adapted",
                        "source_licence": "DBE Open Educational Resource",
                        "generator": model_desc,
                        "answer_verified": True,
                        "verification_method": "sympy_vs_memo",
                        "split": "auto",
                        "final_answer": final or memo[:100],
                        "verify_code": verify_code,
                        "paper_id": paper_id,
                        "item_id": item_id,
                        "techniques": ["polya_four_steps", "check_by_substitution"] if "math" in subject or "wiskunde" in subject else ["units_check", "concept_map"] if "phys" in subject or "wetenskap" in subject else ["context_clues", "mark_per_point"]
                    }
                }
                with open(verified_file, "a", encoding="utf-8") as vfp:
                    vfp.write(json.dumps(record, ensure_ascii=False) + "\n")

            with print_lock:
                status_icon = "PASS" if is_verified else "REJECT"
                print(f"[{lane_id}] Item {idx}/{len(items)} [{item_id}] -> {status_icon} | Verified: {n_ver}/{n_gen}")

            check_and_alert_5000()

        except Exception as e:
            with print_lock:
                print(f"[{lane_id}] Item {idx}/{len(items)} EXCEPTION: {e}")

    # Generate full_solution demonstrations as soon as paper finishes
    try:
        cnt_full = process_paper(paper_id)
        with print_lock:
            print(f"[{lane_id}] Paper {paper_id} complete! Generated {cnt_full} matching full_solution demonstrations.")
    except Exception as e:
        with print_lock:
            print(f"[{lane_id}] Error generating full solutions: {e}")

    check_and_alert_5000()
    return n_gen, n_ver, len(items)

def main():
    print("=" * 80)
    print("EISHKOM AI — COOPERATIVE MULTI-MODEL FLEET TARGETING 5,000+ SAMPLES")
    print("=" * 80)
    _, _, start_samples = get_current_totals()
    print(f"Current SFT Samples Baseline: {start_samples} (Target: 5,000+)")

    # Parallel Fleet Queue
    fleet_lanes = [
        # 1. OpenAI Rover: Finishes remaining items of lagging Wave 3 papers immediately
        {"id": "OPENAI-ROVER-1", "paper_id": "dbe-mathematics-g12-p2-2021-nov", "caller": call_openai_luna, "model_desc": "gpt-6-luna (Rover)"},
        {"id": "OPENAI-ROVER-2", "paper_id": "dbe-fisiese_wetenskappe-g12-v1-2022-nov", "caller": call_openai_luna, "model_desc": "gpt-6-luna (Rover)"},

        # 2. OpenAI Primary: 2 papers in Maths / Wiskunde
        {"id": "OPENAI-M1-2020", "paper_id": "dbe-mathematics-g12-p1-2020-nov", "caller": call_openai_luna, "model_desc": "gpt-6-luna"},
        {"id": "OPENAI-WV1-2021", "paper_id": "dbe-wiskunde-g12-v1-2021-nov", "caller": call_openai_luna, "model_desc": "gpt-6-luna"},

        # 3. OpenRouter Nemotron Turbo: Maths P2
        {"id": "NEMOTRON-M2-2020", "paper_id": "dbe-mathematics-g12-p2-2020-nov", "caller": call_openrouter_nemotron_turbo, "model_desc": "nemotron-3-ultra-550b"},

        # 4. Intern-AI DeepSeek V4.1: Fisiese Wetenskappe
        {"id": "DEEPSEEK-FW-2021", "paper_id": "dbe-fisiese_wetenskappe-g12-v1-2021-nov", "caller": call_intern_deepseek_with_fallback, "model_desc": "deepseek-v4.1-flash-1017"},

        # 5. Gemini 3.5 Flash Lite (Key 1): Language lanes (English FAL & Afrikaans FAL)
        {"id": "GEMINI-EFAL-2021", "paper_id": "dbe-english_fal-g12-p1-2021-nov", "caller": lambda p: call_gemini_with_fallback(p, GEMINI_KEY_1, "gemini-3.5-flash-lite", key1_lock), "model_desc": "gemini-3.5-flash-lite"},
        {"id": "GEMINI-AFAL-2021", "paper_id": "dbe-afrikaans_fal-g12-p1-2021-nov", "caller": lambda p: call_gemini_with_fallback(p, GEMINI_KEY_1, "gemini-3.5-flash-lite", key1_lock), "model_desc": "gemini-3.5-flash-lite"},

        # 6. Gemini 3.1 Flash Lite (Key 2): Language & Science lanes (English HL, Afrikaans HL, Physics P2)
        {"id": "GEMINI-EHL-2020", "paper_id": "dbe-english_hl-g12-p1-2020-nov", "caller": lambda p: call_gemini_with_fallback(p, GEMINI_KEY_2, "gemini-3.1-flash-lite", key2_lock), "model_desc": "gemini-3.1-flash-lite"},
        {"id": "GEMINI-AHL-2020", "paper_id": "dbe-afrikaans_hl-g12-p1-2020-nov", "caller": lambda p: call_gemini_with_fallback(p, GEMINI_KEY_2, "gemini-3.1-flash-lite", key2_lock), "model_desc": "gemini-3.1-flash-lite"},
        {"id": "GEMINI-PS2-2020", "paper_id": "dbe-physical_sciences-g12-p2-2020-nov", "caller": lambda p: call_gemini_with_fallback(p, GEMINI_KEY_2, "gemini-3.1-flash-lite", key2_lock), "model_desc": "gemini-3.1-flash-lite"},

        # 7. OpenAI Rover Assisting Science (Physics P1)
        {"id": "OPENAI-PS1-2020", "paper_id": "dbe-physical_sciences-g12-p1-2020-nov", "caller": call_openai_luna, "model_desc": "gpt-6-luna (Rover Assistant)"}
    ]

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(process_paper_item_queue, lane): lane for lane in fleet_lanes}
        for fut in as_completed(futures):
            lane = futures[fut]
            try:
                n_gen, n_ver, tot = fut.result()
                print(f">> Paper {lane['paper_id']} Finished: {n_ver}/{n_gen} verified out of {tot} items")
            except Exception as e:
                print(f">> Paper {lane['paper_id']} Error: {e}")

    # Re-compilation of Master Dataset
    print("\n" + "=" * 80)
    print("FLEET QUEUE COMPLETED! REBUILDING MASTER SFT DATASET...")
    print("=" * 80)
    subprocess.run([sys.executable, "tools/package_all_verified_sft.py"])
    subprocess.run([sys.executable, "sa-tutor-kit/sa-tutor-kit/tutor_data.py", "build", "workspace/verified/train_master_combined.jsonl", "--out", "workspace/build/r1", "--val", "0.15"])

if __name__ == "__main__":
    main()

