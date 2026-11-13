"""
stage-2/quality/rubric_checker.py - Deterministic Quality Rubric Checker (Zero API Cost).

Evaluates:
  1. Alternation & structure: Starts on user, ends on assistant, alternating roles.
  2. Length & substance: No empty messages, no trivially short turns (< 15 chars).
  3. Private reasoning: Every assistant message must have substantive 'reasoning'.
  4. Anti-spoiler: Turn 1 assistant message MUST NOT leak the final answer.
  5. Anti-reflexive praise: Banned opener words ("Exactly!", "Presies!", "Brilliant!",
     "Perfek!", "Spot on!", "Uitstekend!") unless justified.
  6. Tool call validation (STEM): No placeholders ("1+1", "0+0", "custom", "none").
  7. Tool policy (Language): Tools strictly forbidden for language subjects.
  8. Language consistency: Afrikaans subjects must contain authentic Afrikaans markers.
  9. Mathematical / numerical precision: Robust numeric matcher handling SA decimal
     commas (0,15), LaTeX fractions (\frac{a}{b}), scientific notation (1.6 x 10^-19),
     and 1% relative tolerance.
"""

import re
import json
from typing import Tuple, List, Optional

_PLACEHOLDER_EXPR = re.compile(r"^\s*(custom|none|null|nan|[01]\s*[-+*/]\s*[01]|[01])\s*$", re.I)

BANNED_PRAISE_OPENERS = {
    "exactly", "brilliant", "perfect", "spot on", "great job", "well done",
    "presies", "perfek", "pragtig", "uitstekend", "absoluut"
}

AFRIKAANS_MARKERS = {"die", "en", "van", "vir", "met", "nie", "wat", "jou", "ons", "hierdie", "is", "om"}

# ── Robust Forensic Numeric Matcher (from parse_repair) ──────────────────────

def extract_numbers_from_text(s: str) -> List[float]:
    """Pull numbers out of text, handling SA decimal commas, fractions, and scientific notation."""
    s = str(s)
    vals = []

    def _frac(m):
        try:
            vals.append(float(m.group(1)) / float(m.group(2)))
        except Exception:
            pass
        return " "

    s = re.sub(r"\\d?frac\{(-?\d+)\}\{(\d+)\}", _frac, s)
    s = re.sub(r"(-?\d+)\s*/\s*(\d+)", _frac, s)

    def _sci(m):
        try:
            base = float(m.group(1).replace(",", "."))
            exp = int(m.group(2))
            vals.append(base * (10 ** exp))
        except Exception:
            pass
        return " "

    s = re.sub(r"(-?\d+(?:[.,]\d+)?)\s*(?:x|X|\\times|×|\*|·)\s*10\s*\^\s*\{?\s*(-?\d+)\s*\}?", _sci, s)

    for x in re.findall(r"-?\d+(?:[.,]\d+)?(?:[eE][-+]?\d+)?", s):
        try:
            vals.append(float(x.replace(",", ".")))
        except Exception:
            pass

    return vals

def numeric_match(model_answer: str, memo_answer: str, rel_tol: float = 0.01) -> Optional[bool]:
    """
    True if every number in the memo answer appears (within rel_tol) in the model's answer.
    None = memo has no numbers (MCQ or qualitative text).
    """
    want = extract_numbers_from_text(memo_answer)
    got = extract_numbers_from_text(model_answer)
    if not want:
        return None

    def close(g, w):
        return abs(g) <= 1e-9 if w == 0 else abs(g - w) <= rel_tol * abs(w)

    return all(any(close(g, w) for g in got) for w in want)

def is_placeholder_tool_call(expr: str) -> bool:
    if expr is None:
        return False
    return bool(_PLACEHOLDER_EXPR.match(str(expr).strip()))

# ── Multi-Dimensional Quality Rubric ────────────────────────────────────────

def check_rubric(record: dict,
                 expected_strategy: str = None,
                 expected_lang: str = "en",
                 is_language_subject: bool = False,
                 min_turns: int = 2) -> Tuple[bool, List[str], int]:
    """
    Scores record on a 0-100 scale using deterministic checks.
    Returns: (passed, issues, score)
    """
    issues = []
    score = 100
    messages = record.get("messages", [])
    meta = record.get("meta", {})
    final_answer = str(meta.get("final_answer") or "").strip()

    # 1. Structure check
    if not messages or not isinstance(messages, list):
        return False, ["No messages array"], 0

    messages = [m for m in messages if isinstance(m, dict)]
    if not messages:
        return False, ["No valid message dicts"], 0

    if messages[0].get("role") != "user":
        issues.append("Dialogue must start on user turn")
        score -= 20

    if messages[-1].get("role") != "assistant":
        issues.append("Dialogue must end on assistant turn")
        score -= 20

    user_msgs = [m for m in messages if m.get("role") == "user"]
    asst_msgs = [m for m in messages if m.get("role") == "assistant"]

    if len(asst_msgs) < min_turns:
        issues.append(f"Too few assistant turns: {len(asst_msgs)} (expected >= {min_turns})")
        score -= 15

    # 2. Content length and substance check
    for idx, m in enumerate(messages):
        content = (m.get("content") or "").strip()
        if not content:
            issues.append(f"Message {idx} ({m.get('role')}) is empty")
            score -= 25
        elif len(content) < 15 and m.get("role") == "assistant":
            issues.append(f"Assistant message {idx} is trivially short ({len(content)} chars)")
            score -= 15

    # 3. Private reasoning check
    for idx, m in enumerate(asst_msgs):
        reasoning = (m.get("reasoning") or "").strip()
        if not reasoning:
            issues.append(f"Assistant message {idx} missing private reasoning trace")
            score -= 15
            break

    # 4. Anti-spoiler check: First assistant message should NOT leak the final answer
    if len(asst_msgs) >= 2 and final_answer and len(final_answer) >= 3:
        first_asst = (asst_msgs[0].get("content") or "").lower()
        target_clean = final_answer.lower().replace("$", "").replace("\\", "").strip()
        if len(target_clean) >= 4 and target_clean in first_asst:
            issues.append("First assistant message leaks the final answer (non-Socratic)")
            score -= 25

    # 5. Anti-reflexive praise check
    for idx, m in enumerate(asst_msgs):
        content = (m.get("content") or "").strip()
        words = content.split()
        if words:
            opener = words[0].lower().strip("!.,:;?")
            if opener in BANNED_PRAISE_OPENERS:
                # Deduct if it's not the final turn or if opener is purely reflexive
                if idx < len(asst_msgs) - 1:
                    issues.append(f"Assistant message {idx} opens with unearned reflexive praise: '{words[0]}'")
                    score -= 10
                    break

    # 6. Tool-calling validation
    tool_check = meta.get("tool_call") or meta.get("tool_check")
    if is_language_subject:
        # Check if model used a calculator tool in reasoning
        for m in asst_msgs:
            reas = m.get("reasoning", "")
            if "[TOOL CHECK: calculator" in reas:
                issues.append("Language subject illegally emitted calculator tool call")
                score -= 15
                break
    else:
        # Check for placeholder tool expressions
        for m in asst_msgs:
            reas = m.get("reasoning", "")
            m_tool = re.search(r'\[TOOL CHECK:\s*calculator\((?:expression=)?["\']?([^"\']+)["\']?\)', reas)
            if m_tool and is_placeholder_tool_call(m_tool.group(1)):
                issues.append(f"Placeholder tool check detected: '{m_tool.group(1)}'")
                score -= 10
                break

    # 7. Language consistency check
    if expected_lang == "af":
        all_asst_text = " ".join((m.get("content") or "").lower() for m in asst_msgs)
        words_found = sum(1 for marker in AFRIKAANS_MARKERS if f" {marker} " in f" {all_asst_text} ")
        if words_found < 3:
            issues.append("Expected Afrikaans response, but insufficient Afrikaans markers detected")
            score -= 25

    score = max(0, score)
    passed = score >= 50

    return passed, issues, score

def format_rubric_report(passed: bool, issues: List[str], score: int) -> str:
    status = "PASS" if passed else "FAIL"
    lines = [f"[RUBRIC {status}] Score: {score}/100"]
    if issues:
        for issue in issues:
            lines.append(f"  * {issue}")
    return "\n".join(lines)
