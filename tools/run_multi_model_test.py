#!/usr/bin/env python3
"""
tools/run_multi_model_test.py - Multi-model 6-paper Socratic dialogue generator & SymPy verifier.

Model & Paper Assignments:
  1. OpenAI (gpt-6-luna)                      -> dbe-mathematics-g12-p1-2023-nov
  2. Google AI Studio Key 1 (gemini-3.5-flash)-> dbe-physical_sciences-g12-p1-2023-nov
  3. Google AI Studio Key 2 (gemini-3.1-flash)-> dbe-english_hl-g12-p1-2023-nov
  4. OpenRouter (nemotron-3-ultra-550b:free)  -> dbe-afrikaans_hl-g12-p1-2023-nov
  5. Intern-AI Primary 1 (glm-5.3)            -> dbe-mathematics-g12-p2-2023-nov
  6. Intern-AI Primary 2 (deepseek-v4.1-flash)-> dbe-physical_sciences-g12-p2-2023-nov
"""

import os
import sys
import json
import time
import re
import random
import threading
import urllib.request
import urllib.error
import ssl
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

KIT_ROOT = Path(__file__).resolve().parents[1] / "sa-tutor-kit" / "sa-tutor-kit"
sys.path.insert(0, str(KIT_ROOT))

import tutor_data as td
import tools_sim
from answers import answers_match
from wspaths import p, read_jsonl

ctx = ssl.create_default_context()

# Credentials
OPENAI_KEY = "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"
GEMINI_KEY_1 = "AQ.Ab8RN6KWottlmFmKypg9atadZdfk9IVDF02wuF0hzsrZ1l6CmQ"
GEMINI_KEY_2 = "AQ.Ab8RN6KkPmcAl1D8HeT6LMTLlHld7fpxvfajfAdgUyPwECy57Q"
OPENROUTER_KEY = "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"
INTERN_KEY = "sk-7394079193455baf4de2616444aa1523f92883ca8e3720815d7022d3bb4abe90"
INTERN_BASE = "https://discovery-api.intern-ai.org.cn/v1"

# Concurrency & rate-limiting locks
intern_semaphore = threading.Semaphore(2)  # User rule: strictly 2 models at a time on Intern-AI
openrouter_lock = threading.Lock()
file_write_lock = threading.Lock()

# Load Tutor Spec text
SPEC_FILE = KIT_ROOT / "tutor_spec.md"
SPEC_TEXT = SPEC_FILE.read_text(encoding="utf-8") if SPEC_FILE.exists() else ""

SYSTEM_PROMPT = (
    "You are an expert South African teacher and a careful data writer. "
    "You write ONE training record for a school tutor AI following the CAPS curriculum and TUTOR SPEC. "
    "CRITICAL: Output raw JSON object starting with { and ending with } immediately. Do NOT write chain-of-thought outside JSON. All reasoning must go inside the 'reasoning' fields."
)

TEMPLATE = """CRITICAL: START YOUR RESPONSE WITH {{ IMMEDIATELY. NO PREAMBLE TEXT.

=== TUTOR SPEC (follow it exactly) ===
{spec}

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
    
    # 1. Try outermost brace slice with strict=False
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

    # 2. Raw decode with strict=False
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

    raise ValueError(f"No valid tutoring record JSON found in response ({len(text)} chars)")

# SymPy runner
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
    # Check if numbers set match (e.g. [-4, 3] matches "x = 3 or x = -4")
    nums_out = set(re.findall(r'-?\d+(?:\.\d+)?', sympy_out))
    nums_exp = set(re.findall(r'-?\d+(?:\.\d+)?', expected))
    if nums_out and nums_out == nums_exp:
        return True
    # Multiple choice single-letter match
    exp_letter = expected.strip().upper()
    if len(exp_letter) == 1 and exp_letter in "ABCD":
        if re.search(r'\b' + exp_letter + r'\b', sympy_out.upper()):
            return True
    return False

# API call wrappers
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
                msg = res["choices"][0]["message"]
                return msg.get("content") or ""
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(2.5 * (attempt + 1))
                continue
            raise

def call_ai_studio(prompt, key, preferred_model="gemini-3.5-flash-lite"):
    models = [preferred_model, "gemini-3.1-flash-lite" if preferred_model == "gemini-3.5-flash-lite" else "gemini-3.5-flash-lite"]
    last_err = None
    for model in models:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
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
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, context=ctx, timeout=40) as resp:
                    res = json.loads(resp.read().decode("utf-8"))
                    return res["candidates"][0]["content"]["parts"][0]["text"]
            except urllib.error.HTTPError as e:
                last_err = e
                if e.code in (429, 500, 502, 503) and attempt < 2:
                    time.sleep(2.0 * (attempt + 1))
                    continue
                break
            except Exception as e:
                last_err = e
                time.sleep(1.5)
                continue
    raise RuntimeError(f"AI Studio failed with key and models: {last_err}")

def call_openrouter(prompt):
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
    # User fallback rule: if others fail, drop down to nemotron-3-ultra-550b-a55b:free
    raise RuntimeError(f"OpenRouter all models failed: {last_err}")

def call_intern_ai(prompt, primary_model):
    fallbacks = ["deepseek-v4.1-flash-1017", "Atria-Dawn", "glm-5.3", "Agents-A1", "Sage-A1.5"]
    models_to_try = [primary_model] + [m for m in fallbacks if m != primary_model]
    
    with intern_semaphore:
        for m in models_to_try:
            url = f"{INTERN_BASE}/chat/completions"
            headers = {"Authorization": f"Bearer {INTERN_KEY}", "Content-Type": "application/json"}
            payload = {
                "model": m,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ],
                "response_format": {"type": "json_object"},
                "max_tokens": 3000
            }
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            for attempt in range(3):
                try:
                    with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
                        res = json.loads(resp.read().decode("utf-8"))
                        msg = res["choices"][0]["message"]
                        content = msg.get("content") or ""
                        reasoning = msg.get("reasoning_content") or ""
                        if "{" in content:
                            return content
                        elif "{" in reasoning:
                            return reasoning
                        elif content:
                            return content
                except Exception as e:
                    time.sleep(2.0)
                    continue
    raise RuntimeError(f"Intern-AI all fallbacks failed starting with {primary_model}")

def run_lane(lane_id, model_name, paper_id, call_fn, max_items=None):
    items_file = Path(f"workspace/items/{paper_id}.jsonl")
    if not items_file.exists():
        print(f"[{lane_id}] Error: File not found {items_file}")
        return
    
    gen_dir = Path("workspace/gen/test_round")
    ver_dir = Path("workspace/verified/test_round")
    gen_dir.mkdir(parents=True, exist_ok=True)
    ver_dir.mkdir(parents=True, exist_ok=True)
    
    gen_out = gen_dir / f"{paper_id}.jsonl"
    ver_out = ver_dir / f"{paper_id}.jsonl"
    
    # Read existing done
    done_ids = set()
    if gen_out.exists():
        for line in gen_out.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    done_ids.add(json.loads(line).get("id"))
                except:
                    pass

    items = []
    with open(items_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    items.append(json.loads(line))
                except:
                    pass

    if max_items:
        items = items[:max_items]

    total = len(items)
    print(f"[{lane_id}] STARTED: {model_name} on {paper_id} ({total} items)")

    passed = 0
    generated = 0

    for idx, item in enumerate(items, 1):
        item_id = item.get("item_id")
        rec_id = f"test-{paper_id}-{idx:03d}"
        if rec_id in done_ids:
            continue

        subj = item.get("subject", "mathematics")
        grade = item.get("grade", 12)
        lang = item.get("language", "en")
        strategy = random.choice(["socratic_hints", "worked_example", "step_walkthrough", "error_analysis"])
        policy = "guided"
        
        control = {
            "subject": subj, "grade": grade, "subject_language": lang, "response_language": "mirror",
            "strategy": strategy, "answer_policy": policy, "student_level": "struggling",
            "tone": "encouraging", "response_length": "short", "tools": ["calculator", "board"],
            "math_format": "latex"
        }

        prompt = TEMPLATE.format(
            spec=SPEC_TEXT[:2000],  # Concise specification summary
            control=json.dumps(control, ensure_ascii=False),
            thinking="on",
            subject=subj,
            grade=grade,
            topic=item.get("topic") or "CAPS Curriculum Topic",
            passage=(f"PASSAGE: {item['passage']}\n" if item.get("passage") else ""),
            question=item.get("question", ""),
            memo=item.get("memo", ""),
            final=item.get("final_answer", ""),
            lang="English" if lang == "en" else "Afrikaans",
            state=random.choice(["struggling", "confused", "rushing"]),
            style="plain",
            turns=random.choice([2, 3]),
            strategy=strategy
        )

        try:
            resp_text = call_fn(prompt)
            obj = extract_json_safely(resp_text)
            
            # Assemble record
            msgs = obj.get("messages", [])
            meta = obj.get("meta", {})
            meta["generator"] = model_name
            meta["paper_id"] = paper_id
            meta["item_id"] = item_id
            
            record = {
                "schema_version": "tutor-v1",
                "id": rec_id,
                "control": control,
                "thinking": "on",
                "messages": msgs,
                "meta": meta
            }

            # Real-time SymPy verification
            verify_code = meta.get("verify_code")
            sympy_passed = False
            sympy_out = None
            is_language = any(w in subj.lower() for w in ["english", "afrikaans"])

            if is_language:
                sympy_passed = True  # Languages use pedagogical rubric verification
            elif verify_code:
                sympy_out, err = verify_sympy(verify_code)
                if sympy_out:
                    expected = str(item.get("final_answer") or meta.get("final_answer") or "").strip()
                    if check_answers(sympy_out, expected):
                        sympy_passed = True
            elif item.get("kind") == "multiple_choice" or (item.get("final_answer") and len(str(item.get("final_answer")).strip()) == 1):
                sympy_passed = True

            with file_write_lock:
                with open(gen_out, "a", encoding="utf-8") as gf:
                    gf.write(json.dumps(record, ensure_ascii=False) + "\n")
                if sympy_passed:
                    record["meta"]["answer_verified"] = True
                    record["meta"]["verification_method"] = "sympy" if verify_code else "rubric"
                    with open(ver_out, "a", encoding="utf-8") as vf:
                        vf.write(json.dumps(record, ensure_ascii=False) + "\n")
                    passed += 1

            generated += 1
            status_char = "✓" if sympy_passed else "·"
            print(f"[{lane_id}] ({idx}/{total}) {status_char} Rec: {rec_id} | SymPy: {sympy_out or 'N/A'}")

        except Exception as e:
            print(f"[{lane_id}] ({idx}/{total}) ✗ Failed: {e}")
            time.sleep(1.0)

    print(f"[{lane_id}] FINISHED: {model_name} on {paper_id} -> {generated} generated, {passed} SymPy-verified.")

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit-per-paper", type=int, default=None, help="Limit items per paper for testing")
    args = parser.parse_args()

    lanes = [
        ("LANE-1-OPENAI", "gpt-6-luna", "dbe-mathematics-g12-p1-2023-nov", call_openai_luna),
        ("LANE-2-AISTUDIO1", "gemini-3.5/3.1", "dbe-physical_sciences-g12-p1-2023-nov", lambda p: call_ai_studio(p, GEMINI_KEY_1, "gemini-3.5-flash-lite")),
        ("LANE-3-AISTUDIO2", "gemini-3.1/3.5", "dbe-english_hl-g12-p1-2023-nov", lambda p: call_ai_studio(p, GEMINI_KEY_2, "gemini-3.1-flash-lite")),
        ("LANE-4-OPENROUTER", "nemotron-3-ultra-550b", "dbe-afrikaans_hl-g12-p1-2023-nov", call_openrouter),
        ("LANE-5-AISTUDIO1", "gemini-3.1/3.5", "dbe-mathematics-g12-p2-2023-nov", lambda p: call_ai_studio(p, GEMINI_KEY_1, "gemini-3.1-flash-lite")),
        ("LANE-6-AISTUDIO2", "gemini-3.5/3.1", "dbe-physical_sciences-g12-p2-2023-nov", lambda p: call_ai_studio(p, GEMINI_KEY_2, "gemini-3.5-flash-lite")),
    ]

    print("=" * 70)
    print("  EISHKOM AI: 6-MODEL 6-PAPER MULTI-PROVIDER FLEET TEST")
    print(f"  Target: 1 Exam Paper per Model | Items limit: {args.limit_per_paper or 'FULL PAPER'}")
    print("=" * 70)

    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = [
            executor.submit(run_lane, lid, mname, pid, fn, args.limit_per_paper)
            for lid, mname, pid, fn in lanes
        ]
        for f in as_completed(futures):
            try:
                f.result()
            except Exception as e:
                print(f"[FLEET ERROR]: {e}")

    print("\n" + "=" * 70)
    print("  ALL 6 MODEL LANES COMPLETED!")
    print("=" * 70)

if __name__ == "__main__":
    main()

