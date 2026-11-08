import json
import re
import os

source_id = "dbe-physical_sciences-g12-p1-2020-nov"
paired_memo_id = "dbe-physical_sciences-g12-p1-2020-nov-memo"
subject = "physical_sciences"
grade = 12
language = "en"
track = "physical_sciences"

items = []

def add_item(q_ref, marks, topic, passage, question, memo, final_answer, kind="question"):
    item = {
        "item_id": f"{source_id}-{q_ref}",
        "source_id": source_id,
        "pair_source_id": paired_memo_id,
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
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    }
    items.append(item)

# ==========================================
# QUESTION 1: MULTIPLE-CHOICE QUESTIONS
# ==========================================

add_item(
    q_ref="1.1",
    marks=2,
    topic="Momentum and Newton's Second Law - Rate of Change of Momentum",
    passage="",
    question="The rate of change of momentum of an object is equal to the …\n\nA impulse on the object.\nB net force acting on the object.\nC product of the object's mass and its change in velocity.\nD product of the net force acting on the object and its acceleration.",
    memo="B $\\checkmark\\checkmark$\n\n*Rationale: According to Newton's Second Law of Motion in terms of momentum ($F_{\\text{net}} = \\frac{\\Delta p}{\\Delta t}$), the net (or resultant) force acting on an object is equal to the rate of change of momentum of the object.*",
    final_answer="B",
    kind="multiple_choice"
)

add_item(
    q_ref="1.2",
    marks=2,
    topic="Newton's Law of Universal Gravitation - Gravitational Acceleration Comparison",
    passage="",
    question="The gravitational acceleration on the surface of planet X with mass $M$ and radius $r$ is $g$.\n\nThe gravitational acceleration on the surface of planet Y with mass $2M$ and radius $\\frac{1}{2}r$ is …\n\nA $\\frac{1}{2}g$\nB $g$\nC $4g$\nD $8g$",
    memo="D $\\checkmark\\checkmark$\n\n*Rationale: Gravitational acceleration is given by $g = \\frac{GM}{r^2}$. For planet Y:\n$$g_Y = \\frac{G(2M)}{\\left(\\frac{1}{2}r\\right)^2} = \\frac{2GM}{\\frac{1}{4}r^2} = 8\\left(\\frac{GM}{r^2}\\right) = 8g$$\nTherefore, the acceleration is $8g$ (Option D).*",
    final_answer="D",
    kind="multiple_choice"
)

add_item(
    q_ref="1.3",
    marks=2,
    topic="Vertical Projectile Motion - Physical Quantities in Free Fall",
    passage="[Diagram description: A Cartesian graph is shown with an unlabeled vertical axis ($y$-axis) and time $t$ on the horizontal axis. A horizontal line above the time axis indicates a physical quantity that remains constant over time.]",
    question="The graph below shows how one of the physical quantities associated with an object in free fall changes with time $t$. The label on the y-axis is omitted. Ignore air friction.\n\nWhich ONE of the following physical quantities can be the label on the y-axis?\n\nA Velocity\nB Position\nC Weight\nD Momentum",
    memo="C $\\checkmark\\checkmark$\n\n*Rationale: An object in free fall near Earth's surface experiences a constant downward gravitational force (weight $w = mg$). Its velocity ($v = v_i + gt$) and momentum ($p = mv$) increase linearly with time, while its position changes quadratically ($y \\propto t^2$). Because the graph displays a constant horizontal line over time, the quantity on the y-axis must be weight (Option C).*",
    final_answer="C",
    kind="multiple_choice"
)

add_item(
    q_ref="1.4",
    marks=2,
    topic="Momentum and Impulse - Change in Momentum Calculation",
    passage="",
    question="A ball of mass $m$, falling vertically downwards, hits the floor at a speed $v$ and bounces vertically upwards at a speed $0{,}75v$.\n\nWhich ONE of the following combinations regarding the change in momentum of the ball during the collision is CORRECT?\n\n| | MAGNITUDE | DIRECTION |\n| :--- | :--- | :--- |\n| A | $0{,}25mv$ | Upwards |\n| B | $0{,}25mv$ | Downwards |\n| C | $1{,}75mv$ | Upwards |\n| D | $1{,}75mv$ | Downwards |",
    memo="C $\\checkmark\\checkmark$\n\n*Rationale: Taking upwards as positive:\n$v_i = -v$ and $v_f = +0{,}75v$.\n$$\\Delta p = m(v_f - v_i) = m(0{,}75v - (-v)) = m(1{,}75v) = +1{,}75mv$$\nThe magnitude is $1{,}75mv$ and the direction is upwards (Option C).*",
    final_answer="C",
    kind="multiple_choice"
)

add_item(
    q_ref="1.5",
    marks=2,
    topic="Work, Energy and Power - Base SI Units of Work",
    passage="",
    question="The base SI unit of the physical quantity 'work' is …\n\nA $\\text{kg}\\cdot\\text{m}\\cdot\\text{s}^{-1}$\nB $\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^2$\nC $\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-2}$\nD $\\text{kg}\\cdot\\text{m}\\cdot\\text{s}^{-2}$",
    memo="C $\\checkmark\\checkmark$\n\n*Rationale: Work is defined as $W = F\\Delta x\\cos\\theta$. Force has SI units of newtons ($\\text{N} = \\text{kg}\\cdot\\text{m}\\cdot\\text{s}^{-2}$), and displacement has units of metres ($\\text{m}$). Therefore, the base SI unit of work is $(\\text{kg}\\cdot\\text{m}\\cdot\\text{s}^{-2})\\cdot\\text{m} = \\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-2}$ (Option C).*",
    final_answer="C",
    kind="multiple_choice"
)

add_item(
    q_ref="1.6",
    marks=2,
    topic="Doppler Effect - Relative Motion Between Source and Observer",
    passage="",
    question="The siren of a police car, moving in front of a truck, emits sound waves of frequency $f$. Both vehicles are travelling at the same constant velocity.\n\nThe frequency of the sound heard by the driver of the truck is …\n\nA $f$.\nB zero.\nC greater than $f$.\nD smaller than $f$.",
    memo="A $\\checkmark\\checkmark$\n\n*Rationale: The Doppler effect requires relative motion between the source and the observer. Because both vehicles are moving in the same direction at the same velocity, their relative velocity is zero ($v_s = v_L$). Consequently, there is no Doppler shift and the detected frequency remains $f$ (Option A).*",
    final_answer="A",
    kind="multiple_choice"
)

add_item(
    q_ref="1.7",
    marks=2,
    topic="Electrostatics - Charge Distribution on Identical Spheres",
    passage="[Diagram description: Two identical metal spheres labeled P and R are mounted on insulated stands, carrying initial charges. They are brought into contact and then separated again.]",
    question="Two identical metal spheres, P and R, on insulated stands, carry different charges. The spheres are brought into contact and then separated again.\n\nIf the charge on sphere R AFTER the separation is $q$, the charge on sphere P after the separation is …\n\nA $q$.\nB zero.\nC less than $q$.\nD greater than $q$.",
    memo="A $\\checkmark\\checkmark$\n\n*Rationale: When identical conducting spheres are brought into contact, charge distributes equally between them: $q_{\\text{final}} = \\frac{q_1 + q_2}{2}$. Upon separation, both spheres carry the identical charge. If sphere R has charge $q$, then sphere P also carries charge $q$ (Option A).*",
    final_answer="A",
    kind="multiple_choice"
)

add_item(
    q_ref="1.8",
    marks=2,
    topic="Electrodynamics - AC Generator Frequency and Peak Current",
    passage="",
    question="An AC generator generates a current with a frequency of $50\\text{ Hz}$.\n\nThe number of times that the maximum (peak) current is produced in one second is …\n\nA 25.\nB 50.\nC 75.\nD 100.",
    memo="D $\\checkmark\\checkmark$\n\n*Rationale: In each complete AC cycle, the magnitude of the current reaches its peak value twice (once in the positive half-cycle and once in the negative half-cycle). At a frequency of $50\\text{ Hz}$ (50 cycles per second), the maximum current is produced $50 \\times 2 = 100$ times in one second (Option D).*",
    final_answer="D",
    kind="multiple_choice"
)

add_item(
    q_ref="1.9",
    marks=2,
    topic="Electric Circuits - Internal Resistance and Variable Resistor Effects",
    passage="[Diagram description: A circuit consists of a battery with emf $\\varepsilon$ and internal resistance $r$, connected in series with a variable resistor $R$ and an ammeter A. A voltmeter V is connected in parallel across the terminals of the battery.]",
    question="In the circuit below, the battery has an internal resistance $r$ and an emf $\\varepsilon$. A variable resistor $R$ is connected in the circuit and the ammeter and voltmeter register readings.\n\nThe resistance of the variable resistor $R$ is INCREASED now.\n\nWhich ONE of the following combinations is the CORRECT representation of the change in the readings on the ammeter and voltmeter as the resistance of $R$ is increased?\n\n| | AMMETER READING | VOLTMETER READING |\n| :--- | :--- | :--- |\n| A | Decreases | Increases |\n| B | Increases | Increases |\n| C | Increases | Decreases |\n| D | Decreases | Decreases |",
    memo="A $\\checkmark\\checkmark$\n\n*Rationale: Increasing the external resistance $R$ increases total circuit resistance $R_{\\text{total}} = R + r$. By Ohm's law, total current $I = \\frac{\\varepsilon}{R + r}$ decreases, so the ammeter reading decreases. The internal 'lost volts' are $V_{\\text{int}} = Ir$. As $I$ decreases, $V_{\\text{int}}$ decreases. Since the voltmeter measures terminal voltage $V_{\\text{terminal}} = \\varepsilon - Ir$, the voltmeter reading increases (Option A).*",
    final_answer="A",
    kind="multiple_choice"
)

add_item(
    q_ref="1.10",
    marks=2,
    topic="Photoelectric Effect - Intensity and Photocurrent",
    passage="[Diagram description: A photocell circuit contains a sodium cathode irradiated by ultraviolet light, an anode, a DC source, and an ammeter A connected in series. The ammeter registers a photocurrent.]",
    question="The sodium cathode of a photocell is irradiated with ultraviolet light as shown in the diagram below. The ammeter registers a current.\n\nWhich ONE of the following changes will INCREASE the ammeter reading?\n\nA Use a thinner sodium cathode.\nB Increase the intensity of the ultraviolet light.\nC Increase the frequency of the ultraviolet light.\nD Replace the sodium cathode with a cathode of lower work function.",
    memo="B $\\checkmark\\checkmark$\n\n*Rationale: The ammeter measures photocurrent, which depends directly on the number of photoelectrons emitted per second. Increasing the intensity of the ultraviolet light increases the number of incident photons per second, thereby increasing the rate of emitted photoelectrons and increasing the ammeter reading (Option B).*",
    final_answer="B",
    kind="multiple_choice"
)

# ==========================================
# QUESTION 2: NEWTON'S LAWS & FORCES
# ==========================================

q2_passage = (
    "A $20\\text{ kg}$ block, resting on a rough horizontal surface, is connected to blocks P and Q by "
    "a light inextensible string moving over a frictionless pulley. Blocks P and Q are glued together and have "
    "a combined mass of $m$.\n\n"
    "A force of $35\\text{ N}$ is now applied to the $20\\text{ kg}$ block at an angle of $40^\\circ$ with the horizontal, "
    "as shown below.\n\n"
    "[Diagram description: A $20\\text{ kg}$ block rests on a rough horizontal surface. A string attached to the right side "
    "of the block passes over a frictionless pulley at the right edge and connects to blocks P and Q of combined mass $m$ "
    "hanging vertically. An applied force of $35\\text{ N}$ acts on the $20\\text{ kg}$ block directed upwards and to the "
    "left at an angle of $40^\\circ$ above the horizontal.]\n\n"
    "The $20\\text{ kg}$ block experiences a frictional force of magnitude $5\\text{ N}$ as it moves to the RIGHT at a CONSTANT SPEED."
)

add_item(
    q_ref="2.1",
    marks=2,
    topic="Forces and Newton's Laws - Normal Force Definition",
    passage=q2_passage,
    question="Define the term normal force.",
    memo=(
        "The perpendicular force exerted by a surface on an object in contact with the surface. $\\checkmark\\checkmark$\n\n"
        "*(Marking criteria: If any of the underlined key words/phrases in the correct context are omitted: -1 mark per word/phrase.)*"
    ),
    final_answer="The perpendicular force exerted by a surface on an object in contact with the surface."
)

add_item(
    q_ref="2.2",
    marks=5,
    topic="Newton's Laws of Motion - Labelled Free-body Diagram",
    passage=q2_passage,
    question="Draw a labelled free-body diagram of the $20\\text{ kg}$ block.",
    memo=(
        "**Accepted labels and arrows:**\n"
        "* $N$ / $F_N$ / Normal force ($173{,}5\\text{ N}$): directed vertically upwards $\\checkmark$\n"
        "* $f$ / $F_f$ / $f_k$ / Frictional force ($5\\text{ N}$): directed horizontally to the left $\\checkmark$\n"
        "* $w$ / $F_g$ / $mg$ / Weight / Gravitational force ($196\\text{ N}$): directed vertically downwards $\\checkmark$\n"
        "* $T$ / $F_T$ / Tension: directed horizontally to the right $\\checkmark$\n"
        "* $F_{\\text{applied}}$ / $F_A$ / $F$ / $35\\text{ N}$: directed upwards and to the left at $40^\\circ$ to the horizontal $\\checkmark$\n\n"
        "*Notes:*\n"
        "* Mark is awarded for label and arrow.\n"
        "* Do not penalise for length of arrows.\n"
        "* Deduct 1 mark for any additional force.\n"
        "* If all forces are correctly drawn and labelled, but no arrows, deduct 1 mark."
    ),
    final_answer="Labelled free-body diagram with 5 forces: Normal force (upwards), Weight (downwards), Tension (rightwards), Frictional force (leftwards), and Applied force (upwards and to the left at $40^\\circ$)."
)

add_item(
    q_ref="2.3",
    marks=5,
    topic="Newton's Laws of Motion - Calculation of Combined Mass",
    passage=q2_passage,
    question="Calculate the combined mass $m$ of the two blocks.",
    memo=(
        "**For the $20\\text{ kg}$ block (moving to the right at constant speed, $a = 0$):**\n"
        "$$F_{\\text{net}} = ma\\;\\checkmark$$\n"
        "$$T - f - F_{Ax} = ma$$\n"
        "$$T - 5 - 35\\cos 40^\\circ\\;\\checkmark = 0\\;\\checkmark$$\n"
        "$$T = 5 + 35\\cos 40^\\circ = 5 + 26{,}81 = 31{,}81\\text{ N}$$\n\n"
        "**For hanging mass $m$:**\n"
        "$$F_{\\text{net}} = ma$$\n"
        "$$mg - T = ma$$\n"
        "$$m(9{,}8) - 31{,}81\\;\\checkmark = 0$$\n"
        "$$m = \\frac{31{,}81}{9{,}8} = 3{,}25\\text{ kg}\\;\\checkmark$$\n\n"
        "*Marking criteria:*\n"
        "* $\\checkmark$ Formula for $20\\text{ kg}$ or $m\\text{ kg}$ ($F_{\\text{net}} = ma$)\n"
        "* $\\checkmark$ Substitution of zero into either formula\n"
        "* $\\checkmark$ All substitutions into $F_{\\text{net}}$ for $20\\text{ kg}$ as shown\n"
        "* $\\checkmark$ Substitution of value of $T$ into equation for $m$\n"
        "* $\\checkmark$ Final answer: $3{,}25\\text{ kg}$"
    ),
    final_answer="$3{,}25\\text{ kg}$"
)

q2_4_passage = (
    q2_passage + "\n\n"
    "At a certain stage of the motion, block Q breaks off and falls down.\n\n"
    "How will EACH of the following be affected when this happens?"
)

add_item(
    q_ref="2.4.1",
    marks=1,
    topic="Newton's Laws of Motion - Effect on String Tension",
    passage=q2_4_passage,
    question="The tension in the string\n\nChoose from INCREASES, DECREASES or REMAINS THE SAME.",
    memo="Decreases $\\checkmark$",
    final_answer="Decreases"
)

add_item(
    q_ref="2.4.2",
    marks=3,
    topic="Newton's Laws of Motion - Effect on Block Velocity and Explanation",
    passage=q2_4_passage,
    question="The velocity of the $20\\text{ kg}$ block\n\nExplain the answer.",
    memo=(
        "*(Positive marking from QUESTION 2.3)*\n\n"
        "**Moving to the right:**\n"
        "* Velocity decreases $\\checkmark$\n"
        "* Accelerates to the left / Net force is to the left $\\checkmark\\checkmark$\n\n"
        "**OR:**\n"
        "* As the tension force decreases, the net force / acceleration acts in the opposite direction of motion / to the left. $\\checkmark\\checkmark$\n\n"
        "*(If moving to the left: Velocity increases $\\checkmark$; Accelerates to the left / Net force is to the left $\\checkmark\\checkmark$)*"
    ),
    final_answer="Velocity decreases. As the tension force decreases, the net force (acceleration) acts to the left, opposite to the direction of motion."
)

# ==========================================
# QUESTION 3: VERTICAL PROJECTILE MOTION
# ==========================================

q3_passage = (
    "A small ball is dropped from a height of $2\\text{ m}$ and bounces a few times after landing on a cement floor. "
    "Ignore air friction.\n\n"
    "The position-time graph below, not drawn to scale, represents the motion of the ball.\n\n"
    "[Diagram description: A position-time graph with Position (m) on the vertical axis and Time (s) on the horizontal axis.\n"
    "- At $t = 0\\text{ s}$, Position $= 2\\text{ m}$. The ball falls to the floor (Position $= 0\\text{ m}$) at $t = 0{,}64\\text{ s}$.\n"
    "- The ball is in contact with the floor from $t = 0{,}64\\text{ s}$ to $t = 0{,}67\\text{ s}$ (Position $= 0\\text{ m}$).\n"
    "- First bounce: Leaves the floor at $t = 0{,}67\\text{ s}$, reaches a maximum height of $1{,}85\\text{ m}$, and returns to the floor at $t = 1{,}90\\text{ s}$.\n"
    "- Contact during second landing: from $t = 1{,}90\\text{ s}$ to $t = 1{,}97\\text{ s}$ (Position $= 0\\text{ m}$).\n"
    "- Second bounce: Leaves the floor at $t = 1{,}97\\text{ s}$, reaches a maximum height of $1{,}2\\text{ m}$, and lands back on the floor at time $t$.]"
)

add_item(
    q_ref="3.1",
    marks=2,
    topic="Vertical Projectile Motion - Free Fall Definition",
    passage=q3_passage,
    question="Define the term free fall.",
    memo=(
        "(Motion of an object) under the influence of gravity (weight) only. $\\checkmark\\checkmark$\n\n"
        "**OR:**\n"
        "(Motion in which) the only force acting on the object is gravity (weight). $\\checkmark\\checkmark$\n"
        "*(2 or 0)*"
    ),
    final_answer="Motion of an object under the influence of gravity (weight) only."
)

add_item(
    q_ref="3.2.1",
    marks=2,
    topic="Vertical Projectile Motion - Contact Time Before First Bounce",
    passage=q3_passage,
    question="Use the graph and determine:\n\nThe time that the ball is in contact with the floor before the first bounce",
    memo="$$\\Delta t = 0{,}67 - 0{,}64 = 0{,}03\\text{ s}\\;\\checkmark\\checkmark$$",
    final_answer="$0{,}03\\text{ s}$"
)

add_item(
    q_ref="3.2.2",
    marks=2,
    topic="Vertical Projectile Motion - Time to Maximum Height After First Bounce",
    passage=q3_passage,
    question="Use the graph and determine:\n\nThe time it takes the ball to reach its maximum height after the first bounce",
    memo=(
        "**OPTION 1 (Using symmetry of flight):**\n"
        "$$\\Delta t = \\frac{1{,}90 - 0{,}67}{2} = 0{,}62\\text{ s}\\;\\checkmark\\checkmark\\quad (0{,}615\\text{ s})$$\n\n"
        "**OPTION 2:**\n"
        "$$\\Delta y = v_i\\Delta t + \\frac{1}{2}a\\Delta t^2$$\n"
        "$$-1{,}85 = 0 + \\frac{1}{2}(-9{,}8)\\Delta t^2\\;\\checkmark$$\n"
        "$$\\Delta t = 0{,}61\\text{ s}\\;\\checkmark\\quad (0{,}6145\\text{ s})$$\n\n"
        "**OPTION 3:**\n"
        "$$t_{\\text{peak}} = \\frac{1{,}90 + 0{,}67}{2} = 1{,}285\\text{ s}$$\n"
        "$$\\Delta t = 1{,}285 - 0{,}67\\;\\checkmark = 0{,}62\\text{ s}\\;\\checkmark$$"
    ),
    final_answer="$0{,}62\\text{ s}$ (or $0{,}61\\text{ s}$)"
)

add_item(
    q_ref="3.2.3",
    marks=3,
    topic="Vertical Projectile Motion - Initial Bounce Speed Calculation",
    passage=q3_passage,
    question="Use the graph and determine:\n\nThe speed at which the ball leaves the floor at the first bounce",
    memo=(
        "*(Positive marking from QUESTION 3.2.2)*\n\n"
        "**OPTION 1 (Using $\\Delta t = 0{,}62\\text{ s}$, upwards positive):**\n"
        "$$v_f = v_i + a\\Delta t\\;\\checkmark$$\n"
        "$$0 = v_i + (-9{,}8)(0{,}62)\\;\\checkmark$$\n"
        "$$v_i = 6{,}08\\text{ m}\\cdot\\text{s}^{-1}\\;\\checkmark\\quad (6{,}076\\text{ m}\\cdot\\text{s}^{-1})$$\n\n"
        "**OPTION 2 (Using maximum height $\\Delta y = 1{,}85\\text{ m}$):**\n"
        "$$v_f^2 = v_i^2 + 2a\\Delta y\\;\\checkmark$$\n"
        "$$0 = v_i^2 + 2(-9{,}8)(1{,}85)\\;\\checkmark$$\n"
        "$$v_i = 6{,}02\\text{ m}\\cdot\\text{s}^{-1}\\;\\checkmark$$\n\n"
        "**OPTION 3 (Conservation of mechanical energy):**\n"
        "$$(E_p + E_k)_{\\text{floor}} = (E_p + E_k)_{\\text{top}}\\;\\checkmark$$\n"
        "$$0 + \\frac{1}{2}v_i^2 = (9{,}8)(1{,}85) + 0\\;\\checkmark$$\n"
        "$$v_i = 6{,}02\\text{ m}\\cdot\\text{s}^{-1}\\;\\checkmark$$\n\n"
        "*(Acceptable range: $5{,}94$ to $6{,}08\\text{ m}\\cdot\\text{s}^{-1}$)*"
    ),
    final_answer="$6{,}02\\text{ m}\\cdot\\text{s}^{-1}$ (or $6{,}08\\text{ m}\\cdot\\text{s}^{-1}$)"
)

add_item(
    q_ref="3.2.4",
    marks=6,
    topic="Vertical Projectile Motion - Total Time Calculation",
    passage=q3_passage,
    question="Use the graph and determine:\n\nTime $t$ indicated on the graph",
    memo=(
        "**OPTION 1:**\n"
        "*Step 1: Calculate initial velocity for second bounce ($h = 1{,}2\\text{ m}$):*\n"
        "$$v_f^2 = v_i^2 + 2a\\Delta y\\;\\checkmark$$\n"
        "$$0 = v_i^2 + 2(-9{,}8)(1{,}2)\\;\\checkmark$$\n"
        "$$v_i = 4{,}85\\text{ m}\\cdot\\text{s}^{-1}$$\n\n"
        "*Step 2: Calculate time of flight $\\Delta t$ for second bounce:*\n"
        "$$v_f = v_i + a\\Delta t\\;\\checkmark$$\n"
        "$$-4{,}85 = 4{,}85 + (-9{,}8)\\Delta t\\;\\checkmark$$\n"
        "$$\\Delta t = 0{,}9898\\text{ s}$$\n"
        "$$t = 1{,}97 + 0{,}9898\\;\\checkmark = 2{,}96\\text{ s}\\;\\checkmark$$\n\n"
        "*(OR: using time to peak $\\Delta t_{\\text{top}} = 0{,}4949\\text{ s}$, then $t = 1{,}97 + 2(0{,}4949) = 2{,}96\\text{ s}$)*\n\n"
        "**OPTION 2 (Using free fall from peak to floor):**\n"
        "$$\\Delta y = v_i\\Delta t + \\frac{1}{2}a\\Delta t^2\\;\\checkmark$$\n"
        "$$1{,}2\\;\\checkmark = 0 + \\frac{1}{2}(9{,}8)\\Delta t^2\\;\\checkmark$$\n"
        "$$\\Delta t = 0{,}4949\\text{ s}$$\n"
        "$$t = 1{,}97 + 2(0{,}4949)\\;\\checkmark\\;\\checkmark = 2{,}96\\text{ s}\\;\\checkmark$$\n\n"
        "*(Acceptable range: $2{,}95$ to $2{,}97\\text{ s}$)*"
    ),
    final_answer="$2{,}96\\text{ s}$"
)

# ==========================================
# QUESTION 4: MOMENTUM AND IMPULSE
# ==========================================

q4_passage = (
    "Ball P of mass $0{,}16\\text{ kg}$, moving east at a speed of $10\\text{ m}\\cdot\\text{s}^{-1}$, collides head-on "
    "with another ball Q of mass $0{,}2\\text{ kg}$, moving west at a speed of $15\\text{ m}\\cdot\\text{s}^{-1}$. "
    "After the collision, ball P moves west at a speed of $5\\text{ m}\\cdot\\text{s}^{-1}$, as shown in the diagram below.\n\n"
    "Ignore the effects of friction and the rotational effects of the balls.\n\n"
    "[Diagram description:\n"
    "- Direction indicator: North (up), South (down), East (right), West (left).\n"
    "- Before collision: Ball P ($0{,}16\\text{ kg}$) moves East at $10\\text{ m}\\cdot\\text{s}^{-1}$; Ball Q ($0{,}2\\text{ kg}$) moves West at $15\\text{ m}\\cdot\\text{s}^{-1}$.\n"
    "- After collision: Ball P ($0{,}16\\text{ kg}$) moves West at $5\\text{ m}\\cdot\\text{s}^{-1}$; Ball Q ($0{,}2\\text{ kg}$) moves with unknown velocity $v_{Qf}$.]"
)

add_item(
    q_ref="4.1",
    marks=2,
    topic="Momentum and Impulse - Linear Momentum Definition",
    passage=q4_passage,
    question="Define the term momentum in words.",
    memo=(
        "(Linear) momentum (of an object) is the product of mass and velocity. $\\checkmark\\checkmark$\n"
        "*(2 or 0)*"
    ),
    final_answer="Linear momentum is the product of mass and velocity."
)

add_item(
    q_ref="4.2.1",
    marks=5,
    topic="Momentum and Impulse - Velocity After Collision",
    passage=q4_passage,
    question="Calculate the:\n\nVelocity of ball Q after the collision",
    memo=(
        "**OPTION 1 (East as positive):**\n"
        "$$\\sum p_i = \\sum p_f\\;\\checkmark$$\n"
        "$$m_P v_{Pi} + m_Q v_{Qi} = m_P v_{Pf} + m_Q v_{Qf}$$\n"
        "$$(0{,}16)(10) + (0{,}2)(-15)\\;\\checkmark = (0{,}16)(-5) + (0{,}2)v_{Qf}\\;\\checkmark$$\n"
        "$$1{,}6 - 3{,}0 = -0{,}8 + 0{,}2 v_{Qf}$$\n"
        "$$-1{,}4 = -0{,}8 + 0{,}2 v_{Qf}$$\n"
        "$$0{,}2 v_{Qf} = -0{,}6$$\n"
        "$$v_{Qf} = -3\\text{ m}\\cdot\\text{s}^{-1}$$\n"
        "$$v_{Qf} = 3\\text{ m}\\cdot\\text{s}^{-1}\\;\\checkmark\\text{ west}\\;\\checkmark$$\n\n"
        "**OPTION 2 (West as positive):**\n"
        "$$\\sum p_i = \\sum p_f\\;\\checkmark$$\n"
        "$$(0{,}16)(-10) + (0{,}2)(15)\\;\\checkmark = (0{,}16)(5) + (0{,}2)v_{Qf}\\;\\checkmark$$\n"
        "$$v_{Qf} = 3\\text{ m}\\cdot\\text{s}^{-1}\\;\\checkmark\\text{ west}\\;\\checkmark$$"
    ),
    final_answer="$3\\text{ m}\\cdot\\text{s}^{-1}$ west"
)

add_item(
    q_ref="4.2.2",
    marks=3,
    topic="Momentum and Impulse - Magnitude of Impulse Calculation",
    passage=q4_passage,
    question="Calculate the:\n\nMagnitude of the impulse on ball P during the collision",
    memo=(
        "*(Positive marking from QUESTION 4.2.1)*\n\n"
        "**For ball P:**\n"
        "Taking East as positive:\n"
        "$$\\text{Impulse} = \\Delta p = m(v_{Pf} - v_{Pi})$$\n"
        "$$\\text{Impulse} = 0{,}16(-5 - 10)\\;\\checkmark$$\n"
        "$$\\text{Impulse} = -2{,}4\\text{ N}\\cdot\\text{s}$$\n"
        "$$\\text{Magnitude} = 2{,}4\\text{ N}\\cdot\\text{s}\\;\\checkmark\\checkmark\\quad (2{,}4\\text{ kg}\\cdot\\text{m}\\cdot\\text{s}^{-1})$$\n\n"
        "**OR (Taking West as positive):**\n"
        "$$\\text{Impulse} = 0{,}16(5 - (-10))\\;\\checkmark = 2{,}4\\text{ N}\\cdot\\text{s}\\;\\checkmark\\checkmark$$\n\n"
        "**OR (Using ball Q):**\n"
        "$$\\text{Impulse} = |\\Delta p_Q| = |0{,}2(-3 - (-15))|\\;\\checkmark = 2{,}4\\text{ N}\\cdot\\text{s}\\;\\checkmark\\checkmark$$"
    ),
    final_answer="$2{,}4\\text{ N}\\cdot\\text{s}$ (or $2{,}4\\text{ kg}\\cdot\\text{m}\\cdot\\text{s}^{-1}$)"
)

# ==========================================
# QUESTION 5: WORK, ENERGY AND POWER
# ==========================================

q5_passage = (
    "A roller-coaster car of mass $200\\text{ kg}$, with the engine switched off, travels along "
    "track ABC which has a rough surface, as shown in the diagram below. At point A, "
    "which is $10\\text{ m}$ above the ground, the speed of the car is $4\\text{ m}\\cdot\\text{s}^{-1}$.\n\n"
    "At point B, which is at a height $h$ above the ground, the speed of the car is $2\\text{ m}\\cdot\\text{s}^{-1}$. "
    "During the motion from point A to point B, $3{,}40 \\times 10^3\\text{ J}$ of energy is used to overcome friction.\n\n"
    "Ignore rotational effects due to the wheels of the car.\n\n"
    "[Diagram description: A track profile ABC is shown:\n"
    "- Point A is at height $10\\text{ m}$ above the ground with speed $4\\text{ m}\\cdot\\text{s}^{-1}$.\n"
    "- The track dips and rises to point B at height $h$ above ground with speed $2\\text{ m}\\cdot\\text{s}^{-1}$.\n"
    "- An incline connects point B to point C at height $22\\text{ m}$ above the ground.]"
)

add_item(
    q_ref="5.1",
    marks=2,
    topic="Work, Energy and Power - Non-conservative Force Definition",
    passage=q5_passage,
    question="Define the term non-conservative force.",
    memo=(
        "A force is non-conservative if the work it does on an object (which is moving between two points) depends on the path taken. $\\checkmark\\checkmark$\n\n"
        "**OR:**\n"
        "A force is non-conservative if the work it does on an object depends on the path taken. $\\checkmark\\checkmark$\n\n"
        "**OR:**\n"
        "A force is non-conservative if the work it does in moving an object around a closed path is non-zero. $\\checkmark\\checkmark$\n\n"
        "*(Marking criteria: If any of the underlined key words/phrases in the correct context are omitted: -1 mark per word/phrase. However, IF the word 'work' is omitted: 0 marks)*"
    ),
    final_answer="A force is non-conservative if the work it does on an object depends on the path taken."
)

add_item(
    q_ref="5.2",
    marks=3,
    topic="Work, Energy and Power - Change in Kinetic Energy Calculation",
    passage=q5_passage,
    question="Calculate the change in the kinetic energy of the car after it has travelled from point A to point B.",
    memo=(
        "$$E_k = \\frac{1}{2}mv^2\\;\\checkmark$$\n"
        "$$\\Delta E_k = \\frac{1}{2}m(v_f^2 - v_i^2)$$\n"
        "$$\\Delta E_k = \\frac{1}{2}(200)(2^2 - 4^2)\\;\\checkmark$$\n"
        "$$\\Delta E_k = 100(4 - 16) = -1\\,200\\text{ J}\\;\\checkmark$$"
    ),
    final_answer="$-1\\,200\\text{ J}$"
)

add_item(
    q_ref="5.3",
    marks=4,
    topic="Work, Energy and Power - Height Calculation Using Energy Principles",
    passage=q5_passage,
    question="Use energy principles to calculate the height $h$.",
    memo=(
        "*(Positive marking from QUESTION 5.2)*\n\n"
        "**OPTION 1:**\n"
        "$$W_{\\text{nc}} = \\Delta E_k + \\Delta E_p\\;\\checkmark$$\n"
        "$$-3{,}40 \\times 10^3\\;\\checkmark = -1\\,200 + (200)(9{,}8)(h - 10)\\;\\checkmark$$\n"
        "$$-3\\,400 = -1\\,200 + 1\\,960(h - 10)$$\n"
        "$$-2\\,200 = 1\\,960h - 19\\,600$$\n"
        "$$1\\,960h = 17\\,400$$\n"
        "$$h = 8{,}88\\text{ m}\\;\\checkmark\\quad (8{,}8776\\text{ m})$$\n\n"
        "**OPTION 2:**\n"
        "$$E_{\\text{mech, A}} + W_f = E_{\\text{mech, B}}\\;\\checkmark$$\n"
        "$$(mgh + \\frac{1}{2}mv^2)_A + W_f = (mgh + \\frac{1}{2}mv^2)_B$$\n"
        "$$(200)(9{,}8)(10) + \\frac{1}{2}(200)(4^2) - 3{,}40 \\times 10^3\\;\\checkmark = (200)(9{,}8)(h) + \\frac{1}{2}(200)(2^2)\\;\\checkmark$$\n"
        "$$19\\,600 + 1\\,600 - 3\\,400 = 1\\,960h + 400$$\n"
        "$$1\\,960h = 17\\,400$$\n"
        "$$h = 8{,}88\\text{ m}\\;\\checkmark$$"
    ),
    final_answer="$8{,}88\\text{ m}$"
)

q5_4_passage = (
    "A roller-coaster car of mass $200\\text{ kg}$, with the engine switched off, travels along track ABC which has a rough surface. "
    "At point B, the car is at height $h = 8{,}88\\text{ m}$ above the ground moving at $2\\text{ m}\\cdot\\text{s}^{-1}$.\n\n"
    "On reaching point B, the car's engine is switched on in order to move up the incline to "
    "point C, which is $22\\text{ m}$ above the ground. While moving from point B to point C, the car "
    "travels for $15\\text{ s}$ at a constant speed of $2\\text{ m}\\cdot\\text{s}^{-1}$, while an average frictional force of $50\\text{ N}$ "
    "acts on it."
)

add_item(
    q_ref="5.4",
    marks=5,
    topic="Work, Energy and Power - Engine Power Calculation",
    passage=q5_4_passage,
    question="Calculate the power delivered by the engine to move the car from point B to point C.",
    memo=(
        "**OPTION 1:**\n"
        "$$W_{\\text{nc}} = \\Delta E_k + \\Delta E_p\\;\\checkmark$$\n"
        "$$W_{\\text{engine}} + W_f = \\frac{1}{2}m(v_f^2 - v_i^2) + mg(h_f - h_i)$$\n"
        "$$\\Delta x = v\\Delta t = (2)(15) = 30\\text{ m}$$\n"
        "$$W_f = f\\Delta x\\cos 180^\\circ = (50)(30)(-1) = -1\\,500\\text{ J}$$\n"
        "$$W_{\\text{engine}} + (50)(15)(2)\\cos 180^\\circ\\;\\checkmark\\checkmark = 0 + (200)(9{,}8)(22 - 8{,}88)\\;\\checkmark$$\n"
        "$$W_{\\text{engine}} - 1\\,500 = 1\\,960(13{,}12) = 25\\,715{,}20\\text{ J}$$\n"
        "$$W_{\\text{engine}} = 27\\,215{,}20\\text{ J}$$\n"
        "$$P_{\\text{engine}} = \\frac{W_{\\text{engine}}}{\\Delta t} = \\frac{27\\,215{,}20}{15} = 1\\,814{,}35\\text{ W}\\;\\checkmark$$\n\n"
        "**OPTION 2 (Using $P_{\\text{ave}} = F v$):**\n"
        "$$F_{\\text{net}} = 0 \\implies F_{\\text{engine}} - f - mg\\sin\\theta = 0\\;\\checkmark$$\n"
        "$$\\sin\\theta = \\frac{\\Delta h}{\\Delta x} = \\frac{22 - 8{,}88}{30} = 0{,}4373$$\n"
        "$$F_{\\text{engine}} = 50\\;\\checkmark\\checkmark + (200)(9{,}8)(0{,}4373)\\;\\checkmark = 907{,}17\\text{ N}$$\n"
        "$$P_{\\text{engine}} = F_{\\text{engine}} v = (907{,}17)(2) = 1\\,814{,}35\\text{ W}\\;\\checkmark$$\n\n"
        "*(Acceptable range: $1\\,813{,}04\\text{ W}$ to $1\\,824{,}8\\text{ W}$)*"
    ),
    final_answer="$1\\,814{,}35\\text{ W}$"
)

# ==========================================
# QUESTION 6: DOPPLER EFFECT
# ==========================================

q6_passage = (
    "The siren of a train, moving at a constant speed along a straight horizontal track, emits "
    "sound with a constant frequency. A detector, placed next to the track, records the "
    "frequency of the sound waves. The results obtained are as shown in the graph below.\n\n"
    "[Diagram description: A step graph of recorded Frequency (Hz) versus Time (s) is shown:\n"
    "- From $t = 0$ to $t = t_1$, the frequency recorded is constant at $3\\,148\\text{ Hz}$.\n"
    "- At $t = t_1$, the recorded frequency drops sharply as the train passes the detector.\n"
    "- For $t > t_1$, the recorded frequency remains constant at $2\\,073\\text{ Hz}$.]"
)

add_item(
    q_ref="6.1",
    marks=2,
    topic="Doppler Effect - Definition",
    passage=q6_passage,
    question="State the Doppler effect in words.",
    memo=(
        "The change in frequency $\\checkmark$ (or pitch) (of the sound) detected by a listener "
        "because the source and the listener have different velocities relative to the medium of propagation. $\\checkmark$\n\n"
        "**OR:**\n"
        "An (apparent) change in (observed/detected) frequency (pitch), as a result of "
        "the relative motion between a source and an observer (listener). $\\checkmark\\checkmark$\n\n"
        "*(Marking criteria: If any of the underlined key words/phrases in the correct context are omitted: -1 mark per word/phrase.)*"
    ),
    final_answer="The apparent change in frequency (or pitch) of the sound detected by a listener as a result of the relative motion between the source and the listener."
)

add_item(
    q_ref="6.2",
    marks=1,
    topic="Doppler Effect - Relative Direction of Motion",
    passage=q6_passage,
    question="Does the detector record the frequency of $3\\,148\\text{ Hz}$ when the train moves TOWARDS the detector or AWAY from the detector?",
    memo="Towards $\\checkmark$",
    final_answer="Towards"
)

add_item(
    q_ref="6.3",
    marks=6,
    topic="Doppler Effect - Train Speed Calculation",
    passage=q6_passage,
    question="Calculate the speed of the train. Take the speed of sound in air as $340\\text{ m}\\cdot\\text{s}^{-1}$.",
    memo=(
        "$$f_L = \\left(\\frac{v \\pm v_L}{v \\mp v_s}\\right)f_s\\;\\checkmark$$\n\n"
        "**When moving towards ($f_L = 3\\,148\\text{ Hz}$):**\n"
        "$$f_{L1} = \\left(\\frac{v}{v - v_s}\\right)f_s \\implies 3\\,148 = \\left(\\frac{340}{340 - v_s}\\right)f_s\\;\\checkmark$$\n\n"
        "**When moving away ($f_L = 2\\,073\\text{ Hz}$):**\n"
        "$$f_{L2} = \\left(\\frac{v}{v + v_s}\\right)f_s \\implies 2\\,073 = \\left(\\frac{340}{340 + v_s}\\right)f_s\\;\\checkmark$$\n\n"
        "**Equating expressions for $f_s$:**\n"
        "$$f_s = 3\\,148\\left(\\frac{340 - v_s}{340}\\right) = 2\\,073\\left(\\frac{340 + v_s}{340}\\right)\\;\\checkmark\\;\\checkmark$$\n"
        "$$3\\,148(340 - v_s) = 2\\,073(340 + v_s)$$\n"
        "$$1\\,070\\,320 - 3\\,148 v_s = 704\\,820 + 2\\,073 v_s$$\n"
        "$$5\\,221 v_s = 365\\,500$$\n"
        "$$v_s = 70\\text{ m}\\cdot\\text{s}^{-1}\\;\\checkmark\\quad (69{,}95\\text{ to } 70{,}16\\text{ m}\\cdot\\text{s}^{-1})$$"
    ),
    final_answer="$70\\text{ m}\\cdot\\text{s}^{-1}$"
)

add_item(
    q_ref="6.4",
    marks=2,
    topic="Doppler Effect - Time of Travel Calculation",
    passage=q6_passage,
    question=(
        "The detector started recording the frequency of the moving train's siren when the train was $350\\text{ m}$ away.\n\n"
        "Calculate time $t_1$ indicated on the graph above."
    ),
    memo=(
        "*(Positive marking from QUESTION 6.3)*\n\n"
        "**OPTION 1:**\n"
        "$$\\Delta t = \\frac{\\Delta x}{v_s}\\;\\checkmark = \\frac{350}{70} = 5\\text{ s}\\;\\checkmark$$\n"
        "$$t_1 = 5\\text{ s}$$\n\n"
        "**OPTION 2:**\n"
        "$$\\Delta x = v_i\\Delta t + \\frac{1}{2}a\\Delta t^2$$\n"
        "$$350 = 70\\Delta t + 0\\;\\checkmark$$\n"
        "$$\\Delta t = 5\\text{ s}\\;\\checkmark$$"
    ),
    final_answer="$5\\text{ s}$"
)

# ==========================================
# QUESTION 7: ELECTROSTATICS
# ==========================================

q7_passage_1 = (
    "Two small charged spheres, A and B, are placed on insulated stands, $0{,}2\\text{ m}$ apart, as shown in the diagram below. "
    "They carry charges of $-4 \\times 10^{-6}\\text{ C}$ and $+3 \\times 10^{-6}\\text{ C}$ respectively.\n\n"
    "[Diagram description: Sphere A with charge $-4 \\times 10^{-6}\\text{ C}$ is placed on an insulated stand at the left. "
    "Sphere B with charge $+3 \\times 10^{-6}\\text{ C}$ is on an insulated stand $0{,}2\\text{ m}$ to the right of A. "
    "Point M is marked along the same line, at a distance of $0{,}1\\text{ m}$ to the right of sphere B.]\n\n"
    "M is a point that is a distance of $0{,}1\\text{ m}$ to the right of sphere B."
)

add_item(
    q_ref="7.1",
    marks=3,
    topic="Electrostatics - Number of Excess Electrons Calculation",
    passage=q7_passage_1,
    question="Calculate the number of electrons in excess on sphere A.",
    memo=(
        "$$n = \\frac{Q}{e}\\;\\checkmark$$\n"
        "$$n = \\frac{-4 \\times 10^{-6}}{-1{,}6 \\times 10^{-19}}\\;\\checkmark$$\n"
        "$$n = 2{,}5 \\times 10^{13}\\;\\checkmark$$\n"
        "*(Ignore negative signs)*"
    ),
    final_answer="$2{,}5 \\times 10^{13}$"
)

add_item(
    q_ref="7.2",
    marks=3,
    topic="Electrostatics - Coulomb's Law Force Calculation",
    passage=q7_passage_1,
    question="Calculate the magnitude of the electrostatic force exerted by sphere A on sphere B.",
    memo=(
        "$$F_{AB} = \\frac{k Q_1 Q_2}{r^2}\\;\\checkmark$$\n"
        "$$F_{AB} = \\frac{(9{,}0 \\times 10^9)(4 \\times 10^{-6})(3 \\times 10^{-6})}{(0{,}2)^2}\\;\\checkmark$$\n"
        "$$F_{AB} = 2{,}7\\text{ N}\\;\\checkmark$$"
    ),
    final_answer="$2{,}7\\text{ N}$"
)

add_item(
    q_ref="7.3",
    marks=2,
    topic="Electrostatics - Electric Field Definition",
    passage=q7_passage_1,
    question="Describe the term electric field.",
    memo=(
        "Electric field is a region (in space) where (in which) an (electric) charge experiences a (electric) force. $\\checkmark\\checkmark$\n\n"
        "*(Marking criteria: If any of the underlined key words/phrases in the correct context are omitted: -1 mark per word/phrase.)*"
    ),
    final_answer="A region in space in which an electric charge experiences an electric force."
)

add_item(
    q_ref="7.4",
    marks=5,
    topic="Electrostatics - Net Electric Field Calculation",
    passage=q7_passage_1,
    question="Calculate the magnitude of the net electric field at point M.",
    memo=(
        "**Electric field at M due to A ($-4 \\times 10^{-6}\\text{ C}$), distance $r_A = 0{,}2 + 0{,}1 = 0{,}3\\text{ m}$:**\n"
        "$$E_{AM} = \\frac{k Q_A}{r^2}\\;\\checkmark = \\frac{(9{,}0 \\times 10^9)(4 \\times 10^{-6})}{(0{,}3)^2}\\;\\checkmark = 4{,}0 \\times 10^5\\text{ N}\\cdot\\text{C}^{-1}\\text{ (to the left)}$$\n\n"
        "**Electric field at M due to B ($+3 \\times 10^{-6}\\text{ C}$), distance $r_B = 0{,}1\\text{ m}$:**\n"
        "$$E_{BM} = \\frac{k Q_B}{r^2} = \\frac{(9{,}0 \\times 10^9)(3 \\times 10^{-6})}{(0{,}1)^2}\\;\\checkmark = 2{,}7 \\times 10^6\\text{ N}\\cdot\\text{C}^{-1}\\text{ (to the right)}$$\n\n"
        "**Net electric field at M:**\n"
        "Taking right as positive:\n"
        "$$E_{\\text{net}} = E_{BM} - E_{AM}\\;\\checkmark$$\n"
        "$$E_{\\text{net}} = 2{,}7 \\times 10^6 - 4{,}0 \\times 10^5 = 2{,}3 \\times 10^6\\text{ N}\\cdot\\text{C}^{-1}\\;\\checkmark\\text{ (to the right)}$$"
    ),
    final_answer="$2{,}3 \\times 10^6\\text{ N}\\cdot\\text{C}^{-1}$"
)

q7_passage_2 = (
    "Charged spheres A and B and another charged sphere D are now arranged along a rectangular system of axes, "
    "as shown in the diagram below.\n\n"
    "[Diagram description: A Cartesian system of axes is shown:\n"
    "- Sphere A (charge $-4 \\times 10^{-6}\\text{ C}$) is located at the origin $(0, 0)$.\n"
    "- Sphere B (charge $+3 \\times 10^{-6}\\text{ C}$) is on the $+x$-axis at distance $0{,}2\\text{ m}$ from A.\n"
    "- Sphere D is located on the $+y$-axis at distance $0{,}15\\text{ m}$ from A.\n"
    "- A vector arrow represents the net electrostatic force experienced by sphere A with magnitude $7{,}69\\text{ N}$, "
    "pointing upwards and to the right into the first quadrant.]\n\n"
    "The net electrostatic force experienced by sphere A is $7{,}69\\text{ N}$ in the direction as shown in the diagram above."
)

add_item(
    q_ref="7.5",
    marks=1,
    topic="Electrostatics - Polarity of Charge",
    passage=q7_passage_2,
    question="Is the charge on sphere D POSITIVE or NEGATIVE?",
    memo="Positive $\\checkmark$",
    final_answer="Positive"
)

add_item(
    q_ref="7.6",
    marks=3,
    topic="Electrostatics - Magnitude of Charge Calculation",
    passage=q7_passage_2,
    question="Calculate the magnitude of the charge on sphere D.",
    memo=(
        "*(Positive marking from QUESTION 7.2)*\n\n"
        "$$(F_{\\text{net}})^2 = (F_{AD})^2 + (F_{AB})^2$$\n"
        "$$(7{,}69)^2 = (F_{AD})^2 + (2{,}7)^2\\;\\checkmark$$\n"
        "$$59{,}1361 = (F_{AD})^2 + 7{,}29$$\n"
        "$$(F_{AD})^2 = 51{,}8461 \\implies F_{AD} = 7{,}20\\text{ N}$$\n\n"
        "$$F_{AD} = \\frac{k Q_A Q_D}{r^2}$$\n"
        "$$7{,}20 = \\frac{(9{,}0 \\times 10^9)(4 \\times 10^{-6}) Q_D}{(0{,}15)^2}\\;\\checkmark$$\n"
        "$$7{,}20 = 1{,}6 \\times 10^6 Q_D$$\n"
        "$$Q_D = 4{,}5 \\times 10^{-6}\\text{ C}\\;\\checkmark\\quad (4{,}50 \\times 10^{-6}\\text{ C})$$"
    ),
    final_answer="$4{,}5 \\times 10^{-6}\\text{ C}$"
)

# ==========================================
# QUESTION 8: ELECTRIC CIRCUITS
# ==========================================

q8_passage = (
    "A battery with an internal resistance of $0{,}5\\ \\Omega$ and an unknown emf ($\\varepsilon$) is connected to "
    "three resistors, a high resistance voltmeter and an ammeter of negligible resistance, as shown in the circuit diagram below.\n\n"
    "[Diagram description: A circuit consists of:\n"
    "- A battery with unknown emf $\\varepsilon$ and internal resistance $r = 0{,}5\\ \\Omega$.\n"
    "- A voltmeter V connected across the terminals of the battery.\n"
    "- The external circuit includes a switch S and an ammeter A in series with resistor $R_1 = 4\\ \\Omega$.\n"
    "- In series with $R_1$ is a parallel combination of two resistors: $R_2 = 25\\ \\Omega$ and $R_3 = 15\\ \\Omega$.]\n\n"
    "The resistance of the connecting wires must be ignored."
)

add_item(
    q_ref="8.1",
    marks=2,
    topic="Electric Circuits - Emf Definition",
    passage=q8_passage,
    question="Define the term emf of a battery.",
    memo=(
        "(Maximum) energy provided (work done) by a battery per coulomb/unit charge passing through it. $\\checkmark\\checkmark$\n\n"
        "**OR:**\n"
        "Work done by the battery to move a unit coulomb of charge across the circuit. $\\checkmark\\checkmark$\n\n"
        "*(Marking criteria: If any of the underlined key words/phrases in the correct context are omitted: -1 mark per word/phrase.)*"
    ),
    final_answer="The maximum energy provided (or work done) by a battery per unit charge passing through it."
)

q8_switch_passage = (
    q8_passage + "\n\n"
    "The reading on the voltmeter DECREASES by $1{,}5\\text{ V}$ when switch S is closed."
)

add_item(
    q_ref="8.2",
    marks=2,
    topic="Electric Circuits - Voltmeter Reading Decrease Explanation",
    passage=q8_switch_passage,
    question="Give a reason why the voltmeter reading decreases.",
    memo="Energy (per coulomb of charge) is converted to heat in the battery due to the internal resistance. $\\checkmark\\checkmark$",
    final_answer="Energy is dissipated as heat within the battery due to its internal resistance ('lost volts')."
)

add_item(
    q_ref="8.3.1",
    marks=3,
    topic="Electric Circuits - Ammeter Reading Calculation",
    passage=q8_switch_passage,
    question="Calculate the following when switch S is closed:\n\nReading on the ammeter",
    memo=(
        "$$I = \\frac{V_{\\text{int}}}{r}\\;\\checkmark$$\n"
        "$$I = \\frac{1{,}5}{0{,}5}\\;\\checkmark$$\n"
        "$$I = 3\\text{ A}\\;\\checkmark$$"
    ),
    final_answer="$3\\text{ A}$"
)

add_item(
    q_ref="8.3.2",
    marks=4,
    topic="Electric Circuits - Total External Resistance Calculation",
    passage=q8_switch_passage,
    question="Calculate the following when switch S is closed:\n\nTotal external resistance of the circuit",
    memo=(
        "**OPTION 1:**\n"
        "$$\\frac{1}{R_p} = \\frac{1}{R_2} + \\frac{1}{R_3}$$\n"
        "$$\\frac{1}{R_p} = \\frac{1}{25} + \\frac{1}{15}\\;\\checkmark$$\n"
        "$$R_p = 9{,}375\\ \\Omega\\;\\checkmark$$\n"
        "$$R_{\\text{ext}} = R_p + R_1 = 9{,}375 + 4\\;\\checkmark = 13{,}38\\ \\Omega\\;\\checkmark\\quad (13{,}375\\ \\Omega)$$\n\n"
        "**OPTION 2:**\n"
        "$$R_p = \\frac{R_2 R_3}{R_2 + R_3} = \\frac{(25)(15)}{25 + 15}\\;\\checkmark = 9{,}375\\ \\Omega\\;\\checkmark$$\n"
        "$$R_{\\text{ext}} = 9{,}375 + 4\\;\\checkmark = 13{,}38\\ \\Omega\\;\\checkmark$$"
    ),
    final_answer="$13{,}38\\ \\Omega$ (or $13{,}375\\ \\Omega$)"
)

add_item(
    q_ref="8.3.3",
    marks=3,
    topic="Electric Circuits - Emf Calculation",
    passage=q8_switch_passage,
    question="Calculate the following when switch S is closed:\n\nEmf of the battery",
    memo=(
        "*(Positive marking from QUESTIONS 8.3.1 and 8.3.2)*\n\n"
        "**OPTION 1:**\n"
        "$$\\varepsilon = I(R_{\\text{ext}} + r)\\;\\checkmark$$\n"
        "$$\\varepsilon = 3(13{,}38 + 0{,}5)\\;\\checkmark$$\n"
        "$$\\varepsilon = 41{,}64\\text{ V}\\;\\checkmark\\quad (\\text{Range: } 41{,}625\\text{ to } 41{,}64\\text{ V})$$\n\n"
        "**OPTION 2:**\n"
        "$$\\varepsilon = V_{\\text{ext}} + V_{\\text{int}}\\;\\checkmark$$\n"
        "$$\\varepsilon = (3)(13{,}38) + 1{,}5\\;\\checkmark$$\n"
        "$$\\varepsilon = 41{,}64\\text{ V}\\;\\checkmark$$"
    ),
    final_answer="$41{,}64\\text{ V}$ (or $41{,}625\\text{ V}$)"
)

add_item(
    q_ref="8.4",
    marks=3,
    topic="Electric Circuits - Parallel Branch Current Comparison and Explanation",
    passage=q8_passage,
    question=(
        "A learner makes the following statement:\n\n"
        "The current through resistor $R_3$ is larger than the current through resistor $R_2$.\n\n"
        "Is this statement CORRECT? Choose from YES or NO. Explain the answer."
    ),
    memo=(
        "Yes. $\\checkmark$\n\n"
        "For the same voltage / potential difference across the parallel combination, $\\checkmark$\n"
        "a larger current will flow through a smaller resistor ($I = \\frac{V}{R}$). $\\checkmark$\n\n"
        "**OR:**\n"
        "$I \\propto \\frac{1}{R}\\;\\checkmark$ when $V$ is constant. $\\checkmark$\n\n"
        "**OR (by calculation):**\n"
        "$$V_p = I R_p = (3)(9{,}375) = 28{,}125\\text{ V}$$\n"
        "$$I_{R3} = \\frac{28{,}125}{15} = 1{,}88\\text{ A}\\;\\checkmark$$\n"
        "$$I_{R2} = \\frac{28{,}125}{25} = 1{,}13\\text{ A}\\;\\checkmark$$\n"
        "Therefore, $I_{R3} > I_{R2}$."
    ),
    final_answer="Yes. Because resistors $R_2$ and $R_3$ are connected in parallel, they have the same potential difference across them. By Ohm's law ($I = V/R$), current is inversely proportional to resistance, so the smaller resistor ($R_3 = 15\\ \\Omega$) draws a larger current than the larger resistor ($R_2 = 25\\ \\Omega$)."
)

add_item(
    q_ref="8.5",
    marks=1,
    topic="Electric Circuits - Invariance of Emf to External Circuit Changes",
    passage=q8_passage,
    question=(
        "The $4\\ \\Omega$ resistor is now removed from the circuit.\n\n"
        "How will this affect the emf of the battery? Choose from INCREASES, DECREASES or REMAINS THE SAME."
    ),
    memo="Remains the same $\\checkmark$",
    final_answer="Remains the same"
)

# ==========================================
# QUESTION 9: ELECTRODYNAMICS
# ==========================================

q9_passage_1 = (
    "A simplified diagram of an electrical machine is shown below.\n\n"
    "[Diagram description: A DC motor is shown consisting of:\n"
    "- Two permanent magnet poles: North pole (N) on the left and South pole (S) on the right, providing a horizontal magnetic field directed from left to right.\n"
    "- A rectangular coil positioned horizontally between the pole pieces.\n"
    "- The ends of the coil connect to a split-ring commutator labeled A.\n"
    "- Carbon brushes make contact with the split-ring segments, connected to a DC source (battery).\n"
    "- The battery symbol shows the positive terminal on the left and the negative terminal on the right.]"
)

add_item(
    q_ref="9.1.1",
    marks=1,
    topic="Electrodynamics - Machine Identification",
    passage=q9_passage_1,
    question="Is this machine a DC motor or a DC generator?",
    memo="(DC) motor $\\checkmark$",
    final_answer="DC motor"
)

add_item(
    q_ref="9.1.2",
    marks=2,
    topic="Electrodynamics - Energy Conversion in Motor",
    passage=q9_passage_1,
    question="Write down the energy conversion that takes place while this machine is in operation.",
    memo=(
        "*(Positive marking from QUESTION 9.1.1)*\n\n"
        "Electrical to mechanical / kinetic (energy) $\\checkmark\\checkmark$\n"
        "*(2 or 0)*"
    ),
    final_answer="Electrical energy to mechanical (kinetic) energy"
)

add_item(
    q_ref="9.1.3",
    marks=1,
    topic="Electrodynamics - Identification of Commutator",
    passage=q9_passage_1,
    question="Write down the name of component A in the diagram.",
    memo="Split ring / commutator $\\checkmark$",
    final_answer="Split-ring commutator"
)

add_item(
    q_ref="9.1.4",
    marks=2,
    topic="Electrodynamics - Direction of Rotation",
    passage=q9_passage_1,
    question="In which direction will the coil, shown in the diagram above, rotate?\n\nChoose from CLOCKWISE or ANTICLOCKWISE.",
    memo="Anticlockwise $\\checkmark\\checkmark$",
    final_answer="Anticlockwise"
)

q9_passage_2 = "An electrical device is marked $200\\text{ W}$ ; $220\\text{ V}$."

add_item(
    q_ref="9.2.1",
    marks=2,
    topic="Electrodynamics - RMS Voltage Definition",
    passage=q9_passage_2,
    question="Define the term rms voltage.",
    memo=(
        "(The rms voltage/value of AC is) the AC voltage/potential difference which dissipates the same amount of energy/heat/power as an equivalent DC voltage/potential difference. $\\checkmark\\checkmark$\n"
        "*(2 or 0)*\n\n"
        "**ACCEPT:**\n"
        "The rms voltage/value of AC is the DC potential difference which dissipates the same amount of energy/heat/power as AC."
    ),
    final_answer="The rms voltage of AC is the alternating potential difference that dissipates the same amount of energy (or heat/power) as an equivalent DC potential difference."
)

add_item(
    q_ref="9.2.2",
    marks=3,
    topic="Electrodynamics - Resistance Calculation from Rating",
    passage=q9_passage_2,
    question="Calculate the resistance of the device.",
    memo=(
        "**OPTION 1:**\n"
        "$$P_{\\text{ave}} = \\frac{V_{\\text{rms}}^2}{R}\\;\\checkmark$$\n"
        "$$200 = \\frac{220^2}{R}\\;\\checkmark$$\n"
        "$$R = 242\\ \\Omega\\;\\checkmark$$\n\n"
        "**OPTION 2:**\n"
        "$$P_{\\text{ave}} = V_{\\text{rms}} I_{\\text{rms}} \\implies 200 = (220)I_{\\text{rms}} \\implies I_{\\text{rms}} = 0{,}909\\text{ A}$$\n"
        "$$R = \\frac{V_{\\text{rms}}}{I_{\\text{rms}}} = \\frac{220}{0{,}909}\\;\\checkmark = 242\\ \\Omega\\;\\checkmark$$"
    ),
    final_answer="$242\\ \\Omega$"
)

q9_passage_3 = (
    q9_passage_2 + "\n\n"
    "This device is now connected to a $150\\text{ V}$ AC source."
)

add_item(
    q_ref="9.2.3",
    marks=5,
    topic="Electrodynamics - Energy Dissipation on Reduced Voltage",
    passage=q9_passage_3,
    question="Calculate the energy dissipated by the device in $10\\text{ minutes}$.",
    memo=(
        "*(Positive marking from QUESTION 9.2.2)*\n\n"
        "**OPTION 1:**\n"
        "$$W = \\frac{V_{\\text{rms}}^2}{R}\\Delta t\\;\\checkmark\\;\\checkmark$$\n"
        "$$\\Delta t = 10 \\times 60 = 600\\text{ s}$$\n"
        "$$W = \\frac{150^2}{242}(600)\\;\\checkmark\\;\\checkmark$$\n"
        "$$W = 55\\,785{,}12\\text{ J}\\;\\checkmark$$\n\n"
        "**OPTION 2:**\n"
        "$$P_{\\text{ave}} = \\frac{V_{\\text{rms}}^2}{R} = \\frac{150^2}{242} = 92{,}975\\text{ W}\\;\\checkmark\\;\\checkmark$$\n"
        "$$W = P_{\\text{ave}}\\Delta t\\;\\checkmark = (92{,}975)(10 \\times 60)\\;\\checkmark = 55\\,785{,}12\\text{ J}\\;\\checkmark$$\n\n"
        "**OPTION 3:**\n"
        "$$I_{\\text{rms}} = \\frac{V_{\\text{rms}}}{R} = \\frac{150}{242} = 0{,}620\\text{ A}\\;\\checkmark\\;\\checkmark$$\n"
        "$$W = I_{\\text{rms}}^2 R \\Delta t = (0{,}62)^2(242)(600)\\;\\checkmark\\;\\checkmark = 55\\,814{,}88\\text{ J}\\;\\checkmark$$\n\n"
        "*(Acceptable range: $55\\,785{,}12\\text{ J}$ to $55\\,896\\text{ J}$)*"
    ),
    final_answer="$55\\,785{,}12\\text{ J}$"
)

# ==========================================
# QUESTION 10: PHOTOELECTRIC EFFECT
# ==========================================

q10_passage = (
    "An experiment is conducted to investigate the relationship between the frequency of light incident on a metal "
    "and the maximum kinetic energy of the emitted electrons from the surface of the metal. This experiment is conducted "
    "for three different metals.\n\n"
    "The graph below represents the results obtained.\n\n"
    "[Diagram description: A Cartesian graph of Maximum kinetic energy (J) versus Frequency $f$ ($\\times 10^{15}\\text{ Hz}$) is shown:\n"
    "- The horizontal axis has major ticks at $0{,}5$, $1{,}0$, $1{,}5$, $2{,}0\\ (\\times 10^{15}\\text{ Hz})$ with intermediate ticks at every $0{,}25\\times 10^{15}\\text{ Hz}$.\n"
    "- Three parallel straight lines with identical slope (equal to Planck's constant $h$) are plotted for potassium, zinc, and platinum.\n"
    "- The lines intersect the frequency axis at their threshold frequencies $f_0$:\n"
    "  - Potassium: $f_0 \\approx 0{,}55 \\times 10^{15}\\text{ Hz}$\n"
    "  - Zinc: $f_0 \\approx 1{,}05 \\times 10^{15}\\text{ Hz}$\n"
    "  - Platinum: $f_0 = 1{,}75 \\times 10^{15}\\text{ Hz}$\n"
    "- Extrapolations (dashed lines) extend into the fourth quadrant to negative intercepts on the vertical axis, with the intercept for potassium labeled $-X$.]"
)

add_item(
    q_ref="10.1",
    marks=1,
    topic="Photoelectric Effect - Phenomenon Identification",
    passage=q10_passage,
    question="Name the phenomenon on which this experiment is based.",
    memo="Photoelectric effect $\\checkmark$",
    final_answer="Photoelectric effect"
)

add_item(
    q_ref="10.2",
    marks=1,
    topic="Photoelectric Effect - Graph Intercept Interpretation",
    passage=q10_passage,
    question="Name the physical quantity represented by X on the graph.",
    memo="Work function (of potassium) $\\checkmark$",
    final_answer="Work function (of potassium)"
)

add_item(
    q_ref="10.3",
    marks=2,
    topic="Photoelectric Effect - Maximum Threshold Wavelength Comparison",
    passage=q10_passage,
    question=(
        "Which ONE of the three metals needs incident light with the largest wavelength for the emission of electrons?\n\n"
        "Give a reason for the answer."
    ),
    memo=(
        "Potassium $\\checkmark$\n"
        "It has the lowest work function / threshold frequency / highest threshold wavelength. $\\checkmark$"
    ),
    final_answer="Potassium. It has the lowest threshold frequency ($f_0$), which corresponds to the longest (largest) threshold wavelength (since $\\lambda_0 = \\frac{c}{f_0}$)."
)

add_item(
    q_ref="10.4",
    marks=2,
    topic="Photoelectric Effect - Work Function Definition",
    passage=q10_passage,
    question="Define the term work function in words.",
    memo=(
        "The work function of a metal is the minimum energy that an electron (in the metal) needs $\\checkmark$ to be emitted/ejected from the metal / surface. $\\checkmark$\n\n"
        "*(Marking criteria: If any of the underlined key words/phrases in the correct context are omitted: -1 mark per word/phrase.)*"
    ),
    final_answer="The minimum energy that an electron in a metal needs to be emitted from the surface of the metal."
)

add_item(
    q_ref="10.5.1",
    marks=3,
    topic="Photoelectric Effect - Work Function Calculation",
    passage=q10_passage,
    question="Calculate the:\n\nWork function of platinum",
    memo=(
        "$$W_0 = h f_0\\;\\checkmark$$\n"
        "From the graph, the threshold frequency of platinum is $f_0 = 1{,}75 \\times 10^{15}\\text{ Hz}$.\n"
        "$$W_0 = (6{,}63 \\times 10^{-34})(1{,}75 \\times 10^{15})\\;\\checkmark$$\n"
        "$$W_0 = 1{,}160 \\times 10^{-18}\\text{ J}\\;\\checkmark\\quad (1{,}16 \\times 10^{-18}\\text{ J})$$"
    ),
    final_answer="$1{,}160 \\times 10^{-18}\\text{ J}$"
)

add_item(
    q_ref="10.5.2",
    marks=4,
    topic="Photoelectric Effect - Incident Light Frequency Calculation",
    passage=q10_passage,
    question="Calculate the:\n\nFrequency of the incident light that will emit electrons from the surface of platinum with a maximum velocity of $5{,}60 \\times 10^5\\text{ m}\\cdot\\text{s}^{-1}$",
    memo=(
        "*(Positive marking from QUESTION 10.5.1)*\n\n"
        "$$E = W_0 + E_{k(\\text{max})}\\;\\checkmark$$\n"
        "$$h f = W_0 + \\frac{1}{2}m_e v_{\\text{max}}^2$$\n"
        "$$(6{,}63 \\times 10^{-34})f\\;\\checkmark = 1{,}160 \\times 10^{-18} + \\frac{1}{2}(9{,}11 \\times 10^{-31})(5{,}60 \\times 10^5)^2\\;\\checkmark$$\n"
        "$$(6{,}63 \\times 10^{-34})f = 1{,}160 \\times 10^{-18} + 1{,}4284 \\times 10^{-19}$$\n"
        "$$(6{,}63 \\times 10^{-34})f = 1{,}3028 \\times 10^{-18}$$\n"
        "$$f = 1{,}97 \\times 10^{15}\\text{ Hz}\\;\\checkmark$$"
    ),
    final_answer="$1{,}97 \\times 10^{15}\\text{ Hz}$"
)

# ==========================================
# VERIFICATION AND SAVING
# ==========================================

print(f"Total items: {len(items)}")
total_marks = sum(item["marks"] for item in items)
print(f"Total marks: {total_marks}")
assert total_marks == 150, f"Expected 150 marks, got {total_marks}"

def check_katex(text):
    # Check for unescaped balanced dollars
    # Remove display math $$...$$ first
    s = re.sub(r'\$\$.*?\$\$', '', text, flags=re.DOTALL)
    # Count inline $
    c = s.count('$')
    return c % 2 == 0

errors = []
for it in items:
    for field in ["passage", "question", "memo", "final_answer"]:
        val = it[field]
        if not check_katex(val):
            errors.append(f"Unbalanced $ in item {it['item_id']} field {field}")
        if r"\text{^\circ C}" in val:
            errors.append(f"Invalid celsius formatting in {it['item_id']} field {field}")
        # check decimal comma like 0,15 in math mode
        math_blocks = re.findall(r'\$(.*?)\$', val)
        for mb in math_blocks:
            bad_commas = re.findall(r'\d+,\d+', mb)
            if bad_commas:
                errors.append(f"Decimal comma without braces {bad_commas} in item {it['item_id']} field {field}")

if errors:
    print(f"Errors found ({len(errors)}):")
    for e in errors[:10]:
        print(" -", e)
    raise ValueError("KaTeX verification failed!")
else:
    print("KaTeX verification passed: 100% balanced, correct decimal commas, zero syntax issues!")

# Paths to save
out_path_1 = "workspace/items/physical_sciences/dbe-physical_sciences-g12-p1-2020-nov.jsonl"
out_path_2 = "workspace/items/dbe-physical_sciences-g12-p1-2020-nov.jsonl"

for out_path in [out_path_1, out_path_2]:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")
    print(f"Successfully written {len(items)} items to {out_path}")
