#!/usr/bin/env python3
"""
grpo_rewards.py - reward functions for GRPO ("let the model try, reward what is right").

    python training/grpo_rewards.py        # self-test

WHAT GRPO IS (plain words)
  For each question the model writes several attempts. A reward function scores each attempt; attempts that
  scored above the group's average are made more likely, the rest less likely. No human writes the good
  answers: only the REWARD FUNCTION knows what "good" means. That works when "good" can be checked by code:
  a maths answer is right or wrong; a reply is in the right language or not; the answer was leaked or not.
  It does NOT work for "was that a nice explanation?" (use SFT data and DPO pairs for that).

HOW TO USE
  Unsloth has an official GRPO notebook for Qwen. Replace its reward functions with these, and make your
  dataset columns match the keyword arguments below (answer, language, policy, max_words).
  Each function takes (prompts, completions, **columns) and returns one float per completion.
  completions are chat-style: [{"role": "assistant", "content": "..."}].
  Do GRPO LAST and only for maths with checkable answers. SFT + DPO fix most problems more cheaply.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tutor_data as td  # noqa: E402
from answers import contains_final_answer  # noqa: E402


def _text(c):
    return c[0]["content"] if isinstance(c, list) else str(c)


def _split(t):
    """(reasoning, reply). Works whether or not the opening <think> tag is in the completion."""
    if "</think>" in t:
        a, b = t.split("</think>", 1)
        return a.replace("<think>", "").strip(), b.strip()
    return "", t.strip()


def reward_correct(prompts, completions, answer=None, **kw):
    """+2 if the reply states the right final answer, else 0 (the answer is in the dataset column `answer`)."""
    return [2.0 if (a and contains_final_answer(_split(_text(c))[1], a)) else 0.0 for c, a in zip(completions, answer or [None] * len(completions))]


def reward_format(prompts, completions, **kw):
    """+0.5 when the thinking block is closed exactly once and a reply follows it; -1 for a runaway thought."""
    out = []
    for c in completions:
        t = _text(c)
        if t.count("</think>") == 1 and _split(t)[1]:
            out.append(0.5)
        elif "</think>" not in t and len(t.split()) > 1200:
            out.append(-1.0)
        else:
            out.append(0.0)
    return out


def reward_language(prompts, completions, language=None, **kw):
    """+1 if the reply is in the expected language (en / af)."""
    out = []
    for c, lang in zip(completions, language or [None] * len(completions)):
        g = td.guess_lang(_split(_text(c))[1])
        out.append(1.0 if (lang and (g == lang or g == "unknown")) else 0.0)
    return out


def reward_no_leak(prompts, completions, policy=None, answer=None, **kw):
    """-2 if a hint_only/guided reply gives the answer away."""
    out = []
    for c, pol, a in zip(completions, policy or [None] * len(completions), answer or [None] * len(completions)):
        leaked = pol in ("hint_only", "guided") and a and contains_final_answer(_split(_text(c))[1], a)
        out.append(-2.0 if leaked else 0.0)
    return out


def reward_length(prompts, completions, max_words=None, **kw):
    """-0.5 when the reply is more than 20% over the word limit (small models ramble)."""
    return [(-0.5 if (m and td.words(_split(_text(c))[1]) > 1.2 * m) else 0.0) for c, m in zip(completions, max_words or [None] * len(completions))]


ALL = [reward_correct, reward_format, reward_language, reward_no_leak, reward_length]


def _self_test():
    good = [{"role": "assistant", "content": "<think>5x = 25, x = 5</think>Subtract 7, then divide by 5: $x = 5$."}]
    bad = [{"role": "assistant", "content": "<think>hmm</think>It is $x = 6$."}]
    leak = [{"role": "assistant", "content": "<think>ok</think>The answer is x = 5. Does that help?"}]
    cols = dict(answer=["x=5"], language=["en"], policy=["full_solution"], max_words=[60])
    checks = [
        ("correct reply rewarded", reward_correct([None], [good], **cols) == [2.0]),
        ("wrong reply not rewarded", reward_correct([None], [bad], **cols) == [0.0]),
        ("format ok", reward_format([None], [good]) == [0.5]),
        ("language ok", reward_language([None], [good], **cols) == [1.0]),
        ("leak penalised under guided", reward_no_leak([None], [leak], policy=["guided"], answer=["x=5"]) == [-2.0]),
        ("no leak penalty for full_solution", reward_no_leak([None], [leak], policy=["full_solution"], answer=["x=5"]) == [0.0]),
        ("length ok", reward_length([None], [good], max_words=[60]) == [0.0]),
    ]
    for name, ok in checks:
        print(("PASS  " if ok else "FAIL  ") + name)
    print("ALL OK" if all(ok for _, ok in checks) else "SOME FAILED")
    return all(ok for _, ok in checks)


if __name__ == "__main__":
    sys.exit(0 if _self_test() else 1)
