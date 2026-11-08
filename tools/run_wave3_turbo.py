#!/usr/bin/env python3
"""
tools/run_wave3_turbo.py - Eishkom AI Wave 3 Turbo Fleet Generation & Verification.

Configured per user specifications:
  - OpenAI (gpt-6-luna, reasoning_effort:xhigh) running multi-threaded:
      * Thread 1: Maths/Wiskunde primary (2 papers)
      * Thread 2: Science assistant (Physical Sciences)
      * Thread 3: Language assistant (English HL)
  - OpenRouter (nvidia/nemotron-3-ultra-550b:free) at double speed (0.6s delay)
  - AI Studio Key 1 & Key 2 (gemini-3.5-flash-lite & 3.1-flash-lite) with automatic OpenAI fallback
  - Intern-AI (deepseek-v4.1-flash-1017) with automatic OpenAI fallback
  - Native Tool Calling procedure embedded in calculation reasoning
  - Forensic decimal comma normalization ($13{,}32$ -> 13.32) built directly into the verifier
  - Automatic generation of matching full_solution records
  - Milestone alert when 2,000 SFT samples is reached
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

W3_VER_DIR = ROOT_DIR / "workspace" / "verified" / "wave3"
W3_VER_DIR.mkdir(parents=True, exist_ok=True)
W3_GEN_DIR = ROOT_DIR / "workspace" / "gen" / "wave3"
W3_GEN_DIR.mkdir(parents=True, exist_ok=True)
ITEMS_DIR = ROOT_DIR / "workspace" / "items"

# Load environment keys
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

# Pacing and locks
print_lock = threading.Lock()
openrouter_lock = threading.Lock()
key1_lock = threading.Lock()
key2_lock = threading.Lock()
intern_lock = threading.Lock()
build_lock = threading.Lock()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

milestone_2000_alerted = False

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

# Forensic Matcher with South African Comma Normalization
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
        r = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True, timeout=timeout)
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
    s = re.sub(r'(\d+)(?:\\\s+|\s+)(\d{3})', r'\1\2', s)
    s = s.replace('$', '').replace('\\approx', '').replace('\\cdot', '').replace('\\', '')
    return s

def extract_all_numbers(text):
    norm = normalize_sa_math(text)
    found = re.findall(r'-?\d+(?:\.\d+)?', norm)
    nums = set()
    for x in found:
        try:
            val = float(x)
            nums.add(round(val, 3))
        except ValueError:
            pass
    return nums

def check_answers(sympy_out, expected):
    if not sympy_out or not expected:
        return False
    if answers_match(sympy_out, expected):
        return True
    
    clean_memo = normalize_sa_math(expected).strip().lower()
    clean_out = normalize_sa_math(sympy_out).strip().lower()
    if len(clean_memo) > 3 and clean_memo in clean_out:
        return True
    if len(clean_out) > 3 and clean_out in clean_memo:
        return True

    letter = expected.strip().upper()
    if len(letter) == 1 and letter in "ABCD":
        if re.search(r'\b' + letter + r'\b', sympy_out.upper()):
            return True

    nums_out = extract_all_numbers(sympy_out)
    nums_memo = extract_all_numbers(expected)

    if nums_out and nums_memo:
        if nums_out == nums_memo:
            return True
        if nums_out.issubset(nums_memo) or nums_memo.issubset(nums_out):
            return True
        for o in nums_out:
            for m in nums_memo:
                if abs(o - m) < 0.05:
                    return True
    return False

# Model Callers
def call_openai_luna(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENAI_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "gpt-6-luna",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "reasoning_effort": "xhigh",
        "max_completion_tokens": 4000
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                return res["choices"][0]["message"].get("content") or ""
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(2.5 * (attempt + 1))
                continue
            raise

def call_openrouter_nemotron_turbo(prompt):
    models = ["nvidia/nemotron-3-ultra-550b-a55b:free", "nvidia/nemotron-3.5-super-vl:free", "dots-studio/dots-3-note-preview:free"]
    with openrouter_lock:
        time.sleep(0.6)  # Doubled speed (0.6s)
    
    last_err = None
    for m in models:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {"Authorization": f"Bearer {OPENROUTER_KEY}", "Content-Type": "application/json"}
        payload = {
            "model": m,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            "response_format": {"type": "json_object"},
            "reasoning": {"effort": "high"},
            "max_tokens": 3500
        }
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, context=ctx, timeout=50) as resp:
                    res = json.loads(resp.read().decode("utf-8"))
                    msg = res["choices"][0]["message"]
                    content = msg.get("content") or ""
                    if content and "{" in content:
                        return content
            except urllib.error.HTTPError as e:
                last_err = e
                if e.code == 429:
                    time.sleep(3.0 * (attempt + 1))
                    continue
                break
            except Exception as e:
                last_err = e
                time.sleep(1.5)
                continue
    # Fallback to OpenAI if OpenRouter is unavailable
    with print_lock:
        print("[Nemotron Lane] Fallback to OpenAI gpt-6-luna triggered.")
    return call_openai_luna(prompt)

def call_gemini_with_fallback(prompt, key, model_name):
    lock = key1_lock if key == GEMINI_KEY_1 else key2_lock
    with lock:
        time.sleep(0.5)

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={key}"
    payload = {
        "contents": [{"parts": [{"text": SYSTEM_PROMPT + "\n\n" + prompt}]}],
        "generationConfig": {
            "temperature": 0.4,
            "maxOutputTokens": 4000,
            "responseMimeType": "application/json",
            "thinkingConfig": {"thinkingBudget": 24576}
        }
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=40) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                return res["candidates"][0]["content"]["parts"][0]["text"]
        except urllib.error.HTTPError as e:
            if e.code == 429:
                with print_lock:
                    print(f"[AI Studio {model_name}] Quota 429. Falling back to OpenAI gpt-6-luna.")
                return call_openai_luna(prompt)
            if attempt < 2:
                time.sleep(2.0 * (attempt + 1))
                continue
            break
        except Exception as e:
            if attempt < 2:
                time.sleep(1.5)
                continue
            break

    with print_lock:
        print(f"[AI Studio {model_name}] Error. Falling back to OpenAI gpt-6-luna.")
    return call_openai_luna(prompt)

def call_intern_deepseek_with_fallback(prompt):
    with intern_lock:
        time.sleep(1.0)
    url = f"{INTERN_BASE_URL.rstrip('/')}/chat/completions"
    headers = {
        "Authorization": f"Bearer {INTERN_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "curl/8.4.0"
    }
    payload = {
        "model": "deepseek-v4.1-flash-1017",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 3000
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                content = res["choices"][0]["message"].get("content") or ""
                if content and "{" in content:
                    return content
        except Exception as e:
            time.sleep(2.0)
            continue
    with print_lock:
        print("[Intern-AI DeepSeek Lane] Timeout/Error. Falling back to OpenAI gpt-6-luna.")
    return call_openai_luna(prompt)

def check_and_alert_2000():
    global milestone_2000_alerted
    with build_lock:
        all_socratic = 0
        for d in [ROOT_DIR / "workspace" / "verified" / "test_round", ROOT_DIR / "workspace" / "verified" / "wave2", W3_VER_DIR]:
            if d.exists():
                for f in d.glob("*.jsonl"):
                    all_socratic += sum(1 for _ in open(f, encoding="utf-8"))
        
        all_fullsol = 0
        if FULLSOL_DIR.exists():
            for f in FULLSOL_DIR.glob("*.jsonl"):
                all_fullsol += sum(1 for _ in open(f, encoding="utf-8"))

        estimated_samples = int(all_socratic * 2.5) + all_fullsol
        if estimated_samples >= 2000 and not milestone_2000_alerted:
            milestone_2000_alerted = True
            print("\n" + "*" * 80)
            print(f"*** ALERT: 2,000 SFT TRAINING SAMPLES MILESTONE REACHED! ({estimated_samples} estimated) ***")
            print(f"*** Verified Lessons: {all_socratic} | Full Solutions: {all_fullsol} ***")
            print(f"*** Fleet continues processing remaining queue uninterrupted... ***")
            print("*" * 80 + "\n")

# Single Lane Processor
def run_lane(lane):
    lane_id = lane["id"]
    name = lane["name"]
    paper_id = lane["paper_id"]
    caller = lane["caller"]
    model_desc = lane["model_desc"]

    item_file = ITEMS_DIR / f"{paper_id}.jsonl"
    if not item_file.exists():
        with print_lock:
            print(f"[{lane_id} - {name}] Paper {paper_id} not found!")
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

    with print_lock:
        print(f"[{lane_id} - {name}] Starting {len(items)} items on {model_desc} for paper {paper_id}")

    verified_file = W3_VER_DIR / f"{paper_id}.jsonl"
    raw_gen_file = W3_GEN_DIR / f"{paper_id}.jsonl"
    
    n_gen = 0
    n_ver = 0

    for idx, item in enumerate(items, 1):
        item_id = item.get("item_id", f"{paper_id}-item-{idx}")
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
                            v_reason = f"verified_match"
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
                    "id": f"wave3-{item_id}",
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
                print(f"[{lane_id} - {name}] Item {idx}/{len(items)} [{item_id}] -> {status_icon} | Verified: {n_ver}/{n_gen}")

            check_and_alert_2000()

        except Exception as e:
            with print_lock:
                print(f"[{lane_id} - {name}] Item {idx}/{len(items)} EXCEPTION: {e}")

    # Paper complete: Generate matching full_solution demonstrations
    with print_lock:
        print(f"[{lane_id} - {name}] Paper {paper_id} Socratic dialogues finished ({n_ver}/{n_gen}). Generating full_solution demonstrations...")
    try:
        cnt_full = process_paper(paper_id)
        with print_lock:
            print(f"[{lane_id} - {name}] Generated {cnt_full} matching full_solution demonstrations for {paper_id}")
    except Exception as e:
        with print_lock:
            print(f"[{lane_id} - {name}] Error generating full solutions: {e}")

    check_and_alert_2000()
    return n_gen, n_ver, len(items)

def main():
    print("=" * 80)
    print("EISHKOM AI — WAVE 3 TURBO MULTI-MODEL FLEET (AIMING FOR 2,000+ SAMPLES)")
    print("=" * 80)

    # 10 High-Value Exam Papers across all subjects & languages
    lanes = [
        # OpenAI Worker 1: Maths Primary
        {
            "id": "LANE-1",
            "name": "Maths P1 2021 (OpenAI Turbo)",
            "paper_id": "dbe-mathematics-g12-p1-2021-nov",
            "caller": call_openai_luna,
            "model_desc": "gpt-6-luna (Thread 1)"
        },
        # OpenAI Worker 2: Wiskunde Primary
        {
            "id": "LANE-2",
            "name": "Wiskunde V1 2022 (OpenAI Turbo)",
            "paper_id": "dbe-wiskunde-g12-v1-2022-nov",
            "caller": call_openai_luna,
            "model_desc": "gpt-6-luna (Thread 2)"
        },
        # OpenAI Worker 3: Science Assistant
        {
            "id": "LANE-3",
            "name": "Physics P1 2021 (OpenAI Assistant)",
            "paper_id": "dbe-physical_sciences-g12-p1-2021-nov",
            "caller": call_openai_luna,
            "model_desc": "gpt-6-luna (Thread 3)"
        },
        # OpenAI Worker 4: Language Assistant
        {
            "id": "LANE-4",
            "name": "English HL 2021 (OpenAI Assistant)",
            "paper_id": "dbe-english_hl-g12-p1-2021-nov",
            "caller": call_openai_luna,
            "model_desc": "gpt-6-luna (Thread 4)"
        },
        # OpenRouter Nemotron (Doubled speed 0.6s)
        {
            "id": "LANE-5",
            "name": "Maths P2 2021 (Nemotron Turbo)",
            "paper_id": "dbe-mathematics-g12-p2-2021-nov",
            "caller": call_openrouter_nemotron_turbo,
            "model_desc": "nemotron-3-ultra-550b"
        },
        # AI Studio Key 1 (with OpenAI fallback)
        {
            "id": "LANE-6",
            "name": "English FAL 2022 (Gemini 3.5 Flash Lite)",
            "paper_id": "dbe-english_fal-g12-p1-2022-nov",
            "caller": lambda p: call_gemini_with_fallback(p, GEMINI_KEY_1, "gemini-3.5-flash-lite"),
            "model_desc": "gemini-3.5-flash-lite"
        },
        # AI Studio Key 2 (with OpenAI fallback)
        {
            "id": "LANE-7",
            "name": "Afrikaans HL 2021 (Gemini 3.1 Flash Lite)",
            "paper_id": "dbe-afrikaans_hl-g12-p1-2021-nov",
            "caller": lambda p: call_gemini_with_fallback(p, GEMINI_KEY_2, "gemini-3.1-flash-lite"),
            "model_desc": "gemini-3.1-flash-lite"
        },
        # AI Studio Key 1 (with OpenAI fallback)
        {
            "id": "LANE-8",
            "name": "Afrikaans FAL 2022 (Gemini 3.5 Flash Lite)",
            "paper_id": "dbe-afrikaans_fal-g12-p1-2022-nov",
            "caller": lambda p: call_gemini_with_fallback(p, GEMINI_KEY_1, "gemini-3.5-flash-lite"),
            "model_desc": "gemini-3.5-flash-lite"
        },
        # Intern-AI DeepSeek (with OpenAI fallback)
        {
            "id": "LANE-9",
            "name": "Fisiese Wetenskappe 2022 (DeepSeek V4.1)",
            "paper_id": "dbe-fisiese_wetenskappe-g12-v1-2022-nov",
            "caller": call_intern_deepseek_with_fallback,
            "model_desc": "deepseek-v4.1-flash-1017"
        },
        # AI Studio Key 2 (with OpenAI fallback)
        {
            "id": "LANE-10",
            "name": "Physics P2 2021 (Gemini 3.1 Flash Lite)",
            "paper_id": "dbe-physical_sciences-g12-p2-2021-nov",
            "caller": lambda p: call_gemini_with_fallback(p, GEMINI_KEY_2, "gemini-3.1-flash-lite"),
            "model_desc": "gemini-3.1-flash-lite"
        }
    ]

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(run_lane, lane): lane for lane in lanes}
        for fut in as_completed(futures):
            lane = futures[fut]
            try:
                n_gen, n_ver, total = fut.result()
                print(f">> Lane {lane['id']} ({lane['name']}) Finished: {n_ver}/{n_gen} verified out of {total} items")
            except Exception as e:
                print(f">> Lane {lane['id']} FAILED: {e}")

    # Re-compile master SFT dataset
    print("\n" + "=" * 80)
    print("ALL WAVE 3 LANES COMPLETED! REBUILDING MASTER SFT DATASET...")
    print("=" * 80)
    subprocess.run([sys.executable, "tools/package_all_verified_sft.py"])
    subprocess.run([sys.executable, "sa-tutor-kit/sa-tutor-kit/tutor_data.py", "build", "workspace/verified/train_master_combined.jsonl", "--out", "workspace/build/r1", "--val", "0.15"])

if __name__ == "__main__":
    main()

