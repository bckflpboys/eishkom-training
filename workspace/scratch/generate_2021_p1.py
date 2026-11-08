# -*- coding: utf-8 -*-
"""
Extraction script for Physical Sciences Grade 12 Paper 1 November 2021
Source ID: dbe-physical_sciences-g12-p1-2021-nov
Paired Memo ID: dbe-physical_sciences-g12-p1-2021-nov-memo
Total Marks: 150
"""

import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

SOURCE_ID = "dbe-physical_sciences-g12-p1-2021-nov"
PAIR_SOURCE_ID = "dbe-physical_sciences-g12-p1-2021-nov-memo"
SUBJECT = "physical_sciences"
GRADE = 12
LANGUAGE = "en"
TRACK = "physical_sciences"
LICENCE = "DBE copyright - check terms"
ATTRIBUTION = "Department of Basic Education"

items = []

def make_item(q_ref, kind, marks, topic, passage, question, memo, final_answer):
    return {
        "item_id": f"{SOURCE_ID}-{q_ref}",
        "source_id": SOURCE_ID,
        "pair_source_id": PAIR_SOURCE_ID,
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
        "licence": LICENCE,
        "attribution": ATTRIBUTION
    }

# ==========================================
# QUESTION 1: MULTIPLE-CHOICE QUESTIONS (1.1 to 1.10)
# ==========================================

# 1.1
items.append(make_item(
    q_ref="1.1",
    kind="multiple_choice",
    marks=2,
    topic="Forces and Newton's Laws - Normal Force Definition",
    passage="",
    question="Consider the statement below.\n\nThe perpendicular force exerted by a surface on an object in contact with the surface.\n\nWhich ONE of the following forces is defined by the statement above?\n\nA Normal force\nB Resultant force\nC Frictional force\nD Gravitational force",
    memo="A $\\checkmark\\checkmark$\n\n*Rationale: By definition, the normal force is the force or the component of a force which a surface exerts on an object with which it is in contact, and which is perpendicular to the surface. Therefore, the statement defines the normal force (Option A).*",
    final_answer="A"
))

# 1.2
items.append(make_item(
    q_ref="1.2",
    kind="multiple_choice",
    marks=2,
    topic="Vertical Projectile Motion - Free Fall",
    passage="",
    question="Two balls of masses $m$ and $2m$ are dropped simultaneously from the same height above the ground. Ignore air resistance.\n\nWhen the balls strike the ground, which ONE of the following physical quantities will be the same for both balls?\n\nA Weight\nB Velocity\nC Momentum\nD Kinetic energy",
    memo="B $\\checkmark\\checkmark$\n\n*Rationale: In free fall under gravity (ignoring air resistance), both balls experience the same gravitational acceleration $g = 9{,}8\\text{ m}\\cdot\\text{s}^{-2}$, independent of mass. Since both are dropped from rest ($v_i = 0$) from the same height $\\Delta y$, their final velocity on striking the ground is given by $v_f^2 = v_i^2 + 2g\\Delta y = 2g\\Delta y$, which is identical for both balls. In contrast, weight ($w = mg$), momentum ($p = mv$), and kinetic energy ($E_k = \\frac{1}{2}mv^2$) all depend directly on mass and are therefore twice as large for the ball of mass $2m$.*",
    final_answer="B"
))

# 1.3
items.append(make_item(
    q_ref="1.3",
    kind="multiple_choice",
    marks=2,
    topic="Momentum and Newton's Second Law - Momentum-Time Graph",
    passage="The graph shows how the momentum ($p$) of an object changes with time ($t$):\n* At $t = 0\\text{ s}$, $p = 0\\text{ kg}\\cdot\\text{m}\\cdot\\text{s}^{-1}$.\n* From $t = 0\\text{ s}$ to $t = 1\\text{ s}$, $p$ increases linearly from $0$ to $20\\text{ kg}\\cdot\\text{m}\\cdot\\text{s}^{-1}$.\n* From $t = 1\\text{ s}$ to $t = 2\\text{ s}$, $p$ decreases linearly from $20\\text{ kg}\\cdot\\text{m}\\cdot\\text{s}^{-1}$ to $10\\text{ kg}\\cdot\\text{m}\\cdot\\text{s}^{-1}$.\n* From $t = 2\\text{ s}$ to $t = 3\\text{ s}$, $p$ decreases linearly from $10\\text{ kg}\\cdot\\text{m}\\cdot\\text{s}^{-1}$ to $-10\\text{ kg}\\cdot\\text{m}\\cdot\\text{s}^{-1}$ (crossing zero at $t = 2{,}5\\text{ s}$).\n* From $t = 3\\text{ s}$ to $t = 4\\text{ s}$, $p$ increases linearly from $-10\\text{ kg}\\cdot\\text{m}\\cdot\\text{s}^{-1}$ to $20\\text{ kg}\\cdot\\text{m}\\cdot\\text{s}^{-1}$.",
    question="The graph below shows how the momentum ($p$) of an object changes with time ($t$).\n\nDuring which ONE of the following time intervals, measured in seconds, is the magnitude of the net force acting on the object the greatest?\n\nA $0$ to $1$\nB $1$ to $2$\nC $2$ to $3$\nD $3$ to $4$",
    memo="D $\\checkmark\\checkmark$\n\n*Rationale: According to Newton's Second Law expressed in terms of momentum, $F_{\\text{net}} = \\frac{\\Delta p}{\\Delta t}$, which is the gradient (slope) of the momentum-time graph. Calculating the magnitude of the slope for each interval:\n* $0$ to $1\\text{ s}$: $|F_{\\text{net}}| = \\left|\\frac{20 - 0}{1 - 0}\\right| = 20\\text{ N}$\n* $1$ to $2\\text{ s}$: $|F_{\\text{net}}| = \\left|\\frac{10 - 20}{2 - 1}\\right| = 10\\text{ N}$\n* $2$ to $3\\text{ s}$: $|F_{\\text{net}}| = \\left|\\frac{-10 - 10}{3 - 2}\\right| = 20\\text{ N}$\n* $3$ to $4\\text{ s}$: $|F_{\\text{net}}| = \\left|\\frac{20 - (-10)}{4 - 3}\\right| = 30\\text{ N}$\nThe greatest magnitude of net force is $30\\text{ N}$, which occurs during the interval $3$ to $4\\text{ s}$ (Option D).*",
    final_answer="D"
))

# 1.4
items.append(make_item(
    q_ref="1.4",
    kind="multiple_choice",
    marks=2,
    topic="Work, Energy and Power - Conservation of Mechanical Energy Graph",
    passage="A ball is dropped from a height above a floor. The ball makes an elastic collision with the floor at time $t_0$ and bounces vertically upwards. Ignore air resistance.\n\nFour graphs show possible variations of total mechanical energy ($E_M$) with time ($t$):\n* Graph A: $E_M$ increases linearly from $0$ to a peak at $t_0$, then decreases linearly back to $0$.\n* Graph B: $E_M$ remains constant (horizontal straight line) from $t = 0$ through and beyond $t_0$.\n* Graph C: $E_M$ decreases linearly from an initial positive value to $0$ at $t_0$, then increases linearly.\n* Graph D: $E_M$ decreases linearly to a non-zero minimum at $t_0$, then increases linearly.",
    question="A ball is dropped from a height above a floor. The ball makes an elastic collision with the floor at time $t_0$ and bounces vertically upwards.\n\nIgnore air resistance.\n\nWhich ONE of the following graphs shows how the total mechanical energy ($E_M$) of the ball changes with time?\n\nA Graph A (triangle peaking at $t_0$)\nB Graph B (horizontal straight line)\nC Graph C (V-shape touching zero at $t_0$)\nD Graph D (V-shape with non-zero minimum at $t_0$)",
    memo="B $\\checkmark\\checkmark$\n\n*Rationale: Mechanical energy $E_M$ is the sum of gravitational potential energy and kinetic energy ($E_M = E_p + E_k$). In free fall, with air resistance ignored, only the conservative gravitational force does work, so mechanical energy is conserved. Since the collision with the floor is specified as elastic, total kinetic energy is conserved during the collision with no mechanical energy converted into internal energy, heat, or sound. Thus, $E_M$ remains constant over the entire duration of the motion, represented by a horizontal line (Graph B).*",
    final_answer="B"
))

# 1.5
items.append(make_item(
    q_ref="1.5",
    kind="multiple_choice",
    marks=2,
    topic="Doppler Effect - Red Shift in Atomic Spectra",
    passage="Consider the two spectrum diagrams below:\n* Diagram 1 represents the spectrum of an element in a laboratory on Earth, showing absorption lines situated towards the blue end of the visible spectrum.\n* Diagram 2 represents the spectrum of the same element from a distant star as observed from Earth, where all corresponding absorption lines are shifted towards the red end of the spectrum.",
    question="Consider the two spectrum diagrams below.\n\nDiagram 1 represents the spectrum of an element in a laboratory on Earth.\nDiagram 2 represents the spectrum of the same element from a distant star as observed from Earth.\n\nWhich ONE of the following can be deduced from the spectra above?\n\nA The star is moving towards Earth.\nB The star is at rest relative to Earth.\nC The star is moving away from Earth.\nD Both the star and Earth are moving towards each other.",
    memo="C $\\checkmark\\checkmark$\n\n*Rationale: Comparing Diagram 2 to Diagram 1, the absorption lines of the element from the distant star are shifted towards the red end of the spectrum (longer wavelengths, lower frequencies). This phenomenon is known as a red shift, which according to the Doppler effect indicates that the distance between the source (star) and observer (Earth) is increasing; that is, the star is moving away from Earth (Option C).*",
    final_answer="C"
))

# 1.6
items.append(make_item(
    q_ref="1.6",
    kind="multiple_choice",
    marks=2,
    topic="Electrostatics - Electric Field Lines and Charge Polarity",
    passage="The diagram shows the field lines for the combined electric field due to two small charged spheres, P and Q:\n* Electric field lines point radially outwards from sphere P.\n* Electric field lines point radially inwards towards sphere Q.\n* Curved electric field lines run continuously from sphere P to sphere Q.",
    question="The diagram below shows the field lines for the combined electric field due to two small charged spheres P and Q.\n\nWhich ONE of the combinations below correctly shows the polarity of spheres P and Q?\n\nA Sphere P: Negative; Sphere Q: Positive\nB Sphere P: Negative; Sphere Q: Negative\nC Sphere P: Positive; Sphere Q: Positive\nD Sphere P: Positive; Sphere Q: Negative",
    memo="D $\\checkmark\\checkmark$\n\n*Rationale: By definition and convention, electric field lines point away from positive charges and towards negative charges. The arrows on the field lines originate from sphere P and enter sphere Q. Therefore, sphere P is positively charged and sphere Q is negatively charged (Option D).*",
    final_answer="D"
))

# 1.7
items.append(make_item(
    q_ref="1.7",
    kind="multiple_choice",
    marks=2,
    topic="Electrostatics - Newton's Third Law and Coulomb's Force",
    passage="Two identical spheres, P and Q, carry charges of $+q$ and $-2q$ respectively. Sphere P exerts an electrostatic force of magnitude $F$ on sphere Q.",
    question="Two identical spheres, P and Q, carry charges of $+q$ and $-2q$ respectively. Sphere P exerts an electrostatic force of magnitude $F$ on sphere Q.\n\nWhich ONE of the following represents the magnitude of the electrostatic force exerted on sphere P by sphere Q?\n\nA $\\frac{1}{2}F$\nB $F$\nC $2F$\nD $4F$",
    memo="B $\\checkmark\\checkmark$\n\n*(Accept: B or F)*\n\n*Rationale: According to Coulomb's Law, the electrostatic force between two point charges is given by $F = \\frac{k|q_1 q_2|}{r^2}$. Furthermore, according to Newton's Third Law of Motion, when body P exerts an electrostatic force on body Q, body Q simultaneously exerts an electrostatic force on body P of equal magnitude and opposite direction. Therefore, the magnitude of the force exerted by Q on P is equal to $F$ (Option B).*",
    final_answer="B"
))

# 1.8
items.append(make_item(
    q_ref="1.8",
    kind="multiple_choice",
    marks=2,
    topic="Electric Circuits - Potential Difference Distribution",
    passage="In the circuit diagram shown, all the resistors are IDENTICAL (each of resistance $R$). The battery has emf $\\varepsilon$ and negligible internal resistance ($r = 0$).\n* Switch S is in series with the cell and a single resistor $R$ across which voltmeter $V_1$ is connected.\n* In series with this first resistor is a parallel combination of two identical resistors, each of resistance $R$.\n* Voltmeter $V_2$ is connected across the upper parallel branch resistor $R$.\n* Voltmeter $V_3$ is connected across the lower parallel branch resistor $R$.\n* Voltmeter $V_4$ is connected across the parallel combination of the two branches.",
    question="In the circuit diagram shown below all the resistors are IDENTICAL. Ignore the internal resistance of the cell.\n\nWhich voltmeter will have the HIGHEST reading when switch S is closed?\n\nA $V_1$\nB $V_2$\nC $V_3$\nD $V_4$",
    memo="A $\\checkmark\\checkmark$\n\n*(Accept: A or $V_1$)*\n\n*Rationale: Let each resistor have resistance $R$. The parallel combination of the two identical resistors has an equivalent resistance $R_p = \\frac{R \\cdot R}{R + R} = 0{,}5R$. The total external resistance of the circuit is $R_{\\text{tot}} = R + R_p = 1{,}5R$. The total current leaving the battery is $I = \\frac{\\varepsilon}{1{,}5R} = \\frac{2\\varepsilon}{3R}$. The potential difference across the single series resistor (measured by $V_1$) is $V_1 = IR = \\left(\\frac{2\\varepsilon}{3R}\\right)R = \\frac{2}{3}\\varepsilon \\approx 0{,}67\\varepsilon$. The potential difference across the parallel combination (measured by $V_2$, $V_3$, and $V_4$) is $V_p = IR_p = \\left(\\frac{2\\varepsilon}{3R}\\right)(0{,}5R) = \\frac{1}{3}\\varepsilon \\approx 0{,}33\\varepsilon$. Since $\\frac{2}{3}\\varepsilon > \\frac{1}{3}\\varepsilon$, voltmeter $V_1$ has the highest reading (Option A).*",
    final_answer="A"
))

# 1.9
items.append(make_item(
    q_ref="1.9",
    kind="multiple_choice",
    marks=2,
    topic="Electrodynamics - Electrical Energy Conversion",
    passage="",
    question="In which ONE of the following electrical machines is electrical energy converted to mechanical energy?\n\nA AC generator\nB DC generator\nC AC dynamo\nD DC motor",
    memo="D $\\checkmark\\checkmark$\n\n*Rationale: Generators and dynamos (both AC and DC) convert mechanical energy into electrical energy via electromagnetic induction. An electric motor (such as a DC motor) converts electrical energy into mechanical energy through the motor effect. Therefore, Option D is correct.*",
    final_answer="D"
))

# 1.10
items.append(make_item(
    q_ref="1.10",
    kind="multiple_choice",
    marks=2,
    topic="Optical Phenomena - Emission and Absorption Spectra Transitions",
    passage="",
    question="Which ONE of the following combinations correctly links an emission spectrum and an absorption spectrum to the energy transitions of an electron in an atom?\n\nA Emission spectrum: From low to high energy levels; Absorption spectrum: From high to low energy levels\nB Emission spectrum: From low to high energy levels; Absorption spectrum: From low to high energy levels\nC Emission spectrum: From high to low energy levels; Absorption spectrum: From high to low energy levels\nD Emission spectrum: From high to low energy levels; Absorption spectrum: From low to high energy levels",
    memo="D $\\checkmark\\checkmark$\n\n*Rationale: An atomic emission spectrum is produced when electrons drop from higher energy levels to lower energy levels, releasing energy in the form of emitted photons ($E = hf$). An atomic absorption spectrum is formed when electrons absorb photons of specific energies and are excited from lower energy levels to higher energy levels. Thus, emission corresponds to transitions from high to low energy levels, while absorption corresponds to transitions from low to high energy levels (Option D).*",
    final_answer="D"
))

print(f"Added {len(items)} items for Question 1.")

# Save temporary check
with open("workspace/scratch/test_gen.py", "w", encoding="utf-8") as f:
    f.write("# ok")
