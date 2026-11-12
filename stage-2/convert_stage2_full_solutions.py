#!/usr/bin/env python3
"""
stage-2/convert_stage2_full_solutions.py - Convert raw exam items for Stage 2 papers
into structured "full_solution" canonical SFT records.

Outputs directly to workspace/verified/stage2_full_solutions/<paper_id>.jsonl
(leaving Stage 1 full solutions in workspace/verified/full_solutions/ untouched).
"""

import json
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
ITEMS_DIR = ROOT_DIR / "workspace" / "items"
OUT_DIR = ROOT_DIR / "workspace" / "verified" / "stage2_full_solutions"
OUT_DIR.mkdir(parents=True, exist_ok=True)

VALID_SUBJECTS = {
    "mathematics", "mathematical_literacy", "natural_sciences",
    "physical_sciences", "life_sciences", "english", "afrikaans"
}

def clean_subject(raw_subj):
    lang_track = None
    if raw_subj in ("afrikaans_hl", "languages_af_hl"):
        clean = "afrikaans"
        lang_track = "HL"
    elif raw_subj in ("afrikaans_fal", "languages_af_fal"):
        clean = "afrikaans"
        lang_track = "FAL"
    elif raw_subj in ("english_hl", "languages_en_hl"):
        clean = "english"
        lang_track = "HL"
    elif raw_subj in ("english_fal", "languages_en_fal"):
        clean = "english"
        lang_track = "FAL"
    elif raw_subj in ("wiskunde", "core_maths_af"):
        clean = "mathematics"
    elif raw_subj in ("fisiese_wetenskappe", "phys_sci_af"):
        clean = "physical_sciences"
    else:
        clean = raw_subj if raw_subj in VALID_SUBJECTS else "mathematics"
    return clean, lang_track

def find_item_file(paper_id: str) -> Path:
    flat = ITEMS_DIR / f"{paper_id}.jsonl"
    if flat.exists():
        return flat
    for s_dir in ITEMS_DIR.iterdir():
        if s_dir.is_dir():
            nested = s_dir / f"{paper_id}.jsonl"
            if nested.exists():
                return nested
    return flat

def process_paper_s2(paper_id: str) -> int:
    item_file = find_item_file(paper_id)
    if not item_file.exists():
        return 0

    out_file = OUT_DIR / f"{paper_id}.jsonl"
    records = []

    with open(item_file, encoding="utf-8") as fp:
        for line in fp:
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
            except Exception:
                continue
            item_id = item.get("item_id", "")
            raw_subj = item.get("subject", "mathematics")
            clean_subj, lang_track = clean_subject(raw_subj)
            grade = int(item.get("grade", 12))
            is_af = "afrikaans" in raw_subj or "wiskunde" in raw_subj or "wetenskap" in raw_subj
            lang = "af" if is_af else "en"
            topic = item.get("topic") or f"Grade {grade} {clean_subj.title()}"
            question = item.get("question", "").strip()
            memo = item.get("memo") or item.get("solution") or item.get("answer", "").strip()
            passage = f"Context / Passage:\n{item.get('passage')}\n\n" if item.get("passage") else ""
            marks = item.get("marks", 1)

            if not question or not memo:
                continue

            # Student prompt asking for full worked solution
            if is_af:
                user_msg = f"{passage}Wys my asseblief die volledige stap-vir-stap uitgewerkte memorandum-oplossing vir hierdie vraag ({marks} punte):\n{question}"
                reasoning = (
                    f"Die leerder vra vir die volledige uitgewerkte oplossing vir '{topic}'. "
                    f"Ek gee 'n duidelike, gestruktureerde oplossing wat aan die DBE-nasienriglyne voldoen, "
                    f"met formules, substitusies en motiverings vir elke stap."
                )
                assistant_msg = (
                    f"Hier is die volledige uitgewerkte oplossing volgens die KABV-nasienriglyne ({marks} punte):\n\n"
                    f"{memo}\n\n"
                    f"**Belangrike eksamenwenk:** Maak seker jy skryf die formule eerste neer, "
                    f"vervang die waardes akkuraat, en gee jou finale antwoord met die regte eenhede of afronding."
                )
            else:
                user_msg = f"{passage}Please show me the complete step-by-step worked memorandum solution for this question ({marks} marks):\n{question}"
                reasoning = (
                    f"The learner requested the complete worked solution for '{topic}'. "
                    f"I will provide a structured, CAPS-aligned breakdown matching the official DBE marking memorandum, "
                    f"showing formulas, substitutions, and reasons for each step."
                )
                assistant_msg = (
                    f"Here is the complete worked solution following official CAPS marking guidelines ({marks} marks):\n\n"
                    f"{memo}\n\n"
                    f"**Exam Technique Note:** Always state the formula first, substitute carefully, "
                    f"and verify that your final answer includes the appropriate units and rounding."
                )

            ctrl = {
                "subject": clean_subj,
                "grade": grade,
                "subject_language": lang,
                "response_language": lang,
                "strategy": "step_walkthrough",
                "answer_policy": "full_solution",
                "student_level": "on_track",
                "tone": "calm_neutral",
                "response_length": "medium",
                "tools": [],
                "math_format": "latex"
            }
            if lang_track:
                ctrl["language_track"] = lang_track
            elif clean_subj in ("english", "afrikaans"):
                ctrl["language_track"] = "HL"

            rec = {
                "schema_version": "tutor-v2",
                "id": f"s2-fullsol-{item_id}",
                "group_id": str(item_id),
                "control": ctrl,
                "thinking": "on",
                "messages": [
                    {"role": "user", "content": user_msg},
                    {"role": "assistant", "reasoning": reasoning, "content": assistant_msg}
                ],
                "meta": {
                    "topic": topic,
                    "task_type": "solve_problem" if clean_subj not in ("english", "afrikaans") else "comprehension",
                    "student_language": lang,
                    "strategy_used": "step_walkthrough",
                    "source_type": "past_paper_adapted",
                    "source_licence": "DBE Open Educational Resource",
                    "generator": "dbe-official-memorandum",
                    "answer_verified": True,
                    "verification_method": "official_memo_direct",
                    "split": "auto",
                    "final_answer": item.get("final_answer") or memo[:100],
                    "paper_id": paper_id,
                    "item_id": item_id,
                    "stage": "stage-2",
                    "techniques": ["given_formula_substitute_answer", "mark_per_point"]
                }
            }
            records.append(rec)

        with open(out_file, "w", encoding="utf-8") as out_fp:
            for r in records:
                out_fp.write(json.dumps(r, ensure_ascii=False) + "\n")

    return len(records)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        pid = sys.argv[1]
        cnt = process_paper_s2(pid)
        print(f"Paper {pid}: Generated {cnt} Stage 2 full solution records")
    else:
        print("Usage: python convert_stage2_full_solutions.py <paper_id>")

