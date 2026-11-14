"""
sampler_agentic.py - Spec builders + deterministic helpers for page-worker, synthesiser and study tasks.

Rule: CODE owns every number (marks totals, dates, schedules, rankings). The model only reads and explains them.
The same aggregate_notes() / build_schedule() / rank_weak_topics() / time_plan() should run in the real app.
"""
import copy
import datetime as dt
import random
import json
from pathlib import Path

# ----------------------------------------------------------------------------- verified SA helplines
HELPLINE_TEXT_EN = (
    "SADAG Mental Health Line: 0800 456 789 | 24hr Suicide Crisis Helpline: 0800 567 567 (SMS: 31393) | "
    "Childline South Africa: 116 | LifeLine SA: 0861 322 322"
)
HELPLINE_TEXT_AF = (
    "SADAG Geestesgesondheidslyn: 0800 456 789 | 24-uur Selfmoordkrisislyn: 0800 567 567 (SMS: 31393) | "
    "Childline Suid-Afrika: 116 | LifeLine SA: 0861 322 322"
)

# ----------------------------------------------------------------------------- shared
GRADE_WEIGHTS = {7: 10, 8: 10, 9: 12, 10: 16, 11: 18, 12: 34}
LANGUAGE_WEIGHTS = {"en": 65, "af": 35}
THINKING_MODES = {"none": 30, "short": 40, "full": 30}
STUDY_TECHNIQUES = [
    "retrieval_practice", "spaced_revision", "past_paper_first", "explain_it_back", "time_boxing", "interleaving",
    "south_african_everyday_analogy", "mnemonic", "common_mistake_warning", "light_humour",
]

# Comprehensive closed CAPS topic lists per subject across Grades 7-12
TOPIC_KEYS = {
    "Mathematics": [
        "algebra_equations_inequalities", "sequences_series", "functions_graphs", "finance_growth_decay",
        "differential_calculus", "probability_counting", "analytical_geometry", "trigonometry",
        "euclidean_geometry", "statistics"
    ],
    "Physical Sciences": [
        "momentum_impulse", "vertical_projectile_motion", "work_energy_power", "doppler_effect",
        "electrostatics", "electric_circuits", "electrodynamics", "photoelectric_effect",
        "organic_chemistry", "reaction_rates", "chemical_equilibrium", "acids_bases", "electrochemistry"
    ],
    "Natural Sciences": [
        "matter_materials", "energy_change", "life_living", "earth_beyond"
    ],
    "English": [
        "comprehension_text_analysis", "summary_writing", "language_structures_conventions",
        "poetry_analysis", "novel_drama_literature", "transactional_writing"
    ],
    "Afrikaans": [
        "begripslees_teksontleding", "opsomming", "taalstrukture_konvensies",
        "poesie_gedigontleding", "roman_drama_letterkunde", "transaksionele_teks"
    ],
}

STUDY_TASKS = {
    "intake": 14,
    "study_plan": 20,
    "study_guide_section": 20,
    "revision_session": 18,
    "weak_topic_diagnosis": 10,
    "exam_strategy": 8,
}
PAPER_TASKS = {
    "paper_walkthrough": 50,
    "paper_prep_guide": 30,
    "paper_exam_strategy": 20,
}

STUDY_STATES = {
    "overwhelmed": 12, "organised_wants_optimisation": 12, "procrastinator_days_left": 10, "anxious_perfectionist": 8,
    "behind_syllabus": 10, "wants_shortcut": 10, "knows_weak_topics": 14, "unsure_whats_weak": 10,
    "unmotivated_parent_pushed": 6, "returning_after_break": 6, "distress_signal": 2,
}

BASE_SCRIPTS = {   # learner replies AFTER the opener; teacher_turns = len(script) + 1
    "intake": [["gives_missing_info", "picks_next_step"], ["picks_next_step"]],
    "study_plan": [["says_plan_too_heavy", "accepts"], ["asks_why_this_order", "accepts"],
                   ["accepts", "asks_what_if_i_fall_behind"]],
    "study_guide_section": [["asks_easier_explanation", "accepts"], ["asks_for_another_example", "accepts"],
                            ["accepts"]],
    "weak_topic_diagnosis": [["disagrees_with_ranking", "accepts"], ["asks_what_first", "accepts"], ["accepts"]],
    "exam_strategy": [["asks_time_per_section", "accepts"], ["asks_what_if_stuck", "accepts"], ["accepts"]],
}
SYNTH_FOLLOWUPS = {
    "asks_detail_on_question": 25, "asks_about_unreadable_page": 15, "asks_for_memo_answer": 15,
    "asks_will_this_come_in_exam": 15, "accepts_and_picks_next_step": 30
}
REVISION_OUTCOMES = {"correct": 55, "partial": 25, "wrong": 20}
PAGE_DAMAGE = ["cropped_bottom", "cropped_top", "blurry", "low_contrast", "rotated", "glare", "shadow"]


def _pick(weights, rng):
    keys = list(weights)
    return rng.choices(keys, weights=[weights[k] for k in keys])[0]


# ----------------------------------------------------------------------------- profiles
def subjects_for(grade, rng):
    pool = ["Mathematics", "Natural Sciences" if grade <= 9 else "Physical Sciences",
            rng.choice(["English", "English Fal"]), rng.choice(["Afrikaans", "Afrikaans Fal"])]
    return rng.sample(pool, k=rng.choice([1, 1, 2, 2, 3]))


def time_phrase(days, lang):
    if lang == "af":
        return "môre" if days == 1 else f"oor {days} dae" if days < 14 else f"oor {days // 7} weke"
    return "tomorrow" if days == 1 else f"in {days} days" if days < 14 else f"in {days // 7} weeks"


def make_profile(rng, today, topic_keys=None):
    topic_keys = topic_keys or TOPIC_KEYS
    grade = _pick(GRADE_WEIGHTS, rng)
    lang = _pick(LANGUAGE_WEIGHTS, rng)
    bucket = _pick({(1, 3): 10, (4, 7): 20, (8, 14): 25, (15, 30): 25, (31, 90): 20}, rng)
    days = rng.randint(*bucket)
    if days >= 14:
        days = 7 * round(days / 7)            # so "in N weeks" is exact
    subjects = subjects_for(grade, rng)
    keyed = [s for s in subjects if s in topic_keys]
    weak = {}
    if keyed:
        s = rng.choice(keyed)
        weak[s] = rng.sample(topic_keys[s], k=min(len(topic_keys[s]), rng.choice([1, 2, 3])))
    return {
        "grade": grade, "subjects": subjects, "language": lang, "days_to_exam": days,
        "exam_date": (today + dt.timedelta(days=days)).isoformat(),
        "time_to_exam_phrase": time_phrase(days, lang),
        "hours_per_day": rng.choice([1, 1.5, 2, 3, 4]), "weak_topics": weak
    }


# ----------------------------------------------------------------------------- deterministic tools
def build_schedule(args, today=None):
    """Reference implementation. args: exam_date, hours_per_day, topics[{subject, topic|None, weak}], start_date.
    Returns {"full": [...every day...], "summary": {...compact, this is what the model sees...}}."""
    start = dt.date.fromisoformat(args.get("start_date") or (today or dt.date.today()).isoformat())
    exam = dt.date.fromisoformat(args["exam_date"])
    n = max((exam - start).days, 1)                      # study days: start .. day before exam
    minutes_day = int(args["hours_per_day"] * 60)
    # every topic once, then weak topics again: weak topics come back spaced apart, never twice in a row
    seq = [(t["subject"], t.get("topic")) for t in args["topics"]]
    seq += [(t["subject"], t.get("topic")) for t in args["topics"] if t.get("weak")]
    subjects = sorted({t["subject"] for t in args["topics"]})
    seen, cursor, pp_count, full = set(), 0, 0, []
    for d in range(n):
        date = (start + dt.timedelta(days=d)).isoformat()
        if n >= 14 and (d + 1) % 7 == 0 and d < n - 2:
            full.append({"date": date, "kind": "rest", "blocks": []})
            continue
        if n >= 7 and (d + 1) % 4 == 0 and d < n - 1:
            subj = subjects[pp_count % len(subjects)]
            pp_count += 1
            full.append({"date": date, "kind": "past_paper",
                         "blocks": [{"topic": f"past_paper:{subj}", "minutes": minutes_day, "activity": "timed_paper"}]})
            continue
        last = (d == n - 1 and n >= 3)
        mins = minutes_day // 2 if last else minutes_day
        nb = max(1, round(mins / 45))
        blocks = []
        for _ in range(nb):
            subj, topic = seq[cursor % len(seq)]
            cursor += 1
            key = (subj, topic)
            act = "light_review" if last else ("retrieval_practice" if key in seen else "learn")
            seen.add(key)
            name = f"{subj}:{topic}" if topic else subj
            same = next((b for b in blocks if b["topic"] == name), None)
            if same:                                     # one block per topic per day
                same["minutes"] += mins // nb
            else:
                blocks.append({"topic": name, "minutes": mins // nb, "activity": act})
        full.append({"date": date, "kind": "light_review" if last else "study", "blocks": blocks})
    by_topic = {}
    for day in full:
        for b in day["blocks"]:
            by_topic[b["topic"]] = by_topic.get(b["topic"], 0) + b["minutes"]
    summary = {
        "start": start.isoformat(), "exam_date": exam.isoformat(), "days": n,
        "study_days": sum(1 for x in full if x["kind"] in ("study", "light_review")),
        "rest_days": sum(1 for x in full if x["kind"] == "rest"),
        "past_paper_days": sum(1 for x in full if x["kind"] == "past_paper"),
        "minutes_by_topic": dict(sorted(by_topic.items(), key=lambda kv: -kv[1])),
        "first_days": full[:3], "last_day": full[-1]
    }
    return {"full": full, "summary": summary}


def rank_weak_topics(results, weights=None):
    rows = []
    for t, r in results.items():
        w = (weights or {}).get(t, 1)
        frac_lost = 1 - r["scored"] / r["out_of"]
        rows.append({
            "topic": t, "percent": round(100 * r["scored"] / r["out_of"]),
            "marks_lost": r["out_of"] - r["scored"], "weight": w, "priority": round(frac_lost * w, 3)
        })
    rows.sort(key=lambda x: (-x["priority"], x["topic"]))
    for i, r in enumerate(rows, 1):
        r["rank"] = i
    return rows


def time_plan(paper_facts, marks_by_section=None):
    tm, dur = paper_facts.get("total_marks"), paper_facts.get("duration_minutes")
    if not tm or not dur:
        return None
    mpm = dur / tm
    secs = marks_by_section or {s["label"]: s["marks"] for s in paper_facts.get("sections", [])}
    return {"minutes_per_mark": round(mpm, 2), "minutes_by_section": {k: int(round(v * mpm)) for k, v in secs.items()}}


# ----------------------------------------------------------------------------- page notes
def aggregate_notes(notes, pages_total):
    """Totals the app computes from worker notes. One entry per question number, marks from whichever page shows them."""
    seen = {n["page"]["index"]: n for n in notes}
    status = {s: sorted(i for i, n in seen.items() if n["page"]["status"] == s) for s in ("ok", "partial", "unreadable", "blank")}
    qs, facts = {}, {}
    for i in sorted(seen):
        for k, v in (seen[i].get("paper_facts") or {}).items():
            if facts.get(k) in (None, [], "") and v not in (None, [], ""):
                facts[k] = v
        for q in seen[i].get("questions", []):
            e = qs.setdefault(q["number"], {"marks": None, "topic": None, "section": None})
            for k in e:
                if e[k] is None and q.get(k) is not None:
                    e[k] = q[k]
    by_topic, by_section, sec_q = {}, {}, {}
    for num, e in qs.items():
        if e["marks"] is not None:
            by_topic[e["topic"] or "other"] = by_topic.get(e["topic"] or "other", 0) + e["marks"]
            by_section[e["section"] or "-"] = by_section.get(e["section"] or "-", 0) + e["marks"]
        sec_q.setdefault(e["section"] or "-", []).append(num)
    read = sum(by_topic.values())
    printed = facts.get("total_marks")
    agg = {
        "pages_total": pages_total, "pages_ok": status["ok"], "pages_partial": status["partial"],
        "pages_unreadable": status["unreadable"], "pages_blank": status["blank"],
        "pages_missing": [i for i in range(1, pages_total + 1) if i not in seen],
        "questions_found": len(qs), "questions_missing_marks": sorted(n for n, e in qs.items() if e["marks"] is None),
        "total_marks_read": read, "total_marks_printed": printed,
        "total_check": "unknown" if printed is None else "match" if printed == read else "differs",
        "marks_by_topic": dict(sorted(by_topic.items(), key=lambda kv: -kv[1])),
        "marks_by_section": by_section, "questions_by_section": sec_q, "paper_facts": facts or None
    }
    if facts:
        agg["time_plan"] = time_plan(facts, by_section)
    return agg


def apply_defects(notes, rng):
    """Damage a clean set of notes so the synthesiser learns to report gaps. Returns (notes, defects)."""
    n_def = rng.choices([0, 1, 2, 3], [40, 35, 20, 5])[0]
    idx = [n["page"]["index"] for n in notes]
    chosen = set(rng.sample(idx, k=min(n_def, len(idx))))
    out, defects = [], {"missing": [], "partial": [], "unreadable": []}
    for n in notes:
        i = n["page"]["index"]
        if i not in chosen:
            out.append(n)
            continue
        kind = rng.choice(["missing", "partial", "unreadable"])
        defects[kind].append(i)
        if kind == "missing":
            continue
        n = copy.deepcopy(n)
        if kind == "unreadable":
            n["page"].update(status="unreadable", issues=["blurry"])
            n["questions"], n["passages"] = [], []
        else:
            n["page"].update(status="partial", issues=["cropped_bottom"])
            n["questions"] = n["questions"][:-1]
        out.append(n)
    return out, defects


# ----------------------------------------------------------------------------- spec builders
def make_page_spec(page_index, pages_total, rng, subject, topic_keys=None):
    topic_keys = topic_keys or TOPIC_KEYS.get(subject, ["general_content"])
    kind = rng.choices(["image", "pdf_text"], [60, 40])[0]
    damage = []
    if kind == "image" and rng.random() < 0.4:
        damage = rng.sample(PAGE_DAMAGE, k=rng.choice([1, 1, 2]))
    return {
        "task_type": "page_worker", "page_index": page_index, "pages_total": pages_total, "input_kind": kind,
        "damage_tags": damage, "has_carry_in": page_index > 1, "subject": subject, "topic_keys": topic_keys
    }


def make_synth_spec(rng, defects):
    task = _pick(PAPER_TASKS, rng)
    has_gaps = any(defects.values())
    first = _pick(SYNTH_FOLLOWUPS, rng)
    if first == "asks_about_unreadable_page" and not has_gaps:
        first = "asks_detail_on_question"
    script = [first] if first == "accepts_and_picks_next_step" else [first, "accepts_and_picks_next_step"]
    return {
        "task_type": task, "learner_language": _pick(LANGUAGE_WEIGHTS, rng),
        "learner_state": _pick(STUDY_STATES, rng) if rng.random() < 0.5 else "neutral",
        "learner_script": script, "teacher_turns": len(script) + 1,
        "techniques": rng.sample(STUDY_TECHNIQUES, k=rng.choice([1, 2])),
        "thinking_mode": _pick(THINKING_MODES, rng), "tool_allowed": False
    }


def make_study_spec(rng, today, topic_keys=None, task=None):
    topic_keys = topic_keys or TOPIC_KEYS
    p = make_profile(rng, today, topic_keys)
    task = task or _pick(STUDY_TASKS, rng)
    state = _pick(STUDY_STATES, rng)
    helpline = HELPLINE_TEXT_AF if p["language"] == "af" else HELPLINE_TEXT_EN
    spec = {
        "task_type": task, "learner_state": state, "today": today.isoformat(), "learner_language": p["language"],
        "profile": p, "techniques": rng.sample(STUDY_TECHNIQUES, k=rng.choice([1, 2])),
        "thinking_mode": _pick(THINKING_MODES, rng), "tool_allowed": True, "tools": [], "tool_results": [],
        "needs": [], "helpline_text": helpline
    }
    if state == "distress_signal":
        spec.update(learner_script=["gives_a_bit_more"], teacher_turns=2, tool_allowed=False, override="distress_protocol")
        return spec
    keyed = [s for s in p["subjects"] if s in topic_keys]

    if task == "intake":
        spec["revealed_fields"] = rng.sample(["grade", "subjects", "time_to_exam", "weak_topics", "hours_per_day"],
                                             k=rng.choice([1, 2, 3]))
        spec["tools"] = ["update_profile"]
        script = list(rng.choice(BASE_SCRIPTS["intake"]))
    elif task == "study_plan":
        dropped = rng.sample(["subjects", "time_to_exam", "hours_per_day"],
                             k=rng.choices([0, 1, 2], [50, 35, 15])[0])
        spec["profile_missing_fields"] = dropped
        spec["tools"] = ["build_schedule"]
        script = list(rng.choice(BASE_SCRIPTS["study_plan"]))
        if "says_plan_too_heavy" in script and p["hours_per_day"] <= 1:
            script[script.index("says_plan_too_heavy")] = "asks_why_this_order"
        if dropped:
            script = ["gives_missing_info"] + script
        topics = []
        for s in p["subjects"]:
            ks = topic_keys.get(s)
            if ks:
                topics += [{"subject": s, "topic": k, "weak": k in p["weak_topics"].get(s, [])} for k in ks]
            else:
                topics.append({"subject": s, "topic": None, "weak": False})
        args = {
            "exam_date": p["exam_date"], "hours_per_day": p["hours_per_day"], "topics": topics,
            "start_date": today.isoformat()
        }
        spec["expected_tool_calls"] = [{"name": "build_schedule", "args": args}]
        spec["tool_results"] = [build_schedule(args)["summary"]]
        if "says_plan_too_heavy" in script:
            args2 = dict(args, hours_per_day=max(1, p["hours_per_day"] - 1))
            spec["expected_tool_calls"].append({"name": "build_schedule", "args": args2})
            spec["tool_results"].append(build_schedule(args2)["summary"])
    elif task in ("study_guide_section", "revision_session"):
        spec["tool_allowed"] = False
        s = rng.choice(keyed) if keyed else "Mathematics"
        spec["subject"] = s
        spec["topic"] = rng.choice(topic_keys[s]) if s in topic_keys else "algebra"
        if task == "study_guide_section":
            spec["needs"] = ["source_excerpts"]
            script = list(rng.choice(BASE_SCRIPTS["study_guide_section"]))
        else:
            spec["needs"] = ["question_bank"]
            q = rng.choice([3, 4, 5])
            spec["question_count"] = q
            script = [_pick(REVISION_OUTCOMES, rng) for _ in range(q)]
    elif task == "weak_topic_diagnosis":
        spec["tools"] = ["rank_weak_topics"]
        s = rng.choice([x for x in keyed if len(topic_keys[x]) >= 4]) if any(len(topic_keys[x]) >= 4 for x in keyed) else "Mathematics"
        spec["subject"] = s
        if s and s in topic_keys:
            ts = rng.sample(topic_keys[s], k=rng.choice([4, 5, 6]))
            results = {}
            for t in ts:
                out_of = rng.choice([12, 16, 20, 24, 30, 40])
                results[t] = {"scored": rng.randint(int(out_of * 0.2), out_of), "out_of": out_of}
            spec["results"] = results
            spec["expected_tool_calls"] = [{"name": "rank_weak_topics", "args": {"results": results}}]
            spec["tool_results"] = [rank_weak_topics(results)]
        else:
            spec["needs"] = ["results"]
        script = list(rng.choice(BASE_SCRIPTS["weak_topic_diagnosis"]))
    else:  # exam_strategy
        spec["tool_allowed"] = False
        spec["has_paper_facts"] = rng.random() < 0.6
        spec["needs"] = ["paper_facts"] if spec["has_paper_facts"] else []
        script = list(rng.choice(BASE_SCRIPTS["exam_strategy"]))

    spec["learner_script"] = script
    spec["teacher_turns"] = len(script) + 1
    return spec

