import json
import re
import os
import sys

source_id = "dbe-physical_sciences-g12-p1-2019-nov"
pair_source_id = "dbe-physical_sciences-g12-p1-2019-nov-memo"
subject = "physical_sciences"
grade = 12
language = "en"
track = "physical_sciences"
licence = "DBE copyright - check terms"
attribution = "Department of Basic Education"

items = []

def add_item(q_ref, kind, marks, topic, passage, question, memo, final_answer):
    items.append({
        "item_id": f"{source_id}-{q_ref}",
        "source_id": source_id,
        "pair_source_id": pair_source_id,
        "subject": subject,
        "grade": grade,
        "language": language,
        "track": track,
        "kind": kind,
        "question_ref": q_ref,
        "marks": marks,
        "topic": topic,
        "passage": passage,
        "question": question,
        "memo": memo,
        "final_answer": final_answer,
        "needs_review": False,
        "licence": licence,
        "attribution": attribution
    })

# ==========================================
# QUESTION 1: MULTIPLE-CHOICE (1.1 - 1.10)
# ==========================================

add_item(
    q_ref="1.1",
    kind="multiple_choice",
    marks=2,
    topic="Momentum and Newton's Second Law - Rate of Change of Momentum",
    passage="",
    question="Which physical quantity is equal to the rate of change of momentum?\n\nA Mass\nB Impulse\nC Net force\nD Acceleration",
    memo="C $\\checkmark\\checkmark$\n\n*Rationale: According to Newton's Second Law of Motion in terms of momentum ($F_{\\text{net}} = \\frac{\\Delta p}{\\Delta t}$), the resultant or net force acting on an object is equal to the rate of change of momentum of the object.*",
    final_answer="C"
)

add_item(
    q_ref="1.2",
    kind="multiple_choice",
    marks=2,
    topic="Newton's Law of Universal Gravitation - Gravitational Acceleration at Height",
    passage="",
    question="The gravitational acceleration on the surface of a planet of radius $R$ is $g$.\n\nThe gravitational acceleration at a height of $2R$ above the surface of the same planet is …\n\nA $\\frac{g}{9}$\n\nB $\\frac{g}{4}$\n\nC $4g$\n\nD $9g$",
    memo="A $\\checkmark\\checkmark$\n\n*Rationale: Gravitational acceleration is given by $g = \\frac{GM}{r^2}$, where $r$ is the distance from the centre of the planet. At a height of $2R$ above the surface, the distance from the centre is $r = R + 2R = 3R$. Therefore:\n$$g' = \\frac{GM}{(3R)^2} = \\frac{GM}{9R^2} = \\frac{1}{9}\\left(\\frac{GM}{R^2}\\right) = \\frac{g}{9}$$\nThus, the gravitational acceleration is $\\frac{g}{9}$ (Option A).*",
    final_answer="A"
)

add_item(
    q_ref="1.3",
    kind="multiple_choice",
    marks=2,
    topic="Vertical Projectile Motion - Free Fall Quantities",
    passage="",
    question="A ball falls from the edge of a table. Ignore the effects of air friction.\n\nWhich ONE of the physical quantities associated with the ball during the fall remains constant?\n\nA Weight\nB Momentum\nC Kinetic energy\nD Gravitational potential energy",
    memo="A $\\checkmark\\checkmark$\n\n*Rationale: As the ball falls freely under gravity in the absence of air friction, the only force acting on it is the gravitational force (weight, $w = mg$). Since mass $m$ and gravitational acceleration $g$ are constant, its weight remains constant. Momentum ($p = mv$) and kinetic energy ($E_k = \\frac{1}{2}mv^2$) increase as speed increases, while gravitational potential energy ($E_p = mgh$) decreases as height decreases.*",
    final_answer="A"
)

add_item(
    q_ref="1.4",
    kind="multiple_choice",
    marks=2,
    topic="Conservation of Linear Momentum - Compressed Spring Trolley System",
    passage="Two trolleys, X and Y, of masses $m$ and $2m$ respectively, are held together on a frictionless horizontal floor with a compressed spring between them. Initially, both trolleys are stationary.",
    question="Two trolleys, X and Y, of masses $m$ and $2m$ respectively, are held together by a compressed spring between them. Initially they are stationary on a horizontal floor, as shown below. Ignore the effects of friction.\n\nThe spring is now released and falls to the floor while the trolleys move apart.\n\nThe magnitude of the MOMENTUM of trolley X while it moves away is …\n\nA zero.\nB half the magnitude of the momentum of trolley Y.\nC twice the magnitude of the momentum of trolley Y.\nD the same as the magnitude of the momentum of trolley Y.",
    memo="D $\\checkmark\\checkmark$\n\n*Rationale: According to the principle of conservation of linear momentum, the total linear momentum in an isolated system is conserved:\n$$\\Sigma p_i = \\Sigma p_f$$\n$$0 = p_X + p_Y \\implies p_X = -p_Y$$\nTherefore, the magnitudes of their momenta are equal: $|p_X| = |p_Y|$ (Option D).*",
    final_answer="D"
)

add_item(
    q_ref="1.5",
    kind="multiple_choice",
    marks=2,
    topic="Vertical Projectile Motion and Momentum - Dependence on Fall Distance",
    passage="",
    question="An object is dropped from rest and after falling a distance $x$, its momentum is $p$. Ignore the effects of air friction.\n\nThe momentum of the object, after it has fallen a distance $2x$, is …\n\nA $p$\n\nB $\\sqrt{2}p$\n\nC $\\frac{p}{2}$\n\nD $2p$",
    memo="B $\\checkmark\\checkmark$\n\n*Rationale: From the equations of motion with $v_i = 0$:\n$$v_f^2 = v_i^2 + 2g\\Delta y = 0 + 2gx \\implies v_f = \\sqrt{2gx}$$\nThe momentum after distance $x$ is $p = mv_f = m\\sqrt{2gx}$.\nAfter falling a distance $2x$:\n$$v_f' = \\sqrt{2g(2x)} = \\sqrt{2} \\cdot \\sqrt{2gx} = \\sqrt{2}v_f$$\nThus, the new momentum is $p' = mv_f' = \\sqrt{2}mv_f = \\sqrt{2}p$ (Option B).*",
    final_answer="B"
)

add_item(
    q_ref="1.6",
    kind="multiple_choice",
    marks=2,
    topic="Doppler Effect - Moving Source Towards Stationary Detector",
    passage="",
    question="A police car, with its siren on, is travelling at a constant speed TOWARDS a stationary sound detector. The siren emits sound waves of frequency $f$ and speed $v$.\n\nWhich ONE of the following combinations best describes the frequency and speed of the detected sound waves?\n\n| | FREQUENCY | SPEED |\n| :--- | :--- | :--- |\n| A | Less than $f$ | $v$ |\n| B | Less than $f$ | Less than $v$ |\n| C | Greater than $f$ | Less than $v$ |\n| D | Greater than $f$ | $v$ |",
    memo="D $\\checkmark\\checkmark$\n\n*Rationale: By the Doppler effect, when a sound source moves towards a stationary detector, the detected frequency is higher than the emitted source frequency ($f_L > f$). However, the speed of sound waves ($v$) depends solely on the properties of the medium (air at constant temperature and pressure) and remains unchanged at $v$. Thus, Option D is correct.*",
    final_answer="D"
)

add_item(
    q_ref="1.7",
    kind="multiple_choice",
    marks=2,
    topic="Electrostatics - Charge Sharing and Coulomb's Law",
    passage="Two identical spheres, R and S, on insulated stands, carrying charges of $+q$ and $-q$ respectively, are placed a distance apart. Sphere R exerts an electrostatic force of magnitude $F$ on sphere S.",
    question="Two identical spheres, R and S, on insulated stands, carrying charges of $+q$ and $-q$ respectively, are placed a distance apart. Sphere R exerts an electrostatic force of magnitude $F$ on sphere S.\n\nThe two spheres are now brought into contact and returned to their original positions.\n\nThe magnitude of the electrostatic force that sphere R exerts on sphere S is now …\n\nA zero\nB $\\frac{F}{2}$\nC $F$\nD $2F$",
    memo="A $\\checkmark\\checkmark$\n\n*Rationale: When identical conducting spheres touch, charges are shared equally:\n$$q_{\\text{new}} = \\frac{q_R + q_S}{2} = \\frac{+q + (-q)}{2} = 0\\text{ C}$$\nSince both spheres become uncharged ($q = 0$), the electrostatic force between them when returned to their original positions is zero ($F' = \\frac{k(0)(0)}{r^2} = 0$) (Option A).*",
    final_answer="A"
)

add_item(
    q_ref="1.8",
    kind="multiple_choice",
    marks=2,
    topic="Electric Circuits - Potential Difference vs Current for Ohmic Conductor",
    passage="Four graphs of potential difference ($V$) on the vertical axis versus current ($I$) on the horizontal axis are given:\n- Graph A: A horizontal line where potential difference $V$ remains constant as current $I$ increases.\n- Graph B: A straight line passing through the origin $(0, 0)$ with a constant positive gradient.\n- Graph C: A straight line with a negative gradient, starting on the vertical axis and decreasing down to the horizontal axis.\n- Graph D: A curved line starting from the origin $(0, 0)$ with a changing gradient.",
    question="Which ONE of the graphs below best represents the relationship between potential difference ($V$) and current ($I$) for an ohmic conductor?\n\nA A horizontal line showing constant potential difference as current increases.\nB A straight line passing through the origin with a constant positive slope.\nC A straight line with a negative slope showing decreasing potential difference as current increases.\nD A curve through the origin showing non-linear variation of potential difference with current.",
    memo="B $\\checkmark\\checkmark$\n\n*Rationale: According to Ohm's Law ($V = IR$), the potential difference across an ohmic conductor is directly proportional to the current through it, provided the temperature remains constant. The graph of $V$ versus $I$ is therefore a straight line passing through the origin with a constant positive gradient equal to the resistance $R$ (Option B).*",
    final_answer="B"
)

add_item(
    q_ref="1.9",
    kind="multiple_choice",
    marks=2,
    topic="Electrodynamics - Energy Conversions in Motors and Generators",
    passage="",
    question="Which ONE of the following combinations regarding the energy conversions in electric motors and electric generators is CORRECT?\n\n| | ENERGY CONVERSION IN MOTORS | ENERGY CONVERSION IN GENERATORS |\n| :--- | :--- | :--- |\n| A | Mechanical to electrical | Electrical to mechanical |\n| B | Mechanical to electrical | Mechanical to electrical |\n| C | Electrical to mechanical | Electrical to mechanical |\n| D | Electrical to mechanical | Mechanical to electrical |",
    memo="D $\\checkmark\\checkmark$\n\n*Rationale: An electric motor converts electrical energy into mechanical energy (motion). An electric generator converts mechanical energy into electrical energy. Thus, Option D is correct.*",
    final_answer="D"
)

add_item(
    q_ref="1.10",
    kind="multiple_choice",
    marks=2,
    topic="Photoelectric Effect - Quantum Nature of Light",
    passage="",
    question="Consider the statements below regarding the photoelectric effect.\n\nThe photoelectric effect proves that …\n\n(i) light energy is quantised.\n(ii) light has a particle nature.\n(iii) light has a wave nature.\n\nWhich of the statements above is/are CORRECT?\n\nA (i) only\nB (ii) only\nC (i) and (ii) only\nD (i) and (iii) only",
    memo="C $\\checkmark\\checkmark$\n\n*Rationale: The photoelectric effect demonstrates that light energy is emitted and absorbed in discrete packets called photons (energy is quantised, $E = hf$) and that light interacts with electrons as particles (particle nature). The wave nature of light is demonstrated by phenomena such as diffraction and interference, not the photoelectric effect. Thus, statements (i) and (ii) are correct (Option C).*",
    final_answer="C"
)

# ==========================================
# QUESTION 2: NEWTON'S LAWS ON AN INCLINE
# ==========================================

passage_q2 = (
    "Block P, of mass $2\\text{ kg}$, is connected to block Q, of mass $3\\text{ kg}$, by a light inextensible string. "
    "Both blocks are on a plane inclined at an angle of $30^\\circ$ to the horizontal.\n\n"
    "Block Q is pulled by a constant force of $40\\text{ N}$ at an angle of $25^\\circ$ to the incline (upwards and outwards relative to the incline surface).\n\n"
    "Block P moves on a rough section, AB, of the incline, while block Q moves on a frictionless section, BC, of the incline.\n\n"
    "An average constant frictional force of $2{,}5\\text{ N}$ acts on block P as it moves from A to B up the incline."
)

add_item(
    q_ref="2.1",
    kind="question",
    marks=2,
    topic="Newton's Second Law of Motion - Statement",
    passage=passage_q2,
    question="State Newton's Second Law in words.",
    memo=(
        "When a resultant/net force acts on an object, the object will accelerate in the direction of the force with an acceleration that is directly proportional to the force and inversely proportional to the mass of the object. $\\checkmark\\checkmark$\n\n"
        "*OR*\n\n"
        "The resultant/net force acting on an object is equal to the rate of change of momentum of the object (in the direction of the resultant/net force). $\\checkmark\\checkmark$\n\n"
        "*(Marking criteria: -1 mark for each key word/phrase omitted in the correct context.)*"
    ),
    final_answer="When a net force acts on an object, the object will accelerate in the direction of the force with an acceleration directly proportional to the force and inversely proportional to the mass of the object."
)

add_item(
    q_ref="2.2",
    kind="question",
    marks=4,
    topic="Newton's Laws - Free-Body Diagram for Block on Incline",
    passage=passage_q2,
    question="Draw a labelled free-body diagram for block P.",
    memo=(
        "Accepted forces acting on block P:\n"
        "* $\\checkmark$ $T$ / $F_T$ / Tension (acting up the incline, parallel to the incline surface)\n"
        "* $\\checkmark$ $w$ / $F_g$ / $mg$ / weight / gravitational force ($19{,}6\\text{ N}$, acting vertically downwards) [OR components: $w_\\parallel$ acting down the incline and $w_\\perp$ acting perpendicular into the surface]\n"
        "* $\\checkmark$ $N$ / $F_N$ / Normal force ($16{,}97\\text{ N}$, acting perpendicular to the incline surface, away from the plane)\n"
        "* $\\checkmark$ $f$ / $F_f$ / $f_k$ / frictional force ($2{,}5\\text{ N}$, acting down the incline, parallel to surface opposite to motion)\n\n"
        "*(Marking notes:*\n"
        "* *Mark is awarded for label and arrow.*\n"
        "* *Do not penalise for length of arrows.*\n"
        "* *Deduct 1 mark for any additional force.*\n"
        "* *If force(s) do not make contact with body/dot: Max $3/4$.*\n"
        "* *If arrows missing: Max $3/4$.)*"
    ),
    final_answer="Labelled free-body diagram showing 4 forces on block P: Tension T (up incline), Normal force N (perpendicular to surface), Friction f (down incline), and Weight w (vertically downwards)."
)

add_item(
    q_ref="2.3",
    kind="question",
    marks=8,
    topic="Newton's Laws - Acceleration Calculation for Coupled Blocks on Incline",
    passage=passage_q2,
    question="Calculate the magnitude of the acceleration of block P while block P is moving on section AB.",
    memo=(
        "**OPTION 1 (Simultaneous equations):**\n\n"
        "For the $2\\text{ kg}$ block (P) (taking up the incline as positive):\n"
        "$$F_{\\text{net}} = ma$$\n"
        "$$T - w_\\parallel - f_k = ma$$\n"
        "$$T - (2)(9{,}8)\\sin 30^\\circ\\ \\checkmark - 2{,}5\\ \\checkmark = 2a\\ \\checkmark$$\n"
        "$$T - 9{,}8 - 2{,}5 = 2a$$\n"
        "$$T - 12{,}3 = 2a \\quad \\text{--- (1)}$$\n\n"
        "For the $3\\text{ kg}$ block (Q) (taking up the incline as positive):\n"
        "$$F_{\\text{net}} = ma$$\n"
        "$$F_x - T - w_\\parallel = ma$$\n"
        "$$40\\cos 25^\\circ\\ \\checkmark - T - (3)(9{,}8)\\sin 30^\\circ\\ \\checkmark = 3a\\ \\checkmark$$\n"
        "$$36{,}252 - T - 14{,}7 = 3a$$\n"
        "$$21{,}552 - T = 3a \\quad \\text{--- (2)}$$\n\n"
        "Adding equations (1) and (2):\n"
        "$$(T - 12{,}3) + (21{,}552 - T) = 2a + 3a$$\n"
        "$$9{,}252 = 5a$$\n"
        "$$a = 1{,}85\\text{ m}\\cdot\\text{s}^{-2}\\ \\checkmark$$\n\n"
        "**Marking criteria:**\n"
        "* $\\checkmark$ Formula: $F_{\\text{net}} = ma$\n"
        "* $\\checkmark$ Substitution of $w_\\parallel$ for $2\\text{ kg}$: $(2)(9{,}8)\\sin 30^\\circ$\n"
        "* $\\checkmark$ Substitution of $-2{,}5\\text{ N}$\n"
        "* $\\checkmark$ $2a$ OR $3a$\n"
        "* $\\checkmark$ Calculate component $F_x = 40\\cos 25^\\circ$ (or $40\\sin 65^\\circ$)\n"
        "* $\\checkmark$ Substitution of $w_\\parallel$ for $3\\text{ kg}$: $(3)(9{,}8)\\sin 30^\\circ$\n"
        "* $\\checkmark$ Left hand side substitution for $3\\text{ kg}$\n"
        "* $\\checkmark$ Final answer: $1{,}85\\text{ m}\\cdot\\text{s}^{-2}$\n\n"
        "*(Note: Systems approach / massless string approximation yields Max $5/8$ marks under DBE guidelines:*\n"
        "$$F_{\\text{net}} = ma$$\n"
        "$$40\\cos 25^\\circ\\ \\checkmark - (5)(9{,}8)\\sin 30^\\circ\\ \\checkmark - 2{,}5\\ \\checkmark = 5a$$\n"
        "$$a = 1{,}85\\text{ m}\\cdot\\text{s}^{-2}\\ \\checkmark)*"
    ),
    final_answer="$1{,}85\\text{ m}\\cdot\\text{s}^{-2}$"
)

add_item(
    q_ref="2.4",
    kind="question",
    marks=2,
    topic="Newton's Laws - Qualitative Effect of Friction Removal on Acceleration",
    passage=passage_q2,
    question="If block P has now passed point B, how will its acceleration compare to that calculated in QUESTION 2.3? Choose from GREATER THAN, SMALLER THAN or EQUAL TO.\n\nGive a reason for the answer.",
    memo=(
        "GREATER THAN $\\checkmark$\n\n"
        "$F_{\\text{net}}$ increases. / There is no friction (on section BC). / The surface is smooth. $\\checkmark$"
    ),
    final_answer="GREATER THAN; The net force increases because there is no friction acting on block P on section BC."
)

# ==========================================
# QUESTION 3: VERTICAL PROJECTILE MOTION
# ==========================================

passage_q3_intro = (
    "Stone A is thrown vertically upwards with a speed of $10\\text{ m}\\cdot\\text{s}^{-1}$ from the edge of the roof of a $40\\text{ m}$ high building. "
    "Take the ground as reference ($y = 0$). Ignore the effects of air friction.\n\n"
    "Stone B is dropped from rest from the edge of the roof, $x$ seconds after stone A was thrown upwards.\n\n"
    "Stone A passes stone B when the two stones are $29{,}74\\text{ m}$ above the ground."
)

add_item(
    q_ref="3.1",
    kind="question",
    marks=2,
    topic="Vertical Projectile Motion - Free Fall Definition",
    passage=passage_q3_intro,
    question="Define the term free fall.",
    memo=(
        "(Motion during which) the only force acting is the force of gravity. $\\checkmark\\checkmark$\n\n"
        "*(Marking criteria: 2 marks or 0 marks.)*"
    ),
    final_answer="Motion during which the only force acting is the force of gravity."
)

add_item(
    q_ref="3.2",
    kind="question",
    marks=4,
    topic="Vertical Projectile Motion - Maximum Height Above Ground",
    passage=passage_q3_intro,
    question="Calculate the maximum HEIGHT ABOVE THE GROUND reached by stone A.",
    memo=(
        "**OPTION 1 (Equations of motion):**\n"
        "Taking upwards as positive:\n"
        "$$v_f^2 = v_i^2 + 2a\\Delta y\\ \\checkmark$$\n"
        "$$0^2 = (10)^2 + 2(-9{,}8)\\Delta y\\ \\checkmark$$\n"
        "$$\\Delta y = 5{,}10\\text{ m}\\ (5{,}102\\text{ m})$$\n"
        "$$\\text{Height above ground} = 40 + 5{,}10\\ \\checkmark = 45{,}10\\text{ m}\\ \\checkmark$$\n\n"
        "*(Accept $45{,}1\\text{ m}$)*\n\n"
        "**OPTION 2 (Mechanical Energy Conservation):**\n"
        "$$E_{\\text{mech(roof)}} = E_{\\text{mech(top)}}$$\n"
        "$$(E_p + E_k)_{\\text{roof}} = (E_p + E_k)_{\\text{top}}$$\n"
        "$$m(9{,}8)(40) + \\frac{1}{2}m(10)^2\\ \\checkmark = m(9{,}8)h + 0\\ \\checkmark$$\n"
        "$$h = 45{,}10\\text{ m}\\ \\checkmark$$\n\n"
        "**Marking criteria:**\n"
        "* $\\checkmark$ Any appropriate formula for $\\Delta y$\n"
        "* $\\checkmark$ Whole substitution to calculate $5{,}10\\text{ m}$\n"
        "* $\\checkmark$ $40 + \\text{answer from calculation}$ ($40 + 5{,}10$)\n"
        "* $\\checkmark$ Final answer: $45{,}10\\text{ m}$"
    ),
    final_answer="$45{,}10\\text{ m}$"
)

add_item(
    q_ref="3.3",
    kind="question",
    marks=2,
    topic="Vertical Projectile Motion - Acceleration at Maximum Height",
    passage=passage_q3_intro,
    question="Write down the magnitude and direction of the acceleration of stone A at this maximum height.",
    memo="$9{,}8\\text{ m}\\cdot\\text{s}^{-2}\\ \\checkmark$ downwards $\\checkmark$",
    final_answer="$9{,}8\\text{ m}\\cdot\\text{s}^{-2}$ downwards"
)

add_item(
    q_ref="3.4",
    kind="question",
    marks=6,
    topic="Vertical Projectile Motion - Time Interval Calculation for Two Projectiles",
    passage=passage_q3_intro,
    question="Stone A passes stone B when the two stones are $29{,}74\\text{ m}$ above the ground.\n\nCalculate the value of $x$.",
    memo=(
        "Displacement of stones from roof ($40\\text{ m}$) to meeting point ($29{,}74\\text{ m}$):\n"
        "$$\\Delta y = 29{,}74 - 40 = -10{,}26\\text{ m}$$\n\n"
        "**Stone A (taking upwards as positive):**\n"
        "$$\\Delta y_A = v_i\\Delta t_A + \\frac{1}{2}a\\Delta t_A^2\\ \\checkmark$$\n"
        "$$-10{,}26 = (10)\\Delta t_A + \\frac{1}{2}(-9{,}8)\\Delta t_A^2\\ \\checkmark$$\n"
        "$$4{,}9\\Delta t_A^2 - 10\\Delta t_A - 10{,}26 = 0$$\n"
        "$$\\Delta t_A = \\frac{10 \\pm \\sqrt{(-10)^2 - 4(4{,}9)(-10{,}26)}}{2(4{,}9)} = 2{,}79\\text{ s}\\ (2{,}789\\text{ s})$$\n\n"
        "**Stone B (dropped from rest, $v_i = 0$):**\n"
        "$$\\Delta y_B = v_i\\Delta t_B + \\frac{1}{2}a\\Delta t_B^2$$\n"
        "$$-10{,}26\\ \\checkmark = 0 + \\frac{1}{2}(-9{,}8)\\Delta t_B^2\\ \\checkmark$$\n"
        "$$\\Delta t_B^2 = \\frac{10{,}26}{4{,}9} = 2{,}0939 \\implies \\Delta t_B = 1{,}45\\text{ s}\\ (1{,}447\\text{ s})$$\n\n"
        "**Time delay $x$:**\n"
        "$$x = \\Delta t_A - \\Delta t_B = 2{,}79 - 1{,}45\\ \\checkmark = 1{,}34\\text{ s}\\ \\checkmark$$\n\n"
        "*(Accept range: $1{,}34\\text{ s} - 1{,}35\\text{ s}$)*"
    ),
    final_answer="$1{,}34\\text{ s}$"
)

passage_q3_graph = (
    "Stone A is thrown vertically upwards with a speed of $10\\text{ m}\\cdot\\text{s}^{-1}$ from the roof of a $40\\text{ m}$ high building. "
    "Stone B is dropped from rest from the roof $x$ seconds after stone A was thrown upwards. "
    "The graphs of position versus time for part of the motion of both stones are shown:\n\n"
    "Graph features:\n"
    "- Vertical axis: Position (m) above the ground, marked with values $0$, $c$ (passing height, $29{,}74\\text{ m}$), $b$ (roof height, $40\\text{ m}$), $h$, and $a$ (maximum height of stone A, $45{,}10\\text{ m}$).\n"
    "- Horizontal axis: Time (s), marked with values $0$, $d$ (during the rising phase of stone A), $e$ (time stone A reaches maximum height), $f$ (time stone B is dropped, $t = x$), and $g$ (time when the two stones pass each other).\n"
    "- Curve for Stone A: Parabolic arc starting at $(0, b)$, rising to maximum height at $(e, a)$, and then falling down through point $(g, c)$.\n"
    "- Curve for Stone B: Parabolic arc starting from rest at $(f, b)$ and curving downwards, intersecting stone A's curve at $(g, c)$."
)

add_item(
    q_ref="3.5.1",
    kind="question",
    marks=1,
    topic="Vertical Projectile Motion - Interpreting Position-Time Graph (Positive Velocity)",
    passage=passage_q3_graph,
    question="Which of labels a to h on the graphs represents the time at which stone A has a positive velocity?",
    memo="d $\\checkmark$\n\n*(Accept: $0 - e$; $0 - d$; $d - e$)*",
    final_answer="d"
)

add_item(
    q_ref="3.5.2",
    kind="question",
    marks=1,
    topic="Vertical Projectile Motion - Interpreting Position-Time Graph (Maximum Height)",
    passage=passage_q3_graph,
    question="Which of labels a to h on the graphs represents the maximum height reached by stone A?",
    memo="a $\\checkmark$",
    final_answer="a"
)

add_item(
    q_ref="3.5.3",
    kind="question",
    marks=1,
    topic="Vertical Projectile Motion - Interpreting Position-Time Graph (Release Time)",
    passage=passage_q3_graph,
    question="Which of labels a to h on the graphs represents the time when stone B was dropped?",
    memo="f $\\checkmark$",
    final_answer="f"
)

add_item(
    q_ref="3.5.4",
    kind="question",
    marks=1,
    topic="Vertical Projectile Motion - Interpreting Position-Time Graph (Meeting Height)",
    passage=passage_q3_graph,
    question="Which of labels a to h on the graphs represents the height at which the stones pass each other?",
    memo="c $\\checkmark$",
    final_answer="c"
)

# ==========================================
# QUESTION 4: MOMENTUM & IMPULSE
# ==========================================

passage_q4 = (
    "A bullet moves east at a velocity of $480\\text{ m}\\cdot\\text{s}^{-1}$. It hits a wooden block that is fixed to the floor. "
    "The bullet takes $0{,}01\\text{ s}$ to move through the stationary block and emerges from the block at a velocity of $80\\text{ m}\\cdot\\text{s}^{-1}$ east.\n\n"
    "Ignore the effects of air resistance. Consider the block-bullet system as an isolated system.\n\n"
    "The magnitude of the momentum of the bullet before it enters the block is $24\\text{ kg}\\cdot\\text{m}\\cdot\\text{s}^{-1}$."
)

add_item(
    q_ref="4.1",
    kind="question",
    marks=2,
    topic="Momentum - Isolated System Definition",
    passage=passage_q4,
    question="Explain what is meant by an isolated system as used in Physics.",
    memo=(
        "An isolated system is a system on which the resultant/net external force is zero. $\\checkmark\\checkmark$\n\n"
        "*OR*\n\n"
        "An isolated system is one that has no net / external force acting on it. $\\checkmark\\checkmark$\n\n"
        "*(Marking criteria: -1 mark for each key word/phrase omitted in the correct context.)*"
    ),
    final_answer="An isolated system is a system on which the net external force is zero."
)

add_item(
    q_ref="4.2.1",
    kind="question",
    marks=3,
    topic="Momentum - Calculating Bullet Mass",
    passage=passage_q4,
    question="Calculate the mass of the bullet.",
    memo=(
        "$$p = mv\\ \\checkmark$$\n"
        "$$24 = m(480)\\ \\checkmark$$\n"
        "$$m = 0{,}05\\text{ kg}\\ \\checkmark$$"
    ),
    final_answer="$0{,}05\\text{ kg}$"
)

add_item(
    q_ref="4.2.2",
    kind="question",
    marks=5,
    topic="Impulse and Momentum - Average Net Force on Bullet",
    passage=passage_q4,
    question="Calculate the average net force exerted by the wooden block on the bullet.",
    memo=(
        "**POSITIVE MARKING FROM QUESTION 4.2.1**\n\n"
        "**OPTION 1 (Impulse-momentum theorem):**\n"
        "Taking east as positive:\n"
        "$$F_{\\text{net}}\\Delta t = \\Delta p\\ \\checkmark$$\n"
        "$$F_{\\text{net}}\\Delta t = (mv)_{\\text{f}} - (mv)_{\\text{i}}$$\n"
        "$$F_{\\text{net}}(0{,}01)\\ \\checkmark = (0{,}05)(80) - 24\\ \\checkmark$$\n"
        "$$F_{\\text{net}}(0{,}01) = 4 - 24 = -20$$\n"
        "$$F_{\\text{net}} = -2\\ 000\\text{ N}$$\n"
        "$$F_{\\text{net}} = 2\\ 000\\text{ N}\\ \\checkmark\\text{ west (or left)}\\ \\checkmark$$\n\n"
        "**OPTION 2 (Newton's second law and motion equation):**\n"
        "$$v_f = v_i + a\\Delta t$$\n"
        "$$80 = 480 + a(0{,}01)\\ \\checkmark \\implies a = -40\\ 000\\text{ m}\\cdot\\text{s}^{-2}$$\n"
        "$$F_{\\text{net}} = ma\\ \\checkmark = (0{,}05)(-40\\ 000)\\ \\checkmark = -2\\ 000\\text{ N}$$\n"
        "$$F_{\\text{net}} = 2\\ 000\\text{ N}\\ \\checkmark\\text{ west (or left)}\\ \\checkmark$$\n\n"
        "**Marking criteria:**\n"
        "* $\\checkmark$ Appropriate formula including $F_{\\text{net}}$ or $W_{\\text{net}}$\n"
        "* $\\checkmark\\checkmark$ Correct substitutions\n"
        "* $\\checkmark$ Final answer: $2\\ 000\\text{ N}$\n"
        "* $\\checkmark$ Correct direction: west or left"
    ),
    final_answer="$2\\ 000\\text{ N}$ west"
)

# ==========================================
# QUESTION 5: WORK, ENERGY AND POWER
# ==========================================

passage_q5 = (
    "An object of mass $1{,}8\\text{ kg}$ slides down a rough curved track and passes point A, which is $1{,}5\\text{ m}$ above the ground, at a speed of $0{,}95\\text{ m}\\cdot\\text{s}^{-1}$.\n\n"
    "The object reaches point B at the bottom of the track (at ground level) at a speed of $4\\text{ m}\\cdot\\text{s}^{-1}$.\n\n"
    "Surface BC is horizontal and frictionless."
)

add_item(
    q_ref="5.1",
    kind="question",
    marks=2,
    topic="Work, Energy and Power - Conservative Force Definition",
    passage=passage_q5,
    question="Define the term conservative force.",
    memo=(
        "A conservative force is a force for which the work done (in moving an object between two points) is independent of the path taken. $\\checkmark\\checkmark$\n\n"
        "*OR*\n\n"
        "A conservative force is a force for which the work done in moving an object in a closed path is zero. $\\checkmark\\checkmark$\n\n"
        "*(Note: -1 mark for each key word/phrase omitted in the correct context. If the word 'work' is omitted: 0 marks.)*"
    ),
    final_answer="A conservative force is a force for which the work done in moving an object between two points is independent of the path taken."
)

add_item(
    q_ref="5.2",
    kind="question",
    marks=1,
    topic="Work, Energy and Power - Identifying Conservative Force",
    passage=passage_q5,
    question="Name the conservative force acting on the object.",
    memo="Gravitational force / Gravity / Gravitation / Weight $\\checkmark$",
    final_answer="Gravitational force (or weight)"
)

add_item(
    q_ref="5.3",
    kind="question",
    marks=2,
    topic="Work, Energy and Power - Conservation of Mechanical Energy Check",
    passage=passage_q5,
    question="Is mechanical energy conserved as the object slides from point A to point B? Choose from YES or NO. Give a reason for the answer.",
    memo=(
        "NO $\\checkmark$\n\n"
        "There is friction / a non-conservative force (doing work). / It is not an isolated system. / The net work done by the non-conservative forces is not zero. $\\checkmark$"
    ),
    final_answer="NO; Friction (a non-conservative force) does work on the object, dissipating mechanical energy."
)

add_item(
    q_ref="5.4",
    kind="question",
    marks=3,
    topic="Work, Energy and Power - Gravitational Potential Energy Calculation",
    passage=passage_q5,
    question="Calculate the gravitational potential energy of the object when it was at point A.",
    memo=(
        "$$E_p = mgh\\ \\checkmark$$\n"
        "$$E_p = (1{,}8)(9{,}8)(1{,}5)\\ \\checkmark$$\n"
        "$$E_p = 26{,}46\\text{ J}\\ \\checkmark$$"
    ),
    final_answer="$26{,}46\\text{ J}$"
)

add_item(
    q_ref="5.5",
    kind="question",
    marks=4,
    topic="Work, Energy and Power - Work Done by Friction",
    passage=passage_q5,
    question="Using energy principles, calculate the work done by friction on the object as it slides from point A to point B.",
    memo=(
        "**POSITIVE MARKING FROM QUESTION 5.4**\n\n"
        "**OPTION 1 (Work done by non-conservative forces):**\n"
        "$$W_{\\text{nc}} = \\Delta E_k + \\Delta E_p$$\n"
        "$$W_f = \\frac{1}{2}m(v_f^2 - v_i^2) + mg(h_f - h_i)$$\n"
        "$$W_f = \\frac{1}{2}(1{,}8)(4^2 - 0{,}95^2)\\ \\checkmark + (0 - 26{,}46)\\ \\checkmark$$\n"
        "$$W_f = 13{,}58775 - 26{,}46$$\n"
        "$$W_f = -12{,}87\\text{ J}\\ \\checkmark\\ (-12{,}872\\text{ J})$$\n\n"
        "**OPTION 2 (Work-Energy Theorem):**\n"
        "$$W_{\\text{net}} = \\Delta E_k$$\n"
        "$$W_f + W_g = \\frac{1}{2}mv_f^2 - \\frac{1}{2}mv_i^2$$\n"
        "$$W_f + 26{,}46\\ \\checkmark = \\frac{1}{2}(1{,}8)[(4)^2 - (0{,}95)^2]\\ \\checkmark$$\n"
        "$$W_f = -12{,}87\\text{ J}\\ \\checkmark$$\n\n"
        "**OPTION 3 (Energy balance):**\n"
        "$$(E_p + E_k)_A + W_f = (E_p + E_k)_B$$\n"
        "$$26{,}46 + \\frac{1}{2}(1{,}8)(0{,}95^2)\\ \\checkmark + W_f = 0 + \\frac{1}{2}(1{,}8)(4^2)\\ \\checkmark$$\n"
        "$$W_f = -12{,}87\\text{ J}\\ \\checkmark$$"
    ),
    final_answer="$-12{,}87\\text{ J}$"
)

add_item(
    q_ref="5.6",
    kind="question",
    marks=1,
    topic="Work, Energy and Power - Net Work on Frictionless Horizontal Surface",
    passage=passage_q5,
    question="Surface BC in the diagram above is frictionless.\n\nWhat is the value of the net work done on the object as it slides from point B to point C?",
    memo="$W_{\\text{net}} = 0\\text{ J}$ / zero $\\checkmark$\n\n*(Rationale: On a horizontal frictionless surface, the normal force and gravity are perpendicular to displacement, and frictional force is zero. Therefore, $F_{\\text{net}} = 0$ and $W_{\\text{net}} = 0\\text{ J}$.)*",
    final_answer="$0\\text{ J}$"
)

# ==========================================
# QUESTION 6: DOPPLER EFFECT
# ==========================================

passage_q6 = (
    "The siren of a police car, which is travelling at a constant speed along a straight horizontal road, emits sound waves of constant frequency. "
    "Detector P is placed inside the police car and detector Q is placed next to the road at a certain distance away from the car. "
    "The two detectors record the changes in the air pressure readings caused by the sound waves emitted by the siren as a function of time.\n\n"
    "The graphs below were obtained from the recorded results:\n\n"
    "- GRAPH A: AIR PRESSURE VS TIME RECORDED BY DETECTOR P IN THE CAR\n"
    "A sinusoidal waveform of air pressure versus time ($\\times 10^{-4}\\text{ s}$). "
    "The first crest reaches zero at $8{,}5\\times 10^{-4}\\text{ s}$ (half cycle), one complete cycle ends at $17\\times 10^{-4}\\text{ s}$, and one and a half cycles end at $25{,}5\\times 10^{-4}\\text{ s}$.\n\n"
    "- GRAPH B: AIR PRESSURE VS TIME RECORDED BY DETECTOR Q NEXT TO THE ROAD\n"
    "A sinusoidal waveform of air pressure versus time ($\\times 10^{-4}\\text{ s}$). "
    "The first crest reaches zero at $9\\times 10^{-4}\\text{ s}$ (half cycle), one complete cycle ends at $18\\times 10^{-4}\\text{ s}$, and one and a half cycles end at $27\\times 10^{-4}\\text{ s}$."
)

add_item(
    q_ref="6.1",
    kind="question",
    marks=1,
    topic="Doppler Effect - Phenomenon Identification",
    passage=passage_q6,
    question="Different patterns are shown above for the same sound wave emitted by the siren. What phenomenon is illustrated by the two detectors showing the different patterns?",
    memo="Doppler effect $\\checkmark$",
    final_answer="Doppler effect"
)

add_item(
    q_ref="6.2",
    kind="question",
    marks=1,
    topic="Doppler Effect - Direction of Motion from Wave Periods",
    passage=passage_q6 + "\n\nThe police car is moving AWAY from detector Q.",
    question="Use the graphs and give a reason why it can be confirmed that the police car is moving away from detector Q.",
    memo=(
        "Detector Q records sounds with a longer period / longer time per wave / lower frequency than detector P. $\\checkmark$\n\n"
        "*OR*\n\n"
        "Detector P records sounds with a shorter period / shorter time per wave / higher frequency than detector Q. $\\checkmark$\n\n"
        "*(ACCEPT: Detector Q records a longer wavelength / Detector P records a shorter wavelength.)*"
    ),
    final_answer="Detector Q records a longer wave period (lower frequency) than detector P, confirming the source is moving away from detector Q."
)

add_item(
    q_ref="6.3",
    kind="question",
    marks=3,
    topic="Doppler Effect - Frequency of Waves Recorded by Source Detector P",
    passage=passage_q6,
    question="Calculate the frequency of the sound waves recorded by detector P.",
    memo=(
        "**OPTION 1:**\n"
        "From Graph A, the period of one complete wave is $T = 17 \\times 10^{-4}\\text{ s}$:\n"
        "$$f = \\frac{1}{T}\\ \\checkmark$$\n"
        "$$f = \\frac{1}{17 \\times 10^{-4}}\\ \\checkmark$$\n"
        "$$f = 588{,}24\\text{ Hz}\\ \\checkmark\\ (5{,}88 \\times 10^2\\text{ Hz})$$\n\n"
        "**OPTION 2:**\n"
        "$$v = f\\lambda\\ \\checkmark$$\n"
        "$$\\text{Distance for } 1\\frac{1}{2}\\lambda = 340 \\times (25{,}5 \\times 10^{-4}) = 0{,}867\\text{ m} \\implies \\lambda = 0{,}578\\text{ m}$$\n"
        "$$340 = f(0{,}578)\\ \\checkmark \\implies f = 588{,}24\\text{ Hz}\\ \\checkmark$$"
    ),
    final_answer="$588{,}24\\text{ Hz}$"
)

add_item(
    q_ref="6.4",
    kind="question",
    marks=6,
    topic="Doppler Effect - Calculating Speed of Moving Source",
    passage=passage_q6,
    question="Use the information in the graphs to calculate the speed of the police car. Take the speed of sound in air as $340\\text{ m}\\cdot\\text{s}^{-1}$.",
    memo=(
        "**POSITIVE MARKING FROM QUESTIONS 6.2 AND 6.3**\n\n"
        "*(Do not penalise if $10^{-4}$ is again omitted.)*\n\n"
        "**Step 1: Calculate frequency detected by Q ($f_L$):**\n"
        "From Graph B, period $T_L = 18 \\times 10^{-4}\\text{ s}$:\n"
        "$$f_L = \\frac{1}{T_L} = \\frac{1}{18 \\times 10^{-4}}\\ \\checkmark = 555{,}56\\text{ Hz}$$\n\n"
        "**Step 2: Apply the Doppler formula for a source moving away:**\n"
        "$$f_L = \\left(\\frac{v}{v + v_s}\\right) f_s\\ \\checkmark$$\n"
        "$$555{,}56\\ \\checkmark = \\left(\\frac{340\\ \\checkmark}{340 + v_s\\ \\checkmark}\\right)(588{,}24)$$\n"
        "$$340 + v_s = \\frac{340 \\times 588{,}24}{555{,}56} = 360$$\n"
        "$$v_s = 20\\text{ m}\\cdot\\text{s}^{-1}\\ \\checkmark$$\n\n"
        "*(Accept range: $19{,}57\\text{ m}\\cdot\\text{s}^{-1} - 20{,}09\\text{ m}\\cdot\\text{s}^{-1}$)*"
    ),
    final_answer="$20\\text{ m}\\cdot\\text{s}^{-1}$"
)

# ==========================================
# QUESTION 7: ELECTROSTATICS
# ==========================================

passage_q7_1 = (
    "A small sphere, Y, carrying an unknown charge, is suspended at the end of a light inextensible string which is attached to a fixed point. "
    "Another sphere, X, carrying a charge of $+6 \\times 10^{-6}\\text{ C}$, on an insulated stand is brought close to sphere Y.\n\n"
    "Sphere Y experiences an electrostatic force and comes to rest $0{,}2\\text{ m}$ away from sphere X, with the string at an angle of $10^\\circ$ with the vertical, as shown in the diagram."
)

add_item(
    q_ref="7.1.1",
    kind="question",
    marks=1,
    topic="Electrostatics - Determining Nature of Unknown Charge",
    passage=passage_q7_1,
    question="What is the nature of the charge on sphere Y? Choose from POSITIVE or NEGATIVE.",
    memo="Positive $\\checkmark$\n\n*Rationale: Sphere X is positively charged ($+6 \\times 10^{-6}\\text{ C}$) and sphere Y is repelled to the right away from sphere X. Since like charges repel, sphere Y must carry a positive charge.*",
    final_answer="Positive"
)

add_item(
    q_ref="7.1.2",
    kind="question",
    marks=3,
    topic="Electrostatics - Coulomb's Law Charge Calculation",
    passage=passage_q7_1,
    question="Calculate the magnitude of the charge on sphere Y if the magnitude of the electrostatic force acting on it is $3{,}05\\text{ N}$.",
    memo=(
        "**OPTION 1:**\n"
        "$$F = \\frac{k Q_1 Q_2}{r^2}\\ \\checkmark$$\n"
        "$$3{,}05 = \\frac{(9{,}0 \\times 10^9)(6 \\times 10^{-6}) Q_Y}{(0{,}2)^2}\\ \\checkmark$$\n"
        "$$3{,}05 = \\frac{54\\ 000 Q_Y}{0{,}04} = 1{,}35 \\times 10^6 Q_Y$$\n"
        "$$Q_Y = 2{,}26 \\times 10^{-6}\\text{ C}\\ \\checkmark\\ (2{,}259 \\times 10^{-6}\\text{ C})$$\n\n"
        "**OPTION 2:**\n"
        "$$E = \\frac{k Q}{r^2} = \\frac{(9{,}0 \\times 10^9)(6 \\times 10^{-6})}{(0{,}2)^2} = 1{,}35 \\times 10^6\\text{ N}\\cdot\\text{C}^{-1}$$\n"
        "$$F = Eq\\ \\checkmark$$\n"
        "$$3{,}05 = (1{,}35 \\times 10^6)q\\ \\checkmark$$\n"
        "$$q = 2{,}26 \\times 10^{-6}\\text{ C}\\ \\checkmark$$"
    ),
    final_answer="$2{,}26 \\times 10^{-6}\\text{ C}$"
)

add_item(
    q_ref="7.1.3",
    kind="question",
    marks=3,
    topic="Electrostatics - Free-Body Diagram for Suspended Sphere",
    passage=passage_q7_1,
    question="Draw a labelled free-body diagram for sphere Y.",
    memo=(
        "Accepted forces acting on sphere Y:\n"
        "* $\\checkmark$ $T$ / $F_T$ / tension (acting upwards and to the left along the string at $10^\\circ$ to the vertical)\n"
        "* $\\checkmark$ $F_E$ / $F$ / electrostatic force / Coulomb force ($3{,}05\\text{ N}$, acting horizontally to the right, away from X)\n"
        "* $\\checkmark$ $w$ / $F_g$ / $F_w$ / weight / $mg$ / gravitational force (acting vertically downwards)\n\n"
        "*(Marking notes:*\n"
        "* *Mark is awarded for label and arrow.*\n"
        "* *Do not penalise for length of arrows.*\n"
        "* *Deduct 1 mark for any additional force.*\n"
        "* *If force(s) do not make contact with dot: Max $2/3$.*\n"
        "* *If arrows missing: Max $2/3$.)*"
    ),
    final_answer="Labelled free-body diagram with 3 forces on sphere Y: Tension T (up-left along string), Electrostatic force F_E (horizontally right), and Weight w (vertically down)."
)

add_item(
    q_ref="7.1.4",
    kind="question",
    marks=3,
    topic="Electrostatics - String Tension Calculation in Equilibrium",
    passage=passage_q7_1,
    question="Calculate the magnitude of the tension in the string.",
    memo=(
        "In equilibrium, the net force is zero ($F_{\\text{net}} = 0$):\n"
        "$$\\Sigma F_x = 0 \\implies F_E = T\\sin 10^\\circ$$\n"
        "$$3{,}05 = T\\sin 10^\\circ\\ \\checkmark\\checkmark$$\n"
        "$$T = \\frac{3{,}05}{\\sin 10^\\circ} = 17{,}56\\text{ N}\\ \\checkmark\\ (17{,}564\\text{ N})$$\n\n"
        "*OR using complementary angle ($80^\\circ$ to the horizontal):*\n"
        "$$3{,}05 = T\\cos 80^\\circ\\ \\checkmark\\checkmark \\implies T = 17{,}56\\text{ N}\\ \\checkmark$$\n\n"
        "*(Note: If $T\\cos 10^\\circ = 3{,}05$ is used incorrectly: $1/3$ marks).* "
    ),
    final_answer="$17{,}56\\text{ N}$"
)

passage_q7_2 = (
    "Two small charged spheres, A and B, on insulated stands, with charges $+2 \\times 10^{-5}\\text{ C}$ and $-4 \\times 10^{-5}\\text{ C}$ respectively, "
    "are placed $0{,}4\\text{ m}$ apart. M is the midpoint between spheres A and B (distance from A to M is $0{,}2\\text{ m}$ and from M to B is $0{,}2\\text{ m}$)."
)

add_item(
    q_ref="7.2.1",
    kind="question",
    marks=2,
    topic="Electrostatics - Electric Field at a Point Definition",
    passage=passage_q7_2,
    question="Define the term electric field at a point.",
    memo=(
        "The electric field at a point is the (electrostatic) force experienced per unit positive charge placed at that point. $\\checkmark\\checkmark$\n\n"
        "*OR*\n\n"
        "The electric field at a point is the (electrostatic) force experienced by a UNIT positive charge placed at that point. $\\checkmark\\checkmark$\n\n"
        "*(Marking criteria: -1 mark for each key word/phrase omitted in the correct context. If the word 'unit' or phrase 'positive charge' is omitted: -1 for each. If 'UNIT' is omitted in the second definition: 0 marks.)*"
    ),
    final_answer="The electric field at a point is the electrostatic force experienced per unit positive charge placed at that point."
)

add_item(
    q_ref="7.2.2",
    kind="question",
    marks=6,
    topic="Electrostatics - Net Electric Field Calculation at Midpoint",
    passage=passage_q7_2,
    question="Calculate the net electric field at point M.",
    memo=(
        "**OPTION 1:**\n"
        "Electric field at M due to charge A ($Q_A = +2 \\times 10^{-5}\\text{ C}$), directed to the right (away from positive charge A):\n"
        "$$E_A = \\frac{k Q_A}{r^2}\\ \\checkmark = \\frac{(9{,}0 \\times 10^9)(2 \\times 10^{-5})}{(0{,}2)^2}\\ \\checkmark = 4{,}5 \\times 10^6\\text{ N}\\cdot\\text{C}^{-1}\\text{ to the right}$$\n\n"
        "Electric field at M due to charge B ($Q_B = -4 \\times 10^{-5}\\text{ C}$), directed to the right (towards negative charge B):\n"
        "$$E_B = \\frac{k Q_B}{r^2} = \\frac{(9{,}0 \\times 10^9)(4 \\times 10^{-5})}{(0{,}2)^2}\\ \\checkmark = 9{,}0 \\times 10^6\\text{ N}\\cdot\\text{C}^{-1}\\text{ to the right}$$\n\n"
        "Net electric field at M:\n"
        "$$E_{\\text{net}} = E_A + E_B = (4{,}5 \\times 10^6 + 9{,}0 \\times 10^6)\\ \\checkmark$$\n"
        "$$E_{\\text{net}} = 1{,}35 \\times 10^7\\text{ N}\\cdot\\text{C}^{-1}\\ \\checkmark\\text{ to the right (towards B / away from A)}\\ \\checkmark$$\n\n"
        "**OPTION 2 (Force method):**\n"
        "$$F_{\\text{net}} = \\frac{k Q_A q}{(0{,}2)^2} + \\frac{k Q_B q}{(0{,}2)^2} = 4{,}5 \\times 10^6 q + 9 \\times 10^6 q = 1{,}35 \\times 10^7 q\\text{ N}$$\n"
        "$$E_{\\text{net}} = \\frac{F_{\\text{net}}}{q} = 1{,}35 \\times 10^7\\text{ N}\\cdot\\text{C}^{-1}\\ \\checkmark\\text{ to the right}\\ \\checkmark$$\n\n"
        "*(Note: If $F = \\frac{kQ}{r^2}$ is used instead of $E = \\frac{kQ}{r^2}$: Max $2/6$).*"
    ),
    final_answer="$1{,}35 \\times 10^7\\text{ N}\\cdot\\text{C}^{-1}$ to the right"
)

# ==========================================
# QUESTION 8: ELECTRIC CIRCUITS
# ==========================================

passage_q8_1 = (
    "In the circuit diagram below, resistor R, with a resistance of $5{,}6\\ \\Omega$, is connected, together with a switch S, "
    "an ammeter A and a high-resistance voltmeter V, to a battery of emf $\\mathcal{E}$ with an unknown internal resistance, $r$.\n\n"
    "The resistance of the connecting wires and the ammeter may be ignored.\n\n"
    "The graph below shows the potential difference across the terminals of the battery as a function of time:\n"
    "- For $t < t_1$, switch S is OPEN: The voltmeter reading is constant at $13\\text{ V}$.\n"
    "- At time $t_1$, switch S is CLOSED: The voltmeter reading drops to $10{,}5\\text{ V}$ and remains constant."
)

add_item(
    q_ref="8.1",
    kind="question",
    marks=2,
    topic="Electric Circuits - emf Definition",
    passage=passage_q8_1,
    question="Define the term emf of a battery.",
    memo=(
        "(Maximum) energy provided (work done) $\\checkmark$ by a battery per coulomb / unit charge passing through it. $\\checkmark$\n\n"
        "*ACCEPT:*\n"
        "The reading on a voltmeter connected across a battery when there is no current / in an open circuit. $\\checkmark\\checkmark$"
    ),
    final_answer="The maximum energy provided by a battery per unit charge passing through it."
)

add_item(
    q_ref="8.2",
    kind="question",
    marks=1,
    topic="Electric Circuits - Reading emf from Terminal Potential Difference Graph",
    passage=passage_q8_1,
    question="Write down the value of the emf of the battery.",
    memo="$13\\text{ V}\\ \\checkmark$",
    final_answer="$13\\text{ V}$"
)

add_item(
    q_ref="8.3.1",
    kind="question",
    marks=3,
    topic="Electric Circuits - Current Calculation Using Ohm's Law",
    passage=passage_q8_1,
    question="When switch S is CLOSED, calculate the current through resistor R.",
    memo=(
        "$$R = \\frac{V}{I}\\ \\checkmark$$\n"
        "$$5{,}6 = \\frac{10{,}5}{I}\\ \\checkmark$$\n"
        "$$I = 1{,}88\\text{ A}\\ \\checkmark\\ (1{,}875\\text{ A})$$\n\n"
        "**Marking criteria:**\n"
        "* $\\checkmark$ Appropriate formula\n"
        "* $\\checkmark$ Whole substitution\n"
        "* $\\checkmark$ Final answer: $1{,}88\\text{ A}$"
    ),
    final_answer="$1{,}88\\text{ A}$"
)

add_item(
    q_ref="8.3.2",
    kind="question",
    marks=3,
    topic="Electric Circuits - Power Dissipated in Resistor",
    passage=passage_q8_1,
    question="When switch S is CLOSED, calculate the power dissipated in resistor R.",
    memo=(
        "**POSITIVE MARKING FROM QUESTION 8.3.1**\n\n"
        "**OPTION 1:**\n"
        "$$P = VI\\ \\checkmark = (10{,}5)(1{,}88)\\ \\checkmark = 19{,}74\\text{ W}\\ \\checkmark\\ (19{,}688\\text{ W})$$\n\n"
        "**OPTION 2:**\n"
        "$$P = I^2 R\\ \\checkmark = (1{,}88)^2(5{,}6)\\ \\checkmark = 19{,}79\\text{ W}\\ \\checkmark\\ (19{,}688\\text{ W})$$\n\n"
        "**OPTION 3:**\n"
        "$$P = \\frac{V^2}{R}\\ \\checkmark = \\frac{(10{,}5)^2}{5{,}6}\\ \\checkmark = 19{,}69\\text{ W}\\ \\checkmark\\ (19{,}688\\text{ W})$$"
    ),
    final_answer="$19{,}69\\text{ W}$"
)

add_item(
    q_ref="8.3.3",
    kind="question",
    marks=3,
    topic="Electric Circuits - Internal Resistance Calculation",
    passage=passage_q8_1,
    question="When switch S is CLOSED, calculate the internal resistance, $r$, of the battery.",
    memo=(
        "**POSITIVE MARKING FROM QUESTIONS 8.2 AND 8.3.1**\n\n"
        "**OPTION 1:**\n"
        "$$\\mathcal{E} = I(R + r)\\ \\checkmark$$\n"
        "$$13 = 1{,}88(5{,}6 + r)\\ \\checkmark$$\n"
        "$$r = 1{,}31\\ \\Omega\\ \\checkmark\\ (1{,}31\\ \\Omega - 1{,}33\\ \\Omega)$$\n\n"
        "**OPTION 2:**\n"
        "$$V_{\\text{int}} = \\mathcal{E} - V_{\\text{ext}} = 13 - 10{,}5 = 2{,}5\\text{ V}$$\n"
        "$$r = \\frac{V_{\\text{int}}}{I}\\ \\checkmark = \\frac{2{,}5}{1{,}88}\\ \\checkmark = 1{,}33\\ \\Omega\\ \\checkmark\\ (1{,}31\\ \\Omega - 1{,}33\\ \\Omega)$$\n\n"
        "**OPTION 3:**\n"
        "$$V_{\\text{int}} = Ir\\ \\checkmark \\implies 2{,}5 = (1{,}88)r\\ \\checkmark \\implies r = 1{,}31\\ \\Omega\\ \\checkmark$$"
    ),
    final_answer="$1{,}31\\ \\Omega$"
)

passage_q8_2 = (
    "Two IDENTICAL resistors, each with resistance $X$, are now connected in the same circuit with switch S closed.\n\n"
    "Circuit configuration: The original resistor R ($5{,}6\\ \\Omega$) is in parallel with a branch containing the two identical resistors of resistance $X$ connected in series with each other (total branch resistance $R_{2X} = 2X$).\n\n"
    "The ammeter reading now increases to $4\\text{ A}$."
)

add_item(
    q_ref="8.4.1",
    kind="question",
    marks=2,
    topic="Electric Circuits - Internal Resistance and Voltmeter Reading Change",
    passage=passage_q8_2,
    question="How would the voltmeter reading change? Choose from INCREASES, DECREASES or REMAINS THE SAME.\n\nGive a reason for the answer by referring to $V_{\\text{internal resistance}}$.",
    memo=(
        "DECREASES $\\checkmark$\n\n"
        "$V_{\\text{internal resistance}}$ (or internal volts / lost volts) increases. $\\checkmark$\n\n"
        "*(Rationale: Since total current increases to $4\\text{ A}$, the internal voltage drop $V_{\\text{int}} = Ir$ increases. Because the terminal potential difference is $V_{\\text{ext}} = \\mathcal{E} - Ir$, the voltmeter reading decreases).* "
    ),
    final_answer="DECREASES; Internal voltage drop (V_internal resistance = Ir) increases as current increases, which reduces the terminal potential difference."
)

add_item(
    q_ref="8.4.2",
    kind="question",
    marks=5,
    topic="Electric Circuits - Calculating Unknown Resistance in Parallel Combination",
    passage=passage_q8_2,
    question="Calculate resistance $X$.",
    memo=(
        "**POSITIVE MARKING FROM QUESTIONS 8.2 AND 8.3.3**\n\n"
        "**OPTION 1 (Equivalent resistance method):**\n"
        "$$\\mathcal{E} = I(R_{\\text{ext}} + r)\\ \\checkmark$$\n"
        "$$13 = 4(R_{\\text{ext}} + 1{,}31)\\ \\checkmark$$\n"
        "$$R_{\\text{ext}} = 1{,}94\\ \\Omega\\ (1{,}92\\ \\Omega)$$\n\n"
        "Since resistor R ($5{,}6\\ \\Omega$) is in parallel with the series branch of resistance $R_{2X} = 2X$:\n"
        "$$\\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2}$$\n"
        "$$\\frac{1}{1{,}94} = \\frac{1}{5{,}6} + \\frac{1}{R_{2X}}\\ \\checkmark$$\n"
        "$$R_{2X} = 2{,}97\\ \\Omega\\ (2{,}92\\ \\Omega)$$\n\n"
        "Since the two resistors in series are identical:\n"
        "$$X = \\frac{1}{2} R_{2X}\\ \\checkmark = \\frac{1}{2}(2{,}97) = 1{,}49\\ \\Omega\\ \\checkmark$$\n\n"
        "*(Accept range: $1{,}46\\ \\Omega - 1{,}49\\ \\Omega$)*\n\n"
        "**OPTION 2 (Branch currents and voltage method):**\n"
        "$$\\mathcal{E} = I(R + r)\\ \\checkmark$$\n"
        "$$V_{\\text{ext}} = 13 - (4)(1{,}31)\\ \\checkmark = 7{,}76\\text{ V}$$\n"
        "$$I_{5{,}6\\,\\Omega} = \\frac{V_{\\text{ext}}}{5{,}6} = \\frac{7{,}76}{5{,}6} = 1{,}39\\text{ A}$$\n"
        "$$I_{2X} = I_{\\text{total}} - I_{5{,}6\\,\\Omega} = 4 - 1{,}39 = 2{,}61\\text{ A}$$\n"
        "$$V_{2X} = I_{2X}(2X) \\implies 7{,}76 = (2{,}61)(2X)\\ \\checkmark\\checkmark$$\n"
        "$$X = 1{,}49\\ \\Omega\\ \\checkmark$$\n\n"
        "**Marking criteria:**\n"
        "* $\\checkmark$ Formula: $\\mathcal{E} = I(R + r)$\n"
        "* $\\checkmark$ Correct substitution into $\\mathcal{E} = I(R + r)$\n"
        "* $\\checkmark$ Substitution of values into $R_p$ formula\n"
        "* $\\checkmark$ Halving value of $R_{2X}$ ($X = \\frac{1}{2}R_{2X}$)\n"
        "* $\\checkmark$ Final answer: $1{,}49\\ \\Omega$"
    ),
    final_answer="$1{,}49\\ \\Omega$"
)

# ==========================================
# QUESTION 9: ELECTRODYNAMICS & AC/DC
# ==========================================

passage_q9_1 = (
    "A simplified diagram of an electric generator is shown below. "
    "A rectangular armature coil is mounted between the North and South magnetic poles of a permanent magnet. "
    "The two ends of the coil are connected to the segments of a split-ring commutator, which contact stationary carbon brushes connected to an external circuit. "
    "When the coil is rotated at a constant speed, an emf is induced in the coil."
)

add_item(
    q_ref="9.1.1",
    kind="question",
    marks=1,
    topic="Electrodynamics - Identifying DC Generator from Split-Ring Commutator",
    passage=passage_q9_1,
    question="Is this an AC generator or a DC generator?",
    memo="DC (generator) $\\checkmark$\n\n*Rationale: The generator has a split-ring commutator rather than slip rings, which reverses the connection to the external circuit every half turn to provide unidirectional direct current (DC).*",
    final_answer="DC generator"
)

add_item(
    q_ref="9.1.2",
    kind="question",
    marks=2,
    topic="Electrodynamics - Principle of Electromagnetic Induction in Generator",
    passage=passage_q9_1,
    question="Briefly explain how an emf is generated in the coil when the coil is rotated by referring to the principle of electromagnetic induction.",
    memo=(
        "Emf is induced as a result of a change of magnetic flux (linked) with the coil. $\\checkmark\\checkmark$\n\n"
        "*(Marking criteria: -1 mark for each key word/phrase omitted in correct context.)*"
    ),
    final_answer="An emf is induced in the coil as a result of the change of magnetic flux linked with the coil as it rotates."
)

add_item(
    q_ref="9.1.3",
    kind="question",
    marks=2,
    topic="Electrodynamics - Sketch Graph of DC Generator Output Voltage",
    passage=passage_q9_1,
    question="Draw a sketch graph of the output voltage versus time for this generator. Show ONE complete cycle.",
    memo=(
        "**POSITIVE MARKING FROM QUESTION 9.1.1**\n\n"
        "A sketch graph of output voltage $V$ (or emf) on the vertical axis versus time $t$ on the horizontal axis showing:\n"
        "* $\\checkmark$ Correct shape (pulsating direct voltage: two positive half-sine humps above the time axis, touching $V = 0$ at the start, middle, and end of the cycle; OR two negative half-sine humps depending on assigned polarity)\n"
        "* $\\checkmark$ One complete cycle (showing 2 peaks / pulsations per complete rotation cycle)\n\n"
        "*(If AC was identified in 9.1.1: 1 full sinusoidal wave cycle with one positive and one negative half cycle awarded 2 marks).* "
    ),
    final_answer="A sketch graph of output voltage versus time showing pulsating DC: two positive half-sine humps above the time axis for one complete cycle."
)

passage_q9_2 = (
    "A $200\\ \\Omega$ resistor is connected to a DC voltage supply, as shown in Diagram A. "
    "The energy dissipated in the resistor in $10\\text{ s}$ is $500\\text{ J}$.\n\n"
    "The same resistor is now connected to an AC source (Diagram B) and $500\\text{ J}$ of energy is also dissipated in the resistor in $10\\text{ s}$."
)

add_item(
    q_ref="9.2.1",
    kind="question",
    marks=2,
    topic="Alternating Current - Definition of rms Voltage",
    passage=passage_q9_2,
    question="Define the term rms voltage of an AC source.",
    memo=(
        "The AC potential difference/voltage which dissipates the same amount of energy $\\checkmark$ as an equivalent DC potential difference/voltage. $\\checkmark$\n\n"
        "*OR*\n\n"
        "(The rms value of AC is) the DC potential difference/voltage which dissipates the same amount of energy $\\checkmark$ as the AC potential difference/voltage. $\\checkmark$"
    ),
    final_answer="The rms voltage of an AC source is the AC potential difference that dissipates the same amount of energy as an equivalent DC potential difference."
)

add_item(
    q_ref="9.2.2",
    kind="question",
    marks=5,
    topic="Alternating Current - Calculating Maximum (Peak) Voltage",
    passage=passage_q9_2,
    question="Calculate the maximum (peak) voltage of the AC source.",
    memo=(
        "**OPTION 1:**\n"
        "$$W = \\frac{V_{\\text{rms}}^2 \\Delta t}{R}\\ \\checkmark$$\n"
        "$$500 = \\frac{V_{\\text{rms}}^2 (10)}{200}\\ \\checkmark$$\n"
        "$$V_{\\text{rms}}^2 = \\frac{500 \\times 200}{10} = 10\\ 000 \\implies V_{\\text{rms}} = 100\\text{ V}$$\n\n"
        "$$V_{\\text{rms}} = \\frac{V_{\\text{max}}}{\\sqrt{2}}\\ \\checkmark$$\n"
        "$$100 = \\frac{V_{\\text{max}}}{\\sqrt{2}}\\ \\checkmark$$\n"
        "$$V_{\\text{max}} = 100\\sqrt{2} = 141{,}42\\text{ V}\\ \\checkmark$$\n\n"
        "**OPTION 2 (Average Power):**\n"
        "$$P_{\\text{ave}} = \\frac{W}{\\Delta t} = \\frac{500}{10} = 50\\text{ W}$$\n"
        "$$P_{\\text{ave}} = \\frac{V_{\\text{rms}}^2}{R}\\ \\checkmark \\implies 50 = \\frac{V_{\\text{rms}}^2}{200}\\ \\checkmark \\implies V_{\\text{rms}} = 100\\text{ V}$$\n"
        "$$V_{\\text{rms}} = \\frac{V_{\\text{max}}}{\\sqrt{2}}\\ \\checkmark \\implies 100 = \\frac{V_{\\text{max}}}{\\sqrt{2}}\\ \\checkmark \\implies V_{\\text{max}} = 141{,}42\\text{ V}\\ \\checkmark$$"
    ),
    final_answer="$141{,}42\\text{ V}$"
)

# ==========================================
# QUESTION 10: PHOTOELECTRIC EFFECT
# ==========================================

passage_q10 = (
    "During an experiment, light of different frequencies is radiated onto a silver cathode of a photocell and the corresponding maximum speed of the ejected photoelectrons are measured.\n\n"
    "A graph of the energy of the incident photons ($E$, in $\\times 10^{-19}\\text{ J}$) versus the square of the maximum speed of the ejected photoelectrons ($v_{\\text{max}}^2$, in $\\times 10^{12}\\text{ m}^2\\cdot\\text{s}^{-2}$) is shown below.\n\n"
    "Graph features:\n"
    "- Vertical axis: Energy of photons ($E$, $\\times 10^{-19}\\text{ J}$)\n"
    "- Horizontal axis: Square of maximum speed of photoelectrons ($v_{\\text{max}}^2$, $\\times 10^{12}\\text{ m}^2\\cdot\\text{s}^{-2}$)\n"
    "- A straight line with a constant positive gradient.\n"
    "- Vertical intercept at $v_{\\text{max}}^2 = 0$: $E = 7{,}48 \\times 10^{-19}\\text{ J}$.\n"
    "- Marked point on the line: At $v_{\\text{max}}^2 = X$, $E = 11{,}98 \\times 10^{-19}\\text{ J}$."
)

add_item(
    q_ref="10.1",
    kind="question",
    marks=2,
    topic="Photoelectric Effect - Definition",
    passage=passage_q10,
    question="Define the term photoelectric effect.",
    memo=(
        "The process whereby electrons are ejected from a metal / surface when light (of suitable frequency) is incident on that surface. $\\checkmark\\checkmark$\n\n"
        "*(Marking criteria: -1 mark for each key word/phrase omitted in correct context.)*"
    ),
    final_answer="The process whereby electrons are ejected from a metal surface when light of suitable frequency is incident on that surface."
)

add_item(
    q_ref="10.2",
    kind="question",
    marks=3,
    topic="Photoelectric Effect - Work Function from Graph Intercept",
    passage=passage_q10,
    question="Write down the value of the work function of silver.\n\nUse a relevant equation to justify the answer.",
    memo=(
        "Value: $7{,}48 \\times 10^{-19}\\text{ J}\\ \\checkmark$\n\n"
        "Equation and justification:\n"
        "$$E = W_0 + E_{k(\\text{max})} = W_0 + \\frac{1}{2}mv_{\\text{max}}^2\\ \\checkmark$$\n"
        "When $E_{k(\\text{max})} = 0$ / $v_{\\text{max}}^2 = 0$, $E = W_0$ (i.e. $W_0$ is the y-intercept of the graph). $\\checkmark$"
    ),
    final_answer="$7{,}48 \\times 10^{-19}\\text{ J}$; From E = W_0 + E_k(max), when v_max^2 = 0, E = W_0 (the vertical intercept of the graph)."
)

add_item(
    q_ref="10.3",
    kind="question",
    marks=1,
    topic="Photoelectric Effect - Physical Quantity Determined from Gradient",
    passage=passage_q10,
    question="Which physical quantity can be determined from the gradient of the graph?",
    memo=(
        "Mass (of photo-electron) / $m$ $\\checkmark$\n\n"
        "*ACCEPT:*\n"
        "$\\frac{1}{2}m$ / half the mass of an electron $\\checkmark$\n\n"
        "*(Rationale: Comparing $E = W_0 + \\frac{1}{2}m v_{\\text{max}}^2$ to $y = c + mx$, the gradient equals $\\frac{1}{2}m$, from which the mass of an electron can be determined).* "
    ),
    final_answer="Mass of an electron (or half the mass of an electron)"
)

add_item(
    q_ref="10.4",
    kind="question",
    marks=5,
    topic="Photoelectric Effect - Calculating Unknown Velocity Squared X",
    passage=passage_q10,
    question="Calculate the value of X as shown on the graph.",
    memo=(
        "**POSITIVE MARKING FROM QUESTION 10.2**\n\n"
        "**OPTION 1 (Photoelectric equation):**\n"
        "$$E = W_0 + E_{k(\\text{max})}$$\n"
        "$$E = W_0 + \\frac{1}{2}m v_{\\text{max}}^2$$\n"
        "$$11{,}98 \\times 10^{-19}\\ \\checkmark = 7{,}48 \\times 10^{-19}\\ \\checkmark + \\frac{1}{2}(9{,}11 \\times 10^{-31}) (X \\times 10^{12})\\ \\checkmark$$\n"
        "$$4{,}50 \\times 10^{-19} = 4{,}555 \\times 10^{-19} X$$\n"
        "$$X = 0{,}9879\\ \\checkmark\\ (0{,}99\\text{ or } 0{,}988)$$\n\n"
        "*(Accept: $X = 0{,}9879 \\times 10^{12}\\text{ m}^2\\cdot\\text{s}^{-2}$ or $9{,}88 \\times 10^{11}\\text{ m}^2\\cdot\\text{s}^{-2}$)*\n\n"
        "**OPTION 2 (Gradient method):**\n"
        "$$\\text{Gradient} = \\frac{1}{2}m$$\n"
        "$$\\frac{11{,}98 \\times 10^{-19} - 7{,}48 \\times 10^{-19}}{X \\times 10^{12} - 0}\\ \\checkmark = \\frac{1}{2}(9{,}11 \\times 10^{-31})\\ \\checkmark$$\n"
        "$$X = 0{,}9879\\ \\checkmark\\ (0{,}99)$$\n\n"
        "*(Accept range: $0{,}9868 - 0{,}9879$)*"
    ),
    final_answer="$0{,}99$ (or $0{,}988$)"
)

passage_q10_intensity = passage_q10 + "\n\nThe experiment above is now repeated using light of higher intensity."

add_item(
    q_ref="10.5.1",
    kind="question",
    marks=1,
    topic="Photoelectric Effect - Effect of Intensity on Graph Gradient",
    passage=passage_q10_intensity,
    question="How will the gradient of the graph be affected? Choose from INCREASES, DECREASES or REMAINS THE SAME.",
    memo=(
        "REMAINS THE SAME $\\checkmark$\n\n"
        "*Rationale: The gradient represents $\\frac{1}{2}m$, where $m$ is the mass of an electron, which is a physical constant independent of the intensity of incident light.*"
    ),
    final_answer="REMAINS THE SAME"
)

add_item(
    q_ref="10.5.2",
    kind="question",
    marks=1,
    topic="Photoelectric Effect - Effect of Intensity on Emission Rate",
    passage=passage_q10_intensity,
    question="How will the number of photoelectrons emitted per unit time be affected? Choose from INCREASES, DECREASES or REMAINS THE SAME.",
    memo=(
        "INCREASES $\\checkmark$\n\n"
        "*Rationale: Higher intensity light contains more photons incident per unit time. Each photon with sufficient energy ejects one photoelectron, so more photoelectrons are emitted per unit time.*"
    ),
    final_answer="INCREASES"
)

# ==========================================
# VERIFICATION & OUTPUT
# ==========================================

print(f"Total items created: {len(items)}")
total_marks = sum(item["marks"] for item in items)
print(f"Total marks: {total_marks} (Expected: 150)")
assert total_marks == 150, f"Total marks mismatch: got {total_marks}, expected 150"

# Verify KaTeX balance and decimal commas
def check_katex(text, item_id, field_name):
    # Check balanced single dollars (ignoring escaped dollars)
    # Split by display math $$ first
    parts = text.split("$$")
    for i, p in enumerate(parts):
        # In odd parts (inside $$), should not have single $
        # In even parts, count single $
        single_dollars = re.findall(r'(?<!\\)\$', p)
        if len(single_dollars) % 2 != 0:
            print(f"WARNING: Unbalanced $ in {item_id} [{field_name}]: {p}")
            return False
    # Check for invalid degrees C
    if r"\text{^\circ C}" in text or r"^\circ C" in text or r"^\circ\text{ C}" in text:
        print(f"WARNING: Potential degree C issue in {item_id} [{field_name}]")
    return True

all_valid = True
for it in items:
    for field in ["passage", "question", "memo", "final_answer"]:
        if not check_katex(it[field], it["item_id"], field):
            all_valid = False

if all_valid:
    print("All KaTeX balances verified successfully!")

# Write to both destinations
out_dir1 = "workspace/items/physical_sciences"
os.makedirs(out_dir1, exist_ok=True)
out_file1 = os.path.join(out_dir1, f"{source_id}.jsonl")

out_dir2 = "workspace/items"
os.makedirs(out_dir2, exist_ok=True)
out_file2 = os.path.join(out_dir2, f"{source_id}.jsonl")

with open(out_file1, "w", encoding="utf-8") as f1, open(out_file2, "w", encoding="utf-8") as f2:
    for it in items:
        line = json.dumps(it, ensure_ascii=False)
        f1.write(line + "\n")
        f2.write(line + "\n")

print(f"Successfully written to:\n  - {out_file1}\n  - {out_file2}")
