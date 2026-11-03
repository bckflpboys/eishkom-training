#!/usr/bin/env python3
"""
board.py - the blackboard: a tiny command language on a grid, plus a reference interpreter.

WHY THIS EXISTS
  The tutor model does NOT write HTML/CSS/JS. It sends a few short commands, one per string, and your
  app draws them. The app keeps the board state, so "erase B2" works without re-sending the board.
  This file is the reference for what each command means. Your Next.js app implements the same rules
  (draw with canvas/SVG + KaTeX), and the training pipeline uses this file to (1) check that commands
  in training data are valid and (2) generate the tool result text the model will see.

THE GRID
  Columns A-L (12), rows 1-30. A cell is like A1 or C10. A range is C10-C13 or C10:C13
  (a rectangle between two corners).

COMMANDS (one per string)
  write A1 "3x - 9 = 0"          put text in a cell (KaTeX like $x^2$ is allowed inside the text)
  write next "3x = 9"            put text in the first empty cell of column A (the app auto-places)
  box C10-C13 [color]            draw a box around the cells
  underline C10-C13 [color]      underline the cells
  highlight B2 [color]           highlight the cells
  circle B2 [color]              circle the cells
  arrow A1 -> A3 ["label"] [color]   arrow from one cell to another (shows where something comes from)
  erase B2                       erase text and marks in a cell or range
  erase all                      clear the board
  Colors: yellow red green blue orange purple black grey (every command has a sensible default).

USAGE
  python board.py demo            run a demo and print the ASCII board
  python board.py run 'write A1 "hi"' 'arrow A1 -> B2'      run commands from the command line
"""
from __future__ import annotations

import re
import sys

COLS = "ABCDEFGHIJKL"
MAX_ROW = 30
COLORS = {"yellow", "red", "green", "blue", "orange", "purple", "black", "grey"}
DEFAULT_COLOR = {"box": "blue", "underline": "red", "highlight": "yellow", "circle": "red", "arrow": "black"}

_CELL = r"[A-L](?:[1-9]|[12][0-9]|30)"
_RANGE = rf"{_CELL}(?:[-:]{_CELL})?"
_STR = r'"(?:[^"\\]|\\.)*"'

RE_WRITE = re.compile(rf'^write\s+(?P<target>next|{_CELL})\s+(?P<text>{_STR})\s*$')
RE_MARK = re.compile(rf'^(?P<verb>box|underline|highlight|circle)\s+(?P<range>{_RANGE})(?:\s+(?P<color>[a-z]+))?\s*$')
RE_ARROW = re.compile(rf'^arrow\s+(?P<a>{_CELL})\s*->\s*(?P<b>{_CELL})(?:\s+(?P<label>{_STR}))?(?:\s+(?P<color>[a-z]+))?\s*$')
RE_ERASE = re.compile(rf'^erase\s+(?P<target>all|{_RANGE})\s*$')


class BoardError(Exception):
    pass


def _unquote(s):
    return s[1:-1].replace('\\"', '"').replace("\\\\", "\\")


def cell_xy(cell):
    return COLS.index(cell[0]), int(cell[1:])


def xy_cell(c, r):
    return f"{COLS[c]}{r}"


def parse_range(text):
    """'C10-C13' -> (col1, row1, col2, row2) with col1<=col2, row1<=row2 (columns are 0-based)."""
    parts = re.split(r"[-:]", text)
    (c1, r1) = cell_xy(parts[0])
    (c2, r2) = cell_xy(parts[-1])
    return (min(c1, c2), min(r1, r2), max(c1, c2), max(r1, r2))


def range_str(rng):
    c1, r1, c2, r2 = rng
    a, b = xy_cell(c1, r1), xy_cell(c2, r2)
    if a == b:
        return a
    if c1 == c2 or r1 == r2:
        return f"{a}-{b}"
    return f"{a}:{b}"


def cells_in(rng):
    c1, r1, c2, r2 = rng
    return [xy_cell(c, r) for r in range(r1, r2 + 1) for c in range(c1, c2 + 1)]


def intersects(r1, r2):
    return not (r1[2] < r2[0] or r2[2] < r1[0] or r1[3] < r2[1] or r2[3] < r1[1])


def parse_command(line):
    """Parse one command string into an op dict, or raise BoardError with a helpful message."""
    s = line.strip()
    if not s:
        raise BoardError("empty command")
    verb = s.split()[0].lower()
    if verb == "write":
        m = RE_WRITE.match(s)
        if not m:
            raise BoardError('write needs a cell (A1-L30 or next) and quoted text, e.g. write A1 "3x = 9"')
        return {"op": "write", "target": m["target"], "text": _unquote(m["text"])}
    if verb in DEFAULT_COLOR and verb != "arrow":
        m = RE_MARK.match(s)
        if not m:
            raise BoardError(f"{verb} needs a cell or range such as C10 or C10-C13 and an optional color")
        color = m["color"] or DEFAULT_COLOR[verb]
        if color not in COLORS:
            raise BoardError(f"unknown color '{color}' (use {', '.join(sorted(COLORS))})")
        return {"op": verb, "range": parse_range(m["range"]), "color": color}
    if verb == "arrow":
        m = RE_ARROW.match(s)
        if not m:
            raise BoardError('arrow needs two cells, e.g. arrow A1 -> C3 "add 9 to both sides"')
        color = m["color"] or DEFAULT_COLOR["arrow"]
        if color not in COLORS:
            raise BoardError(f"unknown color '{color}' (use {', '.join(sorted(COLORS))})")
        return {"op": "arrow", "a": m["a"], "b": m["b"], "label": _unquote(m["label"]) if m["label"] else "", "color": color}
    if verb == "erase":
        m = RE_ERASE.match(s)
        if not m:
            raise BoardError("erase needs a cell, a range, or 'all'")
        return {"op": "erase", "target": "all" if m["target"] == "all" else parse_range(m["target"])}
    raise BoardError(f"unknown command '{verb}' (use write, box, underline, highlight, circle, arrow, erase)")


class Board:
    def __init__(self):
        self.cells = {}      # "A1" -> text
        self.marks = []      # dicts: {"type": "underline"|"box"|..., "range": (...), "color"} or arrows

    # -- applying ---------------------------------------------------------------------------------
    def apply(self, op):
        """Apply a parsed op. Returns a list of warning strings. Raises BoardError for real errors."""
        warnings = []
        kind = op["op"]
        if kind == "write":
            target = op["target"]
            if target == "next":
                target = next((f"A{r}" for r in range(1, MAX_ROW + 1) if f"A{r}" not in self.cells), None)
                if target is None:
                    raise BoardError("the board is full (column A has no empty cell)")
            self.cells[target] = op["text"]
        elif kind in ("box", "underline", "highlight", "circle"):
            if not any(c in self.cells for c in cells_in(op["range"])):
                warnings.append(f"{kind} {range_str(op['range'])} covers empty cells")
            self.marks.append({"type": kind, "range": op["range"], "color": op["color"]})
        elif kind == "arrow":
            for end in (op["a"], op["b"]):
                if end not in self.cells:
                    warnings.append(f"arrow endpoint {end} is empty")
            self.marks.append({"type": "arrow", "a": op["a"], "b": op["b"], "label": op["label"], "color": op["color"]})
        elif kind == "erase":
            if op["target"] == "all":
                self.cells.clear()
                self.marks.clear()
            else:
                rng = op["target"]
                gone = set(cells_in(rng))
                self.cells = {c: t for c, t in self.cells.items() if c not in gone}
                kept = []
                for m in self.marks:
                    if m["type"] == "arrow":
                        if m["a"] in gone or m["b"] in gone:
                            continue
                    elif intersects(m["range"], rng):
                        continue
                    kept.append(m)
                self.marks = kept
        return warnings

    # -- describing -------------------------------------------------------------------------------
    def describe(self):
        """Compact text of the board. This is what the model sees as the tool result."""
        if not self.cells and not self.marks:
            return "Board is empty."
        parts = []
        if self.cells:
            ordered = sorted(self.cells.items(), key=lambda kv: (cell_xy(kv[0])[1], cell_xy(kv[0])[0]))
            parts.append("Cells: " + "; ".join(f'{c}="{t}"' for c, t in ordered) + ".")
        if self.marks:
            out = []
            for m in self.marks:
                if m["type"] == "arrow":
                    lab = f' "{m["label"]}"' if m["label"] else ""
                    out.append(f"arrow {m['a']}->{m['b']}{lab}")
                else:
                    out.append(f"{m['type']} {range_str(m['range'])} ({m['color']})")
            parts.append("Marks: " + "; ".join(out) + ".")
        return " ".join(parts)

    def ascii(self, width=11):
        """A rough picture for debugging in a terminal (not the real drawing)."""
        used_rows = sorted({cell_xy(c)[1] for c in self.cells} | {r for m in self.marks if m["type"] != "arrow"
                           for r in (m["range"][1], m["range"][3])} | {cell_xy(x)[1] for m in self.marks
                           if m["type"] == "arrow" for x in (m["a"], m["b"])})
        if not used_rows:
            return "(empty board)"
        last = max(used_rows)
        header = "    " + "".join(f"{c:<{width + 1}}" for c in COLS[:max(4, max([cell_xy(c)[0] for c in self.cells] + [3]) + 1)])
        lines = [header]
        ncols = len(header.split())
        for r in range(1, last + 1):
            row = f"{r:>3} "
            for ci in range(ncols):
                t = self.cells.get(xy_cell(ci, r), "")
                t = (t[: width - 1] + "~") if len(t) > width else t
                row += f"{t:<{width + 1}}"
            lines.append(row.rstrip())
        lines.append("marks: " + (self.describe().split("Marks: ")[1] if "Marks: " in self.describe() else "none"))
        return "\n".join(lines)


def run_commands(board, commands):
    """Run a list of command strings on `board`.
    Returns (result_text, errors, warnings). Valid commands are applied even if a later one fails."""
    errors, warnings, applied = [], [], 0
    for i, line in enumerate(commands, 1):
        try:
            op = parse_command(line)
            warnings += [f"command {i}: {w}" for w in board.apply(op)]
            applied += 1
        except BoardError as e:
            errors.append(f"command {i}: {e}")
    state = board.describe()
    if errors:
        head = f"ERROR: {len(errors)} of {len(commands)} commands failed. " + " ".join(errors) + f" Applied {applied}."
    else:
        head = "OK."
    return f"{head} {state}", errors, warnings


def check_commands(commands, board=None):
    """Validate commands for training data. Returns (errors, warnings). Mutates `board` if given."""
    board = board if board is not None else Board()
    if not isinstance(commands, list) or not commands or not all(isinstance(c, str) for c in commands):
        return ["board.commands must be a non-empty list of strings"], []
    _, errors, warnings = run_commands(board, commands)
    return errors, warnings


def _demo():
    b = Board()
    cmds = ['write A1 "3x - 9 = 0"', 'write next "3x = 9"', 'arrow A1 -> A2 "add 9 to both sides"',
            'write A3 "x = 3"', 'underline A3', 'highlight B2 yellow', 'erase B2']
    text, errors, warnings = run_commands(b, cmds)
    print(text)
    print("warnings:", warnings)
    print(b.ascii())


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "demo":
        _demo()
    elif len(sys.argv) >= 3 and sys.argv[1] == "run":
        bd = Board()
        print(run_commands(bd, sys.argv[2:])[0])
        print(bd.ascii())
    else:
        print(__doc__)
