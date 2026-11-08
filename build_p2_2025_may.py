import json
import os
import re

SOURCE_ID = "dbe-physical_sciences-g12-p2-2025-may"
PAIR_SOURCE_ID = "dbe-physical_sciences-g12-p2-2025-may-memo"
SUBJECT = "physical_sciences"
GRADE = 12
LANGUAGE = "en"
TRACK = "sciences"
LICENCE = "DBE copyright - check terms"
ATTRIBUTION = "Department of Basic Education"

items = []

def add_item(qref, marks, topic, passage, question, memo, final_answer, kind="question", needs_review=False):
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
        "needs_review": needs_review,
        "licence": LICENCE,
        "attribution": ATTRIBUTION
    }
    items.append(item)

# ==========================================
# QUESTION 1: MULTIPLE-CHOICE (20 MARKS)
# ==========================================

add_item(
    qref="1.1",
    marks=2,
    topic="Intermolecular Forces - Van der Waals Forces",
    passage="",
    question="How many types of Van der Waals forces are present between the molecules of $\\text{CH}_3\\text{CH}_2\\text{Br}$?\n\nA 1\nB 2\nC 3\nD 4",
    memo="B $\\checkmark\\checkmark$ (ACCEPT: 2)\n\n*Rationale: Bromoethane ($\\text{CH}_3\\text{CH}_2\\text{Br}$) is a polar haloalkane. Between its molecules, two types of Van der Waals forces are present: London forces (dispersion forces) and dipole-dipole forces.*",
    final_answer="B"
)

add_item(
    qref="1.2",
    marks=2,
    topic="Organic Chemistry - IUPAC Naming & Formulae",
    passage="",
    question="Which ONE of the following is the CORRECT formula of methylbutanone?\n\nA $\\text{CH}_3\\text{CH(OH)CH(CH}_3\\text{)CH}_3$\nB $\\text{HCOOCH(CH}_3\\text{)CH}_2\\text{CH}_3$\nC $\\text{CH}_3\\text{CH}_2\\text{CH(CH}_3\\text{)CHO}$\nD $\\text{CH}_3\\text{COCH(CH}_3\\text{)CH}_3$",
    memo="D $\\checkmark\\checkmark$\n\n*Rationale: Methylbutanone (3-methylbutan-2-one) is a ketone containing a carbonyl group ($-\\text{C}(=\\text{O})-$) on carbon 2 and a methyl branch on carbon 3 of a butane chain, giving the condensed formula $\\text{CH}_3\\text{COCH(CH}_3)\\text{CH}_3$. Option A is an alcohol, option B is an ester, and option C is an aldehyde.*",
    final_answer="D"
)

add_item(
    qref="1.3",
    marks=2,
    topic="Organic Chemistry - Reactions (Cracking)",
    passage="",
    question="A compound $\\text{CH}_3(\\text{CH}_2)_5\\text{CH}_3$ undergoes the following reaction:\n$$\\text{CH}_3(\\text{CH}_2)_5\\text{CH}_3 \\rightarrow \\text{R} + \\text{CH}_3(\\text{CH}_2)_2\\text{CH}_3$$\n\nWhich ONE of the following combinations CORRECTLY describes the type of reaction and the IUPAC name of compound R?\n\n| | TYPE OF REACTION | IUPAC NAME |\n|---|---|---|\n| A | Elimination | Propane |\n| B | Addition | Propene |\n| C | Cracking | Propane |\n| D | Cracking | Propene |",
    memo="D $\\checkmark\\checkmark$\n\n*Rationale: Heptane ($\\text{C}_7\\text{H}_{16}$) undergoes cracking to break into a shorter alkane (butane, $\\text{C}_4\\text{H}_{10}$) and an alkene. By conservation of atoms: $\\text{C}_7\\text{H}_{16} \\rightarrow \\text{C}_3\\text{H}_6 + \\text{C}_4\\text{H}_{10}$. Thus, compound R is the alkene propene ($\\text{C}_3\\text{H}_6$), and the reaction type is cracking.*",
    final_answer="D"
)

add_item(
    qref="1.4",
    marks=2,
    topic="Reaction Rate - Concentration & Collision Theory",
    passage="[DIAGRAM: Four closed reaction containers A, B, C, and D are shown at the same temperature containing gas molecules of two reactant gases (represented by black circles and white circles):\n* Container A: Volume $V_1 = 5\\text{ cm}^3$, containing 14 reactant molecules (6 black, 8 white).\n* Container B: Volume $V_2 = 5\\text{ cm}^3$, containing 10 reactant molecules (4 black, 6 white).\n* Container C: Volume $V_3 = 10\\text{ cm}^3$, containing 15 reactant molecules (6 black, 9 white).\n* Container D: Volume $V_4 = 20\\text{ cm}^3$, containing 27 reactant molecules (12 black, 15 white).]",
    question="Two gases are added into each of four empty containers at the same temperature. The diagrams below show the molecules of the gases and the volumes of the containers at the start of the reaction.\n\nIn which ONE of the following containers is the initial reaction rate the highest?\n\nA A\nB B\nC C\nD D",
    memo="A $\\checkmark\\checkmark$\n\n*Rationale: Reaction rate is directly proportional to reactant concentration (number of particles per unit volume). Container A has volume $V_1 = 5\\text{ cm}^3$ and 14 reactant molecules (concentration = $14 / 5 = 2{,}8\\text{ particles/cm}^3$), which is higher than B ($2{,}0$), C ($1{,}5$), and D ($1{,}35$). The highest concentration yields the highest frequency of effective collisions, resulting in the highest initial reaction rate.*",
    final_answer="A"
)

add_item(
    qref="1.5",
    marks=2,
    topic="Chemical Equilibrium - Catalysts",
    passage="",
    question="Which ONE of the following statements is TRUE for the effect of a catalyst on a reaction at equilibrium?\n\nA The equilibrium constant increases.\nB The rate of the reverse reaction increases.\nC The activation energy for the reverse reaction increases.\nD The enthalpy change, $\\Delta H$, for the forward reaction decreases.",
    memo="B $\\checkmark\\checkmark$\n\n*Rationale: A catalyst increases the rates of both the forward and reverse reactions equally by providing an alternative reaction pathway with lower activation energy. It has no effect on the equilibrium constant ($K_c$) or the enthalpy change ($\\Delta H$).*",
    final_answer="B"
)

add_item(
    qref="1.6",
    marks=2,
    topic="Chemical Equilibrium - Le Chatelier's Principle & Temperature",
    passage="",
    question="Carbonyl chloride gas, $\\text{COCl}_2(\\text{g})$, decomposes in a closed container and reaches equilibrium according to the following equation:\n$$\\text{COCl}_2(\\text{g}) \\rightleftharpoons \\text{CO}(\\text{g}) + \\text{Cl}_2(\\text{g}) \\quad \\Delta H > 0$$\n\nConsider the following statements.\nAn increase in temperature will:\n(i) Favour the reverse reaction\n(ii) Increase the concentration of the products\n(iii) Increase the equilibrium constant\n\nWhich of the statements above are TRUE?\n\nA (i) and (ii) only\nB (i) and (iii) only\nC (ii) and (iii) only\nD (i), (ii) and (iii)",
    memo="C $\\checkmark\\checkmark$\n\n*Rationale: Since $\\Delta H > 0$, the forward reaction is endothermic. According to Le Chatelier's principle, an increase in temperature favours the endothermic forward reaction. This increases the concentration of the products ($[\\text{CO}]$ and $[\\text{Cl}_2]$), which in turn increases the equilibrium constant ($K_c = \\frac{[\\text{CO}][\\text{Cl}_2]}{[\\text{COCl}_2]}$). Therefore, statements (ii) and (iii) are true.*",
    final_answer="C"
)

add_item(
    qref="1.7",
    marks=2,
    topic="Acids and Bases - Lowry-Brønsted Theory / Conjugate Acid-Base Pairs",
    passage="",
    question="Consider the equation for the acid-base reaction below.\n$$\\text{HSO}_4^-(\\text{aq}) + \\text{NH}_3(\\text{aq}) \\rightleftharpoons \\text{SO}_4^{2-}(\\text{aq}) + \\text{NH}_4^+(\\text{aq})$$\n\nThe two acids in this reaction are ...\n\nA $\\text{NH}_3(\\text{aq})$ and $\\text{NH}_4^+(\\text{aq})$\nB $\\text{HSO}_4^-(\\text{aq})$ and $\\text{SO}_4^{2-}(\\text{aq})$\nC $\\text{HSO}_4^-(\\text{aq})$ and $\\text{NH}_3(\\text{aq})$\nD $\\text{HSO}_4^-(\\text{aq})$ and $\\text{NH}_4^+(\\text{aq})$",
    memo="D $\\checkmark\\checkmark$\n\n*Rationale: According to the Lowry-Brønsted definition, an acid is a proton ($\\text{H}^+$) donor. In the forward reaction, $\\text{HSO}_4^-$ donates a proton to $\\text{NH}_3$, acting as an acid. In the reverse reaction, $\\text{NH}_4^+$ donates a proton to $\\text{SO}_4^{2-}$, acting as an acid. Thus, the two acids are $\\text{HSO}_4^-(\\text{aq})$ and $\\text{NH}_4^+(\\text{aq})$.*",
    final_answer="D"
)

add_item(
    qref="1.8",
    marks=2,
    topic="Acids and Bases - Strength of Acids & Electrical Conductivity",
    passage="[DIAGRAM: Two separate electrical conductivity circuits at $25\\,^\\circ\\text{C}$:\n* Circuit A: DC power supply connected in series with light bulb A and two inert carbon electrodes immersed in $1\\text{ mol}\\cdot\\text{dm}^{-3}$ nitric acid solution, $\\text{HNO}_3(\\text{aq})$.\n* Circuit B: Identical DC power supply connected in series with light bulb B and two inert carbon electrodes immersed in $1\\text{ mol}\\cdot\\text{dm}^{-3}$ ethanoic acid solution, $\\text{CH}_3\\text{COOH}(\\text{aq})$.]",
    question="The conductivity of two acids, $\\text{HNO}_3(\\text{aq})$ and $\\text{CH}_3\\text{COOH}(\\text{aq})$, each with a concentration of $1\\text{ mol}\\cdot\\text{dm}^{-3}$, is compared at $25\\,^\\circ\\text{C}$. The simplified diagrams below show the apparatus used. The electrodes are made of carbon.\n\nWhich ONE of the following combinations CORRECTLY describes the brightness of bulb A and bulb B, and provides the reason for this?\n\n| | BRIGHTNESS OF BULBS | REASON |\n|---|---|---|\n| A | A is brighter than B | $\\text{CH}_3\\text{COOH}$ is the stronger acid |\n| B | A is brighter than B | $\\text{HNO}_3$ is the stronger acid |\n| C | B is brighter than A | $\\text{CH}_3\\text{COOH}$ is the weaker acid |\n| D | A and B have equal brightness | Acids are of equal concentration |",
    memo="B $\\checkmark\\checkmark$\n\n*Rationale: Nitric acid ($\\text{HNO}_3$) is a strong acid that ionises completely in aqueous solution, resulting in a high concentration of free mobile ions and high electrical conductivity. Ethanoic acid ($\\text{CH}_3\\text{COOH}$) is a weak acid that ionises only partially, resulting in a low concentration of ions and low conductivity. Therefore, bulb A is brighter than bulb B because $\\text{HNO}_3$ is the stronger acid.*",
    final_answer="B"
)

add_item(
    qref="1.9",
    marks=2,
    topic="Electrochemistry - Standard Hydrogen Half-cell",
    passage="",
    question="Which ONE of the following combinations of temperature and pressure is CORRECT for the standard hydrogen half-cell?\n\n| | TEMPERATURE ($^\\circ\\text{C}$) | PRESSURE ($\\text{kPa}$) |\n|---|---|---|\n| A | 0 | 273 |\n| B | 25 | 273 |\n| C | 25 | 101{,}3 |\n| D | 0 | 101{,}3 |",
    memo="C $\\checkmark\\checkmark$\n\n*Rationale: Standard conditions for electrochemical measurements (including the standard hydrogen electrode) are a temperature of $25\\,^\\circ\\text{C}$ ($298\\text{ K}$) and a gas pressure of $101{,}3\\text{ kPa}$ ($1\\text{ atm}$), along with a solution concentration of $1\\text{ mol}\\cdot\\text{dm}^{-3}$.*",
    final_answer="C"
)

add_item(
    qref="1.10",
    marks=2,
    topic="Electrochemistry - Electrolytic Cells / Refining of Copper",
    passage="",
    question="Impure copper is refined in an electrolytic cell. Which ONE of the following combinations CORRECTLY identifies the anode and the electrolyte for this cell?\n\n| | ANODE | ELECTROLYTE |\n|---|---|---|\n| A | Pure copper | $\\text{Cu(NO}_3)_2(\\text{aq})$ |\n| B | Pure copper | $\\text{AgNO}_3(\\text{aq})$ |\n| C | Impure copper | $\\text{Cu(NO}_3)_2(\\text{aq})$ |\n| D | Impure copper | $\\text{AgNO}_3(\\text{aq})$ |",
    memo="C $\\checkmark\\checkmark$\n\n*Rationale: In the electro-refining of copper, the impure copper is placed as the anode (positive electrode where oxidation $\\text{Cu}(\\text{s}) \\rightarrow \\text{Cu}^{2+}(\\text{aq}) + 2\\text{e}^-$ occurs). The electrolyte must contain copper(II) ions, such as $\\text{Cu(NO}_3)_2(\\text{aq})$ or $\\text{CuSO}_4(\\text{aq})$. Pure copper deposits at the cathode.*",
    final_answer="C"
)

# ==========================================
# QUESTION 2: ORGANIC MOLECULES (19 MARKS)
# ==========================================

PASSAGE_Q2 = """The letters **A** to **F** in the table below represent organic compounds.

| | | | |
|---|---|---|---|
| **A** | $\\text{C}_5\\text{H}_{10}\\text{O}$ | **B** | [DIAGRAM: Structural formula of 3-ethyl-4-iodohexane: a 6-carbon parent chain with an ethyl group ($-\\text{CH}_2\\text{CH}_3$) at carbon 3 and an iodo substituent ($-\\text{I}$) at carbon 4: $\\text{CH}_3-\\text{CH}_2-\\text{CH(CH}_2\\text{CH}_3)-\\text{CH(I)}-\\text{CH}_2-\\text{CH}_3$] |
| **C** | Butanoic acid | **D** | $(\\text{CH}_3)_3\\text{COH}$ |
| **E** | $\\text{CH}_2\\text{C(CH}_3)_2$ | **F** | $\\text{HCOOCH}_2\\text{CH}_2\\text{CH}_3$ |"""

add_item(
    qref="2.1",
    marks=2,
    topic="Organic Chemistry - Definitions (Unsaturated Compound)",
    passage=PASSAGE_Q2,
    question="Define the term *unsaturated compound*.",
    memo="Compounds with one or more multiple bonds between C atoms in the hydrocarbon chain. $\\checkmark\\checkmark$ *(2 or 0)*\n\n**OR/OF**\nA hydrocarbon with two or more bonds between the C-atoms.\n\n**OR/OF**\nHydrocarbons containing not only single bonds between C atoms.\n\n**ACCEPT/AANVAAR:**\nCompounds with one or more double/triple bonds between C atoms in the hydrocarbon chain. *(2)*",
    final_answer="Compounds with one or more multiple bonds between C atoms in the hydrocarbon chain."
)

add_item(
    qref="2.2.1",
    marks=1,
    topic="Organic Chemistry - Identification (Unsaturated Compound)",
    passage=PASSAGE_Q2,
    question="Write down the LETTER that represents an unsaturated compound.",
    memo="E $\\checkmark$ *(1)*",
    final_answer="E"
)

add_item(
    qref="2.2.2",
    marks=1,
    topic="Organic Chemistry - Functional Isomers",
    passage=PASSAGE_Q2,
    question="Write down the LETTER that represents a functional isomer of compound **C**.",
    memo="F $\\checkmark$ *(1)*\n\n*Rationale: Compound C is butanoic acid (a carboxylic acid, $\\text{C}_4\\text{H}_8\\text{O}_2$) and compound F is propyl methanoate (an ester, $\\text{C}_4\\text{H}_8\\text{O}_2$). Carboxylic acids and esters are functional isomers.*",
    final_answer="F"
)

add_item(
    qref="2.3",
    marks=2,
    topic="Organic Chemistry - Homologous Series",
    passage=PASSAGE_Q2,
    question="Name the TWO homologous series to which **A** belongs.",
    memo="Ketones $\\checkmark$\nAldehydes $\\checkmark$ *(2)*\n\n*(Accept: Ketone / Aldehyde / Ketone and aldehyde)*",
    final_answer="Ketones and Aldehydes"
)

add_item(
    qref="2.4",
    marks=2,
    topic="Organic Chemistry - Classification of Alcohols",
    passage=PASSAGE_Q2,
    question="Is compound **D** a PRIMARY, SECONDARY or TERTIARY alcohol? Give a reason for the answer.",
    memo="Tertiary $\\checkmark$\n\nThe hydroxyl group/functional group ($-\\text{OH}$) is bonded to a C atom that is bonded to three other C atoms. $\\checkmark$\n\n**OR/OF**\nThe functional group ($-\\text{C-OH}$) is bonded to three other C atoms. *(2)*",
    final_answer="Tertiary. The hydroxyl group is bonded to a carbon atom that is bonded to three other carbon atoms."
)

add_item(
    qref="2.5.1",
    marks=3,
    topic="Organic Chemistry - IUPAC Naming",
    passage=PASSAGE_Q2,
    question="Write down the IUPAC name of compound **B**.",
    memo="**Marking criteria:**\n* Correct stem, i.e. hexane. $\\checkmark$\n* Both substituents (ethyl and iodo) correctly identified. $\\checkmark$\n* IUPAC name completely correct including numbering, sequence, hyphens and commas. $\\checkmark$\n\n3-ethyl-4-iodohexane $\\checkmark\\checkmark\\checkmark$ *(3)*",
    final_answer="3-ethyl-4-iodohexane"
)

add_item(
    qref="2.5.2",
    marks=2,
    topic="Organic Chemistry - IUPAC Naming (Positional Isomer)",
    passage=PASSAGE_Q2,
    question="Write down the IUPAC name of the POSITIONAL isomer of compound **D**.",
    memo="**Marking criteria:**\n* Correct stem and substituents: methyl and propanol $\\checkmark$\n* IUPAC name completely correct including numbering, sequence, hyphens and commas. $\\checkmark$\n\n2-methylpropan-1-ol / 2-methyl-1-propanol / methylpropan-1-ol / methyl-1-propanol $\\checkmark\\checkmark$ *(2)*",
    final_answer="2-methylpropan-1-ol"
)

add_item(
    qref="2.6.1",
    marks=1,
    topic="Organic Chemistry - Reactions (Esterification)",
    passage=PASSAGE_Q2,
    question="Ethanol reacts with compound **C** to form an organic compound **Z**.\n\nWrite down the type of reaction.",
    memo="Esterification / Condensation $\\checkmark$ *(1)*",
    final_answer="Esterification"
)

add_item(
    qref="2.6.2",
    marks=2,
    topic="Organic Chemistry - Structural Formula (Ethyl butanoate)",
    passage=PASSAGE_Q2,
    question="Ethanol reacts with compound **C** to form an organic compound **Z**.\n\nWrite down the STRUCTURAL FORMULA of compound **Z**.",
    memo="**Marking criteria:**\n* Functional group correct ($-\\text{COO}-$). $\\checkmark$\n* Whole structure correct (ethyl butanoate). $\\checkmark$\n\nStructural representation:\n$$\\text{CH}_3\\text{CH}_2\\text{CH}_2-\\text{C}(=\\text{O})-\\text{O}-\\text{CH}_2\\text{CH}_3$$\nAll bonds showing: 4 carbons on acyl part, carbonyl oxygen double-bonded to carbon 4, bridging single-bonded oxygen to ethyl group (2 carbons), all hydrogens explicit.\n\n**IF/INDIEN:**\n* More than one functional group / wrong functional group: $0/2$\n* If condensed structural formulae used: Max. $1/2$ *(2)*",
    final_answer="CH3CH2CH2COOCH2CH3"
)

add_item(
    qref="2.7.1",
    marks=1,
    topic="Organic Chemistry - Empirical Formula",
    passage=PASSAGE_Q2,
    question="Write down the empirical formula of compound **F**.",
    memo="$\\text{C}_2\\text{H}_4\\text{O} \\checkmark$ *(1)*\n\n*Working: Molecular formula of compound F (propyl methanoate, $\\text{HCOOCH}_2\\text{CH}_2\\text{CH}_3$) is $\\text{C}_4\\text{H}_8\\text{O}_2$. Dividing the subscripts by 2 yields the simplest whole number ratio: $\\text{C}_2\\text{H}_4\\text{O}$.*",
    final_answer="C2H4O"
)

add_item(
    qref="2.7.2",
    marks=2,
    topic="Organic Chemistry - Structural Formula (Chain Isomer)",
    passage=PASSAGE_Q2,
    question="Write down the STRUCTURAL FORMULA of the CHAIN ISOMER of compound **E**.",
    memo="**Marking criteria:**\n* Correct functional group (carbon-carbon double bond). $\\checkmark$\n* Whole structure correct (straight chain of 4 carbons: but-1-ene or but-2-ene). $\\checkmark$\n\n**But-1-ene:**\n$$\\text{CH}_2=\\text{CH}-\\text{CH}_2-\\text{CH}_3$$\n*or*\n**But-2-ene:**\n$$\\text{CH}_3-\\text{CH}=\\text{CH}-\\text{CH}_3$$\n*(with all bonds between atoms explicitly shown in structural formula)*\n\n**IF/INDIEN:**\n* More than one functional group / wrong functional group: $0/2$\n* If condensed structural formulae used: Max. $1/2$ *(2)*",
    final_answer="CH2=CH-CH2-CH3 or CH3-CH=CH-CH3"
)

# ==========================================
# QUESTION 3: PHYSICAL PROPERTIES (14 MARKS)
# ==========================================

PASSAGE_Q3_1 = """3.1 The boiling points of straight chain aldehydes and straight chain carboxylic acids are compared. The table below shows the results obtained.

| INVESTIGATION 1 | INVESTIGATION 2 |
| :---: | :---: |
| Number of carbon atoms in the compound | Boiling point of aldehydes ($^\\circ\\text{C}$) | Boiling point of carboxylic acids ($^\\circ\\text{C}$) |
| 1 | -19 | 101 |
| 2 | 20 | 118 |
| 3 | 49 | 141 |
| 4 | 75 | 164 |"""

add_item(
    qref="3.1.1",
    marks=2,
    topic="Organic Chemistry - Definitions (Homologous Series)",
    passage=PASSAGE_Q3_1,
    question="Define the term *homologous series*.",
    memo="(A series of organic) compounds that can be described by the same general formula. $\\checkmark\\checkmark$ *(2 or 0)*\n\n**OR**\n(A series of organic) compounds in which one member differs from the next by a $\\text{CH}_2$ group. *(2)*",
    final_answer="A series of organic compounds that can be described by the same general formula."
)

add_item(
    qref="3.1.2a",
    marks=1,
    topic="Organic Chemistry - Functional Groups (Aldehydes)",
    passage=PASSAGE_Q3_1,
    question="Write down the NAME of the FUNCTIONAL GROUP of the aldehydes.",
    memo="Formyl (group) $\\checkmark$ *(1)*",
    final_answer="Formyl group"
)

add_item(
    qref="3.1.2b",
    marks=2,
    topic="Physical Properties - Vapour Pressure (Methanal)",
    passage=PASSAGE_Q3_1,
    question="Write down the IUPAC NAME of the compound with the highest vapour pressure in this comparison.",
    memo="**Marking criteria:**\n* Correct chain length, i.e. Meth. $\\checkmark$\n* Everything else correct. $\\checkmark$\n\nMethanal $\\checkmark\\checkmark$ *(2)*\n\n*Rationale: Vapour pressure is inversely related to boiling point. The compound with the lowest boiling point ($-19\\,^\\circ\\text{C}$) has the weakest intermolecular forces and therefore the highest vapour pressure.*",
    final_answer="Methanal"
)

add_item(
    qref="3.1.3a",
    marks=1,
    topic="Physical Properties - Variables (Controlled Variable)",
    passage=PASSAGE_Q3_1,
    question="For INVESTIGATION 2:\nWrite down the controlled variable.",
    memo="**ANY ONE:**\n* Homologous series / Functional group $\\checkmark$\n* Type of intermolecular forces $\\checkmark$\n* Straight chain (unbranched) structure $\\checkmark$\n* Atmospheric pressure $\\checkmark$ *(1)*",
    final_answer="Homologous series"
)

add_item(
    qref="3.1.3b",
    marks=1,
    topic="Physical Properties - Boiling Point Trend",
    passage=PASSAGE_Q3_1,
    question="For INVESTIGATION 2:\nDescribe the trend in the boiling points.",
    memo="The boiling points of the carboxylic acids increase with an increase in the chain length / number of carbon atoms / surface area / molecular mass. $\\checkmark$\n\n**OR**\nThe boiling points of the carboxylic acids decrease with a decrease in the chain length / number of carbon atoms / surface area / molecular mass. *(1)*",
    final_answer="The boiling points of the carboxylic acids increase with an increase in chain length."
)

add_item(
    qref="3.1.3c",
    marks=2,
    topic="Physical Properties - Explanation of Boiling Point Trend",
    passage=PASSAGE_Q3_1,
    question="For INVESTIGATION 2:\nFully explain the answer to QUESTION 3.1.3(b).",
    memo="**Marking criteria:**\n* Compare the strength of intermolecular forces: As the number of C atoms / chain length / surface area / contact area / molecular mass increases, the strength of intermolecular forces (London / dispersion forces) increases. $\\checkmark$\n* Compare the energy required: More energy is needed to overcome intermolecular forces / London forces. $\\checkmark$\n\n**OR**\n* As the number of C atoms / chain length decreases, the strength of intermolecular forces decreases. $\\checkmark$\n* Less energy is needed to overcome intermolecular forces. $\\checkmark$ *(2)*",
    final_answer="As chain length increases, intermolecular forces become stronger, requiring more energy to overcome."
)

add_item(
    qref="3.1.4",
    marks=1,
    topic="Physical Properties - Boiling Point Reading (Butanal)",
    passage=PASSAGE_Q3_1,
    question="Write down the boiling point of butanal.",
    memo="$75\\,^\\circ\\text{C} \\checkmark$ *(1)*\n\n*(Unit not required, but if given must be correct: $75\\,^\\circ\\text{C}$)*",
    final_answer="75 °C"
)

PASSAGE_Q3_2 = """3.2 The vapour pressures of compounds **A** and **B** are compared.
* **A:** $\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}_2\\text{CH}_2\\text{OH}$
* **B:** $\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{COOH}$"""

add_item(
    qref="3.2",
    marks=4,
    topic="Physical Properties - Intermolecular Forces & Vapour Pressure Comparison",
    passage=PASSAGE_Q3_2,
    question="How does the vapour pressure of compound **A** compare to that of compound **B**? Choose from HIGHER THAN, LOWER THAN or EQUAL TO.\n\nFully explain the answer.",
    memo="**Marking criteria:**\n* Higher than $\\checkmark$\n* State that carboxylic acids have more than one (two) sites for hydrogen bonding and alcohols have one site for hydrogen bonding (in addition to London and dipole-dipole forces). $\\checkmark$\n* Comparing the strength of IMFs: Intermolecular forces in compound B (carboxylic acid / butanoic acid) are stronger than in compound A (alcohol / pentan-1-ol), OR intermolecular forces in compound A are weaker. $\\checkmark$\n* Comparing energy / vapour phase: More energy is needed to overcome/break intermolecular forces in compound B than in compound A, OR at a given temperature there will be fewer molecules of compound B in the vapour phase than compound A (more molecules of compound A in vapour phase). $\\checkmark$\n\n**Summary:**\n* Higher than $\\checkmark$\n* Compound B ($\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{COOH}$ / butanoic acid) has two sites for hydrogen bonding between molecules, while compound A ($\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}_2\\text{CH}_2\\text{OH}$ / pentan-1-ol) has one site for hydrogen bonding between molecules. $\\checkmark$\n* The intermolecular forces in compound B are stronger than in compound A (or in compound A are weaker than in compound B). $\\checkmark$\n* More energy is needed to overcome the intermolecular forces in compound B (or at a given temperature there are more molecules of compound A in the vapour phase). $\\checkmark$ *(4)*",
    final_answer="HIGHER THAN"
)

# ==========================================
# QUESTION 4: ORGANIC REACTIONS (17 MARKS)
# ==========================================

PASSAGE_Q4 = """In the flow diagram below, a primary alcohol **P** is used as a starting reactant to form different organic compounds under different reaction conditions.

[DIAGRAM: Flow diagram showing reaction pathways starting from Compound P:
* Compound P (Primary alcohol) undergoes Reaction I (Elimination) to form Compound Q.
* Compound Q undergoes Reaction II (Addition) to form Butane ($\text{CH}_3\text{CH}_2\text{CH}_2\text{CH}_3$).
* Compound Q reacts with $\text{H}_2\text{O}$ via Reaction III (Addition) to form Compound S (major product).]"""

add_item(
    qref="4.1.1",
    marks=1,
    topic="Organic Reactions - Addition Reaction (Hydrogenation)",
    passage=PASSAGE_Q4,
    question="Write down the TYPE of addition reaction represented by reaction II.",
    memo="Hydrogenation $\\checkmark$ *(1)*",
    final_answer="Hydrogenation"
)

add_item(
    qref="4.1.2",
    marks=1,
    topic="Organic Reactions - Elimination Reaction (Dehydration)",
    passage=PASSAGE_Q4,
    question="Write down the TYPE of elimination reaction represented by reaction I.",
    memo="Dehydration $\\checkmark$ *(1)*",
    final_answer="Dehydration"
)

add_item(
    qref="4.2",
    marks=2,
    topic="Organic Reactions - IUPAC Naming (Butan-1-ol)",
    passage=PASSAGE_Q4,
    question="Write down the IUPAC name of compound **P**.",
    memo="**Marking criteria:**\n* Correct chain length, i.e. But. $\\checkmark$\n* Everything else correct: IUPAC name completely correct including numbering. $\\checkmark$\n\nButan-1-ol / 1-butanol $\\checkmark\\checkmark$ *(2)*",
    final_answer="butan-1-ol"
)

add_item(
    qref="4.3.1",
    marks=4,
    topic="Organic Reactions - Reaction Equations (Hydration of but-1-ene)",
    passage=PASSAGE_Q4,
    question="Consider reaction III.\n\nWrite down the balanced equation using CONDENSED structural formulae.",
    memo="**Marking criteria:**\n* Whole condensed structural formula of alkene correct (but-1-ene). $\\checkmark$\n* $\\text{H}_2\\text{O}$. $\\checkmark$\n* Hydroxyl group / OH. $\\checkmark$\n* Whole condensed structural formula of alcohol correct (OH on second C-atom, butan-2-ol). $\\checkmark$\n\n$$\\text{CH}_2\\text{CHCH}_2\\text{CH}_3 \\checkmark + \\text{H}_2\\text{O} \\checkmark \\rightarrow \\text{CH}_3\\text{CHOHCH}_2\\text{CH}_3 \\checkmark$$\n**OR/OF**\n$$\\text{CH}_2=\\text{CHCH}_2\\text{CH}_3 \\checkmark + \\text{H}_2\\text{O} \\checkmark \\rightarrow \\text{CH}_3\\text{CH(OH)CH}_2\\text{CH}_3 \\checkmark$$\n\n**IF/INDIEN:**\n* Any additional reactants or products: Deduct 1 mark.\n* Structural formulae used: Max. $3/4$\n* Molecular formulae used: Max. $1/4$\n* Only reactants without arrow: Max. $2/4$ *(4)*",
    final_answer="CH2=CHCH2CH3 + H2O -> CH3CH(OH)CH2CH3"
)

add_item(
    qref="4.3.2",
    marks=1,
    topic="Organic Reactions - Reaction Conditions / Catalyst",
    passage=PASSAGE_Q4,
    question="Consider reaction III.\n\nWrite down the NAME or FORMULA of a suitable catalyst.",
    memo="Sulphuric acid / $\\text{H}_2\\text{SO}_4$ / Phosphoric acid / $\\text{H}_3\\text{PO}_4$ $\\checkmark$ *(1)*",
    final_answer="H2SO4"
)

add_item(
    qref="4.4",
    marks=5,
    topic="Organic Reactions - Two-Step Conversion of Butane to Butan-1-ol",
    passage=PASSAGE_Q4,
    question="Butane can be converted to compound **P** in a TWO-STEP reaction. Use STRUCTURAL FORMULAE and write down the balanced equations for these TWO reactions.",
    memo="**Marking criteria:**\n* $\\text{X}_2 = \\text{Br}_2 / \\text{Cl}_2$. $\\checkmark$\n* Whole structural formula of 1-halobutane correct. $\\checkmark$\n* $\\text{H}_2\\text{O} / \\text{NaOH} / \\text{KOH} / \\text{LiOH}$. $\\checkmark$\n* Whole structural formula of alcohol correct (butan-1-ol). $\\checkmark$\n* $\\text{HX} / \\text{NaX} / \\text{KX} / \\text{LiX}$ where $\\text{X} = \\text{Br} / \\text{Cl}$. $\\checkmark$\n\n**Step 1 (Halogenation / Free radical substitution):**\n$$\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}_3 + \\text{X}_2 \\xrightarrow{\\text{uv/heat}} \\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}_2\\text{X} + \\text{HX}$$\n*(drawn as full structural formulae showing all bonds)*\n\n**Step 2 (Hydrolysis / Nucleophilic substitution):**\n$$\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}_2\\text{X} + \\text{NaOH} \\xrightarrow{\\text{mild heat}} \\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}_2\\text{OH} + \\text{NaX}$$\n**OR/OF**\n$$\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}_2\\text{X} + \\text{H}_2\\text{O} \\xrightarrow{\\text{mild heat}} \\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}_2\\text{OH} + \\text{HX}$$\n*(drawn as full structural formulae showing all bonds)*\n\n**IF/INDIEN:**\n* Any additional reactants or products: Max. $4/5$\n* Condensed structural formulae used: Deduct 1 mark.\n* If inorganic product does not correspond with inorganic reactant: No mark for inorganic product.\n* Molecular formulae used: Max. $3/5$ *(5)*",
    final_answer="Step 1: CH3CH2CH2CH3 + Br2 -> CH3CH2CH2CH2Br + HBr; Step 2: CH3CH2CH2CH2Br + NaOH -> CH3CH2CH2CH2OH + NaBr"
)

add_item(
    qref="4.5",
    marks=3,
    topic="Organic Reactions - Combustion of Butane",
    passage=PASSAGE_Q4,
    question="Write down a balanced equation using MOLECULAR FORMULAE for the complete combustion of butane.",
    memo="$$2\\text{C}_4\\text{H}_{10} \\checkmark + 13\\text{O}_2 \\rightarrow 8\\text{CO}_2 + 10\\text{H}_2\\text{O} \\checkmark \\quad \\text{Bal.} \\checkmark$$\n\nIgnore phases.\n**Marking criteria:**\n* $\\text{C}_4\\text{H}_{10} \\checkmark$\n* $\\text{O}_2$, $\\text{CO}_2$ and $\\text{H}_2\\text{O} \\checkmark$\n* Balancing $\\checkmark$\n* Ignore double arrows.\n\n**IF/INDIEN:**\n* Structural formulae $\\text{C}_4\\text{H}_{10}$ used: Max. $2/3$\n* Balancing mark only if everything else is correct. *(3)*",
    final_answer="2C4H10 + 13O2 -> 8CO2 + 10H2O"
)

# ==========================================
# QUESTION 5: RATES OF REACTION (17 MARKS)
# ==========================================

PASSAGE_Q5 = """The reaction between magnesium carbonate pellets, $\\text{MgCO}_3(\\text{s})$, and EXCESS dilute hydrochloric acid, $\\text{HCl}(\\text{aq})$, is used to investigate the effect of concentration on the rate of a reaction.
$$\\text{MgCO}_3(\\text{s}) + 2\\text{HCl}(\\text{aq}) \\rightarrow \\text{MgCl}_2(\\text{aq}) + \\text{H}_2\\text{O}(\\ell) + \\text{CO}_2(\\text{g})$$

The apparatus used for this investigation is shown below.
[DIAGRAM: An open Erlenmeyer flask containing the reaction mixture (pellets of $\\text{MgCO}_3$ reacting with dilute $\\text{HCl}$) placed on top of an electronic balance reading an initial mass of $144{,}500\\text{ g}$.]"""

add_item(
    qref="5.1",
    marks=2,
    topic="Reaction Rate - Definitions (Rate of Reaction)",
    passage=PASSAGE_Q5,
    question="Define the term *rate of reaction*.",
    memo="**NOTE:** Give the mark for per unit time only if in context of reaction rate.\n**ANY ONE:**\n* Change in concentration $\\checkmark$ of products/reactants per (unit) time. $\\checkmark$\n* Change in amount/number of moles/volume/mass of products or reactants per (unit) time.\n* Amount/number of moles/volume/mass of products formed/reactants used per (unit) time.\n* Rate of change in concentration/amount/number of moles/volume/mass. $\\checkmark\\checkmark$ *(2 or 0)* *(2)*",
    final_answer="Change in concentration of products or reactants per unit time."
)

add_item(
    qref="5.2",
    marks=1,
    topic="Reaction Rate - Controlled Variables",
    passage=PASSAGE_Q5,
    question="Write down ONE controlled variable for this investigation.",
    memo="**ANY ONE:**\n* Temperature $\\checkmark$\n* (Initial) amount/Mass of magnesium carbonate $\\checkmark$\n* Surface area / state of division of magnesium carbonate $\\checkmark$ *(1)*",
    final_answer="Temperature"
)

PASSAGE_Q5_EXP = """Three experiments using different concentrations of $\\text{HCl}(\\text{aq})$ are carried out. The concentration of the $\\text{HCl}(\\text{aq})$ during each experiment does not change.

| EXPERIMENT | CONCENTRATION OF $\\text{HCl}(\\text{aq})$ ($\\text{mol}\\cdot\\text{dm}^{-3}$) |
| :---: | :---: |
| 1 | 0{,}1 |
| 2 | 0{,}5 |
| 3 | 1{,}0 |

The INCOMPLETE graph of the results of the experiments is shown below.
[DIAGRAM: Graph of Mass of reaction mixture and flask (g) vs Time (s):
* Initial mass at $t = 0\\text{ s}$ is $144{,}50\\text{ g}$ for all three curves.
* At $t = 120\\text{ s}$:
  - Curve A reaches $144{,}37\\text{ g}$ (least mass loss, slowest rate).
  - Curve B reaches $143{,}87\\text{ g}$ (intermediate mass loss).
  - Curve C reaches $143{,}24\\text{ g}$ (steepest curve, greatest mass loss).]"""

add_item(
    qref="5.3",
    marks=1,
    topic="Reaction Rate - Mass Loss Reasoning",
    passage=PASSAGE_Q5_EXP,
    question="Give a reason why the mass of the reaction mixture and flask decreases.",
    memo="$\\text{CO}_2$ / gas escapes from the reaction flask. $\\checkmark$ *(1)*",
    final_answer="Carbon dioxide gas escapes from the reaction flask."
)

add_item(
    qref="5.4",
    marks=6,
    topic="Reaction Rate - Average Rate Calculation",
    passage=PASSAGE_Q5_EXP,
    question="For curve **B**, calculate the average rate at which $\\text{CO}_2(\\text{g})$ is produced for the first $120\\text{ s}$ in $\\text{dm}^3\\cdot\\text{s}^{-1}$. The molar gas volume is $24{,}5\\text{ dm}^3\\cdot\\text{mol}^{-1}$.",
    memo="**Marking criteria:**\n(a) Mass subtraction: $m(\\text{CO}_2) = 144{,}50 - 143{,}87 = 0{,}63\\text{ g}$ $\\checkmark$\n(b) Formula: $n = \\frac{m}{M}$ or $V = nV_m$ $\\checkmark$\n(c) Substitute $M = 44\\text{ g}\\cdot\\text{mol}^{-1}$ in $n(\\text{CO}_2) = \\frac{m}{M}$ with $m(\\text{CO}_2)$ from (a): $n(\\text{CO}_2) = \\frac{0{,}63}{44} = 1{,}43 \\times 10^{-2}\\text{ mol}$ $\\checkmark$\n(d) Substitute $24{,}5\\text{ dm}^3$ in $V = nV_m$: $V(\\text{CO}_2) = (1{,}43 \\times 10^{-2})(24{,}5) = 0{,}35\\text{ dm}^3$ $\\checkmark$\n(e) Substitute $V_{\\text{CO}_2}$ and $120$ in rate formula $\\checkmark$\n(f) Final correct answer: $2{,}92 \\times 10^{-3}\\text{ dm}^3\\cdot\\text{s}^{-1}$ $\\checkmark$ (Range: $2{,}08 \\times 10^{-3}$ to $3 \\times 10^{-3}$)\n\n**Calculation:**\n$$m(\\text{CO}_2) = 144{,}50 - 143{,}87 = 0{,}63\\text{ g} \\quad \\checkmark \\text{ (a)}$$\n$$n(\\text{CO}_2) = \\frac{m}{M} = \\frac{0{,}63}{44} = 1{,}4318 \\times 10^{-2}\\text{ mol} \\quad \\checkmark \\text{ (b, c)}$$\n$$V(\\text{CO}_2) = nV_m = (1{,}4318 \\times 10^{-2})(24{,}5) = 0{,}3508\\text{ dm}^3 \\quad \\checkmark \\text{ (d)}$$\n$$\\text{Average rate} = \\frac{\\Delta V(\\text{CO}_2)}{\\Delta t} = \\frac{0{,}3508 - 0}{120 - 0} = 2{,}92 \\times 10^{-3}\\text{ dm}^3\\cdot\\text{s}^{-1} \\quad \\checkmark \\text{ (e, f)}$$ *(6)*",
    final_answer="2.92 x 10^-3 dm^3/s"
)

add_item(
    qref="5.5",
    marks=5,
    topic="Reaction Rate - Collision Theory Explanation",
    passage=PASSAGE_Q5_EXP,
    question="Which curve represents EXPERIMENT 1? Choose from **A**, **B** or **C**.\n\nUse the collision theory to explain the answer.",
    memo="**Marking criteria:**\n* $\\text{A}$ $\\checkmark$\n* Comparison of the curves of the graph: Gradient is least steep / lowest reaction rate / least amount of gas produced in $120\\text{ s}$. $\\checkmark$\n* Comparison of concentration: Lowest concentration of $\\text{HCl}(\\text{aq})$ ($0{,}1\\text{ mol}\\cdot\\text{dm}^{-3}$). $\\checkmark$\n* Collision theory - particles per volume: Least/less particles per unit volume. $\\checkmark$\n* Collision theory - effective collisions: Least/less effective collisions per unit time / second (OR lowest/lower frequency of effective collisions). $\\checkmark$ *(5)*",
    final_answer="A"
)

add_item(
    qref="5.6",
    marks=2,
    topic="Reaction Rate - Stoichiometric Yield / Limiting Reactant",
    passage=PASSAGE_Q5_EXP,
    question="How will the final mass of $\\text{CO}_2(\\text{g})$ produced in EXPERIMENT 2 compare to that of EXPERIMENT 3? Choose from MORE THAN, LESS THAN or THE SAME.\n\nGive a reason for the answer.",
    memo="THE SAME $\\checkmark$\n\nThe same amount / mass of $\\text{MgCO}_3$ is used in each experiment (and $\\text{HCl}$ is in excess in both). $\\checkmark$ *(2)*",
    final_answer="THE SAME. The same amount of magnesium carbonate is used in each experiment."
)

# ==========================================
# QUESTION 6: CHEMICAL EQUILIBRIUM (19 MARKS)
# ==========================================

PASSAGE_Q6 = """The reaction between powdered carbon, $\\text{C}(\\text{s})$, and carbon dioxide gas, $\\text{CO}_2(\\text{g})$, takes place in a closed $3\\text{ dm}^3$ container according to the balanced equation below.
$$\\text{C}(\\text{s}) + \\text{CO}_2(\\text{g}) \\rightleftharpoons 2\\text{CO}(\\text{g}) \\quad \\Delta H < 0$$

Equilibrium is reached at temperature $T\\,^\\circ\\text{C}$.

The graph below, not drawn to scale, shows the curves for the mass of the reactants in the container against time.
[DIAGRAM: Graph of Mass of reactants (g) vs Time (minutes):
* $\\text{CO}_2(\\text{g})$ curve starts at $41{,}2\\text{ g}$ at $t = 0$ and decreases to an equilibrium plateau at mass $X$ at time $t_1$.
* $\\text{C}(\\text{s})$ curve starts at $14{,}0\\text{ g}$ at $t = 0$ and decreases to an equilibrium plateau at $4{,}44\\text{ g}$ at time $t_1$.]"""

add_item(
    qref="6.1.1",
    marks=1,
    topic="Chemical Equilibrium - Factors (Catalyst)",
    passage=PASSAGE_Q6,
    question="How will the following change affect the number of moles of $\\text{CO}_2(\\text{g})$ at equilibrium?\nA catalyst is added.\n\nChoose from INCREASES, DECREASES or REMAINS THE SAME.",
    memo="Remains the same $\\checkmark$ *(1)*",
    final_answer="REMAINS THE SAME"
)

add_item(
    qref="6.1.2",
    marks=1,
    topic="Chemical Equilibrium - Factors (Volume/Pressure)",
    passage=PASSAGE_Q6,
    question="How will the following change affect the number of moles of $\\text{CO}_2(\\text{g})$ at equilibrium?\nThe volume of the container is increased at a constant temperature.\n\nChoose from INCREASES, DECREASES or REMAINS THE SAME.",
    memo="Decreases $\\checkmark$ *(1)*",
    final_answer="DECREASES"
)

add_item(
    qref="6.1.3",
    marks=1,
    topic="Chemical Equilibrium - Factors (Adding Solid Reactant)",
    passage=PASSAGE_Q6,
    question="How will the following change affect the number of moles of $\\text{CO}_2(\\text{g})$ at equilibrium?\nMore powdered carbon is added.\n\nChoose from INCREASES, DECREASES or REMAINS THE SAME.",
    memo="Remains the same $\\checkmark$ *(1)*",
    final_answer="REMAINS THE SAME"
)

add_item(
    qref="6.2",
    marks=2,
    topic="Chemical Equilibrium - Le Chatelier's Principle",
    passage=PASSAGE_Q6,
    question="Explain the answer to QUESTION 6.1.2 by referring to Le Chatelier's principle.",
    memo="* An increase in volume causes a decrease in pressure; a decrease in pressure favours the reaction that produces a greater number of moles / amount of gas. $\\checkmark$\n* The forward reaction produces 2 moles of gas while the reverse reaction consumes 1 mole of gas, so the forward reaction is favoured ($[\\text{CO}]$ increases AND $[\\text{CO}_2]$ decreases). $\\checkmark$ *(2)*",
    final_answer="A decrease in pressure favours the reaction that produces a greater number of moles of gas (forward reaction)."
)

add_item(
    qref="6.3",
    marks=6,
    topic="Chemical Equilibrium - Stoichiometric Mass Calculation (X)",
    passage=PASSAGE_Q6,
    question="Calculate the value of **X** shown on the graph.",
    memo="**Marking criteria:**\n(a) Change in mass of carbon: $m(\\text{C})_{\\text{used}} = 14{,}0 - 4{,}44 = 9{,}56\\text{ g}$ $\\checkmark$\n(b) Calculate moles of carbon reacted: $n(\\text{C})_{\\text{used}} = \\frac{m}{M} = \\frac{9{,}56}{12} = 0{,}7967\\text{ mol}$ $\\checkmark$ (Substitute 12 in $n = \\frac{m}{M}$)\n(c) Use mole ratio $n(\\text{C}) : n(\\text{CO}_2) = 1 : 1 \\implies n(\\text{CO}_2)_{\\text{reacted}} = 0{,}7967\\text{ mol}$ $\\checkmark$\n(d) Calculate initial moles of $\\text{CO}_2$: $n(\\text{CO}_2)_{\\text{initial}} = \\frac{41{,}2}{44} = 0{,}9364\\text{ mol}$ $\\checkmark$ (Substitute 44 in $n = \\frac{m}{M}$)\n(e) Equilibrium moles of $\\text{CO}_2$: $n(\\text{CO}_2)_{\\text{eq}} = 0{,}9364 - 0{,}7967 = 0{,}1397\\text{ mol}$ $\\checkmark$\n(f) Final answer for $X$: $X = m(\\text{CO}_2)_{\\text{eq}} = n \\times M = 0{,}1397 \\times 44 = 6{,}15\\text{ g}$ (or $6{,}16\\text{ g}$) $\\checkmark$\n\n*(Range: $6{,}00\\text{ to } 6{,}16\\text{ g}$ accepted per memo)* *(6)*",
    final_answer="6.16 g"
)

add_item(
    qref="6.4",
    marks=5,
    topic="Chemical Equilibrium - Equilibrium Constant (Kc) Calculation",
    passage=PASSAGE_Q6,
    question="Calculate the equilibrium constant, $K_c$, at $T\\,^\\circ\\text{C}$.",
    memo="**POSITIVE MARKING FROM QUESTION 6.3:**\n**Marking criteria:**\n(a) Use of ratio $n(\\text{CO}_2) : n(\\text{CO}) = 1 : 2 \\implies n(\\text{CO})_{\\text{eq}} = 2 \\times 0{,}8 = 1{,}6\\text{ mol}$ (or $2 \\times 0{,}7967 = 1{,}593\\text{ mol}$) $\\checkmark$\n(b) Divide equilibrium moles by $3\\text{ dm}^3$: $[\\text{CO}] = \\frac{1{,}6}{3} = 0{,}533\\text{ mol}\\cdot\\text{dm}^{-3}$, $[\\text{CO}_2] = \\frac{0{,}14}{3} = 0{,}0467\\text{ mol}\\cdot\\text{dm}^{-3}$ $\\checkmark$\n(c) Correct $K_c$ expression (formulae in square brackets, omitting solid carbon): $K_c = \\frac{[\\text{CO}]^2}{[\\text{CO}_2]}$ $\\checkmark$\n(d) Substitution of concentrations into $K_c$ expression: $K_c = \\frac{(0{,}533)^2}{0{,}0467}$ $\\checkmark$\n(e) Final answer: $5{,}98$ $\\checkmark$ (Range: $5{,}98 - 7{,}29$)\n\n**Calculation:**\n$$n(\\text{CO}_2)_{\\text{initial}} = \\frac{41{,}2}{44} = 0{,}936\\text{ mol}$$\n$$\\Delta n(\\text{CO}_2) = 0{,}8\\text{ mol} \\implies \\Delta n(\\text{CO}) = 1{,}6\\text{ mol} \\quad \\checkmark \\text{ (a)}$$\n$$[\\text{CO}]_{\\text{eq}} = \\frac{1{,}6}{3} = 0{,}53\\text{ mol}\\cdot\\text{dm}^{-3}, \\quad [\\text{CO}_2]_{\\text{eq}} = \\frac{0{,}14}{3} = 0{,}047\\text{ mol}\\cdot\\text{dm}^{-3} \\quad \\checkmark \\text{ (b)}$$\n$$K_c = \\frac{[\\text{CO}]^2}{[\\text{CO}_2]} \\quad \\checkmark \\text{ (c)}$$\n$$K_c = \\frac{(0{,}53)^2}{0{,}047} = 5{,}98 \\quad \\checkmark \\text{ (d, e)}$$ *(5)*",
    final_answer="5.98"
)

PASSAGE_Q6_DISTURB = """The balanced equation for this reaction is rewritten below for easy reference.
$$\\text{C}(\\text{s}) + \\text{CO}_2(\\text{g}) \\rightleftharpoons 2\\text{CO}(\\text{g}) \\quad \\Delta H < 0$$

The graph below shows the equilibrium number of moles of $\\text{CO}(\\text{g})$, $\\text{C}(\\text{s})$ and $\\text{CO}_2(\\text{g})$ in the flask at time $t_1$.
At $t_2$, some $\\text{CO}(\\text{g})$ is added to the flask and the reaction is allowed to reach equilibrium. Curve **Z** correctly shows the change in the amount of $\\text{CO}(\\text{g})$ between $t_2$ and $t_3$.
A learner draws corresponding curves, labelled **X** and **Y**, for $\\text{C}(\\text{s})$ and $\\text{CO}_2(\\text{g})$ respectively.

[DIAGRAM: Graph of Amount (moles) vs Time (minutes):
* At $t_1$, all three substances are at horizontal equilibrium plateaus.
* At $t_2$, $\\text{CO}(\\text{g})$ shows a sharp vertical increase (addition of CO), then gradually decreases along curve Z to a new equilibrium at $t_3$.
* Curve X: Shows amount of $\\text{C}(\\text{s})$ over time.
* Curve Y: Shows amount of $\\text{CO}_2(\\text{g})$ over time, gradually increasing from $t_2$ to reach a higher equilibrium at $t_3$.]"""

add_item(
    qref="6.5",
    marks=2,
    topic="Chemical Equilibrium - Disturbance Curves",
    passage=PASSAGE_Q6_DISTURB,
    question="Which of these curves is the CORRECT representation for these changes?\n\nChoose from:\n**X** or\n**Y** or\n**X and Y**",
    memo="Y $\\checkmark\\checkmark$ *(2)*\n\n*Rationale: When CO is added at $t_2$, Le Chatelier's principle dictates that the reverse reaction is favoured to consume the added CO. As the reverse reaction proceeds, more $\\text{CO}_2(\\text{g})$ is formed, so the amount of $\\text{CO}_2(\\text{g})$ increases gradually without an initial step, which is correctly depicted by curve Y.*",
    final_answer="Y"
)

add_item(
    qref="6.6",
    marks=1,
    topic="Chemical Equilibrium - Factors Affecting Kc",
    passage=PASSAGE_Q6_DISTURB,
    question="What effect will the addition of $\\text{CO}(\\text{g})$ have on the equilibrium constant, $K_c$?\n\nChoose from INCREASES, DECREASES or REMAINS THE SAME.",
    memo="Remains the same $\\checkmark$ *(1)*\n\n*Rationale: The equilibrium constant $K_c$ is dependent solely on temperature. Changing the concentration or amount of any reactant or product at constant temperature does not affect $K_c$.*",
    final_answer="REMAINS THE SAME"
)

# ==========================================
# QUESTION 7: ACIDS AND BASES (22 MARKS)
# ==========================================

add_item(
    qref="7.1",
    marks=2,
    topic="Acids and Bases - Definitions (Arrhenius Acid)",
    passage="",
    question="Define an acid according to the Arrhenius theory.",
    memo="An acid produces hydrogen ions / $\\text{H}^+$ / hydronium ions / $\\text{H}_3\\text{O}^+$ in aqueous solution / water. $\\checkmark\\checkmark$ *(2 or 0)* *(2)*",
    final_answer="An acid produces hydrogen ions (or hydronium ions) in aqueous solution."
)

PASSAGE_Q7_2 = """7.2 The table below shows aqueous solutions of different substances, each of concentration $1\\text{ mol}\\cdot\\text{dm}^{-3}$ at room temperature.

| | | | |
| :---: | :---: | :---: | :---: |
| $\\text{HNO}_3(\\text{aq})$ | $\\text{H}_2\\text{SO}_4(\\text{aq})$ | $\\text{NaCl}(\\text{aq})$ | $\\text{NaOH}(\\text{aq})$ |
| $(\\text{COOH})_2(\\text{aq})$ | $\\text{HCO}_3^-(\\text{aq})$ | $\\text{Mg(OH)}_2(\\text{aq})$ | $\\text{NH}_3(\\text{aq})$ | $\\text{CH}_3\\text{COOH}(\\text{aq})$ |"""

add_item(
    qref="7.2.1",
    marks=1,
    topic="Acids and Bases - Diprotic Acid",
    passage=PASSAGE_Q7_2,
    question="Identify from the table and write down the FORMULA for a weak diprotic acid.",
    memo="$(\\text{COOH})_2 \\checkmark$ *(1)*",
    final_answer="(COOH)2"
)

add_item(
    qref="7.2.2",
    marks=1,
    topic="Acids and Bases - Neutral Solution (pH 7)",
    passage=PASSAGE_Q7_2,
    question="Identify from the table and write down the FORMULA for a solution with a pH of 7.",
    memo="$\\text{NaCl} \\checkmark$ *(1)*",
    final_answer="NaCl"
)

add_item(
    qref="7.2.3",
    marks=1,
    topic="Acids and Bases - Ampholytes",
    passage=PASSAGE_Q7_2,
    question="Identify from the table and write down the FORMULA for an ampholyte.",
    memo="$\\text{HCO}_3^- \\checkmark$ **OR/OF** $\\text{NH}_3$ *(1)*",
    final_answer="HCO3^-"
)

add_item(
    qref="7.2.4",
    marks=2,
    topic="Acids and Bases - Hydrolysis / Salt Formation (pH > 7)",
    passage=PASSAGE_Q7_2,
    question="Identify from the table and write down the FORMULA for the solution, which when neutralised with $(\\text{COOH})_2(\\text{aq})$, will have a pH greater than 7.",
    memo="$\\text{NaOH} \\checkmark\\checkmark$ **OR/OF** $\\text{Mg(OH)}_2$ *(2)*\n\n*Rationale: Oxalic acid, $(\\text{COOH})_2$, is a weak acid. Neutralisation of a weak acid with a strong base (such as $\\text{NaOH}$ or $\\text{Mg(OH)}_2$) produces a basic salt whose conjugate base undergoes hydrolysis in water, producing $\\text{OH}^-$ ions and giving a pH greater than 7.*",
    final_answer="NaOH"
)

add_item(
    qref="7.3",
    marks=6,
    topic="Acids and Bases - Titration Calculation & Balanced Equation",
    passage="",
    question="An unknown acid $\\text{H}_x\\text{Y}$ is investigated.\n\nDuring a titration, $23{,}64\\text{ cm}^3$ of a $0{,}11\\text{ mol}\\cdot\\text{dm}^{-3}$ $\\text{H}_x\\text{Y}$ solution neutralises $20\\text{ cm}^3$ of a $0{,}26\\text{ mol}\\cdot\\text{dm}^{-3}$ $\\text{NaOH}$ solution.\n\nCalculate the value of $x$. Hence, write down the balanced equation for this reaction.",
    memo="**Marking criteria:**\n(a) Calculate $n(\\text{H}_x\\text{Y}) = cV = (0{,}11)(0{,}02364) = 2{,}6004 \\times 10^{-3}\\text{ mol}$ $\\checkmark$\n(b) Calculate $n(\\text{NaOH}) = cV = (0{,}26)(0{,}020) = 5{,}2 \\times 10^{-3}\\text{ mol}$ $\\checkmark$\n(c) Determine mole ratio: $\\frac{n(\\text{NaOH})}{n(\\text{H}_x\\text{Y})} = \\frac{5{,}2 \\times 10^{-3}}{2{,}6004 \\times 10^{-3}} = 2 \\implies x = 2$ $\\checkmark$\n(d) Balanced equation: Reactants $\\text{H}_2\\text{Y}(\\text{aq}) + 2\\text{NaOH}(\\text{aq})$ $\\checkmark$, Products $\\text{Na}_2\\text{Y}(\\text{aq}) + 2\\text{H}_2\\text{O}(\\ell)$ $\\checkmark$, Balancing $\\checkmark$\n\n$$\\text{H}_2\\text{Y}(\\text{aq}) \\checkmark + 2\\text{NaOH}(\\text{aq}) \\rightarrow \\text{Na}_2\\text{Y}(\\text{aq}) + 2\\text{H}_2\\text{O}(\\ell) \\checkmark \\quad \\text{Bal.} \\checkmark$$ *(6)*",
    final_answer="x = 2; H2Y + 2NaOH -> Na2Y + 2H2O"
)

PASSAGE_Q7_4 = """In an experiment, $1{,}5\\text{ g}$ of a powdered IMPURE calcium carbonate sample, $\\text{CaCO}_3(\\text{s})$, is reacted with $200\\text{ cm}^3$ of a $0{,}15\\text{ mol}\\cdot\\text{dm}^{-3}$ hydrochloric acid solution, $\\text{HCl}(\\text{aq})$. The balanced equation for the reaction is:
$$\\text{CaCO}_3(\\text{s}) + 2\\text{HCl}(\\text{aq}) \\rightarrow \\text{CaCl}_2(\\text{aq}) + \\text{CO}_2(\\text{g}) + \\text{H}_2\\text{O}(\\ell)$$

All the $\\text{CO}_2(\\text{g})$ formed escapes from the solution.
The resulting solution has a pH of $1{,}61$ and a volume of $200\\text{ cm}^3$.
Assume that ALL the $\\text{CaCO}_3(\\text{s})$ in the impure sample reacted with the $\\text{HCl}(\\text{aq})$ and none of the impurities reacted."""

add_item(
    qref="7.4",
    marks=9,
    topic="Acids and Bases - Stoichiometry / Impure Sample & pH",
    passage=PASSAGE_Q7_4,
    question="Calculate the mass of the impurities present in the $1{,}5\\text{ g}$ sample of impure $\\text{CaCO}_3(\\text{s})$.",
    memo="**Marking criteria:**\n(a) Any formula: $\\text{pH} = -\\log[\\text{H}_3\\text{O}^+]$ or $[\\text{H}_3\\text{O}^+] = 10^{-\\text{pH}}$ $\\checkmark$\n(b) Substitute $1{,}61$ in $\\text{pH} = -\\log[\\text{H}_3\\text{O}^+]$: $[\\text{H}_3\\text{O}^+] = 10^{-1{,}61} = 2{,}455 \\times 10^{-2}\\text{ mol}\\cdot\\text{dm}^{-3}$ $\\checkmark$\n(c) Calculate $n(\\text{HCl})_{\\text{unused}} = cV = (2{,}455 \\times 10^{-2})(0{,}200) = 4{,}91 \\times 10^{-3}\\text{ mol}$ $\\checkmark$\n(d) Calculate $n(\\text{HCl})_{\\text{initial}} = cV = (0{,}15)(0{,}200) = 3{,}00 \\times 10^{-2}\\text{ mol}$ $\\checkmark$\n(e) Calculate $n(\\text{HCl})_{\\text{used}} = n(\\text{HCl})_{\\text{initial}} - n(\\text{HCl})_{\\text{unused}} = 3{,}00 \\times 10^{-2} - 4{,}91 \\times 10^{-3} = 2{,}509 \\times 10^{-2}\\text{ mol}$ $\\checkmark$\n(f) Use ratio $n(\\text{CaCO}_3) : n(\\text{HCl}) = 1 : 2$: $n(\\text{CaCO}_3) = \\frac{1}{2}(2{,}509 \\times 10^{-2}) = 1{,}255 \\times 10^{-2}\\text{ mol}$ $\\checkmark$\n(g) Substitute $M = 100\\text{ g}\\cdot\\text{mol}^{-1}$ and $n(\\text{CaCO}_3)$ in $n = \\frac{m}{M}$: $m(\\text{CaCO}_3) = (1{,}255 \\times 10^{-2})(100) = 1{,}255\\text{ g}$ $\\checkmark$\n(h) Mass subtraction: $m_{\\text{impurity}} = m_{\\text{sample}} - m(\\text{CaCO}_3)$ $\\checkmark$\n(i) Final answer: $m_{\\text{impurity}} = 1{,}50 - 1{,}255 = 0{,}25\\text{ g}$ $\\checkmark$ (Range: $0{,}2\\text{ g to } 0{,}3\\text{ g}$)\n\n**Calculation:**\n$$\\text{pH} = 1{,}61 \\implies [\\text{H}_3\\text{O}^+] = 10^{-1{,}61} = 2{,}455 \\times 10^{-2}\\text{ mol}\\cdot\\text{dm}^{-3} \\quad \\checkmark \\text{ (a, b)}$$\n$$n(\\text{HCl})_{\\text{unused}} = cV = (2{,}455 \\times 10^{-2})(0{,}200) = 4{,}91 \\times 10^{-3}\\text{ mol} \\quad \\checkmark \\text{ (c)}$$\n$$n(\\text{HCl})_{\\text{initial}} = cV = (0{,}15)(0{,}200) = 3{,}00 \\times 10^{-2}\\text{ mol} \\quad \\checkmark \\text{ (d)}$$\n$$n(\\text{HCl})_{\\text{used}} = 3{,}00 \\times 10^{-2} - 4{,}91 \\times 10^{-3} = 2{,}509 \\times 10^{-2}\\text{ mol} \\quad \\checkmark \\text{ (e)}$$\n$$n(\\text{CaCO}_3) = \\frac{1}{2}n(\\text{HCl})_{\\text{used}} = 1{,}255 \\times 10^{-2}\\text{ mol} \\quad \\checkmark \\text{ (f)}$$\n$$m(\\text{CaCO}_3) = n \\times M = (1{,}255 \\times 10^{-2})(100) = 1{,}255\\text{ g} \\quad \\checkmark \\text{ (g)}$$\n$$m(\\text{impurity}) = 1{,}50 - 1{,}255 = 0{,}25\\text{ g} \\quad \\checkmark \\text{ (h, i)}$$ *(9)*",
    final_answer="0.25 g"
)

# ==========================================
# QUESTION 8: GALVANIC CELLS (13 MARKS)
# ==========================================

PASSAGE_Q8 = """The simplified diagram below shows a cell that can be used to measure the standard electrode potential of the half-reaction represented by the equation below.
$$\\text{Fe}^{3+}(\\text{aq}) + \\text{e}^- \\rightleftharpoons \\text{Fe}^{2+}(\\text{aq})$$

[DIAGRAM: Galvanic cell under standard conditions consisting of two half-cells connected by a salt bridge and an external circuit with a voltmeter V:
* Left half-cell: Beaker containing an aqueous solution of $\\text{Fe}^{3+}(\\text{aq})$ and $\\text{Fe}^{2+}(\\text{aq})$ ions ($1\\text{ mol}\\cdot\\text{dm}^{-3}$ each) with an inert electrode A immersed.
* Right half-cell: Standard hydrogen electrode (SHE) comprising an inert electrode B in an inverted tube with hydrogen gas $\\text{H}_2(\\text{g})$ at $101{,}3\\text{ kPa}$ bubbled into Solution D ($1\\text{ mol}\\cdot\\text{dm}^{-3} \\text{ H}^+(\\text{aq})$).]"""

add_item(
    qref="8.1",
    marks=1,
    topic="Electrochemical Cells - Standard Hydrogen Electrode",
    passage=PASSAGE_Q8,
    question="For solution D, write down the NAME or FORMULA of the ions needed.",
    memo="$\\text{H}^+ / \\text{H}_3\\text{O}^+$ ions / hydrogen ions / hydronium ions / oxonium ions $\\checkmark$ *(1)*",
    final_answer="H+"
)

add_item(
    qref="8.2",
    marks=1,
    topic="Electrochemical Cells - Standard Cell Potential",
    passage=PASSAGE_Q8,
    question="Write down the initial reading on the voltmeter.",
    memo="$0{,}77\\text{ V} \\checkmark$ *(1)*\n\n*Working: $E^\\circ_{\\text{cell}} = E^\\circ_{\\text{cathode}} - E^\\circ_{\\text{anode}} = 0{,}77\\text{ V} - 0{,}00\\text{ V} = 0{,}77\\text{ V}$*",
    final_answer="0.77 V"
)

add_item(
    qref="8.3",
    marks=1,
    topic="Electrochemical Cells - Identification of Cathode",
    passage=PASSAGE_Q8,
    question="Which electrode, **A** or **B**, is the cathode?",
    memo="A $\\checkmark$ *(1)*",
    final_answer="A"
)

add_item(
    qref="8.4",
    marks=3,
    topic="Electrochemical Cells - Relative Strengths of Reducing Agents",
    passage=PASSAGE_Q8,
    question="Explain the answer to QUESTION 8.3 in terms of the relative strengths of the reducing agents.",
    memo="* $\\text{H}_2$ is a stronger reducing agent $\\checkmark$\n* than $\\text{Fe}^{2+} / \\text{Fe(II)}$ ions $\\checkmark$\n* and will reduce $\\text{Fe}^{3+} / \\text{Fe(III)}$ ions (to $\\text{Fe}^{2+}$ ions). $\\checkmark$ *(3)*",
    final_answer="H2 is a stronger reducing agent than Fe^2+ and will reduce Fe^3+ ions to Fe^2+."
)

add_item(
    qref="8.5.1",
    marks=1,
    topic="Electrochemical Cells - Inert Electrode Material",
    passage=PASSAGE_Q8,
    question="Write down the NAME or FORMULA of the metal used as electrode A.",
    memo="Platinum / $\\text{Pt} \\checkmark$ *(1)*",
    final_answer="Pt"
)

add_item(
    qref="8.5.2",
    marks=2,
    topic="Electrochemical Cells - Half-reaction at Anode",
    passage=PASSAGE_Q8,
    question="Write down the half-reaction that occurs at electrode B.",
    memo="$$\\text{H}_2 \\rightarrow 2\\text{H}^+ + 2\\text{e}^- \\checkmark\\checkmark$$ *(2)*\n*(Accept single or double arrows, ignore phases)*",
    final_answer="H2 -> 2H+ + 2e-"
)

add_item(
    qref="8.5.3",
    marks=3,
    topic="Electrochemical Cells - Standard Cell Notation",
    passage=PASSAGE_Q8,
    question="Write down the cell notation for this cell.",
    memo="**Marking criteria:**\n* Oxidation half-cell / Anode on the left: $\\text{Pt}(\\text{s}) \\mid \\text{H}_2(\\text{g}) \\mid \\text{H}^+(\\text{aq})$ $\\checkmark$\n* Salt bridge: $\\parallel$ $\\checkmark$\n* Reduction half-cell / Cathode on the right: $\\text{Fe}^{3+}(\\text{aq}), \\text{Fe}^{2+}(\\text{aq}) \\mid \\text{Pt}(\\text{s})$ $\\checkmark$\n\n$$\\text{Pt}(\\text{s}) \\mid \\text{H}_2(\\text{g}) \\mid \\text{H}^+(\\text{aq}) \\parallel \\text{Fe}^{3+}(\\text{aq}), \\text{Fe}^{2+}(\\text{aq}) \\mid \\text{Pt}(\\text{s}) \\checkmark\\checkmark\\checkmark$$ *(3)*",
    final_answer="Pt(s) | H2(g) | H+(aq) || Fe^3+(aq), Fe^2+(aq) | Pt(s)"
)

add_item(
    qref="8.6",
    marks=1,
    topic="Electrochemical Cells - Chemical Equilibrium in Galvanic Cells",
    passage=PASSAGE_Q8,
    question="Give a reason why the voltmeter reading drops to zero after the cell has operated for some time.",
    memo="The reaction reaches equilibrium / rate of forward reaction equals rate of reverse reaction / no net charge or electrons flow. $\\checkmark$ *(1)*",
    final_answer="The cell reaction has reached chemical equilibrium."
)

# ==========================================
# QUESTION 9: ELECTROLYTIC CELLS (9 MARKS)
# ==========================================

PASSAGE_Q9 = """The simplified diagram below represents an electrolytic cell used to demonstrate the electrolysis of a concentrated sodium chloride solution, $\\text{NaCl}(\\text{aq})$.
**X** and **Y** are carbon electrodes.

[DIAGRAM: Electrolytic cell showing:
* An electrolytic container holding concentrated aqueous sodium chloride solution, $\\text{NaCl}(\\text{aq})$.
* Two carbon electrodes X and Y immersed in the solution and connected to an external DC power source.
* Electrode X is connected to the positive terminal (anode, where oxidation of $\\text{Cl}^-$ produces chlorine gas).
* Electrode Y is connected to the negative terminal (cathode, where reduction of $\\text{H}_2\\text{O}$ produces hydrogen gas).
* Inverted test tubes filled with electrolyte are mounted over electrodes X and Y to collect the gases evolved.]"""

add_item(
    qref="9.1",
    marks=2,
    topic="Electrolytic Cells - Definitions (Electrolysis)",
    passage=PASSAGE_Q9,
    question="Define the term *electrolysis*.",
    memo="**ANY ONE:**\n* The (chemical) process in which electrical energy is converted to chemical energy. $\\checkmark\\checkmark$ *(2 or 0)*\n* The use of electrical energy to produce a chemical change.\n* Decomposition of an ionic compound by means of electrical energy.\n* The process during which an electric current passes through a solution / ionic liquid / molten ionic compound. *(2)*",
    final_answer="The chemical process in which electrical energy is converted to chemical energy."
)

add_item(
    qref="9.2",
    marks=2,
    topic="Electrolytic Cells - Reduction Half-reaction",
    passage=PASSAGE_Q9,
    question="Write down the reduction half-reaction for this cell.",
    memo="$$2\\text{H}_2\\text{O}(\\ell) + 2\\text{e}^- \\rightarrow \\text{H}_2(\\text{g}) + 2\\text{OH}^-(\\text{aq}) \\checkmark\\checkmark$$ *(2)*\n*(Accept single or double arrows, ignore phases)*",
    final_answer="2H2O(l) + 2e- -> H2(g) + 2OH-(aq)"
)

add_item(
    qref="9.3",
    marks=1,
    topic="Electrolytic Cells - Electron Flow in External Circuit",
    passage=PASSAGE_Q9,
    question="What is the direction of the electron flow in the external circuit? Choose from **X to Y** or **Y to X**.",
    memo="**X to Y** $\\checkmark$ *(1)*\n\n*Rationale: Electrode X is the anode (positive electrode), where $\\text{Cl}^-$ ions are oxidised releasing electrons into electrode X: $2\\text{Cl}^- \\rightarrow \\text{Cl}_2 + 2\\text{e}^-$. These electrons flow through the external circuit from electrode X to the positive terminal of the power supply, and from the negative terminal to electrode Y (cathode), where water molecules are reduced: $2\\text{H}_2\\text{O} + 2\\text{e}^- \\rightarrow \\text{H}_2 + 2\\text{OH}^-$. Therefore, the electron flow in the external circuit is from X to Y.*",
    final_answer="X to Y"
)

add_item(
    qref="9.4",
    marks=4,
    topic="Electrolytic Cells - Stoichiometry of Charge & Electrons Transferred",
    passage=PASSAGE_Q9,
    question="Calculate the number of electrons transferred through the external circuit when $300\\text{ cm}^3$ gas is collected at electrode **X**.\nTake the molar gas volume as $24\\text{ dm}^3\\cdot\\text{mol}^{-1}$.",
    memo="**Marking criteria:**\n(a) Substitute $300 \\times 10^{-3}\\text{ dm}^3$ and $24\\text{ dm}^3\\cdot\\text{mol}^{-1}$ into $n = \\frac{V}{V_m}$: $n(\\text{Cl}_2) = \\frac{0{,}300}{24} = 0{,}0125\\text{ mol}$ $\\checkmark$\n(b) Using ratio $1:2$ from oxidation half-reaction ($2\\text{Cl}^- \\rightarrow \\text{Cl}_2 + 2\\text{e}^-$) to calculate $n(\\text{e}^-)$: $n(\\text{e}^-) = 2 \\times 0{,}0125 = 0{,}025\\text{ mol}$ $\\checkmark$\n(c) Substitute $6{,}02 \\times 10^{23}\\text{ mol}^{-1}$ in $N = n \\times N_A$: $N(\\text{e}^-) = 0{,}025 \\times (6{,}02 \\times 10^{23})$ $\\checkmark$\n(d) Final correct answer: $1{,}505 \\times 10^{22}\\text{ electrons}$ (or $1{,}51 \\times 10^{22}$) $\\checkmark$ (Range: $1{,}505 \\times 10^{22}$ to $2{,}41 \\times 10^{22}$)\n\n**Calculation:**\n$$n(\\text{Cl}_2) = \\frac{V}{V_m} = \\frac{300 \\times 10^{-3}}{24} = 0{,}0125\\text{ mol} \\quad \\checkmark \\text{ (a)}$$\n$$n(\\text{e}^-) = 2n(\\text{Cl}_2) = 2(0{,}0125) = 0{,}025\\text{ mol} \\quad \\checkmark \\text{ (b)}$$\n$$N(\\text{e}^-) = n \\times N_A = 0{,}025 \\times (6{,}02 \\times 10^{23}) = 1{,}505 \\times 10^{22}\\text{ electrons} \\quad \\checkmark \\text{ (c, d)}$$ *(4)*",
    final_answer="1.505 x 10^22 electrons"
)

# ==========================================
# VALIDATION AND WRITING
# ==========================================

print(f"Total items extracted: {len(items)}")
total_marks = sum(item["marks"] for item in items)
print(f"Total marks: {total_marks} / 150")
assert total_marks == 150, f"Mark sum error: expected 150, got {total_marks}"

# Validate KaTeX / LaTeX formatting
bare_deg_re = re.compile(r'(?<!\^\\circ\\text\{)°C|(?<!\^\\circ)°C')
for item in items:
    for field in ["question", "memo", "passage"]:
        val = item[field]
        # Check dollar balance
        # count single dollars not part of double dollars
        s = val.replace("$$", "")
        if s.count("$") % 2 != 0:
            raise ValueError(f"Unbalanced dollar sign in {item['item_id']} field {field}")
        if "°C" in val and "$^\\circ\\text{C}$" not in val and "$25\\,^\\circ\\text{C}$" not in val:
            # check if bare °C exists
            matches = [m.start() for m in re.finditer(r'°C', val)]
            for m in matches:
                # check context
                sub = val[max(0, m-10):min(len(val), m+10)]
                if not ("^\\circ" in sub or "\\circ" in sub):
                    raise ValueError(f"Bare °C found in {item['item_id']} field {field}: {sub}")

out_path_1 = "sa-tutor-kit/sa-tutor-kit/workspace/items/physical_sciences/dbe-physical_sciences-g12-p2-2025-may.jsonl"
out_path_2 = "sa-tutor-kit/sa-tutor-kit/workspace/items/dbe-physical_sciences-g12-p2-2025-may.jsonl"

os.makedirs(os.path.dirname(out_path_1), exist_ok=True)
os.makedirs(os.path.dirname(out_path_2), exist_ok=True)

for path in [out_path_1, out_path_2]:
    with open(path, "w", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"Successfully written: {path} ({os.path.getsize(path)} bytes)")

print("EXTRACTION COMPLETE AND VERIFIED!")
