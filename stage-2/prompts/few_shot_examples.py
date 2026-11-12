"""
stage-2/prompts/few_shot_examples.py - High-quality few-shot exemplars for Stage 2 generation.

Format:
  - Dialogue: Socratic diagnostic questions, student replies without reflexive praise.
  - Final Turn:
    * Math/Science:
        Final Answer
        📖 Formula Breakdown (How It Works)
          • The Formula
          • What the letters mean
          • Why we use it
        🎯 Exam Tip
    * Language (English & Afrikaans):
        Model Answer
        📖 Concept & Thought Process (How to Understand It)
          • The Rule / Concept
          • The Thought Process (How to analyze it step-by-step)
          • How DBE Markers Score It
        🎯 Exam Tip
"""

# ── 1. MATHEMATICS (Deep-Dive Mode: 3-4 turns) ─────────────────────────────
MATH_EXEMPLAR = r"""{
  "messages": [
    {"role": "user", "content": "I need help with this question: Solve for x: 2x² + 5x − 3 = 0 (4 marks)"},
    {"role": "assistant", "reasoning": "The learner has a quadratic equation with a leading coefficient of 2. Let me start by checking if they can identify the type of equation and the method to use. [TOOL CHECK: calculator(expression=\"discriminant = 5**2 - 4*2*(-3)\") -> 49]", "content": "Let's work through this together step by step! 🙂\n\nFirst, take a look at the equation: $2x^2 + 5x - 3 = 0$. What type of equation is this, and what method do you usually use to solve it?"},
    {"role": "user", "content": "its a quadratic equation. i usually try factorising but the 2 in front makes it hard so maybe the formula?"},
    {"role": "assistant", "reasoning": "Great diagnosis by student. They identified it as quadratic and correctly recognized that the formula avoids tricky factorisation with a leading 2. Let me provide the formula and ask for a, b, c. [TOOL CHECK: calculator(expression=\"(-5 + 7) / (2*2)\") -> 0.5]", "content": "Using the quadratic formula is a great choice here — especially when the number in front of $x^2$ isn't 1! 💪\n\nThe quadratic formula is:\n$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$$\n\nLooking at $2x^2 + 5x - 3 = 0$, what are the values of $a$, $b$, and $c$?"},
    {"role": "user", "content": "a = 2, b = 5, and c = -3"},
    {"role": "assistant", "reasoning": "Correct values. Let me guide them to substitute and calculate the discriminant first. [TOOL CHECK: calculator(expression=\"(-5 - 7) / (2*2)\") -> -3.0]", "content": "Spot on values! Now let's substitute them into the formula:\n$$x = \\frac{-(5) \\pm \\sqrt{(5)^2 - 4(2)(-3)}}{2(2)}$$\n\nCan you calculate what is inside the square root first? That part under the root ($b^2 - 4ac$) is called the **discriminant**."},
    {"role": "user", "content": "5 squared is 25, and -4 * 2 * -3 is +24, so 25 + 24 = 49. and sqrt of 49 is 7"},
    {"role": "assistant", "reasoning": "Correct calculation. Now finalize both roots: x = (-5+7)/4 = 2/4 = 1/2, or x = (-5-7)/4 = -12/4 = -3. Provide clean final answer, formula breakdown, and exam tip.", "content": "Excellent calculation! Since $\\sqrt{49} = 7$, we split into two answers:\n$$x = \\frac{-5 + 7}{4} = \\frac{2}{4} = \\frac{1}{2} \\quad \\text{or} \\quad x = \\frac{-5 - 7}{4} = \\frac{-12}{4} = -3$$\n\n**Final Answer:** $x = \\frac{1}{2}$ or $x = -3$\n\n---\n### 📖 Formula Breakdown (How It Works):\n* **The Formula:** $x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$\n* **What the letters mean:**\n  * $a$ is the number in front of $x^2$ (here: $2$)\n  * $b$ is the number in front of $x$ (here: $5$)\n  * $c$ is the constant number at the end (here: $-3$)\n* **Why we use it:** It works for **any** quadratic equation. The $\\pm$ symbol gives us two separate answers because squaring either a positive or negative number equals the discriminant ($49$).\n\n🎯 **Exam Tip:** Always write out $a$, $b$, and $c$ first. In the DBE exam, you earn 1 mark just for showing the correct numbers substituted inside the formula brackets before calculating!"}
  ],
  "meta": {
    "strategy_used": "step_walkthrough",
    "final_answer": "x = 1/2 or x = -3",
    "verify_code": "import sympy as sp\nx = sp.Symbol('x')\nsol = sp.solve(2*x**2 + 5*x - 3, x)\nprint(f\"x = {sol[0]} or x = {sol[1]}\")",
    "techniques": ["polya_four_steps", "given_formula_substitute_answer", "check_by_substitution"]
  }
}"""

# ── 2. MATHEMATICS SHORT MODE (Quick / Fast-Track Mode: 2 turns) ────────────
MATH_SHORT_EXEMPLAR = r"""{
  "messages": [
    {"role": "user", "content": "How do I find the gradient of the line passing through A(2, 3) and B(6, 11)? (2 marks)"},
    {"role": "assistant", "reasoning": "Student needs gradient between two points. Fast-track mode: ask for the formula and substitution in one go. [TOOL CHECK: calculator(expression=\"(11 - 3) / (6 - 2)\") -> 2.0]", "content": "To find the gradient ($m$) between two coordinate points, we use the gradient formula:\n$$m = \\frac{y_2 - y_1}{x_2 - x_1}$$\n\nUsing $A(2, 3)$ as $(x_1, y_1)$ and $B(6, 11)$ as $(x_2, y_2)$, what do you get when you substitute the coordinates?"},
    {"role": "user", "content": "m = (11 - 3) / (6 - 2) = 8 / 4 = 2"},
    {"role": "assistant", "reasoning": "Correct substitution and calculation. Finalize with clear answer, formula breakdown, and exam tip.", "content": "That is completely correct! ✅\n$$m = \\frac{11 - 3}{6 - 2} = \\frac{8}{4} = 2$$\n\n**Final Answer:** Gradient $m = 2$\n\n---\n### 📖 Formula Breakdown (How It Works):\n* **The Formula:** $m = \\frac{y_2 - y_1}{x_2 - x_1}$\n* **What the letters mean:**\n  * $y_2 - y_1$ is the vertical change (rise: $11 - 3 = 8$)\n  * $x_2 - x_1$ is the horizontal change (run: $6 - 2 = 4$)\n  * $m$ is the gradient (steepness of the line)\n* **Why we use it:** Gradient measures steepness. $\\frac{8}{4} = 2$ tells us that for every 1 step right along the x-axis, the line climbs 2 steps up on the y-axis.\n\n🎯 **Exam Tip:** Watch out for negative numbers! If a coordinate is negative, use brackets: $y_2 - (-y_1) = y_2 + y_1$."}
  ],
  "meta": {
    "strategy_used": "exam_technique",
    "final_answer": "m = 2",
    "verify_code": "import sympy as sp\nm = (11 - 3) / (6 - 2)\nprint(f\"m = {int(m)}\")",
    "techniques": ["given_formula_substitute_answer", "check_by_substitution"]
  }
}"""

# ── 3. PHYSICAL SCIENCES (Deep-Dive Mode with Formula Breakdown) ────────────
SCIENCE_EXEMPLAR = r"""{
  "messages": [
    {"role": "user", "content": "A 5 kg block slides down a frictionless incline at 30° to the horizontal. Calculate the acceleration of the block down the slope. (3 marks)"},
    {"role": "assistant", "reasoning": "Inclined plane mechanics problem. Weight component parallel to slope is mg sin(theta). Frictionless, so F_net = F_gx = mg sin(theta). a = g sin(theta). [TOOL CHECK: calculator(expression=\"9.8 * sin(radians(30))\") -> 4.9]", "content": "Let's break down the forces acting on this incline! 🔬\n\nWhen an object is placed on a slope at angle $\\theta$, gravity ($F_g = mg$) pulls straight down. Which component of gravity pulls the block **parallel down the slope** — is it $mg\\sin\\theta$ or $mg\\cos\\theta$?"},
    {"role": "user", "content": "is it mg sin theta? cos theta is the one into the surface right?"},
    {"role": "assistant", "reasoning": "Correct force component resolution. Now guide them to apply Newton's second law F_net = ma and calculate. [TOOL CHECK: calculator(expression=\"9.8 * 0.5\") -> 4.9]", "content": "Yes, that's exactly right! $mg\\cos\\theta$ pushes into the surface (balancing the normal force), while $mg\\sin\\theta$ pulls down the incline. ✅\n\nSince the surface is frictionless, the only force acting along the slope is $F_{gx} = mg\\sin\\theta$.\nUsing Newton's Second Law ($F_{net} = ma$):\n$$mg\\sin\\theta = ma$$\n\nNotice that mass ($m$) appears on both sides. Can you simplify and calculate the acceleration using $g = 9{,}8\\text{ m}\\cdot\\text{s}^{-2}$?"},
    {"role": "user", "content": "the mass cancels out! so a = g * sin(30) = 9.8 * 0.5 = 4.9 m/s^2"},
    {"role": "assistant", "reasoning": "Correct calculation and units. Finalize with complete vector answer, formula breakdown, and exam tip.", "content": "Yes! The mass cancels out entirely! 🎉\n$$a = g\\sin\\theta = 9{,}8 \\times \\sin 30^\\circ = 9{,}8 \\times 0{,}5 = 4{,}9\\text{ m}\\cdot\\text{s}^{-2}$$\n\n**Final Answer:** $a = 4{,}9\\text{ m}\\cdot\\text{s}^{-2}$ down the incline\n\n---\n### 📖 Formula Breakdown (How It Works):\n* **The Formula:** $a = g\\sin\\theta$ (derived from $F_{net} = ma$, where $F_{net} = mg\\sin\\theta$)\n* **What the letters mean:**\n  * $a$ is acceleration along the slope (in $\\text{m}\\cdot\\text{s}^{-2}$)\n  * $g$ is gravitational acceleration ($9{,}8\\text{ m}\\cdot\\text{s}^{-2}$ on Earth)\n  * $\\theta$ is the angle of the incline to the horizontal ($30^\\circ$)\n* **Why we use it:** Gravity pulls straight down, but the surface supports part of the block's weight. Only the component along the slope ($mg\\sin\\theta$) accelerates the block. Because there is no friction, mass cancels out!\n\n🎯 **Exam Tip:** Always state the direction (\"down the incline\")! Acceleration is a vector quantity, and in DBE exams, omitting direction loses the final accuracy mark."}
  ],
  "meta": {
    "strategy_used": "concept_map",
    "final_answer": "4,9 m·s⁻² down the incline",
    "verify_code": "import sympy as sp\ng = sp.Rational(98, 10)\ntheta = sp.pi / 6\na = g * sp.sin(theta)\nprint(f\"{float(a):.1f}\".replace('.', ','))",
    "techniques": ["concept_map", "units_check", "given_formula_substitute_answer"]
  }
}"""

# ── 4. AFRIKAANS WISKUNDE (Met eenvoudige Formule-verduideliking) ────────────
AFRIKAANS_MATH_EXEMPLAR = r"""{
  "messages": [
    {"role": "user", "content": "Ek het hulp nodig met hierdie vraag: Los op vir x: 3x + 7 = 22 (2 punte)"},
    {"role": "assistant", "reasoning": "Lineêre vergelyking. Eenvoudige tweestap-algebra. Laat die student die eerste inverse bewerking identifiseer. [TOOL CHECK: calculator(expression=\"(22 - 7) / 3\") -> 5.0]", "content": "Kom ons los dit saam stap vir stap op! 🙂\n\nOns doelwit is om $x$ heeltemal alleen aan die linkerkant te kry. Wat is die eerste stap — watter getal moet ons eerste wegruim, en watter bewerking doen ons?"},
    {"role": "user", "content": "ons moet die +7 wegruim. trek 7 af aan albei kante?"},
    {"role": "assistant", "reasoning": "Korrek. 3x = 15. Laat hulle nou deel deur 3 om x te vind.", "content": "Presies reg! Ons doen die teenoorgestelde van $+7$, wat $-7$ is:\n$$3x + 7 - 7 = 22 - 7$$\n$$3x = 15$$\n\nNou het ons $3x = 15$. Hoe kry ons $x$ nou heeltemal alleen?"},
    {"role": "user", "content": "deel deur 3 aan albei kante. 15 / 3 = 5 so x = 5"},
    {"role": "assistant", "reasoning": "Korrekte oplossing. Gee finale antwoord, eenvoudige reël-uiteensetting, en eksamenwenk.", "content": "Uitstekend gedoen! 🎉\n$$x = \\frac{15}{3} = 5$$\n\n**Finale Antwoord:** $x = 5$\n\n---\n### 📖 Formule & Reël-Uiteensetting (Hoe dit werk):\n* **Die Reël:** Om 'n lineêre vergelyking op te los, gebruik ons **inverse (teenoorgestelde) bewerkings** in omgekeerde volgorde.\n* **Wat die stappe beteken:**\n  * Ons kanselleer $+7$ uit deur $7$ af te trek ($22 - 7 = 15$).\n  * Ons kanselleer vermenigvuldiging met $3$ uit deur deur $3$ te deel ($15 \\div 3 = 5$).\n* **Waarom ons dit gebruik:** 'n Vergelyking is soos 'n weegskaal. Wat jy aan die linkerkant van die gelykheidsteken ($=$) doen, moet jy presies dieselfde aan die regterkant doen sodat dit gebalanseerd bly!\n\n🎯 **Eksamen-wenk:** Toets altyd jou antwoord deur dit terug te sit in die oorspronklike som: $3(5) + 7 = 15 + 7 = 22$ ✅"}
  ],
  "meta": {
    "strategy_used": "step_walkthrough",
    "final_answer": "x = 5",
    "verify_code": "import sympy as sp\nx = sp.Symbol('x')\nsol = sp.solve(3*x + 7 - 22, x)\nprint(f\"x = {sol[0]}\")",
    "techniques": ["polya_four_steps", "work_backwards", "check_by_substitution"]
  }
}"""

# ── 5. ENGLISH LANGUAGE (Comprehension & Concept Thought Process) ────────────
LANGUAGE_EXEMPLAR = r"""{
  "messages": [
    {"role": "user", "content": "Read the following sentence: 'The politician's promises were mere shadows in the mist.' Identify the figure of speech used, and explain why it is effective. (3 marks)"},
    {"role": "assistant", "reasoning": "Literary analysis question. 'were mere shadows' is a direct metaphor (not a simile since no 'like' or 'as'). Effect: shadows in mist are intangible, fleeting, cannot be grasped, suggesting the promises will never be fulfilled.", "content": "Let's unpack this sentence together! 📚\n\nLook closely at the comparison: *'The politician's promises were mere shadows in the mist.'*\nNotice there is no 'like' or 'as'. What figure of speech directly compares two things by saying one thing IS another?"},
    {"role": "user", "content": "is it a metaphor? because it says the promises WERE shadows, not like shadows"},
    {"role": "assistant", "reasoning": "Correct identification. Now guide student to explain the effect: what are shadows in mist like? Intangible, empty, disappearing.", "content": "Spot on — it's a **metaphor**! ✅ That earns you the first mark.\n\nNow for the remaining 2 marks: why is this comparison effective? Think about what *'shadows in the mist'* look and feel like. Can you hold a shadow? Can you see clearly through mist?"},
    {"role": "user", "content": "you cant hold a shadow and mist makes things hard to see. so the promises are empty and will disappear?"},
    {"role": "assistant", "reasoning": "Great understanding. Formalize into a full-mark DBE exam response with rule breakdown and mark coaching.", "content": "That is a brilliant interpretation! 🌟 You've captured the exact mood the writer created.\n\n**Model Answer for Exam:**\n> It is a **metaphor** (1). Just as shadows in the mist are intangible, unclear, and cannot be grasped (1), the politician's promises are insubstantial, empty, and will never be fulfilled or trusted (1).\n\n---\n### 📖 Concept & Thought Process (How to Understand It):\n* **The Concept / Rule:** A **metaphor** directly equates two unlike things to transfer qualities from the image (shadows/mist) onto the subject (promises).\n* **The Thought Process (How to Unpack It):**\n  1. *Step 1 — Literal Image:* What does the image physically do? A shadow in mist has no substance, cannot be caught, and vanishes as the sun comes up.\n  2. *Step 2 — Figurative Connection:* How does that describe the promises? They sound big from afar, but they have no real substance and will vanish without results.\n* **How DBE Markers Score It (The 3-Mark Formula):**\n  * **Mark 1:** Name the figure of speech correctly (**Metaphor**).\n  * **Mark 2:** State the literal meaning of the comparison image.\n  * **Mark 3:** Apply it to the context of the sentence (the promises are hollow).\n\n🎯 **Exam Tip:** Never just write \"it creates an image in the reader's mind\" — DBE markers give 0 marks for generic statements! Always state WHAT specific image is created and HOW it describes the character or event."}
  ],
  "meta": {
    "strategy_used": "exam_technique",
    "final_answer": "Metaphor; conveys that the promises are empty, elusive, and will never materialize",
    "verify_code": "",
    "techniques": ["context_clues", "mark_per_point", "command_word_decode"]
  }
}"""

# ── 6. AFRIKAANS TAAL & BEGRIP (Begrip & Denkwyse Uiteensetting) ──────────────
AFRIKAANS_LANGUAGE_EXEMPLAR = r"""{
  "messages": [
    {"role": "user", "content": "Lees die volgende sin uit die teks: 'My ouma se hande was soos droë herfsblare.' Benoem die beeldspraak en verduidelik die doeltreffendheid daarvan. (3 punte)"},
    {"role": "assistant", "reasoning": "Beeldspraak-analise. 'soos droë herfsblare' gebruik die woord 'soos' -> vergelyking (simile). Effek: herfsblare is gerimpel, droog, broos en aan die einde van hul lewensiklus. Dit beklemtoon die ouma se hoë ouderdom, broosheid en harde werk deur die jare.", "content": "Kom ons kyk mooi na hierdie sin saam! 📚\n\nLees weer: *'My ouma se hande was soos droë herfsblare.'*\nLet op die woord **'soos'**. Watter beeldspraak vergelyk twee sake met mekaar deur 'soos' of 'net soos' te gebruik?"},
    {"role": "user", "content": "dis 'n vergelyking omdat dit die woord 'soos' gebruik"},
    {"role": "assistant", "reasoning": "Korrekte identifikasie (1 punt). Lei die leerder nou om die oordrag van eienskappe te verduidelik: watter eienskappe van herfsblare pas by 'n ouma se hande?", "content": "Presies reg — dit is 'n **vergelyking**! ✅ Daarmee verdien jy jou eerste punt.\n\nNou vir die ander 2 punte: waarom is hierdie vergelyking doeltreffend? Dink aan 'n herfsblaar — hoe lyk en voel dit? En hoe pas dit by 'n ouma se hande?"},
    {"role": "user", "content": "herfsblare is bruin, vol plooie, breek maklik en val van die boom af. so dit wys haar hande is oud, gerimpel en broos?"},
    {"role": "assistant", "reasoning": "Uitstekende interpretasie. Formuleer nou die volpunt KABV-modelantwoord met die Denkwyse-uiteensetting.", "content": "Uitstekende interpretasie! 🌟 Jy het die presiese gevoel raakgesien.\n\n**Model-antwoord vir die Eksamen:**\n> Dit is 'n **vergelyking** (1). Net soos herfsblare droog, vol plooie en broos is (1), beklemtoon dit dat die ouma se hande baie oud, gerimpel en verswak is na baie jare se lewe en werk (1).\n\n---\n### 📖 Begrip & Denkwyse (Hoe om dit te Verstaan):\n* **Die Reël / Stylfiguur:** 'n **Vergelyking** bring twee verskillende sake langs mekaar met die woord *\"soos\"* om 'n eienskap van die een na die ander oor te dra.\n* **Die Denkwyse (Stap-vir-Stap):**\n  1. *Stap 1 — Die Fisiese Beeld:* Herfsblare is aan die einde van hul lewensiklus, vol nerfies en baie broos.\n  2. *Stap 2 — Die Figuurlike Koppel:* Die ouma is ook in die \"herfs\" van haar lewe; haar vel is dun en gerimpel.\n* **Hoe KABV-Nasieners Punte Toeken (Die 3-Punt Formule):**\n  * **Punt 1:** Noem die korrekte beeldspraak (**Vergelyking**).\n  * **Punt 2:** Noem die letterlike eienskappe van die beeld (droog, gerimpel, broos).\n  * **Punt 3:** Koppel dit aan die figuurlike betekenis van die ouma se ouderdom/kwesbaarheid.\n\n🎯 **Eksamen-wenk:** Moet nooit net skryf \"dit skep 'n prentjie\" nie — nasieners gee nul punte daarvoor! Skryf altyd WATTER eienskap oorgedra word."}
  ],
  "meta": {
    "strategy_used": "exam_technique",
    "final_answer": "Vergelyking; beklemtoon die ouma se hoë ouderdom, gerimpelde vel en broosheid",
    "verify_code": "",
    "techniques": ["context_clues", "mark_per_point", "command_word_decode"]
  }
}"""


def get_few_shot_for_subject(subject_raw: str, mode: str = "normal") -> str:
    """Return the most appropriate few-shot exemplar."""
    s = str(subject_raw).lower()
    if mode == "short":
        return MATH_SHORT_EXEMPLAR
    if "afrikaans" in s:
        return AFRIKAANS_LANGUAGE_EXEMPLAR
    elif "wiskunde" in s:
        return AFRIKAANS_MATH_EXEMPLAR
    elif any(k in s for k in ["math", "mathematical"]):
        return MATH_EXEMPLAR
    elif any(k in s for k in ["phys", "science", "wetenskap", "natural"]):
        return SCIENCE_EXEMPLAR
    else:
        return LANGUAGE_EXEMPLAR
