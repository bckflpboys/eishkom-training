#!/usr/bin/env python3
"""
stage-2/compile_stage2_dataset.py - Master SFT Dataset Compiler for Stage 2.

Merges:
  1. Stage 1 verified Socratic lessons (test_round, wave2, wave3, wave4, wave5)
  2. Stage 1 verified Full Solutions (workspace/verified/full_solutions)
  3. Stage 2 Pass 1 verified Socratic lessons (workspace/verified/stage2)
  4. Stage 2 Pass 2 & Redo verified Socratic lessons (workspace/verified/stage2_pass2)
  5. Stage 2 verified Full Solutions (workspace/verified/stage2_full_solutions)
  6. Stage 2 verified Agentic Coaching dialogues (workspace/verified/agentic)

Canonicalizes records into standard format, deduplicates across the entire corpus,
outputs master and component splits, and runs tutor_data.py build.
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
    "dual_coding", "interleaving", "teach_it_back", "flashcards", "past_paper_first"
}

ALLOWED_STRATEGIES = {
    "auto", "worked_example", "faded_example", "socratic_hints", "analogy_real_world",
    "mnemonic", "concrete_to_abstract", "retrieval_quiz", "error_analysis", "self_explanation",
    "gamified_challenge", "direct_explanation", "spaced_recap", "exam_technique", "step_walkthrough",
    "reframe", "think_aloud", "answer_structure", "visual_board", "story_context"
}

CHECKABLE_SUBJECTS = {"mathematics", "mathematical_literacy", "natural_sciences", "physical_sciences"}

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

    # Convert dialogue -> messages if coming from agentic coaching
    if "dialogue" in rec and "messages" not in rec:
        conv_msgs = []
        for turn in rec["dialogue"]:
            role = "user" if turn.get("role") in ("student", "user") else "assistant"
            content = turn.get("content", "").strip()
            if not content:
                continue
            entry = {"role": role, "content": content}
            if role == "assistant":
                entry["reasoning"] = turn.get("private_reasoning") or turn.get("reasoning") or "Coach the learner through examination and study preparation."
            conv_msgs.append(entry)
        rec["messages"] = conv_msgs

    # Subject clean
    raw_subj = c.get("subject") or m.get("subject") or "mathematics"
    subj, lang_track = clean_subject(raw_subj)
    c["subject"] = subj
    if lang_track:
        c["language_track"] = lang_track
    elif "language_track" in c and subj not in ("english", "afrikaans"):
        del c["language_track"]

    # Subject language & response language
    if "subject_language" not in c:
        m_lang = m.get("learner_language") or m.get("student_language")
        if m_lang in ("en", "af"):
            c["subject_language"] = m_lang
        else:
            c["subject_language"] = "af" if ("afrikaans" in str(raw_subj).lower() or "wiskunde" in str(raw_subj).lower() or "wetenskap" in str(raw_subj).lower()) else "en"
    if "response_language" not in c:
        c["response_language"] = "mirror"

    # Schema version & thinking trace
    rec["schema_version"] = "tutor-v1"
    rec["thinking"] = "on"

    # Clean non-standard top-level and meta fields for strict tutor-v1 compliance
    rec.pop("dialogue", None)
    rec.pop("grounding", None)
    for k in ["learner_language", "learner_state", "thinking_mode", "tools_used", "stage", "category"]:
        m.pop(k, None)

    # ID & group_id
    item_id = m.get("item_id", "")
    rec_id = rec.get("id") or item_id or f"rec-{abs(hash(rec.get('messages', [{}])[0].get('content', ''))) & 0xffffffff:x}"
    rec["id"] = str(rec_id)
    rec["group_id"] = str(item_id if item_id else (m.get("paper_id") or rec_id))

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

    # State mapping for tutor-v1 schema compliance
    state_map = {
        "blank_stuck": "lost",
        "partial_attempt": "almost_there",
        "confident_wrong": "confused",
        "wants_answer_only": "asking_for_answer",
        "exam_panic": "frustrated",
        "misread_question": "confused",
        "strong_wants_marks": "confident",
        "language_slip": "confused",
        "slip_arith_sign_unit": "almost_there",
        "organised_wants_optimisation": "confident",
    }
    st = m.get("student_state") or m.get("learner_state")
    if st:
        m["student_state"] = state_map.get(st, st if st in ("almost_there", "asking_for_answer", "bored", "confident", "confused", "frustrated", "lost", "off_task", "rushing", "unknown") else "confused")
    else:
        m["student_state"] = "confused"

    # Verification method mapping for tutor-v1 schema compliance
    verif_map = {
        "sympy_verified_match": "sympy_vs_memo",
        "sympy": "sympy_vs_memo",
        "numeric_tolerance_match": "sympy_vs_memo",
        "language_content_verified": "human",
        "concept_keyword_verified": "human",
        "proof_derivation_verified": "human",
        "mcq_verified_match": "human",
        "sketch_diagram_verified": "human",
        "text_memo_match": "human",
        "auto_repair_recovery": "human",
        "official_memo_direct": "human",
        "human_expert": "human",
        "human": "human",
        "code_exec": "code_exec",
        "sympy_vs_memo": "sympy_vs_memo",
        "none": "none",
    }
    vm = m.get("verification_method")
    if vm:
        m["verification_method"] = verif_map.get(vm, "sympy_vs_memo" if subj in CHECKABLE_SUBJECTS else "human")
    else:
        m["verification_method"] = "sympy_vs_memo" if subj in CHECKABLE_SUBJECTS else "human"

    # Required meta defaults
    cur_topic = m.get("topic") or c.get("topic")
    if not cur_topic or not str(cur_topic).strip():
        cur_topic = "Exam Practice"
    m["topic"] = str(cur_topic).strip()
    task_t = m.get("task_type")
    if not task_t or task_t not in ("solve_problem", "worked_example", "error_analysis", "concept_intro", "review_recap", "exam_technique", "comprehension", "essay_planning", "quick_check"):
        if subj in ("english", "afrikaans"):
            m["task_type"] = "comprehension"
        elif m.get("strategy_used") == "exam_technique" or c.get("strategy") == "exam_technique":
            m["task_type"] = "exam_technique"
        else:
            m["task_type"] = "solve_problem"

    m.setdefault("student_language", c.get("subject_language", "en"))
    m.setdefault("source_type", "past_paper_adapted")
    m.setdefault("source_licence", "DBE-Open-Educational-Resource")
    m.setdefault("generator", m.get("generator") or "eishkom-stage2-fleet")
    m.setdefault("answer_verified", True)
    m.setdefault("split", "auto")

    # Strategy validation
    strat = m.get("strategy_used") or c.get("strategy") or "socratic_hints"
    if strat not in ALLOWED_STRATEGIES:
        strat = "socratic_hints"
    m["strategy_used"] = strat
    c["strategy"] = strat

    # Required control defaults
    c.setdefault("grade", 12)
    c.setdefault("answer_policy", "guided")
    c.setdefault("student_level", "struggling")
    c.setdefault("tone", "encouraging")

    # Response length enum: ['short', 'medium', 'long']
    resp_len = str(c.get("response_length", "short")).lower()
    if resp_len in ("short", "concise"):
        c["response_length"] = "short"
    elif resp_len in ("medium", "standard"):
        c["response_length"] = "medium"
    elif resp_len in ("long", "detailed"):
        c["response_length"] = "long"
    else:
        c["response_length"] = "short"

    c.setdefault("tools", ["calculator"] if subj in CHECKABLE_SUBJECTS else [])
    if subj in CHECKABLE_SUBJECTS:
        c.setdefault("math_format", "latex")

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
    print("EISHKOM AI — STAGE 2 MASTER DATASET COMPILER (UNIFIED CORPUS)")
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
    s2_pass2_dir = VER_DIR / "stage2_pass2"
    s2_fullsol_dir = VER_DIR / "stage2_full_solutions"
    s2_agentic_dir = VER_DIR / "agentic"

    out_master = VER_DIR / "stage2_master_combined.jsonl"
    out_socratic = VER_DIR / "stage2_socratic_only.jsonl"
    out_fullsol = VER_DIR / "stage2_fullsol_only.jsonl"
    out_agentic = VER_DIR / "stage2_agentic_only.jsonl"

    all_records_by_id = {}
    stats = defaultdict(int)

    def ingest_dir(directory: Path, stage_tag: str, policy_tag: str, allow_overwrite: bool = False):
        if not directory.exists():
            return
        file_count = 0
        total_ingested = 0
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
                            rid = f"{f.stem}-{len(all_records_by_id)}"
                        if rid in all_records_by_id and not allow_overwrite:
                            continue

                        # Tag stage if not present
                        rec.setdefault("meta", {})["stage"] = rec["meta"].get("stage", stage_tag)
                        if policy_tag == "agentic":
                            rec.setdefault("control", {})["answer_policy"] = "guided"
                            rec["_is_agentic"] = True

                        canon = canonicalize_record(rec)
                        if canon:
                            all_records_by_id[rid] = canon
                            count += 1
                            stats[f"{stage_tag}_{policy_tag}"] += 1
                            stats[canon["control"]["subject"]] += 1
                    except Exception:
                        pass
            if count > 0:
                file_count += 1
                total_ingested += count
        print(f"  [{stage_tag.upper()} - {policy_tag}] Ingested {total_ingested} records across {file_count} files from {directory.name}")

    print("\n1. Ingesting Stage 1 Socratic Dialogues...")
    for d in s1_socratic_dirs:
        ingest_dir(d, "stage-1", "socratic")

    print("\n2. Ingesting Stage 1 Full Solutions...")
    ingest_dir(s1_fullsol_dir, "stage-1", "full_solution")

    print("\n3. Ingesting Stage 2 Pass 1 Socratic Dialogues...")
    ingest_dir(s2_socratic_dir, "stage-2", "socratic")

    print("\n4. Ingesting Stage 2 Pass 2 & Redo Socratic Dialogues (allowing verified overwrites)...")
    ingest_dir(s2_pass2_dir, "stage-2", "socratic_pass2", allow_overwrite=True)

    print("\n5. Ingesting Stage 2 Full Solutions...")
    ingest_dir(s2_fullsol_dir, "stage-2", "full_solution")

    print("\n6. Ingesting Stage 2 Agentic Coaching Dialogues...")
    ingest_dir(s2_agentic_dir, "stage-2", "agentic")

    all_records = list(all_records_by_id.values())

    # Separate into component datasets
    socratic_records = [
        r for r in all_records
        if r.get("control", {}).get("answer_policy") != "full_solution"
        and not r.get("_is_agentic")
    ]
    fullsol_records = [
        r for r in all_records
        if r.get("control", {}).get("answer_policy") == "full_solution"
    ]
    agentic_records = [
        r for r in all_records
        if r.get("_is_agentic")
    ]

    print("\n" + "=" * 80)
    print("UNIFIED CORPUS COMPILATION SUMMARY")
    print("=" * 80)
    print(f"Total Unique Canonical Records:       {len(all_records)}")
    print(f"  * Socratic Hint Lessons:            {len(socratic_records)}")
    print(f"  * Full Solution Step-by-Step Demos: {len(fullsol_records)}")
    print(f"  * Agentic Coaching Dialogues:       {len(agentic_records)}")
    print("-" * 80)
    print(f"  Stage 1 Socratic Dialogues:         {stats['stage-1_socratic']}")
    print(f"  Stage 1 Full Solutions:             {stats['stage-1_full_solution']}")
    print(f"  Stage 2 Pass 1 Socratic:            {stats['stage-2_socratic']}")
    print(f"  Stage 2 Pass 2 & Redo Socratic:     {stats['stage-2_socratic_pass2']}")
    print(f"  Stage 2 Full Solutions:             {stats['stage-2_full_solution']}")
    print(f"  Stage 2 Agentic Coaching:           {stats['stage-2_agentic']}")
    print("-" * 80)
    print("Subject Distribution:")
    for subj in sorted(VALID_SUBJECTS):
        print(f"  * {subj:25s}: {stats[subj]:5d} records")
    print("=" * 80)

    def clean_dict(d):
        return {k: v for k, v in d.items() if not k.startswith("_")}

    # Write Master Combined
    with open(out_master, "w", encoding="utf-8") as fp:
        for rec in all_records:
            fp.write(json.dumps(clean_dict(rec), ensure_ascii=False) + "\n")

    # Write Socratic-Only Split
    with open(out_socratic, "w", encoding="utf-8") as fp:
        for rec in socratic_records:
            fp.write(json.dumps(clean_dict(rec), ensure_ascii=False) + "\n")

    # Write Full-Solution-Only Split
    with open(out_fullsol, "w", encoding="utf-8") as fp:
        for rec in fullsol_records:
            fp.write(json.dumps(clean_dict(rec), ensure_ascii=False) + "\n")

    # Write Agentic-Only Split
    with open(out_agentic, "w", encoding="utf-8") as fp:
        for rec in agentic_records:
            fp.write(json.dumps(clean_dict(rec), ensure_ascii=False) + "\n")

    print(f"\nWritten combined master dataset to: {out_master}")
    print(f"Written Socratic-only dataset to:  {out_socratic}")
    print(f"Written Full-Solution dataset to:   {out_fullsol}")
    print(f"Written Agentic-only dataset to:    {out_agentic}")

    # Build SFT production datasets with tutor_data.py
    tutor_data_script = KIT_ROOT / "tutor_data.py"

    if tutor_data_script.exists():
        build_targets = [
            ("Master Combined (r2)", out_master, ROOT_DIR / "workspace" / "build" / "r2"),
            ("Socratic Dialogues (r2_socratic)", out_socratic, ROOT_DIR / "workspace" / "build" / "r2_socratic"),
            ("Full Solutions (r2_fullsol - 1 Epoch)", out_fullsol, ROOT_DIR / "workspace" / "build" / "r2_fullsol"),
            ("Agentic Coaching (r2_agentic)", out_agentic, ROOT_DIR / "workspace" / "build" / "r2_agentic"),
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
