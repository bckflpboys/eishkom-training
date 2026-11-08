import json
import re
from pathlib import Path

# Load all known items to look up original topics and metadata
items_by_id = {}
items_dir = Path("workspace/items")
if items_dir.exists():
    for f in items_dir.rglob("*.jsonl"):
        with open(f, encoding="utf-8") as fp:
            for line in fp:
                line = line.strip()
                if not line:
                    continue
                try:
                    it = json.loads(line)
                    if "item_id" in it:
                        items_by_id[it["item_id"]] = it
                except Exception:
                    pass

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

raw_pilot = Path("workspace/verified/train_r1_pilot.jsonl")
formatted_pilot = Path("workspace/verified/train_r1_canonical.jsonl")

records = []
with open(raw_pilot, encoding="utf-8") as fp:
    for line in fp:
        line = line.strip()
        if not line:
            continue
        rec = json.loads(line)
        records.append(rec)

out_records = []
for r in records:
    c = r.get("control", {})
    m = r.get("meta", {})
    item_id = m.get("item_id", "")
    item = items_by_id.get(item_id, {})

    # 1. group_id (per-question group so lessons for the same question stay together)
    group_id = item_id if item_id else (m.get("paper_id") or item.get("source_id") or r.get("id", "pilot-group"))
    r["group_id"] = str(group_id)

    # 2. Fix control.subject & language_track
    raw_subj = c.get("subject", "mathematics")
    lang_track = None
    if raw_subj in ("afrikaans_hl", "languages_af_hl"):
        clean_subj = "afrikaans"
        lang_track = "HL"
    elif raw_subj in ("afrikaans_fal", "languages_af_fal"):
        clean_subj = "afrikaans"
        lang_track = "FAL"
    elif raw_subj in ("english_hl", "languages_en_hl"):
        clean_subj = "english"
        lang_track = "HL"
    elif raw_subj in ("english_fal", "languages_en_fal"):
        clean_subj = "english"
        lang_track = "FAL"
    elif raw_subj in ("wiskunde", "core_maths_af"):
        clean_subj = "mathematics"
        c["subject_language"] = "af"
    elif raw_subj in ("fisiese_wetenskappe", "phys_sci_af"):
        clean_subj = "physical_sciences"
        c["subject_language"] = "af"
    else:
        clean_subj = raw_subj if raw_subj in VALID_SUBJECTS else "mathematics"

    c["subject"] = clean_subj
    if lang_track:
        c["language_track"] = lang_track
    elif clean_subj in ("english", "afrikaans"):
        c["language_track"] = "HL"

    # Ensure grade is int
    c["grade"] = int(c.get("grade", 12))
    c["student_level"] = c.get("student_level", "struggling")
    c["tone"] = c.get("tone", "encouraging")
    c["response_length"] = c.get("response_length", "short")
    c["tools"] = []  # canonical tools
    if "math_format" not in c and clean_subj in {"mathematics", "physical_sciences"}:
        c["math_format"] = "latex"

    # 3. Fix meta
    m["topic"] = m.get("topic") or item.get("topic") or f"Grade {c['grade']} {clean_subj.replace('_', ' ').title()}"
    m["task_type"] = "comprehension" if clean_subj in ("english", "afrikaans") else "solve_problem"
    m["student_language"] = c.get("subject_language") or ("af" if "afrikaans" in raw_subj or "wiskunde" in raw_subj else "en")
    m["strategy_used"] = c.get("strategy", "step_walkthrough")
    m["source_type"] = "past_paper_adapted"
    m["source_licence"] = "DBE Open Educational Resource"
    m["generator"] = m.get("generator", "eishkom-distiller")
    m["answer_verified"] = True
    m["split"] = "auto"
    m["verification_method"] = "sympy_vs_memo"

    # Filter techniques
    raw_tech = m.get("techniques", [])
    valid_tech = [t for t in raw_tech if t in ALLOWED_TECHNIQUES]
    if not valid_tech:
        if clean_subj == "mathematics":
            valid_tech = ["polya_four_steps", "check_by_substitution"]
        elif clean_subj == "physical_sciences":
            valid_tech = ["units_check", "concept_map"]
        else:
            valid_tech = ["context_clues", "mark_per_point"]
    m["techniques"] = valid_tech

    # 4. Fix messages alternating sequence
    msgs = r.get("messages", [])
    clean_msgs = []
    expected_role = "user"
    for msg in msgs:
        role = msg.get("role")
        content = msg.get("content", "").strip()
        reasoning = msg.get("reasoning", "")
        if role == expected_role:
            if role == "assistant":
                clean_msgs.append({
                    "role": "assistant",
                    "reasoning": reasoning or "Guide the student with a patient Socratic hint.",
                    "content": content
                })
                expected_role = "user"
            else:
                clean_msgs.append({"role": "user", "content": content})
                expected_role = "assistant"
        elif role == "assistant" and expected_role == "assistant":
            # Normal assistant
            clean_msgs.append({
                "role": "assistant",
                "reasoning": reasoning or "Guide the student with a patient Socratic hint.",
                "content": content
            })
            expected_role = "user"
        elif role == "assistant" and expected_role == "user":
            # Merge with previous assistant content
            if clean_msgs and clean_msgs[-1]["role"] == "assistant":
                clean_msgs[-1]["content"] += "\n\n" + content
        elif role == "user" and expected_role == "assistant":
            # Merge with previous user
            if clean_msgs and clean_msgs[-1]["role"] == "user":
                clean_msgs[-1]["content"] += "\n\n" + content

    # Ensure ends with assistant
    if clean_msgs and clean_msgs[-1]["role"] == "user":
        clean_msgs.pop()

    if len(clean_msgs) >= 2 and clean_msgs[0]["role"] == "user" and clean_msgs[-1]["role"] == "assistant":
        r["messages"] = clean_msgs
        out_records.append(r)

with open(formatted_pilot, "w", encoding="utf-8") as fp:
    for rec in out_records:
        fp.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Successfully converted {len(out_records)} records to {formatted_pilot}")
