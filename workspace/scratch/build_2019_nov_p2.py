import json
import os
import re

SOURCE_ID = "dbe-mathematics-g12-p2-2019-nov"
PAIR_SOURCE_ID = "dbe-mathematics-g12-p2-2019-nov-memo"
SUBJECT = "mathematics"
GRADE = 12
LANGUAGE = "en"
TRACK = "core_maths"
LICENCE = "DBE copyright - check terms"
ATTRIBUTION = "Department of Basic Education"

items = []

def add_item(qref, marks, topic, passage, question, memo, final_answer, kind="question"):
    item = {
        "item_id": f"{SOURCE_ID}-{qref}",
        "source_id": SOURCE_ID,
        "pair_source_id": PAIR_SOURCE_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": kind,
        "question_ref": qref,
        "marks": marks,
        "topic": topic,
        "passage": passage,
        "question": question,
        "memo": memo,
        "final_answer": final_answer,
        "needs_review": False,
        "licence": LICENCE,
        "attribution": ATTRIBUTION
    }
    items.append(item)

# ==========================================
# QUESTION 1: Statistics - Bivariate Data
# ==========================================
p_q1 = """The table below shows the monthly income (in rands) of 6 different people and the amount (in rands) that each person spends on the monthly repayment of a motor vehicle.

| MONTHLY INCOME (IN RANDS) | 9 000 | 13 500 | 15 000 | 16 500 | 17 000 | 20 000 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| MONTHLY REPAYMENT (IN RANDS) | 2 000 | 3 000 | 3 500 | 5 200 | 5 500 | 6 000 |"""

add_item(
    qref="1.1",
    marks=3,
    topic="Statistics - Bivariate Data & Regression",
    passage=p_q1,
    question="Determine the equation of the least squares regression line for the data.",
    memo="""Using a calculator:
$$a = -1946{,}875 \approx -1946{,}88$$
$$b = 0{,}4057\dots \approx 0{,}41$$
$$\hat{y} = -1946{,}88 + 0{,}41x$$

* $\\checkmark a = -1946{,}88$
* $\\checkmark b = 0{,}41$
* $\\checkmark$ equation ($\hat{y} = -1946{,}88 + 0{,}41x$)""",
    final_answer="\\hat{y} = -1946{,}88 + 0{,}41x"
)

add_item(
    qref="1.2",
    marks=2,
    topic="Statistics - Bivariate Data & Regression",
    passage=p_q1,
    question="If a person earns R14 000 per month, predict the monthly repayment that the person could make towards a motor vehicle.",
    memo="""Using the regression equation:
$$\\hat{y} = -1946{,}88 + 0{,}41(14\\,000) \\approx \\text{R}3\\,793{,}12$$
OR using unrounded calculator values:
$$\\hat{y} \\approx \\text{R}3\\,727{,}16$$

* $\\checkmark$ substitution of $x = 14\\,000$
* $\\checkmark$ answer ($\\text{R}3\\,727{,}16$ or $\\text{R}3\\,793{,}12$)""",
    final_answer="\\text{R}3\\,727{,}16"
)

add_item(
    qref="1.3",
    marks=1,
    topic="Statistics - Bivariate Data & Regression",
    passage=p_q1,
    question="Determine the correlation coefficient between the monthly income and the monthly repayment of a motor vehicle.",
    memo="""$$r = 0{,}946\\dots \\approx 0{,}95$$

* $\\checkmark$ answer ($r = 0{,}95$)""",
    final_answer="0{,}95"
)

add_item(
    qref="1.4",
    marks=2,
    topic="Statistics - Bivariate Data & Regression",
    passage=p_q1,
    question="""A person who earns R18 000 per month has to decide whether to spend R9 000 as a monthly repayment of a motor vehicle, or not. If the above information is a true representation of the population data, which of the following would the person most likely decide on:

A: Spend R9 000 per month because there is a very strong positive correlation between the amount earned and the monthly repayment.
B: NOT to spend R9 000 per month because there is a very weak positive correlation between the amount earned and the monthly repayment.
C: Spend R9 000 per month because the point $(18\\,000; 9\\,000)$ lies very near to the least squares regression line.
D: NOT to spend R9 000 per month because the point $(18\\,000; 9\\,000)$ lies very far from the least squares regression line.""",
    memo="""Option D: NOT to spend R9 000 per month because the point $(18\\,000; 9\\,000)$ lies very far from the least squares regression line.

For $x = 18\\,000$, predicted repayment is $\\hat{y} \\approx \\text{R}5\\,433{,}12$, which is significantly less than $\\text{R}9\\,000$.

* $\\checkmark\\checkmark$ answer (Option D)""",
    final_answer="D",
    kind="multiple_choice"
)

# ==========================================
# QUESTION 2: Statistics - Grouped Data & Ogive
# ==========================================
p_q2 = """A survey was conducted among 100 people about the amount that they paid on a monthly basis for their cellphone contracts. The person carrying out the survey calculated the estimated mean to be R309 per month. Unfortunately, he lost some of the data thereafter. The partial results of the survey are shown in the frequency table below:

| AMOUNT PAID (IN RANDS) | FREQUENCY |
| :---: | :---: |
| $0 < x \\le 100$ | 7 |
| $100 < x \\le 200$ | 12 |
| $200 < x \\le 300$ | $a$ |
| $300 < x \\le 400$ | 35 |
| $400 < x \\le 500$ | $b$ |
| $500 < x \\le 600$ | 6 |"""

add_item(
    qref="2.1",
    marks=1,
    topic="Statistics - Grouped Data & Measures of Central Tendency",
    passage=p_q2,
    question="How many people paid R200 or less on their monthly cellphone contracts?",
    memo="""$$\\text{Number of people} = 7 + 12 = 19$$

* $\\checkmark$ answer ($19$)""",
    final_answer="19"
)

add_item(
    qref="2.2",
    marks=5,
    topic="Statistics - Grouped Data & Measures of Central Tendency",
    passage=p_q2,
    question="Use the information above to show that $a = 24$ and $b = 16$.",
    memo="""Total frequency:
$$7 + 12 + a + 35 + b + 6 = 100$$
$$a + b = 40 \\implies a = 40 - b$$

Using class midpoints ($50, 150, 250, 350, 450, 550$):
$$\\bar{x} = \\frac{\\sum f \\cdot m}{n} = 309$$
$$\\frac{7(50) + 12(150) + a(250) + 35(350) + b(450) + 6(550)}{100} = 309$$
$$\\frac{350 + 1\\,800 + 250(40 - b) + 12\\,250 + 450b + 3\\,300}{100} = 309$$
$$27\\,700 + 200b = 30\\,900$$
$$200b = 3\\,200 \\implies b = 16$$
$$a = 40 - 16 = 24$$

* $\\checkmark \\sum f = 100$
* $\\checkmark a = 40 - b$ (or $b = 40 - a$)
* $\\checkmark \\sum f \\cdot m$ expansion using midpoints
* $\\checkmark \\frac{\\sum f \\cdot m}{n} = 309$
* $\\checkmark 200b = 3\\,200 \\implies b = 16 \\text{ and } a = 24$""",
    final_answer="a = 24, b = 16"
)

add_item(
    qref="2.3",
    marks=1,
    topic="Statistics - Grouped Data & Measures of Central Tendency",
    passage=p_q2,
    question="Write down the modal class for the data.",
    memo="""The interval with the highest frequency ($35$) is:
$$300 < x \\le 400$$

* $\\checkmark$ answer ($300 < x \\le 400$)""",
    final_answer="300 < x \\le 400"
)

add_item(
    qref="2.4",
    marks=4,
    topic="Statistics - Ogive & Cumulative Frequency",
    passage=p_q2,
    question="On the grid provided in the ANSWER BOOK, draw an ogive (cumulative frequency graph) to represent the data.",
    memo="""Cumulative frequency values plotted at upper class limits:
* $(0; 0)$
* $(100; 7)$
* $(200; 19)$
* $(300; 19 + 24 = 43)$
* $(400; 43 + 35 = 78)$
* $(500; 78 + 16 = 94)$
* $(600; 94 + 6 = 100)$

* $\\checkmark$ grounded at $(0; 0)$
* $\\checkmark$ upper endpoint at $(600; 100)$
* $\\checkmark$ cumulative frequencies correctly plotted at upper limits
* $\\checkmark$ smooth S-shaped curve""",
    final_answer="Smooth S-curve grounded at $(0; 0)$, passing through $(100; 7), (200; 19), (300; 43), (400; 78), (500; 94)$, and ending at $(600; 100)$."
)

add_item(
    qref="2.5",
    marks=2,
    topic="Statistics - Ogive & Cumulative Frequency",
    passage=p_q2,
    question="Determine how many people paid more than R420 per month for their cellphone contracts.",
    memo="""From the ogive at $x = 420$:
Cumulative frequency $\\approx 82$ (accept $80 - 84$ people).
Number of people paying more than $\\text{R}420 = 100 - 82 = 18$ people (accept $16 - 20$ people).

* $\\checkmark 82$ (or reading from ogive between $80$ and $84$)
* $\\checkmark$ answer ($18$ people, accept $16 - 20$)""",
    final_answer="18\\text{ people (accept } 16 - 20)"
)

# ==========================================
# QUESTION 3: Analytical Geometry - Lines & Polygons
# ==========================================
p_q3 = """In the Cartesian plane:
$P$, $R(3; 5)$, $S(-3; -7)$ and $T(-5; k)$ are vertices of trapezium $PRST$ with $PT \\parallel RS$.
$RS$ and $PR$ intersect the $y$-axis at $D$ and $C(0; 5)$ respectively.
$PT$ and $RS$ intersect the $x$-axis at $E$ and $F$ respectively.
$P\\hat{E}F = \\theta$."""

add_item(
    qref="3.1",
    marks=1,
    topic="Analytical Geometry - Equations of Lines",
    passage=p_q3,
    question="Write down the equation of $PR$.",
    memo="""Since $C(0; 5)$ and $R(3; 5)$ both have $y$-coordinate $5$, $PR$ is horizontal:
$$y = 5$$

* $\\checkmark$ answer ($y = 5$)""",
    final_answer="y = 5"
)

add_item(
    qref="3.2.1",
    marks=2,
    topic="Analytical Geometry - Gradient",
    passage=p_q3,
    question="Calculate the gradient of $RS$.",
    memo="""$$m_{RS} = \\frac{y_2 - y_1}{x_2 - x_1} = \\frac{5 - (-7)}{3 - (-3)} = \\frac{12}{6} = 2$$

* $\\checkmark$ substitution of $R(3; 5)$ and $S(-3; -7)$ into gradient formula
* $\\checkmark$ answer ($m_{RS} = 2$)""",
    final_answer="2"
)

add_item(
    qref="3.2.2",
    marks=3,
    topic="Analytical Geometry - Inclination Angle",
    passage=p_q3,
    question="Calculate the size of $\\theta$.",
    memo="""Since $PT \\parallel RS$:
$$m_{PT} = m_{RS} = 2$$
$$\\tan \\theta = m_{PT} = 2$$
$$\\theta = \\arctan(2) \\approx 63{,}43^\\circ$$

* $\\checkmark m_{PT} = m_{RS}$
* $\\checkmark \\tan \\theta = 2$
* $\\checkmark \\theta = 63{,}43^\\circ$""",
    final_answer="63{,}43^\\circ"
)

add_item(
    qref="3.2.3",
    marks=3,
    topic="Analytical Geometry - Equations of Lines",
    passage=p_q3,
    question="Calculate the coordinates of $D$.",
    memo="""Equation of line $RS$ with gradient $m = 2$ through $R(3; 5)$:
$$y - y_1 = m(x - x_1)$$
$$y - 5 = 2(x - 3)$$
$$y = 2x - 1$$
$D$ is the $y$-intercept ($x = 0$):
$$y = 2(0) - 1 = -1$$
$$\\therefore D(0; -1)$$

* $\\checkmark$ substitution
* $\\checkmark$ equation of $RS$ ($y = 2x - 1$)
* $\\checkmark$ coordinates of $D$ ($(0; -1)$)""",
    final_answer="(0; -1)"
)

add_item(
    qref="3.3",
    marks=4,
    topic="Analytical Geometry - Distance Formula",
    passage=p_q3,
    question="If it is given that $TS = 2\\sqrt{5}$, calculate the value of $k$.",
    memo="""Using the distance formula between $T(-5; k)$ and $S(-3; -7)$:
$$TS = \\sqrt{(x_S - x_T)^2 + (y_S - y_T)^2} = 2\\sqrt{5}$$
$$((-3) - (-5))^2 + ((-7) - k)^2 = (2\\sqrt{5})^2$$
$$(2)^2 + (k + 7)^2 = 20$$
$$4 + (k + 7)^2 = 20$$
$$(k + 7)^2 = 16$$
$$k + 7 = \\pm 4$$
$$k = -3 \\quad \\text{or} \\quad k = -11$$
From the diagram, $T(-5; k)$ lies above $S(-3; -7)$ where $y_S = -7$, so $k > -7$:
$$\\therefore k = -3$$

* $\\checkmark$ substitute $S$ and $T$ into distance formula
* $\\checkmark (k + 7)^2 = 16$ or standard form $k^2 + 14k + 33 = 0$
* $\\checkmark k + 7 = \\pm 4$ or factors $(k + 3)(k + 11) = 0$
* $\\checkmark$ answer ($k = -3$)""",
    final_answer="k = -3"
)

add_item(
    qref="3.4",
    marks=3,
    topic="Analytical Geometry - Transformations & Parallelograms",
    passage=p_q3,
    question="Parallelogram $TDNS$, with $N$ in the $4^{\\text{th}}$ quadrant, is drawn. Calculate the coordinates of $N$.",
    memo="""Method 1 (Translation):
From $T(-5; -3)$ to $S(-3; -7)$:
$$(x; y) \\to (x + 2; y - 4)$$
Applying this translation to $D(0; -1)$ gives $N$:
$$N(0 + 2; -1 - 4) = N(2; -5)$$

Method 2 (Midpoint of diagonals):
In parallelogram $TDNS$, the diagonals $TN$ and $SD$ bisect each other:
$$\\text{Midpoint of } SD = \\left(\\frac{-3 + 0}{2}; \\frac{-7 + (-1)}{2}\\right) = \\left(-\\frac{3}{2}; -4\\right)$$
$$\\text{Midpoint of } TN = \\left(\\frac{-5 + x_N}{2}; \\frac{-3 + y_N}{2}\\right)$$
$$\\frac{-5 + x_N}{2} = -\\frac{3}{2} \\implies x_N = 2$$
$$\\frac{-3 + y_N}{2} = -4 \\implies y_N = -5$$
$$\\therefore N(2; -5)$$

* $\\checkmark$ method (translation or midpoint of diagonals)
* $\\checkmark x$-coordinate ($2$)
* $\\checkmark y$-coordinate ($-5$)""",
    final_answer="(2; -5)"
)

add_item(
    qref="3.5",
    marks=3,
    topic="Analytical Geometry - Transformations & Angle Between Lines",
    passage=p_q3,
    question="$\\Delta PRD$ is reflected about the $y$-axis to form $\\Delta P'R'D'$. Calculate the size of $R\\hat{D}R'$.",
    memo="""Method 1:
Inclination of line $RS$ (through $D(0; -1)$ and $R(3; 5)$):
$$\\beta = \\arctan(2) \\approx 63{,}434\\dots^\\circ$$
The angle between line $RD$ and the positive $y$-axis is:
$$O\\hat{D}F = 90^\\circ - 63{,}434\\dots^\\circ = 26{,}565\\dots^\\circ$$
Since reflection across the $y$-axis reflects line $RD$ across the $y$-axis:
$$R\\hat{D}R' = 2 \\times 26{,}565\\dots^\\circ \\approx 53{,}13^\\circ$$

Method 2:
In right-angled triangle $\\Delta RCD$ with $C(0; 5)$ and $D(0; -1)$:
$CD = 5 - (-1) = 6$ and $CR = 3$.
$$\\tan(R\\hat{D}C) = \\frac{CR}{CD} = \\frac{3}{6} = 0{,}5$$
$$R\\hat{D}C = \\arctan(0{,}5) \\approx 26{,}565\\dots^\\circ$$
By reflection across the $y$-axis:
$$R\\hat{D}R' = 2 \\times 26{,}565\\dots^\\circ \\approx 53{,}13^\\circ$$

* $\\checkmark \\tan(R\\hat{D}C) = \\frac{3}{6}$ or inclination $\\beta = 63{,}43^\\circ$
* $\\checkmark R\\hat{D}C = 26{,}57^\\circ$
* $\\checkmark$ answer ($R\\hat{D}R' = 53{,}13^\\circ$)""",
    final_answer="53{,}13^\\circ"
)

# ==========================================
# QUESTION 4: Analytical Geometry - Circles & Tangents
# ==========================================
p_q4 = """In the Cartesian plane:
A circle with centre $M$ touches the $x$-axis at $A(-1; 0)$ and the $y$-axis at $B(0; 1)$.
A smaller circle, centred at $N\\left(-\\frac{1}{2}; \\frac{3}{2}\\right)$, passes through $M$ and cuts the larger circle at $B$ and $C$.
$BNC$ is a diameter of the smaller circle.
A tangent drawn to the smaller circle at $C$, cuts the $x$-axis at $D$."""

add_item(
    qref="4.1",
    marks=3,
    topic="Analytical Geometry - Circles & Tangents",
    passage=p_q4,
    question="Determine the equation of the circle centred at $M$ in the form $(x-a)^2 + (y-b)^2 = r^2$.",
    memo="""Since the circle touches the $x$-axis at $A(-1; 0)$ and the $y$-axis at $B(0; 1)$, the centre is $M(-1; 1)$ and the radius $r = 1$.
Equation of the circle:
$$(x - (-1))^2 + (y - 1)^2 = 1^2$$
$$(x + 1)^2 + (y - 1)^2 = 1$$

* $\\checkmark M(-1; 1)$
* $\\checkmark \\text{LHS: } (x + 1)^2 + (y - 1)^2$
* $\\checkmark \\text{RHS: } 1$""",
    final_answer="(x + 1)^2 + (y - 1)^2 = 1"
)

add_item(
    qref="4.2",
    marks=2,
    topic="Analytical Geometry - Circles & Tangents",
    passage=p_q4,
    question="Calculate the coordinates of $C$.",
    memo="""Since $BNC$ is a diameter of the smaller circle, $N\\left(-\\frac{1}{2}; \\frac{3}{2}\\right)$ is the midpoint of $BC$:
$$\\frac{0 + x_C}{2} = -\\frac{1}{2} \\implies x_C = -1$$
$$\\frac{1 + y_C}{2} = \\frac{3}{2} \\implies y_C = 2$$
$$\\therefore C(-1; 2)$$

* $\\checkmark x$-coordinate ($-1$)
* $\\checkmark y$-coordinate ($2$)""",
    final_answer="(-1; 2)"
)

add_item(
    qref="4.3",
    marks=4,
    topic="Analytical Geometry - Circles & Tangents",
    passage=p_q4,
    question="Show that the equation of the tangent $CD$ is $y - x = 3$.",
    memo="""Gradient of diameter $BC$ (or radius $NC$):
$$m_{radius} = \\frac{y_C - y_B}{x_C - x_B} = \\frac{2 - 1}{-1 - 0} = -1$$
Since the tangent $CD$ is perpendicular to the radius ($CD \\perp BC$):
$$m_{tangent} = -\\frac{1}{-1} = 1$$
Equation of tangent $CD$ passing through $C(-1; 2)$:
$$y - y_1 = m(x - x_1)$$
$$y - 2 = 1(x - (-1))$$
$$y - 2 = x + 1$$
$$y = x + 3 \\implies y - x = 3$$

* $\\checkmark m_{radius} = -1$
* $\\checkmark m_{tangent} = 1$
* $\\checkmark$ substitution of $(-1; 2)$ and $m = 1$
* $\\checkmark$ simplification to $y - x = 3$""",
    final_answer="y - x = 3"
)

add_item(
    qref="4.4",
    marks=3,
    topic="Analytical Geometry - Circles & Tangents",
    passage=p_q4,
    question="Determine the values of $t$ for which the line $y = x + t$ will NOT touch or cut the smaller circle.",
    memo="""The tangent to the smaller circle at $C(-1; 2)$ is:
$$y = x + 3 \\quad (t = 3)$$
The parallel tangent on the opposite side of the circle passes through $B(0; 1)$:
$$y - 1 = 1(x - 0) \\implies y = x + 1 \\quad (t = 1)$$
Lines $y = x + t$ touch or cut the smaller circle for $1 \\le t \\le 3$.
Therefore, lines that do NOT touch or cut the smaller circle satisfy:
$$t > 3 \\quad \\text{or} \\quad t < 1$$

* $\\checkmark y = x + 1$ (finding boundary tangent $t = 1$)
* $\\checkmark t > 3$
* $\\checkmark t < 1$""",
    final_answer="t > 3 \\text{ or } t < 1"
)

add_item(
    qref="4.5",
    marks=3,
    topic="Analytical Geometry - Circles & Tangents",
    passage=p_q4,
    question="The smaller circle centred at $N$ is transformed such that point $C$ is translated along the tangent to $D$. Calculate the coordinates of $E$, the new centre of the smaller circle.",
    memo="""First find coordinates of $D$:
$D$ is the $x$-intercept of tangent $y - x = 3$:
$$0 - x = 3 \\implies x = -3 \\implies D(-3; 0)$$
Method 1 (Translation vector):
Vector from point $C(-1; 2)$ to centre $N\\left(-\\frac{1}{2}; \\frac{3}{2}\\right)$ is:
$$\\vec{CN} = \\left(-\\frac{1}{2} - (-1); \\frac{3}{2} - 2\\right) = (0{,}5; -0{,}5)$$
When point $C$ translates to $D(-3; 0)$, the new centre $E$ has the same relative position to $D$:
$$E(-3 + 0{,}5; 0 - 0{,}5) = E(-2{,}5; -0{,}5) = E\\left(-\\frac{5}{2}; -\\frac{1}{2}\\right)$$

Method 2 (Midpoint of $DN$):
$CNED$ forms a rectangle where diagonals $CE$ and $DN$ bisect each other:
$$\\text{Midpoint of } DN = \\left(\\frac{-3 + (-0{,}5)}{2}; \\frac{0 + 1{,}5}{2}\\right) = \\left(-\\frac{7}{4}; \\frac{3}{4}\\right)$$
$$\\therefore E = \\left(-\\frac{5}{2}; -\\frac{1}{2}\\right) = (-2{,}5; -0{,}5)$$

* $\\checkmark$ coordinates of $D(-3; 0)$ (or midpoint of $DN$)
* $\\checkmark x$-coordinate ($-2{,}5$ or $-\\frac{5}{2}$)
* $\\checkmark y$-coordinate ($-0{,}5$ or $-\\frac{1}{2}$)""",
    final_answer="\\left(-\\frac{5}{2}; -\\frac{1}{2}\\right) \\text{ or } (-2{,}5; -0{,}5)"
)

add_item(
    qref="4.6",
    marks=5,
    topic="Analytical Geometry - Circles & Tangents",
    passage=p_q4,
    question="If it is given that the area of quadrilateral $OBCD$ is $2a^2$ square units and $a > 0$, show that $a = \\frac{\\sqrt{7}}{2}$ units.",
    memo="""Vertices of quadrilateral $OBCD$:
$O(0; 0)$, $B(0; 1)$, $C(-1; 2)$, $D(-3; 0)$.
Divide quadrilateral $OBCD$ into trapezium $AOBC$ and triangle $\\Delta ACD$, where $A(-1; 0)$ is on the $x$-axis:
1. Area of trapezium $AOBC$:
   Parallel vertical sides $OB = 1$ and $AC = 2$, perpendicular height $OA = 1$:
   $$\\text{Area}(AOBC) = \\frac{1}{2}(OB + AC) \\times OA = \\frac{1}{2}(1 + 2)(1) = \\frac{3}{2} = 1{,}5 \\text{ sq units}$$
2. Area of $\\Delta ACD$:
   Base along $x$-axis $AD = |-1 - (-3)| = 2$, perpendicular height $h = y_C = 2$:
   $$\\text{Area}(\\Delta ACD) = \\frac{1}{2} \\times 2 \\times 2 = 2 \\text{ sq units}$$
3. Total area of quadrilateral $OBCD$:
   $$\\text{Area}(OBCD) = \\frac{3}{2} + 2 = \\frac{7}{2} = 3{,}5 \\text{ sq units}$$
Equating to $2a^2$:
$$2a^2 = \\frac{7}{2}$$
$$a^2 = \\frac{7}{4}$$
$$a = \\frac{\\sqrt{7}}{2} \\quad (\\text{since } a > 0)$$

* $\\checkmark$ substitution into area of trapezium formula
* $\\checkmark$ area of trapezium ($= \\frac{3}{2}$)
* $\\checkmark$ area of triangle ($= 2$)
* $\\checkmark$ area of quadrilateral $OBCD$ ($= \\frac{7}{2}$)
* $\\checkmark$ equating $2a^2 = \\frac{7}{2} \\implies a = \\frac{\\sqrt{7}}{2}$""",
    final_answer="a = \\frac{\\sqrt{7}}{2}"
)

# ==========================================
# QUESTION 5: Trigonometry - Identities, Double Angles & General Solution
# ==========================================
add_item(
    qref="5.1",
    marks=5,
    topic="Trigonometry - Identities & Reduction Formulas",
    passage="",
    question="""Simplify the following expression to ONE trigonometric term:
$$\\frac{\\sin x}{\\cos x \\cdot \\tan x} + \\sin(180^\\circ + x)\\cos(90^\\circ - x)$$""",
    memo="""$$\\frac{\\sin x}{\\cos x \\cdot \\tan x} + \\sin(180^\\circ + x)\\cos(90^\\circ - x)$$
Since $\\tan x = \\frac{\\sin x}{\\cos x}$:
$$\\cos x \\cdot \\tan x = \\cos x \\cdot \\frac{\\sin x}{\\cos x} = \\sin x$$
$$\\frac{\\sin x}{\\sin x} = 1$$
Using reduction formulae:
$$\\sin(180^\\circ + x) = -\\sin x$$
$$\\cos(90^\\circ - x) = \\sin x$$
Expression becomes:
$$1 + (-\\sin x)(\\sin x) = 1 - \\sin^2 x = \\cos^2 x$$

* $\\checkmark \\tan x = \\frac{\\sin x}{\\cos x}$
* $\\checkmark -\\sin x$
* $\\checkmark \\sin x$
* $\\checkmark 1 - \\sin^2 x$
* $\\checkmark \\cos^2 x$""",
    final_answer="\\cos^2 x"
)

add_item(
    qref="5.2",
    marks=4,
    topic="Trigonometry - Double Angle Formulas",
    passage="",
    question="""Without using a calculator, determine the value of:
$$\\frac{\\sin^2 35^\\circ - \\cos^2 35^\\circ}{4\\sin 10^\\circ \\cos 10^\\circ}$$""",
    memo="""Numerator:
$$\\sin^2 35^\\circ - \\cos^2 35^\\circ = -(\\cos^2 35^\\circ - \\sin^2 35^\\circ) = -\\cos(2 \\times 35^\\circ) = -\\cos 70^\\circ$$
Denominator:
$$4\\sin 10^\\circ \\cos 10^\\circ = 2(2\\sin 10^\\circ \\cos 10^\\circ) = 2\\sin(2 \\times 10^\\circ) = 2\\sin 20^\\circ$$
Using co-functions: $\\sin 20^\\circ = \\cos(90^\\circ - 20^\\circ) = \\cos 70^\\circ$:
$$\\frac{-\\cos 70^\\circ}{2\\sin 20^\\circ} = \\frac{-\\cos 70^\\circ}{2\\cos 70^\\circ} = -\\frac{1}{2}$$

* $\\checkmark -(\\cos^2 35^\\circ - \\sin^2 35^\\circ)$
* $\\checkmark -\\cos 70^\\circ$
* $\\checkmark 2\\sin 20^\\circ$
* $\\checkmark -\\frac{1}{2}$""",
    final_answer="-\\frac{1}{2}"
)

add_item(
    qref="5.3",
    marks=4,
    topic="Trigonometry - Double Angle Formulas",
    passage="",
    question="""Given: $\\cos 26^\\circ = m$

Without using a calculator, determine $2\\sin^2 77^\\circ$ in terms of $m$.""",
    memo="""Method 1:
Using co-functions:
$$\\sin 77^\\circ = \\sin(90^\\circ - 13^\\circ) = \\cos 13^\\circ$$
$$2\\sin^2 77^\\circ = 2\\cos^2 13^\\circ$$
From the double-angle formula for cosine:
$$\\cos(2 \\times 13^\\circ) = 2\\cos^2 13^\\circ - 1$$
$$\\cos 26^\\circ = 2\\cos^2 13^\\circ - 1$$
$$2\\cos^2 13^\\circ = 1 + \\cos 26^\\circ = 1 + m$$

Method 2:
$$\\cos(2 \\times 77^\\circ) = 1 - 2\\sin^2 77^\\circ$$
$$\\cos 154^\\circ = 1 - 2\\sin^2 77^\\circ$$
$$2\\sin^2 77^\\circ = 1 - \\cos 154^\\circ$$
$$\\cos 154^\\circ = \\cos(180^\\circ - 26^\\circ) = -\\cos 26^\\circ = -m$$
$$2\\sin^2 77^\\circ = 1 - (-m) = 1 + m$$

* $\\checkmark$ using co-ratio / double angle formula
* $\\checkmark$ reduction
* $\\checkmark 2\\cos^2 13^\\circ - 1 = \\cos 26^\\circ$ or $1 - 2\\sin^2 77^\\circ = \\cos 154^\\circ$
* $\\checkmark$ answer ($m + 1$ or $1 + m$)""",
    final_answer="m + 1"
)

add_item(
    qref="5.4.1",
    marks=6,
    topic="Trigonometry - General Solutions & Compound Angles",
    passage="",
    question="""Consider: $f(x) = \\sin(x + 25^\\circ)\\cos 15^\\circ - \\cos(x + 25^\\circ)\\sin 15^\\circ$

Determine the general solution of $f(x) = \\tan 165^\\circ$.""",
    memo="""Using the compound angle identity:
$$f(x) = \\sin((x + 25^\\circ) - 15^\\circ) = \\sin(x + 10^\\circ)$$
Equation:
$$\\sin(x + 10^\\circ) = \\tan 165^\\circ$$
$$\\tan 165^\\circ = \\tan(180^\\circ - 15^\\circ) = -\\tan 15^\\circ \\approx -0{,}2679\\dots$$
Reference angle:
$$\\arcsin(0{,}2679\\dots) \\approx 15{,}54^\\circ$$
Since sine is negative:
Quadrant 3:
$$x + 10^\\circ = 180^\\circ + 15{,}54^\\circ + k \\cdot 360^\\circ = 195{,}54^\\circ + k \\cdot 360^\\circ$$
$$x = 185{,}54^\\circ + k \\cdot 360^\\circ; \\quad k \\in \\mathbb{Z}$$
Quadrant 4:
$$x + 10^\\circ = 360^\\circ - 15{,}54^\\circ + k \\cdot 360^\\circ = 344{,}46^\\circ + k \\cdot 360^\\circ$$
$$x = 334{,}46^\\circ + k \\cdot 360^\\circ; \\quad k \\in \\mathbb{Z}$$

* $\\checkmark\\checkmark \\sin(x + 10^\\circ)$
* $\\checkmark -0{,}2679\\dots$
* $\\checkmark 195{,}54^\\circ \\text{ and } 344{,}46^\\circ$
* $\\checkmark 185{,}54^\\circ \\text{ and } 334{,}46^\\circ$
* $\\checkmark + k \\cdot 360^\\circ; \\quad k \\in \\mathbb{Z}$""",
    final_answer="x = 185{,}54^\\circ + k \\cdot 360^\\circ \\text{ or } x = 334{,}46^\\circ + k \\cdot 360^\\circ; \\quad k \\in \\mathbb{Z}"
)

add_item(
    qref="5.4.2",
    marks=3,
    topic="Trigonometry - Functions & Graphs",
    passage="",
    question="""Determine the value(s) of $x$ in the interval $x \\in [0^\\circ; 360^\\circ]$ for which $f(x)$ will have a minimum value.""",
    memo="""$$f(x) = \\sin(x + 10^\\circ)$$
The minimum value of $\\sin \\theta$ is $-1$, which occurs at $\\theta = 270^\\circ$.
For $f(x)$ to be a minimum:
$$x + 10^\\circ = 270^\\circ$$
$$x = 260^\\circ$$
$260^\\circ \\in [0^\\circ; 360^\\circ]$.

* $\\checkmark f(x) = \\sin(x + 10^\\circ)$
* $\\checkmark 270^\\circ$
* $\\checkmark x = 260^\\circ$""",
    final_answer="x = 260^\\circ"
)

# ==========================================
# QUESTION 6: Trigonometry - Functions & Graphs
# ==========================================
p_q6 = """In the Cartesian plane:
The graphs of $f(x) = \\sin x - 1$ and $g(x) = \\cos 2x$ are drawn for the interval $x \\in [-90^\\circ; 360^\\circ]$.
Graphs $f$ and $g$ intersect at $A$.
$B(360^\\circ; -1)$ is a point on $f$."""

add_item(
    qref="6.1",
    marks=2,
    topic="Trigonometry - Functions & Graphs",
    passage=p_q6,
    question="Write down the range of $f$.",
    memo="""Since $-1 \\le \\sin x \\le 1$:
$$-1 - 1 \\le \\sin x - 1 \\le 1 - 1$$
$$-2 \\le f(x) \\le 0$$
$$\\therefore y \\in [-2; 0] \\quad \\text{OR} \\quad -2 \\le y \\le 0$$

* $\\checkmark$ critical values ($-2$ and $0$)
* $\\checkmark$ notation ($y \\in [-2; 0]$ or $-2 \\le y \\le 0$)""",
    final_answer="y \\in [-2; 0] \\text{ or } -2 \\le y \\le 0"
)

add_item(
    qref="6.2",
    marks=2,
    topic="Trigonometry - Functions & Graphs",
    passage=p_q6,
    question="Write down the values of $x$ in the interval $x \\in [-90^\\circ; 360^\\circ]$ for which graph $f$ is decreasing.",
    memo="""The graph of $f(x) = \\sin x - 1$ reaches a maximum at $x = 90^\\circ$ and a minimum at $x = 270^\\circ$.
Graph $f$ decreases between its local maximum and local minimum:
$$x \\in (90^\\circ; 270^\\circ) \\quad \\text{OR} \\quad x \\in [90^\\circ; 270^\\circ] \\quad \\text{OR} \\quad 90^\\circ < x < 270^\\circ$$

* $\\checkmark$ critical values ($90^\\circ$ and $270^\\circ$)
* $\\checkmark$ notation ($x \\in (90^\\circ; 270^\\circ)$ or $90^\\circ \\le x \\le 270^\\circ$)""",
    final_answer="x \\in (90^\\circ; 270^\\circ) \\text{ or } 90^\\circ \\le x \\le 270^\\circ"
)

add_item(
    qref="6.3",
    marks=6,
    topic="Trigonometry - Functions & Graphs",
    passage=p_q6,
    question="$P$ and $Q$ are points on graphs $g$ and $f$ respectively such that $PQ$ is parallel to the $y$-axis. If $PQ$ lies between $A$ and $B$, determine the value(s) of $x$ for which $PQ$ will be a maximum.",
    memo="""Vertical distance between $g$ and $f$:
$$PQ = g(x) - f(x) = \\cos 2x - (\\sin x - 1)$$
Using the double angle identity $\\cos 2x = 1 - 2\\sin^2 x$:
$$PQ = 1 - 2\\sin^2 x - \\sin x + 1 = -2\\sin^2 x - \\sin x + 2$$
This is a quadratic in $\\sin x$:
Maximum occurs at the turning point:
$$\\sin x = -\\frac{b}{2a} = -\\frac{-1}{2(-2)} = -\\frac{1}{4} = -0{,}25$$
Reference angle:
$$\\arcsin(0{,}25) \\approx 14{,}48^\\circ$$
Between $A$ and $B$, sine is negative in quadrants 3 and 4:
Quadrant 3:
$$x = 180^\\circ + 14{,}48^\\circ = 194{,}48^\\circ$$
Quadrant 4:
$$x = 360^\\circ - 14{,}48^\\circ = 345{,}52^\\circ$$

* $\\checkmark PQ = \\cos 2x - (\\sin x - 1)$
* $\\checkmark \\cos 2x = 1 - 2\\sin^2 x$
* $\\checkmark$ substitution into turning point formula $-\\frac{b}{2a}$
* $\\checkmark \\sin x = -\\frac{1}{4}$
* $\\checkmark x = 194{,}48^\\circ$
* $\\checkmark x = 345{,}52^\\circ$""",
    final_answer="x = 194{,}48^\\circ \\text{ or } x = 345{,}52^\\circ"
)

# ==========================================
# QUESTION 7: Trigonometry - 2D & 3D Problems
# ==========================================
p_q7 = """In 3D space:
A solar panel $ABCD$ is fixed to a horizontal concrete slab $EFCD$.
$ABCD$ and $EFCD$ are identical rhombuses with side length $x$ ($AD = DC = CB = BA = DE = EF = FC = CD = x$).
$K$ is a point on $DC$ such that $DK = KC = \\frac{1}{2}x$ and $AK \\perp DC$.
$A\\hat{D}C = C\\hat{D}E = 60^\\circ$.
$AF$ and $KF$ are drawn."""

add_item(
    qref="7.1",
    marks=2,
    topic="Trigonometry - 2D & 3D Applications",
    passage=p_q7,
    question="Determine $AK$ in terms of $x$.",
    memo="""In right-angled triangle $\\Delta AKD$ ($A\\hat{K}D = 90^\\circ$ and $A\\hat{D}K = 60^\\circ$):
$$\\sin 60^\\circ = \\frac{AK}{AD} = \\frac{AK}{x}$$
$$AK = x \\sin 60^\\circ = \\frac{\\sqrt{3}}{2}x \\quad (\\text{or } 0{,}866x)$$

* $\\checkmark$ trig ratio ($\\sin 60^\\circ = \\frac{AK}{x}$)
* $\\checkmark$ answer ($AK = \\frac{\\sqrt{3}}{2}x$)""",
    final_answer="AK = \\frac{\\sqrt{3}}{2}x"
)

add_item(
    qref="7.2",
    marks=1,
    topic="Trigonometry - 2D & 3D Applications",
    passage=p_q7,
    question="Write down the size of $K\\hat{C}F$.",
    memo="""In rhombus $EFCD$, consecutive angles are supplementary ($C\\hat{D}E + D\\hat{C}F = 180^\\circ$):
$$D\\hat{C}F = 180^\\circ - 60^\\circ = 120^\\circ$$
Since $K$ lies on $DC$:
$$K\\hat{C}F = 120^\\circ$$

* $\\checkmark$ answer ($120^\\circ$)""",
    final_answer="120^\\circ"
)

add_item(
    qref="7.3",
    marks=7,
    topic="Trigonometry - 2D & 3D Applications",
    passage=p_q7,
    question="It is further given that $A\\hat{K}F$, the angle between the solar panel and the concrete slab, is $y$. Determine the area of $\\Delta AKF$ in terms of $x$ and $y$.",
    memo="""1. In $\\Delta KCF$:
   $CK = \\frac{1}{2}x$, $CF = x$, and $K\\hat{C}F = 120^\\circ$.
   Using the cosine rule in $\\Delta KCF$:
   $$KF^2 = CK^2 + CF^2 - 2(CK)(CF)\\cos(K\\hat{C}F)$$
   $$KF^2 = \\left(\\frac{x}{2}\\right)^2 + x^2 - 2\\left(\\frac{x}{2}\\right)(x)\\cos 120^\\circ$$
   Since $\\cos 120^\\circ = -\\frac{1}{2}$:
   $$KF^2 = \\frac{x^2}{4} + x^2 - x^2\\left(-\\frac{1}{2}\\right) = \\frac{x^2}{4} + x^2 + \\frac{x^2}{2} = \\frac{7}{4}x^2$$
   $$KF = \\frac{\\sqrt{7}}{2}x$$

2. In $\\Delta AKF$:
   Sides are $AK = \\frac{\\sqrt{3}}{2}x$ and $KF = \\frac{\\sqrt{7}}{2}x$, with included angle $A\\hat{K}F = y$.
   Using the area rule:
   $$\\text{Area}(\\Delta AKF) = \\frac{1}{2}(AK)(KF)\\sin(A\\hat{K}F)$$
   $$\\text{Area}(\\Delta AKF) = \\frac{1}{2}\\left(\\frac{\\sqrt{3}}{2}x\\right)\\left(\\frac{\\sqrt{7}}{2}x\\right)\\sin y = \\frac{\\sqrt{21}}{8}x^2 \\sin y$$

* $\\checkmark$ correct use of cosine rule in $\\Delta KCF$
* $\\checkmark$ substitution of $CK = \\frac{x}{2}$ and $CF = x$
* $\\checkmark \\cos 120^\\circ = -\\frac{1}{2}$
* $\\checkmark KF = \\frac{\\sqrt{7}}{2}x$
* $\\checkmark$ correct use of area rule in $\\Delta AKF$
* $\\checkmark$ substitution of $AK$ and $KF$
* $\\checkmark$ answer in terms of $x$ and $y$ ($\\frac{\\sqrt{21}}{8}x^2 \\sin y$)""",
    final_answer="\\frac{\\sqrt{21}}{8}x^2 \\sin y"
)

# ==========================================
# QUESTION 8: Euclidean Geometry - Circle Geometry & Quadrilaterals
# ==========================================
p_q8_1 = """In the circle:
$PQRS$ is a cyclic quadrilateral. Chord $RS$ is produced to $T$.
$K$ is a point on $RS$ and $W$ is a point on the circle such that $QRKW$ is a parallelogram ($QW \\parallel RK$ and $QR \\parallel WK$).
$PS$ and $QW$ intersect at $U$.
Given: $P\\hat{S}T = 136^\\circ$ and $\\hat{Q}_1 = 100^\\circ$ (where $\\hat{Q}_1 = W\\hat{Q}R$)."""

add_item(
    qref="8.1.1",
    marks=2,
    topic="Euclidean Geometry - Circle Geometry & Quadrilaterals",
    passage=p_q8_1,
    question="Determine, with reasons, the size of $\\hat{R}$.",
    memo="""In parallelogram $QRKW$, $QW \\parallel RK$:
$$\\hat{R} + \\hat{Q}_1 = 180^\\circ \\quad [\\text{co-interior } \\angle\\text{s}; QW \\parallel RK]$$
$$\\hat{R} = 180^\\circ - 100^\\circ = 80^\\circ$$

* $\\checkmark$ Statement: $\\hat{R} = 80^\\circ$
* $\\checkmark$ Reason: co-interior $\\angle\\text{s}; QW \\parallel RK$""",
    final_answer="\\hat{R} = 80^\\circ"
)

add_item(
    qref="8.1.2",
    marks=2,
    topic="Euclidean Geometry - Circle Geometry & Quadrilaterals",
    passage=p_q8_1,
    question="Determine, with reasons, the size of $\\hat{P}$.",
    memo="""$PQRS$ is a cyclic quadrilateral:
$$\\hat{P} + \\hat{R} = 180^\\circ \\quad [\\text{opposite } \\angle\\text{s of cyclic quad}]$$
$$\\hat{P} = 180^\\circ - 80^\\circ = 100^\\circ$$

* $\\checkmark$ Statement: $\\hat{P} = 100^\\circ$
* $\\checkmark$ Reason: opposite $\\angle\\text{s of cyclic quad}$""",
    final_answer="\\hat{P} = 100^\\circ"
)

add_item(
    qref="8.1.3",
    marks=3,
    topic="Euclidean Geometry - Circle Geometry & Quadrilaterals",
    passage=p_q8_1,
    question="Determine, with reasons, the size of $P\\hat{Q}W$.",
    memo="""Method 1:
In cyclic quad $PQRS$:
$$P\\hat{Q}R = P\\hat{S}T = 136^\\circ \\quad [\\text{exterior } \\angle \\text{ of cyclic quad}]$$
Since $P\\hat{Q}R = P\\hat{Q}W + \\hat{Q}_1$ and $\\hat{Q}_1 = 100^\\circ$:
$$P\\hat{Q}W = 136^\\circ - 100^\\circ = 36^\\circ$$

Method 2:
$$P\\hat{U}W = P\\hat{S}T = 136^\\circ \\quad [\\text{corresponding } \\angle\\text{s}; QW \\parallel RK]$$
In $\\Delta PQU$, exterior angle:
$$P\\hat{U}W = \\hat{P} + P\\hat{Q}W \\quad [\\text{exterior } \\angle \\text{ of } \\Delta]$$
$$136^\\circ = 100^\\circ + P\\hat{Q}W \\implies P\\hat{Q}W = 36^\\circ$$

* $\\checkmark$ Statement: $P\\hat{Q}R = 136^\\circ$
* $\\checkmark$ Reason: exterior $\\angle$ of cyclic quad
* $\\checkmark$ Statement: $P\\hat{Q}W = 36^\\circ$""",
    final_answer="P\\hat{Q}W = 36^\\circ"
)

add_item(
    qref="8.1.4",
    marks=2,
    topic="Euclidean Geometry - Circle Geometry & Quadrilaterals",
    passage=p_q8_1,
    question="Determine, with reasons, the size of $\\hat{U}_2$.",
    memo="""Method 1:
$$\\hat{U}_2 = P\\hat{S}T = 136^\\circ \\quad [\\text{alternate } \\angle\\text{s}; QW \\parallel RK]$$

Method 2:
$$\\hat{U}_2 = \\hat{P} + P\\hat{Q}W = 100^\\circ + 36^\\circ = 136^\\circ \\quad [\\text{exterior } \\angle \\text{ of } \\Delta PQU]$$

* $\\checkmark$ Statement: $\\hat{U}_2 = 136^\\circ$
* $\\checkmark$ Reason: alternate $\\angle\\text{s}; QW \\parallel RK$ (or exterior $\\angle$ of $\\Delta$)""",
    final_answer="\\hat{U}_2 = 136^\\circ"
)

p_q8_2 = """In quadrilateral $CDEF$:
The diagonals of quadrilateral $CDEF$ intersect at $T$.
Given side and segment lengths:
$EF = 9$ units, $DC = 18$ units,
$ET = 7$ units, $TC = 10$ units,
$FT = 5$ units, $TD = 14$ units."""

add_item(
    qref="8.2.1",
    marks=4,
    topic="Euclidean Geometry - Similarity & Proportion",
    passage=p_q8_2,
    question="Prove, with reasons, that $E\\hat{F}D = E\\hat{C}D$.",
    memo="""In $\\Delta EFT$ and $\\Delta DCT$:
$$\\frac{EF}{CD} = \\frac{9}{18} = \\frac{1}{2}$$
$$\\frac{FT}{TC} = \\frac{5}{10} = \\frac{1}{2}$$
$$\\frac{ET}{TD} = \\frac{7}{14} = \\frac{1}{2}$$
Since all three pairs of corresponding sides are in the same proportion:
$$\\frac{EF}{CD} = \\frac{FT}{TC} = \\frac{ET}{TD} = \\frac{1}{2}$$
$$\\therefore \\Delta EFT \\mathbin{|||} \\Delta DCT \\quad [\\text{sides of } \\Delta \\text{ in proportion}]$$
$$\\therefore E\\hat{F}T = D\\hat{C}T \\quad [\\text{corresponding } \\angle\\text{s of similar triangles}]$$
$$\\therefore E\\hat{F}D = E\\hat{C}D$$

* $\\checkmark\\checkmark$ all 3 ratios equal to $\\frac{1}{2}$
* $\\checkmark \\Delta EFT \\mathbin{|||} \\Delta DCT$
* $\\checkmark$ Reason: sides of $\\Delta$ in proportion""",
    final_answer="E\\hat{F}D = E\\hat{C}D"
)

add_item(
    qref="8.2.2",
    marks=3,
    topic="Euclidean Geometry - Circle Geometry & Quadrilaterals",
    passage=p_q8_2,
    question="Prove, with reasons, that $D\\hat{F}C = D\\hat{E}C$.",
    memo="""From 8.2.1:
$$E\\hat{F}D = E\\hat{C}D$$
Since line segment $ED$ subtends equal angles at vertices $F$ and $C$ on the same side:
$$\\therefore EFCD \\text{ is a cyclic quadrilateral} \\quad [\\text{converse: angles in the same segment}]$$
Therefore:
$$D\\hat{F}C = D\\hat{E}C \\quad [\\text{angles in the same segment, subtended by chord } DC]$$

* $\\checkmark$ Statement: $EFCD$ is a cyclic quad
* $\\checkmark$ Reason: converse angles in the same segment
* $\\checkmark$ Reason: angles in the same segment""",
    final_answer="D\\hat{F}C = D\\hat{E}C"
)

# ==========================================
# QUESTION 9: Euclidean Geometry - Circle Theorems & Tangents
# ==========================================
p_q9 = """In the circle:
$O$ is the centre of the circle.
$ST$ is a tangent to the circle at $T$.
$M$ and $P$ are points on the circle such that $TM = MP$.
$OT$, $OP$, and $TP$ are drawn.
Let $\\hat{O}_1 = x$ (where $\\hat{O}_1 = T\\hat{O}P$ is the central angle subtending minor arc $TP$)."""

add_item(
    qref="9",
    marks=7,
    topic="Euclidean Geometry - Circle Theorems & Tangents",
    passage=p_q9,
    question="Prove, with reasons, that $S\\hat{T}M = \\frac{1}{4}x$.",
    memo="""$$\\hat{O}_2 = 360^\\circ - x \\quad [\\angle\\text{s round a point}]$$
$$\\hat{M} = \\frac{1}{2}\\hat{O}_2 = \\frac{1}{2}(360^\\circ - x) = 180^\\circ - \\frac{1}{2}x \\quad [\\angle \\text{ at centre } = 2 \\times \\angle \\text{ at circumference}]$$
In $\\Delta TMP$:
$$TM = MP \\implies \\hat{T}_2 = \\hat{P}_1 \\quad [\\angle\\text{s opposite equal sides}]$$
Sum of angles in $\\Delta TMP$:
$$\\hat{T}_2 + \\hat{P}_1 + \\hat{M} = 180^\\circ \\quad [\\text{sum of } \\angle\\text{s in } \\Delta]$$
$$2\\hat{P}_1 + \\left(180^\\circ - \\frac{1}{2}x\\right) = 180^\\circ$$
$$2\\hat{P}_1 = \\frac{1}{2}x \\implies \\hat{P}_1 = \\frac{1}{4}x$$
By the tangent-chord theorem (tangent $ST$ and chord $TM$):
$$S\\hat{T}M = \\hat{P}_1 = \\frac{1}{4}x \\quad [\\text{tan chord theorem}]$$

* $\\checkmark \\hat{O}_2 = 360^\\circ - x$
* $\\checkmark \\hat{M} = 180^\\circ - \\frac{1}{2}x$
* $\\checkmark$ Reason: $\\angle$ at centre $= 2 \\times \\angle$ at circumference
* $\\checkmark \\hat{T}_2 + \\hat{P}_1 = \\frac{1}{2}x$
* $\\checkmark \\hat{P}_1 = \\frac{1}{4}x$
* $\\checkmark$ Reason: $\\angle\\text{s}$ opp equal sides
* $\\checkmark$ Reason: tan chord theorem""",
    final_answer="S\\hat{T}M = \\frac{1}{4}x"
)

# ==========================================
# QUESTION 10: Euclidean Geometry - Proportionality & Similarity
# ==========================================
p_q10_1 = """In $\\Delta ABC$:
$D$ is a point on $AB$ and $E$ is a point on $AC$ such that $DE \\parallel BC$.
$BE$ and $DC$ are drawn."""

add_item(
    qref="10.1",
    marks=6,
    topic="Euclidean Geometry - Proportionality Theorem",
    passage=p_q10_1,
    question="Use the diagram to prove the theorem which states that a line drawn parallel to one side of a triangle divides the other two sides proportionally, in other words prove that $\\frac{AD}{DB} = \\frac{AE}{EC}$.",
    memo="""**Construction:**
Draw height $h_1$ from $E \\perp AB$ (or $\\perp AD$) and height $h_2$ from $D \\perp AC$ (or $\\perp AE$).

**Proof:**
$$\\frac{\\text{Area}(\\Delta ADE)}{\\text{Area}(\\Delta BDE)} = \\frac{\\frac{1}{2} AD \\times h_1}{\\frac{1}{2} DB \\times h_1} = \\frac{AD}{DB}$$
$$\\frac{\\text{Area}(\\Delta ADE)}{\\text{Area}(\\Delta DEC)} = \\frac{\\frac{1}{2} AE \\times h_2}{\\frac{1}{2} EC \\times h_2} = \\frac{AE}{EC}$$
$$\\text{Area}(\\Delta BDE) = \\text{Area}(\\Delta DEC) \\quad [\\text{same base } DE \\text{ and between same parallel lines, } DE \\parallel BC]$$
$$\\therefore \\frac{\\text{Area}(\\Delta ADE)}{\\text{Area}(\\Delta BDE)} = \\frac{\\text{Area}(\\Delta ADE)}{\\text{Area}(\\Delta DEC)}$$
$$\\therefore \\frac{AD}{DB} = \\frac{AE}{EC}$$

* $\\checkmark$ Construction: Draw $h_1$ from $E \\perp AD$ and $h_2$ from $D \\perp AE$ (or reason: common vertex / same height)
* $\\checkmark \\frac{\\text{Area}(\\Delta ADE)}{\\text{Area}(\\Delta BDE)} = \\frac{\\frac{1}{2} AD \\cdot h_1}{\\frac{1}{2} DB \\cdot h_1} = \\frac{AD}{DB}$
* $\\checkmark \\frac{\\text{Area}(\\Delta ADE)}{\\text{Area}(\\Delta DEC)} = \\frac{\\frac{1}{2} AE \\cdot h_2}{\\frac{1}{2} EC \\cdot h_2} = \\frac{AE}{EC}$
* $\\checkmark$ Statement: $\\text{Area}(\\Delta BDE) = \\text{Area}(\\Delta DEC)$
* $\\checkmark$ Reason: same base and height / between parallel lines $DE \\parallel BC$
* $\\checkmark$ Conclusion: $\\frac{AD}{DB} = \\frac{AE}{EC}$""",
    final_answer="\\frac{AD}{DB} = \\frac{AE}{EC}"
)

p_q10_2 = """In the circle:
$ST$ and $VT$ are tangents to the circle at $S$ and $V$ respectively.
$R$ is a point on the circle and $W$ is a point on chord $RS$ such that $WT$ is parallel to $RV$ ($WT \\parallel RV$).
$SV$ and $WV$ are drawn.
$WT$ intersects $SV$ at $K$.
Let $\\hat{S}_2 = x$ (where $\\hat{S}_2 = T\\hat{S}V$, the angle between tangent $ST$ and chord $SV$)."""

add_item(
    qref="10.2.1",
    marks=6,
    topic="Euclidean Geometry - Circle Theorems & Tangents",
    passage=p_q10_2,
    question="Write down, with reasons, THREE other angles EACH equal to $x$.",
    memo="""1. $\\hat{V}_3 = x \\quad [\\text{tangents from same point, } ST = VT]$
2. $\\hat{R} = x \\quad [\\text{tan chord theorem, tangent } ST \\text{ and chord } SV]$
3. $\\hat{W}_3 = x \\quad [\\text{corresponding } \\angle\\text{s}; WT \\parallel RV]$

* $\\checkmark$ Statement: $\\hat{V}_3 = x$
* $\\checkmark$ Reason: tangents from same point ($ST = VT$)
* $\\checkmark$ Statement: $\\hat{R} = x$
* $\\checkmark$ Reason: tan chord theorem
* $\\checkmark$ Statement: $\\hat{W}_3 = x$
* $\\checkmark$ Reason: corresponding $\\angle\\text{s}; WT \\parallel RV$""",
    final_answer="\\hat{V}_3 = x \\text{ (tangents from same point)}, \\hat{R} = x \\text{ (tan chord theorem)}, \\hat{W}_3 = x \\text{ (corresponding angles, } WT \\parallel RV)"
)

add_item(
    qref="10.2.2(a)",
    marks=2,
    topic="Euclidean Geometry - Circle Geometry & Quadrilaterals",
    passage=p_q10_2,
    question="Prove, with reasons, that $WSTV$ is a cyclic quadrilateral.",
    memo="""From 10.2.1:
$$\\hat{W}_3 = \\hat{V}_3 = x$$
Since line segment $ST$ subtends equal angles at vertices $W$ and $V$ on the same side:
$$\\therefore WSTV \\text{ is a cyclic quadrilateral} \\quad [\\text{converse: angles in the same segment}]$$

* $\\checkmark$ Statement: $\\hat{W}_3 = \\hat{V}_3 = x$
* $\\checkmark$ Reason: converse angles in the same segment""",
    final_answer="WSTV \\text{ is a cyclic quad (converse: angles in the same segment)}"
)

add_item(
    qref="10.2.2(b)",
    marks=4,
    topic="Euclidean Geometry - Circle Geometry & Quadrilaterals",
    passage=p_q10_2,
    question="Prove, with reasons, that $\\Delta WRV$ is isosceles.",
    memo="""In cyclic quad $WSTV$:
$$\\hat{W}_2 = \\hat{S}_2 = x \\quad [\\text{angles in the same segment, subtended by chord } TV]$$
Since $WT \\parallel RV$:
$$\\hat{V}_1 = \\hat{W}_2 = x \\quad [\\text{alternate } \\angle\\text{s}; WT \\parallel RV]$$
From 10.2.1:
$$\\hat{R} = x$$
Therefore:
$$\\hat{V}_1 = \\hat{R} = x$$
$$\\therefore WR = WV \\quad [\\text{sides opposite equal } \\angle\\text{s}]$$
$$\\therefore \\Delta WRV \\text{ is isosceles}$$

* $\\checkmark$ Statement: $\\hat{W}_2 = \\hat{S}_2 = x$
* $\\checkmark$ Reason: angles in the same segment
* $\\checkmark$ Statement & Reason: $\\hat{V}_1 = \\hat{W}_2 = x$ [alternate $\\angle\\text{s}; WT \\parallel RV$]
* $\\checkmark$ Statement: $WR = WV \\implies \\Delta WRV$ is isosceles""",
    final_answer="\\Delta WRV \\text{ is isosceles since } WR = WV \\text{ (sides opposite equal angles, } \\hat{V}_1 = \\hat{R} = x)"
)

add_item(
    qref="10.2.2(c)",
    marks=3,
    topic="Euclidean Geometry - Similarity & Proportion",
    passage=p_q10_2,
    question="Prove, with reasons, that $\\Delta WRV \\mathbin{|||} \\Delta TSV$.",
    memo="""In $\\Delta WRV$ and $\\Delta TSV$:
1. $\\hat{R} = \\hat{S}_2 = x \\quad [\\text{proved in 10.2.1 / tan chord theorem}]$
2. $\\hat{V}_1 = \\hat{V}_3 = x \\quad [\\text{proved in 10.2.1 and 10.2.2(b)}]$
3. $R\\hat{W}V = S\\hat{T}V \\quad [\\text{sum of } \\angle\\text{s in } \\Delta]$
$$\\therefore \\Delta WRV \\mathbin{|||} \\Delta TSV \\quad [\\angle, \\angle, \\angle]$$

* $\\checkmark$ Statement: $\\hat{R} = \\hat{S}_2 = x$
* $\\checkmark$ Statement: $\\hat{V}_1 = \\hat{V}_3 = x$
* $\\checkmark$ Reason: $\\angle, \\angle, \\angle$ (or third angle)""",
    final_answer="\\Delta WRV \\mathbin{|||} \\Delta TSV \\quad [\\angle, \\angle, \\angle]"
)

add_item(
    qref="10.2.2(d)",
    marks=4,
    topic="Euclidean Geometry - Similarity & Proportion",
    passage=p_q10_2,
    question="Prove, with reasons, that $\\frac{RV}{SR} = \\frac{KV}{TS}$.",
    memo="""From $\\Delta WRV \\mathbin{|||} \\Delta TSV$ in 10.2.2(c):
$$\\frac{RV}{SV} = \\frac{WR}{TS}$$
$$RV \\times TS = WR \\times SV$$

In $\\Delta SRV$, since $WT \\parallel RV$ (or $WK \\parallel RV$):
$$\\frac{WR}{SR} = \\frac{KV}{SV} \\quad [\\text{prop theorem}; WT \\parallel RV]$$
$$WR \\times SV = SR \\times KV$$

Equating the two expressions for $WR \\times SV$:
$$RV \\times TS = SR \\times KV$$
Dividing both sides by $SR \\times TS$:
$$\\frac{RV}{SR} = \\frac{KV}{TS}$$

* $\\checkmark$ correct ratio from similarity: $\\frac{RV}{SV} = \\frac{WR}{TS}$
* $\\checkmark$ proportionality theorem ratio: $\\frac{WR}{SR} = \\frac{KV}{SV}$
* $\\checkmark$ Reason: prop theorem; $WT \\parallel RV$
* $\\checkmark$ equating $WR \\times SV$ and concluding $\\frac{RV}{SR} = \\frac{KV}{TS}$""",
    final_answer="\\frac{RV}{SR} = \\frac{KV}{TS}"
)

# ==========================================
# VALIDATION & DUAL OUTPUT WRITING
# ==========================================
total_marks = sum(item["marks"] for item in items)
print(f"Total items: {len(items)}")
print(f"Total marks: {total_marks} (Expected: 150)")
assert total_marks == 150, f"Total marks mismatch: got {total_marks}, expected 150"

# Verify KaTeX dollar balancing
for item in items:
    for field in ["passage", "question", "memo", "final_answer"]:
        text = item[field]
        # Count dollars not preceded by backslash
        dollars = re.findall(r'(?<!\\)\$', text)
        if len(dollars) % 2 != 0:
            raise ValueError(f"Unbalanced $ in {item['item_id']} field {field}: found {len(dollars)} $ signs.")

print("All KaTeX dollar delimiters are perfectly balanced!")

# Dual output paths
out_path_sub = "workspace/items/mathematics/dbe-mathematics-g12-p2-2019-nov.jsonl"
out_path_root = "workspace/items/dbe-mathematics-g12-p2-2019-nov.jsonl"

os.makedirs(os.path.dirname(out_path_sub), exist_ok=True)
os.makedirs(os.path.dirname(out_path_root), exist_ok=True)

with open(out_path_sub, "w", encoding="utf-8") as f_sub, open(out_path_root, "w", encoding="utf-8") as f_root:
    for item in items:
        line = json.dumps(item, ensure_ascii=False) + "\n"
        f_sub.write(line)
        f_root.write(line)

print(f"Successfully written {len(items)} items to:")
print(f"  - {out_path_sub}")
print(f"  - {out_path_root}")
