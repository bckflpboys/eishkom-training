"""
Build script for dbe-physical_sciences-g12-p2-2023-may UDVES extraction
"""
import json
import os
import re

SOURCE_ID = "dbe-physical_sciences-g12-p2-2023-may"
PAIR_SOURCE_ID = "dbe-physical_sciences-g12-p2-2023-may-memo"
SUBJECT = "physical_sciences"
GRADE = 12
LANGUAGE = "en"
TRACK = "sciences"

items = []

def add_item(q_ref, marks, topic, passage, question, memo, final_answer, needs_review=False):
    item = {
        "item_id": f"{SOURCE_ID}-{q_ref}",
        "source_id": SOURCE_ID,
        "pair_source_id": PAIR_SOURCE_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": "question",
        "question_ref": q_ref,
        "marks": marks,
        "topic": topic,
        "passage": passage,
        "question": question,
        "memo": memo,
        "final_answer": final_answer,
        "needs_review": needs_review,
        "licence": "DBE copyright - check terms",
        "attribution": "Department of Basic Education"
    }
    items.append(item)

# ==============================================================================
# QUESTION 1
# ==============================================================================

add_item(
    q_ref="1.1",
    marks=2,
    topic="Organic Chemistry - Chain Isomers",
    passage="",
    question="For which ONE of the following molecular formulae are CHAIN isomers possible?\n\nA $\\text{C}_4\\text{H}_{10}$\nB $\\text{C}_3\\text{H}_8$\nC $\\text{C}_2\\text{H}_6\\text{O}$\nD $\\text{C}_3\\text{H}_8\\text{O}$",
    memo="A $\\checkmark\\checkmark$\n\n**Reasoning:**\nChain isomers require a minimum of 4 carbon atoms for alkanes (butane, $\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}_3$, and 2-methylpropane, $\\text{CH}_3\\text{CH}(\\text{CH}_3)\\text{CH}_3$). Propane ($\\text{C}_3\\text{H}_8$) has only one possible carbon chain. $\\text{C}_2\\text{H}_6\\text{O}$ has functional isomers (ethanol and methoxymethane), but no chain isomers. $\\text{C}_3\\text{H}_8\\text{O}$ has positional isomers (propan-1-ol and propan-2-ol) and a functional isomer (methoxyethane), but no chain isomers because the 3-carbon chain cannot branch.",
    final_answer="A"
)

add_item(
    q_ref="1.2",
    marks=2,
    topic="Organic Chemistry - Vapour Pressure and Intermolecular Forces",
    passage="",
    question="Which ONE of the following compounds has the LOWEST vapour pressure under the same conditions?\n\nA [DIAGRAM: Structural formula | Butane, $\\text{H}-\\text{C}(\\text{H}_2)-\\text{C}(\\text{H}_2)-\\text{C}(\\text{H}_2)-\\text{C}(\\text{H}_2)-\\text{H}$]\nB [DIAGRAM: Structural formula | Propanal, $\\text{H}-\\text{C}(\\text{H}_2)-\\text{C}(\\text{H}_2)-\\text{C}(=\\text{O})-\\text{H}$]\nC [DIAGRAM: Structural formula | Propan-1-ol, $\\text{H}-\\text{C}(\\text{H}_2)-\\text{C}(\\text{H}_2)-\\text{C}(\\text{H}_2)-\\text{O}-\\text{H}$]\nD [DIAGRAM: Structural formula | Ethanoic acid, $\\text{H}-\\text{C}(\\text{H}_2)-\\text{C}(=\\text{O})-\\text{O}-\\text{H}$]",
    memo="D $\\checkmark\\checkmark$\n\n**Reasoning:**\nVapour pressure is inversely proportional to the strength of intermolecular forces. Compounds with stronger intermolecular forces have lower vapour pressures at the same temperature.\n- Compound A (butane) has weak London forces.\n- Compound B (propanal) has dipole-dipole forces.\n- Compound C (propan-1-ol) has one site for hydrogen bonding per molecule.\n- Compound D (ethanoic acid, a carboxylic acid) has two sites for hydrogen bonding per molecule and can form stable dimers. Carboxylic acids have the strongest intermolecular forces among these compounds, requiring the most energy to overcome, resulting in the lowest vapour pressure.",
    final_answer="D"
)

add_item(
    q_ref="1.3",
    marks=2,
    topic="Organic Reactions - Dehydrohalogenation of Haloalkanes",
    passage="",
    question="The type of organic compound formed when a haloalkane is heated in the presence of a concentrated strong base is an …\n\nA alkane.\nB alkene.\nC alkyne.\nD alcohol.",
    memo="B $\\checkmark\\checkmark$\n\n**Reasoning:**\nHeating a haloalkane with a concentrated strong base (e.g. concentrated $\\text{NaOH}$ or $\\text{KOH}$ in ethanol) undergoes an elimination reaction (dehydrohalogenation) to form an alkene, a halide salt, and water.",
    final_answer="B"
)

add_item(
    q_ref="1.4",
    marks=2,
    topic="Reaction Kinetics - Factors Affecting Reaction Rate",
    passage="",
    question="EXCESS $\\text{HC}\\ell(\\text{aq})$ of concentration $0{,}1\\text{ mol}\\cdot\\text{dm}^{-3}$ reacts with $2\\text{ g}$ of $\\text{Mg}$ under different conditions.\n\nWhich ONE of the following combinations of conditions will produce the largest volume of $\\text{H}_2(\\text{g})$ in the FIRST MINUTE of the reaction?\n\n| | STATE OF DIVISION OF $\\text{Mg}$ | TEMPERATURE OF $\\text{HC}\\ell(\\text{aq})$ ($^\\circ\\text{C}$) |\n|---|---|---|\n| A | Powder | 20 |\n| B | Granules | 20 |\n| C | Powder | 50 |\n| D | Granules | 50 |",
    memo="C $\\checkmark\\checkmark$\n\n**Reasoning:**\nThe initial rate of reaction determines the volume of gas produced in the first minute:\n1. State of division: Powder has a much larger surface area than granules, providing more contact area for collisions between reactant particles.\n2. Temperature: At $50\\,^\\circ\\text{C}$ compared to $20\\,^\\circ\\text{C}$, particles have higher average kinetic energy, so a greater fraction of colliding particles have kinetic energy equal to or greater than the activation energy ($E_k \\ge E_a$).\nBoth factors together ensure that Powder at $50\\,^\\circ\\text{C}$ (Option C) produces the highest rate and the largest volume of $\\text{H}_2(\\text{g})$ in the first minute.",
    final_answer="C"
)

add_item(
    q_ref="1.5",
    marks=2,
    topic="Reaction Kinetics - Potential Energy Diagrams",
    passage="[DIAGRAM: Potential energy curve vs Course of reaction | Axes: Potential energy (kJ) on y-axis, Course of reaction on x-axis; Reactants start at potential energy level Y; Curve rises to a maximum peak at energy level Z (activated complex); Curve falls to products at energy level X; Baseline is at 0 kJ]",
    question="The potential energy diagram for a chemical reaction is shown below.\n\nWhich ONE of the following combinations is CORRECT for the FORWARD reaction?\n\n| | $\\Delta H$ | ACTIVATION ENERGY | POTENTIAL ENERGY OF THE ACTIVATED COMPLEX |\n|---|---|---|---|\n| A | $\\text{Y} - \\text{X}$ | $\\text{Z} + \\text{Y}$ | $\\text{Z}$ |\n| B | $\\text{Y} - \\text{X}$ | $\\text{Z} - \\text{Y}$ | $\\text{Z} + \\text{Y}$ |\n| C | $\\text{X} - \\text{Y}$ | $\\text{Z} - \\text{Y}$ | $\\text{Z}$ |\n| D | $\\text{X} - \\text{Y}$ | $\\text{Z}$ | $\\text{Z} - \\text{Y}$ |",
    memo="C $\\checkmark\\checkmark$\n\n**Reasoning:**\n- Heat of reaction $\\Delta H = E_{\\text{products}} - E_{\\text{reactants}} = \\text{X} - \\text{Y}$.\n- Activation energy $E_a = E_{\\text{activated complex}} - E_{\\text{reactants}} = \\text{Z} - \\text{Y}$.\n- Potential energy of the activated complex is the energy level at the peak of the curve, which is $\\text{Z}$.\nThus, Option C correctly identifies all three quantities.",
    final_answer="C"
)

add_item(
    q_ref="1.6",
    marks=2,
    topic="Chemical Equilibrium - Le Chatelier's Principle and Disturbance",
    passage="",
    question="Consider the following reaction that reaches equilibrium in a beaker:\n\n$$2\\text{CrO}_4^{2-}(\\text{aq}) + 2\\text{H}^+(\\text{aq}) \\rightleftharpoons \\text{Cr}_2\\text{O}_7^{2-}(\\text{aq}) + \\text{H}_2\\text{O}(\\ell)$$\n\nA few drops of concentrated $\\text{NaOH}(\\text{aq})$ are now added to the beaker.\n\nWhich ONE of the following combinations correctly identifies the DISTURBANCE ON THE SYSTEM and the SYSTEM'S RESPONSE to the disturbance?\n\n| | DISTURBANCE ON THE SYSTEM | SYSTEM'S RESPONSE |\n|---|---|---|\n| A | $[\\text{H}^+]$ decreases | Forward reaction favoured |\n| B | $[\\text{H}^+]$ decreases | Reverse reaction favoured |\n| C | $[\\text{CrO}_4^{2-}]$ decreases | Reverse reaction favoured |\n| D | $[\\text{CrO}_4^{2-}]$ increases | Forward reaction favoured |",
    memo="B $\\checkmark\\checkmark$\n\n**Reasoning:**\nAdding $\\text{NaOH}(\\text{aq})$ introduces hydroxide ions ($\\text{OH}^-$), which react with $\\text{H}^+$ ions to form water ($\\text{H}^+ + \\text{OH}^- \\to \\text{H}_2\\text{O}$). This decreases $[\\text{H}^+]$.\nAccording to Le Chatelier's principle, when $[\\text{H}^+]$ decreases, the equilibrium shifts to favour the reaction that replaces $\\text{H}^+$, which is the reverse reaction.\nTherefore, the disturbance is $[\\text{H}^+]$ decreases, and the response is the reverse reaction favoured (Option B).",
    final_answer="B"
)

add_item(
    q_ref="1.7",
    marks=2,
    topic="Acids and Bases - Lowry-Brønsted Theory",
    passage="",
    question="According to the Lowry-Brønsted theory, a conjugate base is formed when a/an …\n\nA proton is added to the acid.\nB electron is added to the acid.\nC proton is removed from the acid.\nD electron is removed from the acid.",
    memo="C $\\checkmark\\checkmark$\n\n**Reasoning:**\nIn Lowry-Brønsted theory, an acid is a proton donor. When an acid donates (loses) a proton ($\\text{H}^+$), the species remaining is its conjugate base ($\\text{HA} \\rightleftharpoons \\text{A}^- + \\text{H}^+$). Thus, a conjugate base is formed when a proton is removed from the acid.",
    final_answer="C"
)

add_item(
    q_ref="1.8",
    marks=2,
    topic="Acids and Bases - Properties of Alkaline Substances",
    passage="",
    question="Consider the statements below regarding an alkaline substance.\n\nAn alkaline substance:\n(i) Reacts with an acid to form a neutral solution\n(ii) Turns red litmus blue\n(iii) Forms a salt when it reacts with an acid\n\nWhich of the statements above are ALWAYS TRUE?\n\nA (i), (ii) and (iii)\nB (i) and (ii) only\nC (i) and (iii) only\nD (ii) and (iii) only",
    memo="D $\\checkmark\\checkmark$\n\n**Reasoning:**\n- Statement (i) is NOT always true: reacting an acid with a base does not always yield a neutral solution ($\\text{pH} = 7$), as hydrolysis of the salt formed from a weak acid and strong base or strong acid and weak base produces an alkaline or acidic solution respectively, or reactants may not be equimolar.\n- Statement (ii) is always true: alkaline solutions have $\\text{pH} > 7$ and turn red litmus paper blue.\n- Statement (iii) is always true: the reaction between an acid and a base (or alkaline substance) always produces a salt (and water).\nHence statements (ii) and (iii) only are always true (Option D).",
    final_answer="D"
)

add_item(
    q_ref="1.9",
    marks=2,
    topic="Electrochemistry - Galvanic Cell Half-Reactions",
    passage="",
    question="Consider the cell notation for a galvanic cell:\n\n$$\\text{Pt} \\mid \\text{H}_2(\\text{g}) \\mid \\text{OH}^-(\\text{aq}) \\mid \\text{H}_2\\text{O}(\\ell) \\parallel \\text{Ag}^+(\\text{aq}) \\mid \\text{Ag}(\\text{s})$$\n\nWhich ONE of the following equations represents the half-reaction taking place at the positive electrode?\n\nA $\\text{Ag}^+(\\text{aq}) + \\text{e}^- \\to \\text{Ag}(\\text{s})$\nB $\\text{Ag}(\\text{s}) \\to \\text{Ag}^+(\\text{aq}) + \\text{e}^-$\nC $2\\text{H}_2\\text{O}(\\ell) + 2\\text{e}^- \\to \\text{H}_2(\\text{g}) + 2\\text{OH}^-(\\text{aq})$\nD $\\text{H}_2(\\text{g}) + 2\\text{OH}^-(\\text{aq}) \\to 2\\text{H}_2\\text{O}(\\ell) + 2\\text{e}^-$",
    memo="A $\\checkmark\\checkmark$\n\n**Reasoning:**\nIn standard cell notation, the anode (negative electrode in a galvanic cell) is written on the left, and the cathode (positive electrode) is written on the right:\n$$\\text{Anode }(-) \\parallel \\text{Cathode }(+)$$\nAt the cathode (positive electrode), reduction takes place. The cathode half-cell is $\\text{Ag}^+(\\text{aq}) \\mid \\text{Ag}(\\text{s})$, and its reduction half-reaction is:\n$$\\text{Ag}^+(\\text{aq}) + \\text{e}^- \\to \\text{Ag}(\\text{s})$$\nOption A is correct.",
    final_answer="A"
)

add_item(
    q_ref="1.10",
    marks=2,
    topic="Electrochemistry - Electrolysis of Concentrated NaCl",
    passage="",
    question="A concentrated solution of sodium chloride, $\\text{NaC}\\ell(\\text{aq})$, undergoes electrolysis.\n\nWhich ONE of the combinations correctly shows the products formed at each electrode?\n\n| | CATHODE | ANODE |\n|---|---|---|\n| A | $\\text{Na}$ | $\\text{C}\\ell_2$ |\n| B | $\\text{H}_2$ | $\\text{OH}^-$ |\n| C | $\\text{C}\\ell_2$ | $\\text{H}_2\\text{ and }\\text{OH}^-$ |\n| D | $\\text{H}_2\\text{ and }\\text{OH}^-$ | $\\text{C}\\ell_2$ |",
    memo="D $\\checkmark\\checkmark$\n\n**Reasoning:**\nIn the electrolysis of concentrated brine ($\\text{NaC}\\ell(\\text{aq})$):\n- At the cathode (negative electrode), water is a stronger oxidising agent than $\\text{Na}^+$ ($E^\\circ = -0{,}83\\text{ V}$ vs $-2{,}71\\text{ V}$), so water is reduced: $2\\text{H}_2\\text{O}(\\ell) + 2\\text{e}^- \\to \\text{H}_2(\\text{g}) + 2\\text{OH}^-(\\text{aq})$. Products at cathode: $\\text{H}_2$ and $\\text{OH}^-$.\n- At the anode (positive electrode), despite water having a slightly lower standard oxidation potential, the high concentration of chloride ions causes $\\text{C}\\ell^-$ to be oxidised preferentially: $2\\text{C}\\ell^-(\\text{aq}) \\to \\text{C}\\ell_2(\\text{g}) + 2\\text{e}^-$. Product at anode: $\\text{C}\\ell_2$.\nTherefore, Option D is correct.",
    final_answer="D"
)

# ==============================================================================
# QUESTION 2
# ==============================================================================

Q2_PASSAGE = (
    "[TABLE: Organic compounds A to E |\n"
    "A: [DIAGRAM: Structural formula | 5-carbon horizontal chain with ethyl branch at C2 and methyl branch at C4: "
    "CH3-CH(CH2CH3)-CH2-CH(CH3)-CH3, i.e. 2,4-dimethylhexane];\n"
    "B: [DIAGRAM: Structural formula | 3-carbon straight chain alcohol: CH3-CH2-CH2-OH, i.e. propan-1-ol];\n"
    "C: C4H8O;\n"
    "D: CH3(CH2)4CHCH2;\n"
    "E: CxHyOz]"
)

add_item(
    q_ref="2.1",
    marks=2,
    topic="Organic Chemistry - Definition of Unsaturated Hydrocarbon",
    passage=Q2_PASSAGE,
    question="Define the term unsaturated hydrocarbon.",
    memo=(
        "Compounds with one or more multiple bonds between C atoms in the hydrocarbon chain. $\\checkmark\\checkmark$ (2 or 0)\n"
        "(Verbindings met een of meer meervoudige bindings tussen C-atome in die koolwaterstofkettings.)\n\n"
        "OR/OF\n"
        "A hydrocarbon with two or more bonds between the C-atoms.\n"
        "(’n Koolwaterstof met twee of meer bindings tussen die C-atome.)\n\n"
        "OR/OF\n"
        "Hydrocarbons containing not only single bonds between C atoms.\n"
        "(Koolwaterstowwe wat nie slegs enkelbindings tussen die C-atome bevat nie.)\n\n"
        "ACCEPT/AANVAAR:\n"
        "Compounds with one or more double/triple bonds between C atoms in the hydrocarbon chain.\n"
        "(Verbindings met een of meer dubbel/trippelbindings tussen C-atome in die koolwaterstofkettings.)"
    ),
    final_answer=""
)

add_item(
    q_ref="2.2.1",
    marks=1,
    topic="Organic Chemistry - Identification of Unsaturated Hydrocarbon",
    passage=Q2_PASSAGE,
    question="Write down the letter that represents an UNSATURATED hydrocarbon.",
    memo="D $\\checkmark$",
    final_answer="D"
)

add_item(
    q_ref="2.2.2",
    marks=3,
    topic="Organic Chemistry - IUPAC Naming of Branched Alkane",
    passage=Q2_PASSAGE,
    question="Write down the IUPAC name of compound A.",
    memo=(
        "2,4-dimethylhexane $\\checkmark\\checkmark\\checkmark$\n"
        "(2,4-dimetielheksaan)\n\n"
        "Marking criteria:\n"
        "• Correct stem i.e. hexane. $\\checkmark$\n"
        "• Substituents (dimethyl) correctly identified. $\checkmark$\n"
        "• IUPAC name completely correct including numbering, sequence, hyphens and commas. $\\checkmark$"
    ),
    final_answer="2,4-dimethylhexane"
)

add_item(
    q_ref="2.2.3",
    marks=2,
    topic="Organic Chemistry - IUPAC Naming of Positional Isomer",
    passage=Q2_PASSAGE,
    question="Write down the IUPAC name of the POSITIONAL isomer of compound B.",
    memo=(
        "Propan-2-ol / 2-propanol $\\checkmark\\checkmark$\n"
        "(Propan-2-ol / 2-propanol)\n\n"
        "Marking criteria:\n"
        "• Correct stem i.e. propanol. $\\checkmark$\n"
        "• IUPAC name completely correct including numbering and hyphens. $\\checkmark$"
    ),
    final_answer="propan-2-ol"
)

add_item(
    q_ref="2.2.4",
    marks=2,
    topic="Organic Chemistry - IUPAC Naming of Alkene",
    passage=Q2_PASSAGE,
    question="Write down the IUPAC name of compound D.",
    memo=(
        "hept-1-ene / 1-heptene $\\checkmark\\checkmark$\n"
        "(hept-1-een / 1-hepteen)\n\n"
        "Marking criteria:\n"
        "• Correct stem i.e. heptene. $\\checkmark$\n"
        "• IUPAC name completely correct including numbering and hyphens. $\\checkmark$"
    ),
    final_answer="hept-1-ene"
)

add_item(
    q_ref="2.2.5",
    marks=3,
    topic="Organic Chemistry - Balanced Combustion Equation",
    passage=Q2_PASSAGE,
    question="Write down the balanced equation, using MOLECULAR FORMULAE, for the complete combustion of compound A.",
    memo=(
        "$$2\\text{C}_8\\text{H}_{18} + 25\\text{O}_2 \\to 16\\text{CO}_2 + 18\\text{H}_2\\text{O}$$\n\n"
        "Marking criteria:\n"
        "• Correct molecular formula: $\\text{C}_8\\text{H}_{18}$ $\\checkmark$\n"
        "• Correct molecular formula of inorganic reactant and products ($\\text{O}_2$, $\\text{CO}_2$, $\\text{H}_2\\text{O}$). $\\checkmark$\n"
        "• Balancing $\\checkmark$\n\n"
        "Notes:\n"
        "• Ignore double arrows and phases.\n"
        "• If condensed structural formulae used: Max 2/3."
    ),
    final_answer="2C8H18 + 25O2 -> 16CO2 + 18H2O"
)

add_item(
    q_ref="2.3.1",
    marks=2,
    topic="Organic Chemistry - Definition of Functional Isomer",
    passage="The formula $\\text{C}_4\\text{H}_8\\text{O}$ represents two compounds that are functional isomers of each other.",
    question="Define the term functional isomer.",
    memo=(
        "Compounds with the same molecular formula but different functional groups/homologous series. $\\checkmark\\checkmark$\n"
        "(Verbindings met dieselfde molekulêre formule maar verskillende funksionele groepe/homoloë reekse.)\n\n"
        "Marking criteria:\n"
        "If any one of the underlined key phrases in the correct context is omitted, deduct 1 mark."
    ),
    final_answer=""
)

add_item(
    q_ref="2.3.2",
    marks=4,
    topic="Organic Chemistry - Structural Formulae of Functional Isomers",
    passage="The formula $\\text{C}_4\\text{H}_8\\text{O}$ represents two compounds that are functional isomers of each other.",
    question="Write down the STRUCTURAL FORMULAE of each of these two FUNCTIONAL isomers.",
    memo=(
        "Aldehyde (butanal):\n"
        "$$\\begin{array}{cccc}\n"
        "\\text{H} & \\text{H} & \\text{H} & \\text{O} \\\\\n"
        "\\mid & \\mid & \\mid & \\parallel \\\\\n"
        "\\text{H}-\\text{C}-\\text{C}-\\text{C}-\\text{C}-\\text{H} \\\\\n"
        "\\mid & \\mid & \\mid & \\\\\n"
        "\\text{H} & \\text{H} & \\text{H} &\n"
        "\\end{array}$$\n"
        "(ACCEPT: 2-methylpropanal: $\\text{CH}_3\\text{CH}(\\text{CH}_3)\\text{CHO}$)\n\n"
        "Ketone (butan-2-one / butanone):\n"
        "$$\\begin{array}{cccc}\n"
        "\\text{H} & \\text{O} & \\text{H} & \\text{H} \\\\\n"
        "\\mid & \\parallel & \\mid & \\mid \\\\\n"
        "\\text{H}-\\text{C}-\\text{C}-\\text{C}-\\text{C}-\\text{H} \\\\\n"
        "\\mid & & \\mid & \\mid \\\\\n"
        "\\text{H} & & \\text{H} & \\text{H}\n"
        "\\end{array}$$\n\n"
        "Marking criteria:\n"
        "• Functional group for aldehyde correct $\\checkmark$\n"
        "• Whole structure of aldehyde correct $\\checkmark$\n"
        "• Functional group for ketone correct $\\checkmark$\n"
        "• Whole structure of ketone correct $\\checkmark$"
    ),
    final_answer=""
)

add_item(
    q_ref="2.4",
    marks=6,
    topic="Organic Chemistry - Empirical and Molecular Formula Calculation",
    passage="A $2\\text{ g}$ sample of compound E contains $1{,}09\\text{ g}$ carbon and $0{,}18\\text{ g}$ hydrogen. The molecular mass of compound E is $88\\text{ g}\\cdot\\text{mol}^{-1}$.",
    question="Determine the molecular formula of compound E by means of a calculation.",
    memo=(
        "OPTION 1:\n"
        "Mass of oxygen: $m(\\text{O}) = 2 - (1{,}09 + 0{,}18) = 0{,}73\\text{ g}$ $\\checkmark$\n\n"
        "Moles of each element:\n"
        "$n(\\text{C}) = \\frac{m}{M} = \\frac{1{,}09}{12} = 0{,}0908\\text{ mol}$\n"
        "$n(\\text{H}) = \\frac{m}{M} = \\frac{0{,}18}{1} = 0{,}18\\text{ mol}$\n"
        "$n(\\text{O}) = \\frac{m}{M} = \\frac{0{,}73}{16} = 0{,}0456\\text{ mol}$ $\\checkmark$ (for C & H $\\checkmark$, for O $\\checkmark$)\n\n"
        "Simplest mole ratio (divide by smallest mole value $0{,}0456$):\n"
        "$\\text{C}: \\frac{0{,}0908}{0{,}0456} \\approx 2$\n"
        "$\\text{H}: \\frac{0{,}18}{0{,}0456} \\approx 4$\n"
        "$\\text{O}: \\frac{0{,}0456}{0{,}0456} = 1$ $\\checkmark$\n\n"
        "Empirical formula: $\\text{C}_2\\text{H}_4\\text{O}$\n"
        "Molar mass of empirical formula: $M(\\text{C}_2\\text{H}_4\\text{O}) = 2(12) + 4(1) + 16 = 44\\text{ g}\\cdot\\text{mol}^{-1}$\n"
        "Ratio factor $n = \\frac{88}{44} = 2$\n\n"
        "Molecular formula of compound E: $\\text{C}_4\\text{H}_8\\text{O}_2$ $\\checkmark\\checkmark$\n\n"
        "OPTION 2:\n"
        "Percentage composition:\n"
        "$\\%\\text{C} = \\frac{1{,}09}{2} \\times 100 = 54{,}5\\%$\n"
        "$\\%\\text{H} = \\frac{0{,}18}{2} \\times 100 = 9{,}0\\%$\n"
        "$\\%\\text{O} = 100 - (54{,}5 + 9{,}0) = 36{,}5\\%$ $\\checkmark$\n\n"
        "In $100\\text{ g}$:\n"
        "$n(\\text{C}) = \\frac{54{,}5}{12} = 4{,}54\\text{ mol}$\n"
        "$n(\\text{H}) = \\frac{9{,}0}{1} = 9{,}0\\text{ mol}$\n"
        "$n(\\text{O}) = \\frac{36{,}5}{16} = 2{,}28\\text{ mol}$ $\\checkmark\\checkmark$\n\n"
        "Simplest ratio: $\\text{C}:\\text{H}:\\text{O} = 2 : 4 : 1$ $\\checkmark$\n"
        "Empirical formula: $\\text{C}_2\\text{H}_4\\text{O}$\n"
        "$M(\\text{C}_2\\text{H}_4\\text{O}) = 44\\text{ g}\\cdot\\text{mol}^{-1}$\n"
        "$n = \\frac{88}{44} = 2$\n"
        "Molecular formula of compound E: $\\text{C}_4\\text{H}_8\\text{O}_2$ $\\checkmark\\checkmark$"
    ),
    final_answer="C4H8O2"
)

# ==============================================================================
# QUESTION 3
# ==============================================================================

Q3_BASE_PASSAGE = (
    "Learners investigate the boiling points of the four organic compounds given below:\n\n"
    "| ORGANIC COMPOUND | MOLECULAR MASS ($\\text{g}\\cdot\\text{mol}^{-1}$) |\n"
    "|---|---|\n"
    "| Butanone | 72 |\n"
    "| Butan-1-ol | 74 |\n"
    "| Propanoic acid | 74 |\n"
    "| 2-methylpropan-1-ol | 74 |"
)

Q3_GRAPH_PASSAGE = (
    Q3_BASE_PASSAGE + "\n\n"
    "The curves P, Q, R and S below were obtained from the results of the investigation. "
    "X represents a specific temperature.\n\n"
    "[DIAGRAM: Temperature vs Time heating curves | "
    "Axes: Temperature (°C) on y-axis, Time (minute) on x-axis; "
    "Four curves P, Q, R, S starting from room temperature and leveling off at constant horizontal temperature plateaus (boiling points): "
    "Curve P levels off at highest temperature plateau X; "
    "Curve Q levels off at second highest plateau; "
    "Curve R levels off at third plateau; "
    "Curve S levels off at lowest plateau]"
)

add_item(
    q_ref="3.1",
    marks=2,
    topic="Organic Chemistry - Boiling Point Definition",
    passage=Q3_BASE_PASSAGE,
    question="Define the term boiling point.",
    memo=(
        "The temperature at which the vapour pressure (of a compound) equals atmospheric pressure. $\\checkmark\\checkmark$\n"
        "(Die temperatuur waarby die dampdruk (van 'n verbinding) gelyk is aan die atmosferiese druk.)\n\n"
        "Marking criteria:\n"
        "If any one of the underlined key phrases in the correct context is omitted, deduct 1 mark."
    ),
    final_answer=""
)

add_item(
    q_ref="3.2",
    marks=4,
    topic="Organic Chemistry - Boiling Point Comparison of Alcohols",
    passage=Q3_BASE_PASSAGE,
    question="Which compound, butan-1-ol or 2-methylpropan-1-ol, will have the higher boiling point? Fully explain the answer.",
    memo=(
        "Butan-1-ol $\\checkmark$\n"
        "• Has a longer chain length / is less branched / has a larger surface area / contact area. $\\checkmark$\n"
        "• Strength of the intermolecular forces is greater / There are more sites for London forces. $\\checkmark$\n"
        "• More energy is needed to overcome/break intermolecular forces. $\\checkmark$\n\n"
        "OR/OF\n"
        "• 2-methylpropan-1-ol has a shorter chain length / is more branched / has a smaller surface area / contact area.\n"
        "• Strength of the intermolecular forces is weaker / There are fewer sites for London forces.\n"
        "• Less energy is needed to overcome/break intermolecular forces.\n\n"
        "Marking criteria:\n"
        "• Identify Butan-1-ol $\\checkmark$\n"
        "• Compare compounds in terms of branches / chain lengths / surface area $\\checkmark$\n"
        "• Compare strengths of intermolecular forces $\\checkmark$\n"
        "• Compare energy needed to overcome intermolecular forces $\\checkmark$"
    ),
    final_answer="Butan-1-ol"
)

add_item(
    q_ref="3.3",
    marks=1,
    topic="Organic Chemistry - Physical Property from Heating Curve",
    passage=Q3_GRAPH_PASSAGE,
    question="Which physical property is represented by temperature X?",
    memo="Boiling point / Kookpunt $\\checkmark$",
    final_answer="boiling point"
)

add_item(
    q_ref="3.4.1",
    marks=1,
    topic="Organic Chemistry - Identifying Heating Curve for Ketone",
    passage=Q3_GRAPH_PASSAGE,
    question="Which curve (P, Q, R or S) represents Butanone?",
    memo="S $\\checkmark$",
    final_answer="S"
)

add_item(
    q_ref="3.4.2",
    marks=1,
    topic="Organic Chemistry - Identifying Heating Curve for Carboxylic Acid",
    passage=Q3_GRAPH_PASSAGE,
    question="Which curve (P, Q, R or S) represents Propanoic acid?",
    memo="P $\\checkmark$",
    final_answer="P"
)

add_item(
    q_ref="3.4.3",
    marks=1,
    topic="Organic Chemistry - Identifying Heating Curve for Branched Alcohol",
    passage=Q3_GRAPH_PASSAGE,
    question="Which curve (P, Q, R or S) represents 2-methylpropan-1-ol?",
    memo="R $\\checkmark$",
    final_answer="R"
)

add_item(
    q_ref="3.5",
    marks=1,
    topic="Organic Chemistry - Intermolecular Forces in Carboxylic Acids",
    passage=Q3_GRAPH_PASSAGE,
    question="Give a reason for the answer to QUESTION 3.4.2.",
    memo=(
        "Propanoic acid / P has the strongest intermolecular forces. $\\checkmark$\n"
        "OR/OF\n"
        "Two sites for hydrogen bonding (which is stronger than other intermolecular forces).\n"
        "OR/OF\n"
        "Most energy needed to separate the chains / overcome intermolecular forces.\n\n"
        "(Propanoësuur / P het die sterkste intermolekulêre kragte. / Twee plekke vir waterstofbindings (wat sterker is as die ander intermolekulêre kragte). / Meeste energie benodig om kettings te skei.)"
    ),
    final_answer=""
)

# ==============================================================================
# QUESTION 4
# ==============================================================================

Q4_1_PASSAGE = (
    "The flow diagram below shows different organic reactions. P, Q and R are organic compounds.\n\n"
    "[DIAGRAM: Reaction Flow Diagram |\n"
    "Alcohol P --(Reaction 4: Elimination)--> Compound Q;\n"
    "Compound Q --(Reaction 1: + Br2, Addition)--> 1,2-dibromo-2-methylpropane;\n"
    "Compound Q --(Reaction 2: + HCl)--> Compound R (major product);\n"
    "Compound R --(Reaction 3)--> Alcohol P]"
)

add_item(
    q_ref="4.1.1",
    marks=1,
    topic="Organic Reactions - Type of Addition Reaction",
    passage=Q4_1_PASSAGE,
    question="Reaction 1 is an addition reaction.\n\nWrite down the TYPE of addition reaction.",
    memo="Halogenation / Bromination $\\checkmark$\n(Halogenering / Brominering)",
    final_answer="halogenation"
)

add_item(
    q_ref="4.1.2",
    marks=1,
    topic="Organic Reactions - Observation in Halogenation Reaction",
    passage=Q4_1_PASSAGE,
    question="Write down ONE observable change which occurs in the container during reaction 1.",
    memo=(
        "The bromine water / $\\text{Br}_2$ / solution decolourises. / Brown colour disappears. $\\checkmark$\n"
        "(Die broomwater / $\\text{Br}_2$ / oplossing ontkleur. / Bruin kleur verdwyn.)\n\n"
        "OR/OF\n"
        "Bromine water / $\\text{Br}_2$ / solution changes from brown / reddish to colourless.\n"
        "(Broomwater / $\\text{Br}_2$ / oplossing verander van bruin / rooierig na kleurloos.)"
    ),
    final_answer=""
)

add_item(
    q_ref="4.1.3",
    marks=2,
    topic="Organic Reactions - Structural Formula of Alkene",
    passage=Q4_1_PASSAGE,
    question="Write down the STRUCTURAL FORMULA of compound Q.",
    memo=(
        "$$\\begin{array}{ccc}\n"
        "\\text{H} & & \\text{H} \\\\\n"
        "\\mid & & \\mid \\\\\n"
        "\\text{H}-\\text{C} & & \\text{C}-\\text{H} \\\\\n"
        "\\mid & & \\parallel \\\\\n"
        "\\text{H}-\\text{C} & - & \\text{C} \\\\\n"
        "\\mid & & \\mid \\\\\n"
        "\\text{H} & & \\text{H}\n"
        "\\end{array}$$\n"
        "Condensed: $\\text{CH}_2=\\text{C}(\\text{CH}_3)_2$ (2-methylpropene)\n\n"
        "Marking criteria:\n"
        "• Functional group ($>\\text{C}=\\text{C}<$) correct $\\checkmark$\n"
        "• Whole structure correct $\\checkmark$"
    ),
    final_answer=""
)

add_item(
    q_ref="4.1.4",
    marks=2,
    topic="Organic Reactions - IUPAC Naming of Haloalkane",
    passage=Q4_1_PASSAGE,
    question="Consider reaction 2.\n\nWrite down the IUPAC name of compound R.",
    memo=(
        "2-chloro-2-methylpropane $\\checkmark\\checkmark$\n"
        "(2-chloro-2-metielpropaan)\n\n"
        "ACCEPT/AANVAAR:\n"
        "2-chloromethylpropane / 2-chlorometielpropaan"
    ),
    final_answer="2-chloro-2-methylpropane"
)

add_item(
    q_ref="4.1.5",
    marks=6,
    topic="Organic Reactions - Hydrolysis Reaction Equation",
    passage=Q4_1_PASSAGE,
    question="For reaction 3, write down a balanced equation using STRUCTURAL FORMULAE for the organic compounds.",
    memo=(
        "$$\\begin{array}{ccc}\n"
        "& \\text{H} & \\\\\n"
        "& \\mid & \\\\\n"
        "& \\text{H}-\\text{C}-\\text{H} & \\\\\n"
        "& \\mid & \\\\\n"
        "\\text{H}-\\text{C}-\\text{C}-\\text{C}-\\text{H} & + & \\text{NaOH}(\\text{aq}) & \\to & \n"
        "\\begin{array}{ccc}\n"
        "& \\text{H} & \\\\\n"
        "& \\mid & \\\\\n"
        "& \\text{H}-\\text{C}-\\text{H} & \\\\\n"
        "& \\mid & \\\\\n"
        "\\text{H}-\\text{C}-\\text{C}-\\text{C}-\\text{H} & + & \\text{NaC}\\ell(\\text{aq}) \\\\\n"
        "\\mid & \\mid & \\mid \\\\\n"
        "\\text{H} & \\text{O}-\\text{H} & \\text{H}\n"
        "\\end{array} \\\\\n"
        "\\mid & \\mid & \\mid \\\\\n"
        "\\text{H} & \\text{C}\\ell & \\text{H}\n"
        "\\end{array}$$\n\n"
        "(Also accept $\\text{KOH}(\\text{aq}) / \\text{LiOH}(\\text{aq})$ or $\\text{H}_2\\text{O}$ as the inorganic reactant with matching product $\\text{KC}\\ell / \\text{LiC}\\ell$ or $\\text{HC}\\ell$)\n\n"
        "Marking criteria:\n"
        "• $\\text{C}\\ell$ atom on second C atom of compound R $\\checkmark$\n"
        "• Whole structure of compound R correct $\\checkmark$\n"
        "• React compound R with $\\text{NaOH}(\\text{aq}) / \\text{KOH}(\\text{aq}) / \\text{LiOH}(\\text{aq})$ OR $\\text{H}_2\\text{O}$ $\\checkmark$\n"
        "• $\\text{OH}$-group replaces $\\text{C}\\ell$ atom at the same position $\\checkmark$\n"
        "• Whole structure of alcohol correct $\\checkmark$\n"
        "• $\\text{NaC}\\ell(\\text{aq}) / \\text{KC}\\ell(\\text{aq}) / \\text{LiC}\\ell(\\text{aq})$ OR $\\text{HC}\\ell(\\text{aq})$ (must correspond to the inorganic reactant used) $\\checkmark$\n\n"
        "Notes:\n"
        "• Ignore $\\rightleftharpoons$.\n"
        "• Accept all inorganic reagents as condensed.\n"
        "• Accept coefficients that are multiples.\n"
        "• Any additional reactants and/or products: Max 5/6.\n"
        "• Incorrect balancing: Max 5/6.\n"
        "• Molecular formulae: Max 2/6.\n"
        "• Condensed formulae: Max 4/6."
    ),
    final_answer=""
)

add_item(
    q_ref="4.1.6",
    marks=2,
    topic="Organic Chemistry - IUPAC Naming of Tertiary Alcohol",
    passage=Q4_1_PASSAGE,
    question="Write down the IUPAC name of alcohol P.",
    memo=(
        "2-methylpropan-2-ol / 2-methyl-2-propanol $\\checkmark\\checkmark$\n"
        "(2-metielpropan-2-ol / 2-metiel-2-propanol)\n\n"
        "ACCEPT/AANVAAR:\n"
        "Methylpropan-2-ol / Metielpropan-2-ol"
    ),
    final_answer="2-methylpropan-2-ol"
)

add_item(
    q_ref="4.1.7",
    marks=1,
    topic="Organic Reactions - Type of Elimination Reaction",
    passage=Q4_1_PASSAGE,
    question="Reaction 4 is an elimination reaction.\n\nWrite down the TYPE of elimination reaction.",
    memo="Dehydration / Dehidrasie / Dehidratering $\\checkmark$",
    final_answer="dehydration"
)

Q4_2_PASSAGE = "Butan-1-ol reacts with propanoic acid in the presence of a catalyst."

add_item(
    q_ref="4.2.1",
    marks=1,
    topic="Organic Reactions - Type of Esterification Reaction",
    passage=Q4_2_PASSAGE,
    question="Write down the TYPE of reaction that takes place.",
    memo="Esterification / Condensation $\\checkmark$\n(Verestering / Esterfikasie / Kondensasie)",
    final_answer="esterification"
)

add_item(
    q_ref="4.2.2",
    marks=2,
    topic="Organic Chemistry - IUPAC Naming of Ester",
    passage=Q4_2_PASSAGE,
    question="Write down the IUPAC name of the organic product formed.",
    memo=(
        "Butyl propanoate $\\checkmark\\checkmark$\n"
        "(Butielpropanoaat)\n\n"
        "Marking criteria:\n"
        "• Butyl $\\checkmark$\n"
        "• propanoate $\\checkmark$"
    ),
    final_answer="butyl propanoate"
)

# ==============================================================================
# QUESTION 5
# ==============================================================================

Q5_PASSAGE = (
    "Consider the following decomposition reaction that takes place in a sealed $2\\text{ dm}^3$ container:\n\n"
    "$$2\\text{N}_2\\text{O}_5(\\text{g}) \\to 4\\text{NO}_2(\\text{g}) + \\text{O}_2(\\text{g})$$\n\n"
    "The graph below shows how the concentrations of $\\text{N}_2\\text{O}_5(\\text{g})$ and $\\text{NO}_2(\\text{g})$ change with time.\n\n"
    "[DIAGRAM: Concentration vs Time graph |\n"
    "Axes: Concentration ($\\times 10^{-4}\\text{ mol}\\cdot\\text{dm}^{-3}$) on y-axis from 0 to 300, Time (s) on x-axis from 0 to 800;\n"
    "Curve A (product): Starts at $(0, 0)$, rises through $(100, 62)$, $(200, 110)$, $(300, 160)$, $(400, 200)$, $(500, 230)$, $(600, 255)$, $(700, 280)$;\n"
    "Curve B (reactant): Starts at $(0, 200)$, decreases through $(100, 170)$, $(200, 140)$, $(300, 120)$, $(400, 100)$, $(500, 88)$, $(600, 70)$, $(700, 60)$]"
)

add_item(
    q_ref="5.1",
    marks=1,
    topic="Reaction Kinetics - Concentration-Time Graph Interpretation",
    passage=Q5_PASSAGE,
    question="Refer to the graph above and give a reason why curve A represents the change in the concentration of $\\text{NO}_2(\\text{g})$.",
    memo=(
        "Initial concentration is 0 (of $\\text{NO}_2$). / Concentration increases. / Curve starts at 0. $\\checkmark$\n"
        "(Beginkonsentrasie is 0 (van $\\text{NO}_2$). / Konsentrasie verhoog. / Kurwe begin by 0.)\n\n"
        "OR/OF\n"
        "Curve B has an initial concentration and is the reactant as its concentration decreases.\n"
        "(Kurwe B het 'n beginkonsentrasie en is die reaktant aangesien sy konsentrasie afneem.)"
    ),
    final_answer=""
)

add_item(
    q_ref="5.2",
    marks=2,
    topic="Reaction Kinetics - Reaction Rate Mole Ratio",
    passage=Q5_PASSAGE,
    question=(
        "Consider the statement below:\n\n"
        "The rate of decomposition of $\\text{N}_2\\text{O}_5(\\text{g})$ is half the rate of formation of $\\text{NO}_2(\\text{g})$.\n\n"
        "Is this statement TRUE or FALSE? Give a reason for the answer."
    ),
    memo=(
        "True $\\checkmark$\n"
        "$n\\text{ mol}$ of $\\text{N}_2\\text{O}_5$ forms $2n\\text{ mol}$ of $\\text{NO}_2$ per unit time (mole ratio $2 : 4 = 1 : 2$). $\\checkmark$\n"
        "(Waar. $n\\text{ mol}$ $\\text{N}_2\\text{O}_5$ vorm $2n\\text{ mol}$ $\\text{NO}_2$ per eenheidstyd.)\n\n"
        "OR/OF\n"
        "Gradient of graph for $\\text{NO}_2$ is twice the gradient of graph for $\\text{N}_2\\text{O}_5$.\n"
        "(Gradiënt van grafiek vir $\\text{NO}_2$ is twee keer die gradiënt van grafiek vir $\\text{N}_2\\text{O}_5$.)\n\n"
        "NOTE:\n"
        "If gradients calculated correctly award mark."
    ),
    final_answer="True"
)

add_item(
    q_ref="5.3.1",
    marks=4,
    topic="Reaction Kinetics - Mass Calculation from Concentration Graph",
    passage=Q5_PASSAGE,
    question="Calculate the mass of $\\text{NO}_2(\\text{g})$ present in the container at $400\\text{ s}$.",
    memo=(
        "OPTION 1:\n"
        "$c(\\text{NO}_2) = \\frac{m}{MV}$ $\\checkmark$\n"
        "$200 \\times 10^{-4} = \\frac{m}{(46)(2)}$ $\\checkmark\\checkmark$\n"
        "$m = 1{,}84\\text{ g}$ $\\checkmark$\n\n"
        "OPTION 2:\n"
        "$n(\\text{NO}_2) = cV = (200 \\times 10^{-4})(2) = 4 \\times 10^{-2}\\text{ mol}$ $\\checkmark\\checkmark$\n"
        "$m(\\text{NO}_2) = nM = (4 \\times 10^{-2})(46) = 1{,}84\\text{ g}$ $\\checkmark\\checkmark$\n\n"
        "Marking criteria:\n"
        "• Formula: $c = \\frac{m}{MV} / n(\\text{NO}_2) = cV / n(\\text{NO}_2) = \\frac{m}{M}$ $\\checkmark$\n"
        "• Substitute change in concentration ($200 \\times 10^{-4}\\text{ mol}\\cdot\\text{dm}^{-3}$) $\\checkmark$\n"
        "• Substitute $M = 46\\text{ g}\\cdot\\text{mol}^{-1}$ and $V = 2\\text{ dm}^3$ $\\checkmark$\n"
        "• Final correct answer: $1{,}84\\text{ g}$ $\\checkmark$"
    ),
    final_answer="1.84"
)

add_item(
    q_ref="5.3.2",
    marks=4,
    topic="Reaction Kinetics - Average Reaction Rate Calculation",
    passage=Q5_PASSAGE,
    question="Calculate the average rate of production of $\\text{O}_2(\\text{g})$ in $\\text{mol}\\cdot\\text{dm}^{-3}\\cdot\\text{s}^{-1}$ in $700\\text{ s}$.",
    memo=(
        "OPTION 1:\n"
        "$\\text{Average rate}(\\text{N}_2\\text{O}_5) = -\\frac{\\Delta c}{\\Delta t} = -\\frac{(60 \\times 10^{-4} - 200 \\times 10^{-4})}{700 - 0} = 2 \\times 10^{-5}\\text{ mol}\\cdot\\text{dm}^{-3}\\cdot\\text{s}^{-1}$ $\\checkmark\\checkmark$\n"
        "$\\text{Rate}(\\text{O}_2) = \\frac{1}{2}\\text{Rate}(\\text{N}_2\\text{O}_5) = \\frac{1}{2}(2 \\times 10^{-5}) = 1 \\times 10^{-5}\\text{ mol}\\cdot\\text{dm}^{-3}\\cdot\\text{s}^{-1}$ $\\checkmark\\checkmark$\n\n"
        "OPTION 2:\n"
        "$\\text{Average rate}(\\text{NO}_2) = \\frac{\\Delta c}{\\Delta t} = \\frac{(280 \\times 10^{-4} - 0)}{700 - 0} = 4 \\times 10^{-5}\\text{ mol}\\cdot\\text{dm}^{-3}\\cdot\\text{s}^{-1}$ $\\checkmark\\checkmark$\n"
        "$\\text{Rate}(\\text{O}_2) = \\frac{1}{4}\\text{Rate}(\\text{NO}_2) = \\frac{1}{4}(4 \\times 10^{-5}) = 1 \\times 10^{-5}\\text{ mol}\\cdot\\text{dm}^{-3}\\cdot\\text{s}^{-1}$ $\\checkmark\\checkmark$\n\n"
        "OPTION 3:\n"
        "$\\Delta c(\\text{O}_2) = \\frac{1}{2}\\Delta c(\\text{N}_2\\text{O}_5) = \\frac{1}{2}(140 \\times 10^{-4}) = 7 \\times 10^{-3}\\text{ mol}\\cdot\\text{dm}^{-3}$ $\\checkmark$\n"
        "$\\text{Average rate} = \\frac{\\Delta c}{\\Delta t} = \\frac{7 \\times 10^{-3}}{700} = 1 \\times 10^{-5}\\text{ mol}\\cdot\\text{dm}^{-3}\\cdot\\text{s}^{-1}$ $\\checkmark\\checkmark\\checkmark$\n\n"
        "Marking criteria:\n"
        "• Substitute change in concentration into rate formula $\\checkmark$\n"
        "• Substitute time ($700\\text{ s}$) into rate formula $\\checkmark$\n"
        "• Use mole ratio: $\\text{rate}(\\text{O}_2) = \\frac{1}{2}\\text{rate}(\\text{N}_2\\text{O}_5) / \\frac{1}{4}\\text{rate}(\\text{NO}_2)$ $\\checkmark$\n"
        "• Final correct answer: $1 \\times 10^{-5}\\text{ mol}\\cdot\\text{dm}^{-3}\\cdot\\text{s}^{-1}$ $\\checkmark$\n\n"
        "NOTE:\n"
        "If concentration is converted to moles, final moles per s ($\\text{mol}\\cdot\\text{s}^{-1}$) must be converted back to concentration ($\\text{mol}\\cdot\\text{dm}^{-3}\\cdot\\text{s}^{-1}$). If division/multiplication by 2 is omitted: Max 3/4."
    ),
    final_answer="0.00001"
)

Q5_4_PASSAGE = (
    "The Maxwell-Boltzmann distribution curve for the $\\text{N}_2\\text{O}_5(\\text{g})$ initially present in the container is shown below:\n\n"
    "[DIAGRAM: Maxwell-Boltzmann distribution curve | Axes: Number of particles on y-axis, Kinetic energy on x-axis; Curve labelled P starts at origin, rises to a peak and tapers off to the right at higher kinetic energy]\n\n"
    "The initial concentration of the $\\text{N}_2\\text{O}_5(\\text{g})$ is now INCREASED."
)

add_item(
    q_ref="5.4.1",
    marks=2,
    topic="Reaction Kinetics - Maxwell-Boltzmann Curve at Higher Concentration",
    passage=Q5_4_PASSAGE,
    question="Redraw the distribution curve above in the ANSWER BOOK and label this curve as P.\n\nOn the same set of axes, sketch the curve that will be obtained for the higher concentration of $\\text{N}_2\\text{O}_5(\\text{g})$. Label this curve as Q.",
    memo=(
        "[DIAGRAM: Maxwell-Boltzmann distribution curves P and Q | Axes: Number of particles vs Kinetic energy; "
        "Curve P is original curve; Curve Q starts at origin, lies completely above curve P with a higher peak at the same kinetic energy, and tapers off above curve P without crossing it]\n\n"
        "Marking criteria:\n"
        "• Curve Q must be above the given curve P and have the same shape as the given curve P and the peaks have to correspond (same peak kinetic energy, higher peak height). $\\checkmark$\n"
        "• Starts at origin and not crossing curve P. $\\checkmark$"
    ),
    final_answer=""
)

add_item(
    q_ref="5.4.2",
    marks=3,
    topic="Reaction Kinetics - Collision Theory Explanation of Concentration Effect",
    passage=Q5_4_PASSAGE,
    question="Will the rate of decomposition of $\\text{N}_2\\text{O}_5(\\text{g})$ at the higher concentration be HIGHER THAN, LOWER THAN or EQUAL TO the original rate of decomposition? Explain the answer using the collision theory.",
    memo=(
        "Higher than $\\checkmark$\n"
        "• When the concentration of $\\text{N}_2\\text{O}_5$ is higher there are more $\\text{N}_2\\text{O}_5$ particles per unit volume. $\\checkmark$\n"
        "• More effective collisions per unit time / second. / Higher frequency of effective collisions. $\\checkmark$\n\n"
        "(Hoër as. 'n Hoër konsentrasie van $\\text{N}_2\\text{O}_5$ bevat meer $\\text{N}_2\\text{O}_5$-deeltjies per eenheidsvolume. Meer effektiewe botsings per eenheidstyd/sekonde / Hoër frekwensie van effektiewe botsings.)"
    ),
    final_answer="Higher than"
)

# ==============================================================================
# QUESTION 6
# ==============================================================================

Q6_PASSAGE = (
    "One mole of pure hydrogen iodide gas, $\\text{HI}(\\text{g})$, is sealed in a $1\\text{ dm}^3$ container at $721\\text{ K}$. "
    "Equilibrium is reached according to the following balanced equation:\n\n"
    "$$2\\text{HI}(\\text{g}) \\rightleftharpoons \\text{H}_2(\\text{g}) + \\text{I}_2(\\text{g})$$\n\n"
    "It is found that $0{,}11\\text{ moles}$ of $\\text{I}_2(\\text{g})$ are present at equilibrium."
)

add_item(
    q_ref="6.1",
    marks=2,
    topic="Chemical Equilibrium - Le Chatelier's Principle Definition",
    passage=Q6_PASSAGE,
    question="State Le Chatelier's principle.",
    memo=(
        "When the equilibrium in a closed system is disturbed, the system will reinstate a (new) equilibrium by favouring the reaction that will cancel/oppose the disturbance. $\\checkmark\\checkmark$\n"
        "(Wanneer die ewewig in 'n geslote sisteem versteur word, sal die sisteem 'n (nuwe) ewewig instel deur die reaksie te bevoordeel wat die versteuring kanselleer/teenwerk.)\n\n"
        "Marking criteria:\n"
        "If any one of the underlined key phrases in the correct context is omitted, deduct 1 mark."
    ),
    final_answer=""
)

add_item(
    q_ref="6.2.1",
    marks=1,
    topic="Chemical Equilibrium - Equilibrium Mole Determination for H2",
    passage=Q6_PASSAGE,
    question="Determine the number of moles of $\\text{H}_2(\\text{g})$ at equilibrium.",
    memo="$n[\\text{H}_2(\\text{g})] = 0{,}11\\text{ mol}$ $\\checkmark$",
    final_answer="0.11"
)

add_item(
    q_ref="6.2.2",
    marks=1,
    topic="Chemical Equilibrium - Equilibrium Mole Determination for HI",
    passage=Q6_PASSAGE,
    question="Determine the number of moles of $\\text{HI}(\\text{g})$ at equilibrium.",
    memo=(
        "OPTION 1:\n"
        "$n(\\text{HI})_{\\text{used}} = 2n(\\text{I}_2) = 2(0{,}11) = 0{,}22\\text{ mol}$\n"
        "$n(\\text{HI})_{\\text{eq}} = 1 - 0{,}22 = 0{,}78\\text{ mol}$ $\\checkmark$\n\n"
        "OPTION 2:\n"
        "$$K_c = \\frac{[\\text{H}_2][\\text{I}_2]}{[\\text{HI}]^2}$$\n"
        "$$0{,}02 = \\frac{(0{,}11)(0{,}11)}{[\\text{HI}]^2} \\implies [\\text{HI}] = 0{,}78\\text{ mol}\\cdot\\text{dm}^{-3}$$\n"
        "$n(\\text{HI}) = 0{,}78\\text{ mol}$ $\\checkmark$"
    ),
    final_answer="0.78"
)

Q6_3_PASSAGE = (
    Q6_PASSAGE + "\n\n"
    "The equilibrium constant, $K_c$, at $721\\text{ K}$ is $0{,}02$.\n"
    "The temperature of the container is now increased to $850\\text{ K}$.\n"
    "The equilibrium constant, $K_c$, at $850\\text{ K}$ is $0{,}09$."
)

add_item(
    q_ref="6.3.1",
    marks=1,
    topic="Chemical Equilibrium - Exothermic or Endothermic Identification",
    passage=Q6_3_PASSAGE,
    question="Is the forward reaction EXOTHERMIC or ENDOTHERMIC?",
    memo="Endothermic / Endotermies $\\checkmark$",
    final_answer="Endothermic"
)

add_item(
    q_ref="6.3.2",
    marks=3,
    topic="Chemical Equilibrium - Temperature Effect on Kc Explanation",
    passage=Q6_3_PASSAGE,
    question="Fully explain the answer to QUESTION 6.3.1.",
    memo=(
        "$K_c$ increased:\n"
        "• The concentration of the product / $\\text{H}_2(\\text{g})$ and $\\text{I}_2(\\text{g})$ is increased. / The concentration of the reactant / $\\text{HI}$ decreases. $\\checkmark$\n"
        "• The increase in temperature favours the forward reaction. $\\checkmark$\n"
        "• (According to Le Chatelier's principle) an increase in temperature favours the endothermic reaction. $\\checkmark$\n\n"
        "($K_c$ het verhoog: Die konsentrasie van die produkte/$\\text{H}_2(\\text{g})$ en $\\text{I}_2(\\text{g})$ verhoog / konsentrasie van die reaktanse/$\\text{HI}$ verlaag. 'n Toename in temperatuur bevoordeel die voorwaartse reaksie. (Volgens Le Chatelier se beginsel) sal 'n toename in temperatuur die endotermiese reaksie bevoordeel.)"
    ),
    final_answer=""
)

add_item(
    q_ref="6.3.3",
    marks=8,
    topic="Chemical Equilibrium - Mass of HI at New Equilibrium Calculation",
    passage=Q6_3_PASSAGE,
    question="Calculate the mass of $\\text{HI}(\\text{g})$ present at the new equilibrium at $850\\text{ K}$.",
    memo=(
        "POSITIVE MARKING FROM Q6.2\n\n"
        "OPTION 1 / OPTION 2:\n"
        "$$K_c = \\frac{[\\text{H}_2][\\text{I}_2]}{[\\text{HI}]^2}$$ $\\checkmark$ (a)\n\n"
        "| | $2\\text{HI}$ | $\\text{I}_2$ | $\\text{H}_2$ |\n"
        "|---|---|---|---|\n"
        "| Initial quantity (mol) | $0{,}78$ | $0{,}11$ | $0{,}11$ |\n"
        "| Change (mol) | $-2x$ | $+x$ | $+x$ |\n"
        "| Equilibrium quantity (mol) | $0{,}78 - 2x$ | $0{,}11 + x$ | $0{,}11 + x$ |\n"
        "| Equilibrium concentration ($\\text{mol}\\cdot\\text{dm}^{-3}$) | $0{,}78 - 2x$ | $0{,}11 + x$ | $0{,}11 + x$ |\n\n"
        "Substitute into $K_c$ expression:\n"
        "$$0{,}09 = \\frac{(0{,}11 + x)(0{,}11 + x)}{(0{,}78 - 2x)^2}$$ $\\checkmark\\checkmark\\checkmark\\checkmark$ (b, c, d, e)\n\n"
        "Taking square roots on both sides:\n"
        "$$0{,}3 = \\frac{0{,}11 + x}{0{,}78 - 2x}$$\n"
        "$$0{,}3(0{,}78 - 2x) = 0{,}11 + x$$\n"
        "$$0{,}234 - 0{,}6x = 0{,}11 + x$$\n"
        "$$1{,}6x = 0{,}124 \\implies x = 0{,}0775\\text{ mol}$$\n\n"
        "$[\\text{HI}]_{\\text{equilibrium}} = [\\text{HI}]_{\\text{ini}} - \\Delta[\\text{HI}]$\n"
        "$= 0{,}78 - 2(0{,}0775) = 0{,}625\\text{ mol}\\cdot\\text{dm}^{-3} \\approx 0{,}63\\text{ mol}\\cdot\\text{dm}^{-3}$ $\\checkmark$ (f)\n\n"
        "$n(\\text{HI}) = cV = (0{,}63)(1) = 0{,}63\\text{ mol}$ (or $0{,}625\\text{ mol}$)\n\n"
        "$m(\\text{HI}) = nM = (0{,}63)(128) = 80{,}64\\text{ g}$ $\\checkmark\\checkmark$ (g, h)\n"
        "(Using $0{,}625\\text{ mol}$: $m = 0{,}625 \\times 128 = 80{,}00\\text{ g}$. Accept range: $79{,}36\\text{ to }80{,}64\\text{ g}$)\n\n"
        "Marking criteria:\n"
        "(a) Correct $K_c$ expression (formulae in square brackets). $\\checkmark$\n"
        "(b) Substitution of $0{,}09$ in $K_c$ expression. $\\checkmark$\n"
        "(c) Correct initial moles from 6.2.1 and 6.2.2 ($0{,}11$ and $0{,}78$). $\\checkmark$\n"
        "(d) USING ratio: $n(\\text{HI}) : 2n(\\text{I}_2) = 1 : 2$. $\\checkmark$\n"
        "(e) Substitution of concentrations into correct $K_c$ expression. $\\checkmark$\n"
        "(f) Subtraction $[\\text{HI}]_{\\text{ini}} - \\Delta[\\text{HI}]$. $\\checkmark$\n"
        "(g) Substitution of $128$ in $m = nM$. $\\checkmark$\n"
        "(h) Final answer: $80{,}64\\text{ g}$ (range: $79{,}36 - 80{,}64\\text{ g}$). $\\checkmark$"
    ),
    final_answer="80.64"
)

# ==============================================================================
# QUESTION 7
# ==============================================================================

Q7_1_PASSAGE = (
    "The conductivity of three acid solutions, A, B and C, as shown below is investigated at the same temperature:\n\n"
    "| Solution | Acid |\n"
    "|---|---|\n"
    "| A | $0{,}1\\text{ mol}\\cdot\\text{dm}^{-3}\\text{ H}_2\\text{SO}_4(\\text{aq})$ |\n"
    "| B | $0{,}1\\text{ mol}\\cdot\\text{dm}^{-3}\\text{ HNO}_3(\\text{aq})$ |\n"
    "| C | $0{,}1\\text{ mol}\\cdot\\text{dm}^{-3}\\text{ CH}_3\\text{COOH}(\\text{aq})$ |\n\n"
    "The brightness of the bulb in the apparatus shown below is used as a measure of the conductivity of the solutions.\n\n"
    "[DIAGRAM: Conductivity apparatus | Beaker containing acid solution with two immersed carbon electrodes connected in series with a light bulb and a DC power source (cell)]\n\n"
    "The acid solutions are electrolytes."
)

add_item(
    q_ref="7.1.1",
    marks=2,
    topic="Acids and Bases - Definition of Electrolyte",
    passage=Q7_1_PASSAGE,
    question="Define the term electrolyte.",
    memo=(
        "ANY ONE:\n"
        "• A substance whose aqueous solution contains ions. $\\checkmark\\checkmark$ (2 or 0)\n"
        "• Substance that dissolves in water to give a solution that conducts electricity.\n"
        "• A substance that forms ions in water / forms ions when molten.\n\n"
        "(ENIGE EEN:\n"
        "• 'n Stof waarvan die oplossing ione bevat. $\\checkmark\\checkmark$ (2 of 0)\n"
        "• 'n Stof wat in water oplos om 'n oplossing te vorm wat elektrisiteit gelei.\n"
        "• 'n Stof wat ione vorm in water / ione vorm wanneer gesmelt.)"
    ),
    final_answer=""
)

add_item(
    q_ref="7.1.2",
    marks=2,
    topic="Acids and Bases - Comparing Conductivity of Strong Diprotic vs Monoprotic Acids",
    passage=Q7_1_PASSAGE,
    question="In which solution, A or B, will the bulb be brighter? Give a reason for the answer by referring to the types of acids.",
    memo=(
        "A $\\checkmark$\n"
        "$\\text{H}_2\\text{SO}_4$ is diprotic. / Donates more than one mole of $\\text{H}^+$ ions per mole of acid $\\checkmark$ (and both acids are of the same concentration). / $\\text{H}_2\\text{SO}_4$ has a higher $K_a$ value.\n"
        "(\\text{H}_2\\text{SO}_4 is diproties. / Skenk meer as een mol $\\text{H}^+$ ione per mol suur (en beide sure het dieselfde konsentrasie). / $\\text{H}_2\\text{SO}_4$ het 'n hoër $K_a$-waarde.)\n\n"
        "OR/OF\n"
        "It ionises to produce more than one mole of protons / $\\text{H}^+$ ions for each mole of $\\text{H}_2\\text{SO}_4$.\n"
        "(Dit ioniseer om meer as een mol protone / $\\text{H}^+$-ione vir elke mol $\\text{H}_2\\text{SO}_4$ te vorm.)"
    ),
    final_answer="A"
)

add_item(
    q_ref="7.1.3",
    marks=2,
    topic="Acids and Bases - Comparing Conductivity of Strong vs Weak Monoprotic Acids",
    passage=Q7_1_PASSAGE,
    question="In which solution, B or C, will the bulb be brighter? Give a reason for the answer by referring to the types of acids.",
    memo=(
        "B $\\checkmark$\n"
        "Stronger acid / ionises completely $\\checkmark$ (and both acids are of the same concentration). / $\\text{HNO}_3$ has a higher $K_a$ value.\n"
        "(Sterker suur / ioniseer volledig (en beide sure het dieselfde konsentrasie). / $\\text{HNO}_3$ het 'n hoër $K_a$-waarde.)\n\n"
        "OR/OF\n"
        "C / $\\text{CH}_3\\text{COOH}$ is a weaker acid / ionises incompletely.\n"
        "(C / $\\text{CH}_3\\text{COOH}$ is 'n swak suur / ioniseer onvolledig.)"
    ),
    final_answer="B"
)

Q7_2_BASE_PASSAGE = (
    "A hydrochloric acid solution, $\\text{HC}\\ell(\\text{aq})$, is standardised by titrating it against $25\\text{ cm}^3$ of a $0{,}04\\text{ mol}\\cdot\\text{dm}^{-3}$ sodium carbonate solution, $\\text{Na}_2\\text{CO}_3(\\text{aq})$. "
    "At the endpoint, it is found that $19{,}5\\text{ cm}^3$ of $\\text{HC}\\ell(\\text{aq})$ has reacted.\n\n"
    "The balanced equation for the reaction is:\n\n"
    "$$\\text{Na}_2\\text{CO}_3(\\text{aq}) + 2\\text{HC}\\ell(\\text{aq}) \\to 2\\text{NaC}\\ell(\\text{aq}) + \\text{CO}_2(\\text{g}) + \\text{H}_2\\text{O}(\\ell)$$"
)

add_item(
    q_ref="7.2.1",
    marks=3,
    topic="Acids and Bases - Standardisation of Hydrochloric Acid Calculation",
    passage=Q7_2_BASE_PASSAGE,
    question="Calculate the concentration of the $\\text{HC}\\ell(\\text{aq})$.",
    memo=(
        "OPTION 1:\n"
        "$$\\frac{c_a V_a}{c_b V_b} = \\frac{n_a}{n_b}$$\n"
        "$$\\frac{c_a (19{,}5)}{(0{,}04)(25)} = \\frac{2}{1}$$ $\\checkmark\\checkmark$\n"
        "$$c_a = 0{,}10\\text{ mol}\\cdot\\text{dm}^{-3}$$ (or $0{,}103\\text{ mol}\\cdot\\text{dm}^{-3}$) $\\checkmark$\n\n"
        "OPTION 2:\n"
        "$n(\\text{Na}_2\\text{CO}_3) = cV = (0{,}04)(0{,}025) = 0{,}001\\text{ mol}$\n"
        "$n(\\text{HC}\\ell) = 2n(\\text{Na}_2\\text{CO}_3) = 0{,}002\\text{ mol}$ $\\checkmark$\n"
        "$[\\text{HC}\\ell] = \\frac{n}{V} = \\frac{0{,}002}{0{,}0195} = 0{,}10\\text{ mol}\\cdot\\text{dm}^{-3}$ (or $0{,}103\\text{ mol}\\cdot\\text{dm}^{-3}$) $\\checkmark\\checkmark$\n\n"
        "Marking criteria:\n"
        "• Substitute $0{,}04\\text{ mol}\\cdot\\text{dm}^{-3}$, $25\\text{ cm}^3$, and $19{,}5\\text{ cm}^3$. $\\checkmark$\n"
        "• USE mole ratio: $n(\\text{Na}_2\\text{CO}_3) : n(\\text{HC}\\ell) = 1 : 2$. $\\checkmark$\n"
        "• Final answer: $0{,}10\\text{ to }0{,}103\\text{ mol}\\cdot\\text{dm}^{-3}$. $\\checkmark$"
    ),
    final_answer="0.10"
)

add_item(
    q_ref="7.2.2",
    marks=2,
    topic="Acids and Bases - Effect of Water in Burette on Titration Volume",
    passage=Q7_2_BASE_PASSAGE,
    question=(
        "Suppose a few drops of water were present in the burette before it was filled with the hydrochloric acid solution.\n\n"
        "How will the volume of the $\\text{HC}\\ell$ solution needed to reach the endpoint be affected?\n\n"
        "Choose from GREATER THAN, SMALLER THAN or REMAINS THE SAME. Give a reason for the answer."
    ),
    memo=(
        "Greater than / Groter as $\\checkmark$\n\n"
        "The few drops of water will dilute the $\\text{HC}\\ell$, $\\checkmark$ therefore a greater volume of acid will be needed to neutralise the base.\n"
        "('n Paar druppels water sal die $\\text{HC}\\ell$ verdun, daarom sal 'n groter volume suur benodig word om die basis te neutraliseer.)"
    ),
    final_answer="Greater than"
)

Q7_2_TITRATION_PASSAGE = (
    "A concentrated household product, ChemClean, contains ammonia as the main cleaning agent. "
    "To determine the amount of ammonia present in $1\\text{ dm}^3$ of ChemClean, the following procedure is followed:\n\n"
    "$20\\text{ cm}^3$ of ChemClean is added to a $250\\text{ cm}^3$ flask. The flask is then filled to the $250\\text{ cm}^3$ mark with distilled water.\n\n"
    "[DIAGRAM: Dilution of ChemClean | Beaker of concentrated ChemClean pours 20 cm³ into a 250 cm³ volumetric flask. Arrow pointing right shows flask filled with distilled water to the 250 cm³ mark, producing 250 cm³ of diluted ChemClean]\n\n"
    "The diluted solution is titrated against the hydrochloric acid solution of the concentration as calculated in QUESTION 7.2.1.\n\n"
    "During the titration, $22\\text{ cm}^3$ of the diluted ChemClean solution is neutralised by $18{,}7\\text{ cm}^3$ of the $\\text{HC}\\ell$ solution. "
    "The balanced equation for the reaction is:\n\n"
    "$$\\text{NH}_3(\\text{aq}) + \\text{HC}\\ell(\\text{aq}) \\to \\text{NH}_4^+(\\text{aq}) + \\text{C}\\ell^-(\\text{aq})$$"
)

add_item(
    q_ref="7.2.3",
    marks=7,
    topic="Acids and Bases - Mass of Ammonia in Commercial Cleaner Calculation",
    passage=Q7_2_TITRATION_PASSAGE,
    question="Calculate the mass of ammonia in $1\\text{ dm}^3$ of ChemClean.",
    memo=(
        "POSITIVE MARKING FROM Q7.2.1\n\n"
        "OPTION 1:\n"
        "$n(\\text{HC}\\ell) = cV = (0{,}1)(18{,}7 \\times 10^{-3}) = 1{,}87 \\times 10^{-3}\\text{ mol}$ $\\checkmark$ (a)\n"
        "$n(\\text{NH}_3)_{\\text{reacted}} = n(\\text{HC}\\ell)_{\\text{reacted}} = 1{,}87 \\times 10^{-3}\\text{ mol}$ $\\checkmark$ (b)\n"
        "$n(\\text{NH}_3)\\text{ in }22\\text{ cm}^3 = 1{,}87 \\times 10^{-3}\\text{ mol}$\n\n"
        "$n(\\text{NH}_3)\\text{ in }250\\text{ cm}^3 = \\frac{1{,}87 \\times 10^{-3}}{0{,}022} \\times 0{,}25 = 0{,}02125\\text{ mol}$ $\\checkmark\\checkmark$ (c, d)\n"
        "$n(\\text{NH}_3)\\text{ in initial }20\\text{ cm}^3 = 0{,}02125\\text{ mol}$\n\n"
        "$m(\\text{NH}_3)\\text{ in }20\\text{ cm}^3 = nM = (0{,}02125)(17) = 0{,}361\\text{ g}$ $\\checkmark$ (f)\n\n"
        "Mass in $1000\\text{ cm}^3$ ($1\\text{ dm}^3$):\n"
        "$m(\\text{NH}_3) = \\frac{0{,}361}{0{,}020} \\times 1 = 18{,}06\\text{ g}$ $\\checkmark\\checkmark$ (e, g)\n\n"
        "OPTION 3:\n"
        "$$\\frac{c_b V_b}{c_a V_a} = \\frac{n_b}{n_a}$$\n"
        "$$\\frac{c_b (22)}{(0{,}1)(18{,}7)} = \\frac{1}{1} \\implies c_b = 0{,}085\\text{ mol}\\cdot\\text{dm}^{-3}$$\n"
        "$[\\text{NH}_3]\\text{ in }250\\text{ cm}^3 = 0{,}085\\text{ mol}\\cdot\\text{dm}^{-3}$\n\n"
        "$$c_1 V_1 = c_2 V_2$$\n"
        "$$c_1 (0{,}02) = (0{,}085)(0{,}25) \\implies c_1 = 1{,}0625\\text{ mol}\\cdot\\text{dm}^{-3}$$\n\n"
        "$m = cVM = (1{,}0625)(1)(17) = 18{,}06\\text{ g}$\n\n"
        "Marking criteria:\n"
        "(a) Substitute $0{,}1\\text{ mol}\\cdot\\text{dm}^{-3}$ & $18{,}7 \\times 10^{-3}\\text{ dm}^3$. $\\checkmark$\n"
        "(b) Use mole ratio $1 : 1$. $\\checkmark$\n"
        "(c) Calculate $n(\\text{NH}_3) / m(\\text{NH}_3)$ in $250\\text{ cm}^3$: Substitute $0{,}25\\text{ dm}^3$. $\\checkmark$\n"
        "(d) Substitute $0{,}022\\text{ dm}^3$ ($22\\text{ cm}^3$). $\\checkmark$\n"
        "(e) Substitute $0{,}02\\text{ dm}^3$ ($20\\text{ cm}^3$) to calculate mole/mass in initial solution. $\\checkmark$\n"
        "(f) Use $17\\text{ g}\\cdot\\text{mol}^{-1}$ in $n = \\frac{m}{M}$. $\\checkmark$\n"
        "(g) Final answer: $18{,}06\\text{ g}$ (Range: $17\\text{ to }19{,}13\\text{ g}$). $\\checkmark$"
    ),
    final_answer="18.06"
)

add_item(
    q_ref="7.2.4",
    marks=3,
    topic="Acids and Bases - Hydrolysis of Ammonium Ion and pH at Endpoint",
    passage=Q7_2_TITRATION_PASSAGE,
    question="Will the pH of the solution at the end of the titration be GREATER THAN 7, EQUAL TO 7 or LESS THAN 7?\n\nWrite down the relevant equation as motivation for the answer.",
    memo=(
        "Less than 7 / Minder as 7 $\\checkmark$\n\n"
        "Hydrolysis equation:\n"
        "$$\\text{NH}_4^+(\\text{aq}) + \\text{H}_2\\text{O}(\\ell) \\rightleftharpoons \\text{NH}_3(\\text{aq}) + \\text{H}_3\\text{O}^+(\\text{aq})$$\n"
        "(Reactants $\\checkmark$, Products $\\checkmark$)\n\n"
        "Notes:\n"
        "• Ignore single arrow: $\\to$."
    ),
    final_answer="Less than 7"
)

# ==============================================================================
# QUESTION 8
# ==============================================================================

Q8_PASSAGE = (
    "Learners want to identify an unknown metal X using a standard half-cell, $\\text{X}\\mid\\text{X}^{2+}$.\n\n"
    "They set up an electrochemical cell under standard conditions using two half-cells, as shown in the diagram below:\n\n"
    "[DIAGRAM: Galvanic cell | Left half-cell: metal electrode X in $\\text{X}^{2+}(\\text{aq})$ solution; "
    "Right half-cell: standard hydrogen electrode (SHE) with platinum electrode in $\\text{H}^+(\\text{aq})$ solution and $\\text{H}_2(\\text{g})$ gas inlet; "
    "Salt bridge Y connects both beakers; Voltmeter V connects electrode X and the platinum electrode]\n\n"
    "The initial emf of this cell is $1{,}20\\text{ V}$."
)

add_item(
    q_ref="8.1",
    marks=3,
    topic="Electrochemistry - Standard Conditions for Electrochemical Cells",
    passage=Q8_PASSAGE,
    question="State the standard conditions under which this cell functions.",
    memo=(
        "• Pressure: $1\\text{ atmosphere} / 101{,}3\\text{ kPa} / 1{,}013 \\times 10^5\\text{ Pa}$ $\\checkmark$\n"
        "  (Druk: $1\\text{ atmosfeer} / 101{,}3\\text{ kPa} / 1{,}013 \\times 10^5\\text{ Pa}$)\n"
        "• Temperature: $25\\,^\\circ\\text{C} / 298\\text{ K}$ $\\checkmark$\n"
        "  (Temperatuur: $25\\,^\\circ\\text{C} / 298\\text{ K}$)\n"
        "• Concentration of electrolytes: $1\\text{ mol}\\cdot\\text{dm}^{-3}$ $\\checkmark$\n"
        "  (Konsentrasie van elektroliete: $1\\text{ mol}\\cdot\\text{dm}^{-3}$)"
    ),
    final_answer=""
)

add_item(
    q_ref="8.2",
    marks=1,
    topic="Electrochemistry - Function of Salt Bridge",
    passage=Q8_PASSAGE,
    question="State ONE function of component Y.",
    memo=(
        "To maintain electrical neutrality / To complete the circuit / To allow movement of ions between electrolytes $\\checkmark$\n"
        "(Om elektriese neutraliteit te verseker / Om die stroombaan te voltooi / Laat ione toe om tussen elektroliete te beweeg)"
    ),
    final_answer=""
)

Q8_MASS_PASSAGE = (
    Q8_PASSAGE + "\n\n"
    "After the cell has operated for some time, it is found that the mass of electrode X has increased."
)

add_item(
    q_ref="8.3",
    marks=5,
    topic="Electrochemistry - Identification of Unknown Metal from Cell Emf",
    passage=Q8_MASS_PASSAGE,
    question="Identify X by means of a suitable calculation.",
    memo=(
        "OPTION 1:\n"
        "Since the mass of electrode X increased, reduction takes place at electrode X (X is the cathode):\n"
        "$$E^\\circ_{\\text{cell}} = E^\\circ_{\\text{cathode}} - E^\\circ_{\\text{anode}}$$ $\\checkmark$\n"
        "$$1{,}20 = E^\\circ_{\\text{cathode}} - 0{,}00$$ $\\checkmark\\checkmark\\checkmark$\n"
        "$$E^\\circ_{\\text{cathode}} = 1{,}20\\text{ V}$$\n\n"
        "X is $\\text{Pt}$ / platinum $\\checkmark$\n\n"
        "OPTION 2:\n"
        "$$\\text{X}^{2+} + 2\\text{e}^- \\to \\text{X} \\quad (E^\\circ = 1{,}20\\text{ V})$$ $\\checkmark$\n"
        "$$\\text{H}_2 \\to 2\\text{H}^+ + 2\\text{e}^- \\quad (E^\\circ = 0{,}00\\text{ V})$$ $\\checkmark$\n"
        "$$\\text{H}_2 + \\text{X}^{2+} \\to \\text{X} + 2\\text{H}^+ \\quad (E^\\circ_{\\text{cell}} = 1{,}20\\text{ V})$$ $\\checkmark\\checkmark$\n\n"
        "X is $\\text{Pt}$ / platinum $\\checkmark$\n\n"
        "Notes:\n"
        "• Accept any other correct formula from the data sheet.\n"
        "• Any other formula using unconventional abbreviations (e.g. $E^\\circ_{\\text{cell}} = E^\\circ_{\\text{OA}} - E^\\circ_{\\text{RA}}$) followed by correct substitutions: Max 4/5."
    ),
    final_answer="Pt"
)

add_item(
    q_ref="8.4",
    marks=2,
    topic="Electrochemistry - Oxidation Half-Reaction",
    passage=Q8_MASS_PASSAGE,
    question="Write down the oxidation half-reaction that takes place in this cell.",
    memo=(
        "$$\\text{H}_2(\\text{g}) \\to 2\\text{H}^+(\\text{aq}) + 2\\text{e}^-$$ $\\checkmark\\checkmark$\n\n"
        "Marking criteria:\n"
        "• $\\text{H}_2(\\text{g}) \\to 2\\text{H}^+(\\text{aq}) + 2\\text{e}^-$ (2/2)\n"
        "• $2\\text{H}^+(\\text{aq}) + 2\\text{e}^- \\leftarrow \\text{H}_2(\\text{g})$ (2/2)\n"
        "• $\\text{H}_2(\\text{g}) \\rightleftharpoons 2\\text{H}^+(\\text{aq}) + 2\\text{e}^-$ (1/2)\n"
        "• $\\text{H}_2(\\text{g}) \\leftarrow 2\\text{H}^+(\\text{aq}) + 2\\text{e}^-$ (0/2)\n"
        "• $2\\text{H}^+(\\text{aq}) + 2\\text{e}^- \\rightleftharpoons \\text{H}_2(\\text{g})$ (0/2)\n"
        "• Ignore if charge omitted on electron.\n"
        "• If charge (+) omitted on $\\text{H}^+$: Max 1/2."
    ),
    final_answer="H2 -> 2H+ + 2e-"
)

Q8_5_PASSAGE = (
    Q8_MASS_PASSAGE + "\n\n"
    "Half-cell $\\text{X}\\mid\\text{X}^{2+}$ is now replaced by an $\\text{Au}\\mid\\text{Au}^{3+}$ half-cell.\n"
    "The initial emf of the cell is now $1{,}50\\text{ V}$. As the cell operates, the $\\text{Au}$ electrode increases in mass."
)

add_item(
    q_ref="8.5",
    marks=3,
    topic="Electrochemistry - Ranking Oxidising Agents by Strength",
    passage=Q8_5_PASSAGE,
    question="Arrange the oxidising agents, $\\text{X}^{2+}$, $\\text{Au}^{3+}$ and $\\text{H}^+$, in order of increasing strength. Fully explain the answer.",
    memo=(
        "$$\\text{H}^+, \\text{X}^{2+} (\\text{Pt}^{2+}), \\text{Au}^{3+}$$ $\\checkmark$\n\n"
        "Explanation:\n"
        "• $\\text{H}_2$ loses/donates electrons to both $\\text{Au}$ and $\\text{X}/\\text{Pt}$. / $\\text{H}_2$ is the anode / is oxidised in both cells. Therefore $\\text{H}^+$ is the weakest oxidising agent. $\\checkmark$\n"
        "• The reduction potential of $\\text{X}\\mid\\text{X}^{2+}$ is $1{,}20\\text{ V}$ and that of $\\text{Au}\\mid\\text{Au}^{3+}$ is $1{,}50\\text{ V}$. / The reduction potential of $\\text{X}\\mid\\text{X}^{2+}$ is smaller than that of $\\text{Au}\\mid\\text{Au}^{3+}$. / According to the Table of Standard Reduction Potentials $\\text{Au}^{3+}$ is a stronger oxidising agent than $\\text{Pt}^{2+}$. / The cell containing $\\text{Au}$ produces a higher emf than the cell containing $\\text{X}$. $\\checkmark$\n\n"
        "($\\text{H}_2$ verloor/skenk elektrone aan beide $\\text{Au}$ en $\\text{X}/\\text{Pt}$ / $\\text{H}_2$ is die anode/word geoksideer in beide selle. Daarom is $\\text{H}^+$ die swakste oksideermiddel. Die reduksiepotensiaal van $\\text{X}\\mid\\text{X}^{2+}$ is $1{,}20\\text{ V}$ en dié van $\\text{Au}\\mid\\text{Au}^{3+}$ is $1{,}50\\text{ V}$ / kleiner as dié van $\\text{Au}\\mid\\text{Au}^{3+}$.)"
    ),
    final_answer="H+, X2+, Au3+"
)

# ==============================================================================
# QUESTION 9
# ==============================================================================

Q9_PASSAGE = (
    "The simplified electrolytic cell below is used to electroplate a metal spring. "
    "Zinc nitrate, $\\text{Zn}(\\text{NO}_3)_2(\\text{aq})$, is used as an electrolyte and R is an electrode.\n\n"
    "[DIAGRAM: Electrolytic cell | Beaker contains $\\text{Zn}(\\text{NO}_3)_2(\\text{aq})$ electrolyte; "
    "Electrode R on the left and a spiral metal spring electrode on the right are both immersed in the solution; "
    "Both electrodes are connected to an external DC power supply]"
)

add_item(
    q_ref="9.1",
    marks=2,
    topic="Electrochemistry - Electrolytic Cell Definition",
    passage=Q9_PASSAGE,
    question="Define the term electrolytic cell.",
    memo=(
        "A cell in which electrical energy is converted into chemical energy. $\\checkmark\\checkmark$ (2 or 0)\n"
        "('n Sel waar elektriese energie na chemiese energie omgeskakel word. (2 of 0))"
    ),
    final_answer=""
)

add_item(
    q_ref="9.2",
    marks=2,
    topic="Electrochemistry - Identification of Anode in Electroplating",
    passage=Q9_PASSAGE,
    question="Which electrode (R or METAL SPRING) is the ANODE? Give a reason for the answer.",
    memo=(
        "R $\\checkmark$\n"
        "Oxidation takes place. / R loses electrons. / R decreases in mass. $\\checkmark$\n"
        "(Oksidasie vind plaas. / R verloor elektrone. / R se massa sal afneem.)"
    ),
    final_answer="R"
)

add_item(
    q_ref="9.3.1",
    marks=2,
    topic="Electrochemistry - Cathode Half-Reaction in Zinc Electroplating",
    passage=Q9_PASSAGE,
    question="Write down the equation for the half-reaction occurring at the metal spring.",
    memo=(
        "$$\\text{Zn}^{2+}(\\text{aq}) + 2\\text{e}^- \\to \\text{Zn}(\\text{s})$$ $\\checkmark\\checkmark$\n"
        "(Ignore phases)\n\n"
        "Marking criteria:\n"
        "• $\\text{Zn}^{2+}(\\text{aq}) + 2\\text{e}^- \\to \\text{Zn}(\\text{s})$ (2/2)\n"
        "• $\\text{Zn}(\\text{s}) \\leftarrow \\text{Zn}^{2+}(\\text{aq}) + 2\\text{e}^-$ (2/2)\n"
        "• $\\text{Zn}^{2+}(\\text{aq}) + 2\\text{e}^- \\rightleftharpoons \\text{Zn}(\\text{s})$ (1/2)\n"
        "• $\\text{Zn}^{2+}(\\text{aq}) + 2\\text{e}^- \\leftarrow \\text{Zn}(\\text{s})$ (0/2)\n"
        "• $\\text{Zn}(\\text{s}) \\rightleftharpoons \\text{Zn}^{2+}(\\text{aq}) + 2\\text{e}^-$ (0/2)\n"
        "• Ignore if charge omitted on electron.\n"
        "• If charge (+) omitted on $\\text{Zn}^{2+}$: Max 1/2."
    ),
    final_answer="Zn2+ + 2e- -> Zn"
)

add_item(
    q_ref="9.3.2",
    marks=1,
    topic="Electrochemistry - Anode Metal in Electroplating",
    passage=Q9_PASSAGE,
    question="Write down the NAME or FORMULA of a suitable metal that can be used as electrode R.",
    memo="Zinc / Zn / Sink $\\checkmark$",
    final_answer="Zinc"
)

add_item(
    q_ref="9.4",
    marks=2,
    topic="Electrochemistry - Role of Anode in Electroplating",
    passage=Q9_PASSAGE,
    question="Explain the answer to QUESTION 9.3.2.",
    memo=(
        "$\\text{Zn}^{2+}$ ions are reduced / $[\\text{Zn}^{2+}]$ decreases. $\\checkmark$\n"
        "$\\text{Zn}^{2+}$ ions must be replaced by oxidation of the $\\text{Zn}$ electrode. $\\checkmark$\n\n"
        "($\\text{Zn}^{2+}$-ione word gereduseer / $[\\text{Zn}^{2+}]$ neem af. $\\text{Zn}^{2+}$-ione moet vervang word deur oksidasie van Zn-elektrode.)"
    ),
    final_answer=""
)

# ==============================================================================
# VALIDATION & SAVING
# ==============================================================================

print(f"Total items extracted: {len(items)}")
total_marks = sum(item["marks"] for item in items)
print(f"Total marks: {total_marks}")
assert total_marks == 150, f"Expected 150 marks, got {total_marks}"

# Validate each record
for item in items:
    # Check required fields
    for field in ["item_id", "source_id", "pair_source_id", "subject", "grade", "language", "track", "kind", "question_ref", "marks", "topic", "passage", "question", "memo", "final_answer", "needs_review", "licence", "attribution"]:
        assert field in item, f"Missing field {field} in {item['item_id']}"
    
    # Check dollar balance in text fields
    for field in ["passage", "question", "memo"]:
        text = item[field]
        # Count unescaped dollar signs
        dollars = re.findall(r'(?<!\\)\$', text)
        assert len(dollars) % 2 == 0, f"Unbalanced dollars in {item['item_id']} field {field}: {len(dollars)} dollars found!"
    
    # Check degree Celsius
    for field in ["passage", "question", "memo"]:
        text = item[field]
        assert r"\text{^\circ" not in text, f"Illegal degree Celsius syntax in {item['item_id']} {field}"

print("All validation checks passed!")

# Save to the 4 paths
target_paths = [
    "workspace/items/physical_sciences/dbe-physical_sciences-g12-p2-2023-may.jsonl",
    "workspace/items/dbe-physical_sciences-g12-p2-2023-may.jsonl",
    "sa-tutor-kit/sa-tutor-kit/workspace/items/physical_sciences/dbe-physical_sciences-g12-p2-2023-may.jsonl",
    "sa-tutor-kit/sa-tutor-kit/workspace/items/dbe-physical_sciences-g12-p2-2023-may.jsonl"
]

for p in target_paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"Saved {len(items)} items to {p}")
