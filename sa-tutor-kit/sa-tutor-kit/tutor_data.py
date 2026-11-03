#!/usr/bin/env python3
"""
tutor_data.py - validate, report on, and build training samples from tutor records (schema "tutor-v1").

    python tutor_data.py validate data.jsonl [--strict]
    python tutor_data.py report   data.jsonl [--min-cell 10]
    python tutor_data.py build    data.jsonl --out build/ [options]      (see --help)

Standard library only. What each field means: tutor_spec.md.

What `build` does
  1. validates every record (aborts on errors unless --skip-invalid)
  2. renders the system prompt from `control` (seeded field dropout, one draw per record)
  3. splits each record into ONE SAMPLE PER ASSISTANT TURN:
        {"prompt": [system, ...history], "completion": <assistant message>,
         "tools": [...], "thinking": "on"|"off", ...}
     Train with the loss on `completion` only. Reasoning is kept on the completion, and on earlier
     assistant turns only if they belong to the current user turn (that is what the Qwen-style
     templates replay at inference); use --history-reasoning keep if your app replays all of it.
  4. assigns train/val/test by group_id, so variants of one lesson (EN/AF twins, strategy variants)
     never straddle splits
  5. writes train.jsonl, val.jsonl, test.jsonl, manifest.jsonl, build_summary.json

Turning prompt/completion into token ids with the base model's chat template is deliberately NOT done
here: it depends on which base model you pick. `thinking: "off"` samples should be rendered with
thinking disabled in the template; "on" samples with it enabled.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import board as boardmod

SCHEMA_VERSION = "tutor-v1"
RENDER_VERSION = 2   # bump when SYSTEM_BASE or the rendering rules change, then rebuild everything

# --------------------------------------------------------------------------- #
# Vocabulary (keep in sync with tutor_spec.md section 6)
# --------------------------------------------------------------------------- #
SUBJECTS = {  # subject -> (lowest grade, highest grade) in CAPS
    "mathematics": (7, 12),
    "mathematical_literacy": (10, 12),
    "natural_sciences": (7, 9),
    "physical_sciences": (10, 12),
    "life_sciences": (10, 12),
    "english": (7, 12),
    "afrikaans": (7, 12),
}
SUBJECT_LABEL = {
    "mathematics": "Mathematics",
    "mathematical_literacy": "Mathematical Literacy",
    "natural_sciences": "Natural Sciences",
    "physical_sciences": "Physical Sciences",
    "life_sciences": "Life Sciences",
    "english": "English",
    "afrikaans": "Afrikaans",
}
LANGUAGE_SUBJECTS = {"english", "afrikaans"}
NEEDS_MATH_FORMAT = {"mathematics", "mathematical_literacy", "natural_sciences", "physical_sciences"}
CHECKABLE = NEEDS_MATH_FORMAT          # answers can be verified in code / against a memo
TRACKS = {"HL": "Home Language", "FAL": "First Additional Language"}
LANGS = {"en": "English", "af": "Afrikaans"}
RESPONSE_LANGS = {"en", "af", "mirror"}
STUDENT_LANGS = {"en", "af", "mixed"}

STRATEGY_TEXT = {
    "auto": "choose the method that fits the learner and the topic",
    "worked_example": "show a short worked example, then let the learner try a similar one",
    "faded_example": "work an example together, leaving more steps for the learner each time",
    "socratic_hints": "lead with questions and small hints",
    "analogy_real_world": "explain with an accurate everyday South African analogy and say where it stops working",
    "mnemonic": "give a correct, easy-to-remember memory aid (acronym, rhyme, story or chunking) that never changes the answer",
    "concrete_to_abstract": "start with a concrete case or picture, then move to the general rule",
    "retrieval_quiz": "quiz the learner with short recall questions",
    "error_analysis": "have the learner find and fix a mistake",
    "self_explanation": "ask the learner to explain the step in their own words",
    "gamified_challenge": "turn practice into a short challenge with small goals",
    "direct_explanation": "explain briefly and directly",
    "spaced_recap": "revisit earlier topics with a quick recap and recall questions",
    "exam_technique": "coach how to answer for marks and manage time",
    "step_walkthrough": "walk the learner through the question one step at a time, giving the reason for each step",
    "reframe": "offer a different way to look at the problem (simpler numbers, a picture, working backwards, own words)",
    "think_aloud": "say how an expert thinks about this kind of problem, then let the learner copy that thinking",
    "answer_structure": "show how to lay out the answer and what to write to earn the marks",
    "visual_board": "teach by drawing on the blackboard and pointing at the parts that matter",
    "story_context": "wrap the practice in a short, relatable South African scenario",
}
STRATEGIES = set(STRATEGY_TEXT)
POLICY_TEXT = {
    "hint_only": "give hints only and never state the final answer",
    "guided": "guide step by step with questions; reveal the answer only after the learner has tried",
    "full_solution": "give a complete worked solution with a reason for each step",
}
LEVELS = {"struggling", "on_track", "advanced"}
TONE_TEXT = {
    "friendly_playful": "friendly and playful",
    "calm_neutral": "calm and neutral",
    "encouraging": "warm and encouraging",
    "concise_direct": "concise and direct",
}
LENGTH_WORDS = {"short": 90, "medium": 220, "long": 450}
LENGTH_TEXT = {
    "short": "short (under 90 words)",
    "medium": "medium (under 220 words)",
    "long": "long (up to 450 words)",
}
MATH_TEXT = {"latex": "LaTeX with $...$", "plain": "plain text with Unicode symbols, no LaTeX"}


def _tool(name, description, props, required):
    return {"type": "function", "function": {
        "name": name, "description": description,
        "parameters": {"type": "object", "properties": props, "required": required}}}


# Edit these so they match the tools your app really exposes. Training and app must agree exactly.
TOOL_REGISTRY = {
    "calculator": _tool(
        "calculator", "Evaluate an arithmetic expression exactly. Use it for any non-trivial arithmetic.",
        {"expression": {"type": "string", "description": "e.g. 12.5*8 - 3/4"}}, ["expression"]),
    "plot_function": _tool(
        "plot_function", "Plot y = f(x); returns an image id plus key features (intercepts, vertex).",
        {"expression": {"type": "string", "description": "e.g. x^2 - 4*x + 3"},
         "x_min": {"type": "number"}, "x_max": {"type": "number"}}, ["expression"]),
    "make_cover_page": _tool(
        "make_cover_page", "Create a printable cover page (PDF).",
        {"title": {"type": "string"}, "subject": {"type": "string"}, "grade": {"type": "integer"}}, ["title"]),
    "search_curriculum": _tool(
        "search_curriculum", "Search CAPS documents and textbook passages.",
        {"query": {"type": "string"}, "subject": {"type": "string"}, "grade": {"type": "integer"},
         "language": {"type": "string", "enum": ["en", "af"]}}, ["query"]),
    "web_search": _tool(
        "web_search", "Search the web for current information.",
        {"query": {"type": "string"}}, ["query"]),
    "board": _tool(
        "board", "Draw on the learner's blackboard (grid: columns A-L, rows 1-30). One command per string, for example "
                 'write A1 "text", write next "text", arrow A1 -> A3 "label", underline C10-C13, highlight B2, '
                 "box B2, circle B2, erase B2, erase all.",
        {"commands": {"type": "array", "items": {"type": "string"}, "description": "board commands, in order"}},
        ["commands"]),
}

SOURCE_TYPES = {"past_paper_adapted", "textbook_adapted", "teacher_written", "synthetic_from_source",
                "synthetic_free", "illustrative_example"}
TASK_TYPES = {"solve_problem", "explain_concept", "check_my_work", "practice_request", "revision_summary",
              "language_help", "essay_feedback", "comprehension", "exam_technique", "do_my_work",
              "off_topic", "unsure_curriculum", "photo_problem"}
STUDENT_STATES = {"lost", "confused", "bored", "frustrated", "almost_there", "confident", "rushing",
                  "asking_for_answer", "off_task", "unknown"}
COGNITIVE_LEVELS = {"knowledge", "routine", "complex", "problem_solving"}
SPLITS = {"train", "val", "test", "eval_only", "exclude", "auto"}
# Named teaching techniques (tutor_spec.md section 4). meta.techniques lists the ones a record uses,
# so `report` can show whether the model sees enough of each (e.g. bar models, PEEL, CUBES).
TECHNIQUES = {
    # maths
    "bar_model", "number_line", "area_model", "balance_scale", "cpa", "bodmas", "factor_tree", "soh_cah_toa",
    "cubes", "polya_four_steps", "work_backwards", "estimate_first", "check_by_substitution", "units_check",
    "table_of_values", "draw_a_diagram", "try_simple_numbers", "given_formula_substitute_answer",
    # science
    "predict_observe_explain", "particle_diagram", "energy_chain", "concept_map", "units_conversion",
    # english / afrikaans
    "sq3r", "qar", "peel", "teel", "annotate_text", "five_ws", "skim_and_scan", "context_clues",
    "paraphrase_then_answer", "mark_per_point", "command_word_decode", "plan_write_check",
    # memory (any subject)
    "acronym", "rhyme", "story_chain", "memory_palace", "chunking", "retrieval_practice", "spaced_review",
    "dual_coding", "interleaving", "teach_it_back", "flashcards",
}
VERIFICATION_METHODS = {"sympy_vs_memo", "code_exec", "human", "none"}

REQUIRED_CONTROL = ["subject", "grade", "subject_language", "response_language", "strategy",
                    "answer_policy", "student_level", "tone", "response_length", "tools"]
KNOWN_CONTROL = set(REQUIRED_CONTROL) | {"language_track", "math_format", "learner_context"}
REQUIRED_META = ["topic", "task_type", "student_language", "strategy_used", "source_type",
                 "source_licence", "generator", "answer_verified", "split"]
KNOWN_META = set(REQUIRED_META) | {
    "subtopic", "caps_ref", "cognitive_level", "difficulty", "misconception_targeted", "student_state",
    "final_answer", "verification_method", "human_reviewed", "language_reviewed_by_speaker",
    "teacher_reviewed", "judge_scores", "attribution", "source_ref", "notes", "created",
    "techniques", "verify_code", "item_id", "mode", "tool_results_unverified", "judge_notes", "review_notes",
    "image_kind", "teacher_final_answer"}
KNOWN_TOP = {"schema_version", "id", "group_id", "control", "thinking", "messages", "meta"}
CONTEXT_KEYS = {"recent_topics", "weak_topics", "days_since_last_session"}
PII_KEYS = {"name", "surname", "first_name", "last_name", "school", "email", "phone", "address", "id_number"}

SYSTEM_BASE = ("You are a patient, encouraging South African school tutor (CAPS, Grades 7-12). "
               "You teach so that the learner can do the next problem alone.")

# --------------------------------------------------------------------------- #
# Small helpers
# --------------------------------------------------------------------------- #
_AF = set("die nie ons jy jou hoe wat het dit vir kom ook maar nou dan sal moet daar hier dus eers baie goed "
          "'n van om te kan".split())
_EN = set("the and you your we this that with for can will now then are what how it to of lets let's first "
          "next not".split())

PII_PATTERNS = [
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"), "email address"),
    (re.compile(r"(?<!\d)(?:\+27|0)[6-8]\d{8}(?!\d)"), "phone number"),
    (re.compile(r"(?<!\d)\d{13}(?!\d)"), "13-digit number (SA ID?)"),
]


def words(s):
    return len(s.split())


def strip_math(s):
    return re.sub(r"\$\$.*?\$\$|\$[^$\n]*\$", " ", s, flags=re.S)


def guess_lang(text):
    """Very rough en/af detector from function words. Returns 'en', 'af', 'mixed' or 'unknown'."""
    t = strip_math(text).replace("\u2019", "'").lower()
    toks = re.findall(r"[a-z']+", t)
    af = sum(1 for w in toks if w in _AF)
    en = sum(1 for w in toks if w in _EN)
    if af + en < 3:
        return "unknown"
    r = af / (af + en)
    return "af" if r >= 0.75 else "en" if r <= 0.25 else "mixed"


def norm_answer(s):
    return re.sub(r"[\s$\\{}]", "", s.lower())


IMAGES_ROOT = None      # set by --images-root: image paths in records are then checked to exist


def text_of(content):
    """Text of a message: a plain string, or the text parts of a list-of-parts (vision) message."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return " ".join(p.get("text", "") for p in content if isinstance(p, dict) and p.get("type") == "text")
    return ""


def has_image(content):
    return isinstance(content, list) and any(isinstance(p, dict) and p.get("type") == "image" for p in content)


def check_user_content(content, where, iss):
    """User content is a string, or a list of {"type":"text","text":...} / {"type":"image","path":...} parts."""
    if isinstance(content, str):
        if not content.strip():
            iss.err(f"{where}: user content must not be empty")
        return
    if not isinstance(content, list) or not content:
        iss.err(f"{where}: user content must be a string or a non-empty list of parts")
        return
    n_text = 0
    for k, part in enumerate(content):
        w = f"{where}.content[{k}]"
        if not isinstance(part, dict) or part.get("type") not in ("text", "image"):
            iss.err(f"{w}: each part must be an object with type 'text' or 'image'")
        elif part["type"] == "text":
            if isinstance(part.get("text"), str) and part["text"].strip():
                n_text += 1
            else:
                iss.err(f"{w}: text part needs non-empty 'text'")
        else:
            path = part.get("path")
            if not isinstance(path, str) or not path.strip():
                iss.err(f"{w}: image part needs a 'path'")
            elif IMAGES_ROOT is not None and not (Path(IMAGES_ROOT) / path).exists():
                iss.err(f"{w}: image file not found: {Path(IMAGES_ROOT) / path}")
    if n_text == 0:
        iss.err(f"{where}: a message with an image also needs some text (even just the question)")


def ctrl_of(rec):
    c = rec.get("control")
    return c if isinstance(c, dict) else {}


def meta_of(rec):
    m = rec.get("meta")
    return m if isinstance(m, dict) else {}


def msgs_of(rec):
    m = rec.get("messages")
    return [x for x in m if isinstance(x, dict)] if isinstance(m, list) else []


def lang_of(rec):
    """Language the tutor actually replies in (mirror resolved from meta.student_language)."""
    rl = ctrl_of(rec).get("response_language")
    if rl == "mirror":
        return meta_of(rec).get("student_language") or "?"
    return rl or "?"


class Issues:
    def __init__(self):
        self.items = []

    def err(self, msg):
        self.items.append(("ERROR", msg))

    def warn(self, msg):
        self.items.append(("WARN", msg))


def need_in(iss, where, value, allowed):
    if value not in allowed:
        iss.err(f"{where}: {value!r} is not one of {sorted(allowed, key=str)}")
        return False
    return True


# --------------------------------------------------------------------------- #
# Record checks
# --------------------------------------------------------------------------- #
def check_tool_calls(calls, allowed, where, iss, board_state=None):
    if not isinstance(calls, list) or not calls:
        iss.err(f"{where}.tool_calls must be a non-empty list")
        return
    for k, tc in enumerate(calls):
        w = f"{where}.tool_calls[{k}]"
        fn = tc.get("function") if isinstance(tc, dict) else None
        if not isinstance(fn, dict):
            iss.err(f"{w}.function is missing")
            continue
        name = fn.get("name")
        if name not in TOOL_REGISTRY:
            iss.err(f"{w}: unknown tool {name!r} (known: {sorted(TOOL_REGISTRY)})")
            continue
        if name not in allowed:
            iss.err(f"{w}: tool {name!r} is not listed in control.tools")
        args = fn.get("arguments")
        if isinstance(args, str):
            try:
                args = json.loads(args)
            except json.JSONDecodeError:
                iss.err(f"{w}.arguments is not valid JSON")
                continue
        if not isinstance(args, dict):
            iss.err(f"{w}.arguments must be an object")
            continue
        schema = TOOL_REGISTRY[name]["function"]["parameters"]
        for req in schema["required"]:
            if req not in args:
                iss.err(f"{w}.arguments is missing required {req!r}")
        for key in args:
            if key not in schema["properties"]:
                iss.warn(f"{w}.arguments has unexpected key {key!r}")
        if name == "board" and "commands" in args:
            errs, warns = boardmod.check_commands(args["commands"], board_state)
            for e in errs:
                iss.err(f"{w}: board {e}")
            for wn in warns:
                iss.warn(f"{w}: board {wn}")


def check_messages(rec, iss):
    msgs = rec.get("messages")
    thinking = rec.get("thinking")
    ctrl = ctrl_of(rec)
    allowed = set(ctrl["tools"]) if isinstance(ctrl.get("tools"), list) else set()
    if not isinstance(msgs, list) or not msgs:
        iss.err("messages must be a non-empty list")
        return
    prev, pending = None, 0
    last = None
    board_state = boardmod.Board()          # the blackboard persists across tool calls in one record
    for i, m in enumerate(msgs):
        where = f"messages[{i}]"
        if not isinstance(m, dict):
            iss.err(f"{where} must be an object")
            return
        role, content = m.get("role"), m.get("content")
        last = m
        if role == "system":
            iss.err(f"{where}: do not store a system message; it is rendered from control")
            continue
        if not need_in(iss, f"{where}.role", role, {"user", "assistant", "tool"}):
            continue
        # ordering
        if role == "user":
            if prev is not None and (prev != "assistant" or pending):
                iss.err(f"{where}: a user message can only follow a finished assistant reply")
            check_user_content(content, where, iss)
        elif role == "assistant":
            if prev not in ("user", "tool") or pending:
                iss.err(f"{where}: an assistant message must follow a user message or its tool results")
            calls = m.get("tool_calls")
            if calls:
                check_tool_calls(calls, allowed, where, iss, board_state)
                pending = len(calls) if isinstance(calls, list) else 0
                if content is not None and not isinstance(content, str):
                    iss.err(f"{where}.content must be a string")
            else:
                if not isinstance(content, str) or not content.strip():
                    iss.err(f"{where}: assistant content must be a non-empty string")
            reasoning = m.get("reasoning")
            if thinking == "on":
                if not isinstance(reasoning, str) or not reasoning.strip():
                    iss.err(f"{where}: thinking is 'on' so every assistant message needs 'reasoning'")
            elif thinking == "off":
                if reasoning:
                    iss.err(f"{where}: thinking is 'off' so assistant messages must not have 'reasoning'")
            for field in ("content", "reasoning"):
                t = m.get(field)
                if isinstance(t, str) and re.search(r"</?think>", t):
                    iss.err(f"{where}.{field}: do not write <think> tags; use the 'reasoning' field")
        elif role == "tool":
            if pending <= 0:
                iss.err(f"{where}: tool message without a pending tool call")
            else:
                pending -= 1
            if not isinstance(content, str) or not content.strip():
                iss.err(f"{where}: tool content must be a non-empty string")
        prev = role
    if isinstance(last, dict):
        if last.get("role") != "assistant" or last.get("tool_calls") or not last.get("content"):
            iss.err("the last message must be a plain assistant reply (no tool call)")
    if pending:
        iss.err("a tool call has no tool result")
    if isinstance(msgs[0], dict) and msgs[0].get("role") != "user":
        iss.err("the conversation must start with a user message")


def check_control(rec, iss):
    c = rec.get("control")
    if not isinstance(c, dict):
        iss.err("control must be an object")
        return
    for k in REQUIRED_CONTROL:
        if k not in c:
            iss.err(f"control.{k} is required")
    for k in c:
        if k not in KNOWN_CONTROL:
            iss.warn(f"control.{k} is not a known field (build will ignore it)")
    subj = c.get("subject")
    if need_in(iss, "control.subject", subj, set(SUBJECTS)):
        lo, hi = SUBJECTS[subj]
        g = c.get("grade")
        if not isinstance(g, int) or isinstance(g, bool) or not lo <= g <= hi:
            iss.err(f"control.grade: {g!r} is outside Grades {lo}-{hi} for {subj}")
        if subj in LANGUAGE_SUBJECTS:
            if c.get("language_track") not in TRACKS:
                iss.err("control.language_track must be 'HL' or 'FAL' for english/afrikaans")
        elif c.get("language_track") is not None:
            iss.err("control.language_track is only for english/afrikaans")
        if subj in NEEDS_MATH_FORMAT:
            if c.get("math_format") not in MATH_TEXT:
                iss.err("control.math_format ('latex' or 'plain') is required for maths and science subjects")
        elif c.get("math_format") not in (None, *MATH_TEXT):
            iss.err("control.math_format must be 'latex' or 'plain'")
    if "subject_language" in c:
        need_in(iss, "control.subject_language", c["subject_language"], set(LANGS))
    if "response_language" in c:
        need_in(iss, "control.response_language", c["response_language"], RESPONSE_LANGS)
    if "strategy" in c:
        need_in(iss, "control.strategy", c["strategy"], STRATEGIES)
    if "answer_policy" in c:
        need_in(iss, "control.answer_policy", c["answer_policy"], set(POLICY_TEXT))
    if "student_level" in c:
        need_in(iss, "control.student_level", c["student_level"], LEVELS)
    if "tone" in c:
        need_in(iss, "control.tone", c["tone"], set(TONE_TEXT))
    if "response_length" in c:
        need_in(iss, "control.response_length", c["response_length"], set(LENGTH_WORDS))
    tools = c.get("tools")
    if "tools" in c:
        if not isinstance(tools, list):
            iss.err("control.tools must be a list (use [] for none)")
        else:
            for t in tools:
                if t not in TOOL_REGISTRY:
                    iss.err(f"control.tools: unknown tool {t!r} (known: {sorted(TOOL_REGISTRY)})")
    ctx = c.get("learner_context")
    if ctx is not None:
        if not isinstance(ctx, dict):
            iss.err("control.learner_context must be an object")
        else:
            for k, v in ctx.items():
                if k in PII_KEYS:
                    iss.err(f"control.learner_context.{k}: no personal data about learners in training data")
                elif k not in CONTEXT_KEYS:
                    iss.warn(f"control.learner_context.{k} is not a known key {sorted(CONTEXT_KEYS)}")
            for k in ("recent_topics", "weak_topics"):
                if k in ctx and not (isinstance(ctx[k], list) and all(isinstance(x, str) for x in ctx[k])):
                    iss.err(f"control.learner_context.{k} must be a list of strings")
            d = ctx.get("days_since_last_session")
            if d is not None and (not isinstance(d, int) or isinstance(d, bool) or d < 0):
                iss.err("control.learner_context.days_since_last_session must be a non-negative integer")


def check_meta(rec, iss):
    m = rec.get("meta")
    if not isinstance(m, dict):
        iss.err("meta must be an object")
        return
    c = ctrl_of(rec)
    for k in REQUIRED_META:
        if k not in m:
            iss.err(f"meta.{k} is required")
    for k in m:
        if k not in KNOWN_META:
            iss.warn(f"meta.{k} is not a known field")
    for k in ("topic", "source_licence", "generator"):
        if k in m and (not isinstance(m[k], str) or not m[k].strip()):
            iss.err(f"meta.{k} must be a non-empty string")
    if "task_type" in m:
        need_in(iss, "meta.task_type", m["task_type"], TASK_TYPES)
    if "student_language" in m:
        need_in(iss, "meta.student_language", m["student_language"], STUDENT_LANGS)
    if "strategy_used" in m:
        if need_in(iss, "meta.strategy_used", m["strategy_used"], STRATEGIES - {"auto"}):
            cs = c.get("strategy")
            if cs not in (None, "auto") and m["strategy_used"] != cs:
                iss.err(f"meta.strategy_used {m['strategy_used']!r} must equal control.strategy {cs!r}")
    if "source_type" in m:
        need_in(iss, "meta.source_type", m["source_type"], SOURCE_TYPES)
    if "split" in m:
        need_in(iss, "meta.split", m["split"], SPLITS)
    if "answer_verified" in m and not isinstance(m["answer_verified"], bool):
        iss.err("meta.answer_verified must be true or false")
    if m.get("student_state") is not None:
        need_in(iss, "meta.student_state", m["student_state"], STUDENT_STATES)
    if m.get("cognitive_level") is not None:
        need_in(iss, "meta.cognitive_level", m["cognitive_level"], COGNITIVE_LEVELS)
    if m.get("verification_method") is not None:
        need_in(iss, "meta.verification_method", m["verification_method"], VERIFICATION_METHODS)
    d = m.get("difficulty")
    if d is not None and (not isinstance(d, int) or isinstance(d, bool) or not 1 <= d <= 5):
        iss.err("meta.difficulty must be an integer 1-5")
    for k in ("human_reviewed", "language_reviewed_by_speaker", "teacher_reviewed"):
        if k in m and not isinstance(m[k], bool):
            iss.err(f"meta.{k} must be true or false")
    if "techniques" in m:
        if not (isinstance(m["techniques"], list) and all(isinstance(t, str) for t in m["techniques"])):
            iss.err("meta.techniques must be a list of strings")
        else:
            for t in m["techniques"]:
                if t not in TECHNIQUES:
                    iss.warn(f"meta.techniques: {t!r} is not in the catalogue (add it to TECHNIQUES or fix the name)")
    msgs_ = rec.get("messages") if isinstance(rec.get("messages"), list) else []
    if any(isinstance(x, dict) and has_image(x.get("content")) for x in msgs_) and m.get("task_type") != "photo_problem":
        iss.warn("a message has an image but meta.task_type is not 'photo_problem'")
    if m.get("source_type") == "illustrative_example" and m.get("split") != "exclude":
        iss.err("illustrative_example records must have split 'exclude' (never train on them)")
    subj = c.get("subject")
    if m.get("split") in ("train", "auto") and subj in CHECKABLE and m.get("answer_verified") is False:
        iss.err("maths/science records with answer_verified=false must not go into train (set split to 'exclude')")
    if m.get("answer_verified") is True and subj in CHECKABLE \
            and m.get("verification_method") in (None, "none"):
        iss.warn("answer_verified is true but meta.verification_method is missing or 'none'")


def check_heuristics(rec, iss, strict):
    c, m, msgs = ctrl_of(rec), meta_of(rec), msgs_of(rec)
    subj = c.get("subject")

    # personal data
    for i, msg in enumerate(msgs):
        for field in ("content", "reasoning"):
            t = msg.get(field)
            if isinstance(t, str):
                for rx, label in PII_PATTERNS:
                    if rx.search(t):
                        iss.warn(f"messages[{i}].{field}: possible personal data ({label})")

    # language
    if subj not in LANGUAGE_SUBJECTS:
        rl = c.get("response_language")
        expected = m.get("student_language") if rl == "mirror" else rl
        if expected in ("en", "af"):
            for i, msg in enumerate(msgs):
                if msg.get("role") == "assistant" and isinstance(msg.get("content"), str):
                    g = guess_lang(msg["content"])
                    if g in ("en", "af") and g != expected:
                        iss.warn(f"messages[{i}]: reply looks {g} but the expected reply language is {expected}")
    first_user = next((x for x in msgs if x.get("role") == "user"), None)
    if first_user and m.get("student_language") in ("en", "af") and text_of(first_user.get("content")):
        g = guess_lang(text_of(first_user["content"]))
        if g in ("en", "af") and g != m["student_language"]:
            iss.warn(f"first user message looks {g} but meta.student_language is {m['student_language']}")
    if rec.get("thinking") == "on":
        for i, msg in enumerate(msgs):
            r = msg.get("reasoning")
            if isinstance(r, str) and guess_lang(r) == "af":
                iss.warn(f"messages[{i}].reasoning looks Afrikaans (reasoning is English by default)")

    # length of the last reply
    final = msgs[-1] if msgs else {}
    cap = LENGTH_WORDS.get(c.get("response_length"))
    if cap and final.get("role") == "assistant" and isinstance(final.get("content"), str):
        n = words(final["content"])
        if n > cap:
            iss.warn(f"last reply is {n} words but response_length '{c['response_length']}' allows {cap}")

    # maths notation
    fmt = c.get("math_format")
    for i, msg in enumerate(msgs):
        t = msg.get("content")
        if msg.get("role") != "assistant" or not isinstance(t, str):
            continue
        if fmt == "latex":
            if t.count("$") % 2:
                iss.warn(f"messages[{i}]: unbalanced '$' (breaks LaTeX rendering)")
            if re.search(r"[\u00b2\u00b3\u2074-\u2079\u221a]", strip_math(t)):
                iss.warn(f"messages[{i}]: Unicode superscript/root outside $...$ but math_format is latex")
        elif fmt == "plain":
            if "$" in t or re.search(r"\\(frac|sqrt|cdot|times|left|right|\(|\[)", t):
                iss.warn(f"messages[{i}]: LaTeX found but math_format is plain")

    # tool results: compare with what the real tool returns (needs SymPy; skipped if unavailable)
    try:
        import tools_sim
        fixed, _ = tools_sim.fill_tool_results(rec)
        for i, (old, new) in enumerate(zip(msgs, fixed["messages"])):
            if old.get("role") == "tool" and old.get("content") != new.get("content"):
                iss.warn(f"messages[{i}]: tool result differs from the real tool output "
                         f"(pipeline/verify.py rewrites it): real = {str(new.get('content'))[:80]!r}")
    except ImportError:
        pass

    # answer leak (heuristic)
    fa, pol = m.get("final_answer"), c.get("answer_policy")
    if isinstance(fa, str) and pol in ("hint_only", "guided"):
        a = norm_answer(fa)
        if len(a) >= 3:
            replies = [x for x in msgs if x.get("role") == "assistant" and isinstance(x.get("content"), str)]
            scope = replies if pol == "hint_only" else replies[:1]
            for x in scope:
                if a in norm_answer(x["content"]):
                    where = "a reply" if pol == "hint_only" else "the first reply"
                    iss.warn(f"possible answer leak: meta.final_answer appears in {where} (policy {pol})")
                    break

    if strict:
        if (lang_of(rec) in ("af", "mixed") or subj == "afrikaans") and not m.get("language_reviewed_by_speaker"):
            iss.warn("Afrikaans content not marked language_reviewed_by_speaker (strict)")


def check_record(rec, iss, strict=False):
    for k in rec:
        if k not in KNOWN_TOP:
            iss.warn(f"unknown top-level key {k!r}")
    if rec.get("schema_version", SCHEMA_VERSION) != SCHEMA_VERSION:
        iss.err(f"schema_version must be {SCHEMA_VERSION!r}")
    for k in ("id", "group_id"):
        if not isinstance(rec.get(k), str) or not rec[k].strip():
            iss.err(f"{k} must be a non-empty string")
    need_in(iss, "thinking", rec.get("thinking"), {"on", "off"})
    check_control(rec, iss)
    check_meta(rec, iss)
    check_messages(rec, iss)
    if not any(level == "ERROR" for level, _ in iss.items):
        check_heuristics(rec, iss, strict)


# --------------------------------------------------------------------------- #
# File-level validation
# --------------------------------------------------------------------------- #
def load(path):
    items = []
    with open(path, encoding="utf-8") as f:
        content = f.read()

    # Fast path: standard single-line JSONL
    lines = content.splitlines()
    line_by_line_ok = True
    temp_items = []
    for n, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
            if not isinstance(rec, dict):
                line_by_line_ok = False
                break
            temp_items.append({"line": n, "rec": rec, "issues": []})
        except json.JSONDecodeError:
            line_by_line_ok = False
            break

    if line_by_line_ok and temp_items:
        return temp_items

    # Multi-line / array fallback for beautified JSON or JSONL
    stripped = content.strip()
    if stripped.startswith("[") and stripped.endswith("]"):
        try:
            arr = json.loads(stripped)
            if isinstance(arr, list):
                for idx, r in enumerate(arr, 1):
                    if isinstance(r, dict):
                        items.append({"line": idx, "rec": r, "issues": []})
                    else:
                        items.append({"line": idx, "rec": None, "issues": [("ERROR", "item must be a JSON object")]})
                return items
        except json.JSONDecodeError:
            pass

    dec = json.JSONDecoder()
    idx = 0
    rec_num = 1
    length = len(content)
    while idx < length:
        while idx < length and content[idx].isspace():
            idx += 1
        if idx >= length:
            break
        if content[idx] == ",":
            idx += 1
            while idx < length and content[idx].isspace():
                idx += 1
            if idx >= length:
                break
        try:
            rec, end = dec.raw_decode(content[idx:])
            idx += end
            if isinstance(rec, dict):
                items.append({"line": rec_num, "rec": rec, "issues": []})
            else:
                items.append({"line": rec_num, "rec": None, "issues": [("ERROR", "each item must be a JSON object")]})
            rec_num += 1
        except json.JSONDecodeError as e:
            items.append({"line": rec_num, "rec": None, "issues": [("ERROR", f"invalid JSON: {e}")]})
            break

    return items if items else temp_items


def resolve_split(rec, val, test, seed):
    s = meta_of(rec).get("split", "auto")
    if s != "auto":
        return s
    return auto_split(rec, val, test, seed)


def auto_split(rec, val, test, seed):
    h = int(hashlib.sha1(f"{seed}:{rec.get('group_id')}".encode()).hexdigest()[:8], 16) / 0xFFFFFFFF
    if h < test:
        return "test"
    if h < test + val:
        return "val"
    return "train"


def validate_all(items, strict=False):
    seen_ids, seen_dups = {}, {}
    group_splits = defaultdict(lambda: defaultdict(list))
    for it in items:
        rec = it["rec"]
        if rec is None:
            continue
        iss = Issues()
        check_record(rec, iss, strict)
        it["issues"].extend(iss.items)
        rid = rec.get("id")
        if isinstance(rid, str):
            if rid in seen_ids:
                it["issues"].append(("ERROR", f"duplicate id (also on line {seen_ids[rid]})"))
            else:
                seen_ids[rid] = it["line"]
        first_user = next((x for x in msgs_of(rec) if x.get("role") == "user"), None)
        if first_user and text_of(first_user.get("content")):
            c = ctrl_of(rec)
            key = (re.sub(r"\s+", " ", text_of(first_user["content"]).strip().lower()), c.get("subject"), c.get("grade"),
                   c.get("response_language"), c.get("strategy"))
            if key in seen_dups:
                it["issues"].append(("WARN", f"same first user message, subject, grade, language and strategy "
                                             f"as line {seen_dups[key]}"))
            else:
                seen_dups[key] = it["line"]
        s = meta_of(rec).get("split")
        if s in SPLITS and s not in ("auto", "exclude", "eval_only") and isinstance(rec.get("group_id"), str):
            group_splits[rec["group_id"]][s].append(it)
    for gid, by_split in group_splits.items():
        if len(by_split) > 1:
            names = sorted(by_split)
            for lst in by_split.values():
                for it in lst:
                    it["issues"].append(("ERROR", f"group_id {gid!r} is spread over splits {names}; "
                                                  f"variants of one lesson must share a split"))
    # auto records share a split by construction (hash of group_id), explicit ones were checked above


def print_issues(items):
    for it in items:
        rid = it["rec"].get("id") if it["rec"] else "?"
        for level, msg in it["issues"]:
            print(f"line {it['line']} [{rid}] {level}: {msg}")


def counts(items):
    n_err = sum(1 for it in items for lv, _ in it["issues"] if lv == "ERROR")
    n_warn = sum(1 for it in items for lv, _ in it["issues"] if lv == "WARN")
    return n_err, n_warn


def cmd_validate(args):
    items = load(args.file)
    validate_all(items, args.strict)
    print_issues(items)
    n_err, n_warn = counts(items)
    print(f"\nChecked {len(items)} records: {n_err} errors, {n_warn} warnings.")
    if n_err or (args.strict and n_warn):
        return 1
    return 0


# --------------------------------------------------------------------------- #
# Report
# --------------------------------------------------------------------------- #
def table(headers, rows):
    rows = [[str(x) for x in r] for r in rows]
    widths = [len(h) for h in headers]
    for r in rows:
        for i, x in enumerate(r):
            widths[i] = max(widths[i], len(x))
    out = ["  ".join(h.ljust(widths[i]) for i, h in enumerate(headers)),
           "  ".join("-" * w for w in widths)]
    out += ["  ".join(x.ljust(widths[i]) for i, x in enumerate(r)) for r in rows]
    return "\n".join(out)


def dist(title, counter, total):
    print(f"\n{title}")
    rows = [(k, n, f"{100 * n / total:.1f}%") for k, n in sorted(counter.items(), key=lambda kv: (-kv[1], str(kv[0])))]
    print(table(["value", "n", "share"], rows))


def matrix(title, row_keys, col_keys, count, valid=None, min_cell=None):
    print(f"\n{title}" + (f"   (* = fewer than {min_cell})" if min_cell else ""))
    rows = []
    for rk in row_keys:
        row = [rk]
        for ck in col_keys:
            if valid and not valid(rk, ck):
                row.append("n/a")
                continue
            n = count.get((rk, ck), 0)
            row.append(f"{n}*" if (min_cell and n < min_cell) else str(n))
        rows.append(row)
    print(table([""] + [str(c) for c in col_keys], rows))


def cmd_report(args):
    items = load(args.file)
    recs = [it["rec"] for it in items if it["rec"] is not None]
    bad = len(items) - len(recs)
    if not recs:
        print("no readable records")
        return 1
    total = len(recs)
    asst = sum(1 for r in recs for x in msgs_of(r) if x.get("role") == "assistant")
    groups = {r.get("group_id") for r in recs}
    think_on = sum(1 for r in recs if r.get("thinking") == "on")
    tool_recs = sum(1 for r in recs if any(x.get("tool_calls") for x in msgs_of(r)))
    auto = sum(1 for r in recs if ctrl_of(r).get("strategy") == "auto")
    print(f"records: {total}" + (f"  (+{bad} unreadable lines)" if bad else ""))
    print(f"groups (lessons): {len(groups)}   assistant turns: {asst} ({asst / total:.1f} per record)")
    print(f"thinking on: {think_on} ({100 * think_on / total:.0f}%)   records with tool calls: {tool_recs}   "
          f"strategy 'auto': {auto}")

    dist("subject", Counter(ctrl_of(r).get("subject") for r in recs), total)
    dist("grade", Counter(ctrl_of(r).get("grade") for r in recs), total)
    dist("reply language", Counter(lang_of(r) for r in recs), total)
    dist("student language", Counter(meta_of(r).get("student_language") for r in recs), total)
    dist("strategy used", Counter(meta_of(r).get("strategy_used") for r in recs), total)
    dist("answer policy", Counter(ctrl_of(r).get("answer_policy") for r in recs), total)
    dist("student level", Counter(ctrl_of(r).get("student_level") for r in recs), total)
    dist("task type", Counter(meta_of(r).get("task_type") for r in recs), total)
    dist("student state", Counter(meta_of(r).get("student_state") for r in recs), total)
    dist("source type", Counter(meta_of(r).get("source_type") for r in recs), total)
    techs = Counter(t for r in recs for t in (meta_of(r).get("techniques") or []))
    if techs:
        dist("techniques used (records)", techs, total)
    n_img = sum(1 for r in recs if any(has_image(x.get("content")) for x in msgs_of(r)))
    if n_img:
        print(f"\nrecords with images: {n_img}")
    dist("split", Counter(meta_of(r).get("split") for r in recs), total)

    grades = list(range(7, 13))
    by_sg = Counter((ctrl_of(r).get("subject"), ctrl_of(r).get("grade")) for r in recs)
    matrix("subject x grade", list(SUBJECTS), grades, by_sg,
           valid=lambda s, g: SUBJECTS[s][0] <= g <= SUBJECTS[s][1], min_cell=args.min_cell)

    by_sl = Counter((ctrl_of(r).get("subject"), lang_of(r)) for r in recs)
    print("\nsubject x reply language (Afrikaans share)")
    rows = []
    for s in SUBJECTS:
        en, af, mixed = by_sl.get((s, "en"), 0), by_sl.get((s, "af"), 0), by_sl.get((s, "mixed"), 0)
        n = en + af + mixed
        rows.append((s, en, af, mixed, f"{100 * af / n:.0f}%" if n else "-"))
    print(table(["subject", "en", "af", "mixed", "af share"], rows))

    by_ss = Counter((meta_of(r).get("strategy_used"), ctrl_of(r).get("subject")) for r in recs)
    matrix("strategy used x subject", sorted(STRATEGIES - {"auto"}), list(SUBJECTS), by_ss)

    by_group = defaultdict(set)
    for r in recs:
        by_group[r.get("group_id")].add(lang_of(r))
    twins = [g for g, ls in by_group.items() if {"en", "af"} <= ls]
    single = [g for g, ls in by_group.items() if not {"en", "af"} <= ls]
    print(f"\nEN/AF twins: {len(twins)} groups have both an English and an Afrikaans variant; "
          f"{len(single)} have one language only" + (f" (e.g. {', '.join(map(str, single[:5]))})" if single else ""))

    checkable = [r for r in recs if ctrl_of(r).get("subject") in CHECKABLE]
    ver = sum(1 for r in checkable if meta_of(r).get("answer_verified") is True)
    af_recs = [r for r in recs if lang_of(r) in ("af", "mixed") or ctrl_of(r).get("subject") == "afrikaans"]
    af_rev = sum(1 for r in af_recs if meta_of(r).get("language_reviewed_by_speaker") is True)
    hum = sum(1 for r in recs if meta_of(r).get("human_reviewed") is True)
    tea = sum(1 for r in recs if meta_of(r).get("teacher_reviewed") is True)
    print("\nquality coverage")
    print(f"  maths/science answers verified : {ver}/{len(checkable)}")
    print(f"  Afrikaans reviewed by a speaker: {af_rev}/{len(af_recs)}")
    print(f"  human reviewed                 : {hum}/{total}")
    print(f"  teacher reviewed               : {tea}/{total}")

    cells = Counter((ctrl_of(r).get("subject"), ctrl_of(r).get("grade"), lang_of(r)) for r in recs)
    present = {ctrl_of(r).get("subject") for r in recs}
    absent = [s for s in SUBJECTS if s not in present]
    if absent:
        print(f"\nsubjects with no records yet: {', '.join(absent)}")
    thin = []
    for s, (lo, hi) in SUBJECTS.items():
        if s not in present:
            continue
        for g in range(lo, hi + 1):
            for lg in ("en", "af"):
                n = cells.get((s, g, lg), 0)
                if n < args.min_cell:
                    thin.append((n, s, g, lg))
    thin.sort()
    print(f"\nthin cells (subject, grade, reply language) with fewer than {args.min_cell} records: {len(thin)}")
    for n, s, g, lg in thin[:40]:
        print(f"  {s:<22} Gr {g:<2} {lg}  {n}")
    if len(thin) > 40:
        print(f"  ... and {len(thin) - 40} more")
    return 0


# --------------------------------------------------------------------------- #
# Build
# --------------------------------------------------------------------------- #
OPTIONAL_RENDER = ["subject_language", "response_language", "student_level", "strategy", "answer_policy",
                   "tone", "response_length", "math_format", "learner_context"]


def render_context(ctx):
    parts = []
    if ctx.get("recent_topics"):
        parts.append("recently studied: " + ", ".join(ctx["recent_topics"]))
    if ctx.get("weak_topics"):
        parts.append("finds hard: " + ", ".join(ctx["weak_topics"]))
    if ctx.get("days_since_last_session") is not None:
        parts.append(f"last session {ctx['days_since_last_session']} days ago")
    return "Learner context: " + "; ".join(parts) + "." if parts else ""


def render_system(c, fields):
    """Deterministic system prompt from control. The app must build the same text at inference."""
    lines = [SYSTEM_BASE]
    subj = SUBJECT_LABEL[c["subject"]]
    if c.get("language_track"):
        subj += f" ({TRACKS[c['language_track']]})"
    lines.append(f"Subject: {subj}. Grade: {c['grade']}.")
    if "subject_language" in fields:
        lines.append(f"Material language: {LANGS[c['subject_language']]}.")
    if "response_language" in fields:
        rl = c["response_language"]
        lines.append("Reply in the language the learner writes in." if rl == "mirror" else f"Reply in {LANGS[rl]}.")
    if "student_level" in fields:
        lines.append(f"Learner level: {c['student_level'].replace('_', ' ')}.")
    if "strategy" in fields:
        lines.append(f"Teaching approach: {STRATEGY_TEXT[c['strategy']]}.")
    if "answer_policy" in fields:
        lines.append(f"Answer policy: {POLICY_TEXT[c['answer_policy']]}.")
    if "tone" in fields:
        lines.append(f"Tone: {TONE_TEXT[c['tone']]}.")
    if "response_length" in fields:
        lines.append(f"Length: {LENGTH_TEXT[c['response_length']]}.")
    if "math_format" in fields and c.get("math_format"):
        lines.append(f"Maths notation: {MATH_TEXT[c['math_format']]}.")
    if "learner_context" in fields and c.get("learner_context"):
        ctx = render_context(c["learner_context"])
        if ctx:
            lines.append(ctx)
    return "\n".join(lines)


def droppable(field, c, m):
    """A field may be left out of the prompt only if leaving it out cannot contradict the label."""
    v = c.get(field)
    if field == "response_language":
        return v == "mirror" or v == m.get("student_language")
    if field == "subject_language":
        return v == m.get("student_language")
    if field == "answer_policy":
        return v == "guided"
    if field == "response_length":
        return v == "short"
    if field == "math_format":
        return v == "latex"
    if field == "learner_context":
        return False
    return True    # student_level, strategy, tone: the model should learn to infer or choose these


def choose_fields(rec, rng, p_all, p_field, allowed):
    c, m = ctrl_of(rec), meta_of(rec)
    dropped_all = rng.random() < p_all
    chosen = set()
    for f in OPTIONAL_RENDER:
        r = rng.random()                       # always draw, so the stream does not depend on the data
        if f not in allowed or c.get(f) in (None, ""):
            continue
        if droppable(f, c, m) and (dropped_all or r < p_field):
            continue
        chosen.add(f)
    return chosen, dropped_all


def norm_call(tc):
    fn = tc["function"]
    args = fn.get("arguments")
    if isinstance(args, dict):
        args = json.dumps(args, ensure_ascii=False)
    out = {"type": "function", "function": {"name": fn["name"], "arguments": args}}
    if tc.get("id"):
        out["id"] = tc["id"]
    return out


def clean_msg(m, keep_reasoning):
    out = {"role": m["role"], "content": m.get("content") or ""}
    if m["role"] == "assistant":
        if keep_reasoning and m.get("reasoning"):
            out["reasoning_content"] = m["reasoning"]
        if m.get("tool_calls"):
            out["tool_calls"] = [norm_call(tc) for tc in m["tool_calls"]]
    elif m["role"] == "tool":
        if m.get("name"):
            out["name"] = m["name"]
        if m.get("tool_call_id"):
            out["tool_call_id"] = m["tool_call_id"]
    return out


def explode(rec, system_text, tools, history_reasoning):
    msgs = rec["messages"]
    samples, k = [], 0
    for i, m in enumerate(msgs):
        if m["role"] != "assistant":
            continue
        k += 1
        last_user = max(j for j in range(i) if msgs[j]["role"] == "user")
        hist = []
        for j in range(i):
            h = msgs[j]
            keep = h["role"] == "assistant" and (history_reasoning == "keep" or j > last_user)
            hist.append(clean_msg(h, keep))
        samples.append({
            "id": f"{rec['id']}#{k}",
            "record_id": rec["id"],
            "group_id": rec["group_id"],
            "thinking": rec["thinking"],
            "tools": tools,
            "prompt": [{"role": "system", "content": system_text}] + hist,
            "completion": clean_msg(m, True),
        })
    return samples


def cmd_build(args):
    items = load(args.file)
    validate_all(items, args.strict)
    n_err, n_warn = counts(items)
    if n_err and not args.skip_invalid:
        print_issues(items)
        print(f"\nBuild aborted: {n_err} errors. Fix them, or pass --skip-invalid to build the valid records only.")
        return 1
    if args.strict and n_warn:
        print_issues(items)
        print(f"\nBuild aborted (--strict): {n_warn} warnings.")
        return 1
    if args.render_fields == "all":
        allowed = set(OPTIONAL_RENDER)
    else:
        allowed = {f.strip() for f in args.render_fields.split(",") if f.strip()}
        unknown = allowed - set(OPTIONAL_RENDER)
        if unknown:
            print(f"unknown --render-fields: {sorted(unknown)}; choose from {OPTIONAL_RENDER}")
            return 1

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    handles = {s: open(out / f"{s}.jsonl", "w", encoding="utf-8") for s in ("train", "val", "test")}
    man = open(out / "manifest.jsonl", "w", encoding="utf-8")
    st = Counter()
    rendered_total = 0
    for it in items:
        rec = it["rec"]
        if rec is None or any(lv == "ERROR" for lv, _ in it["issues"]):
            st["records_skipped_invalid"] += 1
            continue
        split = resolve_split(rec, args.val, args.test, args.seed)
        if split == "exclude" and args.include_excluded:
            split = auto_split(rec, args.val, args.test, args.seed)
        if split in ("exclude", "eval_only"):
            st[f"records_skipped_{split}"] += 1
            continue
        rng = random.Random(f"{args.seed}:{rec['id']}")
        fields, dropped_all = choose_fields(rec, rng, args.p_drop_all, args.p_drop_field, allowed)
        system = render_system(rec["control"], fields)
        tools = [TOOL_REGISTRY[t] for t in rec["control"]["tools"]]
        samples = explode(rec, system, tools, args.history_reasoning)
        for s in samples:
            handles[split].write(json.dumps(s, ensure_ascii=False) + "\n")
        man.write(json.dumps({
            "id": rec["id"], "group_id": rec["group_id"], "split": split, "samples": len(samples),
            "render_version": RENDER_VERSION, "rendered_fields": sorted(fields), "dropped_all": dropped_all,
            "control": rec["control"], "thinking": rec["thinking"], "meta": rec["meta"],
        }, ensure_ascii=False) + "\n")
        st[f"records_{split}"] += 1
        st[f"samples_{split}"] += len(samples)
        st["samples_thinking_on"] += len(samples) if rec["thinking"] == "on" else 0
        st["samples_with_tools"] += len(samples) if tools else 0
        st["records_dropped_all"] += 1 if dropped_all else 0
        rendered_total += len(fields)
    for h in handles.values():
        h.close()
    man.close()
    n_rec = sum(v for k, v in st.items() if k.startswith("records_") and k.split("_", 1)[1] in ("train", "val", "test"))
    summary = {
        "schema_version": SCHEMA_VERSION, "render_version": RENDER_VERSION,
        "args": {k: v for k, v in vars(args).items() if k not in ("cmd", "file", "fn")},
        "counts": dict(st), "avg_rendered_optional_fields": round(rendered_total / n_rec, 2) if n_rec else 0,
        "warnings": n_warn,
    }
    (out / "build_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary["counts"], indent=2))
    print(f"\nwrote {out}/ (train.jsonl, val.jsonl, test.jsonl, manifest.jsonl, build_summary.json); "
          f"{n_warn} validation warnings.")
    print("Next: render prompt/completion with the base model's chat template, loss on `completion` only.")
    return 0


# --------------------------------------------------------------------------- #
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    v = sub.add_parser("validate", help="check every record; exit 1 on errors")
    v.add_argument("file")
    v.add_argument("--strict", action="store_true", help="warnings fail too; also require Afrikaans speaker review")
    v.add_argument("--images-root", help="folder that image paths in records are relative to (checks files exist)")
    v.set_defaults(fn=cmd_validate)

    r = sub.add_parser("report", help="coverage and balance tables")
    r.add_argument("file")
    r.add_argument("--min-cell", type=int, default=10, help="flag cells with fewer records than this")
    r.set_defaults(fn=cmd_report)

    b = sub.add_parser("build", help="render system prompts and write train/val/test prompt-completion files")
    b.add_argument("file")
    b.add_argument("--out", required=True)
    b.add_argument("--seed", type=int, default=1)
    b.add_argument("--p-drop-all", type=float, default=0.10,
                   help="chance a record loses all droppable control fields (default 0.10)")
    b.add_argument("--p-drop-field", type=float, default=0.15,
                   help="chance each droppable control field is left out (default 0.15)")
    b.add_argument("--render-fields", default="all",
                   help="comma list of control fields to ever render; others stay constant in the app. "
                        f"Choices: {', '.join(OPTIONAL_RENDER)}")
    b.add_argument("--history-reasoning", choices=["strip", "keep"], default="strip",
                   help="strip: earlier user turns' reasoning is not replayed (Qwen-style); keep: replay all")
    b.add_argument("--val", type=float, default=0.05, help="share of auto-split groups for validation")
    b.add_argument("--test", type=float, default=0.05, help="share of auto-split groups for test")
    b.add_argument("--include-excluded", action="store_true", help="dry run: also build split='exclude' records")
    b.add_argument("--skip-invalid", action="store_true", help="build the valid records only")
    b.add_argument("--strict", action="store_true", help="abort on warnings too")
    b.add_argument("--images-root", help="folder that image paths in records are relative to (checks files exist)")
    b.set_defaults(fn=cmd_build)

    args = ap.parse_args(argv)
    global IMAGES_ROOT
    IMAGES_ROOT = getattr(args, "images_root", None)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
