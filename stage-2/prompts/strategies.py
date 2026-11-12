"""
stage-2/prompts/strategies.py - Teaching strategy and learner persona definitions for Stage 2.

Merges CAPS pedagogical strategies with scripted learner turn progressions.
The pipeline selects:
  - strategy (closed list matching tutor-v1 STRATEGIES)
  - learner_state & learner_script (scripted turn behavior so the student doesn't magically become correct)
  - thinking_mode ('short' | 'full' | 'none')
  - turn count (dynamic based on question marks)
"""

import random

# Subject classification
LANGUAGE_SUBJECTS = {
    "english", "english_hl", "english_fal", "afrikaans", "afrikaans_hl", "afrikaans_fal",
    "languages_en_hl", "languages_en_fal", "languages_af_hl", "languages_af_fal"
}

def classify_subject(subject_raw: str) -> str:
    s = str(subject_raw).lower().strip()
    if any(k in s for k in ["math", "wiskunde"]):
        return "math"
    elif any(k in s for k in ["phys", "science", "wetenskap", "natural"]):
        return "science"
    else:
        return "language"

# ── Closed Strategies (strictly valid in tutor_spec / tutor_data.py) ──────────
STRATEGIES = [
    {
        "name": "step_walkthrough",
        "label": "Step-by-Step Guided Walkthrough",
        "prompt_fragment": (
            "TEACHING STRATEGY: step_walkthrough\n"
            "Walk the learner through the question one step at a time, giving the reason for each step. "
            "At each stage, ask ONE diagnostic question before revealing the next step. "
            "Wait for the learner's attempt before proceeding."
        ),
        "weights": {"math": 25, "science": 25, "language": 15},
    },
    {
        "name": "worked_example",
        "label": "Worked Example with Conceptual Transfer",
        "prompt_fragment": (
            "TEACHING STRATEGY: worked_example\n"
            "Show a short, clear worked example of a similar (parallel) problem first with different numbers/context. "
            "Then guide the learner to transfer that method to the actual question."
        ),
        "weights": {"math": 20, "science": 15, "language": 5},
    },
    {
        "name": "faded_example",
        "label": "Faded Scaffolding",
        "prompt_fragment": (
            "TEACHING STRATEGY: faded_example\n"
            "Work the example together, leaving progressively more calculation/reasoning steps for the learner to complete each turn."
        ),
        "weights": {"math": 15, "science": 15, "language": 5},
    },
    {
        "name": "error_analysis",
        "label": "Spot and Correct Common Misconceptions",
        "prompt_fragment": (
            "TEACHING STRATEGY: error_analysis\n"
            "Focus specifically on the common student misconception or arithmetic/algebraic trap in this problem. "
            "Help the learner diagnose WHY the mistake happens and how to avoid it."
        ),
        "weights": {"math": 15, "science": 15, "language": 15},
    },
    {
        "name": "socratic_hints",
        "label": "Pure Socratic Hint Ladder",
        "prompt_fragment": (
            "TEACHING STRATEGY: socratic_hints\n"
            "Lead strictly with questions and small clues. Never reveal intermediate calculations until the learner has attempted them."
        ),
        "weights": {"math": 10, "science": 10, "language": 20},
    },
    {
        "name": "analogy_real_world",
        "label": "South African Real-World Analogy",
        "prompt_fragment": (
            "TEACHING STRATEGY: analogy_real_world\n"
            "Explain the underlying principle using a relatable, everyday South African analogy or scenario, "
            "then map each element back to the question."
        ),
        "weights": {"math": 5, "science": 10, "language": 15},
    },
    {
        "name": "mnemonic",
        "label": "Mnemonic & Memory Anchor",
        "prompt_fragment": (
            "TEACHING STRATEGY: mnemonic\n"
            "Provide an accurate, memorable cognitive anchor (acronym, rhyme, or chunking rule) that helps the student recall the rule/formula."
        ),
        "weights": {"math": 5, "science": 10, "language": 10},
    },
    {
        "name": "exam_technique",
        "label": "Exam Technique & Mark Allocation Coaching",
        "prompt_fragment": (
            "TEACHING STRATEGY: exam_technique\n"
            "Coach how to answer for marks: formula mark, substitution mark, accuracy mark, units, and what the examiner penalizes."
        ),
        "weights": {"math": 10, "science": 10, "language": 15},
    },
    {
        "name": "direct_explanation",
        "label": "Direct, Kind De-Escalation & Explanation",
        "prompt_fragment": (
            "TEACHING STRATEGY: direct_explanation\n"
            "When the learner is panicking or stuck, provide a brief, reassuring, direct explanation before asking them to try the final calculation."
        ),
        "weights": {"math": 5, "science": 5, "language": 10},
    },
]

STRATEGY_MAP = {s["name"]: s for s in STRATEGIES}

# ── Scripted Learner States & Turn Trajectories ─────────────────────────────
# Each state provides a realistic turn-by-turn script so the student doesn't
# magically get everything right on turn 1.
LEARNER_STATES = {
    "blank_stuck": {
        "weight": 20,
        "kind": "both",
        "student_level": "struggling",
        "script": ["partial", "correct"],
        "desc": "Learner has no idea where to start and gives minimal, hesitant responses.",
    },
    "partial_attempt": {
        "weight": 20,
        "kind": "both",
        "student_level": "struggling",
        "script": ["correct_step", "correct"],
        "desc": "Learner knows the first step or formula but gets stuck on the execution.",
    },
    "confident_wrong": {
        "weight": 20,
        "kind": "both",
        "student_level": "struggling",
        "script": ["wrong_new_error", "partial", "correct"],
        "desc": "Learner is confident but applies the wrong rule or makes a conceptual error.",
    },
    "slip_arith_sign_unit": {
        "weight": 15,
        "kind": "stem",
        "student_level": "on_track",
        "script": ["spots_slip_after_hint", "correct"],
        "desc": "Learner understands the method but made a sign error, unit slip, or calculation mistake.",
    },
    "language_slip": {
        "weight": 15,
        "kind": "language",
        "student_level": "on_track",
        "script": ["spots_slip_after_hint", "correct"],
        "desc": "Learner has the right idea but made a grammatical, spelling, or quote-formatting error.",
    },
    "misread_question": {
        "weight": 10,
        "kind": "both",
        "student_level": "on_track",
        "script": ["realises_misread", "correct"],
        "desc": "Learner answered for a different variable or misread the constraint.",
    },
    "wants_answer_only": {
        "weight": 10,
        "kind": "both",
        "student_level": "struggling",
        "script": ["pushes_back", "accepts_guided_step", "correct"],
        "desc": "Impatient learner asking for the answer directly; teacher holds Socratic boundary kindly.",
    },
    "exam_panic": {
        "weight": 10,
        "kind": "both",
        "student_level": "struggling",
        "script": ["calmer_partial", "correct"],
        "desc": "Anxious learner afraid of failing the exam; teacher provides calm de-escalation.",
    },
    "strong_wants_marks": {
        "weight": 10,
        "kind": "both",
        "student_level": "advanced",
        "script": ["correct", "asks_how_marks_are_awarded", "correct"],
        "desc": "Capable learner aiming for full marks who asks about exam layout and mark breakdown.",
    },
}

# Closed list of techniques strictly from tutor-v1 ALLOWED_TECHNIQUES
TECHNIQUES_BY_CAT = {
    "math": [
        "polya_four_steps", "given_formula_substitute_answer", "check_by_substitution",
        "bodmas", "factor_tree", "soh_cah_toa", "cubes", "work_backwards", "estimate_first",
        "table_of_values", "draw_a_diagram", "try_simple_numbers", "units_conversion"
    ],
    "science": [
        "concept_map", "units_check", "given_formula_substitute_answer", "check_by_substitution",
        "predict_observe_explain", "particle_diagram", "energy_chain", "units_conversion",
        "draw_a_diagram", "estimate_first"
    ],
    "language": [
        "context_clues", "mark_per_point", "command_word_decode", "annotate_text",
        "five_ws", "skim_and_scan", "paraphrase_then_answer", "plan_write_check",
        "sq3r", "qar", "peel", "teel"
    ],
}

def determine_turns_from_marks(marks: int) -> int:
    """Map DBE question marks to dialogue turns."""
    try:
        m = int(marks)
    except Exception:
        m = 2
    if m <= 2:
        return 2
    elif m <= 4:
        return 3
    elif m <= 6:
        return 4
    else:
        return 5

def pick_strategy(subject_raw: str, exclude: set = None) -> dict:
    cat = classify_subject(subject_raw)
    candidates = [s for s in STRATEGIES if s["weights"].get(cat, 0) > 0]
    if exclude:
        filtered = [s for s in candidates if s["name"] not in exclude]
        if filtered:
            candidates = filtered
    weights = [s["weights"][cat] for s in candidates]
    return random.choices(candidates, weights=weights, k=1)[0]

def pick_student_persona(subject_raw: str, marks: int = 2) -> dict:
    cat = classify_subject(subject_raw)
    is_lang = cat == "language"

    eligible_states = {}
    for state_name, s_info in LEARNER_STATES.items():
        kind = s_info["kind"]
        if kind == "both":
            eligible_states[state_name] = s_info["weight"]
        elif kind == "language" and is_lang:
            eligible_states[state_name] = s_info["weight"]
        elif kind == "stem" and not is_lang:
            eligible_states[state_name] = s_info["weight"]

    state_keys = list(eligible_states.keys())
    state_weights = [eligible_states[k] for k in state_keys]
    chosen_state = random.choices(state_keys, weights=state_weights, k=1)[0]
    state_info = LEARNER_STATES[chosen_state]

    num_turns = determine_turns_from_marks(marks)

    # Build turn-by-turn script
    raw_script = list(state_info["script"])
    # Adjust script length to match num_turns - 1 (learner turns after opener)
    target_len = max(1, num_turns - 1)
    if len(raw_script) < target_len:
        while len(raw_script) < target_len:
            raw_script.insert(-1, "partial_progress")
    elif len(raw_script) > target_len:
        raw_script = raw_script[:target_len]

    # 5% chance of gives_up on final learner turn for de-escalation practice
    if random.random() < 0.05:
        raw_script[-1] = "gives_up"
    else:
        raw_script[-1] = "correct"

    # Select 1-2 techniques
    tech_pool = TECHNIQUES_BY_CAT.get(cat, TECHNIQUES_BY_CAT["math"])
    techniques = random.sample(tech_pool, k=min(2, len(tech_pool)))

    return {
        "state": chosen_state,
        "student_level": state_info["student_level"],
        "desc": state_info["desc"],
        "script": raw_script,
        "turns": num_turns,
        "techniques": techniques,
    }
