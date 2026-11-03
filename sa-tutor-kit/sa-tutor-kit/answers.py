#!/usr/bin/env python3
"""
answers.py - compare maths/science answers, and find the final answer inside a tutor reply.

WHY THIS EXISTS
  Two jobs need "is this the right answer?":
    1. verifying teacher-written training records against the memo (pipeline/verify.py)
    2. scoring your trained model on the eval set (eval/score_eval.py)
  String comparison is not enough ("x = 3", "x=3", "3,0", "$x = \\frac{6}{2}$" are all the same answer),
  so we use SymPy for the maths and fall back to cleaned-up strings.

  It is a HEURISTIC. It will sometimes say "no" to a right answer written in a strange way, and rarely
  say "yes" to a wrong one. Treat disagreements as "look at this one", not as the truth.

USAGE
  python answers.py            runs a few self-checks
  from answers import answers_match, contains_final_answer
"""
from __future__ import annotations

import re

try:
    import sympy
    from sympy.parsing.sympy_parser import (parse_expr, standard_transformations,
                                            implicit_multiplication_application, convert_xor)
    _TRANSFORMS = standard_transformations + (implicit_multiplication_application, convert_xor)
except ImportError:          # SymPy missing: we still work with plain string comparison
    sympy = None

_MINUS = "\u2212\u2012\u2013\u2014"


def _clean(s):
    """Turn LaTeX-ish / school notation into something SymPy can read."""
    s = str(s).strip()
    for ch in _MINUS:
        s = s.replace(ch, "-")
    s = s.replace("\u00d7", "*").replace("\u00f7", "/").replace("\u00b7", "*").replace("\u00b2", "^2") \
         .replace("\u00b3", "^3").replace("\u221a", "sqrt").replace("\u03c0", "pi").replace("\u00b0", "")
    s = re.sub(r"\\text\{([^{}]*)\}", r" \1 ", s)
    s = re.sub(r"\\mathrm\{([^{}]*)\}", r" \1 ", s)
    s = s.replace("\\left", "").replace("\\right", "").replace("\\,", " ").replace("\\;", " ").replace("\\!", "")
    for _ in range(3):   # nested fractions
        s = re.sub(r"\\[dt]?frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", s)
    s = re.sub(r"\\sqrt\[(\d+)\]\{([^{}]*)\}", r"((\2)**(1/\1))", s)
    s = re.sub(r"\\sqrt\{([^{}]*)\}", r"sqrt(\1)", s)
    s = s.replace("\\cdot", "*").replace("\\times", "*").replace("\\div", "/").replace("\\pi", "pi")
    s = s.replace("\\theta", "theta").replace("\\therefore", "")
    s = s.replace("$", "").replace("{", "(").replace("}", ")")
    s = re.sub(r"\s+", " ", s).strip().rstrip(".").strip()
    return s


def _split_top(s, seps):
    """Split on separators that are not inside brackets."""
    parts, depth, cur, i = [], 0, "", 0
    while i < len(s):
        ch = s[i]
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        if depth == 0:
            hit = next((sp for sp in seps if s.startswith(sp, i)), None)
            if hit:
                parts.append(cur)
                cur, i = "", i + len(hit)
                continue
        cur += ch
        i += 1
    parts.append(cur)
    return [p.strip() for p in parts if p.strip()]


def split_alternatives(s):
    """'x = 2 or x = 3' -> ['x = 2', 'x = 3']  (also ';', 'of', 'and', 'en')."""
    s = _clean(s)
    parts = _split_top(s, [";", " or ", " of ", " and ", " en ", " OR "])
    return parts or [s]


_LABEL = re.compile(r"^[A-Za-z\u03b8][A-Za-z0-9_']*(?:\([^()]*\))?$")


def _strip_label(part):
    """'x = 3' -> '3'.  Only when the left side is a bare name like x, y, S_10 or f'(x)."""
    if "=" in part:
        left, right = part.rsplit("=", 1)
        pieces = part.split("=")
        if _LABEL.match(pieces[0].strip()):
            return pieces[-1].strip()
    return part


def _decimals(text):
    m = re.search(r"\d[.,](\d+)", text)
    return len(m.group(1)) if m else 0


def _numeric_prefix(s):
    m = re.match(r"^\s*([-+]?\s*(?:\d+(?:[.,]\d+)?|[.,]\d+)(?:\s*[*/]\s*\(?[-+]?\d+(?:[.,]\d+)?\)?|\s*\^\s*\(?[-+]?\d+\)?)*)\s*(.*)$", s)
    return (m.group(1), m.group(2)) if m else (None, None)


_UNITISH = re.compile(r"^[A-Za-z\u00b5\u03bc\u03a9%/\^\-\d\.\s\u00b7*]*$")


_KNOWN_UNITS = {"m", "km", "cm", "mm", "s", "min", "h", "hr", "kg", "g", "mg", "n", "j", "w", "v", "a", "pa", "hz",
                "mol", "l", "ml", "c", "k", "rad", "deg", "ohm", "ohms", "kj", "kw", "kpa", "mpa", "cal", "ev",
                "m2", "m3", "cm2", "cm3", "km2", "mph", "rand", "r", "dm", "dm3"}


def _is_unit_suffix(s, rest):
    """'10 m/s' and '588 N' end in units; '3x' and '2a' do not (no space and not a known unit)."""
    had_space = bool(re.search(r"\d\s+[A-Za-z\u00b5\u03bc\u03a9]", s))
    tokens = [t for t in re.split(r"[/\^\-\s\u00b7*.]+", rest.lower()) if t and not t.isdigit()]
    return had_space or (bool(tokens) and all(t in _KNOWN_UNITS for t in tokens))


def _to_number_text(s):
    """Handle SA number style: '1 000' -> '1000', '2,5' -> '2.5' (decimal comma)."""
    s = re.sub(r"(?<=\d)\s(?=\d{3}(?!\d))", "", s)
    if s.count(",") == 1 and re.match(r"^[-+]?\d+,\d+(?:\D.*)?$", s) and ";" not in s:
        s = s.replace(",", ".")
    return s


def parse_value(part):
    """Return a SymPy value (or None). Units after a number are ignored."""
    if sympy is None:
        return None
    s = _to_number_text(_strip_label(_clean(part)))
    if not s:
        return None
    s = s.replace("%", "")
    candidates = [s]
    num, rest = _numeric_prefix(s)
    if num is not None and rest and _UNITISH.match(rest) and _is_unit_suffix(s, rest):
        candidates = [num, s]          # '10 m/s' -> try plain 10 first
    for c in candidates:
        try:
            c2 = c.replace("^", "**")
            return sympy.sympify(parse_expr(c2, transformations=_TRANSFORMS, evaluate=True), rational=True)
        except Exception:
            continue
    return None


def _values_equal(a, b, text_a, text_b):
    try:
        if a.free_symbols or b.free_symbols:
            return sympy.simplify(a - b) == 0
        fa, fb = float(a), float(b)
        if abs(fa - fb) <= 1e-9 * max(1.0, abs(fb)):
            return True
        da, db = _decimals(text_a), _decimals(text_b)
        if da > db and abs(round(fa, db) - fb) < 1e-12:     # model is more precise than the memo
            return True
        return False
    except Exception:
        return False


def _norm_str(s):
    return re.sub(r"[\s$\\{}()]", "", _clean(s).lower())


def _pair_match(x, y):
    """Compare two single answers (no alternatives)."""
    x, y = _clean(x), _clean(y)
    # ordered pairs like (1;2) or (1,2)
    pa = re.match(r"^\((.+)[;,](.+)\)$", x)
    pb = re.match(r"^\((.+)[;,](.+)\)$", y)
    if pa and pb:
        return _pair_match(pa.group(1), pb.group(1)) and _pair_match(pa.group(2), pb.group(2))
    va, vb = parse_value(x), parse_value(y)
    if va is not None and vb is not None:
        return _values_equal(va, vb, _strip_label(x), _strip_label(y))
    return _norm_str(_strip_label(x)) == _norm_str(_strip_label(y)) and _norm_str(x) != ""


def answers_match(a, b):
    """True if answer strings a and b mean the same thing (order of alternatives does not matter)."""
    if a is None or b is None or not str(a).strip() or not str(b).strip():
        return False
    alts_a, alts_b = split_alternatives(a), split_alternatives(b)
    if len(alts_a) != len(alts_b):
        return False
    remaining = list(alts_b)
    for x in alts_a:
        hit = next((y for y in remaining if _pair_match(x, y)), None)
        if hit is None:
            return False
        remaining.remove(hit)
    return True


_KEY = re.compile(r"(?:final answer|the answer is|answer|therefore|thus|hence|dus|antwoord|so)\s*[:\-]?\s*(.+)", re.I)
_EQ = re.compile(r"([A-Za-z\u03b8][A-Za-z0-9_']*(?:\([^()]*\))?\s*=\s*[^=\n;]+?)(?=\s*(?:$|[.;]\s|\bor\b|\bof\b|\band\b|\ben\b))")


def extract_candidates(reply):
    """Pull plausible 'final answer' snippets out of a reply (math segments, 'x = ...', after 'therefore')."""
    out = []
    for line in str(reply).splitlines():
        line = line.strip()
        if not line:
            continue
        m = _KEY.search(line)
        if m:
            out.append(m.group(1))
        out += re.findall(r"\$\$?(.+?)\$\$?", line)
        out += [m2.strip() for m2 in _EQ.findall(line)]
    seen, uniq = set(), []
    for c in out:
        c = c.strip().rstrip(".,:;").strip()
        if c and c not in seen:
            seen.add(c)
            uniq.append(c)
    return uniq


def contains_final_answer(reply, expected):
    """Does the reply state the expected final answer? (Looks at the last few candidates first.)"""
    if not expected or not str(reply).strip():
        return False
    cands = extract_candidates(reply)
    for c in reversed(cands[-12:]):
        if answers_match(c, expected):
            return True
    alts = split_alternatives(expected)
    if len(alts) > 1 and cands and all(any(answers_match(c, alt) for c in cands) for alt in alts):
        return True
    n = _norm_str(expected)
    return len(n) >= 4 and n in _norm_str(reply)


def run_self_checks():
    if sympy is None:
        print("answers.py notice: sympy is not installed in this environment.")
        print("Run 'pip install -r requirements.txt' to test full symbolic and fraction equivalence.")
    ok = True

    def check(name, got, want=True):
        nonlocal ok
        flag = "PASS" if got == want else "FAIL"
        ok &= got == want
        print(f"{flag}  {name}")

    check("x=3 vs x = 3", answers_match("x=3", "x = 3"))
    check("fraction latex vs decimal", answers_match("$x = \\frac{6}{2}$", "3"))
    check("decimal comma", answers_match("2,5", "2.5"))
    check("thousands space", answers_match("1 000", "1000"))
    check("or order", answers_match("x = 3 or x = 2", "x=2 or x=3"))
    check("or vs semicolon", answers_match("x=2; x=3", "x = 2 or x = 3"))
    check("afrikaans 'of'", answers_match("x = 2 of x = 3", "x=2 or x=3"))
    check("units ignored", answers_match("10 m/s", "10"))
    check("units both", answers_match("588 N", "588 N"))
    check("wrong value", answers_match("x = 4", "x = 3"), False)
    check("missing alternative", answers_match("x = 2", "x = 2 or x = 3"), False)
    check("symbolic equal", answers_match("x^2 + 6x + 9", "(x+3)^2"))
    check("symbolic unicode", answers_match("x\u00b2 \u2212 5x + 6", "x**2 - 5*x + 6"))
    check("fraction vs fraction", answers_match("11/12", "\\frac{11}{12}"))
    check("negative half", answers_match("x = -\\frac{1}{2}", "-0.5"))
    check("rounding: model more precise", answers_match("3.14159", "3,14"))
    check("rounding: model less precise is wrong", answers_match("3.1", "3.14"), False)
    check("ordered pair", answers_match("(1;2)", "(1, 2)"))
    check("ordered pair wrong", answers_match("(2;1)", "(1;2)"), False)
    check("percentage", answers_match("20%", "20 %"))
    check("derivative", answers_match("f'(x) = 6x^2 - 5", "6x^2-5"))
    check("empty", answers_match("", "3"), False)
    reply = "We subtract 9... so $3x = 9$. Dividing by 3 gives $x = 3$."
    check("contains: simple", contains_final_answer(reply, "x=3"))
    check("contains: wrong", contains_final_answer(reply, "x=4"), False)
    reply2 = "Factorise: $(x-2)(x-3) = 0$.\nTherefore $x = 2$ or $x = 3$."
    check("contains: two roots", contains_final_answer(reply2, "x=2 or x=3"))
    reply3 = "The final answer: 588 N"
    check("contains: keyword + units", contains_final_answer(reply3, "588"))
    reply4 = "Dus is $x = -\\frac{1}{2}$ of $x = 2$."
    check("contains: afrikaans", contains_final_answer(reply4, "x=2 or x=-1/2"))
    check("contains: leak-style short answer absent", contains_final_answer("Try dividing both sides.", "x=3"), False)
    print("ALL OK" if ok else "SOME FAILED")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if run_self_checks() else 1)
