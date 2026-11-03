#!/usr/bin/env python3
"""
tools_sim.py - compute REAL tool results for training records.

WHY THIS EXISTS
  When a teacher model writes a training conversation that uses a tool, the tool RESULT it writes is
  a guess ("hallucinated"). If your tutor model learns from guessed results, it learns wrong habits.
  So after the teacher writes a record, this file re-runs every tool call in code and overwrites the
  results with the real ones:
    calculator        -> exact arithmetic (SymPy)
    plot_function     -> real intercepts / vertex (SymPy)
    board             -> the real board state (board.py)
    make_cover_page   -> a stub file name (your app really makes the PDF)
    search_curriculum -> a real BM25 search of YOUR text (retrieval.py), if you built an index
    web_search        -> cannot be simulated; the record is flagged as unverified

  Your app must return results in the SAME text format at run time, or the model will be confused.

USAGE
  python tools_sim.py            run self-checks
  from tools_sim import fill_tool_results
"""
from __future__ import annotations

import copy
import hashlib
import json
import re

import board as boardmod
import retrieval

try:
    import sympy
    from sympy.parsing.sympy_parser import (parse_expr, standard_transformations,
                                            implicit_multiplication_application, convert_xor)
    _T = standard_transformations + (implicit_multiplication_application, convert_xor)
except ImportError:
    sympy = None

from answers import _clean

_ALLOWED_NAMES = {"sqrt", "sin", "cos", "tan", "asin", "acos", "atan", "log", "ln", "exp", "pi", "e", "abs"}


def _calc_locals():
    deg = sympy.pi / 180
    return {
        "sqrt": sympy.sqrt, "exp": sympy.exp, "pi": sympy.pi, "e": sympy.E, "abs": sympy.Abs,
        "sin": lambda x: sympy.sin(x * deg), "cos": lambda x: sympy.cos(x * deg), "tan": lambda x: sympy.tan(x * deg),
        "asin": lambda x: sympy.asin(x) / deg, "acos": lambda x: sympy.acos(x) / deg, "atan": lambda x: sympy.atan(x) / deg,
        "log": lambda x: sympy.log(x, 10), "ln": sympy.log,
    }


def _fmt_number(v):
    """Format a SymPy number the way the tool tells the model."""
    if v.is_Integer:
        return str(int(v))
    if v.is_Rational:
        p, q = v.p, v.q
        d = q
        for f in (2, 5):
            while d % f == 0:
                d //= f
        if d == 1:                                     # terminating decimal
            return format(float(v), "f").rstrip("0").rstrip(".")
        return f"{p}/{q} = {float(v):.10g}"
    return f"{float(sympy.N(v, 15)):.10g}"


def calculator(args):
    """Exact arithmetic. Trig works in degrees, log is base 10, ln is natural log."""
    if sympy is None:
        return None
    expr = args.get("expression")
    if not isinstance(expr, str) or not expr.strip():
        return "ERROR: expression is empty."
    s = _clean(expr).replace("^", "**")
    s = re.sub(r"(?<=\d)\s(?=\d{3}(?!\d))", "", s)
    names = set(re.findall(r"[A-Za-z_]+", s))
    bad = names - _ALLOWED_NAMES
    if bad:
        return f"ERROR: the calculator only does numbers; unknown name(s): {', '.join(sorted(bad))}."
    try:
        val = parse_expr(s, local_dict=_calc_locals(), transformations=_T, evaluate=True)
        val = sympy.nsimplify(val, rational=True) if val.is_Float else sympy.simplify(val)
        if val.free_symbols:
            return "ERROR: the calculator only does numbers."
        if val.is_infinite or val is sympy.nan or val == sympy.zoo:
            return "ERROR: undefined (division by zero?)."
        return _fmt_number(val)
    except Exception as e:                       # noqa: BLE001
        return f"ERROR: could not read the expression ({type(e).__name__})."


def _num(v):
    try:
        f = float(v)
    except Exception:                            # noqa: BLE001
        return str(v)
    return int(f) if abs(f - round(f)) < 1e-9 else round(f, 4)


def plot_function(args):
    """Returns JSON text with an image id and real key features (so a text-only model can 'see' the graph)."""
    if sympy is None:
        return None
    expr = args.get("expression")
    if not isinstance(expr, str) or not expr.strip():
        return "ERROR: expression is empty."
    s = _clean(expr)
    s = re.sub(r"^\s*(?:y|f\(x\))\s*=\s*", "", s).replace("^", "**")
    x = sympy.Symbol("x", real=True)
    try:
        f = parse_expr(s, local_dict={"x": x, "pi": sympy.pi, "e": sympy.E, "sqrt": sympy.sqrt}, transformations=_T)
        if f.free_symbols - {x}:
            return "ERROR: only the variable x is allowed."
        lo, hi = args.get("x_min"), args.get("x_max")
        roots = sympy.solveset(sympy.Eq(f, 0), x, domain=sympy.S.Reals)
        roots = sorted(roots, key=lambda r: float(r)) if roots.is_FiniteSet else []
        if lo is not None and hi is not None:
            roots = [r for r in roots if float(lo) <= float(r) <= float(hi)]
        out = {"image_id": "plot_" + hashlib.sha1((s + str(lo) + str(hi)).encode()).hexdigest()[:6],
               "x_intercepts": [_num(r) for r in roots], "y_intercept": _num(f.subs(x, 0))}
        poly = sympy.Poly(f, x) if f.is_polynomial(x) else None
        if poly is not None and poly.degree() == 2:
            a, b = poly.all_coeffs()[0], poly.all_coeffs()[1]
            xv = -b / (2 * a)
            out["vertex"] = [_num(xv), _num(f.subs(x, xv))]
        return json.dumps(out)
    except Exception as e:                       # noqa: BLE001
        return f"ERROR: could not plot that ({type(e).__name__})."


def make_cover_page(args):
    title = args.get("title")
    if not isinstance(title, str) or not title.strip():
        return "ERROR: title is required."
    return json.dumps({"file": "cover_" + hashlib.sha1(json.dumps(args, sort_keys=True).encode()).hexdigest()[:6] + ".pdf"})


def search_curriculum(args, index):
    if index is None:
        return None
    q = args.get("query")
    if not isinstance(q, str) or not q.strip():
        return "ERROR: query is empty."
    lang = args.get("language")
    res = retrieval.search(index, q, k=3, subject=args.get("subject"), grade=args.get("grade"), language=lang)
    if not res and (args.get("subject") or args.get("grade") or lang):    # loosen filters once
        res = retrieval.search(index, q, k=3)
    return retrieval.format_results(res)


def run_tool(name, args, board, index=None):
    """Return the real result text for one tool call, or None if it cannot be simulated."""
    if name == "calculator":
        return calculator(args)
    if name == "plot_function":
        return plot_function(args)
    if name == "make_cover_page":
        return make_cover_page(args)
    if name == "board":
        cmds = args.get("commands")
        if not isinstance(cmds, list):
            return "ERROR: commands must be a list of strings."
        return boardmod.run_commands(board, [str(c) for c in cmds])[0]
    if name == "search_curriculum":
        return search_curriculum(args, index)
    return None                                   # web_search etc.


def _args_of(tc):
    a = tc["function"].get("arguments")
    if isinstance(a, str):
        try:
            a = json.loads(a)
        except json.JSONDecodeError:
            a = {}
    return a if isinstance(a, dict) else {}


def fill_tool_results(record, index=None):
    """Overwrite every tool message in a record with the REAL result. Returns (new_record, notes).
    `notes` lists tools whose results could not be recomputed (they stay as the teacher wrote them)."""
    rec = copy.deepcopy(record)
    notes, pending = [], []
    bd = boardmod.Board()
    for m in rec.get("messages", []):
        if m.get("role") == "assistant" and m.get("tool_calls"):
            pending = list(m["tool_calls"])
        elif m.get("role") == "tool" and pending:
            tc = pending.pop(0)
            name = tc["function"]["name"]
            result = run_tool(name, _args_of(tc), bd, index)
            if result is None:
                notes.append(name)
                continue
            m["content"] = result
            m["name"] = name
            if tc.get("id") and not m.get("tool_call_id"):
                m["tool_call_id"] = tc["id"]
    return rec, sorted(set(notes))


def _self_checks():
    if sympy is None:
        print("tools_sim.py self-checks skipped: sympy is not installed. Run 'pip install -r requirements.txt' to enable exact calculator arithmetic.")
        return True
    ok = True

    def check(name, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print(("PASS  " if good else f"FAIL  (got {got!r}, want {want!r})  ") + name)

    check("17.5 * 23.4", calculator({"expression": "17.5 * 23.4"}), "409.5")
    check("integer", calculator({"expression": "12*7"}), "84")
    check("1/3 repeating", calculator({"expression": "1/3"}), "1/3 = 0.3333333333")
    check("fraction sum", calculator({"expression": "3/4 + 1/6"}), "11/12 = 0.9166666667")
    check("terminating", calculator({"expression": "7/4"}), "1.75")
    check("sqrt", calculator({"expression": "sqrt(2)"}), "1.414213562")
    check("sin 30 degrees", calculator({"expression": "sin(30)"}), "1/2 = 0.5") if False else None
    r = calculator({"expression": "sin(30)"})
    check("sin 30 degrees", r in ("0.5", "1/2 = 0.5"), True)
    check("log base 10", calculator({"expression": "log(1000)"}), "3")
    check("latex fraction", calculator({"expression": "\\frac{3}{4} + \\frac{1}{4}"}), "1")
    check("unknown name refused", calculator({"expression": "x + 1"}).startswith("ERROR"), True)
    check("division by zero", calculator({"expression": "1/0"}).startswith("ERROR"), True)
    check("code injection refused", calculator({"expression": "__import__('os').system('ls')"}).startswith("ERROR"), True)
    pf = json.loads(plot_function({"expression": "x^2 - 4*x + 3", "x_min": -1, "x_max": 5}))
    check("plot intercepts", pf["x_intercepts"], [1, 3])
    check("plot y-intercept", pf["y_intercept"], 3)
    check("plot vertex", pf["vertex"], [2, -1])
    pl = json.loads(plot_function({"expression": "2x + 1"}))
    check("line x-intercept", pl["x_intercepts"], [-0.5])
    check("cover page", json.loads(make_cover_page({"title": "T"}))["file"].endswith(".pdf"), True)
    rec = {"messages": [
        {"role": "user", "content": "q"},
        {"role": "assistant", "content": "", "tool_calls": [{"id": "c1", "type": "function", "function": {"name": "board", "arguments": {"commands": ['write A1 "x"']}}}]},
        {"role": "tool", "content": "WRONG"},
        {"role": "assistant", "content": "", "tool_calls": [{"id": "c2", "type": "function", "function": {"name": "calculator", "arguments": '{"expression": "2+2"}'}}]},
        {"role": "tool", "content": "five"},
        {"role": "assistant", "content": "", "tool_calls": [{"id": "c3", "type": "function", "function": {"name": "web_search", "arguments": {"query": "x"}}}]},
        {"role": "tool", "content": "whatever"},
        {"role": "assistant", "content": "done"}]}
    new, notes = fill_tool_results(rec)
    check("board result filled", new["messages"][2]["content"], 'OK. Cells: A1="x".')
    check("calc result filled", new["messages"][4]["content"], "4")
    check("web_search left alone + noted", (new["messages"][6]["content"], notes), ("whatever", ["web_search"]))
    check("tool_call_id added", new["messages"][2].get("tool_call_id"), "c1")
    print("ALL OK" if ok else "SOME FAILED")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if _self_checks() else 1)
