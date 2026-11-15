#!/usr/bin/env python3
"""
stage-2/run_stage2_fleet.py - Eishkom AI Stage 2 Multi-Model Fleet Generator.

KEY ARCHITECTURAL UPGRADES:
  1. 10 TEACHING STRATEGIES with weighted rotation across CAPS topics.
  2. SCRIPTED LEARNER PROGRESSIONS: Realistic turn-by-turn student simulation.
  3. TWO COACHING PROFILES:
     - Short / Fast-Track Mode (2 turns): For students who want rapid practice.
     - Deep-Dive Socratic Mode (3-4 turns): Patient step-by-step guidance.
  4. MANDATORY FORMULA & THOUGHT PROCESS BREAKDOWN:
     - STEM: Formula Breakdown (Formula, What the letters mean, Why we use it).
     - Languages: Concept & Thought Process (Rule, Mental Step-by-Step, DBE Mark Formula).
  5. 4x GEMINI LANGUAGE ACCELERATION:
     - Key 1: Gemini 3.5 Flash Lite + Gemini 3.1 Flash Lite (both on language lanes)
     - Key 2: Gemini 3.5 Flash Lite + Gemini 3.1 Flash Lite (language & science lanes)
     This clears the 3,400+ English & Afrikaans language items at maximum speed.
  6. ZERO EXTRA API CALLS FOR VERIFICATION:
     - STEM: Subprocess SymPy verification + LaTeX fraction/scientific notation/tolerance numeric match.
     - Languages: Deterministic rule-based rubric check.
  7. DEDICATED REJECTED FOLDER (workspace/rejected/stage2/):
     Every single rejected item is logged with full diagnostics for manual user inspection.
"""

import os
import sys
import json
import time
import re
import ssl
import random
import argparse
import threading
import subprocess
import urllib.request
import urllib.error
import functools
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict, deque

# Guarantee all output flushes immediately in background/realtime execution
print = functools.partial(print, flush=True)

# ── Path Setup ──────────────────────────────────────────────────────────────
ROOT_DIR = Path(__file__).resolve().parent.parent
KIT_ROOT = ROOT_DIR / "sa-tutor-kit" / "sa-tutor-kit"
STAGE2_DIR = Path(__file__).resolve().parent

sys.path.insert(0, str(KIT_ROOT))
sys.path.insert(0, str(ROOT_DIR / "tools"))
sys.path.insert(0, str(STAGE2_DIR))

try:
    from answers import answers_match
except ImportError:
    def answers_match(a, b):
        return a.strip().lower() == b.strip().lower()

try:
    from json_repair import repair_json
    HAS_JSON_REPAIR = True
except ImportError:
    HAS_JSON_REPAIR = False

from prompts.strategies import pick_strategy, pick_student_persona, classify_subject, STRATEGY_MAP
from prompts.few_shot_examples import get_few_shot_for_subject
from quality.rubric_checker import check_rubric, format_rubric_report, numeric_match
from convert_stage2_full_solutions import process_paper_s2
from compile_stage2_dataset import compile_corpus

# ── Output Directories (Strictly Stage 2; Never touch Stage 1) ──────────────
PASS_NUM = 1
S2_VER_DIR = ROOT_DIR / "workspace" / "verified" / "stage2"
S2_GEN_DIR = ROOT_DIR / "workspace" / "gen" / "stage2"
S2_REJ_DIR = ROOT_DIR / "workspace" / "rejected" / "stage2"
PROGRESS_FILE = STAGE2_DIR / "progress.json"

def init_pass_config(pass_num: int):
    global PASS_NUM, S2_VER_DIR, S2_GEN_DIR, S2_REJ_DIR, PROGRESS_FILE
    PASS_NUM = pass_num
    suffix = f"_pass{pass_num}" if pass_num > 1 else ""
    S2_VER_DIR = ROOT_DIR / "workspace" / "verified" / f"stage2{suffix}"
    S2_GEN_DIR = ROOT_DIR / "workspace" / "gen" / f"stage2{suffix}"
    S2_REJ_DIR = ROOT_DIR / "workspace" / "rejected" / f"stage2{suffix}"
    PROGRESS_FILE = STAGE2_DIR / f"progress{suffix}.json"
    S2_VER_DIR.mkdir(parents=True, exist_ok=True)
    S2_GEN_DIR.mkdir(parents=True, exist_ok=True)
    S2_REJ_DIR.mkdir(parents=True, exist_ok=True)

init_pass_config(1)
S2_FULLSOL_DIR = ROOT_DIR / "workspace" / "verified" / "stage2_full_solutions"
S2_FULLSOL_DIR.mkdir(parents=True, exist_ok=True)
ITEMS_DIR = ROOT_DIR / "workspace" / "items"

# ── Default Configuration ───────────────────────────────────────────────────
TARGET_VERIFIED = 15000      # Target verified Socratic lessons (~15,000 SFT samples)
MAX_PAPERS = 225             # Max papers to process per fleet run (all available untouched papers)
MAX_RETRIES_PER_ITEM = 2     # Retry failed items up to this many times
QUALITY_THRESHOLD = 50       # Minimum rubric score to pass

# ── Load API Keys ──────────────────────────────────────────────────────────
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
ENABLE_OPENAI = False        # Turned OFF by user command - Zero OpenAI calls
ENABLE_CEREBRAS = False      # Turned OFF by user command - Free credits depleted
OPENAI_KEY = ENV_KEYS.get("OPENAI_API_KEY", "") if ENABLE_OPENAI else ""
CEREBRAS_KEY = ENV_KEYS.get("CEREBRAS_API_KEY", "") if ENABLE_CEREBRAS else ""
OPENROUTER_KEY = ENV_KEYS.get("OPENROUTER_API_KEY", "")
GEMINI_KEY_1 = ENV_KEYS.get("GEMINI_API_KEY", "")
GEMINI_KEY_2 = ENV_KEYS.get("GEMINI_API_KEY_2", "") or GEMINI_KEY_1
GEMINI_KEY_3 = ENV_KEYS.get("GEMINI_API_KEY_3", "")
INTERN_KEY = ENV_KEYS.get("INTERN_API_KEY", "")
INTERN_BASE_URL = ENV_KEYS.get("INTERN_BASE_URL", "https://discovery-api.intern-ai.org.cn/v1")
GROQ_KEY = ENV_KEYS.get("GROQ_API_KEY", "")
NVIDIA_KEY = ENV_KEYS.get("NVIDIA_API_KEY", "")
COHERE_KEY = ENV_KEYS.get("COHERE_API_KEY", "iNTzE94EZk0t0ZGlgAudCE3eOHgqVHsL4KKX05Kh")
MAX_COHERE_MONTHLY_REQUESTS = 950
cohere_request_count = 0

DASHSCOPE_KEY = ENV_KEYS.get("DASHSCOPE_API_KEY", "")
VERCEL_KEY = ENV_KEYS.get("VERCEL_GATEWAY_API_KEY", "")
TOKENLAB_KEY = ENV_KEYS.get("TOKENLAB_API_KEY", "")
TOKENHARBOR_KEY = ENV_KEYS.get("TOKENHARBOUR_API_KEY", "")
KILO_KEY = ENV_KEYS.get("KILO_API_KEY", "")
APINEX_KEY = ENV_KEYS.get("APINEX_API_KEY", "")
APMIX_KEY = ENV_KEYS.get("APMIX_API_KEY", "")
REFUSELESS_KEY = ENV_KEYS.get("REFUSELESS_API_KEY", "")
LLM7_KEY = ENV_KEYS.get("LLM7_API_KEY", "")

# ── Thread Locks & Pacing ──────────────────────────────────────────────────
print_lock = threading.Lock()
key1_lock = threading.Lock()
key2_lock = threading.Lock()
key3_lock = threading.Lock()
openrouter_lock = threading.Lock()
intern_lock = threading.Lock()
openai_lock = threading.Lock()
groq_lock = threading.Lock()
cerebras_lock = threading.Lock()
cerebras_qwen_lock = threading.Lock()
cerebras_oss_lock = threading.Lock()
gma1_lock = threading.Lock()
gma2_lock = threading.Lock()
nvidia_lock = threading.Lock()
cohere_lock = threading.Lock()
dashscope_lock = threading.Lock()
vercel_lock = threading.Lock()
tokenlab_lock = threading.Lock()
tokenharbor_lock = threading.Lock()
kilo_lock = threading.Lock()
apinex_lock = threading.Lock()
apmix_lock = threading.Lock()
refuseless_lock = threading.Lock()
llm7_lock = threading.Lock()
stats_lock = threading.Lock()
progress_lock = threading.Lock()
reject_lock = threading.Lock()

last_call_time = defaultdict(float)

def pace_key(lock: threading.Lock, key_id: str, min_interval_sec: float = 1.0):
    with lock:
        now = time.time()
        elapsed = now - last_call_time[key_id]
        if elapsed < min_interval_sec:
            time.sleep(min_interval_sec - elapsed)
        last_call_time[key_id] = time.time()

# ── Global Stats ────────────────────────────────────────────────────────────
global_stats = {
    "total_generated": 0,
    "total_verified": 0,
    "total_rejected": 0,
    "total_rubric_failed": 0,
    "last_milestone": 0,
    "by_strategy": defaultdict(int),
    "by_subject": defaultdict(int),
    "by_model": defaultdict(int),
    "by_mode": defaultdict(int),
    "start_time": None,
    "papers_done": 0,
    "papers_total": 0,
}

# ══════════════════════════════════════════════════════════════════════════════
#  STAGE 2 PROMPT TEMPLATE
# ══════════════════════════════════════════════════════════════════════════════

SYSTEM_PROMPT = (
    "You are an expert South African CAPS curriculum teacher and a careful training-data author. "
    "You write ONE training record for a school tutor AI. "
    "Your output must be a single raw JSON object starting with { and ending with }. "
    "Do NOT write any text before or after the JSON. "
    "All your reasoning and thinking must go INSIDE the 'reasoning' fields of assistant messages. "
    "Do NOT write chain-of-thought or preamble outside the JSON."
)

TEMPLATE_V2 = """CRITICAL: START YOUR RESPONSE WITH {{ IMMEDIATELY. NO PREAMBLE TEXT.

=== QUALITY EXEMPLAR (follow this format and quality level) ===
{few_shot}

=== YOUR TASK: GENERATE A NEW RECORD ===

{strategy_instructions}

SOURCE ITEM:
subject: {subject}   grade: {grade}   topic: {topic}
{passage}question: {question}
memo / worked solution: {memo}
final answer from the memo: {final}

LEARNER SIMULATION:
- learner writes in: {lang}
- learner state: {state} ({state_desc})
- scripted learner turn trajectory: {learner_script}
  (The learner follows this trajectory; they make realistic slips/partial attempts first before understanding)
- total student messages: {turns} (first presents the problem, followed by replies following the script)
- coaching profile: {coaching_mode}

CONTROL BLOCK (embed in output):
{control}

OUTPUT FORMAT (one JSON object):
{{
  "messages": [
    {{"role": "user", "content": "..."}},
    {{"role": "assistant", "reasoning": "...", "content": "..."}},
    ...more turns alternating user and assistant...
  ],
  "meta": {{
    "strategy_used": "{strategy_name}",
    "final_answer": "{final}",
    "verify_code": "import sympy as sp\\n# solve and print final answer",
    "techniques": {techniques_json}
  }}
}}

RULES:
1. PEDAGOGY & SOCRATIC BOUNDARY:
   Ask ONE small diagnostic question at a time and wait. Do NOT reveal the full answer on turn 1.
2. FEEDBACK & PRAISE:
   React directly to what the student JUST wrote.
   NEVER open an assistant message with unearned reflexive praise like 'Exactly!', 'Presies!', 'Brilliant!', 'Perfek!', 'Spot on!', 'Great job!'.
   When the learner is correct, open with the content itself ("Yes, the gradient is 0 because...").
3. REASONING FIELD:
   In EVERY assistant message, include substantive 'reasoning' (teacher diagnosing the student's step and deciding the pedagogical move).
4. TOOL CALLS:
   {tool_instruction}
5. LANGUAGE CONSISTENCY:
   If the subject is in Afrikaans, the ENTIRE conversation (user and assistant) must be in natural, correct Afrikaans.
6. VERIFICATION CODE:
   {verify_code_instruction}
7. MANDATORY FINAL TURN STRUCTURE (CRITICAL):
{final_turn_instruction}
8. FORMAT INTEGRITY:
   Output valid JSON only — NO markdown code blocks, NO backticks around the JSON.
"""

# ══════════════════════════════════════════════════════════════════════════════
#  JSON EXTRACTION WITH JSON-REPAIR FALLBACK
# ══════════════════════════════════════════════════════════════════════════════

def extract_json_safely(text: str) -> dict:
    text = str(text).strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.I | re.S).strip()

    def find_balanced_json(s):
        start = s.find("{")
        if start == -1:
            return None
        depth = 0
        in_string = False
        escape = False
        for i in range(start, len(s)):
            c = s[i]
            if escape:
                escape = False
                continue
            if c == '\\':
                escape = True
                continue
            if c == '"':
                in_string = not in_string
                continue
            if in_string:
                continue
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    return s[start:i + 1]
        return None

    balanced = find_balanced_json(text)
    if balanced:
        for candidate in [balanced, re.sub(r',\s*([}\]])', r'\1', balanced)]:
            for c2 in [candidate, re.sub(r'\\(?![/"\\bfnrtu])', r'\\\\', candidate)]:
                try:
                    obj = json.loads(c2, strict=False)
                    if isinstance(obj, dict) and ("messages" in obj or "meta" in obj):
                        return obj
                except Exception:
                    pass

    if HAS_JSON_REPAIR:
        try:
            repaired = repair_json(text, return_objects=True)
            if isinstance(repaired, dict) and ("messages" in repaired or "meta" in repaired):
                return repaired
            if isinstance(repaired, list) and repaired and isinstance(repaired[0], dict):
                return repaired[0]
        except Exception:
            pass

    dec = json.JSONDecoder(strict=False)
    for variant in [text, re.sub(r'\\(?![/"\\bfnrtu])', r'\\\\', text)]:
        for m in re.finditer(r"\{", variant):
            try:
                obj, _ = dec.raw_decode(variant[m.start():])
                if isinstance(obj, dict) and ("messages" in obj or "meta" in obj):
                    return obj
            except Exception:
                continue

    raise ValueError(f"No valid JSON found in response ({len(text)} chars)")

# ══════════════════════════════════════════════════════════════════════════════
#  AUTOMATIC DATA REPAIR & SELF-HEALING ENGINE
# ══════════════════════════════════════════════════════════════════════════════

def auto_repair_record(record: dict, topic: str = "Exam Question", final_answer: str = "") -> dict:
    if not record or not isinstance(record, dict):
        return record

    messages = record.get("messages", [])
    if not messages or not isinstance(messages, list):
        return record

    repaired_msgs = []
    for idx, m in enumerate(messages):
        if not isinstance(m, dict):
            continue
        role = m.get("role", "user")
        content = (m.get("content") or "").strip()
        reasoning = (m.get("reasoning") or "").strip()

        # 1. Salvage assistant turn if content was cut off but reasoning exists
        if role == "assistant" and not content and reasoning:
            if idx == len(messages) - 1 and final_answer:
                content = (
                    f"**Final Answer:** {final_answer}\n\n"
                    f"### 📖 Concept Breakdown:\n"
                    f"Remember the key steps and rules to arrive at this answer.\n\n"
                    f"🎯 **Exam Tip:** Always show all substitutions and steps clearly to secure full marks!"
                )
            else:
                content = reasoning

        # 2. Strip banned reflexive praise words from assistant message openers
        if role == "assistant" and content:
            content = re.sub(
                r'^(?:exactly|presies|brilliant|perfek|spot on|great job|well done|pragtig|uitstekend)[!.,]?\s*',
                '', content, flags=re.I
            ).strip()
            if content:
                content = content[0].upper() + content[1:]

        # 3. Auto-populate missing reasoning on assistant turns
        if role == "assistant" and not reasoning:
            reasoning = f"Diagnosing the learner's response and guiding them through the next pedagogical step of {topic}."

        # 4. Filter out empty messages
        if content:
            entry = {"role": role, "content": content}
            if role == "assistant":
                entry["reasoning"] = reasoning
            repaired_msgs.append(entry)

    # 5. Guarantee dialogue starts on user turn
    if repaired_msgs and repaired_msgs[0].get("role") != "user":
        repaired_msgs.insert(0, {"role": "user", "content": f"How do I solve this question on {topic}?"})

    # 6. Guarantee dialogue ends on assistant turn (prune trailing hanging user turn)
    while len(repaired_msgs) >= 2 and repaired_msgs[-1].get("role") == "user":
        repaired_msgs.pop()

    record["messages"] = repaired_msgs
    return record

# ══════════════════════════════════════════════════════════════════════════════
#  SYMPY VERIFICATION
# ══════════════════════════════════════════════════════════════════════════════

ALLOWED_IMPORTS = {"sympy", "math", "fractions", "decimal", "itertools",
                   "statistics", "cmath", "numbers"}
BLOCKED = re.compile(
    r"\b(open|exec|eval|compile|__import__|input|globals|locals|getattr|setattr|breakpoint)\s*\(|"
    r"\b(os|sys|subprocess|socket|shutil|pathlib|requests|urllib|ctypes|pickle)\b", re.I
)

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
            capture_output=True, encoding="utf-8", errors="replace", timeout=timeout
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
            except Exception:
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

# ══════════════════════════════════════════════════════════════════════════════
#  API CALLERS (Gemini 3.1 & 3.5 Both Active on Both Keys)
# ══════════════════════════════════════════════════════════════════════════════

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
        "reasoning_effort": "medium",
        "max_completion_tokens": 8000
    }
    pace_key(openai_lock, "openai", min_interval_sec=0.25)
    for attempt in range(6):
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                choice = data["choices"][0]["message"]
                return choice.get("content") or choice.get("reasoning", "")
        except urllib.error.HTTPError as he:
            if he.code == 429:
                time.sleep(3.5 * (attempt + 1))
            else:
                time.sleep(1.5)
        except Exception:
            time.sleep(2.0 * (attempt + 1))
    raise RuntimeError("OpenAI gpt-6-luna failed after 6 attempts")

def call_gemini(prompt, api_key, model_name, lock, key_id):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": SYSTEM_PROMPT + "\n\n" + prompt}]}],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 8192,
            "thinkingConfig": {"thinkingBudget": 2048}
        }
    }
    pace_key(lock, key_id, min_interval_sec=1.2)
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, timeout=90) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                candidates = data.get("candidates", [])
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts", [])
                    texts = [p["text"] for p in parts if "text" in p]
                    return "\n".join(texts)
        except urllib.error.HTTPError as he:
            if he.code == 429:
                time.sleep(6.0 * (attempt + 1))
            else:
                time.sleep(2.0)
        except Exception:
            time.sleep(2.0)
    raise RuntimeError(f"Gemini {model_name} failed")

def call_gemini_language_safe(prompt, api_key, model_name, lock, key_id):
    """
    Dedicated language caller: Keeps all language generation strictly inside Gemini.
    Never falls back to OpenAI so OpenAI stays 100% focused on STEM.
    """
    for attempt in range(2):
        try:
            return call_gemini(prompt, api_key, model_name, lock, key_id)
        except Exception as e:
            # Fall back across Gemini Keys and Models
            alt_key = GEMINI_KEY_2 if (api_key == GEMINI_KEY_1 and GEMINI_KEY_2) else GEMINI_KEY_1
            alt_lock = key2_lock if alt_key == GEMINI_KEY_2 else key1_lock
            alt_id = "gem2_backup" if alt_key == GEMINI_KEY_2 else "gem1_backup"
            alt_model = "gemini-3.1-flash-lite" if "3.5" in model_name else "gemini-3.5-flash-lite"
            with print_lock:
                print(f"[{model_name}] Quota/Error ({e}) -> Trying {alt_model} on {alt_id}...")
            try:
                return call_gemini(prompt, alt_key, alt_model, alt_lock, alt_id)
            except Exception as e2:
                time.sleep(3.0 * (attempt + 1))
    # Final retry on primary
    return call_gemini(prompt, api_key, model_name, lock, key_id)

def call_gemma_aistudio(prompt, api_key, model_name, lock, key_id):
    """
    Dedicated caller for Gemma 4 models on Google AI Studio:
    - Strictly omits thinkingConfig (Gemma throws HTTP 400 with thinkingBudget).
    - Uses timeout=180s so multi-turn Socratic responses never hit premature read timeout.
    - Handles rate limiting (429) and transient 500s with progressive backoff.
    - Falls back across Key 1 and Key 2 if one hits a quota block.
    """
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": SYSTEM_PROMPT + "\n\n" + prompt}]}],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 6144
        }
    }
    timeout = 180
    pace_key(lock, key_id, min_interval_sec=1.0)
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                candidates = data.get("candidates", [])
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts", [])
                    texts = [p["text"] for p in parts if "text" in p]
                    res = "\n".join(texts).strip()
                    if res:
                        return res
        except urllib.error.HTTPError as he:
            if he.code == 429:
                wait_sec = 6.0 * (attempt + 1)
                with print_lock:
                    print(f"[{model_name} on {key_id}] 429 Rate Limit. Backing off {wait_sec}s...")
                time.sleep(wait_sec)
            elif he.code == 500:
                time.sleep(2.0 * (attempt + 1))
            else:
                time.sleep(1.5)
        except Exception as e:
            with print_lock:
                print(f"[{model_name} on {key_id}] Attempt {attempt+1}/4 failed ({e}). Retrying...")
            # Try alt key if available
            alt_key = GEMINI_KEY_2 if (api_key == GEMINI_KEY_1 and GEMINI_KEY_2) else GEMINI_KEY_1
            alt_lock = gma2_lock if alt_key == GEMINI_KEY_2 else gma1_lock
            try:
                time.sleep(1.5)
                alt_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={alt_key}"
                req = urllib.request.Request(alt_url, data=json.dumps(payload).encode("utf-8"), headers=headers)
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    candidates = data.get("candidates", [])
                    if candidates:
                        parts = candidates[0].get("content", {}).get("parts", [])
                        texts = [p["text"] for p in parts if "text" in p]
                        res = "\n".join(texts).strip()
                        if res:
                            return res
            except Exception:
                time.sleep(2.0 * (attempt + 1))
    raise RuntimeError(f"Gemma {model_name} failed on both keys after 4 attempts")

def call_openrouter_nemotron_turbo(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "HTTP-Referer": "https://eishkom.ai",
        "X-Title": "Eishkom AI Tutor Stage 2"
    }
    payload = {
        "model": "nvidia/nemotron-3-ultra-550b-a55b:free",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 4500,
        "reasoning": {"effort": "high"}
    }
    pace_key(openrouter_lock, "openrouter", min_interval_sec=0.8)
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, timeout=90) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                choice = data["choices"][0]["message"]
                return choice.get("content") or choice.get("reasoning", "")
        except urllib.error.HTTPError as he:
            if he.code == 429:
                time.sleep(4.0 * (attempt + 1))
            else:
                time.sleep(1.5)
        except Exception:
            time.sleep(1.5)
    with print_lock:
        print("[OpenRouter Nemotron] 429/Timeout -> Falling back to Gemini 3.5 Flash Lite on Key 1.")
    return call_gemini(prompt, GEMINI_KEY_1, "gemini-3.5-flash-lite", key1_lock, "gem1_35")

_ssl_ctx = ssl.create_default_context()
_ssl_ctx.check_hostname = False
_ssl_ctx.verify_mode = ssl.CERT_NONE

def call_intern_deepseek(prompt):
    """
    Direct Intern-AI API caller for DeepSeek:
    - Strictly runs on the free Intern-AI endpoint (zero OpenRouter cost).
    - Tries deepseek-v4-flash-0731 first (fast ~4.9s latency), with deepseek-v4.1-flash-1017 fallback.
    - Paces requests with 3.5s minimum interval to avoid 429 rate limit triggers.
    - Handles HTTP 429 with progressive backoff (5s, 10s, 15s).
    - Extracts both 'content' and 'reasoning_content' so chain-of-thought does not break parsing.
    """
    url = f"{INTERN_BASE_URL}/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {INTERN_KEY}",
        "User-Agent": "curl/8.4.0"
    }
    pace_key(intern_lock, "intern", min_interval_sec=3.5)
    for model_name in ["deepseek-v4.1-flash-1017"]:
        payload = {
            "model": model_name,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2,
            "max_tokens": 3000
        }
        for attempt in range(2):
            try:
                req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
                with urllib.request.urlopen(req, context=_ssl_ctx, timeout=45) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    choice = data["choices"][0]["message"]
                    content = choice.get("content") or choice.get("reasoning_content") or ""
                    if content:
                        return content
            except urllib.error.HTTPError as he:
                if he.code == 429:
                    wait_sec = 5.0 * (attempt + 1)
                    with print_lock:
                        print(f"[Intern-AI DeepSeek] 429 Rate Limit on {model_name}. Backing off {wait_sec}s...")
                    time.sleep(wait_sec)
                else:
                    time.sleep(2.0)
            except Exception as e:
                with print_lock:
                    print(f"[Intern-AI DeepSeek] {model_name} error: {e}")
                time.sleep(2.0)

    raise RuntimeError("Intern-AI DeepSeek failed on all models")

def call_groq(prompt, model_name="qwen/qwen3.8-27b"):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "curl/8.4.0"
    }
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 4096
    }
    pace_key(groq_lock, "groq", min_interval_sec=0.5)
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                c0 = data.get("choices", [{}])[0]
                if isinstance(c0, dict):
                    msg = c0.get("message", {})
                    if isinstance(msg, dict):
                        res = msg.get("content") or msg.get("reasoning") or ""
                        if res:
                            return str(res)
                    elif isinstance(msg, str):
                        return msg
                elif isinstance(c0, str):
                    return c0
        except urllib.error.HTTPError as he:
            if he.code == 429:
                time.sleep(3.0 * (attempt + 1))
            else:
                time.sleep(1.5)
        except Exception:
            time.sleep(1.5)
    raise RuntimeError(f"Groq {model_name} failed")

def call_cerebras(prompt, model_name="qwen-3.8-27b"):
    """
    Cerebras Wafer-Scale Engine caller:
    - qwen-3.8-27b has a 450 RPM quota (27,000/hr, 648,000/day): paced at 0.08s for blazing sub-second inference.
    - gpt-oss-120b has a strict 5 RPM quota (150/hr, 2,400/day): strictly paced at 12.5s to prevent 429 errors.
    - Captures both 'content' and 'reasoning' fields seamlessly.
    """
    url = "https://api.cerebras.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {CEREBRAS_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "curl/8.4.0"
    }
    is_qwen = "qwen" in model_name.lower()
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 6144 if is_qwen else 4096
    }
    if is_qwen:
        pace_key(cerebras_qwen_lock, "cerebras_qwen", min_interval_sec=0.08)
    else:
        pace_key(cerebras_oss_lock, "cerebras_oss", min_interval_sec=12.5)

    for attempt in range(3):
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, timeout=40) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                c0 = data.get("choices", [{}])[0]
                if isinstance(c0, dict):
                    msg = c0.get("message", {})
                    if isinstance(msg, dict):
                        res = msg.get("content") or msg.get("reasoning") or ""
                        if res:
                            return str(res)
                    elif isinstance(msg, str):
                        return msg
                elif isinstance(c0, str):
                    return c0
        except urllib.error.HTTPError as he:
            if he.code == 429:
                wait_sec = 2.0 if is_qwen else 15.0
                time.sleep(wait_sec * (attempt + 1))
            else:
                time.sleep(1.0)
        except Exception:
            time.sleep(1.0)
    raise RuntimeError(f"Cerebras {model_name} failed")

def call_nvidia(prompt, model_name):
    """
    NVIDIA NIM API caller:
    - Strictly paces at min_interval_sec=1.6 across all NVIDIA workers to keep combined RPM under 40.
    - Handles reasoning_content extraction seamlessly.
    """
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {NVIDIA_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "curl/8.4.0"
    }
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 4096
    }
    pace_key(nvidia_lock, "nvidia", min_interval_sec=1.6)
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                c0 = data.get("choices", [{}])[0]
                if isinstance(c0, dict):
                    msg = c0.get("message", {})
                    if isinstance(msg, dict):
                        res = msg.get("content") or msg.get("reasoning_content") or msg.get("reasoning") or ""
                        if res:
                            return str(res)
                    elif isinstance(msg, str):
                        return msg
                elif isinstance(c0, str):
                    return c0
        except urllib.error.HTTPError as he:
            if he.code == 429:
                time.sleep(4.0 * (attempt + 1))
            else:
                time.sleep(2.0)
        except Exception:
            time.sleep(2.0)
    raise RuntimeError(f"NVIDIA {model_name} failed")

def call_cohere(prompt, model_name):
    """
    Cohere v2 Chat API caller:
    - Enforces monthly request cap (MAX_COHERE_MONTHLY_REQUESTS = 950) to protect the 1,000 monthly free tier.
    - Extracts text content seamlessly from v2 blocks (including reasoning/thinking fallback).
    - Paces at min_interval_sec=0.5 to prevent bursts.
    """
    global cohere_request_count
    with cohere_lock:
        if cohere_request_count >= MAX_COHERE_MONTHLY_REQUESTS:
            raise RuntimeError(f"Cohere monthly limit reached ({cohere_request_count}/{MAX_COHERE_MONTHLY_REQUESTS})")
        cohere_request_count += 1

    url = "https://api.cohere.com/v2/chat"
    headers = {
        "Authorization": f"Bearer {COHERE_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "curl/8.4.0"
    }
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    }
    pace_key(cohere_lock, "cohere", min_interval_sec=0.5)
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                contents = data.get("message", {}).get("content", [])
                text_blocks = [c.get("text", "") for c in contents if c.get("type") == "text"]
                if not text_blocks:
                    text_blocks = [c.get("thinking", "") or c.get("text", "") for c in contents]
                res = "\n".join(text_blocks).strip()
                if res:
                    return res
        except urllib.error.HTTPError as he:
            if he.code == 429:
                time.sleep(3.0 * (attempt + 1))
            else:
                time.sleep(1.5)
        except Exception:
            time.sleep(1.5)
    raise RuntimeError(f"Cohere {model_name} failed")

# ── Generic OpenAI-Compatible Caller ─────────────────────────────────────────
def call_openai_compatible_api(prompt, base_url, api_key, model_name, lock, key_id, min_interval_sec=1.0, temperature=0.3, max_tokens=4096, extra_body=None, timeout=75):
    url = f"{base_url.rstrip('/')}/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens
    }
    if temperature is not None:
        payload["temperature"] = temperature
    if extra_body:
        payload.update(extra_body)

    pace_key(lock, key_id, min_interval_sec=min_interval_sec)
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                choice = data["choices"][0]["message"]
                res = choice.get("content") or choice.get("reasoning") or choice.get("reasoning_content") or ""
                if res.strip():
                    return res.strip()
        except urllib.error.HTTPError as he:
            if he.code == 429:
                wait_sec = 4.0 * (attempt + 1)
                time.sleep(wait_sec)
            else:
                time.sleep(1.5)
        except Exception:
            time.sleep(1.5)
    raise RuntimeError(f"{key_id} ({model_name}) failed after 3 attempts")

def call_dashscope(prompt, model_name="qwen3.8-flash", temperature=0.2):
    # Kimi models on DashScope forbid custom temperature
    t = None if "kimi" in model_name else temperature
    return call_openai_compatible_api(
        prompt=prompt,
        base_url="https://ws-kvneg1w4j01n4v80.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1",
        api_key=DASHSCOPE_KEY,
        model_name=model_name,
        lock=dashscope_lock,
        key_id="dashscope",
        min_interval_sec=0.05,
        temperature=t,
        timeout=120
    )

def call_vercel(prompt, model_name="nvidia/nemotron-3-ultra-550b-a55b"):
    return call_openai_compatible_api(
        prompt=prompt,
        base_url="https://ai-gateway.vercel.sh/v1",
        api_key=VERCEL_KEY,
        model_name=model_name,
        lock=vercel_lock,
        key_id="vercel",
        min_interval_sec=0.05
    )

def call_tokenlab(prompt, model_name="Gemma-4-31B-IT"):
    return call_openai_compatible_api(
        prompt=prompt,
        base_url="https://api.tokenlab.amd.com/v1",
        api_key=TOKENLAB_KEY,
        model_name=model_name,
        lock=tokenlab_lock,
        key_id="tokenlab",
        min_interval_sec=0.05
    )

def call_tokenharbor(prompt, model_name="deepseek-v4.1-flash:free"):
    return call_openai_compatible_api(
        prompt=prompt,
        base_url="https://tokenharbor.ai/v1",
        api_key=TOKENHARBOR_KEY,
        model_name=model_name,
        lock=tokenharbor_lock,
        key_id="tokenharbor",
        min_interval_sec=0.1
    )

def call_kilo(prompt, model_name="kilo-auto/free"):
    return call_openai_compatible_api(
        prompt=prompt,
        base_url="https://kilo.ai/api/gateway/v1",
        api_key=KILO_KEY,
        model_name=model_name,
        lock=kilo_lock,
        key_id="kilo",
        min_interval_sec=0.4
    )

def call_apinex(prompt, model_name="free/qwen-3.8-max"):
    return call_openai_compatible_api(
        prompt=prompt,
        base_url="https://api.apinex.bond/v1",
        api_key=APINEX_KEY,
        model_name=model_name,
        lock=apinex_lock,
        key_id="apinex",
        min_interval_sec=0.4
    )

def call_apmix(prompt, model_name="deepseek-v4.1-flash-1017-free"):
    return call_openai_compatible_api(
        prompt=prompt,
        base_url="https://api.apmix.ai/v1",
        api_key=APMIX_KEY,
        model_name=model_name,
        lock=apmix_lock,
        key_id="apmix",
        min_interval_sec=0.1
    )

def call_refuseless(prompt, model_name="deepseek-v4.1-flash-abliterated-free"):
    return call_openai_compatible_api(
        prompt=prompt,
        base_url="https://api.refuseless.com/v1",
        api_key=REFUSELESS_KEY,
        model_name=model_name,
        lock=refuseless_lock,
        key_id="refuseless",
        min_interval_sec=0.3
    )

def call_llm7(prompt, model_name="default"):
    return call_openai_compatible_api(
        prompt=prompt,
        base_url="https://api.llm7.io/v1",
        api_key=LLM7_KEY,
        model_name=model_name,
        lock=llm7_lock,
        key_id="llm7",
        min_interval_sec=0.2
    )
    return call_openai_compatible_api(
        prompt=prompt,
        base_url="https://api.llm7.io/v1",
        api_key=LLM7_KEY,
        model_name=model_name,
        lock=llm7_lock,
        key_id="llm7",
        min_interval_sec=1.5
    )


# ══════════════════════════════════════════════════════════════════════════════
#  DEDUPLICATION & PAPER DISCOVERY
# ══════════════════════════════════════════════════════════════════════════════

def load_stage1_used_papers() -> set:
    used = set()
    ver_base = ROOT_DIR / "workspace" / "verified"
    for subdir in ["test_round", "wave2", "wave3", "wave4", "wave5", "full_solutions"]:
        d = ver_base / subdir
        if d.exists():
            for f in d.glob("*.jsonl"):
                used.add(f.stem)

    master_file = ver_base / "train_master_combined.jsonl"
    if master_file.exists():
        with open(master_file, encoding="utf-8") as fp:
            for line in fp:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                    m = rec.get("meta", {})
                    pid = m.get("paper_id")
                    if not pid and m.get("item_id"):
                        parts = m["item_id"].split("-")
                        if len(parts) >= 6:
                            pid = "-".join(parts[:6])
                    if pid:
                        used.add(pid)
                except Exception:
                    pass
    return used

def find_item_file(paper_id: str) -> Path:
    flat = ITEMS_DIR / f"{paper_id}.jsonl"
    if flat.exists():
        return flat
    for subject_dir in ITEMS_DIR.iterdir():
        if subject_dir.is_dir():
            nested = subject_dir / f"{paper_id}.jsonl"
            if nested.exists():
                return nested
    return flat

def classify_subject_granular(name_or_id: str) -> str:
    s = str(name_or_id).lower().strip()
    if "wiskunde" in s:
        return "math_af"
    elif any(k in s for k in ["math", "mathematics"]):
        return "math_en"
    elif any(k in s for k in ["fisiese", "wetenskap"]):
        return "sci_af"
    elif any(k in s for k in ["phys", "science"]):
        return "sci_en"
    elif "afrikaans" in s:
        return "lang_af"
    elif "english" in s:
        return "lang_en"
    return "lang_en"

def discover_untouched_papers(stage1_papers: set) -> list:
    available = []
    seen_paper_ids = set()

    if not ITEMS_DIR.exists():
        return available

    for subject_dir in ITEMS_DIR.iterdir():
        if subject_dir.is_dir():
            for f in subject_dir.glob("*.jsonl"):
                paper_id = f.stem
                if paper_id in seen_paper_ids or paper_id in stage1_papers:
                    continue
                seen_paper_ids.add(paper_id)
                try:
                    count = sum(1 for line in open(f, encoding="utf-8") if line.strip())
                    cat = classify_subject_granular(paper_id)
                    available.append((paper_id, count, cat))
                except Exception:
                    pass

    for f in ITEMS_DIR.glob("*.jsonl"):
        paper_id = f.stem
        if paper_id in seen_paper_ids or paper_id in stage1_papers:
            continue
        seen_paper_ids.add(paper_id)
        try:
            count = sum(1 for line in open(f, encoding="utf-8") if line.strip())
            cat = classify_subject_granular(paper_id)
            available.append((paper_id, count, cat))
        except Exception:
            pass

    available.sort(key=lambda x: x[1], reverse=True)
    return available

# ══════════════════════════════════════════════════════════════════════════════
#  REJECTION AUDIT LOGGING
# ══════════════════════════════════════════════════════════════════════════════

def log_rejected_item(paper_id: str, item_id: str, model_desc: str, strategy: str,
                      rejection_reason: str, sympy_out: str, memo_target: str,
                      verify_code: str, rubric_score: int, rubric_issues: list,
                      parsed_record: dict, raw_response: str):
    rej_file = S2_REJ_DIR / f"{paper_id}.jsonl"
    rej_entry = {
        "timestamp": datetime.now().isoformat(),
        "paper_id": paper_id,
        "item_id": item_id,
        "model": model_desc,
        "strategy": strategy,
        "rejection_reason": rejection_reason,
        "sympy_out": sympy_out,
        "memo_target": memo_target,
        "verify_code": verify_code,
        "rubric_score": rubric_score,
        "rubric_issues": rubric_issues,
        "parsed_record": parsed_record,
        "raw_response": raw_response
    }
    with reject_lock:
        with open(rej_file, "a", encoding="utf-8") as rfp:
            rfp.write(json.dumps(rej_entry, ensure_ascii=False) + "\n")

# ══════════════════════════════════════════════════════════════════════════════
#  PROGRESS TRACKING
# ══════════════════════════════════════════════════════════════════════════════

def save_progress(data: dict):
    with progress_lock:
        PROGRESS_FILE.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")

def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        try:
            return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"completed_papers": [], "started_at": None}

# ══════════════════════════════════════════════════════════════════════════════
#  CORE PAPER PROCESSOR (With Adaptive Breakdown & Dual Modes)
# ══════════════════════════════════════════════════════════════════════════════

def process_paper_stage2(lane: dict) -> tuple:
    lane_id = lane["id"]
    paper_id = lane["paper_id"]
    caller = lane["caller"]
    model_desc = lane["model_desc"]
    provider = lane.get("provider", "unknown")

    item_file = find_item_file(paper_id)
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
                except Exception:
                    pass

    if not items:
        return 0, 0, 0

    gen_file = S2_GEN_DIR / f"{paper_id}.jsonl"
    ver_file = S2_VER_DIR / f"{paper_id}.jsonl"

    done_items = set()
    if gen_file.exists():
        with open(gen_file, encoding="utf-8") as fp:
            for line in fp:
                try:
                    rec = json.loads(line)
                    if "item_id" in rec:
                        done_items.add(rec["item_id"])
                except Exception:
                    pass

    with print_lock:
        print(f"[{lane_id}] Starting {paper_id} ({len(items)} items, {len(done_items)} already done) on {model_desc}")

    n_gen = len(done_items)
    n_ver = sum(1 for _ in open(ver_file, encoding="utf-8")) if ver_file.exists() else 0

    used_strategies = set()

    pass1_strategies = {}
    if PASS_NUM > 1:
        p1_file = ROOT_DIR / "workspace" / "verified" / "stage2" / f"{paper_id}.jsonl"
        if p1_file.exists():
            with open(p1_file, encoding="utf-8") as fp:
                for line in fp:
                    try:
                        rec = json.loads(line)
                        iid = rec.get("id") or rec.get("item_id") or rec.get("meta", {}).get("item_id")
                        strat = rec.get("meta", {}).get("strategy_used")
                        if iid and strat:
                            base_id = iid.replace("_p2", "")
                            pass1_strategies[base_id] = strat
                            pass1_strategies[iid] = strat
                    except Exception:
                        pass

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
        marks = item.get("marks", 2)

        is_af = "afrikaans" in subject.lower() or "wiskunde" in subject.lower() or "wetenskappe" in subject.lower()
        lang = "af" if is_af else "en"
        cat = classify_subject(subject)
        is_lang_subj = (cat == "language")

        exclude_strategies = set(used_strategies)
        p1_strat = pass1_strategies.get(item_id)
        if p1_strat:
            exclude_strategies.add(p1_strat)

        strategy = pick_strategy(subject, exclude=exclude_strategies)
        used_strategies.add(strategy["name"])
        if len(used_strategies) >= 8:
            used_strategies.clear()

        # ── Dual Coaching Profile (Short Mode vs Deep-Dive Mode) ──
        is_short_mode = (random.random() < 0.35)  # 35% Short Mode, 65% Deep-Dive Mode
        persona = pick_student_persona(subject, marks=marks)

        if is_short_mode:
            persona["turns"] = 2
            resp_length = "short"
            coaching_mode = "Short / Fast-Track Mode (2 turns: quick diagnostic question, student attempts, tutor delivers answer + simple breakdown for rapid practice)"
            few_shot = get_few_shot_for_subject(subject, mode="short")
            mode_tag = "short"
        else:
            resp_length = "medium"
            coaching_mode = "Deep-Dive Socratic Mode (3-4 turns: patient step-by-step guidance diagnosing misconceptions before the final breakdown)"
            few_shot = get_few_shot_for_subject(subject, mode="normal")
            mode_tag = "deep"

        ctrl = {
            "subject": subject,
            "grade": grade,
            "subject_language": lang,
            "response_language": "mirror",
            "strategy": strategy["name"],
            "answer_policy": "guided",
            "student_level": persona["student_level"],
            "tone": "encouraging" if persona["state"] in ("blank_stuck", "exam_panic", "wants_answer_only") else "calm_neutral",
            "response_length": resp_length,
            "tools": ["calculator", "board"] if not is_lang_subj else [],
            "math_format": "latex"
        }

        # Subject-specific instructions
        if is_lang_subj:
            tool_instr = "DO NOT emit any tool calls. Language subjects must never call a calculator."
            verify_instr = "Leave verify_code as an empty string \"\"."
            if lang == "af":
                final_turn_instr = (
                    "   In die FINALE boodskap MOET jy insluit:\n"
                    "   a) Die volledige KABV-modelantwoord wat ooreenstem met die memorandum.\n"
                    "   b) '### 📖 Begrip & Denkwyse (Hoe om dit te Verstaan):'\n"
                    "      * Die Reël / Stylfiguur: [verduidelik die grammatikareël, stylfiguur of konsep duidelik]\n"
                    "      * Die Denkwyse (Stap-vir-Stap): [verduidelik hoe 'n student die vraag moet ontleed]\n"
                    "      * Hoe KABV-Nasieners Punte Toeken: [die 3-punt formule vir volpunte]\n"
                    "   c) '🎯 Eksamen-wenk:' [praktiese nasienriglyn of algemene slaggat om te vermy]"
                )
            else:
                final_turn_instr = (
                    "   In the FINAL assistant message, you MUST include:\n"
                    "   a) The complete model answer matching the memo.\n"
                    "   b) '### 📖 Concept & Thought Process (How to Understand It):'\n"
                    "      * The Concept / Rule: [explain the grammar rule, literary device, or comprehension concept clearly]\n"
                    "      * The Thought Process (How to Unpack It): [break down the mental method to analyze the question step by step]\n"
                    "      * How DBE Markers Score It: [explain the mark allocation breakdown for full marks]\n"
                    "   c) '🎯 Exam Tip:' [practical exam technique or common pitfall to avoid]"
                )
        else:
            tool_instr = (
                "In your private reasoning, demonstrate the calculation as:\n"
                "   [TOOL CHECK: calculator(expression=\"...\") -> result]\n"
                "   Never use placeholder expressions like 1+1, 0+0, or 'custom'."
            )
            verify_instr = "In meta.verify_code, write a short Python snippet using sympy that prints the final answer."
            if lang == "af":
                final_turn_instr = (
                    "   In die FINALE boodskap MOET jy insluit:\n"
                    "   a) Die finale antwoord wat ooreenstem met die memorandum.\n"
                    "   b) '### 📖 Formule & Reël-Uiteensetting (Hoe dit werk):'\n"
                    "      * Die Formule / Reël: [skryf die formule duidelik in KaTeX neer]\n"
                    "      * Wat die letters beteken:\n"
                    "        * [letter 1]: [betekenis in eenvoudige taal]\n"
                    "        * [letter 2]: [betekenis in eenvoudige taal]\n"
                    "      * Waarom ons dit gebruik: [verduidelik in eenvoudige, vriendelike terme waarom dit werk]\n"
                    "   c) '🎯 Eksamen-wenk:' [punte-toekenning of formule-wenk vir die eksamen]"
                )
            else:
                final_turn_instr = (
                    "   In the FINAL assistant message, you MUST include:\n"
                    "   a) The consolidated final answer matching the memo.\n"
                    "   b) '### 📖 Formula Breakdown (How It Works):'\n"
                    "      * The Formula: [state the exact formula in KaTeX clearly]\n"
                    "      * What the letters mean:\n"
                    "        * [letter 1]: [meaning in plain everyday language]\n"
                    "        * [letter 2]: [meaning in plain everyday language]\n"
                    "      * Why we use it: [explain in simple, accessible, friendly terms why it works and why we chose it]\n"
                    "   c) '🎯 Exam Tip:' [mark allocation tip or common exam pitfall to avoid]"
                )

        prompt = TEMPLATE_V2.format(
            few_shot=few_shot,
            strategy_instructions=strategy["prompt_fragment"],
            subject=subject,
            grade=grade,
            topic=topic,
            passage=passage,
            question=question,
            memo=memo,
            final=final,
            lang=lang,
            state=persona["state"],
            state_desc=persona["desc"],
            learner_script=" -> ".join(persona["script"][:persona["turns"]-1]),
            turns=persona["turns"],
            coaching_mode=coaching_mode,
            control=json.dumps(ctrl, indent=2),
            strategy_name=strategy["name"],
            techniques_json=json.dumps(persona["techniques"]),
            tool_instruction=tool_instr,
            verify_code_instruction=verify_instr,
            final_turn_instruction=final_turn_instr,
        )

        for attempt in range(MAX_RETRIES_PER_ITEM + 1):
            resp_text = ""
            parsed_obj = None
            rejection_reason = "unprocessed"
            sympy_out = None
            verify_code = ""
            rubric_score = 0
            rubric_issues = []

            try:
                resp_text = caller(prompt)
                n_gen += 1
                done_items.add(item_id)

                with open(gen_file, "a", encoding="utf-8") as rfp:
                    rfp.write(json.dumps({
                        "item_id": item_id,
                        "model": model_desc,
                        "strategy": strategy["name"],
                        "persona_state": persona["state"],
                        "mode": mode_tag,
                        "attempt": attempt + 1,
                        "raw": resp_text
                    }, ensure_ascii=False) + "\n")

                parsed_obj = extract_json_safely(resp_text)
                if not isinstance(parsed_obj, dict):
                    raise ValueError(f"Extracted JSON is not a dictionary (type={type(parsed_obj).__name__})")

                # ── Auto-Repair & Self-Healing Engine ──
                target_ans = final if final else memo
                parsed_obj = auto_repair_record(parsed_obj, topic=topic, final_answer=target_ans)
                if not isinstance(parsed_obj, dict):
                    raise ValueError("auto_repair_record returned a non-dictionary")
                raw_msgs = parsed_obj.get("messages")
                if not isinstance(raw_msgs, list):
                    raw_msgs = []
                messages = [m for m in raw_msgs if isinstance(m, dict)]
                parsed_obj["messages"] = messages
                meta = parsed_obj.get("meta", {})
                if not isinstance(meta, dict):
                    meta = {}
                parsed_obj["meta"] = meta
                verify_code = meta.get("verify_code", "")

                # ── Verification Check 1: Mathematical Accuracy (STEM) ──
                is_math_verified = False
                v_math_reason = "not_checked"

                if is_lang_subj:
                    is_math_verified = len(messages) >= 2 and all(len((m.get("content") or "").strip()) > 0 for m in messages)
                    v_math_reason = "language_content_verified"
                else:
                    # Check A: SymPy execution
                    if verify_code:
                        sympy_out, err = verify_sympy(verify_code)
                        if sympy_out and check_answers(sympy_out, target_ans):
                            is_math_verified = True
                            v_math_reason = "sympy_verified_match"
                        elif sympy_out:
                            v_math_reason = f"mismatch: sympy={sympy_out[:30]} vs memo={target_ans[:30]}"
                        else:
                            v_math_reason = f"sympy_err: {err}"

                    # Check B: Fallback numeric tolerance matching on final turn (3% tolerance)
                    if not is_math_verified and messages:
                        final_asst = messages[-1].get("content", "")
                        num_ok = numeric_match(final_asst, target_ans, rel_tol=0.03)
                        if num_ok is True:
                            is_math_verified = True
                            v_math_reason = "numeric_tolerance_match"

                    # Check C: Text / keyword containment match on final turn
                    if not is_math_verified and messages:
                        final_asst = (messages[-1].get("content") or "").lower()
                        t_clean = normalize_sa_math(target_ans).lower()
                        if t_clean and t_clean in normalize_sa_math(final_asst).lower():
                            is_math_verified = True
                            v_math_reason = "text_memo_match"
                        elif target_ans.lower().strip() in final_asst and len(target_ans.strip()) >= 2:
                            is_math_verified = True
                            v_math_reason = "text_memo_match"

                # ── Verification Check 2: Deterministic Rubric Quality ──
                rubric_passed, rubric_issues, rubric_score = check_rubric(
                    parsed_obj,
                    expected_strategy=strategy["name"],
                    expected_lang=lang,
                    is_language_subject=is_lang_subj,
                    min_turns=2
                )

                # Final determination (Zero LLM judge calls!)
                is_verified = is_math_verified and (rubric_passed or rubric_score >= 50)

                if is_verified:
                    n_ver += 1
                    record = {
                        "schema_version": "tutor-v2",
                        "id": f"s2-{item_id}",
                        "group_id": str(item_id),
                        "control": ctrl,
                        "thinking": "on",
                        "messages": messages,
                        "meta": {
                            "topic": topic,
                            "task_type": "comprehension" if is_lang_subj else "solve_problem",
                            "student_language": lang,
                            "strategy_used": strategy["name"],
                            "student_state": persona["state"],
                            "coaching_mode": mode_tag,
                            "source_type": "past_paper_adapted",
                            "source_licence": "DBE Open Educational Resource",
                            "generator": model_desc,
                            "provider": provider,
                            "lane_id": lane_id,
                            "answer_verified": True,
                            "verification_method": v_math_reason,
                            "rubric_score": rubric_score,
                            "split": "auto",
                            "final_answer": final or memo[:100],
                            "verify_code": verify_code,
                            "paper_id": paper_id,
                            "item_id": item_id if PASS_NUM == 1 else f"{item_id}_p2",
                            "pass": PASS_NUM,
                            "stage": f"stage-2-pass{PASS_NUM}" if PASS_NUM > 1 else "stage-2",
                            "pass1_strategy": p1_strat if PASS_NUM > 1 else None,
                            "techniques": meta.get("techniques", persona["techniques"])
                        }
                    }
                    with open(ver_file, "a", encoding="utf-8") as vfp:
                        vfp.write(json.dumps(record, ensure_ascii=False) + "\n")

                    with print_lock:
                        strat_tag = strategy["name"][:14]
                        print(f"[{lane_id}] {idx}/{len(items)} [{item_id}] {strat_tag} ({mode_tag}) -> PASS "
                              f"(rubric:{rubric_score}, math:{v_math_reason[:18]}) | V:{n_ver}/{n_gen}")

                    with stats_lock:
                        global_stats["total_generated"] += 1
                        global_stats["total_verified"] += 1
                        global_stats["by_strategy"][strategy["name"]] += 1
                        global_stats["by_subject"][subject] += 1
                        global_stats["by_model"][model_desc] += 1
                        global_stats["by_mode"][mode_tag] += 1

                        cur_v = global_stats["total_verified"]
                        last_ms = global_stats.get("last_milestone", 0)
                        should_fire_ms = False
                        if cur_v >= last_ms + 1000:
                            global_stats["last_milestone"] = (cur_v // 1000) * 1000
                            should_fire_ms = True
                            ms_target = global_stats["last_milestone"]

                    if should_fire_ms:
                        print_milestone_report(ms_target)
                    break

                else:
                    rejection_reason = f"math:{v_math_reason} | rubric:{', '.join(rubric_issues) or 'score_below_threshold'}"
                    log_rejected_item(
                        paper_id=paper_id,
                        item_id=item_id,
                        model_desc=model_desc,
                        strategy=strategy["name"],
                        rejection_reason=rejection_reason,
                        sympy_out=sympy_out or "",
                        memo_target=final if final else memo,
                        verify_code=verify_code,
                        rubric_score=rubric_score,
                        rubric_issues=rubric_issues,
                        parsed_record=parsed_obj or {},
                        raw_response=resp_text
                    )

                    with print_lock:
                        strat_tag = strategy["name"][:14]
                        print(f"[{lane_id}] {idx}/{len(items)} [{item_id}] {strat_tag} -> REJECT "
                              f"({rejection_reason[:40]}) -> Saved to workspace/rejected/stage2/")

                    if attempt < MAX_RETRIES_PER_ITEM:
                        continue

                    with stats_lock:
                        global_stats["total_generated"] += 1
                        global_stats["total_rejected"] += 1
                    break

            except Exception as e:
                with print_lock:
                    print(f"[{lane_id}] Item {idx}/{len(items)} API RETRY ({attempt + 1}/{MAX_RETRIES_PER_ITEM + 1}): {e}")
                if attempt < MAX_RETRIES_PER_ITEM:
                    time.sleep(2.0 * (attempt + 1))
                    continue
                break

    if PASS_NUM == 1:
        try:
            cnt_full = process_paper_s2(paper_id)
            if cnt_full > 0:
                with print_lock:
                    print(f"[{lane_id}] Paper {paper_id} -> {cnt_full} Stage 2 full_solution demos generated")
        except Exception as e:
            with print_lock:
                print(f"[{lane_id}] Full solution error: {e}")

    with stats_lock:
        global_stats["papers_done"] += 1
    save_progress_snapshot()

    return n_gen, n_ver, len(items)

# ══════════════════════════════════════════════════════════════════════════════
#  FLEET ASSIGNMENT (4x Gemini Workers on Both Keys)
# ══════════════════════════════════════════════════════════════════════════════

def assign_callers():
    callers = []

    # ══════════════════════════════════════════════════════════════════════════
    # PRIORITY 1: NEW EXTERNAL FLEET WORKERS (Alibaba, Vercel, AMD, Kilo, APInex, APMix, Refuseless, TokenHarbor)
    # ══════════════════════════════════════════════════════════════════════════

    # ── Alibaba Model Studio (Active Quota Models: deepseek-v4.1-flash, qwen3-vl-plus, qwen3.7-flash, qwen3.8-flash, qwen3.7-max, deepseek-v4.1-flash-1017, deepseek-v4-pro-0813, deepseek-v4-pro) ──
    if DASHSCOPE_KEY:
        callers.append({
            "caller": lambda p: call_dashscope(p, "qwen3.8-flash"),
            "model_desc": "qwen3.8-flash",
            "affinity": ["math_en", "math_af"],
            "id_prefix": "ALI_Q38F",
            "provider": "alibaba",
        })
        callers.append({
            "caller": lambda p: call_dashscope(p, "qwen3.7-flash"),
            "model_desc": "qwen3.7-flash",
            "affinity": ["math_en", "sci_en"],
            "id_prefix": "ALI_Q37F",
            "provider": "alibaba",
        })
        callers.append({
            "caller": lambda p: call_dashscope(p, "qwen3.7-max"),
            "model_desc": "qwen3.7-max",
            "affinity": ["math_en", "math_af", "sci_en", "sci_af"],
            "id_prefix": "ALI_Q37M",
            "provider": "alibaba",
        })
        callers.append({
            "caller": lambda p: call_dashscope(p, "qwen3-vl-plus"),
            "model_desc": "qwen3-vl-plus",
            "affinity": ["sci_en", "sci_af"],
            "id_prefix": "ALI_QVL",
            "provider": "alibaba",
        })
        callers.append({
            "caller": lambda p: call_dashscope(p, "deepseek-v4.1-flash"),
            "model_desc": "deepseek-v4.1-flash",
            "affinity": ["sci_en", "sci_af", "math_en", "math_af"],
            "id_prefix": "ALI_DS41",
            "provider": "alibaba",
        })
        callers.append({
            "caller": lambda p: call_dashscope(p, "deepseek-v4.1-flash-1017"),
            "model_desc": "deepseek-v4.1-flash-1017",
            "affinity": ["sci_en", "sci_af"],
            "id_prefix": "ALI_DSK",
            "provider": "alibaba",
        })
        callers.append({
            "caller": lambda p: call_dashscope(p, "deepseek-v4-pro"),
            "model_desc": "deepseek-v4-pro",
            "affinity": ["math_en", "math_af", "sci_en", "sci_af"],
            "id_prefix": "ALI_DSPRO",
            "provider": "alibaba",
        })
        callers.append({
            "caller": lambda p: call_dashscope(p, "deepseek-v4-pro-0813"),
            "model_desc": "deepseek-v4-pro-0813",
            "affinity": ["sci_en", "sci_af", "math_en", "math_af"],
            "id_prefix": "ALI_DS0813",
            "provider": "alibaba",
        })

        # ── Alibaba Disabled Models (Quota exhausted on current key; preserved for new key) ──
        # callers.append({"caller": lambda p: call_dashscope(p, "qwen3.8-27b"), "model_desc": "qwen3.8-27b", "affinity": ["math_en", "math_af", "sci_en", "sci_af"], "id_prefix": "ALI_Q27B", "provider": "alibaba"})
        # callers.append({"caller": lambda p: call_dashscope(p, "glm-5.3"), "model_desc": "glm-5.3", "affinity": ["math_af", "lang_af"], "id_prefix": "ALI_GLM", "provider": "alibaba"})
        # callers.append({"caller": lambda p: call_dashscope(p, "qwen-max"), "model_desc": "qwen-max", "affinity": ["math_en", "math_af"], "id_prefix": "ALI_MAX", "provider": "alibaba"})

    # ── Vercel AI Gateway (Nemotron 550B, GPT-OSS 120B, Nemotron 3.5 Super VL, Nemotron Lightning, MiMo Flash, Muse Ember, Inkling, MiniMax) ──
    if VERCEL_KEY:
        callers.append({
            "caller": lambda p: call_vercel(p, "nvidia/nemotron-3-ultra-550b-a55b"),
            "model_desc": "nemotron-3-ultra-550b-a55b",
            "affinity": ["math_af", "math_en", "sci_af"],
            "id_prefix": "VRC_NEM",
            "provider": "vercel",
        })
        callers.append({
            "caller": lambda p: call_vercel(p, "openai/gpt-oss-120b"),
            "model_desc": "gpt-oss-120b",
            "affinity": ["math_en", "sci_en", "math_af"],
            "id_prefix": "VRC_OSS",
            "provider": "vercel",
        })
        callers.append({
            "caller": lambda p: call_vercel(p, "nvidia/nemotron-3.5-super-vl"),
            "model_desc": "nemotron-3.5-super-vl",
            "affinity": ["sci_en", "sci_af"],
            "id_prefix": "VRC_NVL",
            "provider": "vercel",
        })
        callers.append({
            "caller": lambda p: call_vercel(p, "nvidia/nemotron-3.5-lightning-free"),
            "model_desc": "nemotron-3.5-lightning-free",
            "affinity": ["math_en", "sci_en"],
            "id_prefix": "VRC_LGT",
            "provider": "vercel",
        })
        callers.append({
            "caller": lambda p: call_vercel(p, "xiaomi/mimo-v2.6-flash"),
            "model_desc": "mimo-v2.6-flash",
            "affinity": ["lang_en", "lang_af"],
            "id_prefix": "VRC_MMO",
            "provider": "vercel",
        })
        callers.append({
            "caller": lambda p: call_vercel(p, "meta/muse-ember"),
            "model_desc": "muse-ember",
            "affinity": ["lang_af", "lang_en"],
            "id_prefix": "VRC_MBR",
            "provider": "vercel",
        })
        callers.append({
            "caller": lambda p: call_vercel(p, "thinkingmachines/inkling-2-small"),
            "model_desc": "inkling-2-small",
            "affinity": ["math_en", "lang_en"],
            "id_prefix": "VRC_INK",
            "provider": "vercel",
        })
        callers.append({
            "caller": lambda p: call_vercel(p, "minimax/minimax-m3.1-flash"),
            "model_desc": "minimax-m3.1-flash",
            "affinity": ["lang_en"],
            "id_prefix": "VRC_MMX",
            "provider": "vercel",
        })

    # ── Token Lab AMD (Gemma 4 31B Afrikaans & Wiskunde, Qwen 27B Maths, DeepSeek V4 Flash Physics) ──
    if TOKENLAB_KEY:
        callers.append({
            "caller": lambda p: call_tokenlab(p, "Gemma-4-31B-IT"),
            "model_desc": "Gemma-4-31B-IT",
            "affinity": ["lang_af", "math_af", "sci_af"],
            "id_prefix": "AMD_GMA",
            "provider": "tokenlab",
        })
        callers.append({
            "caller": lambda p: call_tokenlab(p, "Qwen3.8-27B"),
            "model_desc": "Qwen3.8-27B",
            "affinity": ["math_en", "sci_en"],
            "id_prefix": "AMD_QWN",
            "provider": "tokenlab",
        })
        callers.append({
            "caller": lambda p: call_tokenlab(p, "DeepSeek-V4-Flash"),
            "model_desc": "DeepSeek-V4-Flash",
            "affinity": ["sci_en", "sci_af"],
            "id_prefix": "AMD_DSK",
            "provider": "tokenlab",
        })

    # ── TokenHarbor (DeepSeek V4.1 Flash Fisiese Wetenskappe, MiMo V2.6 Flash English FAL/HL) ──
    if TOKENHARBOR_KEY:
        callers.append({
            "caller": lambda p: call_tokenharbor(p, "deepseek-v4.1-flash:free"),
            "model_desc": "deepseek-v4.1-flash:free",
            "affinity": ["sci_af", "sci_en"],
            "id_prefix": "THB_DSK",
            "provider": "tokenharbor",
        })
        callers.append({
            "caller": lambda p: call_tokenharbor(p, "mimo-v2.6-flash:free"),
            "model_desc": "mimo-v2.6-flash:free",
            "affinity": ["lang_en", "lang_af"],
            "id_prefix": "THB_MMO",
            "provider": "tokenharbor",
        })
        callers.append({
            "caller": lambda p: call_tokenharbor(p, "deepseek-v4-flash:free"),
            "model_desc": "deepseek-v4-flash:free",
            "affinity": ["sci_en"],
            "id_prefix": "THB_DS4",
            "provider": "tokenharbor",
        })

    # ── Kilo Gateway (Nemotron 550B Wiskunde, Nemotron Super VL Physics, Kilo Auto) ──
    if KILO_KEY:
        callers.append({
            "caller": lambda p: call_kilo(p, "nvidia/nemotron-3-ultra-550b-a55b:free"),
            "model_desc": "nemotron-3-ultra-550b-a55b:free",
            "affinity": ["math_af", "math_en"],
            "id_prefix": "KLO_NEM",
            "provider": "kilo",
        })
        callers.append({
            "caller": lambda p: call_kilo(p, "nvidia/nemotron-3.5-super-vl:free"),
            "model_desc": "nemotron-3.5-super-vl:free",
            "affinity": ["sci_en", "sci_af"],
            "id_prefix": "KLO_NVL",
            "provider": "kilo",
        })

    # ── APInex (Qwen 3.8 Max Maths, MiMo Pro Physics, DeepSeek Flash Physics, GLM 5.3 Flash Wiskunde) ──
    if APINEX_KEY:
        callers.append({
            "caller": lambda p: call_apinex(p, "free/qwen-3.8-max"),
            "model_desc": "free/qwen-3.8-max",
            "affinity": ["math_en", "math_af"],
            "id_prefix": "APN_QWN",
            "provider": "apinex",
        })
        callers.append({
            "caller": lambda p: call_apinex(p, "free/mimo-v2.6-pro"),
            "model_desc": "free/mimo-v2.6-pro",
            "affinity": ["sci_en"],
            "id_prefix": "APN_MMO",
            "provider": "apinex",
        })
        callers.append({
            "caller": lambda p: call_apinex(p, "free/deepseek-v4-flash-0731"),
            "model_desc": "free/deepseek-v4-flash-0731",
            "affinity": ["sci_en"],
            "id_prefix": "APN_DSF",
            "provider": "apinex",
        })
        callers.append({
            "caller": lambda p: call_apinex(p, "free/deepseek-v4.1-flash"),
            "model_desc": "free/deepseek-v4.1-flash",
            "affinity": ["sci_af"],
            "id_prefix": "APN_DS4",
            "provider": "apinex",
        })
        callers.append({
            "caller": lambda p: call_apinex(p, "free/glm-5.3-flash"),
            "model_desc": "free/glm-5.3-flash",
            "affinity": ["math_af", "math_en"],
            "id_prefix": "APN_GLM",
            "provider": "apinex",
        })
        callers.append({
            "caller": lambda p: call_apinex(p, "free/minimax-m3.1-flash"),
            "model_desc": "free/minimax-m3.1-flash",
            "affinity": ["lang_en"],
            "id_prefix": "APN_MMX",
            "provider": "apinex",
        })
        callers.append({
            "caller": lambda p: call_apinex(p, "free/muse-spark-1.3"),
            "model_desc": "free/muse-spark-1.3",
            "affinity": ["lang_af"],
            "id_prefix": "APN_MUS",
            "provider": "apinex",
        })

    # ── APMix & Refuseless (DeepSeek Flash Physical Sciences & Fisiese Wetenskappe) ──
    if APMIX_KEY:
        callers.append({
            "caller": lambda p: call_apmix(p, "deepseek-v4.1-flash-1017-free"),
            "model_desc": "deepseek-v4.1-flash-1017-free",
            "affinity": ["sci_en", "sci_af"],
            "id_prefix": "APM_DSK",
            "provider": "apmix",
        })
    if REFUSELESS_KEY:
        callers.append({
            "caller": lambda p: call_refuseless(p, "deepseek-v4.1-flash-abliterated-free"),
            "model_desc": "deepseek-v4.1-flash-abliterated-free",
            "affinity": ["sci_en"],
            "id_prefix": "RFS_DSK",
            "provider": "refuseless",
        })

    # ══════════════════════════════════════════════════════════════════════════
    # PRIORITY 2: WORKHORSE CAPACITY (Google AI Studio, Groq, Cohere, Cerebras)
    # ══════════════════════════════════════════════════════════════════════════

    # ── Key 1 Lanes (Gemma 4 31B Afrikaans, Gemma 4 26B English, Gemini 3.5 STEM, Gemini 3.1 STEM) ──
    if GEMINI_KEY_1:
        # GMA1_31: Gemma 4 31B — Afrikaans Language & STEM papers
        callers.append({
            "caller": lambda p: call_gemma_aistudio(p, GEMINI_KEY_1, "gemma-4-31b-it", gma1_lock, "gma1_31"),
            "model_desc": "gemma-4-31b-it",
            "affinity": ["lang_af", "math_af", "sci_af"],
            "id_prefix": "GMA1_31",
            "provider": "gemini",
        })
        # GMA1_26: Gemma 4 26B — English Language & STEM papers
        callers.append({
            "caller": lambda p: call_gemma_aistudio(p, GEMINI_KEY_1, "gemma-4-26b-a4b-it", gma1_lock, "gma1_26"),
            "model_desc": "gemma-4-26b-a4b-it",
            "affinity": ["lang_en", "math_en", "sci_en"],
            "id_prefix": "GMA1_26",
            "provider": "gemini",
        })
        # GEM1_HYD: Gemini 4 Hydrogen — Mathematics Focus
        callers.append({
            "caller": lambda p: call_gemini(p, GEMINI_KEY_1, "gemini-4-hydrogen", key1_lock, "gem1_hyd"),
            "model_desc": "gemini-4-hydrogen",
            "affinity": ["math_en", "math_af"],
            "id_prefix": "GEM1_HYD",
            "provider": "gemini",
        })
        # GEM1_35: Gemini 3.5 Flash Lite — STEM focus
        callers.append({
            "caller": lambda p: call_gemini_language_safe(p, GEMINI_KEY_1, "gemini-3.5-flash-lite", key1_lock, "gem1_35"),
            "model_desc": "gemini-3.5-flash-lite",
            "affinity": ["sci_en", "sci_af", "math_en", "math_af"],
            "id_prefix": "GEM1_35",
            "provider": "gemini",
        })
        # GEM1_31: Gemini 3.1 Flash Lite — STEM focus
        callers.append({
            "caller": lambda p: call_gemini_language_safe(p, GEMINI_KEY_1, "gemini-3.1-flash-lite", key1_lock, "gem1_31"),
            "model_desc": "gemini-3.1-flash-lite",
            "affinity": ["math_en", "math_af", "sci_en", "sci_af"],
            "id_prefix": "GEM1_31",
            "provider": "gemini",
        })

    # ── Key 2 Lanes (Gemma 4 31B Afrikaans, Gemma 4 26B English, Gemini 4 Hydrogen, Gemini 3.5 STEM, Gemini 3.1 STEM) ──
    if GEMINI_KEY_2:
        # GMA2_31: Gemma 4 31B — Afrikaans Language & STEM papers
        callers.append({
            "caller": lambda p: call_gemma_aistudio(p, GEMINI_KEY_2, "gemma-4-31b-it", gma2_lock, "gma2_31"),
            "model_desc": "gemma-4-31b-it",
            "affinity": ["lang_af", "math_af", "sci_af"],
            "id_prefix": "GMA2_31",
            "provider": "gemini",
        })
        # GMA2_26: Gemma 4 26B — English Language & STEM papers
        callers.append({
            "caller": lambda p: call_gemma_aistudio(p, GEMINI_KEY_2, "gemma-4-26b-a4b-it", gma2_lock, "gma2_26"),
            "model_desc": "gemma-4-26b-a4b-it",
            "affinity": ["lang_en", "math_en", "sci_en"],
            "id_prefix": "GMA2_26",
            "provider": "gemini",
        })
        # GEM2_HYD: Gemini 4 Hydrogen — Mathematics Focus
        callers.append({
            "caller": lambda p: call_gemini(p, GEMINI_KEY_2, "gemini-4-hydrogen", key2_lock, "gem2_hyd"),
            "model_desc": "gemini-4-hydrogen",
            "affinity": ["math_en", "math_af"],
            "id_prefix": "GEM2_HYD",
            "provider": "gemini",
        })
        # GEM2_35: Gemini 3.5 Flash Lite — STEM focus
        callers.append({
            "caller": lambda p: call_gemini_language_safe(p, GEMINI_KEY_2, "gemini-3.5-flash-lite", key2_lock, "gem2_35"),
            "model_desc": "gemini-3.5-flash-lite",
            "affinity": ["math_en", "math_af", "sci_en", "sci_af"],
            "id_prefix": "GEM2_35",
            "provider": "gemini",
        })
        # GEM2_31: Gemini 3.1 Flash Lite — STEM focus
        callers.append({
            "caller": lambda p: call_gemini_language_safe(p, GEMINI_KEY_2, "gemini-3.1-flash-lite", key2_lock, "gem2_31"),
            "model_desc": "gemini-3.1-flash-lite",
            "affinity": ["sci_af", "sci_en", "math_af", "math_en"],
            "id_prefix": "GEM2_31",
            "provider": "gemini",
        })

    # ── OpenRouter Lane (Maths - Free Model) ──
    if OPENROUTER_KEY:
        callers.append({
            "caller": call_openrouter_nemotron_turbo,
            "model_desc": "nemotron-3-ultra-550b",
            "affinity": ["math_en", "math_af"],
            "id_prefix": "NEM",
            "provider": "openrouter",
        })

    # ── Intern-AI DeepSeek Lane (Physical Sciences - Strictly Free Endpoint) ──
    if INTERN_KEY:
        callers.append({
            "caller": call_intern_deepseek,
            "model_desc": "deepseek-v4.1-flash-1017",
            "affinity": ["sci_en", "sci_af"],
            "id_prefix": "DSK",
            "provider": "intern",
        })

    # ── Groq Lanes (High-Speed LPU: 2x Qwen 27B & 2x GPT-OSS 120B) ──
    if GROQ_KEY:
        callers.append({
            "caller": lambda p: call_groq(p, "qwen/qwen3.8-27b"),
            "model_desc": "qwen3.8-27b",
            "affinity": ["math_en", "math_af", "sci_en", "sci_af"],
            "id_prefix": "GRQ_QWN_1",
            "provider": "groq",
        })
        callers.append({
            "caller": lambda p: call_groq(p, "qwen/qwen3.8-27b"),
            "model_desc": "qwen3.8-27b",
            "affinity": ["math_en", "math_af", "sci_en", "sci_af"],
            "id_prefix": "GRQ_QWN_2",
            "provider": "groq",
        })
        callers.append({
            "caller": lambda p: call_groq(p, "openai/gpt-oss-120b"),
            "model_desc": "gpt-oss-120b",
            "affinity": ["sci_en", "sci_af", "math_en", "math_af"],
            "id_prefix": "GRQ_OSS_1",
            "provider": "groq",
        })
        callers.append({
            "caller": lambda p: call_groq(p, "openai/gpt-oss-120b"),
            "model_desc": "gpt-oss-120b",
            "affinity": ["sci_en", "sci_af", "math_en", "math_af"],
            "id_prefix": "GRQ_OSS_2",
            "provider": "groq",
        })

    # ── Cerebras Lanes (Disabled - User Command: ENABLE_CEREBRAS = False) ──
    if ENABLE_CEREBRAS and CEREBRAS_KEY:
        callers.append({
            "caller": lambda p: call_cerebras(p, "qwen-3.8-27b"),
            "model_desc": "qwen-3.8-27b",
            "affinity": ["math_en", "math_af"],
            "id_prefix": "CRB_QWN",
            "provider": "cerebras",
        })

    # ── NVIDIA NIM Lanes (Strictly Paced at < 40 RPM Combined) ──
    if NVIDIA_KEY:
        callers.append({
            "caller": lambda p: call_nvidia(p, "nvidia/nemotron-3.5-lightning-30b-a3b"),
            "model_desc": "nemotron-3.5-lightning",
            "affinity": ["math_en", "math_af"],
            "id_prefix": "NVD_LGT",
            "provider": "nvidia",
        })
        callers.append({
            "caller": lambda p: call_nvidia(p, "mistralai/mistral-large-4-1t-a52b"),
            "model_desc": "mistral-large-4",
            "affinity": ["sci_en", "sci_af"],
            "id_prefix": "NVD_MST",
            "provider": "nvidia",
        })
        callers.append({
            "caller": lambda p: call_nvidia(p, "minimaxai/minimax-m3.1-flash"),
            "model_desc": "minimax-m3.1-flash",
            "affinity": ["sci_en", "sci_af"],
            "id_prefix": "NVD_MMX",
            "provider": "nvidia",
        })
        callers.append({
            "caller": lambda p: call_nvidia(p, "nvidia/nemotron-3.5-super-vl-120b-a12b"),
            "model_desc": "nemotron-3.5-super-vl",
            "affinity": ["sci_en", "math_en"],
            "id_prefix": "NVD_SVL",
            "provider": "nvidia",
        })

    # ── Cohere Lanes (Strictly Paced & Capped to 950 Requests Monthly Free Budget) ──
    if COHERE_KEY:
        # Command A: Mathematics & Sciences (High speed & structured JSON)
        callers.append({
            "caller": lambda p: call_cohere(p, "command-a-03-2025"),
            "model_desc": "command-a",
            "affinity": ["math_en", "sci_en", "math_af"],
            "id_prefix": "COH_CMA",
            "provider": "cohere",
        })
        # Command R+: High parameter flagship reasoning (DBE Math & Physics)
        callers.append({
            "caller": lambda p: call_cohere(p, "command-r-plus-08-2024"),
            "model_desc": "command-r-plus",
            "affinity": ["math_en", "sci_en"],
            "id_prefix": "COH_CRP",
            "provider": "cohere",
        })
        # Command R: Balanced STEM tutoring
        callers.append({
            "caller": lambda p: call_cohere(p, "command-r-08-2024"),
            "model_desc": "command-r",
            "affinity": ["sci_en", "sci_af"],
            "id_prefix": "COH_CMR",
            "provider": "cohere",
        })
        # Command A Reasoning: Deep step-by-step thinking for hard DBE problems
        callers.append({
            "caller": lambda p: call_cohere(p, "command-a-reasoning-08-2025"),
            "model_desc": "command-a-reasoning",
            "affinity": ["math_en", "math_af"],
            "id_prefix": "COH_CAR",
            "provider": "cohere",
        })
        # Command A+: Advanced multimodal & extended synthesis
        callers.append({
            "caller": lambda p: call_cohere(p, "command-a-plus-05-2026"),
            "model_desc": "command-a-plus",
            "affinity": ["sci_en", "math_en"],
            "id_prefix": "COH_CAP",
            "provider": "cohere",
        })
        # North Mini Code: Efficient sparse MoE code & mathematical execution
        callers.append({
            "caller": lambda p: call_cohere(p, "north-mini-code"),
            "model_desc": "north-mini-code",
            "affinity": ["math_en", "sci_en"],
            "id_prefix": "COH_NMC",
            "provider": "cohere",
        })

    # ── OpenAI Lanes (Disabled - User Command: ENABLE_OPENAI = False) ──
    if ENABLE_OPENAI and OPENAI_KEY:
        # Worker 1 & 2: Mathematics (English) - 2x
        callers.append({
            "caller": call_openai_luna,
            "model_desc": "gpt-6-luna",
            "affinity": ["math_en"],
            "id_prefix": "OAI_MTH_1",
            "provider": "openai",
        })
        callers.append({
            "caller": call_openai_luna,
            "model_desc": "gpt-6-luna",
            "affinity": ["math_en"],
            "id_prefix": "OAI_MTH_2",
            "provider": "openai",
        })
        # Worker 3 & 4: Wiskunde (Afrikaans) - 2x
        callers.append({
            "caller": call_openai_luna,
            "model_desc": "gpt-6-luna",
            "affinity": ["math_af"],
            "id_prefix": "OAI_WSK_1",
            "provider": "openai",
        })
        callers.append({
            "caller": call_openai_luna,
            "model_desc": "gpt-6-luna",
            "affinity": ["math_af"],
            "id_prefix": "OAI_WSK_2",
            "provider": "openai",
        })
        # Worker 5 & 6: Physical Sciences (English) - 2x
        callers.append({
            "caller": call_openai_luna,
            "model_desc": "gpt-6-luna",
            "affinity": ["sci_en"],
            "id_prefix": "OAI_SCI_E1",
            "provider": "openai",
        })
        callers.append({
            "caller": call_openai_luna,
            "model_desc": "gpt-6-luna",
            "affinity": ["sci_en"],
            "id_prefix": "OAI_SCI_E2",
            "provider": "openai",
        })
        # Worker 7 & 8: Fisiese Wetenskappe (Afrikaans) - 2x
        callers.append({
            "caller": call_openai_luna,
            "model_desc": "gpt-6-luna",
            "affinity": ["sci_af"],
            "id_prefix": "OAI_SCI_A1",
            "provider": "openai",
        })
        callers.append({
            "caller": call_openai_luna,
            "model_desc": "gpt-6-luna",
            "affinity": ["sci_af"],
            "id_prefix": "OAI_SCI_A2",
            "provider": "openai",
        })


    return callers

def build_fleet_lanes(papers: list, callers: list) -> list:
    lanes = []
    caller_lane_count = defaultdict(int)

    oai_workers = [c for c in callers if c.get("provider") == "openai"]
    other_workers = [c for c in callers if c.get("provider") != "openai"]

    queues = defaultdict(deque)
    for p in sorted(papers, key=lambda x: x[1], reverse=True):
        queues[p[2]].append(p)

    # Strictly STEM cadence for OpenAI (Zero language papers)
    oai_cadence_order = ["math_en", "math_en", "math_af", "math_af", "sci_en", "sci_af"]

    while any(len(q) > 0 for q in queues.values()):
        assigned_in_round = 0

        # Assign other specialized workers (Gemini for languages, Nemotron for maths, DeepSeek for science)
        for c in other_workers:
            assigned_paper = None
            for aff in c["affinity"]:
                if queues[aff]:
                    assigned_paper = queues[aff].popleft()
                    break
            if assigned_paper:
                assigned_in_round += 1
                pid, cnt, cat = assigned_paper
                caller_lane_count[c["id_prefix"]] += 1
                seq = caller_lane_count[c["id_prefix"]]
                lanes.append({
                    "id": f"{c['id_prefix']}-{seq}",
                    "paper_id": pid,
                    "caller": c["caller"],
                    "model_desc": c["model_desc"],
                    "category": cat,
                    "items_count": cnt,
                })

        # Assign OpenAI workers (Strictly STEM queues: math_en, math_af, sci_en, sci_af)
        for c in oai_workers:
            assigned_paper = None
            for aff in c["affinity"]:
                if queues[aff]:
                    assigned_paper = queues[aff].popleft()
                    break
            if not assigned_paper:
                for fallback_aff in oai_cadence_order:
                    if queues[fallback_aff]:
                        assigned_paper = queues[fallback_aff].popleft()
                        break
            if assigned_paper:
                assigned_in_round += 1
                pid, cnt, cat = assigned_paper
                caller_lane_count[c["id_prefix"]] += 1
                seq = caller_lane_count[c["id_prefix"]]
                lanes.append({
                    "id": f"{c['id_prefix']}-{seq}",
                    "paper_id": pid,
                    "caller": c["caller"],
                    "model_desc": c["model_desc"],
                    "category": cat,
                    "items_count": cnt,
                })

        if assigned_in_round == 0:
            # All remaining papers belong to categories with no eligible callers
            break

    return lanes

def save_progress_snapshot():
    with stats_lock:
        snap = {
            "total_verified": global_stats["total_verified"],
            "total_generated": global_stats["total_generated"],
            "total_rejected": global_stats["total_rejected"],
            "papers_done": global_stats["papers_done"],
            "papers_total": global_stats["papers_total"],
            "by_model": dict(global_stats["by_model"]),
            "by_subject": dict(global_stats["by_subject"]),
            "by_strategy": dict(global_stats["by_strategy"]),
            "by_mode": dict(global_stats["by_mode"]),
            "start_time": global_stats["start_time"],
            "last_update": datetime.now().isoformat(),
            "target_verified": TARGET_VERIFIED
        }
    save_progress(snap)

def print_milestone_report(milestone: int):
    with print_lock:
        elapsed = time.time() - (global_stats["start_time"] or time.time())
        hours = elapsed / 3600
        mins = elapsed / 60
        v_tot = global_stats["total_verified"]
        g_tot = global_stats["total_generated"]
        r_tot = global_stats["total_rejected"]
        pass_rate = (v_tot / g_tot * 100) if g_tot > 0 else 0.0
        speed = (v_tot / mins) if mins > 0 else 0.0

        print("\n" + "╔" + "═" * 78 + "╗")
        print(f"║{'⭐ STAGE 2 FLEET MILESTONE: ' + str(milestone) + ' VERIFIED SAMPLES ⭐':^78}║")
        print("╚" + "═" * 78 + "╝")
        print(f"  Duration:         {hours:.2f} hours ({mins:.1f} mins) | Speed: {speed:.1f} samples/min")
        print(f"  Verified Count:   {v_tot:,} / {TARGET_VERIFIED:,} ({(v_tot/TARGET_VERIFIED*100):.1f}%)")
        print(f"  Pass Rate:        {pass_rate:.1f}% ({v_tot:,} passed, {r_tot:,} rejected)")
        print(f"  Papers Completed: {global_stats['papers_done']}/{global_stats['papers_total']}")

        print("\n  --- Production by Model ---")
        for m, cnt in sorted(global_stats["by_model"].items(), key=lambda x: -x[1]):
            m_share = (cnt / v_tot * 100) if v_tot > 0 else 0
            print(f"    {m:<32s}: {cnt:>5d} ({m_share:.1f}%)")

        print("\n  --- Production by Subject ---")
        for s, cnt in sorted(global_stats["by_subject"].items(), key=lambda x: -x[1]):
            print(f"    {s:<32s}: {cnt:>5d}")

        print("\n  --- Production by Mode ---")
        for mode, cnt in sorted(global_stats["by_mode"].items(), key=lambda x: -x[1]):
            print(f"    {mode:<20s}: {cnt:>5d}")
        print("=" * 80 + "\n")

    save_progress_snapshot()

def print_final_report():
    elapsed = time.time() - (global_stats["start_time"] or time.time())
    hours = elapsed / 3600

    print("\n" + "=" * 80)
    print("EISHKOM AI — STAGE 2 FLEET GENERATION SUMMARY")
    print("=" * 80)
    print(f"Duration:         {hours:.2f} hours ({elapsed:.1f}s)")
    print(f"Papers completed: {global_stats['papers_done']}/{global_stats['papers_total']}")
    print(f"Total generated:  {global_stats['total_generated']}")
    print(f"Total verified:   {global_stats['total_verified']}")
    print(f"Total rejected:   {global_stats['total_rejected']} (saved to workspace/rejected/stage2/)")
    if global_stats['total_generated'] > 0:
        rate = global_stats['total_verified'] / global_stats['total_generated'] * 100
        print(f"Pass rate:        {rate:.1f}%")
    print(f"Estimated SFT samples: ~{int(global_stats['total_verified'] * 2.5)}")

    print("\n--- By Mode ---")
    for mode, count in sorted(global_stats["by_mode"].items(), key=lambda x: -x[1]):
        print(f"  {mode:<20s} {count:>5d}")

    print("\n--- By Strategy ---")
    for strat, count in sorted(global_stats["by_strategy"].items(), key=lambda x: -x[1]):
        print(f"  {strat:<35s} {count:>5d}")

    print("\n--- By Model ---")
    for model, count in sorted(global_stats["by_model"].items(), key=lambda x: -x[1]):
        print(f"  {model:<35s} {count:>5d}")

    print("\n--- By Subject ---")
    for subj, count in sorted(global_stats["by_subject"].items(), key=lambda x: -x[1]):
        print(f"  {subj:<35s} {count:>5d}")
    print("=" * 80)

# ══════════════════════════════════════════════════════════════════════════════
#  TEST / DRY-RUN RUNNER
# ══════════════════════════════════════════════════════════════════════════════

def run_single_test_item(caller, model_desc):
    print("=" * 80)
    print("RUNNING END-TO-END PIPELINE VERIFICATION TEST (1 ITEM)")
    print(f"Model: {model_desc}")
    print("=" * 80)

    test_item = {
        "item_id": "test-verification-item-01",
        "subject": "mathematics",
        "grade": 12,
        "topic": "Quadratic Equations",
        "question": "Solve for x: x^2 - 5x + 6 = 0",
        "memo": "x = 2 or x = 3",
        "final_answer": "x = 2 or x = 3",
        "marks": 3
    }

    strategy = pick_strategy("mathematics")
    persona = pick_student_persona("mathematics", marks=3)
    few_shot = get_few_shot_for_subject("mathematics", mode="normal")

    ctrl = {
        "subject": "mathematics",
        "grade": 12,
        "subject_language": "en",
        "response_language": "mirror",
        "strategy": strategy["name"],
        "answer_policy": "guided",
        "student_level": persona["student_level"],
        "tone": "encouraging",
        "response_length": "medium",
        "tools": ["calculator", "board"],
        "math_format": "latex"
    }

    final_turn_instr = (
        "   In the FINAL assistant message, you MUST include:\n"
        "   a) The consolidated final answer matching the memo.\n"
        "   b) '### 📖 Formula Breakdown (How It Works):'\n"
        "      * The Formula: [state the exact formula in KaTeX clearly]\n"
        "      * What the letters mean:\n"
        "        * [letter 1]: [meaning in plain everyday language]\n"
        "        * [letter 2]: [meaning in plain everyday language]\n"
        "      * Why we use it: [explain in simple, accessible, friendly terms why it works and why we chose it]\n"
        "   c) '🎯 Exam Tip:' [mark allocation tip or common exam pitfall to avoid]"
    )

    prompt = TEMPLATE_V2.format(
        few_shot=few_shot,
        strategy_instructions=strategy["prompt_fragment"],
        subject=test_item["subject"],
        grade=test_item["grade"],
        topic=test_item["topic"],
        passage="",
        question=test_item["question"],
        memo=test_item["memo"],
        final=test_item["final_answer"],
        lang="en",
        state=persona["state"],
        state_desc=persona["desc"],
        learner_script=" -> ".join(persona["script"]),
        turns=persona["turns"],
        coaching_mode="Deep-Dive Socratic Mode (3-4 turns)",
        control=json.dumps(ctrl, indent=2),
        strategy_name=strategy["name"],
        techniques_json=json.dumps(persona["techniques"]),
        tool_instruction="In your private reasoning, demonstrate the calculation as: [TOOL CHECK: calculator(expression=\"...\") -> result]. Never use placeholders like 1+1 or 0+0.",
        verify_code_instruction="In meta.verify_code, write a short Python snippet using sympy that prints the final answer.",
        final_turn_instruction=final_turn_instr,
    )

    print("\n1. Calling model...")
    t0 = time.time()
    resp_text = caller(prompt)
    dt = time.time() - t0
    print(f"Response received in {dt:.2f}s ({len(resp_text)} chars)")

    print("\n2. Parsing JSON...")
    obj = extract_json_safely(resp_text)
    print("JSON successfully parsed! Keys:", list(obj.keys()))
    messages = obj.get("messages", [])
    print(f"Number of dialogue turns: {len(messages)}")

    print("\n3. Testing Quality Rubric...")
    passed, issues, score = check_rubric(
        obj,
        expected_strategy=strategy["name"],
        expected_lang="en",
        is_language_subject=False,
        min_turns=persona["turns"]
    )
    print(format_rubric_report(passed, issues, score))

    print("\n4. Testing SymPy Verification...")
    meta = obj.get("meta", {})
    code = meta.get("verify_code", "")
    print(f"Verify code:\n{code}")
    if code:
        out, err = verify_sympy(code)
        print(f"SymPy execution output: '{out}' (error: {err})")
        match = check_answers(out, test_item["final_answer"])
        print(f"Answer match vs memo: {match}")

    print("\n" + "=" * 80)
    print("PIPELINE TEST PASSED SUCCESSFULLY!")
    print("=" * 80)

# ══════════════════════════════════════════════════════════════════════════════
#  MAIN ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Eishkom AI Stage 2 Multi-Model Fleet Generator")
    parser.add_argument("--dry-run", action="store_true", help="Audit papers and fleet lanes without calling APIs")
    parser.add_argument("--test-item", action="store_true", help="Run a single-item test to verify end-to-end functionality")
    parser.add_argument("--status", action="store_true", help="Display real-time Stage 2 generation dashboard")
    parser.add_argument("--target", type=int, default=TARGET_VERIFIED, help="Target verified count")
    parser.add_argument("--max-papers", type=int, default=MAX_PAPERS, help="Max papers to process")
    parser.add_argument("--pass", dest="pass_num", type=int, default=1, choices=[1, 2], help="Generation pass (1 = baseline multi-strategy, 2 = alternate strategy permutation)")
    args = parser.parse_args()

    init_pass_config(args.pass_num)

    if args.status:
        try:
            sys.path.insert(0, str(ROOT_DIR))
            from tools.stage2_status import print_status_dashboard
            print_status_dashboard()
        except Exception as e:
            print(f"Error reading status: {e}")
        return

    print("=" * 80)
    print(f"EISHKOM AI — STAGE 2 MULTI-MODEL FLEET GENERATOR (PASS {args.pass_num}: {'ALTERNATE STRATEGY PERMUTATION' if args.pass_num == 2 else 'BASELINE'})")
    print(f"Target: {args.target} verified Socratic lessons (~{args.target * 2.5:.0f} SFT samples)")
    print(f"Destination: {S2_VER_DIR}")
    print(f"Rejected items destination: {S2_REJ_DIR}")
    print("=" * 80)

    # Step 1: Discover available untouched papers
    stage1_papers = load_stage1_used_papers()
    print(f"\nStage 1 papers strictly excluded: {len(stage1_papers)}")

    progress = load_progress()
    s2_completed = set(progress.get("completed_papers", []))

    untouched = discover_untouched_papers(stage1_papers)
    available_untouched = [(pid, cnt, cat) for pid, cnt, cat in untouched if pid not in s2_completed]
    total_available_items = sum(cnt for _, cnt, _ in available_untouched)

    print(f"Untouched exam papers ready: {len(available_untouched)} ({total_available_items} total atomic items)")

    # Step 2: Setup fleet callers
    callers = assign_callers()
    if not callers:
        print("ERROR: No API keys found! Please check your .env file.")
        return
    print(f"Active fleet models ({len(callers)} workers): {', '.join(c['id_prefix'] + ':' + c['model_desc'] for c in callers)}")

    # Test item mode
    if args.test_item:
        test_caller = callers[0]["caller"]
        test_desc = callers[0]["model_desc"]
        run_single_test_item(test_caller, test_desc)
        return

    # Select papers
    selected = available_untouched[:args.max_papers]
    total_items = sum(cnt for _, cnt, _ in selected)
    global_stats["papers_total"] = len(selected)

    print(f"\nSelected {len(selected)} papers with {total_items} items for this fleet run")
    by_cat = defaultdict(int)
    for _, cnt, cat in selected:
        by_cat[cat] += cnt
    for cat, cnt in sorted(by_cat.items()):
        print(f"  {cat:<12s}: {cnt:>5d} items")

    lanes = build_fleet_lanes(selected, callers)

    if args.dry_run:
        print("\n" + "=" * 80)
        print("DRY RUN SUMMARY (No API calls made)")
        print("=" * 80)
        print(f"Fleet lanes constructed: {len(lanes)}")
        for l in lanes[:14]:
            print(f"  Lane [{l['id']:<16s}]: {l['paper_id']} -> {l['model_desc']}")
        if len(lanes) > 14:
            print(f"  ... and {len(lanes) - 14} more lanes")
        print("\nAll sanity checks passed successfully!")
        return

    # Step 3: Run fleet in parallel
    global_stats["start_time"] = time.time()
    print(f"\nLaunching {len(lanes)} parallel lanes (max concurrent: 40)...")
    print("-" * 80)

    max_workers = min(len(lanes), 40)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_paper_stage2, lane): lane for lane in lanes}
        for fut in as_completed(futures):
            lane = futures[fut]
            try:
                n_gen, n_ver, tot = fut.result()
                with print_lock:
                    print(f">> Paper {lane['paper_id']} Finished: {n_ver}/{n_gen} verified out of {tot} items")

                progress = load_progress()
                progress.setdefault("completed_papers", []).append(lane["paper_id"])
                progress["last_update"] = datetime.now().isoformat()
                save_progress(progress)

            except Exception as e:
                with print_lock:
                    print(f">> Paper {lane['paper_id']} Error: {e}")

    # Step 4: Final report
    print_final_report()

    # Step 5: Self-contained Stage 2 Compilation
    print("\n" + "=" * 80)
    print("TRIGGERING STAGE 2 COMPILATION (Stage 1 + Stage 2 combined)...")
    print("=" * 80)
    compile_corpus()

if __name__ == "__main__":
    main()
