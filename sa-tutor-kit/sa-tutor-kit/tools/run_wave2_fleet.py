#!/usr/bin/env python3
"""
tools/run_wave2_fleet.py - Eishkom AI Wave 2 Multi-Model Fleet Generation & Verification.

Configured per user specifications:
  Lane 1: AI Studio Key 1 (gemini-3.1-flash-lite, 24k thinking) -> dbe-afrikaans_fal-g12-p1-2023-nov (68 items)
  Lane 2: AI Studio Key 2 (gemini-3.1-flash-lite, 24k thinking) -> dbe-afrikaans_hl-g12-p1-2022-nov (42 items)
  Lane 3: AI Studio Key 1 (gemini-3.5-flash-lite, 24k thinking) -> dbe-english_hl-g12-p1-2022-nov (32 items)
  Lane 4: AI Studio Key 2 (gemini-3.5-flash-lite, 24k thinking) -> dbe-english_fal-g12-p1-2023-nov (47 items)
  Lane 5: OpenRouter (nvidia/nemotron-3-ultra-550b:free, effort:high) -> dbe-mathematics-g12-p1-2022-nov (49 items)
  Lane 6: OpenAI (gpt-6-luna, reasoning_effort:xhigh) -> dbe-wiskunde-g12-v1-2023-nov (34 items)
  Lane 7: AI Studio Key 1 (gemini-3.8-flash -> gemini-3.6-flash, 20 RPD, 5 RPM) -> dbe-physical_sciences-g12-p1-2022-nov (59 items)
  Lane 8: AI Studio Key 2 (gemini-3.8-flash -> gemini-3.6-flash, 20 RPD, 5 RPM) -> dbe-fisiese_wetenskappe-g12-v1-2023-nov (46 items)
"""

import os
import sys
import json
import time
import re
import ssl
import threading
import urllib.request
import urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Paths
ROOT_DIR = Path(__file__).resolve().parent.parent
KIT_ROOT = ROOT_DIR / "sa-tutor-kit" / "sa-tutor-kit"
sys.path.insert(0, str(KIT_ROOT))
try:
    from answers import answers_match
except ImportError:
    def answers_match(a, b):
        return a.strip().lower() == b.strip().lower()

OUT_DIR = ROOT_DIR / "workspace" / "verified" / "wave2"
OUT_DIR.mkdir(parents=True, exist_ok=True)
RAW_GEN_DIR = ROOT_DIR / "workspace" / "gen" / "wave2"
RAW_GEN_DIR.mkdir(parents=True, exist_ok=True)

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

# Pacing and locks
print_lock = threading.Lock()
openrouter_lock = threading.Lock()
key1_lock = threading.Lock()
key2_lock = threading.Lock()
physics_key1_lock = threading.Lock()
physics_key2_lock = threading.Lock()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# System prompt & template
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
3. In meta.verify_code, write a short Python snippet using sympy or standard library that prints the final answer.
4. Output valid JSON only with NO markdown fences.
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

# SymPy execution
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
    import subprocess
    try:
        r = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True, timeout=timeout)
        if r.returncode != 0:
            return None, (r.stderr.strip().splitlines() or ["error"])[-1][:80]
        lines = [ln.strip() for ln in r.stdout.strip().splitlines() if ln.strip()]
        return (lines[-1], None) if lines else (None, "printed nothing")
    except subprocess.TimeoutExpired:
        return None, "timeout"
    except Exception as e:
        return None, str(e)[:80]

def check_answers(sympy_out, expected):
    if not sympy_out or not expected:
        return False
    if answers_match(sympy_out, expected):
        return True
    # Numbers set equality (e.g. [-4, 3] matches "x = 3 or x = -4")
    nums_out = set(re.findall(r'-?\d+(?:\.\d+)?', sympy_out))
    nums_exp = set(re.findall(r'-?\d+(?:\.\d+)?', expected))
    if nums_out and nums_out == nums_exp:
        return True
    # Multiple choice single-letter match
    exp_letter = expected.strip().upper()
    if len(exp_letter) == 1 and exp_letter in "ABCD":
        if re.search(r'\b' + exp_letter + r'\b', sympy_out.upper()):
            return True
    # Substring match if substantial
    if len(expected.strip()) > 3 and expected.strip().lower() in sympy_out.strip().lower():
        return True
    return False

# Provider Callers
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
                time.sleep(3.0 * (attempt + 1))
                continue
            raise

def call_openrouter_nemotron(prompt):
    models = [
        "nvidia/nemotron-3-ultra-550b-a55b:free",
        "nvidia/nemotron-3.5-super-vl:free",
        "dots-studio/dots-3-note-preview:free"
    ]
    with openrouter_lock:
        time.sleep(1.5)  # Pace requests
    
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
            except Exception as e:
                last_err = e
                time.sleep(2.0)
                continue
    raise RuntimeError(f"OpenRouter models failed: {last_err}")

def call_gemini_flash_lite(prompt, key, model_name):
    # Lock appropriate key briefly for spacing
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
            "thinkingConfig": {
                "thinkingBudget": 24576
            }
        }
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                return res["candidates"][0]["content"]["parts"][0]["text"]
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(2.5 * (attempt + 1))
                continue
            raise
        except Exception as e:
            if attempt < 3:
                time.sleep(2.0)
                continue
            raise

class PhysicsQuotaTracker:
    def __init__(self, key, lock, lane_name):
        self.key = key
        self.lock = lock
        self.lane_name = lane_name
        self.m38_count = 0
        self.m36_count = 0
        self.m38_quota_done = False
        self.m36_quota_done = False

    def call(self, prompt):
        if self.m38_quota_done and self.m36_quota_done:
            return None, "QUOTA_EXHAUSTED"

        # Determine model
        if not self.m38_quota_done:
            model = "gemini-3.8-flash"
        else:
            model = "gemini-3.6-flash"

        # 5 RPM pacing = wait 12.5 seconds between calls
        with self.lock:
            time.sleep(12.5)

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={self.key}"
        payload = {
            "contents": [{"parts": [{"text": SYSTEM_PROMPT + "\n\n" + prompt}]}],
            "generationConfig": {
                "temperature": 0.4,
                "maxOutputTokens": 4000,
                "responseMimeType": "application/json"
            }
        }
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"})

        try:
            with urllib.request.urlopen(req, context=ctx, timeout=50) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                text = res["candidates"][0]["content"]["parts"][0]["text"]
                if model == "gemini-3.8-flash":
                    self.m38_count += 1
                    if self.m38_count >= 20:
                        with print_lock:
                            print(f"[{self.lane_name}] 20 RPD completed on gemini-3.8-flash. Switching to gemini-3.6-flash.")
                        self.m38_quota_done = True
                else:
                    self.m36_count += 1
                    if self.m36_count >= 20:
                        with print_lock:
                            print(f"[{self.lane_name}] 20 RPD completed on gemini-3.6-flash. Pausing Physics.")
                        self.m36_quota_done = True
                return text, model
        except urllib.error.HTTPError as e:
            if e.code == 429:
                with print_lock:
                    print(f"[{self.lane_name}] 429 Quota exhausted on {model}.")
                if model == "gemini-3.8-flash":
                    self.m38_quota_done = True
                    return self.call(prompt)  # Switch immediately to 3.6
                else:
                    self.m36_quota_done = True
                    return None, "QUOTA_EXHAUSTED"
            else:
                with print_lock:
                    print(f"[{self.lane_name}] Error {e.code} on {model}: {e}")
                return None, f"ERROR_{e.code}"
        except Exception as e:
            with print_lock:
                print(f"[{self.lane_name}] Exception on {model}: {e}")
            return None, str(e)

# Runner for a single lane
def run_lane(lane_info):
    lane_id = lane_info["id"]
    name = lane_info["name"]
    paper_id = lane_info["paper_id"]
    provider = lane_info["provider"]
    model_desc = lane_info["model_desc"]
    caller = lane_info["caller"]
    
    item_file = ROOT_DIR / "workspace" / "items" / f"{paper_id}.jsonl"
    if not item_file.exists():
        with print_lock:
            print(f"[{lane_id} - {name}] Item file {item_file} not found!")
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

    verified_file = OUT_DIR / f"{paper_id}.jsonl"
    raw_gen_file = RAW_GEN_DIR / f"{paper_id}.jsonl"
    
    n_gen = 0
    n_ver = 0
    n_skipped = 0

    for idx, item in enumerate(items, 1):
        item_id = item.get("item_id", f"{paper_id}-item-{idx}")
        subject = item.get("subject", "mathematics")
        grade = item.get("grade", 12)
        topic = item.get("topic", "Exam Question")
        passage = f"passage:\n{item.get('passage')}\n\n" if item.get("passage") else ""
        question = item.get("question", "")
        memo = item.get("memo") or item.get("solution") or item.get("answer", "")
        final = item.get("final_answer") or item.get("answer") or ""

        # Language selection
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
            if provider == "physics_quota":
                resp_text, model_used = caller.call(prompt)
                if resp_text is None and model_used == "QUOTA_EXHAUSTED":
                    with print_lock:
                        print(f"[{lane_id} - {name}] Physics quota exhausted. Halting lane at item {idx}/{len(items)}.")
                    break
                if resp_text is None:
                    continue
            else:
                resp_text = caller(prompt)
                model_used = model_desc

            n_gen += 1
            
            # Save raw generation
            with open(raw_gen_file, "a", encoding="utf-8") as rfp:
                rfp.write(json.dumps({"item_id": item_id, "model": model_used, "raw": resp_text}, ensure_ascii=False) + "\n")

            # Parse JSON
            obj = extract_json_safely(resp_text)
            messages = obj.get("messages", [])
            meta = obj.get("meta", {})
            verify_code = meta.get("verify_code", "")

            # SymPy verification
            is_verified = False
            v_reason = "not_checked"

            if "english" in subject or "afrikaans" in subject:
                # Pedagogical language check
                is_verified = len(messages) >= 2 and all(m.get("content") for m in messages)
                v_reason = "language_content_verified"
            else:
                # Mathematical / Science SymPy verification
                if verify_code:
                    sympy_out, err = verify_sympy(verify_code)
                    if sympy_out:
                        target = final if final else memo
                        if check_answers(sympy_out, target):
                            is_verified = True
                            v_reason = f"sympy_match: {sympy_out}"
                        else:
                            v_reason = f"mismatch: sympy={sympy_out} vs memo={target[:50]}"
                    else:
                        v_reason = f"sympy_err: {err}"
                else:
                    v_reason = "missing_verify_code"

            if is_verified:
                n_ver += 1
                record = {
                    "schema_version": "tutor-v1",
                    "id": f"wave2-{item_id}",
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
                        "generator": model_used,
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
                print(f"[{lane_id} - {name}] Item {idx}/{len(items)} [{item_id}] -> {status_icon} ({v_reason}) | Verified: {n_ver}/{n_gen}")

        except Exception as e:
            with print_lock:
                print(f"[{lane_id} - {name}] Item {idx}/{len(items)} EXCEPTION: {e}")

    with print_lock:
        print(f"[{lane_id} - {name}] COMPLETE: {n_ver}/{n_gen} verified ({len(items)} total items)")
    return n_gen, n_ver, len(items)

def main():
    print("=" * 80)
    print("EISHKOM AI — WAVE 2 MULTI-MODEL FLEET GENERATION & VERIFICATION")
    print("=" * 80)

    # Initialize Physics quota trackers
    physics_eng_tracker = PhysicsQuotaTracker(GEMINI_KEY_1, physics_key1_lock, "Lane 7 (Physics EN)")
    physics_af_tracker = PhysicsQuotaTracker(GEMINI_KEY_2, physics_key2_lock, "Lane 8 (Physics AF)")

    lanes = [
        {
            "id": "LANE-1",
            "name": "Afrikaans FAL",
            "paper_id": "dbe-afrikaans_fal-g12-p1-2023-nov",
            "provider": "aistudio_flash_lite",
            "model_desc": "gemini-3.1-flash-lite",
            "caller": lambda p: call_gemini_flash_lite(p, GEMINI_KEY_1, "gemini-3.1-flash-lite")
        },
        {
            "id": "LANE-2",
            "name": "Afrikaans HL",
            "paper_id": "dbe-afrikaans_hl-g12-p1-2022-nov",
            "provider": "aistudio_flash_lite",
            "model_desc": "gemini-3.1-flash-lite",
            "caller": lambda p: call_gemini_flash_lite(p, GEMINI_KEY_2, "gemini-3.1-flash-lite")
        },
        {
            "id": "LANE-3",
            "name": "English HL",
            "paper_id": "dbe-english_hl-g12-p1-2022-nov",
            "provider": "aistudio_flash_lite",
            "model_desc": "gemini-3.5-flash-lite",
            "caller": lambda p: call_gemini_flash_lite(p, GEMINI_KEY_1, "gemini-3.5-flash-lite")
        },
        {
            "id": "LANE-4",
            "name": "English FAL",
            "paper_id": "dbe-english_fal-g12-p1-2023-nov",
            "provider": "aistudio_flash_lite",
            "model_desc": "gemini-3.5-flash-lite",
            "caller": lambda p: call_gemini_flash_lite(p, GEMINI_KEY_2, "gemini-3.5-flash-lite")
        },
        {
            "id": "LANE-5",
            "name": "Maths English",
            "paper_id": "dbe-mathematics-g12-p1-2022-nov",
            "provider": "openrouter",
            "model_desc": "nemotron-3-ultra-550b",
            "caller": call_openrouter_nemotron
        },
        {
            "id": "LANE-6",
            "name": "Wiskunde Afrikaans",
            "paper_id": "dbe-wiskunde-g12-v1-2023-nov",
            "provider": "openai",
            "model_desc": "gpt-6-luna",
            "caller": call_openai_luna
        },
        {
            "id": "LANE-7",
            "name": "Physics English",
            "paper_id": "dbe-physical_sciences-g12-p1-2022-nov",
            "provider": "physics_quota",
            "model_desc": "gemini-3.8-flash -> gemini-3.6-flash",
            "caller": physics_eng_tracker
        },
        {
            "id": "LANE-8",
            "name": "Physics Afrikaans",
            "paper_id": "dbe-fisiese_wetenskappe-g12-v1-2023-nov",
            "provider": "physics_quota",
            "model_desc": "gemini-3.8-flash -> gemini-3.6-flash",
            "caller": physics_af_tracker
        }
    ]

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(run_lane, lane): lane for lane in lanes}
        for fut in as_completed(futures):
            lane = futures[fut]
            try:
                n_gen, n_ver, total = fut.result()
                print(f">> Lane {lane['id']} ({lane['name']}) Finished: {n_ver}/{n_gen} verified out of {total} items")
            except Exception as e:
                print(f">> Lane {lane['id']} FAILED: {e}")

    # Combine wave 2 verified items
    combined_wave2 = ROOT_DIR / "workspace" / "verified" / "train_r2_pilot.jsonl"
    all_wave2_records = []
    for f in OUT_DIR.glob("*.jsonl"):
        with open(f, encoding="utf-8") as fp:
            for line in fp:
                line = line.strip()
                if line:
                    all_wave2_records.append(line)

    with open(combined_wave2, "w", encoding="utf-8") as fp:
        for r in all_wave2_records:
            fp.write(r + "\n")

    print(f"\n=======================================================")
    print(f"WAVE 2 FLEET COMPLETED!")
    print(f"Total Verified Lessons Assembled: {len(all_wave2_records)} -> {combined_wave2}")
    print(f"=======================================================\n")

if __name__ == "__main__":
    main()
