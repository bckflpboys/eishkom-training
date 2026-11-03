#!/usr/bin/env python3
"""
plan.py - decide WHAT training data to write before spending any money.

    python pipeline/plan.py --round r1 [--target 300] [--seed 1]

WHY PLAN FIRST
  If you just ask the teacher "write me 3,000 tutoring dialogues" you get 3,000 dialogues that all look
  the same: friendly, medium length, same strategy. Your model then learns ONE teaching style. A plan
  makes the variety deliberate. Each plan row says: use THIS question, with THESE settings (teaching
  strategy, answer policy, learner level, tone, length, thinking on/off, tools, language, learner state,
  a common misconception to include). The settings are sampled from the weights in
  workspace/config/plan_config.json, round-robin over subject x grade so no cell is starved.

  The plan is also the labels: the settings in each row become the record's `control` block, so the
  model learns "when I am told X, I do X".

  Language subjects follow SA rules: English -> English; Afrikaans HL -> Afrikaans; Afrikaans FAL ->
  English explanations for Gr 7-9 (the learner is still learning the language), mirrored from Gr 10.

OUTPUT   workspace/plans/<round>.jsonl
"""
import argparse
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tutor_data as td  # noqa: E402
from wspaths import p, read_jsonl, write_jsonl  # noqa: E402


def wchoice(rng, weights):
    keys = list(weights)
    return rng.choices(keys, weights=[max(0.0, float(weights[k])) for k in keys], k=1)[0]


def grade_band(g):
    return "7-9" if g <= 9 else "10-12"


def load_items(cfg, allow_review):
    items, skipped = [], Counter()
    for f in sorted(p("items").glob("*.jsonl")):
        if cfg["include_sources"] and f.stem not in cfg["include_sources"]:
            continue
        if f.stem in cfg["holdout_sources"]:
            skipped["holdout source"] += 1
            continue
        for it in read_jsonl(f):
            try:
                it["grade"] = int(it["grade"])
            except (TypeError, ValueError):
                skipped["bad grade"] += 1
                continue
            if it["subject"] not in cfg["subjects"] or it["grade"] not in cfg["grades"] or it["kind"] not in cfg["kinds"]:
                continue
            if not it.get("question"):
                continue
            if it.get("needs_review") and not allow_review:
                skipped["needs_review"] += 1
                continue
            items.append(it)
    return items, skipped


def pick_misconception(rng, item, mis):
    cands = [m for m in mis if m["subject"] == item["subject"] and m["grade_min"] <= item["grade"] <= m["grade_max"]]
    topic = (item.get("topic") or "").lower()
    close = [m for m in cands if m["topic"].replace("_", " ") in topic or topic in m["topic"].replace("_", " ")] if topic else []
    pool = close or cands
    return rng.choice(pool) if pool else None


def make_row(rng, cfg, item, lang, variant, has_index, mis, topics_by_subject, counter, round_name):
    subject, grade = item["subject"], item["grade"]
    level = wchoice(rng, cfg["student_level_weights"])
    # --- language ---------------------------------------------------------------------------------
    track = None
    mirror = rng.random() < cfg["response_language_mirror_probability"]
    if subject == "english":
        track = item.get("track") or cfg["default_tracks"].get("english", "HL")
        student_lang, subject_lang, response_lang = "en", "en", "en"
    elif subject == "afrikaans":
        track = item.get("track") or cfg["default_tracks"].get("afrikaans", "FAL")
        subject_lang = "af"
        if track == "HL":
            student_lang, response_lang = "af", ("mirror" if mirror else "af")
        elif grade <= 9:
            student_lang, response_lang = ("en" if rng.random() < 0.75 else "af"), "en"
        else:
            student_lang, response_lang = ("af" if rng.random() < 0.5 else "en"), "mirror"
    else:
        if lang == "en+af" or (cfg.get("mixed_fraction", 0) and rng.random() < cfg["mixed_fraction"]):
            student_lang, response_lang = "mixed", "mirror"
        else:
            student_lang, response_lang = lang, ("mirror" if mirror else lang)
        subject_lang = lang if lang in ("en", "af") else "en"
    # --- teaching settings -------------------------------------------------------------------------
    if rng.random() < cfg["auto_fraction"]:
        strategy = "auto"
    else:
        weights = dict(cfg["strategy_by_level"][level])
        for ex in cfg["strategy_exclude_by_subject"].get(subject, []):
            weights.pop(ex, None)
        strategy = wchoice(rng, weights)
    policy = wchoice(rng, cfg["answer_policy_weights"])
    tone = wchoice(rng, cfg["tone_by_grade_band"][grade_band(grade)])
    length = wchoice(rng, cfg["response_length_weights"])
    if policy == "full_solution" and subject in td.CHECKABLE and length == "short":
        length = "medium"
    thinking = "on" if rng.random() < cfg["thinking_probability"].get(subject, 0.3) else "off"
    avail = [t for t in cfg["tools_by_subject"].get(subject, []) if has_index or t != "search_curriculum"]
    tools = []
    if strategy == "visual_board" and "board" in avail:
        tools = ["board"] + (["calculator"] if "calculator" in avail and rng.random() < 0.5 else [])
    elif avail and rng.random() < cfg["tool_availability_probability"]:
        tools = rng.sample(avail, min(rng.choice([1, 2]), len(avail)))
    control = {"subject": subject, "grade": grade, "subject_language": subject_lang, "response_language": response_lang,
               "strategy": strategy, "answer_policy": policy, "student_level": level, "tone": tone,
               "response_length": length, "tools": tools}
    if track:
        control["language_track"] = track
    if subject in td.NEEDS_MATH_FORMAT:
        control["math_format"] = cfg.get("math_format", "latex")
    if strategy in ("spaced_recap", "retrieval_quiz") and rng.random() < 0.6:
        others = [t for t in topics_by_subject.get(subject, []) if t and t != item.get("topic")]
        if others:
            ctx = {"recent_topics": rng.sample(others, min(len(others), rng.choice([1, 2, 3]))),
                   "days_since_last_session": rng.choice([1, 2, 3, 5, 7, 10, 14])}
            if rng.random() < 0.5:
                ctx["weak_topics"] = [rng.choice(others)]
            control["learner_context"] = ctx
    # --- mode: faithful (real question) or original (invent a new one, verified by code) ------------
    mode = wchoice(rng, cfg["mode_mix"])
    if subject in td.CHECKABLE and not item.get("final_answer"):
        mode = "original"
    state = wchoice(rng, cfg["student_state_weights"])
    mis_row = pick_misconception(rng, item, mis) if rng.random() < cfg["misconception_probability"] else None
    learner = {"student_language": student_lang, "state": state, "turns": int(wchoice(rng, cfg["turns"])),
               "style": wchoice(rng, {"plain": 0.5, "informal": 0.4, "with_attempt": 0.1}),
               "misconception": ({"misconception": mis_row["misconception"], "correct_idea": mis_row["correct_idea"]}
                                 if mis_row else None)}
    counter[0] += 1
    return {"plan_id": f"{round_name}-{counter[0]:05d}", "round": round_name, "item_id": item["item_id"],
            "group_id": f"{item['item_id']}-v{variant}", "mode": mode, "control": control, "thinking": thinking,
            "learner": learner}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=str(p("config", "plan_config.json")))
    ap.add_argument("--round", help="round name (default: from the config file)")
    ap.add_argument("--target", type=int, help="number of rows (default: from the config file)")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--allow-review-items", action="store_true", help="also use items flagged needs_review")
    a = ap.parse_args()

    cfg = json.loads(Path(a.config).read_text(encoding="utf-8"))
    round_name = a.round or cfg["round"]
    target = a.target or cfg["target_records"]
    items, skipped = load_items(cfg, a.allow_review_items)
    if not items:
        sys.exit("no items match the filters in the config (subjects/grades/kinds). Did extract_items.py run? "
                 f"skipped: {dict(skipped)}")
    mis_path = p("config", "misconceptions.jsonl")
    mis = read_jsonl(mis_path) if mis_path.exists() else []
    has_index = p("index", "bm25.json").exists()
    topics_by_subject = defaultdict(list)
    for it in items:
        if it.get("topic") and it["topic"] not in topics_by_subject[it["subject"]]:
            topics_by_subject[it["subject"]].append(it["topic"])

    rng = random.Random(a.seed)
    cells = defaultdict(list)
    for it in items:
        cells[(it["subject"], it["grade"])].append(it)
    for lst in cells.values():
        rng.shuffle(lst)
    order = sorted(cells)
    cursor = {k: 0 for k in order}
    rows, counter, variant_seen = [], [0], Counter()
    langs = cfg["languages"] if len(cfg["languages"]) else ["en"]
    guard = 0
    while len(rows) < target and guard < target * 20:
        for key in order:
            lst = cells[key]
            item = lst[cursor[key] % len(lst)]
            cursor[key] += 1
            variant_seen[item["item_id"]] += 1
            v = variant_seen[item["item_id"]]
            for lang in ([None] if item["subject"] in td.LANGUAGE_SUBJECTS else langs):
                rows.append(make_row(rng, cfg, item, lang, v, has_index, mis, topics_by_subject, counter, round_name))
            if len(rows) >= target:
                break
        guard += 1
    rows = rows[:target]
    out = p("plans", f"{round_name}.jsonl")
    write_jsonl(out, rows)

    print(f"wrote {len(rows)} plan rows to {out}   (items available: {len(items)}; skipped: {dict(skipped)})")
    def show(title, counter_):
        print(f"\n{title}: " + ", ".join(f"{k}={v}" for k, v in sorted(counter_.items(), key=lambda kv: -kv[1])))
    show("subject", Counter(r["control"]["subject"] for r in rows))
    show("grade", Counter(r["control"]["grade"] for r in rows))
    show("reply language setting", Counter(r["control"]["response_language"] for r in rows))
    show("strategy", Counter(r["control"]["strategy"] for r in rows))
    show("answer policy", Counter(r["control"]["answer_policy"] for r in rows))
    show("mode", Counter(r["mode"] for r in rows))
    show("thinking", Counter(r["thinking"] for r in rows))
    show("rows with tools", Counter(bool(r["control"]["tools"]) for r in rows))
    reuse = max(variant_seen.values())
    print(f"\neach item is used up to {reuse} time(s). If that is high, you need more items (more papers/books).")
    print("NEXT: python pipeline/generate.py --round", round_name, "--limit 10   (a cheap test first!)")


if __name__ == "__main__":
    main()
