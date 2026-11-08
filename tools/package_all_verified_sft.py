import json
from pathlib import Path
import subprocess
import sys
import re

ROOT_DIR = Path(__file__).resolve().parent.parent
v_dirs = [
    ROOT_DIR / "workspace" / "verified" / "test_round",
    ROOT_DIR / "workspace" / "verified" / "wave2",
    ROOT_DIR / "workspace" / "verified" / "wave3",
    ROOT_DIR / "workspace" / "verified" / "wave4",
    ROOT_DIR / "workspace" / "verified" / "wave5",
]
fullsol_dir = ROOT_DIR / "workspace" / "verified" / "full_solutions"

out_canonical = ROOT_DIR / "workspace" / "verified" / "train_all_canonical.jsonl"
out_master = ROOT_DIR / "workspace" / "verified" / "train_master_combined.jsonl"

all_records = []
seen_ids = set()

for d in v_dirs:
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

print(f"Total Unique Verified Lessons Gathered from Waves 1-5: {len(all_records)}")

from format_pilot_for_tutor_data import items_by_id, VALID_SUBJECTS, ALLOWED_TECHNIQUES

canonical_records = []
for r in all_records:
    c = r.get("control", {})
    m = r.get("meta", {})
    item_id = m.get("item_id", "")
    item = items_by_id.get(item_id, {})

    # group_id
    group_id = item_id if item_id else (m.get("paper_id") or r.get("id", "socratic-group"))
    r["group_id"] = str(group_id)

    # Subject
    raw_subj = c.get("subject", "mathematics")
    lang_track = None
    if raw_subj in ("afrikaans_hl", "languages_af_hl"):
        subject = "languages"
        lang_track = "afrikaans_hl"
    elif raw_subj in ("afrikaans_fal", "languages_af_fal"):
        subject = "languages"
        lang_track = "afrikaans_fal"
    elif raw_subj in ("english_hl", "languages_en_hl"):
        subject = "languages"
        lang_track = "english_hl"
    elif raw_subj in ("english_fal", "languages_en_fal"):
        subject = "languages"
        lang_track = "english_fal"
    elif raw_subj in ("fisiese_wetenskappe", "sciences"):
        subject = "sciences"
    elif raw_subj in ("physical_sciences", "physical_science"):
        subject = "sciences"
    elif raw_subj in ("wiskunde", "maths", "mathematics"):
        subject = "mathematics"
    elif raw_subj in VALID_SUBJECTS:
        subject = raw_subj
    else:
        subject = "mathematics"

    c["subject"] = subject
    if lang_track:
        c["language_track"] = lang_track
    elif "language_track" in c:
        del c["language_track"]

    if "subject_language" not in c:
        c["subject_language"] = "af" if ("afrikaans" in raw_subj or "wiskunde" in raw_subj or "wetenskappe" in raw_subj) else "en"
    if "response_language" not in c:
        c["response_language"] = "mirror"

    # Meta techniques
    techniques = m.get("techniques", [])
    valid_techs = [t for t in techniques if t in ALLOWED_TECHNIQUES]
    if not valid_techs:
        valid_techs = ["polya_four_steps", "check_by_substitution"] if subject == "mathematics" else ["units_check", "concept_map"] if subject == "sciences" else ["context_clues", "mark_per_point"]
    m["techniques"] = valid_techs

    # Clean messages
    msgs = r.get("messages", [])
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
                "reasoning": reasoning or "Guide the student with a patient Socratic hint.",
                "content": content
            })
            expected_role = "user"
        elif role == "assistant" and expected_role == "user":
            if clean_msgs and clean_msgs[-1]["role"] == "assistant":
                clean_msgs[-1]["content"] += "\n\n" + content

    if clean_msgs and clean_msgs[-1]["role"] == "user":
        clean_msgs.pop()

    if len(clean_msgs) >= 2 and clean_msgs[0]["role"] == "user" and clean_msgs[-1]["role"] == "assistant":
        r["messages"] = clean_msgs
        canonical_records.append(r)

with open(out_canonical, "w", encoding="utf-8") as fp:
    for rec in canonical_records:
        fp.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Successfully compiled {len(canonical_records)} canonical verified Socratic lessons to {out_canonical}")

# Now build train_master_combined.jsonl: Socratic + Full Solutions
master_records = list(canonical_records)
full_count = 0

if fullsol_dir.exists():
    for f in fullsol_dir.glob("*.jsonl"):
        with open(f, encoding="utf-8") as fp:
            for line in fp:
                line = line.strip()
                if line:
                    try:
                        rec = json.loads(line)
                        master_records.append(rec)
                        full_count += 1
                    except Exception:
                        pass

with open(out_master, "w", encoding="utf-8") as fp:
    for rec in master_records:
        fp.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Master Combined Corpus: {len(master_records)} total records ({len(canonical_records)} Socratic lessons + {full_count} Full Solutions)")
print(f"Written to {out_master}")

# Now run tutor_data.py build
print("\nRunning tutor_data.py build...")
cmd = [
    sys.executable,
    str(ROOT_DIR / "sa-tutor-kit" / "sa-tutor-kit" / "tutor_data.py"),
    "build",
    str(out_master),
    "--out",
    str(ROOT_DIR / "workspace" / "build" / "r1"),
    "--val",
    "0.15"
]
subprocess.run(cmd)
