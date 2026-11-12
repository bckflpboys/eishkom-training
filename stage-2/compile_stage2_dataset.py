#!/usr/bin/env python3
"""
stage-2/compile_stage2_dataset.py - Master SFT Dataset Compiler for Stage 2.

Merges:
  1. Stage 1 verified Socratic lessons (test_round, wave2, wave3, wave4, wave5)
  2. Stage 1 verified Full Solutions (workspace/verified/full_solutions)
  3. Stage 2 verified Socratic lessons (workspace/verified/stage2)
  4. Stage 2 verified Full Solutions (workspace/verified/stage2_full_solutions)

Canonicalizes records into standard format, deduplicates across the entire corpus,
outputs to:
  workspace/verified/stage2_master_combined.jsonl
and invokes:
  tutor_data.py build workspace/verified/stage2_master_combined.jsonl --out workspace/build/r2 --val 0.15
"""

import json
import sys
import subprocess
from pathlib import Path
from collections import defaultdict

ROOT_DIR = Path(__file__).resolve().parent.parent
KIT_ROOT = ROOT_DIR / "sa-tutor-kit" / "sa-tutor-kit"
VER_DIR = ROOT_DIR / "workspace" / "verified"

VALID_SUBJECTS = {
    "mathematics", "mathematical_literacy", "natural_sciences",
    "physical_sciences", "life_sciences", "english", "afrikaans"
}

ALLOWED_TECHNIQUES = {
    "bar_model", "number_line", "area_model", "balance_scale", "cpa", "bodmas", "factor_tree", "soh_cah_toa",
    "cubes", "polya_four_steps", "work_backwards", "estimate_first", "check_by_substitution", "units_check",
    "table_of_values", "draw_a_diagram", "try_simple_numbers", "given_formula_substitute_answer",
    "predict_observe_explain", "particle_diagram", "energy_chain", "concept_map", "units_conversion",
    "sq3r", "qar", "peel", "teel", "annotate_text", "five_ws", "skim_and_scan", "context_clues",
    "paraphrase_then_answer", "mark_per_point", "command_word_decode", "plan_write_check",
    "acronym", "rhyme", "story_chain", "memory_palace", "chunking", "retrieval_practice", "spaced_review",
    "dual_coding", "interleaving", "teach_it_back", "flashcards"
}

def clean_subject(raw_subj):
    raw = str(raw_subj).lower().strip()
    lang_track = None
    if raw in ("afrikaans_hl", "languages_af_hl"):
        subject = "afrikaans"
        lang_track = "HL"
    elif raw in ("afrikaans_fal", "languages_af_fal"):
        subject = "afrikaans"
        lang_track = "FAL"
    elif raw in ("english_hl", "languages_en_hl"):
        subject = "english"
        lang_track = "HL"
    elif raw in ("english_fal", "languages_en_fal"):
        subject = "english"
        lang_track = "FAL"
    elif raw in ("fisiese_wetenskappe", "phys_sci_af", "physical_science"):
        subject = "physical_sciences"
    elif raw in ("wiskunde", "core_maths_af", "maths"):
        subject = "mathematics"
    elif raw in VALID_SUBJECTS:
        subject = raw
    else:
        subject = "mathematics"
    return subject, lang_track

def canonicalize_record(rec: dict) -> dict:
    c = rec.setdefault("control", {})
    m = rec.setdefault("meta", {})
    item_id = m.get("item_id", "")

    # group_id
    group_id = item_id if item_id else (m.get("paper_id") or rec.get("id", "socratic-group"))
    rec["group_id"] = str(group_id)

    # Subject clean
    raw_subj = c.get("subject", "mathematics")
    subj, lang_track = clean_subject(raw_subj)
    c["subject"] = subj
    if lang_track:
        c["language_track"] = lang_track
    elif "language_track" in c and subj not in ("english", "afrikaans"):
        del c["language_track"]

    if "subject_language" not in c:
        c["subject_language"] = "af" if ("afrikaans" in str(raw_subj).lower() or "wiskunde" in str(raw_subj).lower() or "wetenskap" in str(raw_subj).lower()) else "en"
    if "response_language" not in c:
        c["response_language"] = "mirror"

    # Meta techniques validation
    techniques = m.get("techniques", [])
    valid_techs = [t for t in techniques if t in ALLOWED_TECHNIQUES]
    if not valid_techs:
        if subj == "mathematics":
            valid_techs = ["polya_four_steps", "check_by_substitution"]
        elif subj in ("physical_sciences", "natural_sciences"):
            valid_techs = ["units_check", "concept_map"]
        else:
            valid_techs = ["context_clues", "mark_per_point"]
    m["techniques"] = valid_techs

    # Clean message alternation
    msgs = rec.get("messages", [])
    clean_msgs = []
    expected_role = "user"
    for msg in msgs:
        role = msg.get("role")
        content = msg.get("content", "").strip()
        reasoning = msg.get("reasoning", "")
        if not content:
            continue
        if role == "user" and expected_role == "user":
            clean_msgs.append({"role": "user", "content": content})
            expected_role = "assistant"
        elif role == "user" and expected_role == "assistant":
            if clean_msgs and clean_msgs[-1]["role"] == "user":
                clean_msgs[-1]["content"] += "\n\n" + content
            else:
                clean_msgs.append({"role": "user", "content": content})
                expected_role = "assistant"
        elif role == "assistant" and expected_role == "assistant":
            clean_msgs.append({
                "role": "assistant",
                "reasoning": reasoning or "Guide the student with patient Socratic guidance.",
                "content": content
            })
            expected_role = "user"
        elif role == "assistant" and expected_role == "user":
            if clean_msgs and clean_msgs[-1]["role"] == "assistant":
                clean_msgs[-1]["content"] += "\n\n" + content

    if clean_msgs and clean_msgs[-1]["role"] == "user":
        clean_msgs.pop()

    if len(clean_msgs) >= 2 and clean_msgs[0]["role"] == "user" and clean_msgs[-1]["role"] == "assistant":
        rec["messages"] = clean_msgs
        return rec
    return None

def compile_corpus():
    print("=" * 80)
    print("EISHKOM AI — STAGE 2 MASTER DATASET COMPILER")
    print("=" * 80)

    # Directory sources
    s1_socratic_dirs = [
        VER_DIR / "test_round",
        VER_DIR / "wave2",
        VER_DIR / "wave3",
        VER_DIR / "wave4",
        VER_DIR / "wave5",
    ]
    s1_fullsol_dir = VER_DIR / "full_solutions"
    s2_socratic_dir = VER_DIR / "stage2"
    s2_fullsol_dir = VER_DIR / "stage2_full_solutions"

    out_master = VER_DIR / "stage2_master_combined.jsonl"
    out_canonical_socratic = VER_DIR / "stage2_socratic_canonical.jsonl"

    all_records = []
    seen_ids = set()
    stats = defaultdict(int)

    def ingest_dir(directory: Path, stage_tag: str, policy_tag: str):
        if not directory.exists():
            return
        for f in sorted(directory.glob("*.jsonl")):
            count = 0
            with open(f, encoding="utf-8") as fp:
                for line in fp:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        rec = json.loads(line)
                        rid = rec.get("id") or rec.get("meta", {}).get("item_id")
                        if not rid:
                            continue
                        if rid in seen_ids:
                            continue
                        seen_ids.add(rid)

                        # Tag stage if not present
                        rec.setdefault("meta", {})["stage"] = rec["meta"].get("stage", stage_tag)

                        canon = canonicalize_record(rec)
                        if canon:
                            all_records.append(canon)
                            count += 1
                            stats[f"{stage_tag}_{policy_tag}"] += 1
                            stats[canon["control"]["subject"]] += 1
                    except Exception:
                        pass
            if count > 0:
                print(f"  [{stage_tag.upper()} - {policy_tag}] {f.stem}: {count} records ingested")

    print("\n1. Ingesting Stage 1 Socratic Dialogues...")
    for d in s1_socratic_dirs:
        ingest_dir(d, "stage-1", "socratic")

    print("\n2. Ingesting Stage 1 Full Solutions...")
    ingest_dir(s1_fullsol_dir, "stage-1", "full_solution")

    print("\n3. Ingesting Stage 2 Socratic Dialogues...")
    ingest_dir(s2_socratic_dir, "stage-2", "socratic")

    print("\n4. Ingesting Stage 2 Full Solutions...")
    ingest_dir(s2_fullsol_dir, "stage-2", "full_solution")

    # Separate Socratic vs Full Solutions
    socratic_records = [r for r in all_records if r.get("control", {}).get("answer_policy") != "full_solution"]
    fullsol_records = [r for r in all_records if r.get("control", {}).get("answer_policy") == "full_solution"]

    out_socratic = VER_DIR / "stage2_socratic_only.jsonl"
    out_fullsol = VER_DIR / "stage2_fullsol_only.jsonl"

    print("\n" + "-" * 80)
    print(f"Total Unique Canonical Records: {len(all_records)}")
    print(f"  Socratic Hint Lessons (Multi-Turn): {len(socratic_records)}")
    print(f"  Full Solution Demos (1-Turn Memo):  {len(fullsol_records)}")
    print(f"  Stage 1 Socratic:      {stats['stage-1_socratic']}")
    print(f"  Stage 1 Full Solutions:{stats['stage-1_full_solution']}")
    print(f"  Stage 2 Socratic:      {stats['stage-2_socratic']}")
    print(f"  Stage 2 Full Solutions:{stats['stage-2_full_solution']}")

    # Write Master Combined
    with open(out_master, "w", encoding="utf-8") as fp:
        for rec in all_records:
            fp.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # Write Socratic-Only Split
    with open(out_socratic, "w", encoding="utf-8") as fp:
        for rec in socratic_records:
            fp.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # Write Full-Solution-Only Split (for strict 1-epoch training)
    with open(out_fullsol, "w", encoding="utf-8") as fp:
        for rec in fullsol_records:
            fp.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"\nWritten combined master dataset to: {out_master}")
    print(f"Written Socratic-only dataset to:  {out_socratic}")
    print(f"Written Full-Solution dataset to:   {out_fullsol}")

    # Build SFT production datasets with tutor_data.py
    tutor_data_script = KIT_ROOT / "tutor_data.py"

    if tutor_data_script.exists():
        build_targets = [
            ("Master Combined (r2)", out_master, ROOT_DIR / "workspace" / "build" / "r2"),
            ("Socratic Dialogues (r2_socratic)", out_socratic, ROOT_DIR / "workspace" / "build" / "r2_socratic"),
            ("Full Solutions (r2_fullsol - 1 Epoch)", out_fullsol, ROOT_DIR / "workspace" / "build" / "r2_fullsol"),
        ]
        for label, src_file, out_dir in build_targets:
            print(f"\nExecuting tutor_data.py build for {label} -> {out_dir}...")
            cmd = [
                sys.executable,
                str(tutor_data_script),
                "build",
                str(src_file),
                "--out",
                str(out_dir),
                "--val",
                "0.15",
                "--skip-invalid"
            ]
            res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
            print(res.stdout)
            if res.stderr:
                print("STDERR:", res.stderr)
        print("All builds complete!")
    else:
        print(f"Warning: tutor_data.py not found at {tutor_data_script}")

    print("=" * 80)
    return len(all_records)

if __name__ == "__main__":
    compile_corpus()

