#!/usr/bin/env python3
"""
check_progress.py - Live progress tracker for Eishkom Stage 1 Vision Extraction.
Run this script anytime to see exact completed counts, characters, and stage breakdown.
"""
import glob
import os
import sys

# Force UTF-8 stdout if supported
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WS = os.path.join(os.path.dirname(__file__), "sa-tutor-kit", "sa-tutor-kit", "workspace", "text")
if not os.path.exists(WS):
    WS = os.path.join(os.path.dirname(__file__), "workspace", "text")

txt_files = [f for f in glob.glob(os.path.join(WS, "*.txt")) if not os.path.basename(f).startswith("_")]

indicators = ["$$", "\\tag{", "[DIAGRAM:", "\\checkmark", "QUESTION", "VRAAG", "AFDELING", "SECTION", "PUNTE:", "MARKS:"]

counts = {}
total_chars = 0
vision_done = 0

for f in txt_files:
    try:
        content = open(f, "r", encoding="utf-8", errors="ignore").read()
        if len(content) > 1000 and sum(1 for ind in indicators if ind in content) >= 2:
            vision_done += 1
            total_chars += len(content)
            parts = os.path.basename(f).split("-")
            subj = parts[1] if len(parts) > 1 else "other"
            counts[subj] = counts.get(subj, 0) + 1
    except Exception:
        pass

total_target = 600
pct = (vision_done / total_target) * 100
bar_len = 30
filled = int(bar_len * (vision_done / total_target))
bar = "=" * filled + "-" * (bar_len - filled)

print("=" * 70)
print("          EISHKOM STAGE 1 -- VISION INGESTION LIVE PROGRESS")
print("=" * 70)
print(f"Overall Progress: [{bar}] {vision_done}/{total_target} ({pct:.1f}%)")
print(f"Total High-Fidelity Characters: {total_chars:,}\n")

print("Stage Breakdown (Vision Verified with KaTeX LaTeX):")
stages = [
    ("Stage 1: Mathematics & Wiskunde", ["mathematics", "wiskunde"], 180),
    ("Stage 2: English (HL & FAL)", ["english_hl", "english_fal"], 120),
    ("Stage 3: Afrikaans (HT & EAT)", ["afrikaans_hl", "afrikaans_fal"], 120),
    ("Stage 4: Physical Sciences & Fisiese", ["physical_sciences", "fisiese_wetenskappe"], 180),
]

for stage_name, subjs, target in stages:
    done = sum(counts.get(s, 0) for s in subjs)
    sub_pct = (done / target) * 100 if target else 0
    if done >= target:
        status_icon = "[DONE]"
    elif done > 0:
        status_icon = "[RUNNING]"
    else:
        status_icon = "[QUEUED]"
    print(f"  * {stage_name:<40} {done:>3}/{target} ({sub_pct:>5.1f}%)  {status_icon}")
    for s in subjs:
        print(f"      - {s:<25}: {counts.get(s, 0)} files")

print("=" * 70)
