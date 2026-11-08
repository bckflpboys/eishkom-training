# -*- coding: utf-8 -*-
"""
Generator for DBE Mathematics Grade 12 Paper 1 May/June 2023 JSONL dataset.
Universal Document & Visual Extraction Standard (UDVES).
"""

import json
import os
import re

SOURCE_ID = "dbe-mathematics-g12-p1-2023-may"
PAIR_SOURCE_ID = "dbe-mathematics-g12-p1-2023-may-memo"
SUBJECT = "mathematics"
GRADE = 12
LANGUAGE = "en"
TRACK = "core_maths"
LICENCE = "DBE copyright - check terms"
ATTRIBUTION = "Department of Basic Education"

items = [
    # ==========================================
    # QUESTION 1 (24 marks)
    # ==========================================
    {
        "question_ref": "1.1.1",
        "marks": 3,
        "topic": "Algebra - Quadratic Equations",
        "passage": "",
        "question": "Solve for $x$:\n$$x^2 - 7x + 12 = 0$$",
        "memo": "$$x^2 - 7x + 12 = 0$$\n$$(x - 4)(x - 3) = 0$$\n$$x = 4 \\quad \\text{or} \\quad x = 3$$\n\n* $\\checkmark$ factors\n* $\\checkmark x = 4$\n* $\\checkmark x = 3$\n\n*(Note: Answer only: Full Marks)*",
        "final_answer": "x = 4 or x = 3",
        "needs_review": False,
    },
    {
        "question_ref": "1.1.2",
        "marks": 4,
        "topic": "Algebra - Quadratic Equations (Quadratic Formula)",
        "passage": "",
        "question": "Solve for $x$ (correct to TWO decimal places):\n$$x(3x + 5) = 1$$",
        "memo": "$$3x^2 + 5x - 1 = 0$$\n$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$$\n$$x = \\frac{-5 \\pm \\sqrt{5^2 - 4(3)(-1)}}{2(3)}$$\n$$x = \\frac{-5 \\pm \\sqrt{37}}{6}$$\n$$x = 0{,}18 \\quad \\text{or} \\quad x = -1{,}85$$\n\n* $\\checkmark$ standard form\n* $\\checkmark$ substitution into the correct formula\n* $\\checkmark x = 0{,}18$\n* $\\checkmark x = -1{,}85$",
        "final_answer": "x = 0.18 or x = -1.85",
        "needs_review": False,
    },
    {
        "question_ref": "1.1.3",
        "marks": 4,
        "topic": "Algebra - Quadratic Inequalities",
        "passage": "",
        "question": "Solve for $x$:\n$$x^2 < -2x + 15$$",
        "memo": "$$x^2 + 2x - 15 < 0$$\n$$(x - 3)(x + 5) < 0$$\nCritical values: $x = 3$ or $x = -5$\n$$-5 < x < 3$$\n\n**OR/OF**\n$$x \\in (-5 ; 3)$$\n\n* $\\checkmark$ standard form\n* $\\checkmark$ critical values\n* $\\checkmark\\checkmark$ answer",
        "final_answer": "-5 < x < 3",
        "needs_review": False,
    },
    {
        "question_ref": "1.1.4",
        "marks": 4,
        "topic": "Algebra - Surd Equations",
        "passage": "",
        "question": "Solve for $x$:\n$$\\sqrt{2(1 - x)} = x - 1$$",
        "memo": "$$\\sqrt{2(1 - x)} = x - 1$$\n$$(\\sqrt{2(1 - x)})^2 = (x - 1)^2$$\n$$2(1 - x) = x^2 - 2x + 1$$\n$$2 - 2x = x^2 - 2x + 1$$\n$$x^2 - 1 = 0$$\n$$(x - 1)(x + 1) = 0$$\n$$x = 1 \\quad \\text{or} \\quad x = -1$$\n\nCheck solutions:\nFor $x = 1$: $\\text{LHS} = \\sqrt{2(1 - 1)} = 0$, $\\text{RHS} = 1 - 1 = 0$ (valid)\nFor $x = -1$: $\\text{LHS} = \\sqrt{2(1 - (-1))} = \\sqrt{4} = 2$, $\\text{RHS} = -1 - 1 = -2 \\neq 2$ (invalid)\n$$\\therefore x = 1 \\quad \\text{and} \\quad x \\neq -1$$\n\n* $\\checkmark$ squaring both sides\n* $\\checkmark$ simplification\n* $\\checkmark$ standard form\n* $\\checkmark$ answer with selection",
        "final_answer": "x = 1",
        "needs_review": False,
    },
    {
        "question_ref": "1.2",
        "marks": 6,
        "topic": "Algebra - Simultaneous Equations",
        "passage": "",
        "question": "Solve for $x$ and $y$ simultaneously:\n$$3^{x+y} = 27 \\quad \\text{and} \\quad x^2 + y^2 = 17$$",
        "memo": "$$3^{x+y} = 27$$\n$$3^{x+y} = 3^3$$\n$$x + y = 3 \\quad \\dots (1)$$\n$$y = 3 - x$$\n\nSubstitute into $x^2 + y^2 = 17$:\n$$x^2 + (3 - x)^2 = 17$$\n$$x^2 + 9 - 6x + x^2 = 17$$\n$$2x^2 - 6x - 8 = 0$$\n$$x^2 - 3x - 4 = 0$$\n$$(x - 4)(x + 1) = 0$$\n$$x = 4 \\quad \\text{or} \\quad x = -1$$\n$$y = 3 - (4) = -1 \\quad \\text{or} \\quad y = 3 - (-1) = 4$$\n\n**OR/OF**\n$$x = 3 - y$$\n$$(3 - y)^2 + y^2 = 17$$\n$$9 - 6y + y^2 + y^2 = 17$$\n$$2y^2 - 6y - 8 = 0$$\n$$y^2 - 3y - 4 = 0$$\n$$(y - 4)(y + 1) = 0$$\n$$y = 4 \\quad \\text{or} \\quad y = -1$$\n$$x = 3 - 4 = -1 \\quad \\text{or} \\quad x = 3 - (-1) = 4$$\n\n* $\\checkmark 3^{x+y} = 3^3$\n* $\\checkmark x + y = 3$\n* $\\checkmark$ substitution\n* $\\checkmark$ standard form\n* $\\checkmark x$-values\n* $\\checkmark y$-values",
        "final_answer": "(x = 4, y = -1) or (x = -1, y = 4)",
        "needs_review": False,
    },
    {
        "question_ref": "1.3",
        "marks": 3,
        "topic": "Algebra - Surds / Telescoping Series",
        "passage": "",
        "question": "Determine, without the use of a calculator, the value of:\n$$\\frac{1}{\\sqrt{1} + \\sqrt{2}} + \\frac{1}{\\sqrt{2} + \\sqrt{3}} + \\frac{1}{\\sqrt{3} + \\sqrt{4}} + \\dots + \\frac{1}{\\sqrt{99} + \\sqrt{100}}$$",
        "memo": "Rationalise each term by multiplying numerator and denominator by the conjugate:\n$$\\frac{1}{\\sqrt{k} + \\sqrt{k+1}} = \\frac{\\sqrt{k+1} - \\sqrt{k}}{(\\sqrt{k+1} + \\sqrt{k})(\\sqrt{k+1} - \\sqrt{k})} = \\frac{\\sqrt{k+1} - \\sqrt{k}}{(k+1) - k} = \\sqrt{k+1} - \\sqrt{k}$$\n\nApplying this to each term in the sum:\n$$\\frac{1}{\\sqrt{1} + \\sqrt{2}} = \\sqrt{2} - \\sqrt{1} = \\sqrt{2} - 1$$\n$$\\frac{1}{\\sqrt{2} + \\sqrt{3}} = \\sqrt{3} - \\sqrt{2}$$\n$$\\frac{1}{\\sqrt{3} + \\sqrt{4}} = \\sqrt{4} - \\sqrt{3}$$\n$$\\dots$$\n$$\\frac{1}{\\sqrt{99} + \\sqrt{100}} = \\sqrt{100} - \\sqrt{99} = 10 - \\sqrt{99}$$\n\nSumming all the rationalised terms:\n$$(\\sqrt{2} - 1) + (\\sqrt{3} - \\sqrt{2}) + (\\sqrt{4} - \\sqrt{3}) + \\dots + (10 - \\sqrt{99})$$\n$$= -1 + 10 = 9$$\n\n* $\\checkmark$ rationalisation\n* $\\checkmark$ simplification ($-1 + 10$)\n* $\\checkmark$ answer ($9$)",
        "final_answer": "9",
        "needs_review": False,
    },

    # ==========================================
    # QUESTION 2 (17 marks)
    # ==========================================
    {
        "question_ref": "2.1.1",
        "marks": 2,
        "topic": "Number Patterns - Geometric Series Convergence",
        "passage": "Given the geometric series: $\\frac{1}{5} + \\frac{1}{15} + \\frac{1}{45} + \\dots$",
        "question": "Is this a convergent geometric series? Justify your answer with the necessary calculations.",
        "memo": "$$r = \\frac{T_2}{T_1} = \\frac{\\frac{1}{15}}{\\frac{1}{5}} = \\frac{1}{3}$$\n$$-1 < \\frac{1}{3} < 1$$\n$\\therefore$ the series is convergent since $-1 < r < 1$.\n\n* $\\checkmark r = \\frac{1}{3}$\n* $\\checkmark$ answer (any indicator of convergence)",
        "final_answer": "Yes, convergent since -1 < r = 1/3 < 1",
        "needs_review": False,
    },
    {
        "question_ref": "2.1.2",
        "marks": 2,
        "topic": "Number Patterns - Sum to Infinity",
        "passage": "Given the geometric series: $\\frac{1}{5} + \\frac{1}{15} + \\frac{1}{45} + \\dots$",
        "question": "Calculate the sum to infinity of this series.",
        "memo": "$$S_\\infty = \\frac{a}{1 - r}$$\n$$a = \\frac{1}{5}, \\quad r = \\frac{1}{3}$$\n$$S_\\infty = \\frac{\\frac{1}{5}}{1 - \\frac{1}{3}} = \\frac{\\frac{1}{5}}{\\frac{2}{3}} = \\frac{1}{5} \\times \\frac{3}{2} = \\frac{3}{10} = 0{,}3$$\n\n* $\\checkmark$ substitution\n* $\\checkmark$ answer ($\\frac{3}{10}$ or $0{,}3$)",
        "final_answer": "3/10",
        "needs_review": False,
    },
    {
        "question_ref": "2.2.1",
        "marks": 2,
        "topic": "Number Patterns - Combined Sequences (Next Terms)",
        "passage": "An arithmetic and a geometric sequence are combined to form the pattern, which is given by:\n$$P_n = x \\ ; \\ \\frac{1}{3} \\ ; \\ 2x \\ ; \\ \\frac{1}{9} \\ ; \\ 3x \\ ; \\ \\frac{1}{27} \\ ; \\ \\dots$$",
        "question": "Write down the next TWO terms of the pattern.",
        "memo": "Odd terms form an arithmetic sequence: $x ; 2x ; 3x ; \\dots$\nEven terms form a geometric sequence: $\\frac{1}{3} ; \\frac{1}{9} ; \\frac{1}{27} ; \\dots$\n\nNext two terms:\n$$T_7 = 4x$$\n$$T_8 = \\frac{1}{27} \\times \\frac{1}{3} = \\frac{1}{81}$$\n\n* $\\checkmark 4x$\n* $\\checkmark \\frac{1}{81}$",
        "final_answer": "4x ; 1/81",
        "needs_review": False,
    },
    {
        "question_ref": "2.2.2",
        "marks": 2,
        "topic": "Number Patterns - Combined Sequences (Odd Terms General Term)",
        "passage": "An arithmetic and a geometric sequence are combined to form the pattern, which is given by:\n$$P_n = x \\ ; \\ \\frac{1}{3} \\ ; \\ 2x \\ ; \\ \\frac{1}{9} \\ ; \\ 3x \\ ; \\ \\frac{1}{27} \\ ; \\ \\dots$$",
        "question": "Determine the general term ($T_n$) for the odd terms of this pattern. Write down your answer in terms of $x$.",
        "memo": "Odd terms: $x ; 2x ; 3x ; \\dots$\nThis is an arithmetic sequence with first term $a = x$ and common difference $d = x$:\n$$T_n = a + (n - 1)d$$\n$$T_n = x + (n - 1)x = x + xn - x = xn$$\n\n* $\\checkmark$ substitution\n* $\\checkmark$ answer ($T_n = xn$ or $nx$)",
        "final_answer": "T_n = xn",
        "needs_review": False,
    },
    {
        "question_ref": "2.2.3",
        "marks": 3,
        "topic": "Number Patterns - Combined Sequences (Term Value)",
        "passage": "An arithmetic and a geometric sequence are combined to form the pattern, which is given by:\n$$P_n = x \\ ; \\ \\frac{1}{3} \\ ; \\ 2x \\ ; \\ \\frac{1}{9} \\ ; \\ 3x \\ ; \\ \\frac{1}{27} \\ ; \\ \\dots$$",
        "question": "Calculate the value of $P_{26}$.",
        "memo": "$P_{26}$ is an even term, corresponding to term $\\frac{26}{2} = 13$ of the geometric sequence:\nGeometric sequence: $\\frac{1}{3} ; \\frac{1}{9} ; \\frac{1}{27} ; \\dots$\nHere $a = \\frac{1}{3}$ and $r = \\frac{1}{3}$, with $n = 13$:\n$$T_{13} = a r^{n-1} = \\left(\\frac{1}{3}\\right)\\left(\\frac{1}{3}\\right)^{12} = \\left(\\frac{1}{3}\\right)^{13} = 3^{-13} = \\frac{1}{1\\,594\\,323} \\approx 6{,}27 \\times 10^{-7}$$\n\n* $\\checkmark n = 13$\n* $\\checkmark r = \\frac{1}{3}$\n* $\\checkmark$ answer ($\\left(\\frac{1}{3}\\right)^{13}$ or $3^{-13}$ or $\\frac{1}{1\\,594\\,323}$)",
        "final_answer": "(1/3)^13",
        "needs_review": False,
    },
    {
        "question_ref": "2.2.4",
        "marks": 6,
        "topic": "Number Patterns - Combined Sequences (Sigma Sum)",
        "passage": "An arithmetic and a geometric sequence are combined to form the pattern, which is given by:\n$$P_n = x \\ ; \\ \\frac{1}{3} \\ ; \\ 2x \\ ; \\ \\frac{1}{9} \\ ; \\ 3x \\ ; \\ \\frac{1}{27} \\ ; \\ \\dots$$",
        "question": "If $\\sum_{n=1}^{21} P_n = 33{,}5$, determine the value of $x$.",
        "memo": "In the first 21 terms of $P_n$, there are 11 odd terms (arithmetic sequence) and 10 even terms (geometric sequence):\n$$\\sum_{n=1}^{21} P_n = S_{11 \\text{ (arithmetic)}} + S_{10 \\text{ (geometric)}}$$\n\nArithmetic sum ($n = 11$, $a = x$, $d = x$):\n$$S_{11} = \\frac{11}{2}[2a + (11 - 1)d] = \\frac{11}{2}[2x + 10x] = \\frac{11}{2}(12x) = 66x$$\n\nGeometric sum ($n = 10$, $a = \\frac{1}{3}$, $r = \\frac{1}{3}$):\n$$S_{10} = \\frac{a(1 - r^{10})}{1 - r} = \\frac{\\frac{1}{3}\\left[1 - \\left(\\frac{1}{3}\\right)^{10}\\right]}{1 - \\frac{1}{3}} = \\frac{\\frac{1}{3}\\left[1 - \\left(\\frac{1}{3}\\right)^{10}\\right]}{\\frac{2}{3}} = \\frac{1}{2}\\left[1 - \\left(\\frac{1}{3}\\right)^{10}\\right] \\approx 0{,}5$$\n\nEquating total sum to $33{,}5$:\n$$66x + 0{,}5 = 33{,}5$$\n$$66x = 33$$\n$$x = \\frac{33}{66} = \\frac{1}{2} = 0{,}5$$\n\n* $\\checkmark S_{11} + S_{10}$\n* $\\checkmark$ arithmetic sum formula\n* $\\checkmark$ geometric sum formula\n* $\\checkmark 66x + 0{,}5$\n* $\\checkmark$ equating to $33{,}5$\n* $\\checkmark$ answer ($x = \\frac{1}{2}$)",
        "final_answer": "x = 1/2",
        "needs_review": False,
    },

    # ==========================================
    # QUESTION 3 (9 marks)
    # ==========================================
    {
        "question_ref": "3.1",
        "marks": 6,
        "topic": "Number Patterns - Quadratic Sequence General Term",
        "passage": "A quadratic sequence has the following properties:\n• The second difference is 10.\n• The first two terms are equal, i.e. $T_1 = T_2$.\n• $T_1 + T_2 + T_3 = 28$",
        "question": "Show that the general term of the sequence is $T_n = 5n^2 - 15n + 16$.",
        "memo": "Let the terms be $T_1 = x$, $T_2 = x$, and $T_3$.\nFirst differences: $T_2 - T_1 = x - x = 0$, and $T_3 - T_2 = T_3 - x$.\nSecond difference is 10:\n$$(T_3 - x) - 0 = 10 \\implies T_3 = x + 10$$\n\nGiven $T_1 + T_2 + T_3 = 28$:\n$$x + x + (x + 10) = 28$$\n$$3x + 10 = 28$$\n$$3x = 18 \\implies x = 6$$\nSo $T_1 = 6$, $T_2 = 6$, $T_3 = 16$.\n\nFor general term $T_n = an^2 + bn + c$:\n$$2a = 10 \\implies a = 5$$\n$$3a + b = T_2 - T_1 = 0 \\implies 3(5) + b = 0 \\implies b = -15$$\n$$a + b + c = T_1 = 6 \\implies 5 - 15 + c = 6 \\implies c = 16$$\n$$\\therefore T_n = 5n^2 - 15n + 16$$\n\n**OR/OF**\n$$2a = 10 \\implies a = 5$$\n$$T_1 = a + b + c = 5 + b + c$$\n$$T_2 = 4a + 2b + c = 20 + 2b + c$$\n$$T_3 = 9a + 3b + c = 45 + 3b + c$$\nSince $T_1 = T_2$:\n$$5 + b + c = 20 + 2b + c \\implies b = -15$$\nThen:\n$$T_1 = 5 - 15 + c = c - 10$$\n$$T_2 = c - 10$$\n$$T_3 = 45 - 45 + c = c$$\n$$T_1 + T_2 + T_3 = 28$$\n$$(c - 10) + (c - 10) + c = 28$$\n$$3c - 20 = 28 \\implies 3c = 48 \\implies c = 16$$\n$$\\therefore T_n = 5n^2 - 15n + 16$$\n\n* $\\checkmark 2a = 10$\n* $\\checkmark 3a + b = 0$\n* $\\checkmark T_3 = x + 10$\n* $\\checkmark 2x + T_3 = 28$\n* $\\checkmark x = 6$\n* $\\checkmark 5 - 15 + c = 6$\n\n**OR/OF**\n* $\\checkmark 2a = 10$\n* $\\checkmark 5 + b + c = 20 + 2b + c$\n* $\\checkmark T_1 = c - 10$\n* $\\checkmark T_2 = c - 10$\n* $\\checkmark 3c - 20 = 28$\n* $\\checkmark c = 16$",
        "final_answer": "T_n = 5n^2 - 15n + 16",
        "needs_review": False,
    },
    {
        "question_ref": "3.2",
        "marks": 3,
        "topic": "Number Patterns - Quadratic Sequence Term Verification",
        "passage": "A quadratic sequence has the general term $T_n = 5n^2 - 15n + 16$.",
        "question": "Is 216 a term in this sequence? Justify your answer with the necessary calculations.",
        "memo": "Set $T_n = 216$:\n$$5n^2 - 15n + 16 = 216$$\n$$5n^2 - 15n - 200 = 0$$\nDivide by 5:\n$$n^2 - 3n - 40 = 0$$\n$$(n - 8)(n + 5) = 0$$\n$$n = 8 \\quad \\text{or} \\quad n = -5$$\nSince $n$ must be a natural number ($n \\in \\mathbb{N}$), $n = 8$ and $n \\neq -5$.\nTherefore, yes, 216 is the $8^{\\text{th}}$ term of the sequence ($T_8 = 216$).\n\n* $\\checkmark$ equating to $216$\n* $\\checkmark$ standard form ($n^2 - 3n - 40 = 0$)\n* $\\checkmark n = 8$, therefore yes ($T_8 = 216$)",
        "final_answer": "Yes, T_8 = 216",
        "needs_review": False,
    },

    # ==========================================
    # QUESTION 4 (18 marks)
    # ==========================================
    {
        "question_ref": "4.1.1",
        "marks": 1,
        "topic": "Functions - Exponential Function Properties",
        "passage": "Given the function $p(x) = \\left(\\frac{1}{3}\\right)^x$.",
        "question": "Is $p$ an increasing or decreasing function?",
        "memo": "Decreasing (since the base $b = \\frac{1}{3}$ is between 0 and 1).\n\n* $\\checkmark$ decreasing",
        "final_answer": "decreasing",
        "needs_review": False,
    },
    {
        "question_ref": "4.1.2",
        "marks": 2,
        "topic": "Functions - Exponential Inverse Equation",
        "passage": "Given the function $p(x) = \\left(\\frac{1}{3}\\right)^x$.",
        "question": "Determine $p^{-1}$, the inverse of $p$, in the form $y = \\dots$",
        "memo": "$$y = \\left(\\frac{1}{3}\\right)^x$$\nSwap $x$ and $y$:\n$$x = \\left(\\frac{1}{3}\\right)^y$$\n$$\\therefore y = \\log_{\\frac{1}{3}} x$$\n\n**OR/OF**\n$$y = 3^{-x}$$\nSwap $x$ and $y$:\n$$x = 3^{-y}$$\n$$\\log_3 x = -y \\implies y = -\\log_3 x$$\n\n* $\\checkmark$ swap $x$ and $y$\n* $\\checkmark$ answer ($y = \\log_{\\frac{1}{3}} x$ or $y = -\\log_3 x$)",
        "final_answer": "y = log_{1/3} x",
        "needs_review": False,
    },
    {
        "question_ref": "4.1.3",
        "marks": 1,
        "topic": "Functions - Inverse Domain",
        "passage": "Given the function $p(x) = \\left(\\frac{1}{3}\\right)^x$.",
        "question": "Write down the domain of $p^{-1}$.",
        "memo": "$$x > 0 ; \\quad x \\in \\mathbb{R} \\quad \\text{or} \\quad (0 ; \\infty)$$\n\n* $\\checkmark$ answer",
        "final_answer": "x > 0",
        "needs_review": False,
    },
    {
        "question_ref": "4.1.4",
        "marks": 1,
        "topic": "Functions - Exponential Asymptote",
        "passage": "Given the function $p(x) = \\left(\\frac{1}{3}\\right)^x$.",
        "question": "Write down the equation of the asymptote of $p(x) - 5$.",
        "memo": "The horizontal asymptote of $p(x)$ is $y = 0$.\nTranslating down by 5 units:\n$$y = -5$$\n\n* $\\checkmark$ answer",
        "final_answer": "y = -5",
        "needs_review": False,
    },
    {
        "question_ref": "4.2.1",
        "marks": 2,
        "topic": "Functions - Hyperbola Asymptotes",
        "passage": "Given: $f(x) = \\frac{4}{x - 1} + 2$",
        "question": "Write down the equations of the asymptotes of $f$.",
        "memo": "$$x = 1$$\n$$y = 2$$\n\n* $\\checkmark x = 1$\n* $\\checkmark y = 2$",
        "final_answer": "x = 1 and y = 2",
        "needs_review": False,
    },
    {
        "question_ref": "4.2.2",
        "marks": 2,
        "topic": "Functions - Hyperbola x-Intercept",
        "passage": "Given: $f(x) = \\frac{4}{x - 1} + 2$",
        "question": "Calculate the $x$-intercept of $f$.",
        "memo": "Set $y = 0$:\n$$\\frac{4}{x - 1} + 2 = 0$$\n$$\\frac{4}{x - 1} = -2$$\n$$4 = -2(x - 1)$$\n$$4 = -2x + 2$$\n$$2x = -2$$\n$$x = -1$$\nIntercept coordinates: $(-1 ; 0)$\n\n* $\\checkmark$ let $y = 0$\n* $\\checkmark x = -1$",
        "final_answer": "x = -1",
        "needs_review": False,
    },
    {
        "question_ref": "4.2.3",
        "marks": 4,
        "topic": "Functions - Hyperbola Sketch",
        "passage": "Given: $f(x) = \\frac{4}{x - 1} + 2$",
        "question": "Sketch the graph of $f$, label all asymptotes and indicate the intercepts with the axes.",
        "memo": "[DIAGRAM: Sketch graph of hyperbola $f(x) = \\frac{4}{x - 1} + 2$.\n• Vertical asymptote: $x = 1$\n• Horizontal asymptote: $y = 2$\n• Intercepts with axes: $x$-intercept at $(-1 ; 0)$ and $y$-intercept at $(0 ; -2)$ (since $f(0) = \\frac{4}{0 - 1} + 2 = -2$).\n• Two hyperbolic branches: one branch in the upper-right region ($x > 1, y > 2$) and one branch in the lower-left region ($x < 1, y < 2$) passing through $(-1 ; 0)$ and $(0 ; -2)$.]\n\n* $\\checkmark$ asymptotes ($x = 1, y = 2$)\n* $\\checkmark x$-intercept ($(-1 ; 0)$)\n* $\\checkmark y$-intercept ($(0 ; -2)$)\n* $\\checkmark$ shape",
        "final_answer": "Hyperbola with asymptotes x = 1, y = 2, intercepts (-1; 0) and (0; -2)",
        "needs_review": False,
    },
    {
        "question_ref": "4.2.4",
        "marks": 2,
        "topic": "Functions - Hyperbola Inequality",
        "passage": "Given: $f(x) = \\frac{4}{x - 1} + 2$\n[DIAGRAM: Hyperbola $f(x) = \\frac{4}{x-1} + 2$ with asymptotes $x = 1, y = 2$, $x$-intercept $(-1 ; 0)$, and $y$-intercept $(0 ; -2)$.]",
        "question": "Use your graph to determine the values of $x$ for which $\\frac{4}{x - 1} \\geq -2$.",
        "memo": "$$\\frac{4}{x - 1} \\geq -2 \\iff \\frac{4}{x - 1} + 2 \\geq 0 \\iff f(x) \\geq 0$$\nFrom the graph, $f(x) \\geq 0$ where the graph lies on or above the $x$-axis:\n$$x \\leq -1 \\quad \\text{or} \\quad x > 1$$\n\n**OR/OF**\n$$x \\in (-\\infty ; -1] \\cup (1 ; \\infty)$$\n\n* $\\checkmark x \\leq -1$\n* $\\checkmark x > 1$",
        "final_answer": "x <= -1 or x > 1",
        "needs_review": False,
    },
    {
        "question_ref": "4.2.5",
        "marks": 3,
        "topic": "Functions - Hyperbola Axis of Symmetry",
        "passage": "Given: $f(x) = \\frac{4}{x - 1} + 2$",
        "question": "Determine the equation of the axis of symmetry of $f(x - 2)$, that has a negative gradient.",
        "memo": "The asymptotes of $f(x)$ intersect at $(1 ; 2)$.\nFor $f(x - 2)$, the hyperbola is translated 2 units to the right, so the asymptotes intersect at $(1 + 2 ; 2) = (3 ; 2)$.\nThe axis of symmetry with a negative gradient has slope $m = -1$:\n$$y - y_1 = m(x - x_1)$$\n$$y - 2 = -1(x - 3)$$\n$$y - 2 = -x + 3$$\n$$y = -x + 5$$\n\n**OR/OF**\nAxis of symmetry of $f(x)$ with negative gradient:\n$$y = -(x - 1) + 2 = -x + 1 + 2 = -x + 3$$\nReplacing $x$ by $x - 2$:\n$$y = -(x - 2) + 3 = -x + 2 + 3 = -x + 5$$\n\n**OR/OF**\n$$y = -(x - p) + q$$\n$$y = -((x - 2) - 1) + 2 = -(x - 3) + 2 = -x + 5$$\n\n* $\\checkmark$ intersection of asymptotes at $(3 ; 2)$\n* $\\checkmark$ substitution of $(3 ; 2)$ and $m = -1$\n* $\\checkmark y = -x + 5$",
        "final_answer": "y = -x + 5",
        "needs_review": False,
    },

    # ==========================================
    # QUESTION 5 (14 marks)
    # ==========================================
    {
        "question_ref": "5.1",
        "marks": 2,
        "topic": "Functions - Parabola Turning Point",
        "passage": "[DIAGRAM: Cartesian plane showing the parabola $f(x) = -(x + 3)^2 + 4$ and the straight line $g(x) = x + 5$. Parabola $f$ has a maximum turning point in the second quadrant above the x-axis, intersects the x-axis at two points and y-axis. Straight line $g$ has positive gradient 1 and y-intercept at $(0 ; 5)$. Line $g$ intersects parabola $f$ at point A on the negative x-axis and point B in the second quadrant. The origin is O.]",
        "question": "Write down the coordinates of the turning point of $f$.",
        "memo": "From $f(x) = -(x + 3)^2 + 4$, the turning point is:\n$$\\text{T.P. } (-3 ; 4)$$\n\n* $\\checkmark -3$\n* $\\checkmark 4$",
        "final_answer": "(-3; 4)",
        "needs_review": False,
    },
    {
        "question_ref": "5.2",
        "marks": 1,
        "topic": "Functions - Parabola Range",
        "passage": "[DIAGRAM: Cartesian plane showing the parabola $f(x) = -(x + 3)^2 + 4$ and the straight line $g(x) = x + 5$. Parabola $f$ has a maximum turning point at $(-3 ; 4)$, intersects the x-axis at two points and y-axis. Straight line $g$ has positive gradient 1 and y-intercept at $(0 ; 5)$. Line $g$ intersects parabola $f$ at point A on the negative x-axis and point B in the second quadrant. The origin is O.]",
        "question": "Write down the range of $f$.",
        "memo": "Since the parabola opens downward with maximum value $y = 4$:\n$$y \\leq 4 \\quad \\text{or} \\quad y \\in (-\\infty ; 4]$$\n\n* $\\checkmark$ answer",
        "final_answer": "y <= 4",
        "needs_review": False,
    },
    {
        "question_ref": "5.3",
        "marks": 4,
        "topic": "Functions - Intersection of Parabola and Line",
        "passage": "[DIAGRAM: Cartesian plane showing the parabola $f(x) = -(x + 3)^2 + 4$ and the straight line $g(x) = x + 5$. Parabola $f$ has a maximum turning point at $(-3 ; 4)$, intersects the x-axis at two points and y-axis. Straight line $g$ has positive gradient 1 and y-intercept at $(0 ; 5)$. Line $g$ intersects parabola $f$ at point A on the negative x-axis and point B in the second quadrant. The origin is O.]",
        "question": "Show that the $x$-coordinates of A and B are $-5$ and $-2$ respectively.",
        "memo": "Equate $f(x) = g(x)$:\n$$-(x + 3)^2 + 4 = x + 5$$\n$$-(x^2 + 6x + 9) + 4 = x + 5$$\n$$-x^2 - 6x - 9 + 4 = x + 5$$\n$$-x^2 - 6x - 5 = x + 5$$\n$$-x^2 - 7x - 10 = 0$$\n$$x^2 + 7x + 10 = 0$$\n$$(x + 5)(x + 2) = 0$$\n$$x = -5 \\quad \\text{or} \\quad x = -2$$\nTherefore, $x_A = -5$ and $x_B = -2$.\n\n* $\\checkmark$ equating $f(x) = g(x)$\n* $\\checkmark -x^2 - 6x - 9$\n* $\\checkmark$ standard form ($x^2 + 7x + 10 = 0$)\n* $\\checkmark$ factors",
        "final_answer": "x_A = -5, x_B = -2",
        "needs_review": False,
    },
    {
        "question_ref": "5.4",
        "marks": 2,
        "topic": "Functions - Roots of Shifted Equations / Nature of Roots",
        "passage": "[DIAGRAM: Cartesian plane showing the parabola $f(x) = -(x + 3)^2 + 4$ and the straight line $g(x) = x + 5$. Parabola $f$ has a maximum turning point at $(-3 ; 4)$, intersects the x-axis at two points and y-axis. Straight line $g$ has positive gradient 1 and y-intercept at $(0 ; 5)$. Line $g$ intersects parabola $f$ at point A $(-5 ; 0)$ and point B $(-2 ; 3)$. The origin is O.]",
        "question": "Hence, determine the values of $c$ for which the equation $-(x + c + 3)^2 + 4 = (x + c) + 5$ has ONE negative and ONE positive root.",
        "memo": "The equation is $f(x + c) = g(x + c)$.\nThe roots of $f(x) = g(x)$ are $x = -5$ and $x = -2$.\nReplacing $x$ by $x + c$ shifts the roots by $-c$ (or shifts the graphs $c$ units to the left / $-c$ to the right):\n$$x + c = -5 \\implies x = -5 - c$$\n$$x + c = -2 \\implies x = -2 - c$$\nFor the roots to have opposite signs (ONE negative and ONE positive root), $0$ must lie strictly between the two roots:\n$$-5 - c < 0 < -2 - c$$\n$$-5 - c < 0 \\implies c > -5$$\n$$-2 - c > 0 \\implies c < -2$$\n$$\\therefore -5 < c < -2$$\n(The graph must shift more than 2 and less than 5 units to the right).\n\n* $\\checkmark\\checkmark -5 < c < -2$",
        "final_answer": "-5 < c < -2",
        "needs_review": False,
    },
    {
        "question_ref": "5.5",
        "marks": 5,
        "topic": "Functions - Vertical Distance and Tangent Line",
        "passage": "[DIAGRAM: Cartesian plane showing the parabola $f(x) = -(x + 3)^2 + 4$ and the straight line $g(x) = x + 5$. Parabola $f$ has a maximum turning point at $(-3 ; 4)$, intersects the x-axis at two points and y-axis. Straight line $g$ has positive gradient 1 and y-intercept at $(0 ; 5)$. Line $g$ intersects parabola $f$ at point A $(-5 ; 0)$ and point B $(-2 ; 3)$. The origin is O.]",
        "question": "The maximum distance between $f$ and $g$ in the interval $x_A < x < x_B$ is $k$.\nIf $h(x) = g(x) + k$, determine the equation of $h$ in the form $h(x) = \\dots$",
        "memo": "The vertical distance $D(x)$ between $f(x)$ and $g(x)$ in the interval $-5 < x < -2$ is:\n$$D(x) = f(x) - g(x) = -(x + 3)^2 + 4 - (x + 5)$$\n$$D(x) = -x^2 - 6x - 9 + 4 - x - 5 = -x^2 - 7x - 10$$\n\nFor maximum distance:\n$$D'(x) = -2x - 7 = 0 \\implies x = -\\frac{7}{2} = -3{,}5$$\n\n**OR/OF**\n$$x = -\\frac{b}{2a} = -\\frac{-7}{2(-1)} = -\\frac{7}{2}$$\n\nSubstitute $x = -\\frac{7}{2}$ into $D(x)$:\n$$k = D\\left(-\\frac{7}{2}\\right) = -\\left(-\\frac{7}{2}\\right)^2 - 7\\left(-\\frac{7}{2}\\right) - 10$$\n$$k = -\\frac{49}{4} + \\frac{49}{2} - 10 = \\frac{49}{4} - 10 = \\frac{9}{4} = 2{,}25$$\n\nNow find $h(x) = g(x) + k$:\n$$h(x) = (x + 5) + 2{,}25$$\n$$h(x) = x + 7{,}25 \\quad \\left(\\text{or } h(x) = x + \\frac{29}{4}\\right)$$\n\n* $\\checkmark D(x) = -x^2 - 7x - 10$\n* $\\checkmark -2x - 7 = 0$\n* $\\checkmark x = -\\frac{7}{2}$\n* $\\checkmark k = 2{,}25$\n* $\\checkmark h(x) = x + 7{,}25$",
        "final_answer": "h(x) = x + 7.25",
        "needs_review": False,
    },

    # ==========================================
    # QUESTION 6 (13 marks)
    # ==========================================
    {
        "question_ref": "6.1.1",
        "marks": 2,
        "topic": "Financial Mathematics - Inflation / Compound Growth",
        "passage": "A company bought a photocopier for R150 000 on 1 July 2022. They will use the old photocopier as a trade-in when they replace it with a similar new photocopier in 5 years' time on 30 June 2027.",
        "question": "The average rate of inflation over the next 5 years will be 6,5% p.a. Determine the price of a similar new photocopier in 5 years' time.",
        "memo": "$$A = P(1 + i)^n$$\n$$A = 150\\,000(1 + 0{,}065)^5$$\n$$A = 150\\,000(1{,}065)^5$$\n$$A = \\text{R}205\\,513{,}03 \\approx \\text{R}205\\,513$$\n\n* $\\checkmark$ substitution into the correct formula\n* $\\checkmark$ answer (R205 513 or R205 513,03)",
        "final_answer": "R205 513",
        "needs_review": False,
    },
    {
        "question_ref": "6.1.2",
        "marks": 2,
        "topic": "Financial Mathematics - Straight-Line Depreciation / Trade-In",
        "passage": "A company bought a photocopier for R150 000 on 1 July 2022. They will use the old photocopier as a trade-in when they replace it with a similar new photocopier in 5 years' time on 30 June 2027.",
        "question": "Calculate the trade-in value of the old photocopier after 5 years, if it depreciates at a rate of 9% p.a. on a straight-line method.",
        "memo": "$$A = P(1 - in)$$\n$$A = 150\\,000(1 - 0{,}09 \\times 5)$$\n$$A = 150\\,000(1 - 0{,}45)$$\n$$A = 150\\,000(0{,}55)$$\n$$A = \\text{R}82\\,500$$\n\n* $\\checkmark$ substitution into the correct formula\n* $\\checkmark$ answer (R82 500)",
        "final_answer": "R82 500",
        "needs_review": False,
    },
    {
        "question_ref": "6.1.3",
        "marks": 4,
        "topic": "Financial Mathematics - Sinking Fund / Future Value Annuity",
        "passage": "A company bought a photocopier for R150 000 on 1 July 2022. They will use the old photocopier as a trade-in when they replace it with a similar new photocopier in 5 years' time on 30 June 2027.",
        "question": "The company set up a sinking fund to cover the replacement cost of the new photocopier. The fund earns interest at the rate of 7,85% p.a., compounded monthly. The company made its first monthly deposit on 31 July 2022 and will continue to do so until 31 May 2027, one month prior to the new photocopier being bought. How much should be deposited at the end of each month so that the company will be able to buy the new photocopier?",
        "memo": "Cost of new photocopier in 5 years = R205 513\nTrade-in value of old photocopier = R82 500\nSinking fund required amount $F$:\n$$F = 205\\,513 - 82\\,500 = \\text{R}123\\,013$$\n\nInterest rate: $i = \\frac{0{,}0785}{12}$\nNumber of monthly deposits: from 31 July 2022 to 31 May 2027 is 59 months, so $n = 59$.\nSince the last deposit is made on 31 May 2027 (1 month prior to purchase on 30 June 2027), the accumulated fund grows with interest for 1 additional month:\n$$F = \\frac{x\\left[\\left(1 + \\frac{0{,}0785}{12}\\right)^{59} - 1\\right]}{\\frac{0{,}0785}{12}} \\times \\left(1 + \\frac{0{,}0785}{12}\\right)$$\n$$123\\,013 = x \\cdot \\frac{\\left[\\left(1 + \\frac{0{,}0785}{12}\\right)^{59} - 1\\right]}{\\frac{0{,}0785}{12}} \\cdot \\left(1 + \\frac{0{,}0785}{12}\\right)$$\n$$x = \\frac{123\\,013 \\times \\frac{0{,}0785}{12}}{\\left[\\left(1 + \\frac{0{,}0785}{12}\\right)^{59} - 1\\right]\\left(1 + \\frac{0{,}0785}{12}\\right)}$$\n$$x \\approx \\text{R}1\\,704{,}01$$\n\n* $\\checkmark F = \\text{R}123\\,013$\n* $\\checkmark i = \\frac{0{,}0785}{12}$\n* $\\checkmark n = 59$ and factor $\\left(1 + \\frac{0{,}0785}{12}\\right)$\n* $\\checkmark$ answer ($x = \\text{R}1\\,704{,}01$)",
        "final_answer": "R1 704.01",
        "needs_review": False,
    },
    {
        "question_ref": "6.2",
        "marks": 5,
        "topic": "Financial Mathematics - Present Value Annuity / Loan Period",
        "passage": "",
        "question": "Today, Andrew borrowed R200 000 from a bank. The bank charges interest at 5,25% p.a., compounded quarterly. Andrew will make repayments of R6 000 at the end of every 3 months. His first repayment will be made in 3 months from now. How long, in years, will it take Andrew to settle the loan?",
        "memo": "$$P = \\frac{x[1 - (1 + i)^{-n}]}{i}$$\n$$P = 200\\,000, \\quad x = 6\\,000, \\quad i = \\frac{0{,}0525}{4} = 0{,}013125$$\n$$200\\,000 = \\frac{6\\,000\\left[1 - \\left(1 + \\frac{0{,}0525}{4}\\right)^{-n}\\right]}{\\frac{0{,}0525}{4}}$$\n$$200\\,000 \\times \\frac{0{,}0525}{4} = 6\\,000\\left[1 - (1{,}013125)^{-n}\\right]$$\n$$2\\,625 = 6\\,000\\left[1 - (1{,}013125)^{-n}\\right]$$\n$$\\frac{2\\,625}{6\\,000} = 1 - (1{,}013125)^{-n}$$\n$$\\frac{7}{16} = 1 - (1{,}013125)^{-n}$$\n$$(1{,}013125)^{-n} = 1 - \\frac{7}{16} = \\frac{9}{16}$$\n$$-n \\log(1{,}013125) = \\log\\left(\\frac{9}{16}\\right)$$\n$$-n = \\frac{\\log\\left(\\frac{9}{16}\\right)}{\\log(1{,}013125)} \\approx -44{,}1243$$\n$$n \\approx 44{,}1243 \\text{ quarters}$$\n\nConvert quarters into years:\n$$\\text{Years} = \\frac{n}{4} = \\frac{44{,}1243}{4} \\approx 11{,}03 \\text{ years}$$\n\n* $\\checkmark$ substitution into correct formula\n* $\\checkmark$ simplification ($(1{,}013125)^{-n} = \\frac{9}{16}$)\n* $\\checkmark$ use of logs\n* $\\checkmark -n = -44{,}1243\\dots$ (or $-4t = -44{,}1243\\dots$)\n* $\\checkmark$ answer ($11{,}03$ years)",
        "final_answer": "11.03 years",
        "needs_review": False,
    },

    # ==========================================
    # QUESTION 7 (13 marks)
    # ==========================================
    {
        "question_ref": "7.1",
        "marks": 5,
        "topic": "Calculus - Derivative from First Principles",
        "passage": "",
        "question": "Determine $f'(x)$ from first principles if $f(x) = -2x^2 - 1$.",
        "memo": "$$f(x) = -2x^2 - 1$$\n$$f'(x) = \\lim_{h \\to 0} \\frac{f(x + h) - f(x)}{h}$$\n$$f'(x) = \\lim_{h \\to 0} \\frac{-2(x + h)^2 - 1 - (-2x^2 - 1)}{h}$$\n$$f'(x) = \\lim_{h \\to 0} \\frac{-2(x^2 + 2xh + h^2) - 1 + 2x^2 + 1}{h}$$\n$$f'(x) = \\lim_{h \\to 0} \\frac{-2x^2 - 4xh - 2h^2 - 1 + 2x^2 + 1}{h}$$\n$$f'(x) = \\lim_{h \\to 0} \\frac{-4xh - 2h^2}{h}$$\n$$f'(x) = \\lim_{h \\to 0} \\frac{h(-4x - 2h)}{h}$$\n$$f'(x) = \\lim_{h \\to 0} (-4x - 2h)$$\n$$f'(x) = -4x$$\n\n**OR/OF**\n$$f(x + h) = -2(x + h)^2 - 1 = -2x^2 - 4xh - 2h^2 - 1$$\n$$f(x + h) - f(x) = -2x^2 - 4xh - 2h^2 - 1 - (-2x^2 - 1) = -4xh - 2h^2$$\n$$f'(x) = \\lim_{h \\to 0} \\frac{f(x + h) - f(x)}{h} = \\lim_{h \\to 0} \\frac{-4xh - 2h^2}{h} = \\lim_{h \\to 0} \\frac{h(-4x - 2h)}{h} = -4x$$\n\n* $\\checkmark$ substitution into the correct formula\n* $\\checkmark -2x^2 - 4xh - 2h^2 - 1$\n* $\\checkmark -4xh - 2h^2$\n* $\\checkmark$ common factor $h$\n* $\\checkmark$ answer ($-4x$)",
        "final_answer": "f'(x) = -4x",
        "needs_review": False,
    },
    {
        "question_ref": "7.2.1",
        "marks": 2,
        "topic": "Calculus - Rules of Differentiation (Polynomial)",
        "passage": "",
        "question": "Determine $f'(x)$, if it is given that $f(x) = -2x^3 + 3x^2$.",
        "memo": "$$f(x) = -2x^3 + 3x^2$$\n$$f'(x) = -2(3x^2) + 3(2x)$$\n$$f'(x) = -6x^2 + 6x$$\n\n* $\\checkmark -6x^2$\n* $\\checkmark +6x$",
        "final_answer": "f'(x) = -6x^2 + 6x",
        "needs_review": False,
    },
    {
        "question_ref": "7.2.2",
        "marks": 4,
        "topic": "Calculus - Rules of Differentiation (Fractional and Surd Powers)",
        "passage": "",
        "question": "Determine $\\frac{dy}{dx}$ if $y = 2x + \\frac{1}{\\sqrt{4x}}$.",
        "memo": "Rewrite in exponential form:\n$$y = 2x + \\frac{1}{\\sqrt{4}\\sqrt{x}} = 2x + \\frac{1}{2x^{\\frac{1}{2}}} = 2x + \\frac{1}{2}x^{-\\frac{1}{2}}$$\nNow differentiate with respect to $x$:\n$$\\frac{dy}{dx} = 2 + \\frac{1}{2}\\left(-\\frac{1}{2}\\right)x^{-\\frac{1}{2} - 1}$$\n$$\\frac{dy}{dx} = 2 - \\frac{1}{4}x^{-\\frac{3}{2}} = 2 - \\frac{1}{4\\sqrt{x^3}}$$\n\n* $\\checkmark \\frac{1}{2}$\n* $\\checkmark x^{-\\frac{1}{2}}$\n* $\\checkmark 2$\n* $\\checkmark -\\frac{1}{4}x^{-\\frac{3}{2}}$",
        "final_answer": "dy/dx = 2 - 1/4 x^(-3/2)",
        "needs_review": False,
    },
    {
        "question_ref": "7.3",
        "marks": 2,
        "topic": "Calculus - Concavity and Second Derivative",
        "passage": "",
        "question": "The graph $y = f'(x)$ has a minimum turning point at $(1 ; -3)$.\nDetermine the values of $x$ for which $f$ is concave down.",
        "memo": "A function $f$ is concave down where its second derivative is negative: $f''(x) < 0$.\nSince $f''(x) = \\frac{d}{dx}[f'(x)]$ is the gradient of $f'(x)$, $f'(x)$ is decreasing when $f''(x) < 0$.\nThe graph $y = f'(x)$ has a minimum turning point at $(1 ; -3)$, so $f'(x)$ is decreasing to the left of $x = 1$.\nTherefore, $f''(x) < 0$ and $f$ is concave down for:\n$$x < 1$$\n\n* $\\checkmark\\checkmark x < 1$",
        "final_answer": "x < 1",
        "needs_review": False,
    },

    # ==========================================
    # QUESTION 8 (16 marks)
    # ==========================================
    {
        "question_ref": "8.1",
        "marks": 1,
        "topic": "Calculus - Cubic Function y-Intercept",
        "passage": "Given: $f(x) = x^3 + 4x^2 - 7x - 10$",
        "question": "Write down the $y$-intercept of $f$.",
        "memo": "At $x = 0$:\n$$f(0) = (0)^3 + 4(0)^2 - 7(0) - 10 = -10$$\n$$y = -10 \\quad \\text{or} \\quad (0 ; -10)$$\n\n* $\\checkmark$ answer ($y = -10$)",
        "final_answer": "y = -10",
        "needs_review": False,
    },
    {
        "question_ref": "8.2",
        "marks": 2,
        "topic": "Calculus - Factor Theorem / Roots of Cubic",
        "passage": "Given: $f(x) = x^3 + 4x^2 - 7x - 10$",
        "question": "Show that 2 is a root of the equation $f(x) = 0$.",
        "memo": "$$f(x) = x^3 + 4x^2 - 7x - 10$$\n$$f(2) = (2)^3 + 4(2)^2 - 7(2) - 10$$\n$$f(2) = 8 + 4(4) - 14 - 10$$\n$$f(2) = 8 + 16 - 14 - 10 = 0$$\nSince $f(2) = 0$, by the Factor Theorem $(x - 2)$ is a factor and 2 is a root of $f(x) = 0$.\n\n* $\\checkmark$ substitution of $x = 2$\n* $\\checkmark f(2) = 0$",
        "final_answer": "f(2) = 0, so 2 is a root",
        "needs_review": False,
    },
    {
        "question_ref": "8.3",
        "marks": 3,
        "topic": "Calculus - Factorisation of Cubic Polynomial",
        "passage": "Given: $f(x) = x^3 + 4x^2 - 7x - 10$",
        "question": "Hence, factorise $f(x)$ completely.",
        "memo": "Since 2 is a root, $(x - 2)$ is a factor of $f(x)$:\n$$f(x) = (x - 2)(x^2 + 6x + 5)$$\nFactorising the quadratic factor:\n$$f(x) = (x - 2)(x + 5)(x + 1)$$\n\n* $\\checkmark (x - 2)$\n* $\\checkmark (x + 5)$\n* $\\checkmark (x + 1)$",
        "final_answer": "(x - 2)(x + 5)(x + 1)",
        "needs_review": False,
    },
    {
        "question_ref": "8.4",
        "marks": 3,
        "topic": "Calculus - Cubic Function Sketch",
        "passage": "Given: $f(x) = x^3 + 4x^2 - 7x - 10$",
        "question": "If it is further given that the coordinates of the turning points are approximately at $(0{,}7 ; -12{,}6)$ and $(-3{,}4 ; 20{,}8)$, draw a sketch graph of $f$ and label all intercepts and turning points.",
        "memo": "[DIAGRAM: Sketch graph of cubic function $f(x) = x^3 + 4x^2 - 7x - 10$.\n• $x$-intercepts: $(-5 ; 0)$, $(-1 ; 0)$, and $(2 ; 0)$\n• $y$-intercept: $(0 ; -10)$\n• Local maximum turning point: $(-3{,}4 ; 20{,}8)$ in the second quadrant\n• Local minimum turning point: $(0{,}7 ; -12{,}6)$ in the fourth quadrant\n• Curve starts in quadrant 3 (bottom-left), passes through $(-5 ; 0)$, reaches local maximum at $(-3{,}4 ; 20{,}8)$, turns downwards passing through $(-1 ; 0)$ and $(0 ; -10)$, reaches local minimum at $(0{,}7 ; -12{,}6)$, turns upwards passing through $(2 ; 0)$ into quadrant 1 (top-right).]\n\n* $\\checkmark x$-intercepts ($(-5 ; 0), (-1 ; 0), (2 ; 0)$)\n* $\\checkmark y$-intercept ($(0 ; -10)$)\n* $\\checkmark$ sketch with turning points in 2nd and 4th quadrants",
        "final_answer": "Cubic graph with x-intercepts (-5; 0), (-1; 0), (2; 0), y-intercept (0; -10), turning points (-3.4; 20.8) and (0.7; -12.6)",
        "needs_review": False,
    },
    {
        "question_ref": "8.5.1",
        "marks": 2,
        "topic": "Calculus - Decreasing Interval",
        "passage": "Given: $f(x) = x^3 + 4x^2 - 7x - 10$\n[DIAGRAM: Cubic curve with turning points at $(-3{,}4 ; 20{,}8)$ (local maximum) and $(0{,}7 ; -12{,}6)$ (local minimum).]",
        "question": "Use your graph to determine the values of $x$ for which:\n$$f'(x) < 0$$",
        "memo": "$f'(x) < 0$ where the curve is strictly decreasing, which is between the local maximum turning point and the local minimum turning point:\n$$-3{,}4 < x < 0{,}7 \\quad \\text{or} \\quad x \\in (-3{,}4 ; 0{,}7)$$\n\n* $\\checkmark\\checkmark -3{,}4 < x < 0{,}7$",
        "final_answer": "-3.4 < x < 0.7",
        "needs_review": False,
    },
    {
        "question_ref": "8.5.2",
        "marks": 2,
        "topic": "Calculus - Minimum Gradient / Point of Inflection",
        "passage": "Given: $f(x) = x^3 + 4x^2 - 7x - 10$\n[DIAGRAM: Cubic curve with turning points at $(-3{,}4 ; 20{,}8)$ and $(0{,}7 ; -12{,}6)$.]",
        "question": "Use your graph to determine the values of $x$ for which:\nThe gradient of a tangent to $f$ will be a minimum",
        "memo": "The gradient of the tangent is given by $f'(x) = 3x^2 + 8x - 7$.\nSince $f'(x)$ is a parabola opening upwards, its minimum occurs at the vertex / point of inflection where $f''(x) = 0$:\n$$f''(x) = 6x + 8 = 0$$\n$$x = -\\frac{8}{6} = -\\frac{4}{3} \\approx -1{,}33$$\n\n**OR/OF**\nUsing the midpoint of the $x$-coordinates of the turning points:\n$$x = \\frac{-3{,}4 + 0{,}7}{2} = \\frac{-2{,}7}{2} = -1{,}35$$\n\n* $\\checkmark f''(x) = 6x + 8 = 0$\n* $\\checkmark$ answer ($x = -\\frac{4}{3} \\approx -1{,}33$ or $-1{,}35$)",
        "final_answer": "x = -4/3",
        "needs_review": False,
    },
    {
        "question_ref": "8.5.3",
        "marks": 3,
        "topic": "Calculus - Product of First and Second Derivatives",
        "passage": "Given: $f(x) = x^3 + 4x^2 - 7x - 10$\n[DIAGRAM: Cubic curve with turning points at $(-3{,}4 ; 20{,}8)$ and $(0{,}7 ; -12{,}6)$, and point of inflection at $x = -1{,}33$.]",
        "question": "Use your graph to determine the values of $x$ for which:\n$$f'(x) \\cdot f''(x) \\leq 0$$",
        "memo": "The product $f'(x) \\cdot f''(x) \\leq 0$ means that $f'(x)$ and $f''(x)$ have opposite signs (or at least one is zero).\n\nKey critical values:\n• Turning points of $f$: $x = -3{,}4$ and $x = 0{,}7$ (where $f'(x) = 0$)\n• Point of inflection of $f$: $x = -1{,}33$ (where $f''(x) = 0$)\n\nInterval analysis:\n1. $x \\leq -3{,}4$:\n   $f'(x) \\geq 0$ and $f''(x) \\leq 0 \\implies f'(x) \\cdot f''(x) \\leq 0$ (satisfied)\n2. $-3{,}4 < x < -1{,}33$:\n   $f'(x) < 0$ and $f''(x) < 0 \\implies f'(x) \\cdot f''(x) > 0$\n3. $-1{,}33 \\leq x \\leq 0{,}7$:\n   $f'(x) \\leq 0$ and $f''(x) \\geq 0 \\implies f'(x) \\cdot f''(x) \\leq 0$ (satisfied)\n4. $x > 0{,}7$:\n   $f'(x) > 0$ and $f''(x) > 0 \\implies f'(x) \\cdot f''(x) > 0$\n\nTherefore:\n$$x \\leq -3{,}4 \\quad \\text{or} \\quad -1{,}33 \\leq x \\leq 0{,}7$$\n\n**OR/OF**\n$$x \\in (-\\infty ; -3{,}4] \\cup [-1{,}33 ; 0{,}7]$$\n(or using $-1{,}35$: $x \\leq -3{,}4$ or $-1{,}35 \\leq x \\leq 0{,}7$)\n\n* $\\checkmark x \\leq -3{,}4$\n* $\\checkmark\\checkmark -1{,}33 \\leq x \\leq 0{,}7$",
        "final_answer": "x <= -3.4 or -1.33 <= x <= 0.7",
        "needs_review": False,
    },

    # ==========================================
    # QUESTION 9 (9 marks)
    # ==========================================
    {
        "question_ref": "9.1",
        "marks": 2,
        "topic": "Calculus - Optimization Geometric Modeling",
        "passage": "A wire, 12 metres long, is cut into two pieces. One part is bent to form an equilateral triangle and the other a square. A side of the triangle has a length of $2x$ metres.",
        "question": "Write down the length of a side of the square in terms of $x$.",
        "memo": "Perimeter of the equilateral triangle $= 3 \\times 2x = 6x$\nRemaining wire for the square $= 12 - 6x$\nSince the square has 4 equal sides:\n$$\\text{Side length of square} = \\frac{12 - 6x}{4} = \\frac{6 - 3x}{2} = 3 - \\frac{3}{2}x$$\n\n* $\\checkmark 12 - 6x$\n* $\\checkmark$ answer ($\\frac{6 - 3x}{2}$ or $3 - \\frac{3}{2}x$)",
        "final_answer": "s = (6 - 3x)/2",
        "needs_review": False,
    },
    {
        "question_ref": "9.2",
        "marks": 7,
        "topic": "Calculus - Optimization Maximum Volume",
        "passage": "A wire, 12 metres long, is cut into two pieces. One part is bent to form an equilateral triangle with side $2x$ metres, and the other a square with side $\\left(3 - \\frac{3}{2}x\\right)$ metres.",
        "question": "If this square is now used as the base of a rectangular prism with a height of $4x$ metres, determine the maximum volume of the rectangular prism.",
        "memo": "Base of the rectangular prism is a square with side $s = \\frac{6 - 3x}{2} = 3 - \\frac{3}{2}x$.\nHeight of the prism is $h = 4x$.\nVolume of the rectangular prism $V(x)$:\n$$V(x) = s^2 \\times h = \\left(\\frac{6 - 3x}{2}\\right)^2 (4x)$$\n$$V(x) = \\left(\\frac{36 - 36x + 9x^2}{4}\\right)(4x)$$\n$$V(x) = (36 - 36x + 9x^2)x = 36x - 36x^2 + 9x^3$$\n$$V(x) = 9x^3 - 36x^2 + 36x$$\n\nFor maximum volume, $V'(x) = 0$:\n$$V'(x) = 27x^2 - 72x + 36 = 0$$\nDivide by 9:\n$$3x^2 - 8x + 4 = 0$$\n$$(3x - 2)(x - 2) = 0$$\n$$x = \\frac{2}{3} \\quad \\text{or} \\quad x = 2$$\n\nIf $x = 2$, the side length of the square is $3 - \\frac{3}{2}(2) = 0$, which is impossible for a prism.\nTherefore, $x = \\frac{2}{3}$.\n\nCalculate the maximum volume:\n$$V\\left(\\frac{2}{3}\\right) = 36\\left(\\frac{2}{3}\\right) - 36\\left(\\frac{2}{3}\\right)^2 + 9\\left(\\frac{2}{3}\\right)^3$$\n$$V\\left(\\frac{2}{3}\\right) = 24 - 36\\left(\\frac{4}{9}\\right) + 9\\left(\\frac{8}{27}\\right)$$\n$$V\\left(\\frac{2}{3}\\right) = 24 - 16 + \\frac{8}{3} = 8 + \\frac{8}{3} = \\frac{32}{3} = 10{,}67 \\text{ m}^3$$\n\n* $\\checkmark V = \\left(\\frac{6 - 3x}{2}\\right)^2(4x)$\n* $\\checkmark \\frac{36 - 36x + 9x^2}{4}$\n* $\\checkmark 36x - 36x^2 + 9x^3$\n* $\\checkmark V'(x) = 27x^2 - 72x + 36$\n* $\\checkmark V'(x) = 0$\n* $\\checkmark x = \\frac{2}{3}$\n* $\\checkmark$ maximum volume $= \\frac{32}{3} \\text{ m}^3 \\approx 10{,}67 \\text{ m}^3$",
        "final_answer": "32/3 m^3",
        "needs_review": False,
    },

    # ==========================================
    # QUESTION 10 (17 marks)
    # ==========================================
    {
        "question_ref": "10.1.1",
        "marks": 3,
        "topic": "Probability - Tree Diagram",
        "passage": "A group of people participated in a trial to test a new headache pill.\n• 50% of the participants received the headache pill.\n• 50% of the participants received a sugar pill.\n• $\\frac{2}{5}$ of the group receiving the headache pill were not cured.\n• $\\frac{3}{10}$ of the group receiving the sugar pill were cured.",
        "question": "Represent the given information on a tree diagram. Indicate on your diagram the probability associated with each branch as well as the outcomes.",
        "memo": "[TREE DIAGRAM:\nEvent A (Pill Type):\n  ├── Headache Pill (H): P(H) = 1/2 (or 50% / 0.5)\n  │     ├── Cured (C): P(C|H) = 3/5  --> Outcome: HC\n  │     └── Not Cured (NC): P(NC|H) = 2/5  --> Outcome: HN\n  │\n  └── Sugar Pill (S): P(S) = 1/2 (or 50% / 0.5)\n        ├── Cured (C): P(C|S) = 3/10  --> Outcome: SC\n        └── Not Cured (NC): P(NC|S) = 7/10  --> Outcome: SN]\n\n* $\\checkmark$ Event A probabilities ($P(H) = \\frac{1}{2}, P(S) = \\frac{1}{2}$)\n* $\\checkmark$ Event B Medication branch: $P(C) = \\frac{3}{5}, P(NC) = \\frac{2}{5}$\n* $\\checkmark$ Event B Sugar pill branch: $P(C) = \\frac{3}{10}, P(NC) = \\frac{7}{10}$",
        "final_answer": "Tree diagram with branches P(H)=1/2, P(S)=1/2, P(C|H)=3/5, P(NC|H)=2/5, P(C|S)=3/10, P(NC|S)=7/10",
        "needs_review": False,
    },
    {
        "question_ref": "10.1.2",
        "marks": 2,
        "topic": "Probability - Total Probability from Tree Diagram",
        "passage": "A group of people participated in a trial to test a new headache pill.\n• 50% of the participants received the headache pill.\n• 50% of the participants received a sugar pill.\n• $\\frac{2}{5}$ of the group receiving the headache pill were not cured.\n• $\\frac{3}{10}$ of the group receiving the sugar pill were cured.\n[TREE DIAGRAM: P(H) = 1/2, P(S) = 1/2; P(C|H) = 3/5, P(NC|H) = 2/5; P(C|S) = 3/10, P(NC|S) = 7/10]",
        "question": "Determine the probability that a person chosen at random from the group will NOT be cured.",
        "memo": "$$P(\\text{Not Cured}) = P(H) \\times P(NC|H) + P(S) \\times P(NC|S)$$\n$$P(\\text{Not Cured}) = \\left(\\frac{1}{2}\\right)\\left(\\frac{2}{5}\\right) + \\left(\\frac{1}{2}\\right)\\left(\\frac{7}{10}\\right)$$\n$$P(\\text{Not Cured}) = \\frac{2}{10} + \\frac{7}{20} = \\frac{4}{20} + \\frac{7}{20} = \\frac{11}{20} = 0{,}55$$\n\n* $\\checkmark$ substitution\n* $\\checkmark$ answer ($\\frac{11}{20}$ or $0{,}55$)",
        "final_answer": "11/20",
        "needs_review": False,
    },
    {
        "question_ref": "10.2.1",
        "marks": 2,
        "topic": "Probability - Mutually Exclusive Events",
        "passage": "Three events, A, B and C, are considered:\n$$P(A) = \\frac{2}{5}, \\quad P(B) = \\frac{1}{4} \\quad \\text{and} \\quad P(A \\text{ or } B) = \\frac{13}{20}.$$",
        "question": "Are events A and B mutually exclusive? Support your answer with the necessary calculations.",
        "memo": "$$P(A \\text{ or } B) = P(A) + P(B) - P(A \\text{ and } B)$$\n$$P(A \\text{ and } B) = P(A) + P(B) - P(A \\text{ or } B)$$\n$$P(A \\text{ and } B) = \\frac{2}{5} + \\frac{1}{4} - \\frac{13}{20} = \\frac{8}{20} + \\frac{5}{20} - \\frac{13}{20} = \\frac{13}{20} - \\frac{13}{20} = 0$$\nSince $P(A \\text{ and } B) = 0$, events A and B are mutually exclusive.\n\n**OR/OF**\n$$P(A) + P(B) = \\frac{2}{5} + \\frac{1}{4} = \\frac{8 + 5}{20} = \\frac{13}{20}$$\nSince $P(A \\text{ or } B) = P(A) + P(B)$, $P(A \\text{ and } B) = 0$.\nTherefore, events A and B are mutually exclusive.\n\n* $\\checkmark$ substitution\n* $\\checkmark$ answer ($P(A \\text{ and } B) = 0$, yes mutually exclusive)",
        "final_answer": "Yes, mutually exclusive since P(A and B) = 0",
        "needs_review": False,
    },
    {
        "question_ref": "10.2.2",
        "marks": 3,
        "topic": "Probability - Venn Diagram / Three Events",
        "passage": "Three events, A, B and C, are considered:\n$$P(A) = \\frac{2}{5}, \\quad P(B) = \\frac{1}{4} \\quad \\text{and} \\quad P(A \\text{ or } B) = \\frac{13}{20}.$$\nIt is further given that:\n$$P(A \\text{ or } C) = \\frac{7}{10}, \\quad P(A \\text{ and } C) = \\frac{2}{5} \\quad \\text{and} \\quad 2P(B \\text{ and } C) = P(A \\text{ and } C).$$",
        "question": "Determine $P(\\text{only } C)$.",
        "memo": "From $2P(B \\text{ and } C) = P(A \\text{ and } C) = \\frac{2}{5}$:\n$$P(B \\text{ and } C) = \\frac{1}{2} \\times \\frac{2}{5} = \\frac{1}{5}$$\n\nAlso, $P(A \\text{ or } C) = P(A) + P(C) - P(A \\text{ and } C)$:\n$$\\frac{7}{10} = \\frac{2}{5} + P(C) - \\frac{2}{5} \\implies P(C) = \\frac{7}{10}$$\n\nSince $A$ and $B$ are mutually exclusive ($A \\cap B = \\emptyset$), there is no triple intersection ($A \\cap B \\cap C = \\emptyset$).\nThus:\n$$P(\\text{only } C) = P(C) - P(A \\text{ and } C) - P(B \\text{ and } C)$$\n$$P(\\text{only } C) = \\frac{7}{10} - \\frac{2}{5} - \\frac{1}{5} = \\frac{7}{10} - \\frac{4}{10} - \\frac{2}{10} = \\frac{1}{10} = 0{,}1$$\n\n* $\\checkmark P(B \\text{ and } C) = \\frac{1}{5}$\n* $\\checkmark \\frac{7}{10} - \\frac{2}{5} - \\frac{1}{5}$\n* $\\checkmark$ answer ($\\frac{1}{10}$ or $0{,}1$)",
        "final_answer": "1/10",
        "needs_review": False,
    },
    {
        "question_ref": "10.2.3",
        "marks": 2,
        "topic": "Probability - Complementary Probability (None of Three Events)",
        "passage": "Three events, A, B and C, are considered:\n$$P(A) = \\frac{2}{5}, \\quad P(B) = \\frac{1}{4}, \\quad P(A \\text{ or } B) = \\frac{13}{20},$$\n$$P(A \\text{ or } C) = \\frac{7}{10}, \\quad P(A \\text{ and } C) = \\frac{2}{5}, \\quad 2P(B \\text{ and } C) = P(A \\text{ and } C).$$\n[DIAGRAM: Venn Diagram for three events A, B, C with disjoint A and B:\n• Region A (which is entirely inside C): P(A and C) = 2/5 = 8/20, P(only A) = 0\n• Region B: P(B and C) = 1/5 = 4/20, P(only B) = 1/4 - 1/5 = 1/20\n• Region C: P(only C) = 1/10 = 2/20\n• Total P(A or B or C) = 8/20 + 4/20 + 1/20 + 2/20 = 15/20 = 3/4 = 0.75]",
        "question": "Determine the probability that events A, B or C do NOT take place.",
        "memo": "$$P(\\text{no event}) = 1 - P(A \\text{ or } B \\text{ or } C)$$\nFrom the Venn diagram components:\n$$P(A \\text{ or } B \\text{ or } C) = P(A \\cap C) + P(\\text{only } C) + P(B \\cap C) + P(\\text{only } B)$$\n$$P(A \\text{ or } B \\text{ or } C) = \\frac{2}{5} + \\frac{1}{10} + \\frac{1}{5} + \\left(\\frac{1}{4} - \\frac{1}{5}\\right) = \\frac{7}{10} + \\frac{1}{20} = \\frac{15}{20} = \\frac{3}{4} = 0{,}75$$\n\nTherefore:\n$$P(\\text{no event}) = 1 - \\frac{15}{20} = \\frac{5}{20} = \\frac{1}{4} = 0{,}25$$\n\n* $\\checkmark 1 - (P(A \\text{ or } B \\text{ or } C))$\n* $\\checkmark$ answer ($\\frac{1}{4}$ or $0{,}25$)",
        "final_answer": "1/4",
        "needs_review": False,
    },
    {
        "question_ref": "10.3.1",
        "marks": 2,
        "topic": "Counting Principles - Permutations with Grouping",
        "passage": "Seven friends (4 boys and 3 girls) want to stand in a straight line next to each other to take a photo.",
        "question": "In how many ways can the 3 girls stand next to each other in the photo?",
        "memo": "Treat the 3 girls as a single unit/block:\nNumber of units = 4 boys + 1 block of girls = 5 units.\nThe 5 units can be arranged in $5!$ ways.\nThe 3 girls within the block can be arranged among themselves in $3!$ ways.\n$$\\text{Total ways} = 3! \\times 5! = 6 \\times 120 = 720$$\n\n* $\\checkmark 3!$\n* $\\checkmark 3! \\times 5! = 720$",
        "final_answer": "720",
        "needs_review": False,
    },
    {
        "question_ref": "10.3.2",
        "marks": 3,
        "topic": "Counting Principles - Probability with Restriction (Not Adjacent)",
        "passage": "Seven friends (4 boys and 3 girls) want to stand in a straight line next to each other to take a photo.",
        "question": "In the next photo, determine the probability that Selwyn (a boy) and Lindiwe (a girl) will NOT stand next to each other in the photo.",
        "memo": "Total possible arrangements of the 7 friends in a line:\n$$n(S) = 7! = 5\\,040$$\n\nNumber of arrangements where Selwyn and Lindiwe stand NEXT to each other:\nTreat Selwyn and Lindiwe as 1 unit. There are 5 other friends + 1 unit = 6 units.\nThe 6 units can be arranged in $6!$ ways, and Selwyn and Lindiwe can be arranged in $2!$ ways within the unit:\n$$n(\\text{together}) = 6! \\times 2! = 720 \\times 2 = 1\\,440$$\n\nNumber of arrangements where they do NOT stand next to each other:\n$$n(\\text{NOT together}) = 7! - (6! \\times 2!) = 5\\,040 - 1\\,440 = 3\\,600$$\n\nProbability:\n$$P(\\text{NOT together}) = \\frac{7! - (6! \\times 2!)}{7!} = \\frac{3\\,600}{5\\,040} = \\frac{5}{7} \\approx 0{,}71$$\n\n**OR/OF**\n$$P(\\text{NOT together}) = 1 - P(\\text{together}) = 1 - \\frac{6! \\times 2!}{7!} = 1 - \\frac{2}{7} = \\frac{5}{7} \\approx 0{,}71$$\n\n* $\\checkmark 7! - (6! \\times 2)$ (or $1 - \\frac{6! \\times 2!}{7!}$)\n* $\\checkmark$ denominator ($7!$)\n* $\\checkmark$ answer ($\\frac{5}{7}$ or $0{,}71$)",
        "final_answer": "5/7",
        "needs_review": False,
    },
]

def make_record(raw):
    ref = raw["question_ref"]
    slug = ref.replace(".", "-")
    item_id = f"{SOURCE_ID}-{slug}"
    return {
        "item_id": item_id,
        "source_id": SOURCE_ID,
        "pair_source_id": PAIR_SOURCE_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": ref,
        "marks": raw["marks"],
        "topic": raw["topic"],
        "passage": raw["passage"],
        "question": raw["question"],
        "memo": raw["memo"],
        "final_answer": raw["final_answer"],
        "needs_review": raw["needs_review"],
        "licence": LICENCE,
        "attribution": ATTRIBUTION,
    }

def main():
    records = [make_record(it) for it in items]
    
    total_marks = sum(r["marks"] for r in records)
    print(f"Total items: {len(records)}")
    print(f"Total marks: {total_marks}")
    assert total_marks == 150, f"Expected 150 marks, got {total_marks}"
    
    out_dir_math = "sa-tutor-kit/sa-tutor-kit/workspace/items/mathematics"
    os.makedirs(out_dir_math, exist_ok=True)
    out_path_1 = os.path.join(out_dir_math, f"{SOURCE_ID}.jsonl")
    
    out_dir_root = "sa-tutor-kit/sa-tutor-kit/workspace/items"
    os.makedirs(out_dir_root, exist_ok=True)
    out_path_2 = os.path.join(out_dir_root, f"{SOURCE_ID}.jsonl")
    
    with open(out_path_1, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"Saved: {out_path_1}")
    
    with open(out_path_2, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"Saved: {out_path_2}")

if __name__ == "__main__":
    main()
