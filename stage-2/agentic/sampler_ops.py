"""
sampler_ops.py - "operations" data + helpers: context compaction, resume-from-state, reply budgets, KV/device maths.

Principle: CODE owns facts and thresholds (token counts, ledger, when to compact, what to keep verbatim).
The MODEL owns language judgement only (a short narrative of what the learner did, and replying correctly after a compaction).
Port the helpers in sections 1-3 to your app language (they are plain logic); sections 4-6 are for the data pipeline.

Assumed input schema for existing dialogues (round-2 pack):
    {"meta": {"item_id"?, "topic"?, "subject"?, "learner_state"?, "learner_script"?}, "dialogue": [{"role": "student|teacher", "content": "..."}]}
Adapt ledger_entry() if your 15,000 Socratic samples use other field names.
"""
import copy
import json
import math
import random
import re

# ----------------------------------------------------------------------------- 1. KV cache + device tiers
def kv_bytes_per_token(n_layers, n_kv_heads, head_dim, bytes_per_elem=2):
    """K and V, every layer. Read the three numbers from your model's config.json. bytes_per_elem: 2 = fp16, 1 = 8-bit KV."""
    return 2 * n_layers * n_kv_heads * head_dim * bytes_per_elem


def kv_cache_bytes(n_tokens, **cfg):
    return n_tokens * kv_bytes_per_token(**cfg)


def memory_budget_tokens(kv_ram_bytes, **cfg):
    return int(kv_ram_bytes // kv_bytes_per_token(**cfg))


def effective_budget(memory_tokens, quality_tokens, latency_tokens):
    """The context you can actually USE = the smallest of: what fits in RAM, where answer quality starts to drop
    (measure with recall tests at 2k/4k/6k/8k tokens), and where time-to-first-token becomes too slow."""
    return min(memory_tokens, quality_tokens, latency_tokens)


# PLACEHOLDERS: replace with measured numbers per device tier (run the three measurements above on real phones).
DEVICE_TIERS = {
    "low":  {"ctx_budget": 3000,  "soft": 0.55, "hard": 0.80, "reply_budget": "short",  "thinking_default": "none"},
    "mid":  {"ctx_budget": 6000,  "soft": 0.55, "hard": 0.80, "reply_budget": "normal", "thinking_default": "short"},
    "high": {"ctx_budget": 12000, "soft": 0.55, "hard": 0.80, "reply_budget": "normal", "thinking_default": "short"},
}


def approx_tokens(text):
    """Crude fallback. Pass your real tokenizer's count function wherever count_tokens is accepted."""
    return max(1, len(str(text)) // 4)


# ----------------------------------------------------------------------------- 2. when and how to compact (app logic)
def compaction_decision(tokens_used, tier, turns_since_compaction, learner_idle, min_gap_turns=4):
    """'none' | 'soft' (do it now, between turns, while the learner is idle) | 'now' (cannot wait)."""
    t = DEVICE_TIERS[tier]
    if turns_since_compaction < min_gap_turns:
        return "none"
    frac = tokens_used / t["ctx_budget"]
    if frac >= t["hard"]:
        return "now"
    if frac >= t["soft"] and learner_idle:
        return "soft"
    return "none"


def prune_history(messages):
    """Free speed: reasoning / thinking never stays in history after its turn."""
    out = []
    for m in messages:
        m = dict(m)
        for k in ("private_reasoning", "thinking", "reasoning"):
            m.pop(k, None)
        out.append(m)
    return out


def split_for_compaction(messages, budget_tokens, keep_fraction=0.30, count_tokens=approx_tokens, min_keep=2):
    """Keep the newest messages verbatim up to keep_fraction of the budget (never fewer than min_keep); compact the rest.
    Cut so that the kept part never starts on a teacher reply."""
    kept, used = [], 0
    for m in reversed(messages):
        c = count_tokens(m.get("content", ""))
        if len(kept) >= min_keep and used + c > keep_fraction * budget_tokens:
            break
        kept.insert(0, m)
        used += c
    while len(kept) > min_keep and kept and kept[0].get("role") == "teacher":
        kept.pop(0)
    return messages[: len(messages) - len(kept)], kept


def rebuild_context(system_prompt, state, pinned_question, kept_messages):
    """Fixed order, static prompt FIRST (so a runtime that caches the prefix can reuse it). Old turns are gone for real:
    the KV cache must be rebuilt from this list, otherwise nothing was saved."""
    msgs = [{"role": "system", "content": system_prompt},
            {"role": "system_event", "content": "SESSION STATE " + json.dumps(state, ensure_ascii=False)}]
    if pinned_question:
        msgs.append({"role": "system_event", "content": "CURRENT QUESTION (verbatim) " + pinned_question})
    return msgs + prune_history(kept_messages)


# ----------------------------------------------------------------------------- 3. ledger (code-owned facts)
STATE_OWNED_KEYS = {"narrative", "misconceptions", "current", "next", "learner_notes"}


def ledger_entry(d, index):
    meta = d.get("meta", {})
    script = meta.get("learner_script") or []
    last = script[-1] if script else "correct"
    teacher_turns = sum(1 for t in d["dialogue"] if t.get("role") == "teacher")
    return {"q": str(meta.get("item_id") or f"Q{index}"), "topic": meta.get("topic") or meta.get("subject"),
            "result": "stuck" if last == "gives_up" else "solved", "hints": max(teacher_turns - 1, 0)}


def ledger_stats(entries):
    return {"attempted": len(entries), "solved": sum(e["result"] == "solved" for e in entries),
            "stuck": sum(e["result"] == "stuck" for e in entries), "hints_total": sum(e["hints"] for e in entries)}


def stitch_session(dialogues, start_index=1):
    """Turn existing dialogues into one long session transcript + the ledger the app would have kept.
    The app inserts a system_event whenever the learner moves to another question."""
    msgs, entries = [], []
    for i, d in enumerate(dialogues, start_index):
        e = ledger_entry(d, i)
        entries.append(e)
        msgs.append({"role": "system_event", "content": f"Question changed to {e['q']}"})
        msgs += prune_history([{"role": t["role"], "content": t["content"]} for t in d["dialogue"]])
    return msgs, {"entries": entries, "stats": ledger_stats(entries)}


# ----------------------------------------------------------------------------- 4. prompts
COMPACT_APP_PROMPT = """SESSION COMPACTION (internal, never shown to the learner). You get the previous session state, the app's ledger, and the conversation since. Return ONLY JSON with the fields narrative, misconceptions, current, next, learner_notes. Keep what the tutor needs next: what the learner actually did wrong or right, the step they were on, anything they said about themselves. Drop greetings and repetition. Write nothing that is not in the conversation. Never copy the ledger. English only; short quotes may stay in the original language. Maximum {{max_tokens}} tokens."""

COMPACT_TEACHER_PROMPT = """TASK: COMPACTION. Write the ideal session state for the compacted part of a tutoring session.
INPUT: prev_state (or null), ledger (computed by code, authoritative), transcript (the messages being compacted), max_tokens.
You write ONLY: narrative, misconceptions, current, next, learner_notes.
RULES
1. Faithful. Every claim is in the transcript or prev_state. No guessing, no filler, no praise.
2. Specific. "Dropped the negative sign when expanding (x-3)^2, twice" and not "struggles with algebra". Name the exact step, rule or word the learner got wrong or right.
3. Merge. With a prev_state: carry forward what is still relevant, update what changed, drop what was resolved. Never restate old content you cannot verify against the transcript or prev_state.
4. Numbers and question ids: only those in the ledger or transcript. Do not count, add or compare anything: the ledger has the stats.
5. narrative <= 120 words. misconceptions <= 5 items, each <= 25 words, tagged with the question id when known. learner_notes <= 5 items, ONLY things the learner SAID about themselves (language preference, exam date, what they find hard). current = {"q","status","last_step"} for the question in progress (status in_progress | between_questions | none; last_step <= 30 words). next = ONE sentence: what the tutor planned to do next.
6. Do not copy the question text: the app keeps it verbatim.
7. English only. Quote at most 6 words in the original language.
OUTPUT: one JSON object, no fence: {"narrative":"","misconceptions":[],"current":{"q":null,"status":"none","last_step":""},"next":"","learner_notes":[]}"""

RESUME_TEACHER_PROMPT = """TASK: RESUME. The session was compacted. The tutor now sees ONLY: the system prompt, state (the app's ledger + the tutor's own compacted notes), the pinned question (verbatim), the last few messages verbatim, and a learner probe. Write the tutor's reply.
probe_type:
- continue_current: continue tutoring the pinned question from state.current.last_step. Do not repeat solved steps.
- recall_in_state: answer from the ledger / narrative / misconceptions. Say only what is there.
- recall_not_in_state: the detail asked for (exact numbers, exact wording, step by step) is NOT in the state. Say you no longer have that detail, say in one line what you DO have, and offer to redo it or ask the learner to share it. Never invent it.
- progress ("how am I doing?"): use ledger.stats numbers exactly, name 1-2 misconceptions, give one concrete next step.
RULES: the COMMON CORE rules apply; reply in learner_language; at most 450 characters; never mention "summary", "compaction", "state" or "memory": say "from what we did earlier". Output the dialogue JSON from the pack: the learner probe, then the teacher reply."""

BUDGET_RULES = """REPLY BUDGET: reply_budget is tiny (1-2 sentences), short (3-4 sentences) or normal. Obey it. In tiny and short give ONE hint or ONE step: no recap, no lists. Honesty, grounding and wellbeing rules still apply in full."""

# ----------------------------------------------------------------------------- 5. spec builders
PROBE_WEIGHTS = {"continue_current": 40, "recall_in_state": 25, "recall_not_in_state": 20, "progress": 15}
BUDGET_WEIGHTS = {"low": {"tiny": 40, "short": 45, "normal": 15}, "mid": {"tiny": 10, "short": 40, "normal": 50},
                  "high": {"tiny": 5, "short": 25, "normal": 70}}
LANG_WEIGHTS = {"en": 65, "af": 35}


def _pick(weights, rng):
    keys = list(weights)
    return rng.choices(keys, weights=[weights[k] for k in keys])[0]


def make_compaction_spec(pool, rng, tier="mid", n_range=(5, 10), max_tokens=350):
    """pool = existing dialogues. Compacts the older part of a stitched session, keeps the newest part verbatim,
    and leaves the last dialogue IN PROGRESS (cut after a teacher turn) so 'current' and the pinned question matter."""
    if len(pool) < 4:
        raise ValueError("need at least 4 dialogues in the pool")
    n = min(rng.randint(*n_range), len(pool))
    picks = rng.sample(pool, k=n)
    keep_n = rng.choice([1, 2])
    old, recent = picks[:-keep_n], copy.deepcopy(picks[-keep_n:])
    cur = recent[-1]
    teacher_idx = [i for i, t in enumerate(cur["dialogue"]) if t["role"] == "teacher"]
    cut = rng.choice(teacher_idx[:-1] if len(teacher_idx) > 1 else teacher_idx)
    cur["dialogue"] = cur["dialogue"][: cut + 1]
    cur["meta"] = dict(cur.get("meta", {}), in_progress=True)
    pinned = next(t["content"] for t in cur["dialogue"] if t["role"] == "student")[:500]
    chain = len(old) >= 6 and rng.random() < 0.5            # second-generation compaction: merge into prev_state
    parts = [old[: len(old) // 2], old[len(old) // 2:]] if chain else [old]
    chunks, start = [], 1
    cumulative = []
    for part in parts:
        msgs, led = stitch_session(part, start_index=start)
        start += len(part)
        cumulative += led["entries"]
        chunks.append({"transcript": msgs, "ledger": {"entries": list(cumulative), "stats": ledger_stats(cumulative)}})
    kept_msgs, _ = stitch_session(recent, start_index=start)
    return {"task_type": "context_compaction", "device_tier": tier, "max_tokens": max_tokens,
            "generation": "chain" if chain else "single", "chunks": chunks,
            "pinned_question": pinned, "kept_messages": kept_msgs}


def make_resume_spec(compaction_spec, rng):
    probe = _pick(PROBE_WEIGHTS, rng)
    entries = compaction_spec["chunks"][-1]["ledger"]["entries"]
    spec = {"task_type": "resume_from_state", "probe_type": probe, "learner_language": _pick(LANG_WEIGHTS, rng),
            "reply_budget": _pick(BUDGET_WEIGHTS[compaction_spec["device_tier"]], rng)}
    if probe in ("recall_in_state", "recall_not_in_state") and entries:
        spec["target_q"] = rng.choice(entries)["q"]
    if probe == "recall_not_in_state":
        spec["detail_kind"] = rng.choice(["exact_numbers", "exact_wording", "step_by_step"])
    return spec


def make_budget_spec(base_spec, rng, tier="mid"):
    """Adds a reply budget to ANY tutoring spec (round-2 or study specs). Low tier + tiny budget forces thinking off."""
    s = dict(base_spec)
    s["reply_budget"] = _pick(BUDGET_WEIGHTS[tier], rng)
    s["device_tier"] = tier
    if tier == "low" and s["reply_budget"] == "tiny":
        s["thinking_mode"] = "none"
    return s


def ops_pool(base_exposures, share, epochs):
    """Unique operational samples needed so they make up `share` of all exposures."""
    return round(share * base_exposures / (1 - share) / epochs)


# ----------------------------------------------------------------------------- 6. verification
# Question ids are matched as Q3, Q3.2 ... Give your items ids in that form (meta.item_id) or change this pattern,
# otherwise invented question ids are not caught.
_QID = re.compile(r"\bQ\d+(?:\.\d+)*\b", re.I)
_NUM = re.compile(r"\d+(?:[.,]\d+)?")


def ungrounded_refs(text, allowed_text):
    """Question ids and numbers in `text` that do not occur in `allowed_text` (ledger + transcript + prev_state)."""
    allowed_ids = {x.upper() for x in _QID.findall(allowed_text)}
    ids = {x.upper() for x in _QID.findall(text)}
    stripped_t, stripped_a = _QID.sub(" ", text), _QID.sub(" ", allowed_text)
    allowed_nums = set(_NUM.findall(stripped_a))
    nums = set(_NUM.findall(stripped_t))
    return {"qids": sorted(ids - allowed_ids), "numbers": sorted(nums - allowed_nums)}


def verify_state(out, ledger, transcript, prev_state=None, count_tokens=approx_tokens, max_tokens=350):
    """Problems list for a model-written session state (empty = accept)."""
    p = []
    if not isinstance(out, dict):
        return ["not_an_object"]
    extra, missing = set(out) - STATE_OWNED_KEYS, STATE_OWNED_KEYS - set(out)
    if extra: p.append("keys_not_owned_by_model:" + ",".join(sorted(extra)))
    if missing: p.append("missing_keys:" + ",".join(sorted(missing)))
    if p:
        return p
    if len(str(out["narrative"]).split()) > 120: p.append("narrative_over_120_words")
    if len(out["misconceptions"]) > 5 or any(len(str(x).split()) > 25 for x in out["misconceptions"]): p.append("misconceptions_too_long_or_many")
    if len(out["learner_notes"]) > 5: p.append("too_many_learner_notes")
    if not isinstance(out["current"], dict) or set(out["current"]) != {"q", "status", "last_step"}: p.append("bad_current")
    elif out["current"]["status"] not in ("in_progress", "between_questions", "none"): p.append("bad_current_status")
    if len(str(out["next"]).split(". ")) > 1 and len(str(out["next"]).split()) > 40: p.append("next_not_one_sentence")
    if count_tokens(json.dumps(out, ensure_ascii=False)) > max_tokens: p.append("over_token_cap")
    src = json.dumps(ledger, ensure_ascii=False) + " " + " ".join(m.get("content", "") for m in transcript) + " " + json.dumps(prev_state or {}, ensure_ascii=False)
    bad = ungrounded_refs(json.dumps({k: out[k] for k in ("narrative", "misconceptions", "current", "next")}, ensure_ascii=False), src)
    if bad["qids"]: p.append("invented_question_ids:" + ",".join(bad["qids"]))
    if bad["numbers"]: p.append("numbers_not_in_source:" + ",".join(bad["numbers"]))
    return p


def verify_resume_reply(reply, state_text, pinned_question=""):
    p = []
    if re.search(r"\b(summary|compaction|memory|session state|opsomming|geheue)\b", reply, re.I):
        p.append("mentions_mechanics")
    bad = ungrounded_refs(reply, state_text + " " + pinned_question)
    if bad["qids"]: p.append("invented_question_ids:" + ",".join(bad["qids"]))
    if bad["numbers"]: p.append("numbers_not_in_state:" + ",".join(bad["numbers"]))
    if len(reply) > 450: p.append("over_450_chars")
    return p


def within_budget(text, budget, count_tokens=approx_tokens):
    limits = {"tiny": (2, 80), "short": (4, 170)}   # sentences, tokens: starting guesses
    if budget not in limits:
        return []
    max_s, max_t = limits[budget]
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]
    p = []
    if len(sentences) > max_s: p.append(f"{len(sentences)}_sentences_over_{max_s}")
    if count_tokens(text) > max_t: p.append("over_token_limit")
    return p

