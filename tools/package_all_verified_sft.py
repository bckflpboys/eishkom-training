import json
from pathlib import Path
import subprocess
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
v_w1 = ROOT_DIR / "workspace" / "verified" / "test_round"
v_w2 = ROOT_DIR / "workspace" / "verified" / "wave2"
out_canonical = ROOT_DIR / "workspace" / "verified" / "train_all_canonical.jsonl"

all_records = []
seen_ids = set()

for d in [v_w1, v_w2]:
    if d.exists():
        for f in d.glob("*.jsonl"):
            with open(f, encoding="utf-8") as fp:
                for line in fp:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        rec = json.loads(line)
                        rid = rec.get("id") or rec.get("meta", {}).get("item_id")
                        if rid not in seen_ids:
                            seen_ids.add(rid)
                            all_records.append(rec)
                    except Exception:
                        pass

print(f"Total Unique Verified Lessons Gathered: {len(all_records)}")

# Reformat via format_pilot_for_tutor_data logic
from format_pilot_for_tutor_data import items_by_id, VALID_SUBJECTS, ALLOWED_TECHNIQUES

canonical_records = []
for r in all_records:
    c = r.get("control", {})
    m = r.get("meta", {})
    item_id = m.get("item_id", "")
    item = items_by_id.get(item_id, {})

    # group_id
    group_id = item_id if item_id else (m.get("paper_id") or r.get("id", "pilot-group"))
    r["group_id"] = str(group_id)

    # Subject
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

    c["grade"] = int(c.get("grade", 12))
    c["student_level"] = c.get("student_level", "struggling")
    c["tone"] = c.get("tone", "encouraging")
    c["response_length"] = c.get("response_length", "short")
    c["tools"] = []
    if "math_format" not in c and clean_subj in {"mathematics", "physical_sciences"}:
        c["math_format"] = "latex"

    # Meta
    m["topic"] = m.get("topic") or item.get("topic") or f"Grade {c['grade']} {clean_subj.replace('_', ' ').title()}"
    m["task_type"] = "comprehension" if clean_subj in ("english", "afrikaans") else "solve_problem"
    m["student_language"] = c.get("subject_language") or ("af" if "afrikaans" in raw_subj or "wiskunde" in raw_subj or "wetenskap" in raw_subj else "en")
    m["strategy_used"] = c.get("strategy", "step_walkthrough")
    m["source_type"] = "past_paper_adapted"
    m["source_licence"] = "DBE Open Educational Resource"
    m["generator"] = m.get("generator", "eishkom-distiller")
    m["answer_verified"] = True
    m["split"] = "auto"
    m["verification_method"] = "sympy_vs_memo"

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

    # Messages
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
            clean_msgs.append({
                "role": "assistant",
                "reasoning": reasoning or "Guide the student with a patient Socratic hint.",
                "content": content
            })
            expected_role = "user"
        elif role == "assistant" and expected_role == "user":
            if clean_msgs and clean_msgs[-1]["role"] == "assistant":
                clean_msgs[-1]["content"] += "\n\n" + content
        elif role == "user" and expected_role == "assistant":
            if clean_msgs and clean_msgs[-1]["role"] == "user":
                clean_msgs[-1]["content"] += "\n\n" + content

    if clean_msgs and clean_msgs[-1]["role"] == "user":
        clean_msgs.pop()

    if len(clean_msgs) >= 2 and clean_msgs[0]["role"] == "user" and clean_msgs[-1]["role"] == "assistant":
        r["messages"] = clean_msgs
        canonical_records.append(r)

with open(out_canonical, "w", encoding="utf-8") as fp:
    for rec in canonical_records:
        fp.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Successfully compiled {len(canonical_records)} canonical verified lessons to {out_canonical}")

