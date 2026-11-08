#!/usr/bin/env python3
"""
fast_batch_extract.py — Ultra-fast, high-fidelity curriculum item extraction pipeline.
Follows the Universal Document & Visual Extraction Standard (UDVES) for Eishkom AI.
Strictly restricted to user-approved models:
  1. gemini-3.1-flash-lite (Primary: 15 RPM, 250K TPM, 500 RPD)
  2. gemma-4-26b-a4b-it   (Secondary: 30 RPM, 16K TPM, 14.4K RPD)
  3. gemma-4-31b-it       (Tertiary: 30 RPM, 16K TPM, 14.4K RPD)
"""

import os
import sys
import json
import re
import time
import argparse
import urllib.request
import urllib.error
from pathlib import Path

# Fix stdout encoding for Windows
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
WORKSPACE = ROOT_DIR / "workspace"
KIT_WORKSPACE = ROOT_DIR / "sa-tutor-kit" / "sa-tutor-kit" / "workspace"

def load_env():
    env_file = ROOT_DIR / ".env"
    if env_file.exists():
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    v = v.strip().strip("'\"")
                    if k not in os.environ:
                        os.environ[k] = v

load_env()
API_KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")

# STRICTLY ALLOWED MODELS ONLY
ALLOWED_MODELS = [
    "gemini-3.1-flash-lite",
    "gemma-4-26b-a4b-it",
    "gemma-4-31b-it"
]

def call_ai_studio(prompt: str, preferred_model: str = "gemini-3.1-flash-lite") -> str:
    """Calls AI Studio across strictly allowed models with automatic failover."""
    models_to_try = [preferred_model] + [m for m in ALLOWED_MODELS if m != preferred_model]
    headers = {"Content-Type": "application/json"}
    
    for model in models_to_try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={API_KEY}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        if "flash" in model:
            payload["generationConfig"] = {"responseMimeType": "application/json"}
            
        data = json.dumps(payload).encode("utf-8")
        
        # Try up to 3 times per model for transient errors
        for attempt in range(3):
            try:
                req = urllib.request.Request(url, data=data, headers=headers)
                timeout = 60 if "flash" in model else 90
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    res = json.loads(resp.read().decode("utf-8"))
                    cand = res.get("candidates", [{}])[0]
                    parts = cand.get("content", {}).get("parts", [])
                    if parts:
                        return parts[0].get("text", "")
            except urllib.error.HTTPError as e:
                err_body = e.read().decode("utf-8") if hasattr(e, "read") else ""
                if e.code in (503, 429) and attempt < 2:
                    wait_sec = 4 * (attempt + 1)
                    print(f"  [API {e.code}] {model} busy. Retrying in {wait_sec}s...")
                    time.sleep(wait_sec)
                    continue
                print(f"  [API {e.code}] {model} error. Switching to next model...")
                time.sleep(2)
                break
            except Exception as e:
                print(f"  [{model} Exception]: {e}")
                time.sleep(2)
                break
                
    raise RuntimeError("All approved models (Gemini 3.1 Flash Lite, Gemma 4 26B, Gemma 4 31B) failed for this chunk.")

def robust_json_loads(text: str):
    """Parses JSON safely handling unescaped LaTeX backslashes."""
    try:
        return json.loads(text, strict=False)
    except Exception:
        pass
    # Escape any backslash that precedes letters (e.g. \checkmark, \text, \frac)
    cleaned = re.sub(r'(?<!\\)\\(?=[a-zA-Z])', r'\\\\', text)
    try:
        return json.loads(cleaned, strict=False)
    except Exception:
        pass
    cleaned2 = re.sub(r'\\(?![/"\\bfnrtu]|u[0-9a-fA-F]{4})', r'\\\\', text)
    return json.loads(cleaned2, strict=False)

def extract_json_array(text: str):
    """Robustly extracts a JSON array from AI output with LaTeX preservation."""
    text = text.strip()
    match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', text)
    if match:
        content = match.group(1).strip()
        try:
            parsed = robust_json_loads(content)
            if isinstance(parsed, list):
                return parsed
        except Exception:
            pass
    for pattern in [r'(\[[\s\S]*\])']:
        m = re.search(pattern, text)
        if m:
            try:
                parsed = robust_json_loads(m.group(1))
                if isinstance(parsed, list):
                    return parsed
            except Exception:
                pass
    parsed = robust_json_loads(text)
    if isinstance(parsed, dict) and "items" in parsed:
        return parsed["items"]
    if isinstance(parsed, list):
        return parsed
    return [parsed]

def split_exam_chunks(text: str, is_memo: bool = False):
    """Splits an exam text into question chunks by headers."""
    pattern = r'(?:\n|^)\s*(?:#+\s*)?(?:QUESTION|VRAAG)\s*([0-9]+)'
    matches = list(re.finditer(pattern, text, re.IGNORECASE))
    
    if not matches or len(matches) < 3:
        pattern_sec = r'(?:\n|^)\s*(?:#+\s*)?(?:SECTION|AFDELING)\s*([A-E])'
        matches = list(re.finditer(pattern_sec, text, re.IGNORECASE))
    
    if not matches:
        return [("1", text)]
    
    chunks = []
    for i, m in enumerate(matches):
        q_label = m.group(1)
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        chunks.append((q_label, text[start:end].strip()))
    return chunks

def extract_question_chunk(source_id: str, memo_id: str, subject: str, grade: int, lang: str, track: str,
                           q_label: str, qp_chunk: str, memo_chunk: str, preferred_model: str):
    prompt = f"""You are an expert South African CAPS curriculum educational data extraction assistant following UDVES.
Extract all atomic subquestions for Question/Section {q_label} from the Question Paper and Memorandum into a JSON array.

SOURCE DETAILS:
- source_id: {source_id}
- pair_source_id: {memo_id}
- subject: {subject}
- grade: {grade}
- language: {lang}
- track: {track}

RULES & UDVES CONTRACT:
1. Extract every subquestion (e.g. {q_label}.1, {q_label}.2.1, etc.) as an atomic item.
   - For Multiple Choice (Q1): each subquestion (1.1 to 1.10) MUST be an atomic item with marks=2.
2. Put any reading text, data table, or diagram description into the "passage" field.
   - Format diagrams as: [DIAGRAM: <Type> | <Details> | <Values>]
3. Standardize math into KaTeX LaTeX ($...$ inline, $$...$$ display).
   - In math mode use comma decimal: $0{{,}}15$, degree Celsius: $^\\circ\\text{{C}}$.
   - In "final_answer" use standard decimal point: 0.15.
4. Put all method marks and worked steps into "memo", with checkmarks formatted as $\\checkmark$.
5. Strictly ensure all '$' delimiters are balanced.

OUTPUT FORMAT:
Return a JSON array of objects:
[
  {{
    "item_id": "{source_id}-{q_label}.1",
    "source_id": "{source_id}",
    "pair_source_id": "{memo_id}",
    "subject": "{subject}",
    "grade": {grade},
    "language": "{lang}",
    "track": "{track}",
    "kind": "question",
    "question_ref": "{q_label}.1",
    "marks": <integer>,
    "topic": "<topic name>",
    "passage": "<table, diagram or text preamble, or empty>",
    "question": "<verbatim question text with KaTeX>",
    "memo": "<marking guideline steps $\\checkmark$>",
    "final_answer": "<short concise answer>",
    "needs_review": false,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
  }}
]

QUESTION PAPER CHUNK:
{qp_chunk}

MEMORANDUM CHUNK:
{memo_chunk}
"""
    raw_response = call_ai_studio(prompt, preferred_model=preferred_model)
    items = extract_json_array(raw_response)
    
    cleaned = []
    for it in items:
        q_ref = str(it.get("question_ref", "")).strip()
        slug = re.sub(r'[^a-zA-Z0-9_\.]', '', q_ref).strip(".")
        if not slug:
            slug = f"{q_label}.1"
        it["item_id"] = f"{source_id}-{slug}"
        it["source_id"] = source_id
        it["pair_source_id"] = memo_id
        it["subject"] = subject
        it["grade"] = grade
        it["language"] = lang
        it["track"] = track
        it["licence"] = "DBE copyright - check terms"
        it["attribution"] = "Department of Basic Education"
        if "marks" in it:
            try:
                it["marks"] = int(it["marks"])
            except Exception:
                it["marks"] = 1
        cleaned.append(it)
    return cleaned

def process_paper(source_id: str, preferred_model: str = "gemini-3.1-flash-lite"):
    print(f"\n========================================================")
    print(f"  PROCESSING: {source_id} (Model: {preferred_model})")
    print(f"========================================================")
    
    parts = source_id.split("-")
    subject = parts[1]
    grade = 12
    lang = "af" if "afrikaans" in subject or "wiskunde" in subject or "fisiese" in subject else "en"
    
    if subject in ["mathematics", "wiskunde"]:
        track = "core_maths"
    elif subject in ["physical_sciences", "fisiese_wetenskappe"]:
        track = "sciences"
    elif "hl" in subject:
        track = "languages_hl"
    else:
        track = "languages_fal"
        
    qp_txt = WORKSPACE / "text" / f"{source_id}.txt"
    memo_id = f"{source_id}-memo"
    memo_txt = WORKSPACE / "text" / f"{memo_id}.txt"
    
    if not qp_txt.exists() or not memo_txt.exists():
        print(f"  [ERROR] Missing text files for {source_id}")
        return False
        
    with open(qp_txt, "r", encoding="utf-8") as f:
        qp_text = f.read()
    with open(memo_txt, "r", encoding="utf-8") as f:
        memo_text = f.read()
        
    qp_chunks = split_exam_chunks(qp_text, is_memo=False)
    memo_chunks = dict(split_exam_chunks(memo_text, is_memo=True))
    
    print(f"  Detected {len(qp_chunks)} question chunks in QP.")
    all_paper_items = []
    
    for q_label, qp_chunk in qp_chunks:
        memo_chunk = memo_chunks.get(q_label, "")
        if not memo_chunk and len(qp_chunks) == len(memo_chunks):
            memo_chunk = list(memo_chunks.values())[qp_chunks.index((q_label, qp_chunk))]
            
        print(f"  Extracting Q/Section {q_label}...", end=" ", flush=True)
        t0 = time.time()
        try:
            items = extract_question_chunk(
                source_id, memo_id, subject, grade, lang, track,
                q_label, qp_chunk, memo_chunk, preferred_model
            )
            elapsed = time.time() - t0
            q_marks = sum(it.get("marks", 0) for it in items)
            print(f"OK! ({len(items)} items, {q_marks}m in {elapsed:.1f}s)")
            all_paper_items.extend(items)
        except Exception as e:
            print(f"FAILED: {e}")
            return False
        time.sleep(3.5) # Exactly respects 15 RPM limit
        
    total_marks = sum(it.get("marks", 0) for it in all_paper_items)
    print(f"\n  Summary: {source_id} -> {len(all_paper_items)} items | {total_marks} marks")
    
    # KaTeX check
    unbalanced = 0
    for it in all_paper_items:
        for f in ["question", "memo", "passage", "final_answer"]:
            val = it.get(f) or ""
            if val.count("$") % 2 != 0:
                unbalanced += 1
    if unbalanced > 0:
        print(f"  [KaTeX Error] {unbalanced} unbalanced dollars found!")
        return False
        
    destinations = [
        WORKSPACE / "items" / subject / f"{source_id}.jsonl",
        WORKSPACE / "items" / f"{source_id}.jsonl",
        KIT_WORKSPACE / "items" / subject / f"{source_id}.jsonl",
        KIT_WORKSPACE / "items" / f"{source_id}.jsonl"
    ]
    
    for dst in destinations:
        dst.parent.mkdir(parents=True, exist_ok=True)
        with open(dst, "w", encoding="utf-8") as f:
            for it in all_paper_items:
                f.write(json.dumps(it, ensure_ascii=False) + "\n")
        print(f"  Saved -> {dst}")
        
    dec_entry = f"""
## 2026-11-07: Fast Batch Extraction: `{source_id}`

- **Paper ID:** `{source_id}`
- **Subject / Track:** `{subject}` / `{track}`
- **Model Used:** `{preferred_model}`
- **Metrics:** Exactly {len(all_paper_items)} atomic items, {total_marks} marks accounted for.
- **KaTeX Health:** 0 delimiter errors, 100% balanced $.
- **Storage:** Quad-mirrored across `workspace/items/` and `sa-tutor-kit/sa-tutor-kit/workspace/items/`.
"""
    for dec_file in [WORKSPACE / "DECISIONS.md", KIT_WORKSPACE / "DECISIONS.md"]:
        if dec_file.exists():
            with open(dec_file, "a", encoding="utf-8") as f:
                f.write(dec_entry)
                
    return True

def get_pending_queue(subject_filter: str = None):
    eval_locked = [
        "dbe-maths-g12-p1-2024-nov", "dbe-afrikaans_fal-g12-p1-2024-nov",
        "dbe-afrikaans_fal-g12-p2-2024-nov", "dbe-afrikaans_hl-g12-p1-2024-nov",
        "dbe-afrikaans_hl-g12-p2-2024-nov", "dbe-english_fal-g12-p1-2024-nov",
        "dbe-english_fal-g12-p2-2024-nov"
    ]
    text_dir = WORKSPACE / "text"
    items_dir = WORKSPACE / "items"
    
    all_qp_files = [
        f.stem for f in text_dir.glob("*.txt") 
        if re.match(r"^dbe-[a-z_]+-g\d+-[pv]\d+-\d{4}-(?:may|nov)$", f.stem)
    ]
    pending = []
    for pid in sorted(all_qp_files):
        if pid in eval_locked or "2024-nov" in pid or "2024-may" in pid:
            continue
        target_jsonl = items_dir / f"{pid}.jsonl"
        if target_jsonl.exists() and target_jsonl.stat().st_size > 1000:
            continue
        if subject_filter and subject_filter not in pid:
            continue
        pending.append(pid)
    return pending

def main():
    parser = argparse.ArgumentParser(description="Eishkom AI Fast Batch Extractor")
    parser.add_argument("--paper", help="Process single specific source_id")
    parser.add_argument("--subject", help="Filter by subject")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of papers (0 = all)")
    parser.add_argument("--model", default="gemini-3.1-flash-lite", choices=ALLOWED_MODELS, help="Allowed models only")
    parser.add_argument("--list-pending", action="store_true", help="List pending papers")
    args = parser.parse_args()
    
    if not API_KEY:
        print("[FATAL] No GEMINI_API_KEY in .env!")
        sys.exit(1)
        
    if args.list_pending:
        queue = get_pending_queue(args.subject)
        print(f"Total pending: {len(queue)}")
        for p in queue:
            print(f"  - {p}")
        return
        
    if args.paper:
        ok = process_paper(args.paper, preferred_model=args.model)
        if ok:
            sync_script = KIT_WORKSPACE / "tools" / "sync_tracker.py"
            if sync_script.exists():
                os.system(f"python \"{sync_script}\"")
        return
        
    queue = get_pending_queue(args.subject)
    print(f"Pending papers in queue: {len(queue)}")
    if args.limit > 0:
        queue = queue[:args.limit]
        print(f"Running batch of {args.limit} papers...")
        
    completed = 0
    for pid in queue:
        ok = process_paper(pid, preferred_model=args.model)
        if ok:
            completed += 1
            sync_script = KIT_WORKSPACE / "tools" / "sync_tracker.py"
            if sync_script.exists():
                os.system(f"python \"{sync_script}\"")
        time.sleep(2)
        
    print(f"\n[ALL COMPLETE] Successfully processed {completed} / {len(queue)} papers.")

if __name__ == "__main__":
    main()
