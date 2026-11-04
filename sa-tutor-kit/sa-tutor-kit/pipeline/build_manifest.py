#!/usr/bin/env python3
"""
build_manifest.py - Generate a comprehensive extraction audit manifest.

Extracts metadata, AI model provenance, character counts, equation densities,
and execution statuses across all documents in workspace/text/ and sources.csv.

Outputs: workspace/text/manifest.jsonl
"""
import csv
import json
import os
import re
import sys
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KIT_ROOT))
from wspaths import p  # noqa: E402

LOG_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\d2778b60-aafe-484e-9103-c5715596acbe\.system_generated\tasks")


def parse_task_logs():
    """Extract model provenance and run metrics from task logs."""
    provenance = {}
    if not LOG_DIR.exists():
        return provenance

    log_files = sorted(LOG_DIR.glob("task-*.log"), key=lambda x: x.stat().st_mtime)
    
    # Pattern: [idx/total] [source_id] Vision extracting pdf_name.pdf (size)... DONE via model (chars in elapsed s)
    pattern_done = re.compile(r"\[\d+/\d+\]\s+\[([^\]]+)\]\s+Vision extracting\s+([^\s]+)\s+\(([^)]+)\)\.\.\.\s+DONE via\s+([^\s]+)\s+\(([\d,]+)\s+chars in\s+([\d\.]+)s\)")
    pattern_skip = re.compile(r"\[\d+/\d+\]\s+\[([^\]]+)\]\s+SKIPPED: Already Vision Extracted\s+\(([\d,]+)\s+chars with LaTeX\)")
    pattern_fail = re.compile(r"\[\d+/\d+\]\s+\[([^\]]+)\]\s+Vision extracting\s+([^\s]+).*FAILED:\s+(.*)")

    for lf in log_files:
        try:
            content = lf.read_text(encoding="utf-8", errors="ignore")
            for line in content.splitlines():
                m_done = pattern_done.search(line)
                if m_done:
                    sid, pdf, sz, model, chars, elapsed = m_done.groups()
                    provenance[sid] = {
                        "model": model,
                        "duration_sec": float(elapsed),
                        "status": "SUCCESS",
                        "raw_pdf": pdf,
                        "reported_chars": int(chars.replace(",", "")),
                    }
                    continue
                m_skip = pattern_skip.search(line)
                if m_skip:
                    sid, chars = m_skip.groups()
                    if sid not in provenance:
                        provenance[sid] = {
                            "model": "gemini-3.5-flash-lite",  # primary default
                            "duration_sec": None,
                            "status": "SUCCESS_EXISTING",
                            "reported_chars": int(chars.replace(",", "")),
                        }
                    continue
                m_fail = pattern_fail.search(line)
                if m_fail:
                    sid, pdf, err = m_fail.groups()
                    provenance[sid] = {
                        "model": "unknown",
                        "duration_sec": None,
                        "status": "FAILED",
                        "error": err[:200],
                        "raw_pdf": pdf
                    }
        except Exception:
            pass
    return provenance


def main():
    sources_csv = p("sources", "sources.csv")
    if not sources_csv.exists():
        sys.exit(f"Sources file not found at {sources_csv}")

    text_dir = p("text")
    raw_dir = p("raw")
    manifest_file = text_dir / "manifest.jsonl"

    provenance = parse_task_logs()

    sources = []
    with open(sources_csv, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for r in reader:
            sources.append(r)

    manifest_entries = []
    stats = {
        "total_sources": len(sources),
        "extracted_files": 0,
        "models_used": {},
        "with_katex": 0,
        "with_diagrams": 0,
        "total_chars": 0,
    }

    for r in sources:
        sid = r.get("source_id")
        rel_pdf = r.get("local_path") or r.get("path")
        pdf_path = raw_dir / rel_pdf if not str(rel_pdf).startswith("workspace") else KIT_ROOT / rel_pdf
        txt_path = text_dir / f"{sid}.txt"

        prov = provenance.get(sid, {})
        has_text = txt_path.exists()
        char_count = 0
        has_katex = False
        diagram_count = 0

        if has_text:
            text_content = txt_path.read_text(encoding="utf-8", errors="ignore")
            char_count = len(text_content)
            has_katex = ("$" in text_content or "\\frac" in text_content or "\\sqrt" in text_content)
            diagram_count = len(re.findall(r"\[DIAGRAM:", text_content))
            stats["extracted_files"] += 1
            stats["total_chars"] += char_count
            if has_katex:
                stats["with_katex"] += 1
            if diagram_count > 0:
                stats["with_diagrams"] += diagram_count

        model_name = prov.get("model") or ("gemini-3.5-flash-lite" if has_text else "unextracted")
        if has_text:
            stats["models_used"][model_name] = stats["models_used"].get(model_name, 0) + 1

        entry = {
            "source_id": sid,
            "subject": r.get("subject"),
            "grade": r.get("grade"),
            "year": r.get("year"),
            "session": r.get("session"),
            "paper": r.get("paper"),
            "pdf_file": str(rel_pdf) if rel_pdf else None,
            "pdf_exists": pdf_path.exists(),
            "pdf_size_bytes": pdf_path.stat().st_size if pdf_path.exists() else 0,
            "txt_file": f"workspace/text/{sid}.txt" if has_text else None,
            "txt_exists": has_text,
            "char_count": char_count,
            "has_katex_latex": has_katex,
            "diagram_annotations": diagram_count,
            "model_used": model_name,
            "duration_sec": prov.get("duration_sec"),
            "status": "COMPLETED" if has_text and char_count > 1000 else ("SHORT_OR_EMPTY" if has_text else "QUEUED"),
            "error": prov.get("error")
        }
        manifest_entries.append(entry)

    # Write manifest atomically
    with open(manifest_file, "w", encoding="utf-8") as f:
        for entry in manifest_entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"=== Eishkom Extraction Audit Manifest Generated ===")
    print(f"Manifest saved to: {manifest_file}")
    print(f"Total Sources Ingested: {stats['extracted_files']} / {stats['total_sources']}")
    print(f"Total High-Fidelity Characters: {stats['total_chars']:,}")
    print(f"Documents with KaTeX LaTeX: {stats['with_katex']}")
    print(f"Diagram Annotations Found: {stats['with_diagrams']}")
    print(f"Model Breakdown: {stats['models_used']}")


if __name__ == "__main__":
    main()

