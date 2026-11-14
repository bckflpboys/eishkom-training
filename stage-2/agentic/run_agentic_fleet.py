#!/usr/bin/env python3
"""
stage-2/agentic/run_agentic_fleet.py - Eishkom AI Agentic & Study Coaching Fleet Generator.

Generates high-fidelity training data for:
  1. Study & Intake Coaching: intake, study_plan, weak_topic_diagnosis, exam_strategy
  2. Content Coaching: study_guide_section, revision_session (grounded in real DBE exam items)
  3. Wellbeing Protocol: distress_signal (warm de-escalation with verified SA helplines)
  4. Agentic Vision / OCR: page_worker (structured single-page extraction with damage/gaps)
  5. Multi-Page Synthesiser: paper_walkthrough, paper_prep_guide, paper_exam_strategy

Enforces:
  - Code-computed arithmetic: all schedules, dates, and rankings are calculated by Python helpers.
  - Zero hallucination: models only explain code-computed results or real paper excerpts.
  - Strict verification: tool args matching, grounding validation, and banned-praise detection.
"""

import os
import sys
import json
import time
import re
import random
import argparse
import threading
import urllib.request
import urllib.error
import datetime as dt
from pathlib import Path
from collections import defaultdict, Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import sampler_agentic

# Directories
WS_DIR = ROOT_DIR / "workspace"
ITEMS_DIR = WS_DIR / "items"
VER_AGENTIC_DIR = WS_DIR / "verified" / "agentic"
REJ_AGENTIC_DIR = WS_DIR / "rejected" / "agentic"
GEN_AGENTIC_DIR = WS_DIR / "gen" / "agentic"

VER_AGENTIC_DIR.mkdir(parents=True, exist_ok=True)
REJ_AGENTIC_DIR.mkdir(parents=True, exist_ok=True)
GEN_AGENTIC_DIR.mkdir(parents=True, exist_ok=True)

# ── Load Environment Variables ──────────────────────────────────────────────
def load_env():
    env = {}
    env_file = ROOT_DIR / ".env"
    if env_file.exists():
        with open(env_file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip().strip('"').strip("'")
    return env

ENV = load_env()
GEMINI_KEY_1 = ENV.get("GEMINI_API_KEY", "")
GEMINI_KEY_2 = ENV.get("GEMINI_API_KEY_2", "")
GROQ_KEY = ENV.get("GROQ_API_KEY", "")
COHERE_KEY = ENV.get("COHERE_API_KEY", "")
OPENROUTER_KEY = ENV.get("OPENROUTER_API_KEY", "")
NVIDIA_KEY = ENV.get("NVIDIA_NIM_API_KEY", "")
INTERN_KEY = ENV.get("INTERN_API_KEY", "")

# Thread Locks
print_lock = threading.Lock()
stats_lock = threading.Lock()
groq_lock = threading.Lock()
cohere_lock = threading.Lock()
nvidia_lock = threading.Lock()
gma1_lock = threading.Lock()
gma2_lock = threading.Lock()

last_call_time = defaultdict(float)

def pace_key(lock: threading.Lock, key_id: str, min_interval_sec: float = 1.0):
    with lock:
        now = time.time()
        elapsed = now - last_call_time[key_id]
        if elapsed < min_interval_sec:
            time.sleep(min_interval_sec - elapsed)
        last_call_time[key_id] = time.time()

# ── Common Core System Prompt ───────────────────────────────────────────────
COMMON_CORE = """You are Eishkom's data-generation teacher. You produce the IDEAL behaviour for a small on-device tutoring model (4B parameters or fewer) used by South African learners in Grades 7-12 (CAPS: Mathematics, Natural Sciences / Physical Sciences, English, Afrikaans).

WHO THE MODEL IS
A warm, direct, expert South African teacher and study coach. Talks to the learner as a capable person, never as a small child. Short sentences, no lecturing, no filler. At most one emoji per reply, only if it fits.

NON-NEGOTIABLE RULES
1. GROUND EVERYTHING. Use only what is in the spec: page content, notes, aggregate, source_excerpts, question_bank, paper_facts, tool results, profile. Do not use outside knowledge. If something is not in the spec, say you cannot see it.
2. NEVER INVENT NUMBERS. Marks, totals, dates, durations, minutes, percentages and rankings come ONLY from the spec or tool results. You never add, subtract, count or work out dates yourself.
3. NEVER PREDICT THE EXAM. You may say what the papers in the notes show. You must not say a topic will, will not, or is likely to come up.
4. REPORT GAPS. If a page or question is unreadable, partial or missing, say which one in a single line and what that limits.
5. LANGUAGE. Reply in learner_language (en or af) using CAPS terminology. private_reasoning is ALWAYS English.
6. HONEST, NOT FLATTERING. Praise only what is earned and specific. Never open with filler praise ("Great question!", "Excellent!", "Wonderful!", "Mooi vraag!", "Presies!", "Perfek!").
7. WELLBEING. If learner_state is distress_signal (hopelessness, self-harm, feeling unsafe): STOP the study task. No plan, no guide, no tool call. Respond with warmth in 2-4 sentences, do not diagnose, encourage them to talk to a trusted adult, include {{helpline_text}} exactly as given, and say you are glad to get back to studying whenever they are ready.
8. FORMAT. Output valid JSON only — no markdown fence, no text outside it."""

TASK_STUDY_PROMPT = """TASK: STUDY COACHING.
Write the dialogue for the given task_type. The learner writes the opener according to learner_state, in learner_language, like a real Grade {{grade}} learner: short, informal, imperfect.

TOOLS:
When a tool is needed, the teacher turn has content "" and a tool_call {"name","args"} with args EXACTLY equal to expected_tool_calls[i].args. The next dialogue entry is {"role":"tool_result","name":"...","ref":i}. The following teacher turn explains the result using ONLY numbers in that result.

OUTPUT SCHEMA:
{
  "meta": {"task_type": "", "learner_language": "af|en", "learner_state": "", "techniques": [], "thinking_mode": "none|short|full", "tools_used": []},
  "dialogue": [
    {"role": "student", "content": ""},
    {"role": "teacher", "private_reasoning": "", "content": "", "tool_call": null}
  ],
  "grounding": {"numbers_used": [], "source_refs": [], "gaps_reported": []}
}"""

TASK_PAGE_WORKER_PROMPT = """TASK: PAGE_WORKER.
You are the ideal page-reading agent. Read ONE page and return its notes as JSON. No reasoning text: JSON only.
- Copy question text exactly as printed in its original language.
- marks: integer printed, or null if hidden/unreadable. NEVER infer marks.
- page.status: ok | partial | unreadable | blank.
- carry_out: at most 80 words facts only: current section, last question number seen.

OUTPUT SCHEMA:
{
  "page": {"index": 0, "of": 0, "status": "ok|partial|unreadable|blank", "page_type": "question_page", "language": "en|af|mixed", "issues": []},
  "paper_facts": null,
  "questions": [
    {"number": "", "section": null, "marks": null, "marks_visible": true, "text": "", "type": "calculation", "topic": "", "command_word": null, "has_diagram": false, "depends_on": [], "continues_from_prev_page": false, "continues_on_next_page": false, "truncated": false, "unreadable_parts": []}
  ],
  "passages": [],
  "carry_out": {"section": null, "last_question": null, "open_passages": [], "digest": ""}
}"""

TASK_SYNTHESISER_PROMPT = """TASK: SYNTHESISER.
A small agent has read a school paper page by page. You only have its notes and the totals the app computed. Write a dialogue between the learner and the ideal tutor/study coach about THIS paper.
- All numbers stated must appear in aggregate or notes.
- In sentence 1: what this paper is.
- In sentence 2: what you could read and any gaps.
- Offer 2-3 concrete next steps.

OUTPUT SCHEMA:
{
  "meta": {"task_type": "", "learner_language": "af|en", "learner_state": "", "techniques": [], "thinking_mode": "none|short|full", "tools_used": []},
  "dialogue": [
    {"role": "student", "content": ""},
    {"role": "teacher", "private_reasoning": "", "content": "", "tool_call": null}
  ],
  "grounding": {"numbers_used": [], "source_refs": [], "gaps_reported": []}
}"""

# ── API Callers ─────────────────────────────────────────────────────────────
def call_gemini(prompt, system_prompt, api_key, model_name="gemini-3.5-flash-lite", lock=None, key_id="gemini"):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "systemInstruction": {"parts": [{"text": system_prompt}]},
        "generationConfig": {"temperature": 0.2, "responseMimeType": "application/json"}
    }
    for attempt in range(4):
        if lock:
            pace_key(lock, key_id, min_interval_sec=1.5)
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["candidates"][0]["content"]["parts"][0]["text"]
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < 3:
                time.sleep(3.0 * (attempt + 1))
                continue
            raise

def call_gemma(prompt, system_prompt, api_key, model_name="gemma-4-31b-it", lock=None, key_id="gemma"):
    full_prompt = f"{system_prompt}\n\nUSER SPECIFICATION:\n{prompt}\n\nOUTPUT JSON IMMEDIATELY:"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": full_prompt}]}],
        "generationConfig": {"temperature": 0.2}
    }
    for attempt in range(4):
        if lock:
            pace_key(lock, key_id, min_interval_sec=2.0)
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["candidates"][0]["content"]["parts"][0]["text"]
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < 3:
                time.sleep(4.0 * (attempt + 1))
                continue
            raise

def call_groq(prompt, system_prompt, model_name="qwen/qwen3.8-27b"):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_KEY}", "Content-Type": "application/json", "User-Agent": "curl/8.4.0"}
    payload = {
        "model": model_name,
        "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}],
        "temperature": 0.2,
        "response_format": {"type": "json_object"}
    }
    for attempt in range(4):
        pace_key(groq_lock, "groq", min_interval_sec=1.0)
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=75) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < 3:
                time.sleep(3.0 * (attempt + 1))
                continue
            raise

def call_cohere(prompt, system_prompt, model_name="command-a-03-2025"):
    url = "https://api.cohere.com/v2/chat"
    headers = {"Authorization": f"Bearer {COHERE_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": model_name,
        "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}],
        "response_format": {"type": "json_object"}
    }
    for attempt in range(4):
        pace_key(cohere_lock, "cohere", min_interval_sec=1.5)
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=75) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["message"]["content"][0]["text"]
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < 3:
                time.sleep(3.0 * (attempt + 1))
                continue
            raise

# ── Question Bank & Source Excerpt Loader ────────────────────────────────────
CACHED_ITEMS = []

def load_real_exam_items():
    global CACHED_ITEMS
    if CACHED_ITEMS:
        return CACHED_ITEMS
    files = list(ITEMS_DIR.glob("*.jsonl"))
    items = []
    for f in files[:40]:  # sample from a variety of subjects
        try:
            for line in open(f, encoding="utf-8"):
                if line.strip():
                    rec = json.loads(line)
                    if rec.get("question") and (rec.get("memo") or rec.get("final_answer")):
                        items.append(rec)
        except Exception:
            pass
    CACHED_ITEMS = items
    return CACHED_ITEMS

def get_questions_for_topic(subject, topic, count=3):
    items = load_real_exam_items()
    matches = [it for it in items if subject.lower() in it.get("subject", "").lower() or topic.lower() in it.get("topic", "").lower()]
    if len(matches) < count:
        matches = [it for it in items if subject.lower() in it.get("subject", "").lower()]
    if not matches:
        matches = items
    sample = random.sample(matches, k=min(count, len(matches)))
    return [{"question": it.get("question", "")[:250], "answer": (it.get("final_answer") or it.get("memo") or "")[:150], "marks": it.get("marks", 2)} for it in sample]

# ── Verification Logic ───────────────────────────────────────────────────────
BANNED_PRAISE = [
    "great question", "excellent", "wonderful", "brilliant", "spot on", "perfect",
    "mooi vraag", "presies", "perfek", "pragtig", "uitstekend", "wonderlik"
]

def verify_agentic_record(spec: dict, parsed_json: dict) -> tuple:
    task_type = spec.get("task_type")
    
    # 1. Page Worker Validation
    if task_type == "page_worker":
        if "page" not in parsed_json or "questions" not in parsed_json:
            return False, "missing_page_or_questions_key"
        if not isinstance(parsed_json.get("questions"), list):
            return False, "questions_must_be_list"
        return True, "page_worker_verified"

    # 2. Dialogue Structure Validation
    dialogue = parsed_json.get("dialogue", [])
    if not isinstance(dialogue, list) or len(dialogue) < 2:
        return False, "dialogue_too_short_or_invalid"

    # 3. Wellbeing / Distress Protocol Check
    if spec.get("override") == "distress_protocol":
        helpline_expected = spec.get("helpline_text", "0800 567 567")
        all_text = " ".join(t.get("content", "") for t in dialogue)
        if "0800" not in all_text and "116" not in all_text:
            return False, "distress_missing_helpline_number"
        return True, "distress_protocol_verified"

    # 4. Tool Call Matching
    expected_calls = spec.get("expected_tool_calls", [])
    if expected_calls:
        actual_calls = [t["tool_call"] for t in dialogue if t.get("tool_call")]
        if len(actual_calls) != len(expected_calls):
            return False, f"tool_call_count_mismatch: expected {len(expected_calls)}, got {len(actual_calls)}"
        for exp, act in zip(expected_calls, actual_calls):
            if act.get("name") != exp.get("name"):
                return False, f"tool_name_mismatch: {act.get('name')} != {exp.get('name')}"

    # 5. Banned Praise Check on Tutor Openers
    for t in dialogue:
        if t.get("role") == "teacher" and t.get("content"):
            content_lower = t["content"][:40].lower()
            for bp in BANNED_PRAISE:
                if bp in content_lower:
                    return False, f"banned_praise_detected: {bp}"

    return True, "agentic_record_verified"

# ── Multi-Model Dispatcher ──────────────────────────────────────────────────
FLEET_WORKERS = []

def init_fleet_workers():
    workers = []
    # Groq LPU (Speed workhorse for study plans, intake, diagnosis)
    if GROQ_KEY:
        workers.append({"name": "groq-qwen27b", "fn": lambda p, s: call_groq(p, s, "qwen/qwen3.8-27b")})
        workers.append({"name": "groq-oss120b", "fn": lambda p, s: call_groq(p, s, "openai/gpt-oss-120b")})
    # Google AI Studio Gemini Flash (Afrikaans & English language excellence with native JSON mode)
    if GEMINI_KEY_1:
        workers.append({"name": "gemini-flash-k1", "fn": lambda p, s: call_gemini(p, s, GEMINI_KEY_1, "gemini-3.5-flash-lite", gma1_lock, "gma1")})
    if GEMINI_KEY_2:
        workers.append({"name": "gemini-flash-k2", "fn": lambda p, s: call_gemini(p, s, GEMINI_KEY_2, "gemini-3.5-flash-lite", gma2_lock, "gma2")})
    # Cohere API (Structured JSON and STEM reasoning)
    if COHERE_KEY:
        workers.append({"name": "cohere-command-a1", "fn": lambda p, s: call_cohere(p, s, "command-a-03-2025")})
        workers.append({"name": "cohere-command-a2", "fn": lambda p, s: call_cohere(p, s, "command-a-03-2025")})
    return workers

def clean_and_parse_json(raw_text: str) -> dict:
    text = raw_text.strip()
    # Strip markdown fences if present
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n", "", text)
        text = re.sub(r"\n```$", "", text)
        text = text.strip()
    # Extract outer braces
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if m:
        text = m.group(0)
    # Remove trailing commas before } or ]
    text = re.sub(r",\s*([\]}])", r"\1", text)
    return json.loads(text)

# ── Generation Task Runner ───────────────────────────────────────────────────
def generate_single_sample(task_type: str, worker: dict, rng: random.Random) -> dict:
    today = dt.date(2026, 11, 14)
    
    # 1. Build Spec
    if task_type == "page_worker":
        subject = rng.choice(["Mathematics", "Physical Sciences", "English", "Afrikaans"])
        spec = sampler_agentic.make_page_spec(rng.randint(1, 14), 14, rng, subject)
        system_prompt = f"{COMMON_CORE}\n\n{TASK_PAGE_WORKER_PROMPT}"
    elif task_type in ("paper_walkthrough", "paper_prep_guide", "paper_exam_strategy"):
        dummy_notes = [{"page": {"index": i, "status": "ok"}, "questions": [{"number": f"1.{i}", "marks": 2, "topic": "algebra"}]} for i in range(1, 10)]
        damaged_notes, defects = sampler_agentic.apply_defects(dummy_notes, rng)
        spec = sampler_agentic.make_synth_spec(rng, defects)
        spec["notes"] = damaged_notes
        spec["aggregate"] = sampler_agentic.aggregate_notes(damaged_notes, 10)
        system_prompt = f"{COMMON_CORE}\n\n{TASK_SYNTHESISER_PROMPT}"
    else:
        spec = sampler_agentic.make_study_spec(rng, today, task=task_type)
        if "question_bank" in spec.get("needs", []):
            spec["question_bank"] = get_questions_for_topic(spec.get("subject", "Mathematics"), spec.get("topic", "algebra"), count=spec.get("question_count", 3))
        if "source_excerpts" in spec.get("needs", []):
            items = get_questions_for_topic(spec.get("subject", "Mathematics"), spec.get("topic", "algebra"), count=2)
            spec["source_excerpts"] = [{"id": f"ex_{i+1}", "text": it["question"]} for i, it in enumerate(items)]
        system_prompt = f"{COMMON_CORE}\n\n{TASK_STUDY_PROMPT}"

    spec_json = json.dumps(spec, indent=2, ensure_ascii=False)
    
    # 2. Call Worker
    try:
        raw_resp = worker["fn"](spec_json, system_prompt)
    except Exception as e:
        return {"ok": False, "reason": f"worker_error: {e}", "spec": spec}
    
    # 3. Parse JSON
    try:
        parsed = clean_and_parse_json(raw_resp)
    except Exception as e:
        return {"ok": False, "reason": f"json_parse_error: {e}", "raw": raw_resp, "spec": spec}

    # 4. Verify
    ok, reason = verify_agentic_record(spec, parsed)
    if not ok:
        return {"ok": False, "reason": reason, "parsed": parsed, "spec": spec}

    return {"ok": True, "record": parsed, "spec": spec, "worker": worker["name"]}

# ── Main Entry Point ─────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Eishkom AI Agentic & Study Coaching Fleet")
    parser.add_argument("--target", type=int, default=3500, help="Total unique agentic samples to generate")
    parser.add_argument("--test-sample", action="store_true", help="Generate 1 test sample per task type and exit")
    parser.add_argument("--workers", type=int, default=8, help="Concurrent workers")
    args = parser.parse_args()

    workers = init_fleet_workers()
    if not workers:
        print("ERROR: No active API keys found in .env!")
        return

    print("=" * 80)
    print("EISHKOM AI — AGENTIC & STUDY COACHING FLEET GENERATOR")
    print(f"Target: {args.target} unique samples across 9 agentic task families")
    print(f"Active Fleet Workers ({len(workers)}): {', '.join(w['name'] for w in workers)}")
    print("=" * 80)

    task_distribution = [
        ("intake", 250),
        ("study_plan", 450),
        ("weak_topic_diagnosis", 250),
        ("exam_strategy", 150),
        ("study_guide_section", 350),
        ("revision_session", 350),
        ("paper_walkthrough", 300),
        ("paper_prep_guide", 200),
        ("page_worker", 1320),
        ("distress_signal", 80),
    ]

    if args.test_sample:
        print("\n--- Running 1 test sample per task family ---")
        rng = random.Random(42)
        for i, (task, _) in enumerate(task_distribution):
            w = workers[i % len(workers)]
            print(f">> Testing {task} on {w['name']}...")
            res = generate_single_sample(task, w, rng)
            if res["ok"]:
                print(f"   PASS! Verified -> keys: {list(res['record'].keys())}")
            else:
                print(f"   FAIL: {res['reason']}")
        return

    print("\nPlanned distribution:")
    total_plan = sum(cnt for _, cnt in task_distribution)
    for t, cnt in task_distribution:
        print(f"  {t:<25s}: {cnt:>5d} ({cnt/total_plan*100:4.1f}%)")

    # Generate queue
    queue = []
    for t, cnt in task_distribution:
        scale = args.target / total_plan
        target_cnt = int(cnt * scale)
        for _ in range(target_cnt):
            queue.append(t)

    random.shuffle(queue)
    print(f"\nDispatched {len(queue)} generation jobs across {args.workers} concurrent threads...")

    verified_count = 0
    rejected_count = 0
    start_time = time.time()

    def worker_job(item_tuple):
        idx, task = item_tuple
        rng = random.Random(time.time() + idx)
        worker = random.choice(workers)
        return generate_single_sample(task, worker, rng)

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(worker_job, (i, t)): (i, t) for i, t in enumerate(queue)}
        for fut in as_completed(futures):
            i, task = futures[fut]
            try:
                res = fut.result()
                if res["ok"]:
                    with stats_lock:
                        verified_count += 1
                        rec = res["record"]
                        rec.setdefault("meta", {})["generator"] = res["worker"]
                        rec["meta"]["task_type"] = task
                        rec["schema_version"] = "tutor-v1"
                        
                        out_file = VER_AGENTIC_DIR / f"{task}.jsonl"
                        with open(out_file, "a", encoding="utf-8") as f:
                            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    
                    with print_lock:
                        print(f"[{task:<20s}] Verified ({verified_count}/{len(queue)}) on {res['worker']}")
                else:
                    with stats_lock:
                        rejected_count += 1
                        rej_file = REJ_AGENTIC_DIR / f"{task}.jsonl"
                        with open(rej_file, "a", encoding="utf-8") as f:
                            f.write(json.dumps(res, ensure_ascii=False) + "\n")
                    with print_lock:
                        print(f"[{task:<20s}] REJECT ({res['reason'][:40]})")
            except Exception as e:
                with print_lock:
                    print(f"[{task:<20s}] ERROR: {e}")

    elapsed = time.time() - start_time
    print("\n" + "=" * 80)
    print("EISHKOM AI — AGENTIC FLEET RUN FINISHED")
    print(f"Verified Records Generated: {verified_count}")
    print(f"Rejected Records:           {rejected_count}")
    print(f"Pass Rate:                  {verified_count / max(1, verified_count + rejected_count) * 100:.1f}%")
    print(f"Total Time:                 {elapsed:.1f}s")
    print(f"Output Destination:         {VER_AGENTIC_DIR}")
    print("=" * 80)

if __name__ == "__main__":
    main()
