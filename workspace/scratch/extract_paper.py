# -*- coding: utf-8 -*-
"""
Extractor script for Physical Sciences Grade 12 Paper 1 November 2022
Source ID: dbe-physical_sciences-g12-p1-2022-nov
Memo ID: dbe-physical_sciences-g12-p1-2022-nov-memo
"""

import json
import os
import re

SOURCE_ID = "dbe-physical_sciences-g12-p1-2022-nov"
MEMO_ID = "dbe-physical_sciences-g12-p1-2022-nov-memo"
SUBJECT = "physical_sciences"
GRADE = 12
LANGUAGE = "en"
TRACK = "physical_sciences"

items = []

def add_item(q_ref, kind, marks, topic, passage, question, memo, final_answer):
    item = {
        "item_id": f"{SOURCE_ID}-{q_ref}",
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": kind,
        "question_ref": q_ref,
        "marks": marks,
        "topic": topic,
        "passage": passage,
        "question": question,
        "memo": memo,
        "final_answer": final_answer,
        "needs_review": False,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    }
    items.append(item)

# ==========================================
# QUESTION 1: MULTIPLE-CHOICE QUESTIONS (20 MARKS)
# ==========================================

# 1.1
add_item(
    q_ref="1.1",
    kind="multiple_choice",
    marks=2,
    topic="Vectors and Scalars",
    passage="",
    question="Which ONE of the following combinations consists of only SCALAR quantities?\n\nA Velocity, speed and time\nB Time, distance and speed\nC Acceleration, speed and distance\nD Displacement, velocity and acceleration",
    memo="B $\\checkmark\\checkmark$\n\n*Rationale: A scalar quantity has magnitude only, with no specific direction. Time, distance, and speed are all scalar quantities. In contrast, velocity, acceleration, and displacement are vector quantities that have both magnitude and direction. Therefore, only combination B consists exclusively of scalar quantities.*",
    final_answer="B"
)

# 1.2
add_item(
    q_ref="1.2",
    kind="multiple_choice",
    marks=2,
    topic="Newton's Law of Universal Gravitation",
    passage="",
    question="The acceleration due to gravity on Earth is $g$.\n\nWhich ONE of the following represents the acceleration due to gravity on a planet that has TWICE the mass and HALF the radius of the Earth?\n\nA $g$\nB $2g$\nC $4g$\nD $8g$",
    memo="D $\\checkmark\\checkmark$\n\n*Rationale: According to Newton's law of universal gravitation, gravitational acceleration on the surface of a planet is given by $g = \\frac{GM}{R^2}$. For a planet with mass $M' = 2M$ and radius $R' = \\frac{1}{2}R$:\n$$g' = \\frac{G(2M)}{\\left(\\frac{1}{2}R\\right)^2} = \\frac{2GM}{\\frac{1}{4}R^2} = 8\\left(\\frac{GM}{R^2}\\right) = 8g$$\nTherefore, the acceleration due to gravity is $8g$ (Option D).*",
    final_answer="D"
)

# 1.3
add_item(
    q_ref="1.3",
    kind="multiple_choice",
    marks=2,
    topic="Vertical Projectile Motion - Mechanical Energy & Acceleration",
    passage="A ball is projected vertically upwards from the ground and reaches its maximum height after a while.\n\nIgnore the effects of air friction.",
    question="How will the ACCELERATION and TOTAL MECHANICAL ENERGY of the ball at its maximum height compare to that immediately after it was projected?\n\n| | ACCELERATION | TOTAL MECHANICAL ENERGY |\n|---|---|---|\n| A | Equal to | Equal to |\n| B | Greater than | Smaller than |\n| C | Equal to | Greater than |\n| D | Smaller than | Equal to |",
    memo="A $\\checkmark\\checkmark$\n\n*Rationale: In free fall (ignoring air friction), the only force acting on the ball throughout its motion is gravity. Therefore, its acceleration remains constant downwards at $g = 9{,}8\\text{ m}\\cdot\\text{s}^{-2}$ (Equal to). Because gravity is a conservative force and no non-conservative forces do work, the total mechanical energy is conserved throughout the entire flight ($E_{\\text{mech}} = E_k + E_p = \\text{constant}$, hence Equal to).*",
    final_answer="A"
)

# 1.4
add_item(
    q_ref="1.4",
    kind="multiple_choice",
    marks=2,
    topic="Work, Energy and Power",
    passage="A car travels at CONSTANT VELOCITY along a horizontal road. A constant frictional force acts on the car during its motion.",
    question="Which ONE of the following statements about the power dissipated by the engine of the car during the motion is CORRECT?\n\nThe power …\n\nA is zero.\nB increases.\nC decreases.\nD remains constant.",
    memo="D $\\checkmark\\checkmark$\n\n*Rationale: Power is given by $P = Fv$. Since the car moves at a constant velocity ($a = 0$), the forward driving force exerted by the engine equals the magnitude of the opposing frictional force ($F_{\\text{engine}} = f$). Because the frictional force $f$ is constant, $F_{\\text{engine}}$ is constant. With both $F$ and $v$ constant, the power output $P = Fv$ remains constant.*",
    final_answer="D"
)

# 1.5
add_item(
    q_ref="1.5",
    kind="multiple_choice",
    marks=2,
    topic="Work, Energy and Momentum - Connected Bodies",
    passage="Block X is placed on a horizontal table and is connected to block Y by a light inextensible string passing over a frictionless pulley, as shown in the diagram. A constant frictional force acts on block X while it moves to the right. P, Q and R are points on the table such that the distance from P to Q is equal to that from Q to R ($PQ = QR$). When block X reaches point Q, the string is cut and block X continues to move towards point R. Ignore the effect of air friction.",
    question="Consider the following statements:\n\n(i) The work done by the frictional force acting on block X is greater when the block moves from point P to point Q than when the block moves from point Q to point R.\n\n(ii) Both the momentum and kinetic energy of block X decrease when the block moves from point Q to point R.\n\n(iii) The total mechanical energy of block X remains constant when the block moves from point Q to point R.\n\nWhich of the statements above is/are CORRECT as block X moves from point Q to point R?\n\nA (i) only\nB (ii) only\nC (i) and (ii) only\nD (ii) and (iii) only",
    memo="B $\\checkmark\\checkmark$\n\n*Rationale:\n- Statement (i) is INCORRECT: The frictional force $f$ is constant and the distances are equal ($PQ = QR = \\Delta x$), so the work done by friction $W_f = f\\Delta x\\cos 180^\\circ = -f\\Delta x$ is identical in magnitude over both intervals.\n- Statement (ii) is CORRECT: Once the string is cut at Q, the only horizontal force acting on block X is friction opposing its motion ($F_{\\text{net}} = -f$). Block X decelerates ($v$ decreases), so its linear momentum ($p = mv$) and kinetic energy ($E_k = \\frac{1}{2}mv^2$) both decrease.\n- Statement (iii) is INCORRECT: Friction is a non-conservative force doing negative work on block X, dissipating mechanical energy as heat ($W_{nc} < 0$). Thus, total mechanical energy decreases, rather than remaining constant.\nTherefore, only statement (ii) is correct (Option B).*",
    final_answer="B"
)

# 1.6
add_item(
    q_ref="1.6",
    kind="multiple_choice",
    marks=2,
    topic="Doppler Effect - Red Shift",
    passage="Light emitted from a distant star contains a spectral line X of frequency $f$. The spectral lines of this star when observed on Earth are red shifted.",
    question="Which ONE of the following combinations of the OBSERVED FREQUENCY of spectral line X and the MOTION OF THE STAR is CORRECT?\n\n| | OBSERVED FREQUENCY | MOTION OF THE STAR |\n|---|---|---|\n| A | Greater than $f$ | Away from Earth |\n| B | Greater than $f$ | Towards Earth |\n| C | Smaller than $f$ | Away from Earth |\n| D | Smaller than $f$ | Towards Earth |",
    memo="C $\\checkmark\\checkmark$\n\n*Rationale: A 'red shift' signifies a shift towards longer wavelengths (lower frequencies) in the visible spectrum, meaning the observed frequency $f_L$ is smaller than the emitted frequency $f$ ($f_L < f$). Under the Doppler effect for electromagnetic radiation, a decrease in observed frequency indicates that the source (the distant star) is moving away from the observer (Earth).*",
    final_answer="C"
)

# 1.7
add_item(
    q_ref="1.7",
    kind="multiple_choice",
    marks=2,
    topic="Electrostatics - Coulomb's Law",
    passage="A proton and an electron are a distance $r$ apart. The magnitude of the electrostatic force that they exert on each other is $F$.",
    question="Which ONE of the following graphs shows the relationship between $F$ and $r^2$ as the proton and the electron approach each other?\n\nA A straight line starting at the origin with a constant positive gradient ($F \\propto r^2$).\nB A curve passing through the origin that is concave downward.\nC A hyperbolic curve that decreases asymptotically towards the $r^2$-axis as $r^2$ increases ($F \\propto \\frac{1}{r^2}$).\nD A straight line with a negative gradient starting at a non-zero $F$ and intersecting the $r^2$-axis.",
    memo="C $\\checkmark\\checkmark$\n\n*Rationale: By Coulomb's Law, the electrostatic force between two point charges is given by $F = \\frac{k|q_1 q_2|}{r^2}$. This means $F$ is inversely proportional to $r^2$ ($F \\propto \\frac{1}{r^2}$). When $F$ is plotted against $r^2$, the relationship is an inverse curve (a rectangular hyperbola asymptotically approaching both axes), which corresponds to Graph C.*",
    final_answer="C"
)

# 1.8
add_item(
    q_ref="1.8",
    kind="multiple_choice",
    marks=2,
    topic="Electric Circuits - Series and Parallel Voltmeters",
    passage="The emf of a battery is $\\mathcal{E}$ and its internal resistance is $r$. The battery is connected to three resistors and four voltmeters, as shown in the circuit diagram. Resistor $R_1$ is connected in series with a parallel network consisting of resistors $R_2$ and $R_3$. Voltmeter $V_1$ is connected across the terminals of the battery. Voltmeter $V_2$ is connected across resistor $R_1$. Voltmeter $V_3$ is connected across resistor $R_2$. Voltmeter $V_4$ is connected across resistor $R_3$. The resistance of the conducting wires is negligible, while the voltmeters have very high resistances.",
    question="Which ONE of the following equations represents the reading on voltmeter $V_1$ in terms of the readings on the other voltmeters?\n\nA $V_1 = V_2 + V_3$\nB $V_1 = V_2 + \\frac{1}{2}V_3$\nC $V_1 = V_2 + V_3 + V_4$\nD $V_1 = V_2 + 2V_3$",
    memo="A $\\checkmark\\checkmark$\n\n*Rationale: Voltmeter $V_1$ measures the total terminal potential difference ($V_{\\text{ext}}$) across the external circuit. In this circuit, resistor $R_1$ is in series with the parallel pair ($R_2 \\parallel R_3$). The voltage across the parallel combination is measured equally by $V_3$ and $V_4$, so $V_p = V_3 = V_4$. The total external voltage is the sum of the potential difference across $R_1$ and the parallel network: $V_1 = V_2 + V_p = V_2 + V_3$ (Option A).*",
    final_answer="A"
)

# 1.9
add_item(
    q_ref="1.9",
    kind="multiple_choice",
    marks=2,
    topic="Electrodynamics - Alternating Current Generator",
    passage="An AC generator consists of a coil which is rotated in a magnetic field. The emf-time graph for one complete rotation of the coil shows an alternating sinusoidal cycle with a peak emf of $150\\text{ V}$ and a period of $0{,}2\\text{ s}$.",
    question="If the speed of rotation of the coil is now DOUBLED, which ONE of the following graphs is CORRECT for one complete rotation of the coil?\n\nA Peak emf $= 150\\text{ V}$, period $= 0{,}2\\text{ s}$\nB Peak emf $= 300\\text{ V}$, period $= 0{,}2\\text{ s}$\nC Peak emf $= 300\\text{ V}$, period $= 0{,}1\\text{ s}$\nD Peak emf $= 150\\text{ V}$, period $= 0{,}1\\text{ s}$",
    memo="C $\\checkmark\\checkmark$\n\n*Rationale: The peak induced emf in an AC generator is given by $\\varepsilon_{\\max} = NBA\\omega = 2\\pi f NBA$. When the rotational speed (frequency $f$) is doubled ($f' = 2f$), the maximum emf doubles: $\\varepsilon_{\\max}' = 2 \\times 150\\text{ V} = 300\\text{ V}$. The period for one complete rotation becomes half of the original period: $T' = \\frac{1}{f'} = \\frac{T}{2} = \\frac{0{,}2\\text{ s}}{2} = 0{,}1\\text{ s}$. Therefore, for one complete rotation, the peak emf is $300\\text{ V}$ and the period is $0{,}1\\text{ s}$ (Option C).*",
    final_answer="C"
)

# 1.10
add_item(
    q_ref="1.10",
    kind="multiple_choice",
    marks=2,
    topic="Optical Phenomena - Atomic Spectra",
    passage="White light is passed through a cold gas and then through a prism, as shown in the diagram. A line spectrum is observed on the screen.",
    question="Which ONE of the following correctly describes the ENERGY TRANSITION of the atoms of the gas and the TYPE OF LINE SPECTRUM observed on the screen?\n\n| | ENERGY TRANSITION | TYPE OF LINE SPECTRUM |\n|---|---|---|\n| A | Higher to lower energy level | Emission |\n| B | Lower to higher energy level | Emission |\n| C | Higher to lower energy level | Absorption |\n| D | Lower to higher energy level | Absorption |",
    memo="D $\\checkmark\\checkmark$\n\n*Rationale: When continuous white light passes through a cold gas, atoms in the gas absorb photons having specific energies equal to the energy gap between atomic energy levels. This causes electrons in the gas atoms to undergo transitions from a lower energy level to a higher energy level. Because these specific wavelengths are absorbed and re-emitted in all directions, dark lines appear in the transmitted spectrum, producing an absorption line spectrum (Option D).*",
    final_answer="D"
)

# ==========================================
# QUESTION 2: NEWTON'S LAWS (13 MARKS)
# ==========================================

Q2_PASSAGE = (
    "Crate P of mass $1{,}25\\text{ kg}$ is connected to another crate, Q, of mass $2\\text{ kg}$ by a light "
    "inextensible string. The two crates are placed on a rough horizontal surface. A constant force $F$ of magnitude "
    "$7{,}5\\text{ N}$, acting at angle $\\theta$ to the horizontal, is applied on crate Q, pulling it to the right, "
    "as shown in the diagram.\n\n"
    "The crates accelerate at $0{,}1\\text{ m}\\cdot\\text{s}^{-2}$ to the right.\n\n"
    "Crate P experiences a constant frictional force of $1{,}8\\text{ N}$ and crate Q experiences a constant "
    "frictional force of $2{,}2\\text{ N}$."
)

# 2.1
add_item(
    q_ref="2.1",
    kind="question",
    marks=2,
    topic="Newton's Laws of Motion - Newton's Second Law",
    passage=Q2_PASSAGE,
    question="State Newton's Second Law of Motion in words.",
    memo="* When a resultant/net force acts on an object, the object will accelerate in the direction of the force. The acceleration is directly proportional to the resultant/net force and inversely proportional to the mass of the object. $\\checkmark\\checkmark$ *(2 or 0)*\n\n**OR**\n\n* The resultant/net force acting on an object is equal to the rate of change of momentum of the object. $\\checkmark\\checkmark$ *(2 or 0)*",
    final_answer="When a resultant/net force acts on an object, the object will accelerate in the direction of the force with an acceleration directly proportional to the resultant/net force and inversely proportional to the mass of the object."
)

# 2.2
add_item(
    q_ref="2.2",
    kind="question",
    marks=4,
    topic="Newton's Laws of Motion - Free-body Diagram",
    passage=Q2_PASSAGE,
    question="Draw a labelled free-body diagram for crate P.",
    memo="* $w$ / $F_g$ / $F_w$ / gravitational force / weight / $mg$ / $12{,}25\\text{ N}$ (downwards) $\\checkmark$\n* $N$ / $F_N$ / normal force (upwards) $\\checkmark$\n* $T$ / $F_T$ / tension / $F_{\\text{string}}$ (to the right) $\\checkmark$\n* $f$ / $F_f$ / $f_k$ / (kinetic) friction / $1{,}8\\text{ N}$ (to the left) $\\checkmark$\n\n*Marking notes:*\n* Mark awarded for label and arrow.\n* Do not penalise for length of arrows since drawing is not to scale.\n* Any additional force: max $3/4$.\n* If everything correct, but no arrows: max $3/4$.\n* If force(s) do not make contact with the dot: max $3/4$.",
    final_answer="Four labelled forces acting on crate P: Weight ($w$ or $F_g$) acting vertically downwards; Normal force ($N$ or $F_N$) acting vertically upwards; Tension ($T$ or $F_T$) acting horizontally to the right; Kinetic friction ($f$ or $f_k$) acting horizontally to the left."
)

# 2.3.1
add_item(
    q_ref="2.3.1",
    kind="question",
    marks=4,
    topic="Newton's Laws of Motion - Tension Calculation",
    passage=Q2_PASSAGE,
    question="Calculate the magnitude of the tension in the string.",
    memo="**OPTION 1 (Right as positive):**\nFor P:\n$$F_{\\text{net}} = ma$$\n$$T - f = ma$$\n$$T - 1{,}8\\;\\checkmark = (1{,}25)(0{,}1)\\;\\checkmark$$\n$$T - 1{,}8 = 0{,}125$$\n$$T = 1{,}93\\text{ N}\\;\\checkmark\\quad (1{,}925\\text{ N})$$\n*(Formula $\\checkmark$, substitution LHS $\\checkmark$, substitution RHS $\\checkmark$, answer $\\checkmark$)*\n\n**OPTION 2 (Left as positive):**\nFor P:\n$$F_{\\text{net}} = ma$$\n$$-T + f = ma$$\n$$-T + 1{,}8\\;\\checkmark = (1{,}25)(-0{,}1)\\;\\checkmark$$\n$$T = 1{,}93\\text{ N}\\;\\checkmark\\quad (1{,}925\\text{ N})$$",
    final_answer="$1{,}93\\text{ N}$"
)

# 2.3.2
add_item(
    q_ref="2.3.2",
    kind="question",
    marks=3,
    topic="Newton's Laws of Motion - Applied Force Angle Calculation",
    passage=Q2_PASSAGE,
    question="Calculate the magnitude of angle $\\theta$.",
    memo="*Positive marking from QUESTION 2.3.1*\n\n**OPTION 1 (Right as positive):**\nFor Q:\n$$F_{\\text{net}} = ma$$\n$$F\\cos\\theta - T - f = ma$$\n$$7{,}5\\cos\\theta - 1{,}93 - 2{,}2\\;\\checkmark = (2)(0{,}1)\\;\\checkmark$$\n$$7{,}5\\cos\\theta - 4{,}13 = 0{,}2$$\n$$7{,}5\\cos\\theta = 4{,}33$$\n$$\\cos\\theta = \\frac{4{,}33}{7{,}5} = 0{,}5773$$\n$$\\theta = 54{,}74^\\circ\\;\\checkmark\\quad (\\text{Range: } 54{,}55^\\circ - 54{,}78^\\circ)$$\n\n**OPTION 2 (Left as positive):**\nFor Q:\n$$F_{\\text{net}} = ma$$\n$$-F\\cos\\theta + T + f = ma$$\n$$-7{,}5\\cos\\theta + 1{,}93 + 2{,}2\\;\\checkmark = (2)(-0{,}1)\\;\\checkmark$$\n$$-7{,}5\\cos\\theta = -4{,}33$$\n$$\\theta = 54{,}74^\\circ\\;\\checkmark$$",
    final_answer="$54{,}74^\\circ$"
)

# ==========================================
# QUESTION 3: VERTICAL PROJECTILE MOTION (16 MARKS)
# ==========================================

Q3_PASSAGE = (
    "A ball is thrown vertically upwards from the top of a building of height $25\\text{ m}$ with a velocity "
    "of $12\\text{ m}\\cdot\\text{s}^{-1}$. On its way down, the ball passes a door which has a height of "
    "$1{,}9\\text{ m}$ and then strikes the ground, as shown in the diagram.\n\n"
    "Ignore the effects of air friction."
)

# 3.1
add_item(
    q_ref="3.1",
    kind="question",
    marks=2,
    topic="Vertical Projectile Motion - Free Fall Definition",
    passage=Q3_PASSAGE,
    question="Define the term free fall.",
    memo="* Motion under the influence of gravity/weight/gravitational force only. $\\checkmark\\checkmark$ *(2 or 0)*\n\n**OR**\n\n* Motion in which the only force acting is gravity/weight/gravitational force. $\\checkmark\\checkmark$ *(2 or 0)*",
    final_answer="Motion under the influence of gravity (weight) only."
)

# 3.2.1
add_item(
    q_ref="3.2.1",
    kind="question",
    marks=3,
    topic="Vertical Projectile Motion - Time to Maximum Height",
    passage=Q3_PASSAGE,
    question="Calculate the time taken for the ball to reach its maximum height.",
    memo="**Marking criteria:**\n* Formula with $\\Delta t$ $\\checkmark$\n* Correct substitution into formula $\\checkmark$\n* Final answer: $1{,}22\\text{ s}\\;\\checkmark$ ($1{,}22\\text{ s}$ to $1{,}23\\text{ s}$)\n\n**OPTION 1 (Upwards as positive):**\nFrom roof (launch point) to maximum height ($v_f = 0$):\n$$v_f = v_i + a\\Delta t\\;\\checkmark$$\n$$0 = 12 + (-9{,}8)\\Delta t\\;\\checkmark$$\n$$\\Delta t = 1{,}22\\text{ s}\\;\\checkmark$$\n\n**OPTION 2 (Downwards as positive):**\n$$v_f = v_i + a\\Delta t\\;\\checkmark$$\n$$0 = -12 + (9{,}8)\\Delta t\\;\\checkmark$$\n$$\\Delta t = 1{,}22\\text{ s}\\;\\checkmark$$\n\n*(Other acceptable methods: Energy / $\\Delta y = 7{,}35\\text{ m}$ followed by $\\Delta y = \\left(\\frac{v_i + v_f}{2}\\right)\\Delta t$ yields $1{,}22\\text{ s}$ to $1{,}23\\text{ s}$.)*",
    final_answer="$1{,}22\\text{ s}$"
)

# 3.2.2
add_item(
    q_ref="3.2.2",
    kind="question",
    marks=4,
    topic="Vertical Projectile Motion - Striking Velocity",
    passage=Q3_PASSAGE,
    question="Calculate the velocity with which the ball strikes the ground.",
    memo="**Marking criteria:**\n* Formula with $v_f$ $\\checkmark$\n* Correct substitution into formula $\\checkmark$\n* Correct final answer: $25{,}18\\text{ m}\\cdot\\text{s}^{-1}\\;\\checkmark$ ($25{,}03\\text{ m}\\cdot\\text{s}^{-1}$ to $25{,}59\\text{ m}\\cdot\\text{s}^{-1}$)\n* Correct direction: downwards $\\checkmark$ *(only if numerical value is given)*\n\n**OPTION 1 (From roof to ground, Upwards as positive):**\nDisplacement $\\Delta y = -25\\text{ m}$:\n$$v_f^2 = v_i^2 + 2a\\Delta y\\;\\checkmark$$\n$$v_f^2 = (12)^2 + 2(-9{,}8)(-25)\\;\\checkmark$$\n$$v_f^2 = 144 + 490 = 634$$\n$$v_f = 25{,}18\\text{ m}\\cdot\\text{s}^{-1}\\;\\checkmark\\text{ downwards}\\;\\checkmark$$\n\n**OPTION 2 (From roof to ground, Downwards as positive):**\n$$v_f^2 = v_i^2 + 2a\\Delta y\\;\\checkmark$$\n$$v_f^2 = (-12)^2 + 2(9{,}8)(25)\\;\\checkmark$$\n$$v_f = 25{,}18\\text{ m}\\cdot\\text{s}^{-1}\\;\\checkmark\\text{ downwards}\\;\\checkmark$$\n\n*(Option using conservation of mechanical energy: $(E_p + E_k)_{\\text{roof}} = (E_p + E_k)_{\\text{ground}} \\implies m(9{,}8)(25) + \\frac{1}{2}m(12)^2 = \\frac{1}{2}mv_f^2$, giving $v_f = 25{,}18\\text{ m}\\cdot\\text{s}^{-1}$ downwards.)*",
    final_answer="$25{,}18\\text{ m}\\cdot\\text{s}^{-1}\\text{ downwards}$"
)

# 3.2.3
add_item(
    q_ref="3.2.3",
    kind="question",
    marks=4,
    topic="Vertical Projectile Motion - Time across Door to Ground",
    passage=Q3_PASSAGE,
    question="Calculate the time it took the ball to move from the top of the door to the ground.",
    memo="*Positive marking from QUESTION 3.2.2*\n\n**Marking criteria:**\n* Substitution into formula to calculate $v$ at the top of the door $\\checkmark$\n* Formula to calculate $\\Delta t$ from top to bottom of door $\\checkmark$\n* Substitution to calculate $\\Delta t$ $\\checkmark$\n* Final answer: $0{,}07\\text{ s}$ to $0{,}08\\text{ s}\\;\\checkmark$\n\n**OPTION 1 (Upwards as positive):**\nThe door is $1{,}9\\text{ m}$ high, located at the ground level, so the top of the door is $1{,}9\\text{ m}$ above the ground, or $\\Delta y = -(25 - 1{,}9) = -23{,}1\\text{ m}$ below the roof:\n$$v_{\\text{top}}^2 = v_i^2 + 2a\\Delta y$$\n$$v_{\\text{top}}^2 = (12)^2 + 2(-9{,}8)(-23{,}1)\\;\\checkmark$$\n$$v_{\\text{top}}^2 = 144 + 452{,}76 = 596{,}76$$\n$$v_{\\text{top}} = -24{,}43\\text{ m}\\cdot\\text{s}^{-1}$$\n\nNow from top of door to ground ($v_f = -25{,}18\\text{ m}\\cdot\\text{s}^{-1}$):\n$$v_f = v_i + a\\Delta t\\;\\checkmark$$\n$$-25{,}18 = -24{,}43 + (-9{,}8)\\Delta t\\;\\checkmark$$\n$$-0{,}75 = -9{,}8\\Delta t$$\n$$\\Delta t = 0{,}08\\text{ s}\\;\\checkmark\\quad (0{,}07\\text{ s} - 0{,}08\\text{ s})$$\n\n**OPTION 2 (Using displacement across the door $\\Delta y = -1{,}9\\text{ m}$):**\n$$v_f^2 = v_i^2 + 2a\\Delta y$$\n$$(-25{,}18)^2 = v_{\\text{top}}^2 + 2(-9{,}8)(-1{,}9)\\;\\checkmark$$\n$$v_{\\text{top}} = 24{,}43\\text{ m}\\cdot\\text{s}^{-1}$$\n$$\\Delta y = \\left(\\frac{v_i + v_f}{2}\\right)\\Delta t\\;\\checkmark$$\n$$-1{,}9 = \\left(\\frac{-24{,}43 + (-25{,}18)}{2}\\right)\\Delta t\\;\\checkmark$$\n$$\\Delta t = 0{,}08\\text{ s}\\;\\checkmark$$",
    final_answer="$0{,}08\\text{ s}$"
)

# 3.3
add_item(
    q_ref="3.3",
    kind="question",
    marks=3,
    topic="Vertical Projectile Motion - Velocity-Time Graph",
    passage=Q3_PASSAGE,
    question="Draw a velocity versus time graph for the motion of the ball from the moment that the ball is thrown upwards until it strikes the ground. Use the ground as zero reference.\n\nClearly indicate the following on your graph:\n* The velocity with which the ball was thrown upwards\n* Time taken by the ball to reach its maximum height\n* The velocity with which the ball strikes the ground",
    memo="*Positive marking from QUESTION 3.2.1 and QUESTION 3.2.2*\n\n**Criteria for graph:**\n* Straight line starting at $v = 12\\text{ m}\\cdot\\text{s}^{-1}$ with negative final velocity (or starting at $v = -12\\text{ m}\\cdot\\text{s}^{-1}$ with positive final velocity) $\\checkmark$\n* Straight line cuts time axis at time calculated in Question 3.2.1 ($t = 1{,}22\\text{ s}$) $\\checkmark$\n* Correct final velocity as calculated in Question 3.2.2 is indicated ($-25{,}18\\text{ m}\\cdot\\text{s}^{-1}$ or $+25{,}18\\text{ m}\\cdot\\text{s}^{-1}$) $\\checkmark$\n\n*(Graph description:*\n*If upwards is positive:* A straight line with a constant negative slope of $-9{,}8\\text{ m}\\cdot\\text{s}^{-2}$, starting at $(0; 12)$, crossing the time axis at $(1{,}22; 0)$, and ending at the strike time with a final velocity of $-25{,}18\\text{ m}\\cdot\\text{s}^{-1}$.\n*If downwards is positive:* A straight line with a constant positive slope of $+9{,}8\\text{ m}\\cdot\\text{s}^{-2}$, starting at $(0; -12)$, crossing the time axis at $(1{,}22; 0)$, and ending at the strike time with a final velocity of $+25{,}18\\text{ m}\\cdot\\text{s}^{-1}$.*)*",
    final_answer="A velocity-time graph showing a straight line with constant negative gradient ($-9{,}8\\text{ m}\\cdot\\text{s}^{-2}$, taking upwards as positive) starting at $v = 12\\text{ m}\\cdot\\text{s}^{-1}$ at $t = 0\\text{ s}$, crossing the time axis at $t = 1{,}22\\text{ s}$, and ending at $v = -25{,}18\\text{ m}\\cdot\\text{s}^{-1}$."
)

# ==========================================
# QUESTION 4: MOMENTUM AND IMPULSE (14 MARKS)
# ==========================================

Q4_PASSAGE = (
    "Trolley X of mass $1{,}2\\text{ kg}$ travels at $8\\text{ m}\\cdot\\text{s}^{-1}$ east and collides with "
    "trolley Y of mass $0{,}5\\text{ kg}$ which is initially at rest.\n\n"
    "Ignore all frictional effects.\n\n"
    "The velocity-time graph shows the velocity of trolley X before, during and after the collision with trolley Y:\n"
    "- Before $t = 20{,}1\\text{ s}$: trolley X travels at a constant velocity of $8\\text{ m}\\cdot\\text{s}^{-1}$ east.\n"
    "- From $t = 20{,}1\\text{ s}$ to $t = 20{,}2\\text{ s}$: the collision takes place, during which the velocity of "
    "trolley X decreases uniformly from $8\\text{ m}\\cdot\\text{s}^{-1}$ to $4\\text{ m}\\cdot\\text{s}^{-1}$ east "
    "($\\Delta t = 0{,}1\\text{ s}$).\n"
    "- After $t = 20{,}2\\text{ s}$: trolley X travels at a constant velocity of $4\\text{ m}\\cdot\\text{s}^{-1}$ east."
)

# 4.1
add_item(
    q_ref="4.1",
    kind="question",
    marks=2,
    topic="Momentum and Impulse - Conservation of Linear Momentum",
    passage=Q4_PASSAGE,
    question="State the principle of conservation of linear momentum.",
    memo="* In an isolated/closed system the total (linear) momentum is conserved/remains constant. $\\checkmark\\checkmark$ *(2 or 0)*",
    final_answer="In an isolated (closed) system, the total linear momentum is conserved (remains constant)."
)

# 4.2.1
add_item(
    q_ref="4.2.1",
    kind="question",
    marks=4,
    topic="Momentum and Impulse - Velocity after Collision",
    passage=Q4_PASSAGE,
    question="Calculate the magnitude of the velocity of trolley Y immediately after the collision.",
    memo="**OPTION 1 (East as positive):**\n$$\\sum p_i = \\sum p_f$$\n$$m_X v_{iX} + m_Y v_{iY} = m_X v_{fX} + m_Y v_{fY}$$\n$$(1{,}2)(8)\\;\\checkmark + (0{,}5)(0) = (1{,}2)(4) + (0{,}5)(v_{fY})\\;\\checkmark$$\n$$9{,}6 = 4{,}8 + 0{,}5 v_{fY}$$\n$$0{,}5 v_{fY} = 4{,}8$$\n$$v_{fY} = 9{,}6\\text{ m}\\cdot\\text{s}^{-1}\\;\\checkmark$$\n*(Formula $\\checkmark$, substitution LHS $\\checkmark$, substitution RHS $\\checkmark$, answer $\\checkmark$)*\n\n**OPTION 2 (Using change in momentum $\\Delta p_X = -\\Delta p_Y$):**\n$$m_X(v_{fX} - v_{iX}) = -m_Y(v_{fY} - v_{iY})$$\n$$1{,}2(4 - 8)\\;\\checkmark = -0{,}5(v_{fY} - 0)\\;\\checkmark$$\n$$-4{,}8 = -0{,}5 v_{fY}$$\n$$v_{fY} = 9{,}6\\text{ m}\\cdot\\text{s}^{-1}\\;\\checkmark$$",
    final_answer="$9{,}6\\text{ m}\\cdot\\text{s}^{-1}$"
)

# 4.2.2
add_item(
    q_ref="4.2.2",
    kind="question",
    marks=3,
    topic="Momentum and Impulse - Average Net Force During Collision",
    passage=Q4_PASSAGE,
    question="Calculate the magnitude of the average net force that trolley X exerts on trolley Y during the collision.",
    memo="*Positive marking from QUESTION 4.2.1*\n\n**OPTION 1 (Impulse on X, East as positive):**\n$$F_{\\text{net}}\\Delta t = \\Delta p = m(v_f - v_i)\\;\\checkmark$$\n$$F_{\\text{net}}(0{,}1) = 1{,}2(4 - 8)\\;\\checkmark$$\n$$F_{\\text{net}}(0{,}1) = -4{,}8$$\n$$F_{\\text{net}} = -48\\text{ N}$$\n$$\\text{Magnitude: } F_{\\text{net}} = 48\\text{ N}\\;\\checkmark$$\n\n**OPTION 2 (Impulse on Y):**\n$$F_{\\text{net}}\\Delta t = m(v_f - v_i)\\;\\checkmark$$\n$$F_{\\text{net}}(0{,}1) = 0{,}5(9{,}6 - 0)\\;\\checkmark$$\n$$F_{\\text{net}} = 48\\text{ N}\\;\\checkmark$$\n\n**OPTION 3 (Newton's Second Law $F_{\\text{net}} = ma$):**\n$$a = \\frac{v_f - v_i}{\\Delta t} = \\frac{4 - 8}{0{,}1} = -40\\text{ m}\\cdot\\text{s}^{-2}$$\n$$F_{\\text{net}} = ma\\;\\checkmark = (1{,}2)(-40)\\;\\checkmark = -48\\text{ N}$$\n$$\\text{Magnitude: } F_{\\text{net}} = 48\\text{ N}\\;\\checkmark$$",
    final_answer="$48\\text{ N}$"
)

# 4.3
add_item(
    q_ref="4.3",
    kind="question",
    marks=5,
    topic="Momentum and Impulse - Elastic vs Inelastic Collision",
    passage=Q4_PASSAGE,
    question="Is the collision ELASTIC or INELASTIC?\n\nExplain the answer by means of suitable calculations.",
    memo="*Positive marking from QUESTION 4.2.1*\n\n* Inelastic $\\checkmark$\n* Formula: $E_k = \\frac{1}{2}mv^2\\;\\checkmark$\n* Initial kinetic energy:\n$$\\sum E_{ki} = \\frac{1}{2}m_X v_{iX}^2 + \\frac{1}{2}m_Y v_{iY}^2 = \\frac{1}{2}(1{,}2)(8)^2 + 0\\;\\checkmark = 38{,}4\\text{ J}$$\n* Final kinetic energy:\n$$\\sum E_{kf} = \\frac{1}{2}m_X v_{fX}^2 + \\frac{1}{2}m_Y v_{fY}^2 = \\frac{1}{2}(1{,}2)(4)^2 + \\frac{1}{2}(0{,}5)(9{,}6)^2\\;\\checkmark = 9{,}6 + 23{,}04 = 32{,}64\\text{ J}$$\n* Comparison: $\\sum E_{ki} \\neq \\sum E_{kf}$ (or $\\sum E_{kf} < \\sum E_{ki}$), therefore total kinetic energy is not conserved $\\checkmark$.\n\n*(Note: If a candidate starts by assuming conservation of kinetic energy: max 4/5 marks.)*",
    final_answer="Inelastic, because total kinetic energy before the collision ($38{,}4\\text{ J}$) does not equal total kinetic energy after the collision ($32{,}64\\text{ J}$)."
)

# ==========================================
# QUESTION 5: WORK, ENERGY AND POWER (15 MARKS)
# ==========================================

Q5_PASSAGE = (
    "A $12\\text{ kg}$ block is initially at rest at point A at the bottom of a ROUGH inclined plane. "
    "The block is pulled up the incline by a constant force $F$ acting parallel to the incline. The block "
    "reaches point B, which is at a vertical height of $4{,}5\\text{ m}$ above the horizontal, with a speed "
    "of $2{,}25\\text{ m}\\cdot\\text{s}^{-1}$, as shown in the diagram.\n\n"
    "Later, the same constant force $F$ moves the block at a CONSTANT VELOCITY across a rough horizontal "
    "surface from point B to point C. Force $F$ acts parallel to the horizontal surface. The magnitude of "
    "the constant frictional force acting on the block while moving from point B to point C is $42\\text{ N}$ "
    "LARGER than the magnitude of the constant frictional force acting on the block when it moves from "
    "point A to point B ($f_{BC} = f_{AB} + 42\\text{ N}$)."
)

# 5.1
add_item(
    q_ref="5.1",
    kind="question",
    marks=2,
    topic="Work, Energy and Power - Non-conservative Force Definition",
    passage=Q5_PASSAGE,
    question="Define the term non-conservative force.",
    memo="* A force is non-conservative if the work done by the force on an object (which is moving between two points) depends on the path taken. $\\checkmark\\checkmark$\n\n**OR**\n\n* A force is non-conservative if the work it does in moving an object around a closed path is non-zero. $\\checkmark\\checkmark$ *(2 or 0)*\n\n*(Note: If 'work done' is omitted, award 0/2.)*",
    final_answer="A force for which the work done in moving an object between two points depends on the path taken."
)

# 5.2
add_item(
    q_ref="5.2",
    kind="question",
    marks=4,
    topic="Work, Energy and Power - Free-body Diagram on Inclined Plane",
    passage=Q5_PASSAGE,
    question="Draw a labelled free-body diagram for the block when it is pulled up the inclined plane.",
    memo="* $F$ / $F_A$ / Applied force / tension / $F_T$ (upwards along the incline) $\\checkmark$\n* $N$ / $F_N$ / normal force (perpendicular to the incline, directed upwards) $\\checkmark$\n* $f$ / $F_f$ / $f_k$ / kinetic friction (downwards along the incline) $\\checkmark$\n* $w$ / $F_g$ / $F_w$ / gravitational force / weight / $mg$ / $117{,}6\\text{ N}$ (vertically downwards) $\\checkmark$\n*(OR if components of weight are shown instead of $w$: $F_{g\\parallel}$ down incline and $F_{g\\perp}$ perpendicular into incline: 1 mark for both)*\n\n*Marking notes:*\n* Mark awarded for label and arrow.\n* Any additional force: max $3/4$.\n* If everything correct, but no arrows: max $3/4$.\n* If force(s) do not make contact with the dot: max $3/4$.",
    final_answer="Four labelled forces: Applied force ($F$) directed up along the incline; Normal force ($N$) perpendicular to the incline surface; Kinetic friction ($f$ or $f_k$) directed down along the incline; Weight ($w$ or $F_g$) directed vertically downwards."
)

# 5.3
add_item(
    q_ref="5.3",
    kind="question",
    marks=4,
    topic="Work, Energy and Power - Work Done by Non-conservative Forces",
    passage=Q5_PASSAGE,
    question="Calculate the total work done on the block by the NON-CONSERVATIVE forces when the block moved from point A to point B.",
    memo="**OPTION 1 (Work-Energy Principle):**\n$$W_{nc} = \\Delta E_k + \\Delta E_p\\;\\checkmark$$\n$$W_{nc} = \\frac{1}{2}m(v_f^2 - v_i^2) + mg(h_f - h_i)$$\n$$W_{nc} = \\frac{1}{2}(12)(2{,}25^2 - 0)\\;\\checkmark + (12)(9{,}8)(4{,}5 - 0)\\;\\checkmark$$\n$$W_{nc} = 30{,}375 + 529{,}2 = 559{,}58\\text{ J}\\;\\checkmark\\quad (559{,}575\\text{ J})$$\n\n**OPTION 2 (Using $W_{\\text{net}} = W_{nc} + W_c$):**\n$$W_{\\text{net}} = \\Delta E_k = \\frac{1}{2}(12)(2{,}25)^2 - 0 = 30{,}375\\text{ J}\\;\\checkmark$$\n$$W_c = W_g = -(12)(9{,}8)(4{,}5) = -529{,}2\\text{ J}$$\n$$W_{\\text{net}} = W_{nc} + W_c\\;\\checkmark$$\n$$30{,}375 = W_{nc} + (-529{,}2)\\;\\checkmark$$\n$$W_{nc} = 559{,}58\\text{ J}\\;\\checkmark$$",
    final_answer="$559{,}58\\text{ J}$"
)

# 5.4
add_item(
    q_ref="5.4",
    kind="question",
    marks=5,
    topic="Work, Energy and Power - Distance Along Incline Calculation",
    passage=Q5_PASSAGE,
    question="Calculate the distance from point A to point B.",
    memo="*Positive marking from QUESTION 5.3*\n\n**Marking criteria for OPTION 1:**\n* Formula for $W_{nc}$ $\\checkmark$\n* Correct substitution of $559{,}58\\text{ J}$ in $W_{nc}$ along inclined plane $\\checkmark$\n* Correct force equation and substitution of 0 for $F_{\\text{net}}$ OR $F = f_2$ on horizontal plane $\\checkmark$\n* Relating the two frictional forces (substitution of $f_1 + 42$ for $f_2$) $\\checkmark$\n* Correct answer: $13{,}32\\text{ m}\\;\\checkmark$\n\n**OPTION 1:**\nAlong the horizontal surface BC (constant velocity, $a = 0$):\n$$F_{\\text{net}} = 0 \\implies F - f_2 = 0\\;\\checkmark$$\nGiven $f_2 = f_1 + 42$:\n$$F - (f_1 + 42) = 0\\;\\checkmark \\implies F - f_1 = 42\\text{ N}$$\n\nAlong the incline AB:\n$$W_{nc} = W_F + W_{f1}$$\n$$W_{nc} = F\\Delta x\\cos 0^\\circ + f_1\\Delta x\\cos 180^\\circ$$\n$$559{,}58\\;\\checkmark = (F - f_1)\\Delta x$$\n$$559{,}58 = (42)\\Delta x$$\n$$\\Delta x = \\frac{559{,}58}{42} = 13{,}32\\text{ m}\\;\\checkmark\\quad (13{,}323\\text{ m})$$\n\n**OPTION 2 (Using $W_{nc} = \\Delta E_k + \\Delta E_p$):**\n$$F - f_2 = 0\\;\\checkmark \\implies F = f_1 + 42\\;\\checkmark$$\n$$(F - f_1)\\Delta x\\cos 0^\\circ = [\\frac{1}{2}m(v_f^2 - v_i^2)] + [mg(h_f - h_i)]\\;\\checkmark$$\n$$(f_1 + 42 - f_1)\\Delta x = [\\frac{1}{2}(12)(2{,}25)^2 - 0] + [(12)(9{,}8)(4{,}5) - 0]\\;\\checkmark$$\n$$42\\Delta x = 559{,}575$$\n$$\\Delta x = 13{,}32\\text{ m}\\;\\checkmark$$",
    final_answer="$13{,}32\\text{ m}$"
)

# ==========================================
# QUESTION 6: DOPPLER EFFECT (10 MARKS)
# ==========================================

Q6_PASSAGE = (
    "A learner investigates the relationship between the observed frequency and the frequency of sound waves "
    "emitted by a stationary source.\n\n"
    "The learner moves towards the source at a constant velocity and records the observed frequency ($f_L$) "
    "for a given source frequency ($f_S$). This process is repeated for different frequencies of the source, "
    "with the learner moving at the same constant velocity each time.\n\n"
    "The graph shows how the observed frequency ($f_L$ in Hz) changes as the frequency of sound waves emitted "
    "by the source ($f_S$ in Hz) changes. The graph is a straight line passing through the origin $(0, 0)$."
)

# 6.1
add_item(
    q_ref="6.1",
    kind="question",
    marks=1,
    topic="Doppler Effect - Phenomenon Identification",
    passage=Q6_PASSAGE,
    question="Name the phenomenon illustrated by the graph.",
    memo="* Doppler Effect $\\checkmark$",
    final_answer="Doppler Effect"
)

# 6.2
add_item(
    q_ref="6.2",
    kind="question",
    marks=1,
    topic="Doppler Effect - Medical Application",
    passage=Q6_PASSAGE,
    question="Name ONE application in the medical field of the phenomenon in QUESTION 6.1.",
    memo="* Measurement of foetal heartbeat $\\checkmark$\n\n**OR**\n\n* Measurement of blood flow $\\checkmark$\n\n**OR**\n\n* Doppler flow meter $\\checkmark$",
    final_answer="Measurement of the rate of blood flow (Doppler flow meter) or monitoring fetal heartbeat"
)

# 6.3
add_item(
    q_ref="6.3",
    kind="question",
    marks=1,
    topic="Doppler Effect - Proportionality",
    passage=Q6_PASSAGE,
    question="Write down the type of proportionality that exists between $f_L$ and $f_S$, as illustrated by the graph.",
    memo="* Directly proportional / Direct proportionality / $f_L \\propto f_S\\;\\checkmark$",
    final_answer="Direct proportionality (directly proportional)"
)

# 6.4
add_item(
    q_ref="6.4",
    kind="question",
    marks=5,
    topic="Doppler Effect - Observer Velocity Calculation",
    passage=Q6_PASSAGE,
    question="The gradient of the graph obtained is found to be 1,06.\n\nIf the speed of sound in air is $340\\text{ m}\\cdot\\text{s}^{-1}$, calculate the magnitude of the velocity at which the learner approaches the source.",
    memo="**Marking criteria:**\n* Doppler formula $\\checkmark$\n* Correct substitution for $v$ and $v_S$ $\\checkmark$\n* Substitution for $\\frac{f_L}{f_S} = 1{,}06$ OR $f_L = 1{,}06 f_S$ $\\checkmark\\checkmark$\n* Final answer: $20{,}4\\text{ m}\\cdot\\text{s}^{-1}\\;\\checkmark$\n\n**OPTION 1:**\n$$f_L = \\left(\\frac{v \\pm v_L}{v \\pm v_S}\\right)f_S\\;\\checkmark$$\nSince the listener approaches a stationary source ($v_S = 0$):\n$$f_L = \\left(\\frac{v + v_L}{v}\\right)f_S$$\n$$\\frac{f_L}{f_S} = \\frac{v + v_L}{v}$$\nSince the gradient of the graph is $\\frac{f_L}{f_S} = 1{,}06$:\n$$1{,}06\\;\\checkmark\\checkmark = \\frac{340 + v_L}{340}\\;\\checkmark$$\n$$340 + v_L = 1{,}06 \\times 340$$\n$$340 + v_L = 360{,}4$$\n$$v_L = 20{,}4\\text{ m}\\cdot\\text{s}^{-1}\\;\\checkmark$$\n\n**OPTION 2:**\n$$\\text{Gradient} = \\frac{f_L}{f_S} = 1{,}06 \\implies f_L = 1{,}06 f_S$$\n$$1{,}06 f_S = \\left(\\frac{340 + v_L}{340}\\right)f_S\\;\\checkmark\\checkmark$$\n$$v_L = 20{,}4\\text{ m}\\cdot\\text{s}^{-1}\\;\\checkmark$$",
    final_answer="$20{,}4\\text{ m}\\cdot\\text{s}^{-1}$"
)

# 6.5
add_item(
    q_ref="6.5",
    kind="question",
    marks=2,
    topic="Doppler Effect - Graph Comparison at Higher Velocity",
    passage=Q6_PASSAGE,
    question="The investigation is now repeated with the learner moving at a HIGHER constant velocity towards the sound source.\n\nCopy the graph above in your ANSWER BOOK and label it as A. On the same set of axes, sketch the graph that will be obtained when the learner is moving at the HIGHER velocity. Label this graph as B.",
    memo="**Marking criteria:**\n* Graph B is a straight line starting at the origin $(0, 0)$ $\\checkmark$\n* Gradient of graph B is greater than the gradient of graph A $\\checkmark$\n\n*(Explanation: The gradient equals $\\frac{v + v_L}{v} = 1 + \\frac{v_L}{v}$. An increased velocity $v_L$ results in a larger gradient/steeper line that still passes through the origin.)*",
    final_answer="A straight line B starting at the origin $(0, 0)$ with a steeper gradient (larger slope) than graph A."
)

# ==========================================
# QUESTION 7: ELECTROSTATICS (17 MARKS)
# ==========================================

Q7_PASSAGE = (
    "A charged sphere M is suspended from a ceiling by a light inextensible, insulated string.\n\n"
    "Another charged sphere N, of mass $2{,}04 \\times 10^{-3}\\text{ kg}$ and carrying a charge of "
    "$+8{,}6 \\times 10^{-8}\\text{ C}$, hangs STATIONARY vertically below sphere M in mid-air. "
    "The centres of the spheres are $0{,}3\\text{ m}$ apart, as shown in the diagram.\n\n"
    "Later, reference point X is positioned $0{,}1\\text{ m}$ vertically below the centre of sphere N."
)

# 7.1
add_item(
    q_ref="7.1",
    kind="question",
    marks=2,
    topic="Electrostatics - Coulomb's Law Definition",
    passage=Q7_PASSAGE,
    question="State Coulomb's law in words.",
    memo="* The magnitude of the electrostatic force exerted by one point charge on another is directly proportional to the product of the magnitudes of the charges and inversely proportional to the square of the distance between them. $\\checkmark\\checkmark$\n\n*(2 or 0)*",
    final_answer="The magnitude of the electrostatic force exerted by one point charge on another is directly proportional to the product of the magnitudes of the charges and inversely proportional to the square of the distance between them."
)

# 7.2
add_item(
    q_ref="7.2",
    kind="question",
    marks=1,
    topic="Electrostatics - Charge Polarity",
    passage=Q7_PASSAGE,
    question="State whether the charge on sphere M is POSITIVE or NEGATIVE.",
    memo="* Negative $\\checkmark$",
    final_answer="Negative"
)

# 7.3
add_item(
    q_ref="7.3",
    kind="question",
    marks=2,
    topic="Electrostatics - Free-body Diagram",
    passage=Q7_PASSAGE,
    question="Draw a labelled free-body diagram for sphere N.",
    memo="* $F_E$ / $F_{\\text{electrostatic}}$ / $F$ / $F_{\\text{M on N}}$ / electrostatic force (directed vertically upwards) $\\checkmark$\n* $w$ / $F_g$ / $mg$ / gravitational force / weight / gravity (directed vertically downwards) $\\checkmark$\n\n*Marking notes:*\n* Mark awarded for label and arrow.\n* Do not penalise for length of arrows.\n* Any additional force: max $1/2$.\n* If arrows are omitted but correctly labelled: max $1/2$.\n* If force(s) do not make contact with the dot: max $1/2$.",
    final_answer="Two labelled vertical collinear forces: Electrostatic force ($F_E$ or $F_{\\text{electrostatic}}$) pointing vertically upwards; Gravitational force ($w$ or $F_g$) pointing vertically downwards."
)

# 7.4
add_item(
    q_ref="7.4",
    kind="question",
    marks=5,
    topic="Electrostatics - Charge Magnitude Calculation",
    passage=Q7_PASSAGE,
    question="Calculate the magnitude of the charge on sphere M.",
    memo="**Marking criteria:**\n* Correct substitution to calculate weight of N: $F_g = mg\\;\\checkmark$\n* Coulomb's formula: $F = \\frac{k Q_1 Q_2}{r^2}\\;\\checkmark$\n* Equating forces ($F_{\\text{net}} = 0 \\implies mg = \\frac{k Q_1 Q_2}{r^2}$ or $0{,}02 = \\frac{k Q_1 Q_2}{r^2}$) $\\checkmark$\n* Correct substitution into Coulomb's formula $\\checkmark$\n* Correct final answer: $2{,}33 \\times 10^{-6}\\text{ C}\\;\\checkmark$ ($2{,}32 \\times 10^{-6}\\text{ C}$ to $2{,}33 \\times 10^{-6}\\text{ C}$)\n\n**Calculation:**\n$$F_g = mg = (2{,}04 \\times 10^{-3})(9{,}8)\\;\\checkmark = 0{,}02\\text{ N}\\quad (0{,}019992\\text{ N})$$\n$$F = \\frac{k Q_M Q_N}{r^2}\\;\\checkmark$$\nSince sphere N is stationary:\n$$F_{\\text{net}} = 0 \\implies F_E = F_g\\;\\checkmark$$\n$$\\frac{(9 \\times 10^9)(Q_M)(8{,}6 \\times 10^{-8})}{(0{,}3)^2}\\;\\checkmark = 0{,}02$$\n$$\\frac{774 Q_M}{0{,}09} = 0{,}02$$\n$$8600 Q_M = 0{,}02$$\n$$Q_M = 2{,}33 \\times 10^{-6}\\text{ C}\\;\\checkmark\\quad (2{,}32 \\times 10^{-6}\\text{ C})$$",
    final_answer="$2{,}33 \\times 10^{-6}\\text{ C}$"
)

# 7.5.1
add_item(
    q_ref="7.5.1",
    kind="question",
    marks=1,
    topic="Newton's Third Law & Electrostatics - Force Comparison: Magnitude",
    passage=Q7_PASSAGE,
    question="How does the electrostatic force that sphere M exerts on sphere N compare to that exerted by sphere N on sphere M with respect to:\n\nMagnitude",
    memo="* Equal / Same $\\checkmark$",
    final_answer="Equal to (the same)"
)

# 7.5.2
add_item(
    q_ref="7.5.2",
    kind="question",
    marks=1,
    topic="Newton's Third Law & Electrostatics - Force Comparison: Direction",
    passage=Q7_PASSAGE,
    question="How does the electrostatic force that sphere M exerts on sphere N compare to that exerted by sphere N on sphere M with respect to:\n\nDirection",
    memo="* Opposite / upwards $\\checkmark$",
    final_answer="Opposite"
)

# 7.6
add_item(
    q_ref="7.6",
    kind="question",
    marks=5,
    topic="Electric Fields - Net Electric Field Calculation",
    passage=Q7_PASSAGE,
    question="Point X is $0{,}1\\text{ m}$ vertically below the centre of sphere N, as shown in the diagram.\n\nCalculate the net electric field at point X.",
    memo="*Positive marking from QUESTION 7.4*\n\n**Marking criteria:**\n* Formula for $E = \\frac{kQ}{r^2}\\;\\checkmark$\n* Correct substitution for M OR N $\\checkmark$\n* Subtraction of $E_M - E_N$ OR $E_N - E_M\\;\\checkmark$\n* Correct final answer: $5{,}37 \\times 10^4\\text{ N}\\cdot\\text{C}^{-1}\\;\\checkmark$ ($5{,}31 \\times 10^4\\text{ N}\\cdot\\text{C}^{-1}$ to $5{,}37 \\times 10^4\\text{ N}\\cdot\\text{C}^{-1}$)\n* Correct direction: upwards / towards M $\\checkmark$\n\n**Calculation:**\nDistance from N to X: $r_N = 0{,}1\\text{ m}$.\nDistance from M to X: $r_M = 0{,}3 + 0{,}1 = 0{,}4\\text{ m}$.\nFormula: $E = \\frac{kQ}{r^2}\\;\\checkmark$\n\n- Field due to positive sphere N at point X (directed downwards, away from N):\n$$E_N = \\frac{(9 \\times 10^9)(8{,}6 \\times 10^{-8})}{(0{,}1)^2} = 77\\,400\\text{ N}\\cdot\\text{C}^{-1}\\text{ downwards}$$\n\n- Field due to negative sphere M at point X (directed upwards, towards M):\n$$E_M = \\frac{(9 \\times 10^9)(2{,}33 \\times 10^{-6})}{(0{,}4)^2}\\;\\checkmark = 131\\,062{,}5\\text{ N}\\cdot\\text{C}^{-1}\\text{ upwards}$$\n\nTaking upwards as positive:\n$$E_{\\text{net}} = E_M - E_N\\;\\checkmark$$\n$$E_{\\text{net}} = 131\\,062{,}5 - 77\\,400 = 53\\,662{,}5\\text{ N}\\cdot\\text{C}^{-1}\\;\\checkmark\\text{ upwards}\\;\\checkmark$$\n$$\\text{or } 5{,}37 \\times 10^4\\text{ N}\\cdot\\text{C}^{-1}\\text{ upwards (towards M)}$$",
    final_answer="$5{,}37 \\times 10^4\\text{ N}\\cdot\\text{C}^{-1}\\text{ upwards (towards M)}$"
)

# ==========================================
# QUESTION 8: ELECTRIC CIRCUITS (20 MARKS)
# ==========================================

Q8_PASSAGE = (
    "The circuit diagram shows four resistors connected to a battery of emf $\\mathcal{E}$ and internal resistance $r$. "
    "The resistances of the ammeter and the connecting wires are negligible, while the voltmeters have very high resistances.\n\n"
    "Circuit details:\n"
    "- A battery of emf $\\mathcal{E}$ and internal resistance $r$.\n"
    "- Voltmeter $V_1$ is connected across the terminals of the battery.\n"
    "- Ammeter A is in the main circuit line.\n"
    "- Resistor branch 1 contains a $3\\,\\Omega$ resistor and a $2\\,\\Omega$ resistor connected in series ($R_{3+2} = 5\\,\\Omega$).\n"
    "- Resistor branch 2 contains switch S connected in series with a $1\\,\\Omega$ resistor.\n"
    "- Branch 1 and Branch 2 are in parallel with each other.\n"
    "- A $4\\,\\Omega$ resistor is connected in series with this parallel combination.\n"
    "- Voltmeter $V_2$ is connected across the parallel combination."
)

# 8.1
add_item(
    q_ref="8.1",
    kind="question",
    marks=2,
    topic="Electric Circuits - Ohm's Law Definition",
    passage=Q8_PASSAGE,
    question="State Ohm's law in words.",
    memo="* The potential difference across a conductor is directly proportional to the current in the conductor at constant temperature (provided temperature and all other physical conditions are constant). $\\checkmark\\checkmark$\n\n**OR**\n\n* The ratio of potential difference to current is constant at constant temperature. $\\checkmark\\checkmark$\n\n**OR**\n\n* The current in a conductor is directly proportional to the potential difference across the conductor at constant temperature. $\\checkmark\\checkmark$\n\n*(2 or 0)*",
    final_answer="The potential difference across a conductor is directly proportional to the current in the conductor at constant temperature."
)

# 8.2.1
add_item(
    q_ref="8.2.1",
    kind="question",
    marks=4,
    topic="Electric Circuits - Total External Resistance Calculation",
    passage=Q8_PASSAGE,
    question="Switch S is CLOSED.\n\nThe reading on the ammeter is $3{,}5\\text{ A}$.\n\nCalculate the total external resistance of the circuit.",
    memo="**Marking criteria:**\n* Formula for parallel combination $\\checkmark$\n* Correct substitution into parallel formula ($R_1 = 1\\,\\Omega$, $R_2 = 3 + 2 = 5\\,\\Omega$) $\\checkmark$\n* Adding the $4\\,\\Omega$ series resistor $\\checkmark$\n* Correct final answer: $4{,}83\\,\\Omega\\;\\checkmark$\n\n**OPTION 1:**\n$$\\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2}\\;\\checkmark$$\n$$\\frac{1}{R_p} = \\frac{1}{1} + \\frac{1}{5}\\;\\checkmark$$\n$$R_p = \\frac{5}{6} \\approx 0{,}83\\,\\Omega$$\n$$R_{\\text{ext}} = R_p + 4\\;\\checkmark = 0{,}83 + 4 = 4{,}83\\,\\Omega\\;\\checkmark$$\n\n**OPTION 2:**\n$$R_p = \\frac{R_1 R_2}{R_1 + R_2}\\;\\checkmark = \\frac{(1)(5)}{1 + 5}\\;\\checkmark = 0{,}83\\,\\Omega$$\n$$R_{\\text{ext}} = R_p + 4\\;\\checkmark = 0{,}83 + 4 = 4{,}83\\,\\Omega\\;\\checkmark$$",
    final_answer="$4{,}83\\,\\Omega$"
)

# 8.2.2
add_item(
    q_ref="8.2.2",
    kind="question",
    marks=3,
    topic="Electric Circuits - Voltmeter Reading Calculation",
    passage=Q8_PASSAGE,
    question="Calculate the reading on voltmeter $V_1$.",
    memo="*Positive marking from QUESTION 8.2.1*\n\n**OPTION 1:**\n$$R = \\frac{V}{I}\\;\\checkmark$$\n$$4{,}83 = \\frac{V_1}{3{,}5}\\;\\checkmark$$\n$$V_1 = (4{,}83)(3{,}5) = 16{,}91\\text{ V}\\;\\checkmark\\quad (16{,}92\\text{ V})$$\n\n**OPTION 2:**\n$$V_p = I R_p = (3{,}5)(0{,}83) = 2{,}91\\text{ V}$$\n$$V_{4\\Omega} = I R_4 = (3{,}5)(4) = 14\\text{ V}$$\n$$V_1 = V_p + V_{4\\Omega} = 2{,}91 + 14 = 16{,}91\\text{ V}\\;\\checkmark$$",
    final_answer="$16{,}91\\text{ V}$"
)

# 8.2.3
add_item(
    q_ref="8.2.3",
    kind="question",
    marks=1,
    topic="Electric Circuits - Comparing Voltmeter Readings",
    passage=Q8_PASSAGE,
    question="How does the reading on voltmeter $V_2$ compare to the reading on voltmeter $V_1$? Choose from SMALLER THAN, EQUAL TO or GREATER THAN.",
    memo="* Smaller than $\\checkmark$",
    final_answer="Smaller than"
)

# 8.3.1
add_item(
    q_ref="8.3.1",
    kind="question",
    marks=2,
    topic="Electric Circuits - Emf Definition",
    passage=Q8_PASSAGE,
    question="A learner concludes that the emf of the battery is equal to the reading on voltmeter $V_1$.\n\nDefine the term emf.",
    memo="* Maximum work done by the battery per unit charge. $\\checkmark\\checkmark$\n\n**OR**\n\n* Maximum energy supplied by the battery per unit charge. $\\checkmark\\checkmark$\n\n**OR**\n\n* The total amount of electric energy supplied by the battery per coulomb/per unit charge. $\\checkmark\\checkmark$\n\n*(2 or 0)*",
    final_answer="Maximum work done by the battery per unit charge."
)

# 8.3.2
add_item(
    q_ref="8.3.2",
    kind="question",
    marks=1,
    topic="Electric Circuits - Emf vs Terminal Potential Difference",
    passage=Q8_PASSAGE,
    question="Is the learner's conclusion CORRECT? Choose from YES or NO.",
    memo="* No $\\checkmark$",
    final_answer="No"
)

# 8.3.3
add_item(
    q_ref="8.3.3",
    kind="question",
    marks=1,
    topic="Electric Circuits - Internal Resistance & Lost Volts",
    passage=Q8_PASSAGE,
    question="Give a reason for the answer to QUESTION 8.3.2.",
    memo="* The battery has internal resistance. $\\checkmark$\n\n**OR**\n\n* Some energy per coulomb of charge / volts is used to overcome internal resistance / there is a potential drop / 'lost volts' inside the battery ($V_{\\text{internal}} = Ir$). $\\checkmark$\n\n**OR**\n\n* $\\mathcal{E} = V_{\\text{ext}} + V_{\\text{int}}$ (or $\\mathcal{E} > V_{\\text{ext}}$). $\\checkmark$",
    final_answer="The battery has internal resistance, so when current flows there is an internal potential drop ('lost volts'), making the terminal potential difference smaller than the emf ($\\mathcal{E} = V_{\\text{ext}} + Ir$)."
)

# 8.4.1
add_item(
    q_ref="8.4.1",
    kind="question",
    marks=1,
    topic="Electric Circuits - Effect of Circuit Changes: Power",
    passage="Switch S is now removed and replaced by voltmeter $V_2$, as shown in the updated circuit diagram.",
    question="How will the power dissipated by the $4\\,\\Omega$ resistor change?\n\n(Choose from INCREASES, DECREASES or REMAINS THE SAME.)",
    memo="* Decreases $\\checkmark$",
    final_answer="Decreases"
)

# 8.4.2
add_item(
    q_ref="8.4.2",
    kind="question",
    marks=1,
    topic="Electric Circuits - Effect of Circuit Changes: Terminal Potential Difference",
    passage="Switch S is now removed and replaced by voltmeter $V_2$, as shown in the updated circuit diagram.",
    question="How will the reading on voltmeter $V_1$ change?\n\n(Choose from INCREASES, DECREASES or REMAINS THE SAME.)",
    memo="* Increases $\\checkmark$",
    final_answer="Increases"
)

# 8.5
add_item(
    q_ref="8.5",
    kind="question",
    marks=4,
    topic="Electric Circuits - Qualitative Analysis of Internal Resistance",
    passage="Switch S is now removed and replaced by voltmeter $V_2$, as shown in the updated circuit diagram.",
    question="Explain the answer to QUESTION 8.4.2.",
    memo="When the voltmeter $V_2$ replaces switch S:\n* No/very little current flows through the $1\\,\\Omega$ branch (the voltmeter has very high resistance / the branch is disabled) OR the resistance of the parallel branch increases $\\checkmark$\n* Total external resistance of the circuit increases $\\checkmark$\n* Total current in the circuit decreases $\\checkmark$\n* $V_{\\text{internal}}$ / internal volts / $V_{\\text{lost}}$ decreases ($V_{\\text{int}} = Ir$) $\\checkmark$\nTherefore, the external terminal voltage $V_1 = \\mathcal{E} - Ir$ increases for a constant emf.",
    final_answer="When voltmeter $V_2$ replaces the switch, its extremely high resistance blocks almost all current through the $1\\,\\Omega$ branch, increasing the total external circuit resistance. This causes the total circuit current to decrease, which reduces the internal potential drop ('lost volts' $V_{\\text{internal}} = Ir$). Since the battery's emf $\\mathcal{E}$ is constant, the reading on voltmeter $V_1$ ($V_1 = \\mathcal{E} - Ir$) increases."
)

# ==========================================
# QUESTION 9: ELECTRODYNAMICS & AC CIRCUITS (11 MARKS)
# ==========================================

Q9_PASSAGE = (
    "The diagram shows the initial position of the coil in a simple DC generator. The coil is rotated in an "
    "anticlockwise direction. A permanent magnet provides a uniform magnetic field from North (on the left) to "
    "South (on the right). The coil has top segment XY and is connected to a split-ring commutator.\n\n"
    "In the second part of the question, wall sockets supply rms voltage and current. A $220\\text{ V}$ AC voltage "
    "is supplied from a wall socket to an electric kettle having a resistance of $32\\,\\Omega$."
)

# 9.1.1
add_item(
    q_ref="9.1.1",
    kind="question",
    marks=1,
    topic="Electrodynamics - DC Generator Component",
    passage=Q9_PASSAGE,
    question="Name the component in this generator that ensures that the induced current in the external circuit is in one direction only.",
    memo="* Split ring / commutator $\\checkmark$",
    final_answer="Split-ring commutator"
)

# 9.1.2
add_item(
    q_ref="9.1.2",
    kind="question",
    marks=1,
    topic="Electrodynamics - Direction of Induced Current",
    passage=Q9_PASSAGE,
    question="Is the direction of the induced current from X to Y or from Y to X?",
    memo="* Y to X OR 0 / no current $\\checkmark$",
    final_answer="Y to X (or 0 / no current in the instantaneous vertical position)"
)

# 9.1.3
add_item(
    q_ref="9.1.3",
    kind="question",
    marks=1,
    topic="Electrodynamics - Period of Generator",
    passage=Q9_PASSAGE,
    question="A maximum voltage of $90\\text{ V}$ is generated when the coil is rotating at a frequency of $20\\text{ Hz}$.\n\nWrite down the time taken for the coil to complete ONE rotation.",
    memo="* $$T = \\frac{1}{f} = \\frac{1}{20} = 0{,}05\\text{ s}\\;\\checkmark$$",
    final_answer="$0{,}05\\text{ s}$"
)

# 9.1.4
add_item(
    q_ref="9.1.4",
    kind="question",
    marks=4,
    topic="Electrodynamics - DC Generator Output Voltage Graph",
    passage=Q9_PASSAGE,
    question="The coil starts rotating from the initial position, as shown in the diagram above.\n\nSketch a graph of output voltage versus time for one complete rotation of the coil. Indicate the maximum voltage and the relevant time values on the graph.",
    memo="*Positive marking from QUESTION 9.1.3*\n\n**Criteria for graph:**\n* Correct pulsating DC shape with one full cycle (two positive half-wave pulses / humps, or two negative pulses) $\\checkmark$\n* Curve starts at zero to first peak $\\checkmark$\n* Any one of the correct time values at the correct position ($t = 0{,}025\\text{ s}$ for first half-cycle, $t = 0{,}05\\text{ s}$ for full rotation) $\\checkmark$\n* Maximum voltage of $90\\text{ V}$ (or $-90\\text{ V}$) indicated at the peaks $\\checkmark$\n\n*(Notes:*\n* Award 1 mark for half cycle / incomplete cycle or more than one cycle.\n* Graph description: Starts at $(0, 0)$, rises to $+90\\text{ V}$, drops to $0\\text{ V}$ at $t = 0{,}025\\text{ s}$, rises to a second peak of $+90\\text{ V}$, and drops to $0\\text{ V}$ at $t = 0{,}05\\text{ s}$.)*",
    final_answer="A pulsating DC output voltage graph starting at $(0, 0)$, showing two positive half-sine humps reaching a maximum peak voltage of $90\\text{ V}$, with the first half-cycle ending at $t = 0{,}025\\text{ s}$ and the complete rotation ending at $t = 0{,}05\\text{ s}$."
)

# 9.2
add_item(
    q_ref="9.2",
    kind="question",
    marks=4,
    topic="Electrodynamics - Average Energy Dissipated by AC Circuit",
    passage=Q9_PASSAGE,
    question="Wall sockets supply rms voltage and current.\n\nA $220\\text{ V}$ AC voltage is supplied from a wall socket to an electric kettle having a resistance of $32\\,\\Omega$.\n\nCalculate the average energy dissipated by the kettle in TWO minutes.",
    memo="**Marking criteria:**\n* Formula to calculate $W_{\\text{ave}}$ $\\checkmark$\n* Substitution of $220\\text{ V}$ and $32\\,\\Omega$ in correct equation $\\checkmark$\n* Substitution of $120\\text{ s}$ for $\\Delta t$ $\\checkmark$\n* Correct answer in range: $181\\,500\\text{ J}$ to $181\\,764\\text{ J}\\;\\checkmark$\n\n**OPTION 1:**\n$$W_{\\text{ave}} = \\frac{V_{\\text{rms}}^2}{R}\\Delta t\\;\\checkmark$$\n$$W_{\\text{ave}} = \\frac{(220)^2}{32}(120)\\;\\checkmark\\;\\checkmark$$\n$$W_{\\text{ave}} = 181\\,500\\text{ J}\\;\\checkmark\\quad (1{,}82 \\times 10^5\\text{ J})$$\n\n**OPTION 2:**\n$$I_{\\text{rms}} = \\frac{V_{\\text{rms}}}{R} = \\frac{220}{32} = 6{,}875\\text{ A}$$\n$$W_{\\text{ave}} = V_{\\text{rms}} I_{\\text{rms}} \\Delta t\\;\\checkmark$$\n$$W_{\\text{ave}} = (220)(6{,}875)(120)\\;\\checkmark\\;\\checkmark = 181\\,500\\text{ J}\\;\\checkmark$$\n*(or using rounded $I_{\\text{rms}} = 6{,}88\\text{ A}$: $W = (220)(6{,}88)(120) = 181\\,632\\text{ J}$)*\n\n**OPTION 3:**\n$$P_{\\text{ave}} = \\frac{V_{\\text{rms}}^2}{R} = \\frac{220^2}{32} = 1512{,}5\\text{ W}\\;\\checkmark$$\n$$W_{\\text{ave}} = P_{\\text{ave}} \\Delta t = (1512{,}5)(120)\\;\\checkmark\\;\\checkmark = 181\\,500\\text{ J}\\;\\checkmark$$",
    final_answer="$181\\,500\\text{ J}$ (or $1{,}82 \\times 10^5\\text{ J}$)"
)

# ==========================================
# QUESTION 10: PHOTOELECTRIC EFFECT (14 MARKS)
# ==========================================

Q10_PASSAGE = (
    "Light is incident on the cathode of a photoelectric cell connected to a battery and a sensitive ammeter, "
    "as shown in the circuit diagram.\n\n"
    "The cathode has a work function of $3{,}42 \\times 10^{-19}\\text{ J}$.\n\n"
    "Light of frequency $5{,}96 \\times 10^{14}\\text{ Hz}$ is shone onto the cathode."
)

# 10.1
add_item(
    q_ref="10.1",
    kind="question",
    marks=1,
    topic="Photoelectric Effect - Nature of Light",
    passage=Q10_PASSAGE,
    question="What conclusive evidence about the nature of light is provided by the photoelectric effect?",
    memo="* Light has a particle nature / is quantized $\\checkmark$",
    final_answer="Light has a particle nature (light is quantized into photons)."
)

# 10.2
add_item(
    q_ref="10.2",
    kind="question",
    marks=2,
    topic="Photoelectric Effect - Work Function Definition",
    passage=Q10_PASSAGE,
    question="The cathode has a work function of $3{,}42 \\times 10^{-19}\\text{ J}$.\n\nDefine the term work function.",
    memo="* The minimum energy (of incident photons) that can eject electrons from a metal/surface. $\\checkmark\\checkmark$ *(2 or 0)*",
    final_answer="The minimum energy needed to eject electrons from the surface of a metal."
)

# 10.3
add_item(
    q_ref="10.3",
    kind="question",
    marks=4,
    topic="Photoelectric Effect - Maximum Kinetic Energy Calculation",
    passage=Q10_PASSAGE,
    question="Light of frequency $5{,}96 \\times 10^{14}\\text{ Hz}$ is shone onto the cathode.\n\nCalculate the maximum kinetic energy of an electron ejected from the cathode.",
    memo="**Marking criteria:**\n* Formula: $E = W_0 + E_{k(\\max)}$ OR $hf = W_0 + E_{k(\\max)}\\;\\checkmark$\n* Correct substitution into $hf$: $(6{,}63 \\times 10^{-34})(5{,}96 \\times 10^{14})\\;\\checkmark$\n* Correct substitution of $W_0$: $3{,}42 \\times 10^{-19}\\;\\checkmark$\n* Correct final answer: $5{,}30 \\times 10^{-20}\\text{ J}$ to $5{,}32 \\times 10^{-20}\\text{ J}\\;\\checkmark$\n\n**Calculation:**\n$$E = W_0 + E_{k(\\max)}\\;\\checkmark$$\n$$hf = W_0 + E_{k(\\max)}$$\n$$(6{,}63 \\times 10^{-34})(5{,}96 \\times 10^{14})\\;\\checkmark = 3{,}42 \\times 10^{-19}\\;\\checkmark + E_{k(\\max)}$$\n$$3{,}95148 \\times 10^{-19} = 3{,}42 \\times 10^{-19} + E_{k(\\max)}$$\n$$E_{k(\\max)} = 3{,}95148 \\times 10^{-19} - 3{,}42 \\times 10^{-19} = 5{,}31 \\times 10^{-20}\\text{ J}\\;\\checkmark\\quad (5{,}30 \\times 10^{-20}\\text{ J} - 5{,}32 \\times 10^{-20}\\text{ J})$$",
    final_answer="$5{,}31 \\times 10^{-20}\\text{ J}$ (or $5{,}30 \\times 10^{-20}\\text{ J}$)"
)

# 10.4
add_item(
    q_ref="10.4",
    kind="question",
    marks=4,
    topic="Photoelectric Effect - Number of Incident Photons Calculation",
    passage=Q10_PASSAGE,
    question="The ammeter registers a constant current of $0{,}012\\text{ A}$.\n\nCalculate the minimum number of photons of light that strike the cathode in a 10 s period.",
    memo="**Marking criteria:**\n* Formula and substitution for charge: $q = I\\Delta t = (0{,}012)(10)\\;\\checkmark$\n* Formula to calculate number of electrons: $n = \\frac{q}{e}\\;\\checkmark$\n* Correct substitution: $n = \\frac{0{,}12}{1{,}6 \\times 10^{-19}}\\;\\checkmark$\n* Final answer (minimum number of photons): $7{,}5 \\times 10^{17}\\;\\checkmark$\n\n**Calculation:**\n$$q = I\\Delta t = (0{,}012)(10)\\;\\checkmark = 0{,}12\\text{ C}$$\n$$n = \\frac{q}{e}\\;\\checkmark$$\n$$n = \\frac{0{,}12}{1{,}6 \\times 10^{-19}}\\;\\checkmark = 7{,}5 \\times 10^{17}\\text{ electrons}$$\nSince each photon releases at most one photoelectron (minimum 1:1 photon-to-electron ratio):\n$$\\text{Minimum number of photons} = 7{,}5 \\times 10^{17}\\;\\checkmark$$",
    final_answer="$7{,}5 \\times 10^{17}\\text{ photons}$"
)

# 10.5
add_item(
    q_ref="10.5",
    kind="question",
    marks=3,
    topic="Photoelectric Effect - Effect of Light Intensity",
    passage=Q10_PASSAGE,
    question="The intensity of the incident light is now INCREASED. How will this change affect the reading on the ammeter?\n\nChoose from INCREASES, DECREASES or REMAINS THE SAME.\nExplain the answer.",
    memo="* Increases $\\checkmark$\n* More photons strike the surface of the metal per unit time / at a higher rate $\\checkmark$\n* Hence more (photo)electrons are ejected per unit time $\\checkmark$ (resulting in increased current).",
    final_answer="Increases. Higher intensity means more photons strike the cathode per unit time, resulting in more photoelectrons emitted per unit time, thereby increasing the current registered by the ammeter."
)

# ==========================================
# VERIFICATION AND OUTPUT
# ==========================================

print(f"Total items extracted: {len(items)}")
total_marks = sum(item["marks"] for item in items)
print(f"Total marks: {total_marks} / 150")

# Verify KaTeX dollar balancing
dollar_errors = 0
for item in items:
    for field in ["passage", "question", "memo", "final_answer"]:
        val = item[field]
        # Count single dollars (accounting for display $$)
        # Replacing $$ with empty, then counting single $
        temp = val.replace("$$", "")
        single_dollars = temp.count("$")
        if single_dollars % 2 != 0:
            print(f"ERROR: Unbalanced $ in item {item['item_id']}, field {field}")
            dollar_errors += 1

print(f"KaTeX unbalanced dollar check: {dollar_errors} errors")

# Write output files
output_dir1 = "workspace/items/physical_sciences"
output_dir2 = "workspace/items"
os.makedirs(output_dir1, exist_ok=True)
os.makedirs(output_dir2, exist_ok=True)

path1 = os.path.join(output_dir1, f"{SOURCE_ID}.jsonl")
path2 = os.path.join(output_dir2, f"{SOURCE_ID}.jsonl")

for path in [path1, path2]:
    with open(path, "w", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"Wrote {len(items)} items to {path}")

# Verification of lines in written files
for path in [path1, path2]:
    with open(path, "r", encoding="utf-8") as f:
        read_lines = [json.loads(line) for line in f]
    sum_m = sum(x["marks"] for x in read_lines)
    print(f"Verified {path}: {len(read_lines)} lines, sum of marks = {sum_m}")

print("Extraction script completed successfully!")
