#!/usr/bin/env python3
"""
ingest_vision.py - Multimodal document vision extraction using Gemini Vision.

Directly ingests South African DBE exam PDFs into clean Markdown and KaTeX LaTeX,
accurately handling MathType formulas, multi-column layouts, scanned image pages,
and geometric diagrams without any third-party PDF text mangling.

Usage:
    # Batch 1: Maths and Wiskunde
    python pipeline/ingest_vision.py --subjects mathematics,wiskunde

    # Batch 2: English
    python pipeline/ingest_vision.py --subjects english

    # Batch 3: Afrikaans
    python pipeline/ingest_vision.py --subjects afrikaans

    # Batch 4: Physical Sciences and Fisiese Wetenskappe
    python pipeline/ingest_vision.py --subjects physical,fisiese

    # Full Pipeline in User Order:
    python pipeline/ingest_vision.py --pipeline-order
"""
import argparse
import base64
import csv
import datetime
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KIT_ROOT))
from wspaths import p  # noqa: E402


PROMPT_QP = """You are an expert transcriber for South African DBE (Department of Basic Education) past examination papers.
Transcribe this entire exam paper faithfully into clean Markdown.

RULES:
1. MATHEMATICS & FORMULAS: Convert all equations, fractions, radicals, indices, and chemical formulas into standard KaTeX LaTeX ($...$ inline, $$...$$ display block). Never omit or invent equations.
2. QUESTION NUMBERING: Keep exact numbering: QUESTION 1, 1.1, 1.1.1, 1.1.2, 1.2, etc.
3. MARKS: Preserve all mark allocations, e.g. (3), [24].
4. DIAGRAMS: If a question references a geometry diagram, circuit, graph, or illustration, write a concise, complete description of all given geometric relations, vertices, angles, parallel lines, tangents, resistors, or coordinates inside:
   [DIAGRAM: concise description of points, lines, angles, and components]
5. LAYOUT: Preserve sections (SECTION A, SECTION B), tables, and instructions cleanly in Markdown.
"""

PROMPT_MEMO = """You are an expert transcriber for South African DBE past examination marking guidelines (memorandums).
Transcribe this entire marking guideline faithfully into clean Markdown.

RULES:
1. MATHEMATICS & FORMULAS: Convert all worked steps, equations, fractions, and solutions into standard KaTeX LaTeX ($...$ inline, $$...$$ display block).
2. NUMBERING & CRITERIA: Preserve exact question numbering (1.1.1, 1.1.2) and all marking criteria with checkmarks (✓ substitution, ✓ answer, etc.).
3. ALTERNATIVES: Clearly document alternative solutions marked OR/OF.
4. MARKS: Keep total marks for sub-questions (e.g. (4)) and whole questions (e.g. [24]).
5. Be 100% faithful to the official marking rubric.
"""


def load_api_key():
    for base in (Path.cwd(), KIT_ROOT):
        env_file = base / ".env"
        if env_file.exists():
            for line in env_file.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line.startswith("TEACHER_API_KEY=") or line.startswith("GEMINI_API_KEY="):
                    k = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if k:
                        return k
    return os.environ.get("GEMINI_API_KEY") or os.environ.get("TEACHER_API_KEY")


QUOTA_FILE = KIT_ROOT / "workspace" / "text" / ".quota_exhausted.json"

MODEL_POOL = [
    "gemini-3.1-flash-lite",    # 500 requests/day, fast & high limit
    "gemini-3.8-flash",         # 20 requests/day, new flagship flash
    "gemini-3-flash-preview",   # 20 requests/day, high-fidelity
    "gemini-3.5-flash-lite",    # 500 requests/day
    "gemini-flash-latest"       # fallback general flash
]


def load_exhausted_models():
    """Load models that hit their daily limit today. Automatically resets at midnight (start of new day)."""
    today_str = datetime.date.today().isoformat()
    if QUOTA_FILE.exists():
        try:
            data = json.loads(QUOTA_FILE.read_text(encoding="utf-8"))
            if data.get("date") == today_str:
                return set(data.get("exhausted_models", []))
        except Exception:
            pass
    # If file doesn't exist or date is older (past midnight), reset automatically
    return set()


def mark_model_exhausted(model_name):
    """Mark a model as exhausted for today and persist to disk so it is not retried until tomorrow."""
    today_str = datetime.date.today().isoformat()
    current = load_exhausted_models()
    current.add(model_name)
    QUOTA_FILE.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "date": today_str,
        "exhausted_models": sorted(list(current)),
        "updated_at": datetime.datetime.now().isoformat()
    }
    QUOTA_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"\n    [Daily Quota Reached] Marked {model_name} as EXHAUSTED for {today_str}. Will NOT retry until tomorrow (12:00 AM reset).", flush=True)


def call_gemini_vision(pdf_bytes, prompt, api_key, model=None, retries=6):
    pdf_b64 = base64.b64encode(pdf_bytes).decode("utf-8")
    exhausted_today = load_exhausted_models()

    # Filter out models that are already known to be exhausted for today
    available_models = [m for m in MODEL_POOL if m not in exhausted_today]
    if model and model in available_models:
        available_models.remove(model)
        available_models.insert(0, model)

    if not available_models:
        raise RuntimeError("All configured Gemini vision models have exhausted their daily quotas for today! Will reset automatically at 12:00 AM.")

    current_idx = 0
    last_err = None

    for attempt in range(retries):
        if current_idx >= len(available_models):
            break
        cur_model = available_models[current_idx]
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{cur_model}:generateContent?key={api_key}"
        payload = {
            "contents": [{
                "parts": [
                    {"inlineData": {"mimeType": "application/pdf", "data": pdf_b64}},
                    {"text": prompt}
                ]
            }],
            "generationConfig": {
                "temperature": 0.1,
                "maxOutputTokens": 8192
            }
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})

        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                cand = res.get("candidates", [{}])[0]
                if cand.get("finishReason") == "RECITATION":
                    raise RuntimeError("RECITATION copyright filter (handled via marking memo)")
                parts = cand.get("content", {}).get("parts", [])
                if not parts:
                    raise RuntimeError(f"Empty content from {cur_model}: finishReason={cand.get('finishReason')}")
                return parts[0]["text"], cur_model
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", "ignore")[:300]
            last_err = f"HTTP {e.code}: {err_body}"
            # Check for daily quota exhaustion -> record in persistent ledger and skip
            if e.code == 429 and ("limit exceeded" in err_body.lower() or "quota" in err_body.lower()):
                mark_model_exhausted(cur_model)
                current_idx += 1
                if current_idx < len(available_models):
                    next_model = available_models[current_idx]
                    print(f"\n    [Auto-Switch] Rotating directly to active model: {next_model}...", flush=True)
                    time.sleep(1)
                    continue
            if e.code in (429, 503):
                # Rotate immediately to the next available model if possible
                if current_idx + 1 < len(available_models):
                    current_idx += 1
                    next_model = available_models[current_idx]
                    print(f"\n    [Status {e.code} on {cur_model}] Rotating immediately to: {next_model}...", flush=True)
                    time.sleep(1)
                    continue
                else:
                    wait = min(20, (2 ** attempt) * 2)
                    print(f"\n    [Status {e.code} on {cur_model}] Pausing {wait}s before retry...", flush=True)
                    time.sleep(wait)
                    continue
            raise RuntimeError(last_err) from e
        except Exception as e:
            if "RECITATION" in str(e):
                raise e
            last_err = str(e)
            time.sleep(2)
    raise RuntimeError(f"Failed after retries: {last_err}")


def is_already_vision_extracted(txt_path):
    if not txt_path.exists():
        return False
    try:
        content = txt_path.read_text(encoding="utf-8", errors="ignore")
        if len(content) < 1000:
            return False
        # Vision-extracted indicators (Math, Science, or Language papers)
        indicators = ["$$", "\\tag{", "[DIAGRAM:", "\\checkmark", "QUESTION", "VRAAG", "AFDELING", "SECTION", "PUNTE:", "MARKS:"]
        matches = sum(1 for ind in indicators if ind in content)
        return matches >= 2
    except Exception:
        return False


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", help="Process a single source_id from sources.csv")
    ap.add_argument("--subjects", help="Comma-separated subjects (e.g. mathematics,wiskunde)")
    ap.add_argument("--pipeline-order", action="store_true", help="Execute in exact curriculum order: Maths/Wiskunde -> English -> Afrikaans -> Physics/Fisiese")
    ap.add_argument("--limit", type=int, default=0, help="Limit number of files to process per subject/batch")
    ap.add_argument("--force", action="store_true", help="Overwrite existing extracted text")
    ap.add_argument("--delay", type=float, default=4.0, help="Delay in seconds between requests (default: 4.0s for 15 RPM)")
    ap.add_argument("--model", default="gemini-3.1-flash-lite", help="Preferred Gemini vision model (default: gemini-3.1-flash-lite)")
    a = ap.parse_args()

    api_key = load_api_key()
    if not api_key:
        sys.exit("Error: No GEMINI_API_KEY or TEACHER_API_KEY found in .env")

    sources_path = p("sources", "sources.csv")
    if not sources_path.exists():
        sys.exit(f"Sources file not found at {sources_path}")

    all_rows = []
    with open(sources_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for r in reader:
            all_rows.append(r)

    # Determine batches
    if a.pipeline_order:
        stages = [
            ("Stage 1: Mathematics & Wiskunde", ["mathematics", "wiskunde"]),
            ("Stage 2: English (HL & FAL)", ["english"]),
            ("Stage 3: Afrikaans (HT & EAT)", ["afrikaans"]),
            ("Stage 4: Physical Sciences & Fisiese Wetenskappe", ["physical", "fisiese"]),
        ]
    elif a.subjects:
        subj_list = [s.strip().lower() for s in a.subjects.split(",") if s.strip()]
        stages = [(f"Subjects: {', '.join(subj_list)}", subj_list)]
    elif a.source:
        stages = [(f"Single source: {a.source}", [a.source])]
    else:
        stages = [("All Sources", [""])]

    out_dir = p("text")
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"=== Eishkom Stage 1 Vision Extraction Pipeline (Model: {a.model}) ===")
    print(f"Output directory: {out_dir}")
    print(f"Safety delay: {a.delay}s per request (stays strictly within free tier quota)\n")

    grand_total_extracted = 0
    grand_total_skipped = 0

    for stage_name, subj_filters in stages:
        if a.source:
            stage_rows = [r for r in all_rows if r["source_id"] == a.source]
        else:
            stage_rows = [r for r in all_rows if any(sf in r["subject"].lower() for sf in subj_filters)]

        if a.limit:
            stage_rows = stage_rows[:a.limit]

        print(f"--------------------------------------------------------------------------------", flush=True)
        print(f"Starting {stage_name} ({len(stage_rows)} documents)...", flush=True)
        print(f"--------------------------------------------------------------------------------", flush=True)

        stage_extracted = 0
        stage_skipped = 0

        for idx, row in enumerate(stage_rows, 1):
            sid = row["source_id"]
            rel_pdf = row.get("local_path") or row.get("path")
            pdf_file = p("raw") / rel_pdf if not str(rel_pdf).startswith("workspace") else KIT_ROOT / rel_pdf
            out_txt = out_dir / f"{sid}.txt"

            if not pdf_file.exists():
                print(f"[{idx}/{len(stage_rows)}] [{sid}] SKIPPED (raw PDF not found: {pdf_file.name})")
                stage_skipped += 1
                continue

            if not a.force and is_already_vision_extracted(out_txt):
                existing_len = len(out_txt.read_text(encoding="utf-8", errors="ignore"))
                print(f"[{idx}/{len(stage_rows)}] [{sid}] SKIPPED: Already Vision Extracted ({existing_len:,} chars with LaTeX)")
                stage_skipped += 1
                continue

            is_memo = "memo" in sid.lower()
            prompt = PROMPT_MEMO if is_memo else PROMPT_QP

            sz_kb = os.path.getsize(pdf_file) / 1024
            print(f"[{idx}/{len(stage_rows)}] [{sid}] Vision extracting {pdf_file.name} ({sz_kb:.1f} KB)...", end=" ", flush=True)

            try:
                t0 = time.time()
                pdf_bytes = pdf_file.read_bytes()
                extracted_text, used_model = call_gemini_vision(pdf_bytes, prompt, api_key, model=a.model)
                out_txt.write_text(extracted_text, encoding="utf-8")
                elapsed = time.time() - t0
                print(f"DONE via {used_model} ({len(extracted_text):,} chars in {elapsed:.1f}s)", flush=True)
                stage_extracted += 1
                time.sleep(a.delay)
            except Exception as e:
                print(f"FAILED: {e}", flush=True)

        print(f"Completed {stage_name}: {stage_extracted} extracted, {stage_skipped} skipped.\n", flush=True)
        grand_total_extracted += stage_extracted
        grand_total_skipped += stage_skipped

    print(f"=== Pipeline Run Complete: {grand_total_extracted} extracted, {grand_total_skipped} skipped. ===", flush=True)


if __name__ == "__main__":
    main()
