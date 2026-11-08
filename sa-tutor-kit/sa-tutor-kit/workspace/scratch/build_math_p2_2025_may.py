# build_math_p2_2025_may.py
import json
import re
import os

items = []

# ==========================================
# QUESTION 1
# ==========================================
q1_passage = """An insurance broker signed contracts with 15 people. The monthly premium (in rands) payable on each contract is given below.

$$\\begin{array}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\\hline
134 & 215 & 325 & 326 & 362 & 429 & 515 & 531 & 598 & 610 & 624 & 728 & 923 & 1\\,034 & 1\\,200 \\\\
\\hline
\\end{array}$$"""

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-1.1",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "1.1",
    "marks": 2,
    "topic": "Statistics - Mean",
    "passage": q1_passage,
    "question": "Calculate the mean of the data.",
    "memo": """$$\\bar{x} = \\frac{8\\,554}{15}$$
$$= 570{,}27$$

* $\\checkmark 8\\,554$
* $\\checkmark \\text{answer}$""",
    "final_answer": "570.27",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-1.2",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "1.2",
    "marks": 1,
    "topic": "Statistics - Standard Deviation",
    "passage": q1_passage,
    "question": "Write down the standard deviation of the data.",
    "memo": """$$\\sigma = 291{,}03$$

* $\\checkmark 291{,}03$""",
    "final_answer": "291.03",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-1.3",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "1.3",
    "marks": 2,
    "topic": "Statistics - Normal Distribution & Spread",
    "passage": q1_passage,
    "question": "Calculate how many monthly premiums are within ONE standard deviation of the mean.",
    "memo": """$$(\\bar{x} - \\sigma ; \\bar{x} + \\sigma) = (570{,}27 - 291{,}03 ; 570{,}27 + 291{,}03) = (279{,}24 ; 861{,}30)$$
$$\\therefore 10 \\text{ premiums}$$

* $\\checkmark (\\bar{x} - \\sigma ; \\bar{x} + \\sigma)$
* $\\checkmark \\text{answer}$""",
    "final_answer": "10",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-1.4",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "1.4",
    "marks": 4,
    "topic": "Statistics - Mean & Percentage Increase",
    "passage": q1_passage,
    "question": """The insurance company decided to increase the monthly premiums.
* Monthly premiums that were less than $\\text{R}500$ increased by $18\\%$
* Monthly premiums that were equal to or more than $\\text{R}500$ increased by $k\\%$

After these increases were applied to the above data, the new mean monthly premium was $\\text{R}686{,}44$. Calculate the value of $k$.""",
    "memo": """$$\\frac{1\\,791 \\times \\frac{118}{100} + 6\\,763 \\times \\frac{k + 100}{100}}{15} = 686{,}44$$
$$6\\,763 \\times \\frac{k + 100}{100} = 8\\,183{,}22$$
$$\\frac{k + 100}{100} = 1{,}2099985\\dots$$
$$k + 100 = 120{,}99985\\dots$$
$$k = 21\\%$$

* $\\checkmark 1\\,791 \\times \\frac{118}{100}$
* $\\checkmark 6\\,763 \\times \\frac{k + 100}{100}$
* $\\checkmark \\frac{\\text{sum of new premiums}}{15} = 686{,}44$
* $\\checkmark \\text{answer } (k = 21\\%)$""",
    "final_answer": "21",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

# ==========================================
# QUESTION 2
# ==========================================
q2_passage = """The manager of a supermarket decided to do a survey on the number of items that a customer ordered online and the time (in minutes) that a packer took to have the order ready for delivery. The supermarket received 10 online orders on a certain day. The information for these 10 orders is shown in the table below.

| Number of items ($x$) | 10 | 3 | 20 | 14 | 17 | 9 | 12 | 18 | 15 | 19 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Time (in minutes) ($y$) | 5 | 5 | 9 | 7 | 6 | 6 | 8 | 11 | 10 | 12 |"""

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-2.1",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "2.1",
    "marks": 3,
    "topic": "Statistics - Scatter Plot",
    "passage": q2_passage + "\n\n[DIAGRAM: Statistics Scatter Plot | Time (in minutes) on y-axis (scale 0 to 14) vs Number of items on x-axis (scale 0 to 25) | 10 data points plotted: (10, 5), (3, 5), (20, 9), (14, 7), (17, 6), (9, 6), (12, 8), (18, 11), (15, 10), (19, 12)]",
    "question": "Draw a scatter plot on the grid provided in the ANSWER BOOK.",
    "memo": """Plotted points on Cartesian grid with Number of items ($x$) on horizontal axis and Time in minutes ($y$) on vertical axis:
$$(10 ; 5), (3 ; 5), (20 ; 9), (14 ; 7), (17 ; 6), (9 ; 6), (12 ; 8), (18 ; 11), (15 ; 10), (19 ; 12)$$

* $\\checkmark 3\\text{ points correctly plotted}$
* $\\checkmark 6\\text{ points correctly plotted}$
* $\\checkmark \\text{all 10 points correctly plotted}$""",
    "final_answer": "Scatter plot drawn with 10 points",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-2.2",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "2.2",
    "marks": 3,
    "topic": "Statistics - Least Squares Regression Line",
    "passage": q2_passage,
    "question": "Determine the equation of the least squares regression line.",
    "memo": """$$a = 3{,}079\\dots \\approx 3{,}08$$
$$b = 0{,}351\\dots \\approx 0{,}35$$
$$\\hat{y} = 3{,}08 + 0{,}35x \\quad\\text{or}\\quad \\hat{y} = 0{,}35x + 3{,}08$$

* $\\checkmark a = 3{,}08$
* $\\checkmark b = 0{,}35$
* $\\checkmark \\text{equation}$""",
    "final_answer": "y = 0.35x + 3.08",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-2.3",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "2.3",
    "marks": 1,
    "topic": "Statistics - Correlation Coefficient",
    "passage": q2_passage,
    "question": "Write down the correlation coefficient of the data.",
    "memo": """$$r = 0{,}74$$

* $\\checkmark 0{,}74$""",
    "final_answer": "0.74",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-2.4",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "2.4",
    "marks": 2,
    "topic": "Statistics - Bivariate Prediction",
    "passage": q2_passage,
    "question": "The supermarket received an online order for 13 items. Predict how long (in minutes) it will take a packer to pack the order and have it ready for delivery.",
    "memo": """$$\\hat{y} = 3{,}08 + 0{,}35(13)$$
$$\\hat{y} = 7{,}63\\text{ minutes}$$

* $\\checkmark \\text{substitute } x = 13$
* $\\checkmark \\text{answer } (7{,}63)$

OR/OF

$$\\hat{y} = 7{,}65\\text{ minutes (using unrounded calculator regression coefficients)}$$

* $\\checkmark\\checkmark 7{,}65$""",
    "final_answer": "7.63",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-2.5",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "2.5",
    "marks": 1,
    "topic": "Statistics - Interpretation of Regression Line",
    "passage": q2_passage,
    "question": "Explain why the $y$-intercept of the least squares regression line in QUESTION 2.2 does NOT make sense in this context.",
    "memo": """It does not make sense to pack 0 items in $3{,}08$ minutes / If no items are ordered ($x = 0$), no packing time ($y = 0$) should be required.

* $\\checkmark \\text{valid reason}$""",
    "final_answer": "Packing 0 items should take 0 minutes, not 3.08 minutes.",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

# ==========================================
# QUESTION 3
# ==========================================
q3_passage = """[DIAGRAM: Analytical Geometry | Triangle SRT in Cartesian plane | R lies on the negative x-axis; T lies on the positive y-axis; S(m; 1) lies in the second quadrant to the left of R with y-coordinate 1; Line RT has equation 2x - y + 10 = 0; Point V lies on line segment ST such that VR is perpendicular to ST (VR ⊥ ST); Origin O is at (0; 0)]

In the diagram below, $\\Delta\\text{SRT}$ is drawn where $R$ lies on the $x$-axis and $S$ lies to the left of $R$. $T$ lies on the $y$-axis and the coordinates of $S$ are $(m ; 1)$. The equation of $RT$ is $2x - y + 10 = 0$."""

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-3.1",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "3.1",
    "marks": 2,
    "topic": "Analytical Geometry - Intercepts",
    "passage": q3_passage,
    "question": "Calculate the coordinates of $R$.",
    "memo": """$$2x - y + 10 = 0$$
$$2x - (0) + 10 = 0$$
$$2x = -10$$
$$x = -5$$
$$R(-5 ; 0)$$

* $\\checkmark y = 0$
* $\\checkmark x = -5$""",
    "final_answer": "R(-5, 0)",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-3.2",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "3.2",
    "marks": 3,
    "topic": "Analytical Geometry - Distance Formula",
    "passage": q3_passage,
    "question": "Calculate the length of $RT$. Leave your answer in surd form.",
    "memo": """$$R(-5 ; 0)$$
$$T(0 ; 10)$$

$$RT^2 = (-5 - 0)^2 + (0 - 10)^2 \\quad\\text{or}\\quad RT^2 = 5^2 + 10^2 \\quad [\\text{Pythagoras}]$$
$$RT = \\sqrt{125}\\text{ units} \\quad\\text{OR/OF}\\quad RT = 5\\sqrt{5}\\text{ units}$$

* $\\checkmark T(0 ; 10)$
* $\\checkmark \\text{substitution of } R \\text{ and } T \\text{ into distance formula or Pythagoras}$
* $\\checkmark \\text{answer } (\\sqrt{125} \\text{ or } 5\\sqrt{5})$""",
    "final_answer": "sqrt(125)",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-3.3",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "3.3",
    "marks": 4,
    "topic": "Analytical Geometry - Distance & Algebra",
    "passage": q3_passage,
    "question": "If it is also given that $2\\text{RT}^2 = 5\\text{SR}^2$, calculate the value of $m$.",
    "memo": """$$2RT^2 = 5SR^2$$
$$2(125) = 5[((m - (-5))^2 + (1 - 0)^2)]$$
$$250 = 5[(m + 5)^2 + 1]$$
$$50 = (m + 5)^2 + 1$$
$$(m + 5)^2 = 49$$
$$m + 5 = \\pm 7$$
$$m = -5 \\pm 7$$
$$m = 2 \\quad\\text{or}\\quad m = -12$$
Since $S$ lies to the left of $R(-5 ; 0)$, $m < -5$:
$$\\therefore m = -12 \\quad (m = 2 \\text{ is N/A})$$

OR/OF

$$(m + 5)^2 - 49 = 0$$
$$m^2 + 10m + 25 - 49 = 0$$
$$m^2 + 10m - 24 = 0$$
$$(m - 2)(m + 12) = 0$$
$$m = 2 \\quad\\text{or}\\quad m = -12$$
$$\\therefore m = -12$$

* $\\checkmark 2RT^2 = 250$
* $\\checkmark 5SR^2 = 5[(m + 5)^2 + 1]$
* $\\checkmark \\text{standard form } (m^2 + 10m - 24 = 0) \\text{ or isolating square } ((m+5)^2 = 49)$
* $\\checkmark \\text{negative answer } (m = -12)$""",
    "final_answer": "-12",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-3.4",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "3.4",
    "marks": 5,
    "topic": "Analytical Geometry - Perpendicular Lines",
    "passage": q3_passage,
    "question": "It is further given that $V$ lies on $ST$ such that $VR$ is perpendicular to $ST$. Determine the equation of $VR$ in the form $y = mx + c$.",
    "memo": """$$m_{ST} = \\frac{1 - 10}{-12 - 0} = \\frac{-9}{-12} = \\frac{3}{4}$$
$$m_{VR} \\times m_{ST} = -1 \\implies m_{VR} = -\\frac{4}{3}$$
$$y - y_1 = m(x - x_1)$$
$$y - 0 = -\\frac{4}{3}(x - (-5)) \\quad\\text{OR/OF}\\quad 0 = -\\frac{4}{3}(-5) + c$$
$$c = -\\frac{20}{3}$$
$$y = -\\frac{4}{3}x - \\frac{20}{3}$$

* $\\checkmark \\text{substitution of } S(-12 ; 1) \\text{ and } T(0 ; 10) \\text{ into gradient formula}$
* $\\checkmark m_{ST} = \\frac{3}{4}$
* $\\checkmark m_{VR} = -\\frac{4}{3}$
* $\\checkmark \\text{substitution of } R(-5 ; 0)$
* $\\checkmark \\text{equation: } y = -\\frac{4}{3}x - \\frac{20}{3}$""",
    "final_answer": "y = -4/3x - 20/3",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-3.5",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "3.5",
    "marks": 2,
    "topic": "Analytical Geometry - Simultaneous Equations",
    "passage": q3_passage,
    "question": "Hence, show that the coordinates of $V$ are $(-8 ; 4)$.",
    "memo": """Equation of $VR$: $y = -\\frac{4}{3}x - \\frac{20}{3}$
Equation of $ST$: $y = \\frac{3}{4}x + 10$

$$\\frac{3}{4}x + 10 = -\\frac{4}{3}x - \\frac{20}{3}$$
$$9x + 120 = -16x - 80$$
$$25x = -200$$
$$x = -8$$
$$y = \\frac{3}{4}(-8) + 10 = -6 + 10 = 4$$
$$\\therefore V(-8 ; 4)$$

* $\\checkmark \\text{equating } VR \\text{ and } ST$
* $\\checkmark \\text{simplification leading to } x = -8 \\implies V(-8 ; 4)$""",
    "final_answer": "(-8, 4)",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-3.6",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "3.6",
    "marks": 5,
    "topic": "Analytical Geometry - Area of Polygon",
    "passage": q3_passage,
    "question": "If $R'$ is the reflection of $R$ about the line $x = 0$, calculate the area of $\\text{RVTR}'$.",
    "memo": """$$R' (5 ; 0)$$

$$VR = \\sqrt{(-8 - (-5))^2 + (4 - 0)^2} = \\sqrt{(-3)^2 + 4^2} = 5\\text{ units}$$
$$VT = \\sqrt{(-8 - 0)^2 + (4 - 10)^2} = \\sqrt{(-8)^2 + (-6)^2} = 10\\text{ units}$$

$$\\text{Area of } RVTR' = \\text{Area } \\Delta VRT + \\text{Area } \\Delta R'RT$$
$$= \\frac{1}{2}VR \\cdot VT + \\frac{1}{2}RR' \\cdot OT$$
$$= \\frac{1}{2}(5)(10) + \\frac{1}{2}(10)(10)$$
$$= 25 + 50 = 75\\text{ units}^2$$

OR/OF

Line $ST$: $y = \\frac{3}{4}x + 10$.
When $y = 0$: $\\frac{3}{4}x + 10 = 0 \\implies x = -\\frac{40}{3}$.
Let $W\\left(-\\frac{40}{3} ; 0\\right)$ be the $x$-intercept of $ST$.
$$WR' = 5 - \\left(-\\frac{40}{3}\\right) = \\frac{55}{3}$$
$$\\text{Area of } RVTR' = \\text{Area } \\Delta TWR' - \\text{Area } \\Delta WVR$$
$$= \\frac{1}{2}\\left(\\frac{55}{3}\\right)(10) - \\frac{1}{2}\\left(-\\frac{40}{3} - (-5)\\right)(4)$$
$$= \\frac{275}{3} - \\frac{1}{2}\\left(\\frac{25}{3}\\right)(4) = \\frac{275}{3} - \\frac{50}{3} = \\frac{225}{3} = 75\\text{ units}^2$$

* $\\checkmark \\text{length of } VR = 5$
* $\\checkmark \\text{length of } VT = 10$
* $\\checkmark \\text{area } \\Delta VRT = 25$
* $\\checkmark \\text{area } \\Delta R'RT = 50$
* $\\checkmark \\text{answer: } 75\\text{ units}^2$""",
    "final_answer": "75",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

# ==========================================
# QUESTION 4
# ==========================================
q4_passage = """[DIAGRAM: Analytical Geometry | Circle and Tangent in Cartesian Plane | Circle centre M on positive x-axis with equation (x - 3)^2 + y^2 = 25; Point E(-1; 3) and point T lie on the circle; Tangent EC touches circle at E and intersects the negative x-axis at D; ED = 15/4 units; Secant MT is produced past T to intersect the tangent at C(-7; p); Origin O is at (0; 0)]

In the diagram, $M$ is the centre of the circle having equation $(x - 3)^2 + y^2 = 25$. $E(-1 ; 3)$ and $T$ are points on the circle. $EC$ is a tangent to the circle at $E$ and cuts the $x$-axis at $D$. $\\text{ED} = \\frac{15}{4}\\text{ units}$. $MT$ is produced to meet the tangent at $C(-7 ; p)$."""

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-4.1",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "4.1",
    "marks": 1,
    "topic": "Analytical Geometry - Tangent to Circle",
    "passage": q4_passage,
    "question": "Write down the size of $\\text{C}\\hat{\\text{E}}\\text{M}$.",
    "memo": """$$\\text{C}\\hat{\\text{E}}\\text{M} = 90^\\circ \\quad [\\text{tangent } \\perp \\text{ radius}]$$

* $\\checkmark 90^\\circ$""",
    "final_answer": "90°",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-4.2",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "4.2",
    "marks": 4,
    "topic": "Analytical Geometry - Equation of Tangent",
    "passage": q4_passage,
    "question": "Determine the equation of the tangent $EC$ in the form $y = mx + c$.",
    "memo": """$$M(3 ; 0), \\quad E(-1 ; 3)$$
$$m_{ME} = \\frac{3 - 0}{-1 - 3} = -\\frac{3}{4}$$
$$m_{ED} = m_{EC} = \\frac{4}{3} \\quad [\\text{radius } \\perp \\text{ tangent}]$$

$$y - 3 = \\frac{4}{3}(x - (-1)) \\quad\\text{OR/OF}\\quad 3 = \\frac{4}{3}(-1) + c$$
$$c = \\frac{13}{3}$$
$$y = \\frac{4}{3}x + \\frac{13}{3}$$

OR/OF

$$DM^2 = 5^2 + \\left(\\frac{15}{4}\\right)^2 = \\frac{625}{16} \\implies DM = \\frac{25}{4} = 6{,}25\\text{ units} \\quad [\\text{Pythagoras}]$$
$$D\\left(-\\frac{13}{4} ; 0\\right)$$
$$m_{ED} = \\frac{3 - 0}{-1 - (-\\frac{13}{4})} = \\frac{3}{\\frac{9}{4}} = \\frac{4}{3}$$
$$y = \\frac{4}{3}x + \\frac{13}{3}$$

* $\\checkmark m_{ME} = -\\frac{3}{4}$ (or coordinates of $D$)
* $\\checkmark m_{ED} = \\frac{4}{3}$
* $\\checkmark \\text{substitution of } E(-1 ; 3)$
* $\\checkmark \\text{equation: } y = \\frac{4}{3}x + \\frac{13}{3}$""",
    "final_answer": "y = 4/3x + 13/3",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-4.3",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "4.3",
    "marks": 3,
    "topic": "Analytical Geometry - Distance & Pythagoras",
    "passage": q4_passage,
    "question": "Calculate the length of $DM$.",
    "memo": """$$y = \\frac{4}{3}x + \\frac{13}{3}$$
$$0 = \\frac{4}{3}x_D + \\frac{13}{3} \\implies x_D = -\\frac{13}{4}$$
$$DM = x_M - x_D = 3 - \\left(-\\frac{13}{4}\\right) = \\frac{25}{4} = 6{,}25\\text{ units}$$

OR/OF

$$EM = 5\\text{ units}, \\quad ED = \\frac{15}{4}\\text{ units}$$
$$DM^2 = 5^2 + \\left(\\frac{15}{4}\\right)^2 = 25 + \\frac{225}{16} = \\frac{625}{16} \\quad [\\text{Pythagoras}]$$
$$DM = \\frac{25}{4} = 6{,}25\\text{ units}$$

* $\\checkmark x_D = -\\frac{13}{4}$ (or $EM = 5\\text{ units}$)
* $\\checkmark x_M - x_D$ (or substitution of $EM$ and $ED$ into Pythagoras)
* $\\checkmark \\text{answer: } \\frac{25}{4} \\text{ or } 6{,}25\\text{ units}$""",
    "final_answer": "6.25",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-4.4",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "4.4",
    "marks": 1,
    "topic": "Analytical Geometry - Coordinates on Line",
    "passage": q4_passage,
    "question": "Show that $p = -5$.",
    "memo": """Equation of $EC$: $y = \\frac{4}{3}x + \\frac{13}{3}$
$$p = \\frac{4}{3}(-7) + \\frac{13}{3} = -\\frac{28}{3} + \\frac{13}{3} = -\\frac{15}{3} = -5$$

OR/OF

$$m_{EC} = \\frac{4}{3}$$
$$\\frac{p - 3}{-7 - (-1)} = \\frac{4}{3}$$
$$\\frac{p - 3}{-6} = \\frac{4}{3}$$
$$3(p - 3) = -24 \\implies p - 3 = -8 \\implies p = -5$$

* $\\checkmark \\text{substitution of } C(-7 ; p) \\text{ into equation or gradient of } EC$""",
    "final_answer": "-5",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-4.5",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "4.5",
    "marks": 3,
    "topic": "Analytical Geometry - Parallelogram Properties",
    "passage": q4_passage,
    "question": "Calculate the coordinates of $S$ if $\\text{SEMC}$ is a parallelogram and $x_S < 0$.",
    "memo": """Method 1 (Translation):
$$M(3 ; 0) \\to E(-1 ; 3): (x ; y) \\to (x - 4 ; y + 3)$$
$$C(-7 ; -5) \\to S: (-7 - 4 ; -5 + 3)$$
$$\\therefore S(-11 ; -2)$$

OR/OF

$$M(3 ; 0) \\to C(-7 ; -5): (x ; y) \\to (x - 10 ; y - 5)$$
$$E(-1 ; 3) \\to S: (-1 - 10 ; 3 - 5)$$
$$\\therefore S(-11 ; -2)$$

OR/OF

Method 2 (Midpoint of diagonals):
Midpoint of $EC$:
$$\\left(\\frac{-1 + (-7)}{2} ; \\frac{3 + (-5)}{2}\\right) = (-4 ; -1)$$
Since $M_{EC}$ is also the midpoint of $SM$, with $M(3 ; 0)$:
$$\\frac{x_S + 3}{2} = -4 \\implies x_S = -11$$
$$\\frac{y_S + 0}{2} = -1 \\implies y_S = -2$$
$$\\therefore S(-11 ; -2)$$

* $\\checkmark \\text{method (translation or midpoint)}$
* $\\checkmark x_S = -11$
* $\\checkmark y_S = -2$""",
    "final_answer": "S(-11, -2)",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-4.6",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "4.6",
    "marks": 3,
    "topic": "Analytical Geometry - Distance & Circle Radius",
    "passage": q4_passage,
    "question": "If the radius of the circle, centred at $M$, is increased by $7$ units, determine whether $S$ lies inside or outside the new circle. Support your answer with the necessary calculations.",
    "memo": """$$r_{\\text{new}} = 5 + 7 = 12\\text{ units}$$
$$MS^2 = (3 - (-11))^2 + (0 - (-2))^2 = 14^2 + 2^2 = 196 + 4 = 200$$
$$MS = \\sqrt{200} = 10\\sqrt{2} \\approx 14{,}14\\text{ units}$$
$$14{,}14 > 12$$
$$\\therefore S(-11 ; -2) \\text{ lies outside the new circle.}$$

* $\\checkmark r_{\\text{new}} = 12$
* $\\checkmark MS = \\sqrt{200} \\text{ or } 10\\sqrt{2} \\text{ or } 14{,}14$
* $\\checkmark \\text{conclusion: } S \\text{ lies outside the circle}$""",
    "final_answer": "Outside",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-4.7",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "4.7",
    "marks": 5,
    "topic": "Analytical Geometry - Angles & Inclination",
    "passage": q4_passage,
    "question": "If $ET$ is drawn, calculate the size of $\\text{E}\\hat{\\text{T}}\\text{M}$.",
    "memo": """Inclination of $EM$:
$$\\tan\\theta_{EM} = m_{ME} = -\\frac{3}{4} \\implies \\text{ref } \\angle = 36{,}87^\\circ$$
$$\\text{Inclination of } EM = 180^\\circ - 36{,}87^\\circ = 143{,}13^\\circ$$
$$\\therefore \\text{D}\\hat{\\text{M}}\\text{E} = 36{,}87^\\circ$$

Inclination of $CM$:
$$\\tan\\theta_{CM} = m_{CM} = \\frac{0 - (-5)}{3 - (-7)} = \\frac{5}{10} = \\frac{1}{2}$$
$$\\theta_{CM} = 26{,}57^\\circ$$

Angle at centre $\\text{E}\\hat{\\text{M}}\\text{T}$:
$$\\text{E}\\hat{\\text{M}}\\text{T} = 26{,}57^\\circ + 36{,}87^\\circ = 63{,}44^\\circ$$

In $\\Delta MET$, $EM = MT = 5$ (radii):
$$\\text{E}\\hat{\\text{T}}\\text{M} = \\frac{180^\\circ - 63{,}44^\\circ}{2} = \\frac{116{,}56^\\circ}{2} = 58{,}28^\\circ$$

* $\\checkmark \\text{inclination of } EM$
* $\\checkmark \\text{D}\\hat{\\text{M}}\\text{E} = 36{,}87^\\circ$
* $\\checkmark \\text{inclination of } CM = 26{,}57^\\circ$
* $\\checkmark \\text{E}\\hat{\\text{M}}\\text{T} = 63{,}44^\\circ$
* $\\checkmark \\text{E}\\hat{\\text{T}}\\text{M} = 58{,}28^\\circ$""",
    "final_answer": "58.28°",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

# ==========================================
# QUESTION 5
# ==========================================
q5_1_passage = "If $\\cos\\theta = -\\frac{5}{13}$ where $180^\\circ < \\theta < 360^\\circ$, determine, without using a calculator, the value of:"

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-5.1.1",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "5.1.1",
    "marks": 3,
    "topic": "Trigonometry - Cartesian Plane & Identities",
    "passage": q5_1_passage,
    "question": "$\\sin^2\\theta$",
    "memo": """$$y^2 = 13^2 - (-5)^2 = 144 \\implies y = -12 \\quad [\\text{Pythagoras in QIII}]$$
$$\\sin^2\\theta = \\left(-\\frac{12}{13}\\right)^2 = \\frac{144}{169}$$

OR/OF

$$\\sin^2\\theta = 1 - \\cos^2\\theta$$
$$= 1 - \\left(-\\frac{5}{13}\\right)^2 = 1 - \\frac{25}{169} = \\frac{144}{169}$$

* $\\checkmark y = -12$ (or square identity)
* $\\checkmark \\text{substitution}$
* $\\checkmark \\text{answer } \\left(\\frac{144}{169}\\right)$""",
    "final_answer": "144/169",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-5.1.2",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "5.1.2",
    "marks": 2,
    "topic": "Trigonometry - Reduction Formulae",
    "passage": q5_1_passage,
    "question": "$\\tan(360^\\circ - \\theta)$",
    "memo": """$$\\tan(360^\\circ - \\theta) = -\\tan\\theta$$
$$= -\\left(\\frac{-12}{-5}\\right) = -\\frac{12}{5}$$

* $\\checkmark -\\tan\\theta$
* $\\checkmark \\text{answer } \\left(-\\frac{12}{5}\\right)$""",
    "final_answer": "-12/5",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-5.1.3",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "5.1.3",
    "marks": 4,
    "topic": "Trigonometry - Compound Angles",
    "passage": q5_1_passage,
    "question": "$\\cos(\\theta - 135^\\circ)$",
    "memo": """$$\\cos(\\theta - 135^\\circ) = \\cos\\theta\\cos 135^\\circ + \\sin\\theta\\sin 135^\\circ$$
$$= \\cos\\theta(-\\cos 45^\\circ) + \\sin\\theta(\\sin 45^\\circ)$$
$$= \\left(-\\frac{5}{13}\\right)\\left(-\\frac{\\sqrt{2}}{2}\\right) + \\left(-\\frac{12}{13}\\right)\\left(\\frac{\\sqrt{2}}{2}\\right) \\quad\\text{OR}\\quad \\left(-\\frac{5}{13}\\right)\\left(-\\frac{1}{\\sqrt{2}}\\right) + \\left(-\\frac{12}{13}\\right)\\left(\\frac{1}{\\sqrt{2}}\\right)$$
$$= \\frac{5\\sqrt{2}}{26} - \\frac{12\\sqrt{2}}{26} = -\\frac{7\\sqrt{2}}{26} \\quad\\text{OR}\\quad -\\frac{7}{13\\sqrt{2}}$$

* $\\checkmark \\text{compound angle expansion}$
* $\\checkmark \\text{reduction: } -\\cos 45^\\circ \\text{ and } \\sin 45^\\circ$
* $\\checkmark \\text{substitution of values}$
* $\\checkmark \\text{answer: } -\\frac{7\\sqrt{2}}{26} \\text{ or } -\\frac{7}{13\\sqrt{2}}$""",
    "final_answer": "-7*sqrt(2)/26",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-5.2",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "5.2",
    "marks": 6,
    "topic": "Trigonometry - Simplification & Double Angles",
    "passage": "",
    "question": "Simplify the expression to a single trigonometric term:\n$$\\frac{2\\cos(180^\\circ - x)\\sin(-x)}{1 - 2\\cos^2(90^\\circ - x)}$$",
    "memo": """$$\\frac{2\\cos(180^\\circ - x)\\sin(-x)}{1 - 2\\cos^2(90^\\circ - x)}$$
$$= \\frac{2(-\\cos x)(-\\sin x)}{1 - 2\\sin^2 x}$$
$$= \\frac{2\\sin x\\cos x}{\\cos 2x}$$
$$= \\frac{\\sin 2x}{\\cos 2x}$$
$$= \\tan 2x$$

* $\\checkmark \\cos(180^\\circ - x) = -\\cos x$
* $\\checkmark \\sin(-x) = -\\sin x$
* $\\checkmark \\cos^2(90^\\circ - x) = \\sin^2 x$
* $\\checkmark 1 - 2\\sin^2 x = \\cos 2x$
* $\\checkmark 2\\sin x\\cos x = \\sin 2x$
* $\\checkmark \\text{answer: } \\tan 2x$""",
    "final_answer": "tan(2x)",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-5.3",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "5.3",
    "marks": 4,
    "topic": "Trigonometry - Product of Tangents & Co-functions",
    "passage": "",
    "question": "Calculate the value of the following expression without using a calculator:\n$$(\\tan 92^\\circ)(\\tan 94^\\circ)(\\tan 96^\\circ) \\dots (\\tan 176^\\circ)(\\tan 178^\\circ)$$",
    "memo": """$$(\\tan 92^\\circ)(\\tan 94^\\circ)(\\tan 96^\\circ) \\dots (\\tan 176^\\circ)(\\tan 178^\\circ)$$
$$= \\left(\\frac{\\sin 92^\\circ}{\\cos 92^\\circ}\\right)\\left(\\frac{\\sin 94^\\circ}{\\cos 94^\\circ}\\right)\\dots\\left(\\frac{\\sin 176^\\circ}{\\cos 176^\\circ}\\right)\\left(\\frac{\\sin 178^\\circ}{\\cos 178^\\circ}\\right)$$
$$= \\left(\\frac{\\cos 2^\\circ}{-\\sin 2^\\circ}\\right)\\left(\\frac{\\cos 4^\\circ}{-\\sin 4^\\circ}\\right)\\dots\\left(\\frac{\\sin 4^\\circ}{-\\cos 4^\\circ}\\right)\\left(\\frac{\\sin 2^\\circ}{-\\cos 2^\\circ}\\right)$$
$$= 1$$

OR/OF

$$(\\tan 92^\\circ)(\\tan 94^\\circ)(\\tan 96^\\circ) \\dots (\\tan 176^\\circ)(\\tan 178^\\circ)$$
$$= (\\tan 92^\\circ)(\\tan 94^\\circ)\\dots(-\\tan 4^\\circ)(-\\tan 2^\\circ)$$
$$= \\left(\\frac{\\sin 92^\\circ}{\\cos 92^\\circ}\\right)\\left(\\frac{\\sin 94^\\circ}{\\cos 94^\\circ}\\right)\\dots\\left(-\\frac{\\sin 4^\\circ}{\\cos 4^\\circ}\\right)\\left(-\\frac{\\sin 2^\\circ}{\\cos 2^\\circ}\\right)$$
$$= \\left(\\frac{\\cos 2^\\circ}{-\\sin 2^\\circ}\\right)\\left(\\frac{\\cos 4^\\circ}{-\\sin 4^\\circ}\\right)\\dots\\left(-\\frac{\\sin 4^\\circ}{\\cos 4^\\circ}\\right)\\left(-\\frac{\\sin 2^\\circ}{\\cos 2^\\circ}\\right)$$
$$= 1$$

* $\\checkmark \\text{quotient identity (or reduction)}$
* $\\checkmark \\text{co-ratios } (\\sin 92^\\circ = \\cos 2^\\circ \\text{ etc.})$
* $\\checkmark \\text{reduction of second half}$
* $\\checkmark \\text{answer: } 1$""",
    "final_answer": "1",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

# ==========================================
# QUESTION 6
# ==========================================
items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-6.1",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "6.1",
    "marks": 4,
    "topic": "Trigonometry - Identities & Double Angles",
    "passage": "",
    "question": "Prove that $2\\cos^2(45^\\circ + x) = 1 - \\sin 2x$.",
    "memo": """$$\\text{LHS} = 2\\cos^2(45^\\circ + x)$$
$$= [2\\cos^2(45^\\circ + x) - 1] + 1$$
$$= \\cos(2(45^\\circ + x)) + 1$$
$$= \\cos(90^\\circ + 2x) + 1$$
$$= -\\sin 2x + 1$$
$$= 1 - \\sin 2x = \\text{RHS}$$

OR/OF

$$\\text{LHS} = 2[\\cos(45^\\circ + x)]^2$$
$$= 2[\\cos 45^\\circ\\cos x - \\sin 45^\\circ\\sin x]^2$$
$$= 2\\left[\\frac{\\sqrt{2}}{2}\\cos x - \\frac{\\sqrt{2}}{2}\\sin x\\right]^2$$
$$= 2\\left(\\frac{1}{2}\\cos^2 x - \\sin x\\cos x + \\frac{1}{2}\\sin^2 x\\right)$$
$$= \\cos^2 x - 2\\sin x\\cos x + \\sin^2 x$$
$$= 1 - \\sin 2x = \\text{RHS}$$

* $\\checkmark +1 - 1$ (or compound angle expansion)
* $\\checkmark \\text{double angle } (\\cos(90^\\circ + 2x)) \\text{ or subst special angle } 45^\\circ$
* $\\checkmark \\text{simplification}$
* $\\checkmark \\text{reduction: } \\cos(90^\\circ + 2x) = -\\sin 2x \\text{ (or } \\cos^2 x + \\sin^2 x = 1)$""",
    "final_answer": "1 - sin(2x)",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

q6_2_passage = "Consider the expression: $\\sin(A - B) - \\sin(A + B)$"

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-6.2.1",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "6.2.1",
    "marks": 2,
    "topic": "Trigonometry - Compound Angle Identities",
    "passage": q6_2_passage,
    "question": "Prove that $\\sin(A - B) - \\sin(A + B) = -2\\cos A \\sin B$.",
    "memo": """$$\\text{LHS} = \\sin(A - B) - \\sin(A + B)$$
$$= (\\sin A\\cos B - \\cos A\\sin B) - (\\sin A\\cos B + \\cos A\\sin B)$$
$$= \\sin A\\cos B - \\cos A\\sin B - \\sin A\\cos B - \\cos A\\sin B$$
$$= -2\\cos A\\sin B = \\text{RHS}$$

* $\\checkmark \\sin A\\cos B - \\cos A\\sin B$
* $\\checkmark -\\sin A\\cos B - \\cos A\\sin B$""",
    "final_answer": "-2*cos(A)*sin(B)",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-6.2.2",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "6.2.2",
    "marks": 2,
    "topic": "Trigonometry - Sum to Product Conversion",
    "passage": q6_2_passage,
    "question": "Simplify the following expression to a single term: $\\sin 4x - \\sin 10x$",
    "memo": """$$\\sin 4x - \\sin 10x = \\sin(7x - 3x) - \\sin(7x + 3x)$$
$$= -2\\cos 7x\\sin 3x$$

* $\\checkmark 4x = 7x - 3x \\text{ and } 10x = 7x + 3x$
* $\\checkmark \\text{answer: } -2\\cos 7x\\sin 3x$""",
    "final_answer": "-2*cos(7x)*sin(3x)",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-6.2.3",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "6.2.3",
    "marks": 5,
    "topic": "Trigonometry - Equations",
    "passage": q6_2_passage,
    "question": "Hence, determine the solution for $\\sin 4x - \\sin 10x = \\sin 3x$ for $x \\in [0^\\circ ; 30^\\circ]$.",
    "memo": """$$\\sin 4x - \\sin 10x = \\sin 3x$$
$$-2\\cos 7x\\sin 3x = \\sin 3x$$
$$2\\cos 7x\\sin 3x + \\sin 3x = 0$$
$$\\sin 3x(2\\cos 7x + 1) = 0$$

$$\\sin 3x = 0 \\quad\\text{or}\\quad \\cos 7x = -\\frac{1}{2}$$

For $\\sin 3x = 0$:
$$3x = 0^\\circ \\implies x = 0^\\circ$$

For $\\cos 7x = -\\frac{1}{2}$:
$$7x = 120^\\circ \\implies x = 17{,}14^\\circ$$
$$7x = 240^\\circ \\implies x = 34{,}29^\\circ \\quad (\\text{N/A, } x \\notin [0^\\circ ; 30^\\circ])$$

$$x = 0^\\circ \\quad\\text{or}\\quad x = 17{,}14^\\circ$$

* $\\checkmark \\text{substitution } -2\\cos 7x\\sin 3x = \\sin 3x$
* $\\checkmark \\text{factorisation}$
* $\\checkmark \\text{both equations: } \\sin 3x = 0 \\text{ and } \\cos 7x = -\\frac{1}{2}$
* $\\checkmark \\text{answer: } x = 0^\\circ$
* $\\checkmark \\text{answer: } x = 17{,}14^\\circ$""",
    "final_answer": "x = 0° or x = 17.14°",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

# ==========================================
# QUESTION 7
# ==========================================
q7_passage = """[DIAGRAM: Trigonometric Functions Graph | Interval [-180°, 180°] | Graph f(x) = 2 cos x + 1 is a cosine curve with amplitude 2, shifted up 1 unit; f(-180°) = -1, maximum at (0°, 3), f(180°) = -1, x-intercepts at -120° and 120°; Graph g(x) = sin 2x is a sine wave with amplitude 1 and period 180°, zeros at -180°, -90°, 0°, 90°, 180°, local max at (-135°, 1) and (45°, 1), local min at (-45°, -1) and (135°, -1)]

In the diagram, the graphs of $f(x) = 2\\cos x + 1$ and $g(x) = \\sin 2x$ are drawn for the interval $x \\in [-180^\\circ ; 180^\\circ]$."""

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-7.1",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "7.1",
    "marks": 1,
    "topic": "Functions - Range",
    "passage": q7_passage,
    "question": "Write down the range of $f$.",
    "memo": """$$\\text{Range of } f: y \\in [-1 ; 3] \\quad\\text{or}\\quad -1 \\le y \\le 3$$

* $\\checkmark y \\in [-1 ; 3] \\text{ or } -1 \\le y \\le 3$""",
    "final_answer": "[-1, 3]",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-7.2",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "7.2",
    "marks": 1,
    "topic": "Functions - Period",
    "passage": q7_passage,
    "question": "Write down the period of $g$.",
    "memo": """$$\\text{Period of } g = 180^\\circ$$

* $\\checkmark 180^\\circ$""",
    "final_answer": "180°",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-7.3",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "7.3",
    "marks": 1,
    "topic": "Functions - Increasing Intervals",
    "passage": q7_passage,
    "question": "For which values of $x$, in the interval $x \\in [-180^\\circ ; 180^\\circ]$, is $f$ increasing?",
    "memo": """$$f \\text{ is increasing for: } x \\in (-180^\\circ ; 0^\\circ) \\quad\\text{or}\\quad -180^\\circ < x < 0^\\circ$$

* $\\checkmark x \\in (-180^\\circ ; 0^\\circ) \\text{ or } -180^\\circ < x < 0^\\circ$""",
    "final_answer": "(-180°, 0°)",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-7.4.1",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "7.4.1",
    "marks": 2,
    "topic": "Calculus & Functions - Derivative Sign & Intervals",
    "passage": q7_passage,
    "question": "Use the graphs to determine the values of $x$, in the interval $x \\in [-180^\\circ ; 180^\\circ]$, for which: $g(x) \\cdot f'(x) < 0$",
    "memo": """$$g(x) \\cdot f'(x) < 0$$
$$x \\in (-90^\\circ ; 0^\\circ) \\cup (0^\\circ ; 90^\\circ) \\quad\\text{or}\\quad -90^\\circ < x < 0^\\circ \\text{ or } 0^\\circ < x < 90^\\circ$$

* $\\checkmark x \\in (-90^\\circ ; 0^\\circ)$
* $\\checkmark x \\in (0^\\circ ; 90^\\circ)$""",
    "final_answer": "(-90°, 0°) U (0°, 90°)",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-7.4.2",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "7.4.2",
    "marks": 3,
    "topic": "Functions - Graph Interpretation & Inequalities",
    "passage": q7_passage,
    "question": "Use the graphs to determine the values of $x$, in the interval $x \\in [-180^\\circ ; 180^\\circ]$, for which: $\\cos x \\le -\\frac{1}{2}$",
    "memo": """$$\\cos x \\le -\\frac{1}{2} \\iff 2\\cos x + 1 \\le 0$$
$$x \\in [-180^\\circ ; -120^\\circ] \\cup [120^\\circ ; 180^\\circ] \\quad\\text{or}\\quad -180^\\circ \\le x \\le -120^\\circ \\text{ or } 120^\\circ \\le x \\le 180^\\circ$$

* $\\checkmark 2\\cos x + 1 \\le 0$
* $\\checkmark x \\in [-180^\\circ ; -120^\\circ]$
* $\\checkmark x \\in [120^\\circ ; 180^\\circ]$""",
    "final_answer": "[-180°, -120°] U [120°, 180°]",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-7.5",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "7.5",
    "marks": 2,
    "topic": "Functions - Transformations",
    "passage": q7_passage,
    "question": "Graph $g$ is shifted $45^\\circ$ to the right to obtain a new graph $h$. Determine the equation of $h$ in its simplest form.",
    "memo": """$$g(x) = \\sin 2x$$
$$h(x) = \\sin(2(x - 45^\\circ))$$
$$= \\sin(2x - 90^\\circ)$$
$$= -\\sin(90^\\circ - 2x)$$
$$= -\\cos 2x$$

* $\\checkmark \\sin(2x - 90^\\circ)$
* $\\checkmark \\text{equation of } h: h(x) = -\\cos 2x$""",
    "final_answer": "h(x) = -cos(2x)",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

# ==========================================
# QUESTION 8
# ==========================================
q8_passage = """[DIAGRAM: 3D Trigonometry | Points A, B, C lie in horizontal plane with AB = AC; D is a vertical point directly above A such that DA ⊥ AB and DA ⊥ AC; AD = p; BC = 2AD = 2p; Angle ABC = x; Angle DBA = y; Shaded horizontal base triangle ABC is isosceles with AB = AC]

In the diagram, $A, B$ and $C$ lie in the same horizontal plane with $AB = AC$. $D$ is directly above $A$ such that $2AD = BC$. Also, $AD = p$, $\\text{A}\\hat{\\text{B}}\\text{C} = x$ and $\\text{D}\\hat{\\text{B}}\\text{A} = y$."""

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-8.1",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "8.1",
    "marks": 2,
    "topic": "3D Trigonometry - Right-angled Triangle",
    "passage": q8_passage,
    "question": "Determine $AB$ in terms of $p$ and $y$.",
    "memo": """$$\\tan y = \\frac{p}{AB}$$
$$AB = \\frac{p}{\\tan y}$$

* $\\checkmark \\text{correct trig ratio } (\\tan y = \\frac{p}{AB})$
* $\\checkmark \\text{answer } \\left(AB = \\frac{p}{\\tan y}\\right)$""",
    "final_answer": "p/tan(y)",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-8.2",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "8.2",
    "marks": 4,
    "topic": "3D Trigonometry - Sine Rule / Cosine Rule",
    "passage": q8_passage,
    "question": "Show that $\\cos x = \\tan y$.",
    "memo": """In $\\Delta BAC$:
$$\\text{B}\\hat{\\text{A}}\\text{C} = 180^\\circ - 2x, \\quad BC = 2p, \\quad AB = \\frac{p}{\\tan y}$$

$$\\frac{BC}{\\sin\\text{B}\\hat{\\text{A}}\\text{C}} = \\frac{AB}{\\sin\\text{A}\\hat{\\text{C}}\\text{B}}$$
$$\\frac{2p}{\\sin(180^\\circ - 2x)} = \\frac{\\frac{p}{\\tan y}}{\\sin x}$$
$$\\frac{2p}{\\sin 2x} = \\frac{p}{\\tan y \\cdot \\sin x}$$
$$\\frac{2p}{2\\sin x\\cos x} = \\frac{p}{\\tan y \\cdot \\sin x}$$
$$\\frac{1}{\\cos x} = \\frac{1}{\\tan y}$$
$$\\cos x = \\tan y$$

OR/OF

In $\\Delta BAC$:
$$BC^2 = AB^2 + AC^2 - 2(AB)(AC)\\cos\\text{B}\\hat{\\text{A}}\\text{C}$$
$$(2p)^2 = \\left(\\frac{p}{\\tan y}\\right)^2 + \\left(\\frac{p}{\\tan y}\\right)^2 - 2\\left(\\frac{p}{\\tan y}\\right)^2\\cos(180^\\circ - 2x)$$
$$4p^2 = 2\\left(\\frac{p}{\\tan y}\\right)^2 - 2\\left(\\frac{p}{\\tan y}\\right)^2(-\\cos 2x)$$
$$4p^2 = \\frac{2p^2}{\\tan^2 y}(1 + \\cos 2x)$$
$$4p^2 = \\frac{2p^2}{\\tan^2 y}(2\\cos^2 x) = \\frac{4p^2\\cos^2 x}{\\tan^2 y}$$
$$\\tan^2 y = \\cos^2 x \\implies \\cos x = \\tan y$$

* $\\checkmark \\text{correct use of sine-rule or cosine-rule}$
* $\\checkmark \\text{substitute } BC \\text{ and } AB$
* $\\checkmark \\sin(180^\\circ - 2x) = \\sin 2x \\text{ (or } \\cos(180^\\circ - 2x) = -\\cos 2x\\text{)}$
* $\\checkmark \\sin 2x = 2\\sin x\\cos x \\text{ (or } \\cos 2x = 2\\cos^2 x - 1\\text{)}$""",
    "final_answer": "cos(x) = tan(y)",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-8.3",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "8.3",
    "marks": 2,
    "topic": "3D Trigonometry - Angle Calculation",
    "passage": q8_passage,
    "question": "If $x = 60^\\circ$, calculate the size of $y$.",
    "memo": """$$\\cos x = \\tan y$$
$$\\cos 60^\\circ = \\tan y$$
$$\\tan y = 0{,}5$$
$$y = 26{,}57^\\circ$$

* $\\checkmark \\text{substitution of } 60^\\circ \\implies \\tan y = 0{,}5$
* $\\checkmark \\text{answer } (y = 26{,}57^\\circ)$""",
    "final_answer": "26.57°",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

# ==========================================
# QUESTION 9
# ==========================================
q9_1_passage = """[DIAGRAM: Euclidean Geometry | Triangle DEF | Line GH intersects DF at G and EF at H such that GH || DE; Given GF / DG = 2 / 5]

In the diagram, $\\Delta\\text{DEF}$ is drawn. Line $GH$ intersects $DF$ and $EF$ at $G$ and $H$ respectively such that $GH \\parallel DE$ and $\\frac{GF}{DG} = \\frac{2}{5}$."""

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-9.1.1",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "9.1.1",
    "marks": 2,
    "topic": "Euclidean Geometry - Proportionality Theorem",
    "passage": q9_1_passage,
    "question": "Write down, with a reason, the value of $\\frac{HF}{EH}$.",
    "memo": """$$\\frac{HF}{EH} = \\frac{GF}{GD} = \\frac{2}{5} \\quad [\\text{line } \\parallel \\text{ to one side of } \\Delta \\quad\\text{OR}\\quad \\text{prop theorem, } GH \\parallel DE]$$

* $\\checkmark \\text{S } \\left(\\frac{HF}{EH} = \\frac{2}{5}\\right)$
* $\\checkmark \\text{R } (\\text{line } \\parallel \\text{ to one side of } \\Delta \\text{ OR prop theorem; } GH \\parallel DE)$""",
    "final_answer": "2/5",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-9.1.2",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "9.1.2",
    "marks": 2,
    "topic": "Euclidean Geometry - Proportionality Theorem",
    "passage": q9_1_passage,
    "question": "If $\\text{EF} = 21\\text{ cm}$, calculate the length of $EH$.",
    "memo": """$$\\frac{EH}{EF} = \\frac{DG}{DF} = \\frac{5}{7} \\quad [\\text{line } \\parallel \\text{ to one side of } \\Delta \\text{ OR prop theorem; } GH \\parallel DE]$$
$$\\frac{EH}{21} = \\frac{5}{7}$$
$$EH = 15\\text{ cm}$$

OR/OF

$$\\frac{HF}{EF} = \\frac{2}{7}$$
$$\\frac{HF}{21} = \\frac{2}{7} \\implies HF = 6\\text{ cm}$$
$$EH = 21 - 6 = 15\\text{ cm}$$

* $\\checkmark \\text{S } \\left(\\frac{EH}{21} = \\frac{5}{7} \\text{ or } HF = 6\\right)$
* $\\checkmark \\text{answer } (EH = 15\\text{ cm})$""",
    "final_answer": "15 cm",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-9.1.3",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "9.1.3",
    "marks": 1,
    "topic": "Euclidean Geometry - Similar Triangles",
    "passage": q9_1_passage,
    "question": "Write down a triangle which is similar to $\\Delta\\text{FGH}$.",
    "memo": """$$\\Delta\\text{FDE} \\quad [\\angle\\angle\\angle]$$

* $\\checkmark \\text{S } (\\Delta FDE)$""",
    "final_answer": "ΔFDE",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-9.1.4",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "9.1.4",
    "marks": 2,
    "topic": "Euclidean Geometry - Similar Triangles Ratio",
    "passage": q9_1_passage,
    "question": "Hence, calculate the value of $\\frac{GH}{DE}$.",
    "memo": """$$\\frac{GH}{DE} = \\frac{FG}{FD} = \\frac{FH}{FE} \\quad [||| \\Delta\\text{s}]$$
$$\\frac{GH}{DE} = \\frac{2}{7}$$

* $\\checkmark \\text{S } \\left(\\frac{GH}{DE} = \\frac{FG}{FD}\\right)$
* $\\checkmark \\text{S } \\left(\\frac{GH}{DE} = \\frac{2}{7}\\right)$""",
    "final_answer": "2/7",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

q9_2_passage = """[DIAGRAM: Euclidean Geometry | Two Intersecting Circles | Larger circle centre O with diameter POL; Smaller circle centre M with diameter TMR; Circles intersect at points L and R; Tangent PLK touches smaller circle at L; Tangent TR touches larger circle at R; Line OM intersects smaller circle at N; Straight lines LT, LR, LN, and PR are drawn; Angles at L: L1 (angle KLT), L2 (angle TLR), L3 (angle RLN), L4 (angle NLO); Angles at R: R1 (angle LRM), R2 (angle LRP); Angles at O: O1 (angle LOM), O2 (angle POM); Angles at M: M1 (angle RMO), M2 (angle TMO); Angles at N: N1 (angle LNM), N2 (angle LNO)]

In the diagram, $POL$ is a diameter of the larger circle with centre $O$. $TMR$ is a diameter of the smaller circle with centre $M$. The two circles intersect at $L$ and $R$. $PLK$ is a tangent to the smaller circle at $L$ and $TR$ is a tangent to the larger circle at $R$. $OM$ intersects the smaller circle at $N$. Straight lines $LT, LR, LN$ and $PR$ are drawn."""

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-9.2.1",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "9.2.1",
    "marks": 4,
    "topic": "Euclidean Geometry - Parallel Lines & Circle Theorems",
    "passage": q9_2_passage,
    "question": "Prove, giving reasons, that $LT \\parallel PR$.",
    "memo": """$$\\hat{L}_2 = 90^\\circ \\quad [\\angle \\text{ in semi-circle}]$$
$$\\hat{R}_2 = 90^\\circ \\quad [\\angle \\text{ in semi-circle}]$$
$$\\therefore \\hat{L}_2 = \\hat{R}_2$$
$$\\therefore LT \\parallel PR \\quad [\\text{alt } \\angle\\text{s =}]$$

OR/OF

$$\\hat{L}_1 = \\hat{R}_1 \\quad [\\text{tan-chord theorem}]$$
$$\\hat{R}_1 = \\hat{P} \\quad [\\text{tan-chord theorem}]$$
$$\\therefore \\hat{L}_1 = \\hat{P}$$
$$\\therefore LT \\parallel PR \\quad [\\text{corresp } \\angle\\text{s =}]$$

* $\\checkmark \\text{S } \\checkmark \\text{R } (\\hat{L}_2 = 90^\\circ \\text{ [}\\angle \\text{ in semi-circle]})$
* $\\checkmark \\text{S/R } (\\hat{R}_2 = 90^\\circ \\text{ [}\\angle \\text{ in semi-circle]})$
* $\\checkmark \\text{R } (LT \\parallel PR \\text{ [alt } \\angle\\text{s =]})$""",
    "final_answer": "LT || PR",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-9.2.2",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "9.2.2",
    "marks": 5,
    "topic": "Euclidean Geometry - Cyclic Quadrilateral",
    "passage": q9_2_passage,
    "question": "Prove, giving reasons, that $\\text{LORM}$ is a cyclic quadrilateral, if it is also given that $LT \\parallel OM$.",
    "memo": """$$\\hat{L}_1 = \\hat{R}_1 \\quad [\\text{tan-chord theorem}]$$
$$\\hat{L}_1 = \\hat{O}_1 \\quad [\\text{corresp } \\angle\\text{s; } LT \\parallel OM]$$
$$\\therefore \\hat{O}_1 = \\hat{R}_1$$
$$\\therefore L, O, R \\text{ and } M \\text{ are concyclic.}$$
$$\\therefore LORM \\text{ is a cyclic quadrilateral } [\\text{converse } \\angle\\text{s in the same seg}]$$

* $\\checkmark \\text{S } \\checkmark \\text{R } (\\hat{L}_1 = \\hat{R}_1 \\text{ [tan-chord theorem]})$
* $\\checkmark \\text{S/R } (\\hat{L}_1 = \\hat{O}_1 \\text{ [corresp } \\angle\\text{s; } LT \\parallel OM])$
* $\\checkmark \\text{S } (\\hat{O}_1 = \\hat{R}_1)$
* $\\checkmark \\text{R } (\\text{converse } \\angle\\text{s in the same seg})$""",
    "final_answer": "LORM is a cyclic quad",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-9.2.3",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "9.2.3",
    "marks": 4,
    "topic": "Euclidean Geometry - Angle Bisector & Central Angle",
    "passage": q9_2_passage,
    "question": "Prove, giving reasons, that $LN$ bisects $\\text{O}\\hat{\\text{L}}\\text{R}$.",
    "memo": """$$\\text{O}\\hat{\\text{L}}\\text{R} = \\hat{M}_1 \\quad [\\angle\\text{s in the same seg}]$$
$$\\hat{M}_1 = 2\\hat{L}_3 \\quad [\\angle \\text{ at centre} = 2 \\times \\angle \\text{ at circumference}]$$
$$\\therefore \\text{O}\\hat{\\text{L}}\\text{R} = 2\\hat{L}_3$$
$$\\therefore \\hat{L}_4 = \\hat{L}_3$$
$$\\therefore LN \\text{ bisects } \\text{O}\\hat{\\text{L}}\\text{R}$$

* $\\checkmark \\text{S/R } (\\text{O}\\hat{\\text{L}}\\text{R} = \\hat{M}_1 \\text{ [}\\angle\\text{s in same seg]})$
* $\\checkmark \\text{S } \\checkmark \\text{R } (\\hat{M}_1 = 2\\hat{L}_3 \\text{ [}\\angle \\text{ at centre} = 2 \\times \\angle \\text{ at circumference]})$
* $\\checkmark \\text{S } (\\hat{L}_4 = \\hat{L}_3 \\implies LN \\text{ bisects } \\text{O}\\hat{\\text{L}}\\text{R})$""",
    "final_answer": "LN bisects OLR",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

# ==========================================
# QUESTION 10
# ==========================================
q10_1_passage = """[DIAGRAM: Euclidean Geometry | Theorem: Equiangular Triangles | Two separate triangles ABC and PKL drawn with angle A = angle P, angle B = angle K, and angle C = angle L]

In the diagram, $\\Delta\\text{ABC}$ and $\\Delta\\text{PKL}$ are drawn such that $\\hat{A} = \\hat{P}$, $\\hat{B} = \\hat{K}$ and $\\hat{C} = \\hat{L}$."""

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-10.1",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "10.1",
    "marks": 6,
    "topic": "Euclidean Geometry - Equiangular Triangles Theorem",
    "passage": q10_1_passage,
    "question": "Use the diagram in the ANSWER BOOK to prove the theorem which states that if two triangles are equiangular, then the corresponding sides are in proportion, i.e. that $\\frac{AB}{PK} = \\frac{AC}{PL}$.",
    "memo": """Construction: Draw line $MN$, where $M$ and $N$ are points on $AB$ and $AC$ respectively such that $AM = PK$ and $AN = PL$.

In $\\Delta AMN$ and $\\Delta PKL$:
$$\\hat{A} = \\hat{P} \\quad [\\text{given}]$$
$$AM = PK \\quad [\\text{construction}]$$
$$AN = PL \\quad [\\text{construction}]$$
$$\\therefore \\Delta AMN \\equiv \\Delta PKL \\quad [s\\angle s]$$
$$\\therefore \\hat{M}_1 = \\hat{K}$$
$$\\text{But } \\hat{B} = \\hat{K} \\quad [\\text{given}]$$
$$\\therefore \\hat{M}_1 = \\hat{B}$$
$$\\therefore MN \\parallel BC \\quad [\\text{corresp } \\angle\\text{s =}]$$
$$\\therefore \\frac{AB}{AM} = \\frac{AC}{AN} \\quad [\\text{line } \\parallel \\text{ to one side of } \\Delta \\text{ OR prop theorem; } MN \\parallel BC]$$
$$\\text{But } AM = PK \\text{ and } AN = PL$$
$$\\therefore \\frac{AB}{PK} = \\frac{AC}{PL}$$

* $\\checkmark \\text{construction}$
* $\\checkmark \\text{S/R } (\\Delta AMN \\equiv \\Delta PKL \\text{ [}s\\angle s\\text{]})$
* $\\checkmark \\text{S } (\\hat{M}_1 = \\hat{K} = \\hat{B})$
* $\\checkmark \\text{S/R } (MN \\parallel BC \\text{ [corresp } \\angle\\text{s =]})$
* $\\checkmark \\text{S } \\checkmark \\text{R } \\left(\\frac{AB}{AM} = \\frac{AC}{AN} \\text{ [line } \\parallel \\text{ one side of } \\Delta\\text{]}\\right)$""",
    "final_answer": "AB/PK = AC/PL",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

q10_2_passage = """[DIAGRAM: Euclidean Geometry | Circle and Triangles | Circle with centre O; Points D and B lie on the circle forming chord BD; Straight line AC passes through B with order of points A, B, F, C; Points A and C lie outside the circle; Side AC of triangle ADC passes through B; Line FO is parallel to chord BD (FO || BD); Point R is the midpoint of chord BD with DR = RB; RO is drawn from centre O to R; Lines DC, OC, AD are drawn]

In the diagram, $O$ is the centre of the circle. Points $D$ and $B$ lie on the circle. Points $A$ and $C$ lie outside the circle such that side $AC$ of $\\Delta\\text{ADC}$ passes through $B$. $F$ is a point on $BC$ such that $FO \\parallel BD$. $DR = RB$ and $RO$ is drawn."""

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-10.2.1",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "10.2.1",
    "marks": 3,
    "topic": "Euclidean Geometry - Similar Triangles",
    "passage": q10_2_passage,
    "question": "Prove, with reasons, that $\\Delta\\text{CFO} \\parallel\\parallel\\parallel \\Delta\\text{CBD}$.",
    "memo": """In $\\Delta CFO$ and $\\Delta CBD$:
$$\\hat{C} = \\hat{C} \\quad [\\text{common}]$$
$$\\text{C}\\hat{\\text{F}}\\text{O} = \\text{C}\\hat{\\text{B}}\\text{D} \\quad [\\text{corresp } \\angle\\text{s; } BD \\parallel FO]$$
$$\\text{C}\\hat{\\text{O}}\\text{F} = \\text{C}\\hat{\\text{D}}\\text{B} \\quad [\\text{sum of } \\angle\\text{s in } \\Delta \\quad\\text{OR}\\quad \\text{corresp } \\angle\\text{s; } BD \\parallel FO]$$
$$\\therefore \\Delta CFO \\parallel\\parallel\\parallel \\Delta CBD \\quad [\\angle\\angle\\angle]$$

* $\\checkmark \\text{S } (\\hat{C} = \\hat{C} \\text{ [common]})$
* $\\checkmark \\text{S/R } (\\text{C}\\hat{\\text{F}}\\text{O} = \\text{C}\\hat{\\text{B}}\\text{D} \\text{ [corresp } \\angle\\text{s; } BD \\parallel FO])$
* $\\checkmark \\text{S/R OR R } (\\text{C}\\hat{\\text{O}}\\text{F} = \\text{C}\\hat{\\text{D}}\\text{B} \\text{ [sum of } \\angle\\text{s in } \\Delta\\text{]} \\text{ and } [\\angle\\angle\\angle])$""",
    "final_answer": "ΔCFO ||| ΔCBD",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-10.2.2",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "10.2.2",
    "marks": 2,
    "topic": "Euclidean Geometry - Similar Triangles & Equal Sides",
    "passage": q10_2_passage,
    "question": "If it is given that $\\text{R}\\hat{\\text{D}}\\text{O} = \\text{F}\\hat{\\text{C}}\\text{O}$, show, with reasons, that $\\text{OF} \\cdot \\text{CD} = \\text{CO} \\cdot \\text{BC}$.",
    "memo": """$$\\frac{FO}{BD} = \\frac{CO}{CD} \\quad [||| \\Delta\\text{s}]$$
$$FO \\cdot CD = CO \\cdot BD$$
$$\\text{But } \\text{R}\\hat{\\text{D}}\\text{O} = \\text{F}\\hat{\\text{C}}\\text{O} \\quad [\\text{given}]$$
$$\\therefore BD = BC \\quad [\\text{sides opp equal } \\angle\\text{s}]$$
$$\\therefore FO \\cdot CD = CO \\cdot BC$$

* $\\checkmark \\text{S/R } \\left(\\frac{FO}{BD} = \\frac{CO}{CD} \\text{ [||| } \\Delta\\text{s]}\\right)$
* $\\checkmark \\text{S/R } (BD = BC \\text{ [sides opp equal } \\angle\\text{s]} \\implies FO \\cdot CD = CO \\cdot BC)$""",
    "final_answer": "OF.CD = CO.BC",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-10.2.3",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "10.2.3",
    "marks": 6,
    "topic": "Euclidean Geometry - Line from Centre Perpendicular to Chord & Proportionality",
    "passage": q10_2_passage,
    "question": "It is further given that $\\text{DC} = 19{,}2\\text{ units}$, $\\text{BD} = 12\\text{ units}$ and $\\frac{\\text{RO}}{\\text{RD}} = \\frac{3}{4}$. Prove, with reasons, that $\\text{BF} = \\frac{75}{16}$.",
    "memo": """$$RD = 6\\text{ units} \\quad [DR = RB]$$
$$\\frac{RO}{RD} = \\frac{3}{4} \\implies RO = \\frac{3}{4}(6) = 4{,}5\\text{ units}$$
$$OR \\perp BD \\quad [\\text{line from centre to midpt of chord}]$$
$$DO^2 = 6^2 + (4{,}5)^2 = 36 + 20{,}25 = 56{,}25 \\quad [\\text{Pythagoras}]$$
$$DO = 7{,}5\\text{ units}$$

In $\\Delta BCD$:
$$\\frac{BC}{BF} = \\frac{DC}{DO} \\quad [\\text{line } \\parallel \\text{ to one side of } \\Delta \\quad\\text{OR}\\quad \\text{prop theorem; } BD \\parallel FO]$$
$$BC = BD = 12\\text{ units} \\quad [\\text{sides opp equal } \\angle\\text{s}]$$
$$\\frac{12}{BF} = \\frac{19{,}2}{7{,}5}$$
$$BF = \\frac{12 \\times 7{,}5}{19{,}2} = \\frac{90}{19{,}2} = \\frac{75}{16}\\text{ units}$$

* $\\checkmark \\text{S } (RD = 6 \\text{ and } RO = 4{,}5)$
* $\\checkmark \\text{S/R } (OR \\perp BD \\text{ [line from centre to midpt of chord]})$
* $\\checkmark \\text{S } (DO = 7{,}5)$
* $\\checkmark \\text{S/R } \\left(\\frac{BC}{BF} = \\frac{DC}{DO} \\text{ [line } \\parallel \\text{ one side of } \\Delta\\text{]}\\right)$
* $\\checkmark \\text{S } (BC = 12)$
* $\\checkmark \\text{S } \\left(BF = \\frac{75}{16}\\right)$""",
    "final_answer": "75/16",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

items.append({
    "item_id": "dbe-mathematics-g12-p2-2025-may-10.2.4",
    "source_id": "dbe-mathematics-g12-p2-2025-may",
    "pair_source_id": "dbe-mathematics-g12-p2-2025-may-memo",
    "subject": "mathematics",
    "grade": 12,
    "language": "en",
    "track": "core_maths",
    "kind": "question",
    "question_ref": "10.2.4",
    "marks": 3,
    "topic": "Euclidean Geometry - Angle Calculations & Cosine Rule",
    "passage": q10_2_passage,
    "question": "Calculate the size of $\\text{A}\\hat{\\text{B}}\\text{D}$.",
    "memo": """Method 1 (Using right-angled $\\Delta ORD$):
$$\\tan\\text{R}\\hat{\\text{D}}\\text{O} = \\frac{RO}{RD} = \\frac{4{,}5}{6} = \\frac{3}{4}$$
$$\\text{R}\\hat{\\text{D}}\\text{O} = 36{,}87^\\circ$$
$$\\text{F}\\hat{\\text{C}}\\text{O} = \\text{R}\\hat{\\text{D}}\\text{O} = 36{,}87^\\circ \\quad [\\text{given}]$$
Since $\\Delta BCD$ is isosceles with $BC = BD = 12$:
$$\\text{B}\\hat{\\text{D}}\\text{C} = \\text{B}\\hat{\\text{C}}\\text{D} = 36{,}87^\\circ$$
$$\\text{A}\\hat{\\text{B}}\\text{D} = \\text{B}\\hat{\\text{D}}\\text{C} + \\text{B}\\hat{\\text{C}}\\text{D} = 36{,}87^\\circ + 36{,}87^\\circ = 73{,}74^\\circ \\quad [\\text{ext } \\angle \\text{ of } \\Delta]$$

OR/OF

Method 2 (Using Cosine Rule in $\\Delta BCD$):
$$CD^2 = BC^2 + BD^2 - 2(BC)(BD)\\cos\\text{D}\\hat{\\text{B}}\\text{C}$$
$$(19{,}2)^2 = 12^2 + 12^2 - 2(12)(12)\\cos\\text{D}\\hat{\\text{B}}\\text{C}$$
$$\\cos\\text{D}\\hat{\\text{B}}\\text{C} = \\frac{12^2 + 12^2 - (19{,}2)^2}{2(12)(12)} = -\\frac{7}{25}$$
$$\\text{D}\\hat{\\text{B}}\\text{C} = 106{,}26^\\circ$$
$$\\text{A}\\hat{\\text{B}}\\text{D} = 180^\\circ - 106{,}26^\\circ = 73{,}74^\\circ \\quad [\\angle\\text{s on straight line}]$$

* $\\checkmark \\text{ratio } (\\tan\\text{R}\\hat{\\text{D}}\\text{O} = \\frac{3}{4} \\text{ or cosine-rule substitution})$
* $\\checkmark \\text{R}\\hat{\\text{D}}\\text{O} = 36{,}87^\\circ \\text{ (or } \\text{D}\\hat{\\text{B}}\\text{C} = 106{,}26^\\circ\\text{)}$
* $\\checkmark \\text{answer: } \\text{A}\\hat{\\text{B}}\\text{D} = 73{,}74^\\circ$""",
    "final_answer": "73.74°",
    "needs_review": False,
    "licence": "DBE copyright - check terms",
    "attribution": "Department of Basic Education"
})

print(f"Total items created: {len(items)}")
total_marks = sum(item["marks"] for item in items)
print(f"Total marks: {total_marks}")

# Save to output locations
out_file1 = "sa-tutor-kit/sa-tutor-kit/workspace/items/mathematics/dbe-mathematics-g12-p2-2025-may.jsonl"
out_file2 = "sa-tutor-kit/sa-tutor-kit/workspace/items/dbe-mathematics-g12-p2-2025-may.jsonl"

for path in [out_file1, out_file2]:
    with open(path, "w", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"Saved {len(items)} items to {path}")
