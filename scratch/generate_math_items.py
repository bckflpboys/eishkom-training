# -*- coding: utf-8 -*-
"""
Generator for DBE Mathematics Grade 12 Paper 2 May/June 2023 JSONL items.
Aligns strictly with the Universal Document & Visual Extraction Standard (UDVES).
"""

import json
import os
import re

SOURCE_ID = "dbe-mathematics-g12-p2-2023-may"
PAIR_SOURCE_ID = "dbe-mathematics-g12-p2-2023-may-memo"
SUBJECT = "mathematics"
GRADE = 12
LANGUAGE = "en"
TRACK = "core_maths"
LICENCE = "DBE copyright - check terms"
ATTRIBUTION = "Department of Basic Education"

items = []

def add_item(
    question_ref,
    marks,
    topic,
    passage,
    question,
    memo,
    final_answer="",
    needs_review=False,
    kind="question"
):
    slug_ref = question_ref.replace("(", "").replace(")", "").replace(".", "-")
    item_id = f"{SOURCE_ID}-{slug_ref}"
    items.append({
        "item_id": item_id,
        "source_id": SOURCE_ID,
        "pair_source_id": PAIR_SOURCE_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": kind,
        "question_ref": question_ref,
        "marks": marks,
        "topic": topic,
        "passage": passage,
        "question": question,
        "memo": memo,
        "final_answer": final_answer,
        "needs_review": needs_review,
        "licence": LICENCE,
        "attribution": ATTRIBUTION
    })

# ==============================================================================
# QUESTION 1 [12 marks]
# ==============================================================================

P_Q1_1 = (
    "The owner of a small company wishes to establish whether advertising in a regional newspaper is effective. "
    "The table below shows the amount spent on advertising and the corresponding sales figures for the last 9 years.\n\n"
    "| Amount spent on advertising (in rands) ($x$) | Sales (in rands) ($y$) |\n"
    "| :--- | :--- |\n"
    "| 21 300 | 311 500 |\n"
    "| 23 700 | 326 700 |\n"
    "| 24 800 | 349 200 |\n"
    "| 30 540 | 470 000 |\n"
    "| 24 100 | 316 100 |\n"
    "| 40 680 | 564 200 |\n"
    "| 22 400 | 314 000 |\n"
    "| 35 250 | 487 300 |\n"
    "| 29 110 | 392 900 |"
)

add_item(
    question_ref="1.1.1",
    marks=3,
    topic="Statistics - Least Squares Regression Line",
    passage=P_Q1_1,
    question="Determine the equation of the least squares regression line for the data.",
    memo=(
        "Using a scientific calculator for bivariate linear regression $\\hat{y} = a + bx$:\n"
        "$$a = 1730{,}224\\dots \\approx 1730{,}22$$\n"
        "$$b = 13{,}957\\dots \\approx 13{,}96$$\n"
        "$$\\hat{y} = 1730{,}22 + 13{,}96x$$\n\n"
        "* $\\checkmark a = 1730{,}22$\n"
        "* $\\checkmark b = 13{,}96$\n"
        "* $\\checkmark \\text{equation}$"
    ),
    final_answer="\\hat{y} = 1730.22 + 13.96x",
    needs_review=False
)

add_item(
    question_ref="1.1.2",
    marks=2,
    topic="Statistics - Regression Line Prediction",
    passage=P_Q1_1,
    question="Predict the sales for a year in which the company will spend R28 500 on advertising.",
    memo=(
        "$$\\hat{y} = 1730{,}22 + 13{,}96(28\\,500)$$\n"
        "$$\\hat{y} = \\text{R}399\\,590{,}22$$\n\n"
        "**OR/OF**\n\n"
        "Using calculator memory (unrounded values):\n"
        "$$\\hat{y} = \\text{R}399\\,599{,}64$$\n\n"
        "* $\\checkmark \\text{substitution}$\n"
        "* $\\checkmark \\text{answer}$\n"
        "(2)\n\n"
        "**OR/OF**\n"
        "* $\\checkmark\\checkmark \\text{answer}$\n"
        "(2)"
    ),
    final_answer="R399 590.22",
    needs_review=False
)

add_item(
    question_ref="1.1.3",
    marks=1,
    topic="Statistics - Correlation Coefficient",
    passage=P_Q1_1,
    question="Write down the correlation coefficient of the data.",
    memo=(
        "Using a calculator:\n"
        "$$r = 0{,}98002\\dots \\approx 0{,}98$$\n\n"
        "* $\\checkmark \\text{answer } r = 0{,}98$"
    ),
    final_answer="0.98",
    needs_review=False
)

add_item(
    question_ref="1.1.4",
    marks=1,
    topic="Statistics - Association Description",
    passage=P_Q1_1,
    question="Describe the association between the amount spent on advertising in the regional newspaper and the sales of this company.",
    memo=(
        "There is a very strong positive correlation (or association) between the amount spent on advertising and sales. /\n"
        "Daar is 'n baie sterk positiewe korrelasie tussen die bedrag spandeer op advertensie en die verkope.\n\n"
        "* $\\checkmark \\text{strong positive}$"
    ),
    final_answer="Very strong positive association",
    needs_review=False
)

P_Q1_2 = (
    "The profit that the small company made over the same 9 years is given in the table below.\n\n"
    "| Year | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |\n"
    "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"
    "| Profit (in rands) | 110 750 | 107 376 | 152 338 | 244 480 | 144 021 | 275 994 | 121 900 | 207 636 | 187 700 |"
)

add_item(
    question_ref="1.2.1",
    marks=2,
    topic="Statistics - Mean Profit",
    passage=P_Q1_2,
    question="Calculate the mean profit made over the 9 years.",
    memo=(
        "$$\\bar{x} = \\frac{\\sum x}{n} = \\frac{1\\,552\\,195}{9}$$\n"
        "$$\\bar{x} = 172\\,466{,}11$$\n\n"
        "* $\\checkmark \\bar{x} = \\frac{1\\,552\\,195}{9}$\n"
        "* $\\checkmark \\text{answer: } 172\\,466{,}11$"
    ),
    final_answer="172466.11",
    needs_review=False
)

add_item(
    question_ref="1.2.2",
    marks=1,
    topic="Statistics - Standard Deviation",
    passage=P_Q1_2,
    question="Write down the standard deviation for the data.",
    memo=(
        "Using a calculator:\n"
        "$$\\sigma = 56\\,950{,}09$$\n\n"
        "* $\\checkmark \\text{answer: } 56\\,950{,}09$"
    ),
    final_answer="56950.09",
    needs_review=False
)

add_item(
    question_ref="1.2.3",
    marks=2,
    topic="Statistics - Standard Deviation Interval",
    passage=P_Q1_2,
    question="Determine the number of years in which the company made a profit that was greater than one standard deviation above the mean.",
    memo=(
        "$$\\bar{x} + \\sigma = 172\\,466{,}11 + 56\\,950{,}09 = 229\\,416{,}20$$\n\n"
        "Profits greater than $\\text{R}229\\,416{,}20$:\n"
        "* Year 4: $244\\,480$\n"
        "* Year 6: $275\\,994$\n\n"
        "Therefore, there are $2\\text{ years}$.\n\n"
        "* $\\checkmark \\bar{x} + \\sigma = 229\\,416{,}20$\n"
        "* $\\checkmark 2\\text{ years}$"
    ),
    final_answer="2",
    needs_review=False
)

# ==============================================================================
# QUESTION 2 [8 marks]
# ==============================================================================

P_Q2 = (
    "The ages of the people who attended a music concert was summarised in the table below.\n\n"
    "| AGE | NUMBER OF PEOPLE |\n"
    "| :---: | :---: |\n"
    "| $5 < x \\le 15$ | 20 |\n"
    "| $15 < x \\le 25$ | 25 |\n"
    "| $25 < x \\le 35$ | 60 |\n"
    "| $35 < x \\le 45$ | 90 |\n"
    "| $45 < x \\le 55$ | 55 |\n"
    "| $55 < x \\le 65$ | 40 |\n"
    "| $65 < x \\le 75$ | 30 |"
)

add_item(
    question_ref="2.1",
    marks=1,
    topic="Statistics - Modal Class",
    passage=P_Q2,
    question="Write down the modal class of the data.",
    memo=(
        "The class with the highest frequency ($90$) is:\n"
        "$$35 < x \\le 45$$\n\n"
        "* $\\checkmark \\text{answer } 35 < x \\le 45$"
    ),
    final_answer="35 < x <= 45",
    needs_review=False
)

add_item(
    question_ref="2.2",
    marks=1,
    topic="Statistics - Total Frequency",
    passage=P_Q2,
    question="How many people attended the music concert?",
    memo=(
        "$$\\sum f = 20 + 25 + 60 + 90 + 55 + 40 + 30 = 320\\text{ people}$$\n\n"
        "* $\\checkmark \\text{answer: } 320\\text{ people}$"
    ),
    final_answer="320",
    needs_review=False
)

add_item(
    question_ref="2.3",
    marks=4,
    topic="Statistics - Cumulative Frequency Graph (Ogive)",
    passage=P_Q2,
    question="On the grid provided in the ANSWER BOOK, draw a cumulative frequency graph (ogive) to represent the above data.",
    memo=(
        "Cumulative frequency table:\n"
        "| Interval | Frequency | Cumulative Frequency | Point Plotted |\n"
        "| :---: | :---: | :---: | :---: |\n"
        "| Grounding | - | 0 | $(5; 0)$ |\n"
        "| $5 < x \\le 15$ | 20 | 20 | $(15; 20)$ |\n"
        "| $15 < x \\le 25$ | 25 | 45 | $(25; 45)$ |\n"
        "| $25 < x \\le 35$ | 60 | 105 | $(35; 105)$ |\n"
        "| $35 < x \\le 45$ | 90 | 195 | $(45; 195)$ |\n"
        "| $45 < x \\le 55$ | 55 | 250 | $(55; 250)$ |\n"
        "| $55 < x \\le 65$ | 40 | 290 | $(65; 290)$ |\n"
        "| $65 < x \\le 75$ | 30 | 320 | $(75; 320)$ |\n\n"
        "* $\\checkmark \\text{cumulative frequencies: } 20, 45, 105, 195, 250, 290, 320$\n"
        "* $\\checkmark \\text{grounding at } (5; 0)$\n"
        "* $\\checkmark \\text{plotting points at upper class limits}$\n"
        "* $\\checkmark \\text{smooth S-shaped curve}$"
    ),
    final_answer="",
    needs_review=True
)

add_item(
    question_ref="2.4",
    marks=2,
    topic="Statistics - Median from Ogive",
    passage=P_Q2,
    question="Use the cumulative frequency graph to determine the median age of the people who attended the music concert.",
    memo=(
        "$$\\text{Position of median} = \\frac{n}{2} = \\frac{320}{2} = 160$$\n"
        "Reading the age value corresponding to a cumulative frequency of $160$ on the ogive:\n"
        "$$\\text{Median} \\approx 41\\text{ years}$$ (Accept values in the range $40$ to $42$)\n\n"
        "* $\\checkmark\\checkmark \\text{answer } 41$"
    ),
    final_answer="41",
    needs_review=False
)

# ==============================================================================
# QUESTION 3 [18 marks]
# ==============================================================================

P_Q3 = (
    "In the diagram, the equation of line $\\text{AF}$ is $y = -x - 11$. $\\text{B}$, a point on the $x$-axis, "
    "is the midpoint of the straight line joining $\\text{A}(-1; t)$ and $\\text{C}$. The angles of inclination of $\\text{AF}$ "
    "and $\\text{AC}$ are $\\alpha$ and $63{,}43^\\circ$ respectively. $\\text{AF}$ cuts the $x$-axis in $\\text{E}$. "
    "$\\text{D}$ is a point such that $\\text{DE} \\parallel \\text{AC}$.\n\n"
    "[DIAGRAM: Cartesian plane showing line AF with angle of inclination $\\alpha$ passing through $E$ on the negative $x$-axis "
    "and $F$ in the second quadrant, with equation $y = -x - 11$. Point $A(-1; t)$ lies on line AF in the fourth quadrant. "
    "Line $AC$ joins $A$ to $C$ in the first quadrant with angle of inclination $63{,}43^\\circ$, crossing the $x$-axis at $B$. "
    "Tick marks on segment $AC$ indicate $AB = BC$, so $B$ is the midpoint of $AC$. From point $E$ on line AF, "
    "ray $ED$ extends into the third quadrant with an arrow indicating $DE \\parallel AC$. Angle $F\\hat{E}D$ is indicated.]"
)

add_item(
    question_ref="3.1.1",
    marks=2,
    topic="Analytical Geometry - Point on a Line",
    passage=P_Q3,
    question="Calculate the value of $t$.",
    memo=(
        "Since $A(-1; t)$ lies on the line $y = -x - 11$:\n"
        "$$t = -(-1) - 11$$\n"
        "$$t = 1 - 11$$\n"
        "$$t = -10$$\n\n"
        "* $\\checkmark \\text{substitution of } x = -1$\n"
        "* $\\checkmark t = -10$"
    ),
    final_answer="-10",
    needs_review=False
)

add_item(
    question_ref="3.1.2",
    marks=2,
    topic="Analytical Geometry - Angle of Inclination",
    passage=P_Q3,
    question="Calculate the size of $\\alpha$.",
    memo=(
        "For line $AF$: $y = -x - 11 \\implies m_{AF} = -1$.\n"
        "$$\\tan\\alpha = -1$$\n"
        "$$\\text{Reference angle} = 45^\\circ$$\n"
        "$$\\alpha = 180^\\circ - 45^\\circ = 135^\\circ$$\n\n"
        "* $\\checkmark \\tan\\alpha = -1$\n"
        "* $\\checkmark 135^\\circ$"
    ),
    final_answer="135",
    needs_review=False
)

add_item(
    question_ref="3.1.3",
    marks=2,
    topic="Analytical Geometry - Gradient from Inclination",
    passage=P_Q3,
    question="Calculate the gradient of $\\text{AC}$, to the nearest whole number.",
    memo=(
        "$$m_{AC} = \\tan 63{,}43^\\circ = 1{,}9998\\dots \\approx 2$$\n\n"
        "* $\\checkmark \\tan 63{,}43^\\circ = m_{AC}$\n"
        "* $\\checkmark m_{AC} = 2$"
    ),
    final_answer="2",
    needs_review=False
)

add_item(
    question_ref="3.2",
    marks=2,
    topic="Analytical Geometry - Equation of a Straight Line",
    passage=P_Q3,
    question="Determine the equation of $\\text{AC}$ in the form $y = mx + k$.",
    memo=(
        "Using $m_{AC} = 2$ and $A(-1; -10)$:\n"
        "$$y = 2x + k$$\n"
        "$$-10 = 2(-1) + k \\implies k = -8$$\n"
        "$$y = 2x - 8$$\n\n"
        "**OR/OF**\n"
        "$$y - y_1 = m(x - x_1)$$\n"
        "$$y - (-10) = 2(x - (-1))$$\n"
        "$$y + 10 = 2x + 2$$\n"
        "$$y = 2x - 8$$\n\n"
        "* $\\checkmark \\text{substitution of } m = 2 \\text{ and } A(-1; -10)$\n"
        "* $\\checkmark y = 2x - 8$"
    ),
    final_answer="y = 2x - 8",
    needs_review=False
)

add_item(
    question_ref="3.3.1",
    marks=3,
    topic="Analytical Geometry - Midpoint and Coordinates",
    passage=P_Q3,
    question="Calculate the coordinates of $\\text{C}$.",
    memo=(
        "Point $B$ is the $x$-intercept of line $AC$ ($y = 0$):\n"
        "$$0 = 2x - 8 \\implies 2x = 8 \\implies x_B = 4 \\implies B(4; 0)$$\n\n"
        "Since $B(4; 0)$ is the midpoint of $AC$ with $A(-1; -10)$ and $C(x_C; y_C)$:\n"
        "$$\\frac{x_C + (-1)}{2} = 4 \\implies x_C - 1 = 8 \\implies x_C = 9$$\n"
        "$$\\frac{y_C + (-10)}{2} = 0 \\implies y_C - 10 = 0 \\implies y_C = 10$$\n"
        "$$\\therefore C(9; 10)$$\n\n"
        "**OR/OF by translation / met translasie:**\n"
        "From $A(-1; -10)$ to $B(4; 0)$: $(x; y) \\to (x + 5; y + 10)$\n"
        "From $B(4; 0)$ to $C$: $(4 + 5; 0 + 10) = (9; 10)$\n\n"
        "* $\\checkmark x_B = 4$\n"
        "* $\\checkmark x_C = 9$\n"
        "* $\\checkmark y_C = 10$\n"
        "(3)\n\n"
        "**OR/OF**\n"
        "* $\\checkmark (x + 5; y + 10)$\n"
        "* $\\checkmark x_C = 9$\n"
        "* $\\checkmark y_C = 10$\n"
        "(3)"
    ),
    final_answer="(9; 10)",
    needs_review=False
)

add_item(
    question_ref="3.3.2",
    marks=3,
    topic="Analytical Geometry - Angle Between Lines",
    passage=P_Q3,
    question="Calculate the size of $\\text{F\\hat{E}D}$.",
    memo=(
        "**Method 1:**\n"
        "$$\\hat{A}_1 = 63{,}43^\\circ \\quad [\\text{vert. opp } \\angle\\text{'s}]$$\n"
        "$$\\hat{E}_2 = 63{,}43^\\circ \\quad [\\text{corres. } \\angle\\text{'s, } DE \\parallel AC]$$\n"
        "$$\\hat{E}_1 = 180^\\circ - 135^\\circ = 45^\\circ \\quad [\\angle\\text{'s on straight line}]$$\n"
        "$$\\text{F\\hat{E}D} = \\hat{E}_1 + \\hat{E}_2 = 45^\\circ + 63{,}43^\\circ = 108{,}43^\\circ$$\n\n"
        "**OR/OF Method 2:**\n"
        "$$\\text{E\\hat{A}B} = 135^\\circ - 63{,}43^\\circ = 71{,}57^\\circ \\quad [\\text{ext } \\angle \\text{ of } \\Delta]$$\n"
        "$$\\text{D\\hat{E}A} = \\text{E\\hat{A}B} = 71{,}57^\\circ \\quad [\\text{alt } \\angle\\text{'s, } DE \\parallel AC]$$\n"
        "$$\\text{F\\hat{E}D} = 180^\\circ - 71{,}57^\\circ = 108{,}43^\\circ \\quad [\\angle\\text{'s on straight line}]$$\n\n"
        "**OR/OF Method 3:**\n"
        "$$\\text{A\\hat{B}E} = 63{,}43^\\circ \\quad [\\text{vert. opp } \\angle\\text{'s}]$$\n"
        "$$\\text{D\\hat{E}O} = 180^\\circ - 63{,}43^\\circ = 116{,}57^\\circ \\quad [\\text{co-int. } \\angle\\text{'s, } DE \\parallel AC]$$\n"
        "$$\\text{F\\hat{E}D} = 360^\\circ - (116{,}57^\\circ + 135^\\circ) = 108{,}43^\\circ$$\n\n"
        "* $\\checkmark \\hat{ABE} = 63{,}43^\\circ$ (or $\\hat{E}_2 = 63{,}43^\\circ$)\n"
        "* $\\checkmark \\hat{E}_1 = 45^\\circ$ (or $\\text{D\\hat{E}A} = 71{,}57^\\circ$ or $\\text{D\\hat{E}O} = 116{,}57^\\circ$)\n"
        "* $\\checkmark \\text{F\\hat{E}D} = 108{,}43^\\circ$"
    ),
    final_answer="108.43",
    needs_review=False
)

add_item(
    question_ref="3.4",
    marks=4,
    topic="Analytical Geometry - Parallelogram and Circle Equation",
    passage=P_Q3,
    question=(
        "$\\text{G}$ is a point such that $\\text{EAGC}$, in that order, is a parallelogram.\n\n"
        "Determine the equation of a circle centred at $\\text{G}$ and passing through the point $\\text{B}$. "
        "Write your answer in the form $(x - a)^2 + (y - b)^2 = r^2$."
    ),
    memo=(
        "Point $E$ is the $x$-intercept of line $AF$ ($y = -x - 11$):\n"
        "$$0 = -x - 11 \\implies x_E = -11 \\implies E(-11; 0)$$\n\n"
        "In parallelogram $EAGC$, the diagonals are $EG$ and $AC$. Diagonals bisect each other at their common midpoint.\n"
        "The midpoint of diagonal $AC$ is point $B(4; 0)$:\n"
        "$$\\frac{x_E + x_G}{2} = x_B \\implies \\frac{-11 + x_G}{2} = 4 \\implies -11 + x_G = 8 \\implies x_G = 19$$\n"
        "$$\\frac{y_E + y_G}{2} = y_B \\implies \\frac{0 + y_G}{2} = 0 \\implies y_G = 0$$\n"
        "$$\\therefore G(19; 0)$$\n\n"
        "The circle is centred at $G(19; 0)$ and passes through $B(4; 0)$:\n"
        "$$r = GB = 19 - 4 = 15$$\n"
        "$$r^2 = 15^2 = 225$$\n\n"
        "Equation of the circle:\n"
        "$$(x - 19)^2 + y^2 = 225$$\n\n"
        "* $\\checkmark x_E = -11$\n"
        "* $\\checkmark x_G = 19$\n"
        "* $\\checkmark (x - 19)^2 + y^2$\n"
        "* $\\checkmark 225$"
    ),
    final_answer="(x - 19)^2 + y^2 = 225",
    needs_review=False
)

# ==============================================================================
# QUESTION 4 [22 marks]
# ==============================================================================

P_Q4 = (
    "In the diagram, the equation of the circle centred at $\\text{N}(-12; 5)$ is $x^2 + y^2 + 24x - 10y + 153 = 0$. "
    "The equation of the circle centred at $\\text{M}$ is $(x + 6)^2 + (y + 3)^2 = 25$. "
    "$\\text{PS}$ and $\\text{PR}$ are tangents to the circle centred at $\\text{M}$ at $\\text{S}$ and $\\text{R}$ respectively. "
    "$\\text{PR}$ is parallel to the $x$-axis. $\\text{K}(-17; -5)$ is a point on $\\text{PS}$. "
    "The straight line joining $\\text{N}$ and $\\text{M}$ cuts the smaller circle at $\\text{T}$ and the larger circle at $\\text{S}$.\n\n"
    "[DIAGRAM: Cartesian plane showing two non-intersecting circles in the second and third/fourth quadrants. "
    "Circle with centre $N(-12; 5)$ has equation $x^2 + y^2 + 24x - 10y + 153 = 0$. "
    "Circle with centre $M$ has equation $(x + 6)^2 + (y + 3)^2 = 25$ with radius $5$. "
    "Line segment $NM$ connects the centres and intersects circle $N$ at $T$ and circle $M$ at $S$. "
    "Tangents $PS$ and $PR$ to circle $M$ intersect at external point $P$, with tangent $PR$ parallel to the $x$-axis at the bottom. "
    "Point $K(-17; -5)$ lies on tangent $PS$.]"
)

add_item(
    question_ref="4.1",
    marks=2,
    topic="Analytical Geometry - Centre of a Circle",
    passage=P_Q4,
    question="Write down the coordinates of $\\text{M}$.",
    memo=(
        "From the circle equation $(x + 6)^2 + (y + 3)^2 = 25$:\n"
        "$$M(-6; -3)$$\n\n"
        "* $\\checkmark x = -6$\n"
        "* $\\checkmark y = -3$"
    ),
    final_answer="(-6; -3)",
    needs_review=False
)

add_item(
    question_ref="4.2.1",
    marks=2,
    topic="Analytical Geometry - Radius of a Circle",
    passage=P_Q4,
    question="Calculate the length of the radius of the smaller circle.",
    memo=(
        "For circle $N$:\n"
        "$$x^2 + y^2 + 24x - 10y + 153 = 0$$\n"
        "$$(x^2 + 24x + 144) + (y^2 - 10y + 25) = -153 + 144 + 25$$\n"
        "$$(x + 12)^2 + (y - 5)^2 = 16$$\n"
        "$$r^2 = 16 \\implies r = 4\\text{ units}$$\n\n"
        "* $\\checkmark r^2 = -153 + 144 + 25 = 16$\n"
        "* $\\checkmark r = 4\\text{ units}$"
    ),
    final_answer="4",
    needs_review=False
)

add_item(
    question_ref="4.2.2",
    marks=4,
    topic="Analytical Geometry - Distance Between Points on Circle Line",
    passage=P_Q4,
    question="Calculate the length of $\\text{TS}$.",
    memo=(
        "Distance between centres $N(-12; 5)$ and $M(-6; -3)$:\n"
        "$$NM = \\sqrt{(-12 - (-6))^2 + (5 - (-3))^2} = \\sqrt{(-6)^2 + (8)^2} = \\sqrt{36 + 64} = 10\\text{ units}$$\n\n"
        "From the diagram, $N, T, S, M$ lie along line segment $NM$:\n"
        "* Radius of smaller circle $N$: $NT = 4\\text{ units}$\n"
        "* Radius of larger circle $M$: $SM = 5\\text{ units}$\n"
        "* $NM = NT + TS + SM$\n"
        "$$10 = 4 + TS + 5$$\n"
        "$$TS = 10 - 9 = 1\\text{ unit}$$\n\n"
        "* $\\checkmark \\text{substitution into distance formula}$\n"
        "* $\\checkmark NM = 10\\text{ units}$\n"
        "* $\\checkmark SM = 5\\text{ units}$\n"
        "* $\\checkmark TS = 1\\text{ unit}$"
    ),
    final_answer="1",
    needs_review=False
)

add_item(
    question_ref="4.3.1",
    marks=2,
    topic="Analytical Geometry - Equation of Horizontal Tangent",
    passage=P_Q4,
    question="Determine the equation of the tangent $\\text{PR}$.",
    memo=(
        "Tangent $PR$ is horizontal (parallel to the $x$-axis) and touches circle $M$ at $R$.\n"
        "Centre $M$ is $(-6; -3)$ and the radius of circle $M$ is $5$.\n"
        "Since $PR$ lies below the centre $M$:\n"
        "$$y_R = y_M - r = -3 - 5 = -8$$\n"
        "Therefore, the equation of the horizontal line $PR$ is:\n"
        "$$y = -8$$\n\n"
        "* $\\checkmark y_R = -8$\n"
        "* $\\checkmark y = -8$"
    ),
    final_answer="y = -8",
    needs_review=False
)

add_item(
    question_ref="4.3.2",
    marks=5,
    topic="Analytical Geometry - Equation of Tangent Line",
    passage=P_Q4,
    question="Determine the equation of the tangent $\\text{PS}$, in the form $y = mx + c$.",
    memo=(
        "**Method 1:**\n"
        "Gradient of the line of centres $NM$ joining $N(-12; 5)$ and $M(-6; -3)$:\n"
        "$$m_{NM} = \\frac{5 - (-3)}{-12 - (-6)} = \\frac{8}{-6} = -\\frac{4}{3}$$\n\n"
        "Since tangent $PS \\perp NM$ at $S$ (radius $\\perp$ tangent):\n"
        "$$m_{\\text{tangent}} = \\frac{3}{4}$$\n\n"
        "Point $K(-17; -5)$ lies on tangent $PS$:\n"
        "$$y - y_1 = m(x - x_1)$$\n"
        "$$y - (-5) = \\frac{3}{4}(x - (-17))$$\n"
        "$$y + 5 = \\frac{3}{4}x + \\frac{51}{4}$$\n"
        "$$y = \\frac{3}{4}x + \\frac{31}{4} \\quad \\left(\\text{or } y = \\frac{3}{4}x + 7\\frac{3}{4} \\text{ or } y = 0{,}75x + 7{,}75\\right)$$\n\n"
        "**OR/OF Method 2:**\n"
        "Since $NM = 10$, $NT = 4$, $TS = 1 \\implies NS = 5$.\n"
        "Since radius $SM = 5$, $S$ is the midpoint of $NM$:\n"
        "$$S\\left(\\frac{-12 + (-6)}{2}; \\frac{5 + (-3)}{2}\\right) = S(-9; 1)$$\n"
        "$$m_{SK} = \\frac{1 - (-5)}{-9 - (-17)} = \\frac{6}{8} = \\frac{3}{4}$$\n"
        "$$y - 1 = \\frac{3}{4}(x - (-9)) \\implies y = \\frac{3}{4}x + \\frac{31}{4}$$\n\n"
        "* $\\checkmark \\text{substitution for } m_{NM}$\n"
        "* $\\checkmark m_{NM} = -\\frac{4}{3}$\n"
        "* $\\checkmark m_{\\text{tangent}} = \\frac{3}{4}$\n"
        "* $\\checkmark \\text{substitution of } m = \\frac{3}{4} \\text{ and } K(-17; -5)$\n"
        "* $\\checkmark y = \\frac{3}{4}x + \\frac{31}{4}$\n"
        "(5)"
    ),
    final_answer="y = 3/4x + 31/4",
    needs_review=False
)

add_item(
    question_ref="4.4.1",
    marks=5,
    topic="Analytical Geometry - Perimeter of Quadrilateral",
    passage=P_Q4,
    question="Quadrilateral $\\text{PSMR}$ is drawn. Calculate the perimeter of $\\text{PSMR}$.",
    memo=(
        "Point $P$ is the intersection of tangents $PR$ and $PS$:\n"
        "Tangent $PR$: $y = -8$\n"
        "Tangent $PS$: $y = \\frac{3}{4}x + \\frac{31}{4}$\n\n"
        "$$-8 = \\frac{3}{4}x + \\frac{31}{4}$$\n"
        "$$-32 = 3x + 31$$\n"
        "$$3x = -63 \\implies x = -21$$\n"
        "$$\\therefore P(-21; -8)$$\n\n"
        "Point $R$ has $x$-coordinate $x_R = x_M = -6$ and $y_R = -8$, so $R(-6; -8)$:\n"
        "$$PR = -6 - (-21) = 15\\text{ units}$$\n\n"
        "Since tangents from an external point to a circle are equal in length:\n"
        "$$PS = PR = 15\\text{ units} \\quad [\\text{tangents from same point}]$$\n"
        "Radii of circle $M$:\n"
        "$$MS = MR = 5\\text{ units}$$\n\n"
        "$$\\text{Perimeter of } PSMR = PS + SM + MR + PR = 15 + 5 + 5 + 15 = 40\\text{ units}$$\n\n"
        "* $\\checkmark -8 = \\frac{3}{4}x + \\frac{31}{4}$\n"
        "* $\\checkmark x = -21$\n"
        "* $\\checkmark PR = PS = 15\\text{ units}$\n"
        "* $\\checkmark MS = MR = 5\\text{ units}$\n"
        "* $\\checkmark \\text{Perimeter} = 40\\text{ units}$"
    ),
    final_answer="40",
    needs_review=False
)

add_item(
    question_ref="4.4.2",
    marks=2,
    topic="Analytical Geometry - Ratio of Areas",
    passage=P_Q4,
    question="Quadrilateral $\\text{PSMR}$ is drawn. Calculate the ratio of $\\frac{\\text{area of }\\Delta\\text{NPS}}{\\text{area of quadrilateral PSMR}}$.",
    memo=(
        "In $\\Delta NPS$, $NS \\perp SP$ (since $NM \\perp PS$ at $S$):\n"
        "$$\\text{Area of } \\Delta NPS = \\frac{1}{2} \\times NS \\times SP = \\frac{1}{2}(5)(15) = 37{,}5$$\n\n"
        "Quadrilateral $PSMR$ is composed of two right-angled triangles $\\Delta SPM$ and $\\Delta PRM$:\n"
        "$$\\text{Area of quadrilateral } PSMR = 2 \\times \\left(\\frac{1}{2} \\times SM \\times SP\\right) = 2 \\times \\left(\\frac{1}{2}(5)(15)\\right) = 75$$\n\n"
        "$$\\frac{\\text{area of } \\Delta NPS}{\\text{area of quadrilateral } PSMR} = \\frac{37{,}5}{75} = \\frac{1}{2}$$\n\n"
        "**OR/OF**\n"
        "$\\Delta NPS \\equiv \\Delta SPM \\equiv \\Delta MPR$ (congruent right-angled triangles with legs $5$ and $15$).\n"
        "Quadrilateral $PSMR$ comprises two such triangles, so:\n"
        "$$\\frac{\\text{area of } \\Delta NPS}{\\text{area of quadrilateral } PSMR} = \\frac{1}{2}$$\n\n"
        "* $\\checkmark \\text{substitution into area formula / congruence relationship}$\n"
        "* $\\checkmark \\text{answer } \\frac{1}{2}$"
    ),
    final_answer="1/2",
    needs_review=False
)

# ==============================================================================
# QUESTION 5 [28 marks]
# ==============================================================================

add_item(
    question_ref="5.1",
    marks=5,
    topic="Trigonometry - Simplification using Reduction Formulae",
    passage="",
    question=(
        "Without using a calculator, simplify the following expression to a single trigonometry ratio:\n"
        "$$\\frac{1 - \\sin(-\\theta)\\cos(90^\\circ + \\theta)}{\\cos(\\theta - 360^\\circ)}$$"
    ),
    memo=(
        "$$\\frac{1 - \\sin(-\\theta)\\cos(90^\\circ + \\theta)}{\\cos(\\theta - 360^\\circ)}$$\n"
        "$$= \\frac{1 - (-\\sin\\theta)(-\\sin\\theta)}{\\cos\\theta}$$\n"
        "$$= \\frac{1 - \\sin^2\\theta}{\\cos\\theta}$$\n"
        "$$= \\frac{\\cos^2\\theta}{\\cos\\theta}$$\n"
        "$$= \\cos\\theta$$\n\n"
        "* $\\checkmark \\sin(-\\theta) = -\\sin\\theta$\n"
        "* $\\checkmark \\cos(90^\\circ + \\theta) = -\\sin\\theta$\n"
        "* $\\checkmark \\cos(\\theta - 360^\\circ) = \\cos\\theta$\n"
        "* $\\checkmark 1 - \\sin^2\\theta = \\cos^2\\theta$\n"
        "* $\\checkmark \\text{answer } \\cos\\theta$"
    ),
    final_answer="\\cos\\theta",
    needs_review=False
)

P_Q5_2 = "Given that $\\cos 20^\\circ = p$"

add_item(
    question_ref="5.2.1",
    marks=2,
    topic="Trigonometry - Reduction Formula in Terms of p",
    passage=P_Q5_2,
    question="Without using a calculator, write $\\cos 200^\\circ$ in terms of $p$.",
    memo=(
        "$$\\cos 200^\\circ = \\cos(180^\\circ + 20^\\circ) = -\\cos 20^\\circ = -p$$\n\n"
        "* $\\checkmark \\text{reduction: } -\\cos 20^\\circ$\n"
        "* $\\checkmark \\text{answer: } -p$"
    ),
    final_answer="-p",
    needs_review=False
)

add_item(
    question_ref="5.2.2",
    marks=2,
    topic="Trigonometry - Negative Angles and Co-functions in Terms of p",
    passage=P_Q5_2,
    question="Without using a calculator, write $\\sin(-70^\\circ)$ in terms of $p$.",
    memo=(
        "$$\\sin(-70^\\circ) = -\\sin 70^\\circ = -\\cos(90^\\circ - 70^\\circ) = -\\cos 20^\\circ = -p$$\n\n"
        "**OR/OF**\n"
        "$$\\sin(-70^\\circ) = -\\sin 70^\\circ = -p$$\n\n"
        "* $\\checkmark \\text{reduction: } -\\sin 70^\\circ \\text{ or } -\\cos 20^\\circ$\n"
        "* $\\checkmark \\text{answer: } -p$"
    ),
    final_answer="-p",
    needs_review=False
)

add_item(
    question_ref="5.2.3",
    marks=3,
    topic="Trigonometry - Double Angle Identity in Terms of p",
    passage=P_Q5_2,
    question="Without using a calculator, write $\\sin 10^\\circ$ in terms of $p$.",
    memo=(
        "Using double angle identity $\\cos 2A = 1 - 2\\sin^2 A$:\n"
        "$$\\cos 20^\\circ = \\cos(2(10^\\circ)) = 1 - 2\\sin^2 10^\\circ$$\n"
        "$$p = 1 - 2\\sin^2 10^\\circ$$\n"
        "$$2\\sin^2 10^\\circ = 1 - p$$\n"
        "$$\\sin^2 10^\\circ = \\frac{1 - p}{2}$$\n"
        "Since $10^\\circ$ is in the first quadrant, $\\sin 10^\\circ > 0$:\n"
        "$$\\sin 10^\\circ = \\sqrt{\\frac{1 - p}{2}}$$\n\n"
        "**OR/OF**\n"
        "$$\\sin 10^\\circ = \\sin(30^\\circ - 20^\\circ)$$\n"
        "$$= \\sin 30^\\circ\\cos 20^\\circ - \\cos 30^\\circ\\sin 20^\\circ$$\n"
        "$$= \\frac{1}{2}p - \\frac{\\sqrt{3}}{2}\\sqrt{1 - p^2} = \\frac{p - \\sqrt{3}\\sqrt{1 - p^2}}{2}$$\n\n"
        "* $\\checkmark \\text{double angle formula: } \\cos 2(10^\\circ) = 1 - 2\\sin^2 10^\\circ$\n"
        "* $\\checkmark \\sin 10^\\circ \\text{ as subject}$\n"
        "* $\\checkmark \\text{answer: } \\sqrt{\\frac{1 - p}{2}}$\n"
        "(3)\n\n"
        "**OR/OF**\n"
        "* $\\checkmark \\text{using special angle } \\sin(30^\\circ - 20^\\circ)$\n"
        "* $\\checkmark \\text{expansion}$\n"
        "* $\\checkmark \\text{answer: } \\frac{p - \\sqrt{3}\\sqrt{1 - p^2}}{2}$\n"
        "(3)"
    ),
    final_answer="\\sqrt{\\frac{1 - p}{2}}",
    needs_review=False
)

add_item(
    question_ref="5.3",
    marks=3,
    topic="Trigonometry - Compound Angle Evaluation",
    passage="",
    question=(
        "Determine, without using a calculator, the value of:\n"
        "$$\\cos(A + 55^\\circ)\\cos(A + 10^\\circ) + \\sin(A + 55^\\circ)\\sin(A + 10^\\circ)$$"
    ),
    memo=(
        "Using compound angle identity $\\cos(x - y) = \\cos x \\cos y + \\sin x \\sin y$:\n"
        "$$\\cos(A + 55^\\circ)\\cos(A + 10^\\circ) + \\sin(A + 55^\\circ)\\sin(A + 10^\\circ)$$\n"
        "$$= \\cos[(A + 55^\\circ) - (A + 10^\\circ)]$$\n"
        "$$= \\cos(A + 55^\\circ - A - 10^\\circ)$$\n"
        "$$= \\cos 45^\\circ$$\n"
        "$$= \\frac{1}{\\sqrt{2}} \\quad \\text{or} \\quad \\frac{\\sqrt{2}}{2}$$\n\n"
        "* $\\checkmark\\checkmark \\text{compound identity: } \\cos[(A + 55^\\circ) - (A + 10^\\circ)]$\n"
        "* $\\checkmark \\text{answer: } \\frac{\\sqrt{2}}{2} \\text{ or } \\frac{1}{\\sqrt{2}}$"
    ),
    final_answer="\\frac{\\sqrt{2}}{2}",
    needs_review=False
)

P_Q5_4 = "Consider: $\\frac{\\cos 2x + \\sin 2x - \\cos^2 x}{\\sin x - 2\\cos x} = -\\sin x$"

add_item(
    question_ref="5.4.1",
    marks=3,
    topic="Trigonometry - Proving an Identity",
    passage=P_Q5_4,
    question="Prove the above identity.",
    memo=(
        "$$\\text{LHS} = \\frac{\\cos 2x + \\sin 2x - \\cos^2 x}{\\sin x - 2\\cos x}$$\n"
        "$$= \\frac{(\\cos^2 x - \\sin^2 x) + 2\\sin x\\cos x - \\cos^2 x}{\\sin x - 2\\cos x}$$\n"
        "$$= \\frac{-\\sin^2 x + 2\\sin x\\cos x}{\\sin x - 2\\cos x}$$\n"
        "$$= \\frac{-\\sin x(\\sin x - 2\\cos x)}{\\sin x - 2\\cos x}$$\n"
        "$$= -\\sin x = \\text{RHS}$$\n\n"
        "* $\\checkmark \\cos 2x = \\cos^2 x - \\sin^2 x$\n"
        "* $\\checkmark \\sin 2x = 2\\sin x\\cos x$\n"
        "* $\\checkmark \\text{common factor of } -\\sin x$"
    ),
    final_answer="",
    needs_review=False
)

add_item(
    question_ref="5.4.2",
    marks=3,
    topic="Trigonometry - Identity Application",
    passage=P_Q5_4,
    question="Determine the value of $\\frac{\\cos 2x + \\sin 2x - \\cos^2 x}{-3\\sin^2 x + 6\\sin x \\cos x}$.",
    memo=(
        "$$\\frac{\\cos 2x + \\sin 2x - \\cos^2 x}{-3\\sin^2 x + 6\\sin x\\cos x} = \\frac{\\cos 2x + \\sin 2x - \\cos^2 x}{-3\\sin x(\\sin x - 2\\cos x)}$$\n"
        "$$= \\frac{1}{-3\\sin x} \\times \\left(\\frac{\\cos 2x + \\sin 2x - \\cos^2 x}{\\sin x - 2\\cos x}\\right)$$\n"
        "From 5.4.1, $\\frac{\\cos 2x + \\sin 2x - \\cos^2 x}{\\sin x - 2\\cos x} = -\\sin x$:\n"
        "$$= \\frac{1}{-3\\sin x} \\times (-\\sin x) = \\frac{-\\sin x}{-3\\sin x} = \\frac{1}{3}$$\n\n"
        "* $\\checkmark \\text{common factor } -3\\sin x(\\sin x - 2\\cos x)$\n"
        "* $\\checkmark \\text{substitution of } -\\sin x$\n"
        "* $\\checkmark \\text{answer } \\frac{1}{3}$"
    ),
    final_answer="1/3",
    needs_review=False
)

P_Q5_5 = "Given: $3\\tan 4x = -2\\cos 4x$"

add_item(
    question_ref="5.5.1",
    marks=4,
    topic="Trigonometry - Trigonometric Equation Proof",
    passage=P_Q5_5,
    question="Without using a calculator, show that $\\sin 4x = -0{,}5$ is the only solution to the above equation.",
    memo=(
        "$$3\\tan 4x = -2\\cos 4x$$\n"
        "$$3\\left(\\frac{\\sin 4x}{\\cos 4x}\\right) = -2\\cos 4x$$\n"
        "$$3\\sin 4x = -2\\cos^2 4x$$\n"
        "$$3\\sin 4x + 2\\cos^2 4x = 0$$\n"
        "Using $\\cos^2 4x = 1 - \\sin^2 4x$:\n"
        "$$3\\sin 4x + 2(1 - \\sin^2 4x) = 0$$\n"
        "$$3\\sin 4x + 2 - 2\\sin^2 4x = 0$$\n"
        "$$2\\sin^2 4x - 3\\sin 4x - 2 = 0$$\n"
        "$$(2\\sin 4x + 1)(\\sin 4x - 2) = 0$$\n"
        "$$2\\sin 4x + 1 = 0 \\implies \\sin 4x = -\\frac{1}{2} = -0{,}5$$\n"
        "$$\\text{or } \\sin 4x - 2 = 0 \\implies \\sin 4x = 2$$\n"
        "Since $-1 \\le \\sin 4x \\le 1$, $\\sin 4x = 2$ has no solution ($\\sin 4x \\ne 2$).\n"
        "Therefore, $\\sin 4x = -0{,}5$ is the only solution.\n\n"
        "* $\\checkmark \\tan 4x = \\frac{\\sin 4x}{\\cos 4x}$\n"
        "* $\\checkmark 1 - \\sin^2 4x$\n"
        "* $\\checkmark \\text{standard form: } 2\\sin^2 4x - 3\\sin 4x - 2 = 0$\n"
        "* $\\checkmark \\text{factors: } (2\\sin 4x + 1)(\\sin 4x - 2) = 0 \\text{ and } \\sin 4x \\ne 2$"
    ),
    final_answer="\\sin 4x = -0.5",
    needs_review=False
)

add_item(
    question_ref="5.5.2",
    marks=3,
    topic="Trigonometry - General Solution",
    passage=P_Q5_5,
    question="Hence, determine the general solution of $x$ in the equation $3\\tan 4x = -2\\cos 4x$.",
    memo=(
        "From 5.5.1: $\\sin 4x = -\\frac{1}{2} = -0{,}5$.\n"
        "$$\\text{Reference angle} = 30^\\circ$$\n\n"
        "Quadrant 3:\n"
        "$$4x = 180^\\circ + 30^\\circ + k \\cdot 360^\\circ = 210^\\circ + k \\cdot 360^\\circ$$\n"
        "$$x = 52{,}5^\\circ + k \\cdot 90^\\circ; \\quad k \\in \\mathbb{Z}$$\n\n"
        "Quadrant 4:\n"
        "$$4x = 360^\\circ - 30^\\circ + k \\cdot 360^\\circ = 330^\\circ + k \\cdot 360^\\circ$$\n"
        "$$x = 82{,}5^\\circ + k \\cdot 90^\\circ; \\quad k \\in \\mathbb{Z}$$\n\n"
        "* $\\checkmark 210^\\circ \\text{ and } 330^\\circ$\n"
        "* $\\checkmark 52{,}5^\\circ \\text{ and } 82{,}5^\\circ$\n"
        "* $\\checkmark + k \\cdot 90^\\circ; k \\in \\mathbb{Z}$"
    ),
    final_answer="x = 52.5^\\circ + k \\cdot 90^\\circ \\text{ or } x = 82.5^\\circ + k \\cdot 90^\\circ, k \\in \\mathbb{Z}",
    needs_review=False
)

# ==============================================================================
# QUESTION 6 [13 marks]
# ==============================================================================

P_Q6 = (
    "In the diagram below, the graph of $f(x) = \\tan(x - 45^\\circ)$ is drawn for $x \\in [-90^\\circ; 180^\\circ]$.\n\n"
    "[DIAGRAM: Cartesian grid with $x \\in [-90^\\circ; 180^\\circ]$ and $y \\in [-3; 3]$. "
    "The graph of $f(x) = \\tan(x - 45^\\circ)$ is drawn with vertical dashed asymptotes at $x = -45^\\circ$ and $x = 135^\\circ$. "
    "Key points shown: endpoint at $(-90^\\circ; 1)$, $y$-intercept at $(0^\\circ; -1)$, $x$-intercept at $(45^\\circ; 0)$, "
    "point at $(90^\\circ; 1)$, and endpoint at $(180^\\circ; -1)$.]"
)

add_item(
    question_ref="6.1",
    marks=1,
    topic="Trigonometric Functions - Period",
    passage=P_Q6,
    question="Write down the period of $f$.",
    memo=(
        "$$\\text{Period} = 180^\\circ$$\n\n"
        "* $\\checkmark \\text{answer } 180^\\circ$"
    ),
    final_answer="180^\\circ",
    needs_review=False
)

add_item(
    question_ref="6.2",
    marks=3,
    topic="Trigonometric Functions - Sketching Cosine Graph",
    passage=P_Q6,
    question=(
        "Draw the graph of $g(x) = -\\cos 2x$ for the interval $x \\in [-90^\\circ; 180^\\circ]$ on the grid given in the ANSWER BOOK. "
        "Show ALL intercepts with the axes, as well as the minimum and maximum points of the graph."
    ),
    memo=(
        "For $g(x) = -\\cos 2x$ on $[-90^\\circ; 180^\\circ]$:\n"
        "* Amplitude $= 1$, Period $= \\frac{360^\\circ}{2} = 180^\\circ$\n"
        "* End points: $(-90^\\circ; 1)$ and $(180^\\circ; -1)$\n"
        "* $y$-intercept: $(0^\\circ; -1)$\n"
        "* $x$-intercepts: $(-45^\\circ; 0)$, $(45^\\circ; 0)$, $(135^\\circ; 0)$\n"
        "* Local maximum points: $(-90^\\circ; 1)$ [endpoint], $(90^\\circ; 1)$\n"
        "* Local minimum points: $(0^\\circ; -1)$, $(180^\\circ; -1)$ [endpoint]\n\n"
        "* $\\checkmark x\\text{-intercepts: } (-45^\\circ; 0), (45^\\circ; 0), (135^\\circ; 0)$\n"
        "* $\\checkmark \\text{turning points: } (0^\\circ; -1), (90^\\circ; 1)$\n"
        "* $\\checkmark \\text{end points: } (-90^\\circ; 1), (180^\\circ; -1)$"
    ),
    final_answer="",
    needs_review=True
)

add_item(
    question_ref="6.3",
    marks=1,
    topic="Trigonometric Functions - Range",
    passage=P_Q6,
    question="Write down the range of $g$.",
    memo=(
        "For $g(x) = -\\cos 2x$:\n"
        "$$y \\in [-1; 1] \\quad \\text{OR/OF} \\quad -1 \\le y \\le 1$$\n\n"
        "* $\\checkmark \\text{answer } y \\in [-1; 1]$"
    ),
    final_answer="[-1; 1]",
    needs_review=False
)

add_item(
    question_ref="6.4",
    marks=2,
    topic="Trigonometric Functions - Horizontal Shift and Identity",
    passage=P_Q6,
    question="The graph of $g$ is shifted $45^\\circ$ to the left to form the graph of $h$. Determine the equation of $h$ in its simplest form.",
    memo=(
        "$$g(x) = -\\cos 2x$$\n"
        "$$h(x) = g(x + 45^\\circ) = -\\cos[2(x + 45^\\circ)]$$\n"
        "$$= -\\cos(2x + 90^\\circ)$$\n"
        "$$= -(-\\sin 2x) = \\sin 2x$$\n\n"
        "* $\\checkmark -\\cos 2(x + 45^\\circ)$\n"
        "* $\\checkmark \\sin 2x$"
    ),
    final_answer="h(x) = \\sin 2x",
    needs_review=False
)

add_item(
    question_ref="6.5.1",
    marks=2,
    topic="Trigonometric Functions - Graphical Inequality",
    passage=P_Q6,
    question="Use the graph(s) to determine the values of $x$ in the interval $x \\in [-90^\\circ; 90^\\circ]$ for which: $f(x) > 1$",
    memo=(
        "For $f(x) = \\tan(x - 45^\\circ)$ on $[-90^\\circ; 90^\\circ]$:\n"
        "At $x = -90^\\circ$, $f(-90^\\circ) = 1$. As $x$ increases towards the asymptote at $x = -45^\\circ$, $f(x) > 1$.\n"
        "From $x = -45^\\circ$ to $x = 90^\\circ$, $f(x) \\le 1$ (reaching $1$ at $x = 90^\\circ$).\n"
        "Therefore:\n"
        "$$x \\in (-90^\\circ; -45^\\circ) \\quad \\text{OR/OF} \\quad -90^\\circ < x < -45^\\circ$$\n\n"
        "* $\\checkmark\\checkmark x \\in (-90^\\circ; -45^\\circ)$"
    ),
    final_answer="-90^\\circ < x < -45^\\circ",
    needs_review=False
)

add_item(
    question_ref="6.5.2",
    marks=4,
    topic="Trigonometric Functions - Graphical Inequality",
    passage=P_Q6,
    question="Use the graph(s) to determine the values of $x$ in the interval $x \\in [-90^\\circ; 90^\\circ]$ for which: $2\\cos 2x - 1 > 0$",
    memo=(
        "$$2\\cos 2x - 1 > 0$$\n"
        "$$\\cos 2x > \\frac{1}{2}$$\n"
        "$$-\\cos 2x < -\\frac{1}{2}$$\n"
        "$$g(x) < -\\frac{1}{2}$$\n\n"
        "Critical values where $-\\cos 2x = -\\frac{1}{2} \\implies \\cos 2x = \\frac{1}{2}$:\n"
        "$$2x = \\pm 60^\\circ \\implies x = \\pm 30^\\circ$$\n\n"
        "From the graph of $g$ on $[-90^\\circ; 90^\\circ]$, $g(x) < -\\frac{1}{2}$ when:\n"
        "$$x \\in (-30^\\circ; 30^\\circ) \\quad \\text{OR/OF} \\quad -30^\\circ < x < 30^\\circ$$\n\n"
        "* $\\checkmark \\cos 2x > \\frac{1}{2}$\n"
        "* $\\checkmark -\\cos 2x < -\\frac{1}{2}$\n"
        "* $\\checkmark x = \\pm 30^\\circ$\n"
        "* $\\checkmark x \\in (-30^\\circ; 30^\\circ)$"
    ),
    final_answer="-30^\\circ < x < 30^\\circ",
    needs_review=False
)

# ==============================================================================
# QUESTION 7 [8 marks]
# ==============================================================================

P_Q7 = (
    "In the diagram, $\\text{A}$, $\\text{B}$ and $\\text{C}$ are points in the same horizontal plane. "
    "$\\text{D}$ is a point directly above $\\text{C}$, that is $\\text{DC} \\perp \\text{AC}$ and $\\text{DC} \\perp \\text{BC}$. "
    "It is given that $\\text{A\\hat{C}B} = 100^\\circ$, $\\text{C\\hat{A}D} = 30^\\circ$, $\\text{AD} = 20\\text{ units}$ and $\\text{BC} = 8\\text{ units}$.\n\n"
    "[DIAGRAM: 3D perspective drawing showing shaded triangle $ABC$ on a horizontal plane with $A\\hat{C}B = 100^\\circ$ and side $BC = 8\\text{ units}$. "
    "A vertical pole $DC$ is directly above $C$, forming right angles with horizontal lines $AC$ and $BC$ ($D\\hat{C}A = 90^\\circ$ and $D\\hat{C}B = 90^\\circ$). "
    "An inclined segment $AD = 20\\text{ units}$ makes an angle $C\\hat{A}D = 30^\\circ$ with the horizontal line $AC$. "
    "Segment $BD$ is drawn connecting $B$ and $D$.]"
)

add_item(
    question_ref="7.1.1",
    marks=2,
    topic="3D Trigonometry - Right-Angled Triangle",
    passage=P_Q7,
    question="Calculate the length of $\\text{AC}$.",
    memo=(
        "In $\\Delta ACD$, $\\text{A\\hat{C}D} = 90^\\circ$:\n"
        "$$\\frac{AC}{AD} = \\cos 30^\\circ$$\n"
        "$$AC = 20\\cos 30^\\circ = 20\\left(\\frac{\\sqrt{3}}{2}\\right) = 10\\sqrt{3} \\approx 17{,}32\\text{ units}$$\n\n"
        "**OR/OF**\n"
        "$$\\frac{AC}{\\sin 60^\\circ} = \\frac{20}{\\sin 90^\\circ} \\implies AC = 20\\sin 60^\\circ \\approx 17{,}32\\text{ units}$$\n\n"
        "* $\\checkmark \\text{trig ratio: } \\frac{AC}{20} = \\cos 30^\\circ$\n"
        "* $\\checkmark \\text{answer: } 17{,}32\\text{ units}$"
    ),
    final_answer="17.32",
    needs_review=False
)

add_item(
    question_ref="7.1.2",
    marks=3,
    topic="3D Trigonometry - Cosine Rule",
    passage=P_Q7,
    question="Calculate the length of $\\text{AB}$.",
    memo=(
        "In $\\Delta ABC$, applying the cosine rule:\n"
        "$$AB^2 = AC^2 + BC^2 - 2(AC)(BC)\\cos \\text{A\\hat{C}B}$$\n"
        "$$AB^2 = (10\\sqrt{3})^2 + 8^2 - 2(10\\sqrt{3})(8)\\cos 100^\\circ$$\n"
        "$$AB^2 = 300 + 64 - 160\\sqrt{3}\\cos 100^\\circ$$\n"
        "$$AB^2 = 364 - (-48{,}123\\dots) \\approx 412{,}123\\dots$$\n"
        "$$AB \\approx 20{,}30\\text{ units}$$\n\n"
        "* $\\checkmark \\text{cosine formula}$\n"
        "* $\\checkmark \\text{substitution into cosine formula}$\n"
        "* $\\checkmark \\text{answer: } 20{,}30\\text{ units}$"
    ),
    final_answer="20.30",
    needs_review=False
)

add_item(
    question_ref="7.2",
    marks=3,
    topic="3D Trigonometry - Sine Rule",
    passage=P_Q7,
    question="If it is further given that $\\text{A\\hat{B}D} = 73{,}4^\\circ$, calculate the size of $\\text{A\\hat{D}B}$.",
    memo=(
        "In $\\Delta ABD$, applying the sine rule:\n"
        "$$\\frac{\\sin \\text{A\\hat{D}B}}{AB} = \\frac{\\sin \\text{A\\hat{B}D}}{AD}$$\n"
        "$$\\frac{\\sin \\text{A\\hat{D}B}}{20{,}30} = \\frac{\\sin 73{,}4^\\circ}{20}$$\n"
        "$$\\sin \\text{A\\hat{D}B} = \\frac{20{,}30\\sin 73{,}4^\\circ}{20}$$\n"
        "$$\\sin \\text{A\\hat{D}B} = \\frac{20{,}30(0{,}95832\\dots)}{20} \\approx 0{,}9727$$\n"
        "$$\\text{A\\hat{D}B} \\approx 76{,}58^\\circ$$\n\n"
        "* $\\checkmark \\text{sine formula in } \\Delta ABD$\n"
        "* $\\checkmark \\text{substitution into sine formula}$\n"
        "* $\\checkmark \\text{answer: } 76{,}58^\\circ$"
    ),
    final_answer="76.58^\\circ",
    needs_review=False
)

# ==============================================================================
# QUESTION 8 [15 marks]
# ==============================================================================

P_Q8_1 = (
    "In the diagram, $\\text{O}$ is the centre of the circle. $\\text{K}$, $\\text{T}$ and $\\text{L}$ are points on the circle. "
    "$\\text{KT}$, $\\text{TL}$, $\\text{KL}$, $\\text{OK}$ and $\\text{OT}$ are drawn. $\\text{OT}$ intersects $\\text{KL}$ at $\\text{M}$. "
    "$\\text{ST}$ is a tangent to the circle at $\\text{T}$. $\\text{S\\hat{T}K} = 36^\\circ$ and $\\text{O\\hat{K}L} = 18^\\circ$.\n\n"
    "[DIAGRAM: Circle with centre $O$. Points $K, T, L$ lie on the circumference. $ST$ is a tangent to the circle at $T$, "
    "forming angle $S\\hat{T}K = \\hat{T}_1 = 36^\\circ$ with chord $KT$. Chords $KT, TL, KL$ form inscribed triangle $\\Delta KTL$. "
    "Radii $OK$ and $OT$ are drawn ($OK = OT$). Radius $OT$ intersects chord $KL$ at $M$. "
    "Angles at $T$: $\\hat{T}_1 = 36^\\circ$, $\\hat{T}_2 = O\\hat{T}K$, $\\hat{T}_3 = O\\hat{T}L$. "
    "Angles at $K$: $\\hat{K}_1 = T\\hat{K}L$, $\\hat{K}_2 = O\\hat{K}L = 18^\\circ$. Angle $\\hat{L} = K\\hat{L}T$.]"
)

add_item(
    question_ref="8.1.1(a)",
    marks=2,
    topic="Euclidean Geometry - Tangent Perpendicular to Radius",
    passage=P_Q8_1,
    question="Determine, giving reasons, the size of $\\hat{\\text{T}}_2$.",
    memo=(
        "$$\\text{S\\hat{T}O} = 90^\\circ \\quad [\\text{tan } \\perp \\text{ radius / rad}]$$\n"
        "$$\\hat{T}_1 + \\hat{T}_2 = 90^\\circ$$\n"
        "$$36^\\circ + \\hat{T}_2 = 90^\\circ$$\n"
        "$$\\hat{T}_2 = 54^\\circ$$\n\n"
        "* $\\checkmark \\text{S: } \\hat{T}_2 = 54^\\circ$\n"
        "* $\\checkmark \\text{R: tan } \\perp \\text{ rad}$"
    ),
    final_answer="54^\\circ",
    needs_review=False
)

add_item(
    question_ref="8.1.1(b)",
    marks=2,
    topic="Euclidean Geometry - Tan-Chord Theorem",
    passage=P_Q8_1,
    question="Determine, giving reasons, the size of $\\hat{\\text{L}}$.",
    memo=(
        "$$\\hat{L} = \\text{S\\hat{T}K} = 36^\\circ \\quad [\\text{tan-chord theorem}]$$\n\n"
        "* $\\checkmark \\text{S: } \\hat{L} = 36^\\circ$\n"
        "* $\\checkmark \\text{R: tan-chord theorem}$"
    ),
    final_answer="36^\\circ",
    needs_review=False
)

add_item(
    question_ref="8.1.1(c)",
    marks=2,
    topic="Euclidean Geometry - Angle at Centre",
    passage=P_Q8_1,
    question="Determine, giving reasons, the size of $\\text{K\\hat{O}T}$.",
    memo=(
        "$$\\text{K\\hat{O}T} = 2\\hat{L} = 2(36^\\circ) = 72^\\circ \\quad [\\angle \\text{ at centre} = 2 \\times \\angle \\text{ at circumference}]$$\n\n"
        "**OR/OF**\n"
        "In $\\Delta OKT$, $OK = OT$ [radii]:\n"
        "$$\\text{O\\hat{K}T} = \\hat{T}_2 = 54^\\circ \\quad [\\angle\\text{'s opp equal sides}]$$\n"
        "$$\\text{K\\hat{O}T} = 180^\\circ - (54^\\circ + 54^\\circ) = 72^\\circ \\quad [\\text{sum of int } \\angle\\text{'s of } \\Delta]$$\n\n"
        "* $\\checkmark \\text{S: } \\text{K\\hat{O}T} = 72^\\circ$\n"
        "* $\\checkmark \\text{R: } \\angle \\text{ at centre} = 2 \\times \\angle \\text{ at circumference}$\n"
        "(2)\n\n"
        "**OR/OF**\n"
        "* $\\checkmark \\text{S/R: } \\text{O\\hat{K}T} = 54^\\circ$\n"
        "* $\\checkmark \\text{S: } \\text{K\\hat{O}T} = 72^\\circ$\n"
        "(2)"
    ),
    final_answer="72^\\circ",
    needs_review=False
)

add_item(
    question_ref="8.1.2",
    marks=3,
    topic="Euclidean Geometry - Line from Centre Perpendicular to Chord",
    passage=P_Q8_1,
    question="Prove, giving reasons, that $\\text{KM} = \\text{ML}$.",
    memo=(
        "**Method 1:**\n"
        "In $\\Delta OKM$:\n"
        "$$\\text{K\\hat{M}O} = 180^\\circ - (\\text{O\\hat{K}M} + \\text{K\\hat{O}M})$$\n"
        "$$\\text{K\\hat{M}O} = 180^\\circ - (18^\\circ + 72^\\circ) = 90^\\circ \\quad [\\text{sum of int } \\angle\\text{'s of } \\Delta]$$\n"
        "$$\\therefore KM = ML \\quad [\\text{line from centre } \\perp \\text{ to chord bisects chord}]$$\n\n"
        "**OR/OF Method 2:**\n"
        "$$\\text{O\\hat{K}T} = \\hat{T}_2 = 54^\\circ \\quad [\\angle\\text{'s opp equal sides}]$$\n"
        "$$\\hat{K}_1 = 54^\\circ - 18^\\circ = 36^\\circ$$\n"
        "In $\\Delta TKM$:\n"
        "$$\\text{T\\hat{M}K} = 180^\\circ - (36^\\circ + 54^\\circ) = 90^\\circ \\quad [\\text{sum of int } \\angle\\text{'s of } \\Delta]$$\n"
        "$$\\therefore KM = ML \\quad [\\text{line from centre } \\perp \\text{ to chord bisects chord}]$$\n\n"
        "* $\\checkmark \\text{S: } \\text{K\\hat{M}O} = 90^\\circ \\text{ or } \\text{T\\hat{M}K} = 90^\\circ$\n"
        "* $\\checkmark \\text{S: } OM \\perp KL$\n"
        "* $\\checkmark \\text{R: line from centre } \\perp \\text{ to chord}$"
    ),
    final_answer="",
    needs_review=False
)

P_Q8_2 = (
    "In the diagram, $\\Delta\\text{RDS}$ is drawn. $\\text{A}$, $\\text{B}$ and $\\text{C}$ are points on $\\text{RD}$, "
    "$\\text{RS}$ and $\\text{DS}$ respectively such that $\\text{AB} \\parallel \\text{DS}$ and $\\text{RB} : \\text{BS} = 5 : 3$. "
    "$\\text{DC} = 20\\text{ units}$ and $\\text{CS} = 12\\text{ units}$.\n\n"
    "[DIAGRAM: Triangle $RDS$ with apex $R$ at the top, $D$ at bottom-left, $S$ at bottom-right. "
    "$A$ lies on $RD$, $B$ lies on $RS$, with line segment $AB$ parallel to base $DS$ (indicated by arrows on $AB$ and $DS$). "
    "$C$ lies on $DS$ such that $DC = 20\\text{ units}$ and $CS = 12\\text{ units}$. "
    "Segment $BC$ is drawn. The ratio $RB : BS = 5 : 3$.]"
)

add_item(
    question_ref="8.2.1",
    marks=3,
    topic="Euclidean Geometry - Proportionality Converse",
    passage=P_Q8_2,
    question="Prove, giving reasons, that $\\text{BC} \\parallel \\text{AD}$.",
    memo=(
        "$$\\frac{DC}{CS} = \\frac{20}{12} = \\frac{5}{3}$$\n"
        "It is given that:\n"
        "$$\\frac{RB}{BS} = \\frac{5}{3}$$\n"
        "$$\\therefore \\frac{DC}{CS} = \\frac{RB}{BS}$$\n"
        "$$\\therefore BC \\parallel DR \\quad [\\text{converse prop theorem OR sides in the same proportion}]$$\n"
        "Since $A$ lies on the line segment $RD$:\n"
        "$$\\therefore BC \\parallel AD$$\n\n"
        "* $\\checkmark \\text{S: } \\frac{DC}{CS} = \\frac{5}{3}$\n"
        "* $\\checkmark \\text{S: } \\frac{DC}{CS} = \\frac{RB}{BS}$\n"
        "* $\\checkmark \\text{R: converse prop theorem / sides in same proportion}$"
    ),
    final_answer="",
    needs_review=False
)

add_item(
    question_ref="8.2.2",
    marks=3,
    topic="Euclidean Geometry - Proportionality Theorem and Parallelogram",
    passage=P_Q8_2,
    question="If it is further given that $\\text{RD} = 48\\text{ units}$, calculate, giving reasons, the value of the ratio $\\text{AD} : \\text{AB}$.",
    memo=(
        "In $\\Delta RDS$, since $AB \\parallel DS$:\n"
        "$$\\frac{AR}{AD} = \\frac{RB}{BS} = \\frac{5}{3} \\quad [\\text{prop theorem, } AB \\parallel DS]$$\n"
        "Since $RD = 48\\text{ units}$ and $AR = RD - AD = 48 - AD$:\n"
        "$$\\frac{48 - AD}{AD} = \\frac{5}{3}$$\n"
        "$$5AD = 3(48 - AD)$$\n"
        "$$5AD = 144 - 3AD$$\n"
        "$$8AD = 144 \\implies AD = 18\\text{ units}$$\n\n"
        "Since $AB \\parallel DS$ ($AB \\parallel CD$) and $BC \\parallel AD$ (proved in 8.2.1):\n"
        "Quadrilateral $ABCD$ is a parallelogram [both pairs of opposite sides $\\parallel$].\n"
        "$$AB = DC = 20\\text{ units} \\quad [\\text{opp sides of parm}]$$\n\n"
        "Therefore:\n"
        "$$\\text{AD} : \\text{AB} = 18 : 20 = 9 : 10$$\n\n"
        "**OR/OF**\n"
        "$$\\frac{AR}{RD} = \\frac{RB}{RS} = \\frac{5}{8} \\quad [\\text{prop theorem, } AB \\parallel DS]$$\n"
        "$$\\frac{AR}{48} = \\frac{5}{8} \\implies AR = 30\\text{ units}$$\n"
        "$$AD = 48 - 30 = 18\\text{ units}$$\n"
        "$$AB = DC = 20\\text{ units} \\quad [\\text{opp sides of parm}]$$\n"
        "$$\\therefore \\text{AD} : \\text{AB} = 18 : 20 = 9 : 10$$\n\n"
        "* $\\checkmark \\frac{AR}{AD} = \\frac{5}{3} \\text{ (or } \\frac{AR}{RD} = \\frac{5}{8}\\text{)}$\n"
        "* $\\checkmark AD = 18$\n"
        "* $\\checkmark \\text{ratio } 9 : 10$"
    ),
    final_answer="9 : 10",
    needs_review=False
)

# ==============================================================================
# QUESTION 9 [9 marks]
# ==============================================================================

P_Q9_1 = (
    "In the diagram, $\\text{O}$ is the centre of the circle. $\\text{ABCD}$ is a cyclic quadrilateral.\n\n"
    "[DIAGRAM: Circle with centre $O$. Cyclic quadrilateral $ABCD$ inscribed in the circle with vertices "
    "$A$ on the left, $B$ at the top, $C$ on the right, and $D$ at the bottom. Centre $O$ is inside the quadrilateral.]"
)

add_item(
    question_ref="9.1",
    marks=5,
    topic="Euclidean Geometry - Cyclic Quadrilateral Theorem Proof",
    passage=P_Q9_1,
    question="Use the diagram in the ANSWER BOOK to prove the theorem which states that the opposite angles of a cyclic quadrilateral are supplementary, that is prove that $\\hat{\\text{B}} + \\hat{\\text{D}} = 180^\\circ$.",
    memo=(
        "**Construction:**\n"
        "Draw radii $OA$ and $OC$. Let the angle at centre subtended by minor arc $ADC$ be $\\hat{O}_1$ "
        "and reflex angle subtended by major arc $ABC$ be $\\hat{O}_2$.\n\n"
        "**Proof:**\n"
        "$$\\hat{O}_1 = 2\\hat{B} \\quad [\\angle \\text{ at centre} = 2 \\times \\angle \\text{ at circumference}]$$\n"
        "$$\\hat{O}_2 = 2\\hat{D} \\quad [\\angle \\text{ at centre} = 2 \\times \\angle \\text{ at circumference}]$$\n"
        "$$\\hat{O}_1 + \\hat{O}_2 = 360^\\circ \\quad [\\angle\\text{'s round a point / revolution}]$$\n"
        "$$2\\hat{B} + 2\\hat{D} = 360^\\circ$$\n"
        "$$2(\\hat{B} + \\hat{D}) = 360^\\circ$$\n"
        "$$\\therefore \\hat{B} + \\hat{D} = 180^\\circ$$\n\n"
        "* $\\checkmark \\text{Construction: Draw radii } OA \\text{ and } OC$\n"
        "* $\\checkmark \\text{S } \\checkmark \\text{R: } \\hat{O}_1 = 2\\hat{B} \\text{ [}\\angle \\text{ at centre} = 2 \\times \\angle \\text{ at circumference]}$\n"
        "* $\\checkmark \\text{S/R: } \\hat{O}_2 = 2\\hat{D} \\text{ and } \\hat{O}_1 + \\hat{O}_2 = 360^\\circ$\n"
        "* $\\checkmark \\text{S: } \\hat{B} + \\hat{D} = 180^\\circ$"
    ),
    final_answer="",
    needs_review=False
)

P_Q9_2 = (
    "In the diagram, $\\text{DEFG}$ is a cyclic quadrilateral such that $\\text{EF} \\parallel \\text{DG}$. "
    "$\\text{H}$ is another point on the circle such that $\\text{DH} \\parallel \\text{FG}$. "
    "Chord $\\text{EH}$ is drawn. Let $\\hat{\\text{D}}_1 = x$.\n\n"
    "[DIAGRAM: Circle containing inscribed cyclic quadrilateral $DEFG$ and point $H$ on the circumference. "
    "Chord $EF$ is parallel to chord $DG$ ($EF \\parallel DG$, shown with single arrows). "
    "Chord $DH$ is parallel to chord $FG$ ($DH \\parallel FG$, shown with double arrows). "
    "Chord $EH$ is drawn. Angles at $D$: $\\hat{D}_1$ (between $DE$ and $DG$, given as $x$) and $\\hat{D}_2$ (between $DG$ and $DH$). "
    "Angles at $E$: $\\hat{E}_1$ and $\\hat{E}_2$. Angle $\\hat{G} = D\\hat{G}F$.]"
)

add_item(
    question_ref="9.2",
    marks=4,
    topic="Euclidean Geometry - Cyclic Quad and Parallel Lines",
    passage=P_Q9_2,
    question="Prove, giving reasons, that $\\hat{\\text{D}}_1 = \\hat{\\text{D}}_2$.",
    memo=(
        "In cyclic quadrilateral $DEFG$:\n"
        "$$\\text{E\\hat{F}G} = 180^\\circ - \\hat{D}_1 \\quad [\\text{opp } \\angle\\text{'s of cyclic quad}]$$\n"
        "$$\\therefore \\text{E\\hat{F}G} = 180^\\circ - x$$\n\n"
        "Since $EF \\parallel DG$:\n"
        "$$\\text{E\\hat{F}G} = 180^\\circ - \\hat{G} \\quad [\\text{co-int } \\angle\\text{'s; } EF \\parallel DG]$$\n"
        "$$\\hat{G} = 180^\\circ - \\text{E\\hat{F}G} = 180^\\circ - (180^\\circ - x) = x$$\n\n"
        "Since $DH \\parallel FG$:\n"
        "$$\\hat{D}_2 = \\hat{G} \\quad [\\text{alt } \\angle\\text{'s; } DH \\parallel FG]$$\n"
        "$$\\therefore \\hat{D}_2 = x$$\n\n"
        "Therefore:\n"
        "$$\\hat{D}_1 = \\hat{D}_2 = x$$\n\n"
        "* $\\checkmark \\text{S } \\checkmark \\text{R: } \\text{E\\hat{F}G} = 180^\\circ - \\hat{D}_1 \\text{ [opp } \\angle\\text{'s of cyclic quad]}$\n"
        "* $\\checkmark \\text{S/R: } \\hat{G} = x \\text{ [co-int } \\angle\\text{'s; } EF \\parallel DG]$\n"
        "* $\\checkmark \\text{S/R: } \\hat{D}_2 = \\hat{G} = x \\text{ [alt } \\angle\\text{'s; } DH \\parallel FG]$"
    ),
    final_answer="",
    needs_review=False
)

# ==============================================================================
# QUESTION 10 [17 marks]
# ==============================================================================

P_Q10 = (
    "In the diagram, $\\text{TR}$ is a diameter of the circle. $\\text{PRKT}$ is a cyclic quadrilateral. "
    "Chords $\\text{TP}$ and $\\text{KR}$ are produced to intersect at $\\text{S}$. "
    "Chord $\\text{PK}$ is drawn such that $\\text{PK} = \\text{TK}$.\n\n"
    "[DIAGRAM: Circle with diameter $TR$. Points on the circle are $T$ (bottom-left), $P$ (upper-left), "
    "$R$ (middle-right), and $K$ (bottom-right). Cyclic quadrilateral $PRKT$ is inscribed in the circle. "
    "Chord $TP$ is produced beyond $P$, and chord $KR$ is produced beyond $R$ to meet at external apex $S$ (top vertex). "
    "Chord $PK$ is drawn, with tick marks indicating $PK = TK$. "
    "Collinear points along lines: $T-P-S$ and $K-R-S$. "
    "Angles at $P$: $\\hat{P}_1 = T\\hat{P}K$, $\\hat{P}_2 = K\\hat{P}R$, $\\hat{P}_3 = S\\hat{P}R$. "
    "Angles at $R$: $\\hat{R}_1 = S\\hat{R}P$, $\\hat{R}_2 = P\\hat{R}T$, $\\hat{R}_3 = T\\hat{R}K$. "
    "Angles at $T$: $\\hat{T}_1 = P\\hat{T}R$, $\\hat{T}_2 = R\\hat{T}K$. "
    "Angles at $K$: $\\hat{K}_1 = T\\hat{K}R$, $\\hat{K}_2 = P\\hat{K}R$.]"
)

add_item(
    question_ref="10.1.1",
    marks=4,
    topic="Euclidean Geometry - Diameter Converse Proof",
    passage=P_Q10,
    question="Prove, giving reasons, that $\\text{SR}$ is a diameter of a circle passing through points $\\text{S}$, $\\text{P}$ and $\\text{R}$.",
    memo=(
        "$$\\text{T\\hat{P}R} = 90^\\circ \\quad [\\angle \\text{ in semi-circle, } TR \\text{ is diameter}]$$\n"
        "$$\\text{S\\hat{P}R} = 180^\\circ - 90^\\circ = 90^\\circ \\quad [\\angle\\text{'s on a straight line, } TPS]$$\n"
        "$$\\therefore SR \\text{ is a diameter of the circle passing through } S, P \\text{ and } R \\quad [\\text{converse } \\angle \\text{ in semi-circle}]$$\n\n"
        "**OR/OF**\n"
        "$$\\text{T\\hat{K}R} = 90^\\circ \\quad [\\angle \\text{ in semi-circle}]$$\n"
        "$$\\text{S\\hat{P}R} = \\text{T\\hat{K}R} = 90^\\circ \\quad [\\text{ext } \\angle \\text{ of cyclic quad } PRKT]$$\n"
        "$$\\therefore SR \\text{ is a diameter of the circle passing through } S, P \\text{ and } R \\quad [\\text{converse } \\angle \\text{ in semi-circle / chord subtends a right angle}]$$\n\n"
        "* $\\checkmark \\text{S } \\checkmark \\text{R: } \\text{T\\hat{P}R} = 90^\\circ \\text{ [}\\angle \\text{ in semi-circle]}$\n"
        "* $\\checkmark \\text{S: } \\text{S\\hat{P}R} = 90^\\circ$\n"
        "* $\\checkmark \\text{R: converse } \\angle \\text{ in semi-circle}$\n"
        "(4)\n\n"
        "**OR/OF**\n"
        "* $\\checkmark \\text{S } \\checkmark \\text{R: } \\text{T\\hat{K}R} = 90^\\circ \\text{ [}\\angle \\text{ in semi-circle]}$\n"
        "* $\\checkmark \\text{S: } \\text{S\\hat{P}R} = 90^\\circ$\n"
        "* $\\checkmark \\text{R: converse } \\angle \\text{ in semi-circle / chord subtends a right angle}$\n"
        "(4)"
    ),
    final_answer="",
    needs_review=False
)

add_item(
    question_ref="10.1.2",
    marks=5,
    topic="Euclidean Geometry - Angle Equality Proof",
    passage=P_Q10,
    question="Prove, giving reasons, that $\\hat{\\text{S}} = \\hat{\\text{P}}_2$.",
    memo=(
        "$$\\hat{R}_1 = \\text{P\\hat{T}K} \\quad [\\text{ext } \\angle \\text{ of cyclic quad } PRKT]$$\n"
        "In $\\Delta PTK$, $PK = TK$ [given]:\n"
        "$$\\hat{P}_1 = \\text{P\\hat{T}K} = \\hat{R}_1 \\quad [\\angle\\text{'s opp equal sides}]$$\n\n"
        "In $\\Delta SPR$, line $TPS$ is produced:\n"
        "$$\\hat{S} + \\hat{R}_1 = \\hat{P}_1 + \\hat{P}_2 \\quad [\\text{ext } \\angle \\text{ of } \\Delta SPR]$$\n"
        "$$\\text{Since } \\hat{P}_1 = \\hat{R}_1:$$\n"
        "$$\\therefore \\hat{S} = \\hat{P}_2$$\n\n"
        "* $\\checkmark \\text{S } \\checkmark \\text{R: } \\hat{R}_1 = \\text{P\\hat{T}K} \\text{ [ext } \\angle \\text{ of cyclic quad]}$\n"
        "* $\\checkmark \\text{S/R: } \\hat{P}_1 = \\text{P\\hat{T}K} = \\hat{R}_1 \\text{ [}\\angle\\text{s opp equal sides]}$\n"
        "* $\\checkmark \\text{S } \\checkmark \\text{R: } \\hat{S} + \\hat{R}_1 = \\hat{P}_1 + \\hat{P}_2 \\text{ [ext } \\angle \\text{ of } \\Delta] \\text{ and } \\hat{S} = \\hat{P}_2$"
    ),
    final_answer="",
    needs_review=False
)

add_item(
    question_ref="10.1.3",
    marks=3,
    topic="Euclidean Geometry - Similar Triangles",
    passage=P_Q10,
    question="Prove, giving reasons, that $\\Delta\\text{SPK} \\parallel\\parallel\\parallel \\Delta\\text{PRK}$.",
    memo=(
        "In $\\Delta SPK$ and $\\Delta PRK$:\n"
        "1. $\\hat{S} = \\hat{P}_2 \\quad [\\text{proved in 10.1.2}]$\n"
        "2. $\\hat{K}_2 = \\hat{K}_2 \\quad [\\text{common}]$\n"
        "3. $\\text{S\\hat{P}K} = \\text{P\\hat{R}K} \\quad [\\text{sum of } \\angle\\text{'s in } \\Delta]$\n"
        "$$\\therefore \\Delta SPK \\parallel\\parallel\\parallel \\Delta PRK \\quad [\\angle, \\angle, \\angle]$$\n\n"
        "**OR/OF**\n"
        "In $\\Delta SPK$ and $\\Delta PRK$:\n"
        "1. $\\hat{S} = \\hat{P}_2 \\quad [\\text{proved in 10.1.2}]$\n"
        "2. $\\hat{K}_2 = \\hat{K}_2 \\quad [\\text{common}]$\n"
        "$$\\therefore \\Delta SPK \\parallel\\parallel\\parallel \\Delta PRK \\quad [\\angle, \\angle, \\angle]$$\n\n"
        "* $\\checkmark \\text{S: } \\hat{S} = \\hat{P}_2 \\text{ [proved]}$\n"
        "* $\\checkmark \\text{S: } \\hat{K}_2 = \\hat{K}_2 \\text{ [common]}$\n"
        "* $\\checkmark \\text{S/R: } \\Delta SPK \\parallel\\parallel\\parallel \\Delta PRK \\text{ [}\\angle, \\angle, \\angle]$"
    ),
    final_answer="",
    needs_review=False
)

add_item(
    question_ref="10.2",
    marks=5,
    topic="Euclidean Geometry - Similar Triangles and Pythagoras Proof",
    passage=P_Q10,
    question="If it is further given that $\\text{SR} = \\text{RK}$, prove that $\\text{ST} = \\sqrt{6}\\text{RK}$.",
    memo=(
        "From 10.1.3, $\\Delta SPK \\parallel\\parallel\\parallel \\Delta PRK$:\n"
        "$$\\frac{PK}{RK} = \\frac{SK}{PK} \\quad [\\Delta SPK \\parallel\\parallel\\parallel \\Delta PRK]$$\n"
        "$$PK^2 = SK \\cdot RK$$\n\n"
        "In $\\Delta TKS$, $TR$ is the diameter of the circle, so $\\text{T\\hat{K}R} = 90^\\circ$ [$\\angle$ in semi-circle].\n"
        "Since $SKR$ is a straight line, $\\text{T\\hat{K}S} = 90^\\circ$.\n"
        "By Pythagoras in right-angled $\\Delta TKS$:\n"
        "$$ST^2 = SK^2 + TK^2 \\quad [\\text{Pythagoras}]$$\n\n"
        "Since $TK = PK$ [given]:\n"
        "$$ST^2 = SK^2 + PK^2$$\n"
        "Substitute $PK^2 = SK \\cdot RK$:\n"
        "$$ST^2 = SK^2 + SK \\cdot RK$$\n\n"
        "Points $S, R, K$ lie on a straight line with $R$ between $S$ and $K$. Given $SR = RK$:\n"
        "$$SK = SR + RK = RK + RK = 2RK$$\n\n"
        "Substitute $SK = 2RK$:\n"
        "$$ST^2 = (2RK)^2 + (2RK)(RK)$$\n"
        "$$ST^2 = 4RK^2 + 2RK^2 = 6RK^2$$\n"
        "$$\\therefore ST = \\sqrt{6}RK$$\n\n"
        "* $\\checkmark \\text{S: } \\frac{PK}{RK} = \\frac{SK}{PK} \\implies PK^2 = SK \\cdot RK$\n"
        "* $\\checkmark \\text{S: } ST^2 = SK^2 + TK^2 \\text{ [Pythagoras]}$\n"
        "* $\\checkmark PK^2 = SK \\cdot RK$\n"
        "* $\\checkmark SK = 2RK$\n"
        "* $\\checkmark ST^2 = 6RK^2 \\implies ST = \\sqrt{6}RK$"
    ),
    final_answer="",
    needs_review=False
)

# ==============================================================================
# VALIDATION AND EXPORT
# ==============================================================================

total_items = len(items)
total_marks = sum(item["marks"] for item in items)
needs_review_count = sum(1 for item in items if item["needs_review"])

print(f"Total items: {total_items}")
print(f"Total marks: {total_marks}")
print(f"Needs review: {needs_review_count}")

assert total_marks == 150, f"Expected 150 marks, got {total_marks}"

# Validate KaTeX syntax: check matching $ and $$ delimiters
latex_issues = []
for item in items:
    for field in ["question", "memo", "passage"]:
        text = item[field]
        # check $$ pairs
        double_dollars = text.count("$$")
        if double_dollars % 2 != 0:
            latex_issues.append(f"{item['item_id']} {field}: unmatched $$")
        # remove $$ blocks before checking inline $
        clean_text = re.sub(r"\$\$.*?\$\$", "", text, flags=re.DOTALL)
        single_dollars = clean_text.count("$")
        if single_dollars % 2 != 0:
            latex_issues.append(f"{item['item_id']} {field}: unmatched $")

if latex_issues:
    print(f"LaTeX issues found ({len(latex_issues)}):")
    for issue in latex_issues:
        print("  -", issue)
    raise ValueError("KaTeX delimiter mismatch!")
else:
    print("KaTeX delimiter check: PASS (All matching)")

# Target output files
out_dir_subject = os.path.join("sa-tutor-kit", "sa-tutor-kit", "workspace", "items", "mathematics")
os.makedirs(out_dir_subject, exist_ok=True)
out_file_subject = os.path.join(out_dir_subject, f"{SOURCE_ID}.jsonl")

out_dir_root = os.path.join("sa-tutor-kit", "sa-tutor-kit", "workspace", "items")
os.makedirs(out_dir_root, exist_ok=True)
out_file_root = os.path.join(out_dir_root, f"{SOURCE_ID}.jsonl")

# Write subject path
with open(out_file_subject, "w", encoding="utf-8") as f:
    for item in items:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

# Write root mirror path
with open(out_file_root, "w", encoding="utf-8") as f:
    for item in items:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"Successfully written to:\n  1. {out_file_subject}\n  2. {out_file_root}")
