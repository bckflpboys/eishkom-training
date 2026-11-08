import json
import re
import sys

SOURCE_ID = "dbe-physical_sciences-g12-p2-2023-nov"
MEMO_SOURCE_ID = "dbe-physical_sciences-g12-p2-2023-nov-memo"
SUBJECT = "physical_sciences"
GRADE = 12
LANGUAGE = "en"
TRACK = "sciences"
LICENCE = "DBE copyright - check terms"
ATTRIBUTION = "Department of Basic Education"

items = []

def add_item(ref, marks, topic, passage, question, memo, final_answer, needs_review=False, kind="question"):
    slug = ref.lower().replace(" ", "-")
    item_id = f"{SOURCE_ID}-{slug}"
    item = {
        "item_id": item_id,
        "source_id": SOURCE_ID,
        "pair_source_id": MEMO_SOURCE_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "language": LANGUAGE,
        "track": TRACK,
        "kind": kind,
        "question_ref": ref,
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

# ==============================================================================
# QUESTION 1: MULTIPLE-CHOICE QUESTIONS (10 items x 2 marks = 20 marks)
# ==============================================================================

add_item(
    ref="1.1",
    marks=2,
    topic="Organic Chemistry - Saturated Hydrocarbons",
    passage="",
    question="Which ONE of the following represents a straight chain SATURATED hydrocarbon?\n\nA $\\text{C}_5\\text{H}_8$\nB $\\text{C}_5\\text{H}_{10}$\nC $\\text{C}_6\\text{H}_{12}$\nD $\\text{C}_6\\text{H}_{14}$",
    memo="D $\\checkmark\\checkmark$\n\n**Reasoning:**\nA saturated hydrocarbon (alkane) contains only single carbon-carbon bonds and follows the general formula $\\text{C}_n\\text{H}_{2n+2}$. For $n = 6$, the number of hydrogen atoms is $2(6) + 2 = 14$, which gives hexane ($\\text{C}_6\\text{H}_{14}$). Option A is an alkyne ($\\text{C}_n\\text{H}_{2n-2}$), and options B and C are alkenes ($\\text{C}_n\\text{H}_{2n}$).",
    final_answer="D"
)

add_item(
    ref="1.2",
    marks=2,
    topic="Organic Chemistry - Classification of Alcohols",
    passage="",
    question="Which ONE of the following is a SECONDARY alcohol?\n\nA $\\text{C}(\\text{CH}_3)_3\\text{OH}$\nB $\\text{CH}_3(\\text{CH}_2)_3\\text{OH}$\nC $\\text{CH}_3(\\text{CH}_2)_2\\text{CHO}$\nD $\\text{CH}_3\\text{CH}_2\\text{CH}(\\text{OH})\\text{CH}_3$",
    memo="D $\\checkmark\\checkmark$\n\n**Reasoning:**\nIn a secondary alcohol, the carbon atom attached to the hydroxyl group ($-\\text{OH}$) is directly bonded to TWO other carbon atoms. In $\\text{CH}_3\\text{CH}_2\\text{CH}(\\text{OH})\\text{CH}_3$ (butan-2-ol), the C2 atom is bonded to C1 and C3. Option A is a tertiary alcohol (2-methylpropan-2-ol), Option B is a primary alcohol (butan-1-ol), and Option C is an aldehyde (butanal).",
    final_answer="D"
)

add_item(
    ref="1.3",
    marks=2,
    topic="Organic Reactions - Hydrolysis",
    passage="",
    question="Which ONE of the following is a HYDROLYSIS reaction?\n\nA $\\text{CH}_3\\text{CH}_2\\text{Br} + \\text{H}_2\\text{O} \\rightarrow \\text{CH}_3\\text{CH}_2\\text{OH} + \\text{HBr}$\nB $\\text{CH}_3\\text{CH}_2\\text{OH} + \\text{HBr} \\rightarrow \\text{CH}_3\\text{CH}_2\\text{Br} + \\text{H}_2\\text{O}$\nC $\\text{CH}_2=\\text{CH}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{CH}_3\\text{CH}_2\\text{OH}$\nD $\\text{CH}_2=\\text{CH}_2 + \\text{H}_2 \\rightarrow \\text{CH}_3\\text{CH}_3$",
    memo="A $\\checkmark\\checkmark$\n\n**Reasoning:**\nHydrolysis is the reaction of a compound with water; specifically, the substitution reaction of a haloalkane with water to form an alcohol and hydrogen halide. Option A is the hydrolysis of bromoethane to ethanol. Option B is haloalkane substitution from an alcohol, Option C is hydration (addition of water to an alkene), and Option D is hydrogenation (addition of hydrogen).",
    final_answer="A"
)

add_item(
    ref="1.4",
    marks=2,
    topic="Reaction Kinetics - Surface Area and Volume of Gas Produced",
    passage="[DIAGRAM: Reaction conditions in test tubes X and Y | Test tube X contains $100\\text{ cm}^3$ of $0{,}1\\text{ mol}\\cdot\\text{dm}^{-3}\\text{ HCl}(aq)$ and zinc powder. Test tube Y contains $200\\text{ cm}^3$ of $0{,}1\\text{ mol}\\cdot\\text{dm}^{-3}\\text{ HCl}(aq)$ and zinc lumps. The mass of zinc used is the same in both test tubes, and hydrochloric acid is in excess.]",
    question="Hydrochloric acid reacts with EXCESS zinc:\n$$\\text{Zn}(s) + 2\\text{HCl}(aq) \\rightarrow \\text{ZnCl}_2(aq) + \\text{H}_2(g)$$\n\nDifferent reaction conditions are shown in the diagrams below. The mass of zinc used is the same in both test tubes.\n\nHow will the INITIAL rate of reaction and FINAL VOLUME of $\\text{H}_2(g)$ produced in test tube Y compare with that in test tube X?\n\n| | INITIAL RATE OF REACTION IN Y | FINAL VOLUME OF $\\text{H}_2(g)$ IN Y |\n| :--- | :--- | :--- |\n| A | Higher | Equal |\n| B | Lower | More |\n| C | Lower | Equal |\n| D | Higher | More |",
    memo="B $\\checkmark\\checkmark$\n\n**Reasoning:**\n1. Initial rate: Zinc lumps in test tube Y have a smaller exposed surface area than zinc powder in test tube X, resulting in fewer effective collisions per unit time and thus a LOWER initial reaction rate in Y.\n2. Final volume of gas: Zinc is in EXCESS in both test tubes, which means $\\text{HCl}$ is the limiting reagent. In test tube X: $n(\\text{HCl}) = c \\times V = (0{,}1)(0{,}100) = 0{,}01\\text{ mol}$. In test tube Y: $n(\\text{HCl}) = c \\times V = (0{,}1)(0{,}200) = 0{,}02\\text{ mol}$. Because test tube Y contains twice the amount of the limiting reactant $\\text{HCl}$, it produces MORE final volume of $\\text{H}_2(g)$.",
    final_answer="B"
)

add_item(
    ref="1.5",
    marks=2,
    topic="Chemical Equilibrium - Equilibrium Constant from Molecular Model",
    passage="[DIAGRAM: Particle model in a $1\\text{ dm}^3$ container at equilibrium at $T\\,^\\circ\\text{C}$ | A square box containing 12 black circles representing $\\text{NO}_2$ molecules and 6 white circles representing $\\text{N}_2\\text{O}_4$ molecules at equilibrium. Key: Black circle = $\\text{NO}_2$, White circle = $\\text{N}_2\\text{O}_4$.]",
    question="The diagram below represents a mixture of $\\text{NO}_2(g)$ and $\\text{N}_2\\text{O}_4(g)$ molecules at equilibrium in a $1\\text{ dm}^3$ container at $T\\,^\\circ\\text{C}$.\n\nThe balanced equation for this reaction is:\n$$2\\text{NO}_2(g) \\rightleftharpoons \\text{N}_2\\text{O}_4(g)$$\n\nWhich ONE of the following is TRUE for the value of the equilibrium constant, $K_c$, for the reaction at $T\\,^\\circ\\text{C}$?\n\nA $K_c = 24$\nB $K_c > 1$\nC $K_c = 1$\nD $0 < K_c < 1$",
    memo="D $\\checkmark\\checkmark$\n\n**Reasoning:**\nVolume $V = 1\\text{ dm}^3$.\nAt equilibrium:\nNumber of $\\text{NO}_2$ particles $= 12 \\implies [\\text{NO}_2] = 12\\text{ mol}\\cdot\\text{dm}^{-3}$\nNumber of $\\text{N}_2\\text{O}_4$ particles $= 6 \\implies [\\text{N}_2\\text{O}_4] = 6\\text{ mol}\\cdot\\text{dm}^{-3}$\n$$K_c = \\frac{[\\text{N}_2\\text{O}_4]}{[\\text{NO}_2]^2} = \\frac{6}{12^2} = \\frac{6}{144} = \\frac{1}{24} \\approx 0{,}0417$$\nSince $0 < \\frac{1}{24} < 1$, option D is correct.",
    final_answer="D"
)

add_item(
    ref="1.6",
    marks=2,
    topic="Chemical Equilibrium - Heterogeneous Systems and Volume Change",
    passage="",
    question="A reaction is at equilibrium in a closed container according to the following balanced equation:\n$$4\\text{CuO}(s) \\rightleftharpoons 2\\text{Cu}_2\\text{O}(s) + \\text{O}_2(g)$$\n\nThe volume of the container is now increased while the temperature remains constant. A new equilibrium is reached. Which ONE of the following combinations is CORRECT for the new equilibrium?\n\n| | CONCENTRATION OF $\\text{O}_2$ | NUMBER OF MOLES OF $\\text{O}_2$ | EQUILIBRIUM CONSTANT ($K_c$) |\n| :--- | :--- | :--- | :--- |\n| A | Decreases | Remains the same | Increases |\n| B | Remains the same | Decreases | Remains the same |\n| C | Remains the same | Increases | Remains the same |\n| D | Decreases | Increases | Remains the same |",
    memo="C $\\checkmark\\checkmark$\n\n**Reasoning:**\nIn this heterogeneous equilibrium involving solids and gas, the equilibrium constant expression is $K_c = [\\text{O}_2]$.\n1. Since temperature remains constant, $K_c$ remains constant (remains the same).\n2. Because $K_c = [\\text{O}_2]$ and $K_c$ is unchanged, the equilibrium concentration of $[\\text{O}_2]$ must return to its original value at the new equilibrium (remains the same).\n3. When the volume $V$ is increased, pressure momentarily drops. By Le Chatelier's principle, the forward reaction is favoured to increase pressure. Because $[\\text{O}_2] = \\frac{n}{V}$ returns to the same constant value in a larger volume $V$, the number of moles of $\\text{O}_2$ ($n = [\\text{O}_2] \\times V$) must increase.",
    final_answer="C"
)

add_item(
    ref="1.7",
    marks=2,
    topic="Acids and Bases - Comparison of Strong and Weak Monoprotic Acids",
    passage="",
    question="Nitric acid, $\\text{HNO}_3(aq)$, and ethanoic acid, $\\text{CH}_3\\text{COOH}(aq)$, of equal volumes and concentrations are compared. Consider the following statements regarding these solutions:\n(i) They have different pH values.\n(ii) Both have the same electrical conductivity.\n(iii) Both solutions require the same number of moles of $\\text{KOH}(aq)$ for complete neutralisation.\n\nWhich of the above statement(s) is/are TRUE?\n\nA (i) only\nB (i) and (ii) only\nC (i) and (iii) only\nD (ii) and (iii) only",
    memo="C $\\checkmark\\checkmark$\n\n**Reasoning:**\n$\\text{HNO}_3$ is a strong monoprotic acid (ionises completely) while $\\text{CH}_3\\text{COOH}$ is a weak monoprotic acid (ionises incompletely).\n- Statement (i) is TRUE: Because $\\text{HNO}_3$ ionises completely, its $[\\text{H}_3\\text{O}^+]$ is higher than that of ethanoic acid of the same concentration, giving $\\text{HNO}_3$ a lower pH.\n- Statement (ii) is FALSE: With a much higher ion concentration, $\\text{HNO}_3(aq)$ has a higher electrical conductivity than $\\text{CH}_3\\text{COOH}(aq)$.\n- Statement (iii) is TRUE: Both acids are monoprotic and have equal volumes and concentrations, so they contain the exact same initial number of moles of acid ($n = c \\times V$). Neutralisation with monoprotic $\\text{KOH}$ follows a $1:1$ stoichiometric ratio, so both require the same number of moles of $\\text{KOH}$.",
    final_answer="C"
)

add_item(
    ref="1.8",
    marks=2,
    topic="Acids and Bases - Titration Curve and Endpoint Overshoot",
    passage="[DIAGRAM: Titration setup | A burette containing $\\text{HCl}(aq)$ dripping into an Erlenmeyer flask containing $\\text{KOH}(aq)$ titration mixture.]",
    question="The apparatus in the diagram below is used for the titration between $\\text{HCl}(aq)$ and $\\text{KOH}(aq)$.\n\nIn a titration, the learner accidentally exceeds the endpoint. Which ONE of the following will be TRUE for the titration mixture?\n\nA $[\\text{H}^+] > [\\text{OH}^-]$ and $\\text{pH} < 7$\nB $[\\text{H}^+] < [\\text{OH}^-]$ and $\\text{pH} < 7$\nC $[\\text{H}^+] < [\\text{OH}^-]$ and $\\text{pH} > 7$\nD $[\\text{H}^+] > [\\text{OH}^-]$ and $\\text{pH} > 7$",
    memo="A $\\checkmark\\checkmark$\n\n**Reasoning:**\nThe acid $\\text{HCl}(aq)$ is added from the burette into the base $\\text{KOH}(aq)$ in the flask. Exceeding the endpoint means that excess acid $\\text{HCl}(aq)$ has been added beyond the neutralisation point. The resulting mixture in the flask is therefore acidic, with $[\\text{H}^+] > [\\text{OH}^-]$ and $\\text{pH} < 7$ at $25\\,^\\circ\\text{C}$.",
    final_answer="A"
)

add_item(
    ref="1.9",
    marks=2,
    topic="Electrochemistry - Standard Reduction Potentials and Galvanic Cell Emf",
    passage="",
    question="The following hypothetical standard reduction potentials relate to a galvanic cell:\n$$\\text{X}^{2+}(aq) + 2e^- \\rightarrow \\text{X}(s) \\quad E^\\theta = +0{,}10\\text{ V}$$\n$$\\text{Y}^+(aq) + e^- \\rightarrow \\text{Y}(s) \\quad E^\\theta = -0{,}10\\text{ V}$$\n\nConsider the following statements for this galvanic cell:\n(i) The emf of the cell is $0{,}20\\text{ V}$ under standard conditions.\n(ii) Electrode Y is the anode.\n(iii) X is oxidised.\n\nWhich of the above statement(s) is/are TRUE for this galvanic cell?\n\nA (i) only\nB (i) and (ii) only\nC (i) and (iii) only\nD (ii) and (iii) only",
    memo="B $\\checkmark\\checkmark$\n\n**Reasoning:**\n- Comparing standard reduction potentials: $E^\\theta(\\text{X}^{2+}/\\text{X}) = +0{,}10\\text{ V}$ (more positive $\\rightarrow$ cathode, reduction), $E^\\theta(\\text{Y}^+/\\text{Y}) = -0{,}10\\text{ V}$ (more negative $\\rightarrow$ anode, oxidation).\n- Statement (i) is TRUE: $E^\\theta_{\\text{cell}} = E^\\theta_{\\text{cathode}} - E^\\theta_{\\text{anode}} = (+0{,}10) - (-0{,}10) = 0{,}20\\text{ V}$.\n- Statement (ii) is TRUE: Electrode Y has the lower reduction potential and is therefore the anode where oxidation takes place ($\\text{Y} \\rightarrow \\text{Y}^+ + e^-$).\n- Statement (iii) is FALSE: $\\text{X}^{2+}$ is reduced at the cathode, not oxidised.",
    final_answer="B"
)

add_item(
    ref="1.10",
    marks=2,
    topic="Electrochemistry - Anode Half-reaction in Electrolysis of Concentrated CuCl2",
    passage="",
    question="Which ONE of the half-reactions below will be the MAIN reaction at the ANODE during the electrolysis of CONCENTRATED $\\text{CuCl}_2(aq)$?\n\nA $\\text{Cu}^{2+}(aq) + 2e^- \\rightarrow \\text{Cu}(s)$\nB $2\\text{H}_2\\text{O}(l) + 2e^- \\rightarrow \\text{H}_2(g) + 2\\text{OH}^-(aq)$\nC $2\\text{H}_2\\text{O}(l) \\rightarrow \\text{O}_2(g) + 4\\text{H}^+(aq) + 4e^-$\nD $2\\text{Cl}^-(aq) \\rightarrow \\text{Cl}_2(g) + 2e^-$",
    memo="D $\\checkmark\\checkmark$\n\n**Reasoning:**\nAt the anode, oxidation takes place (electrons are lost). The anions available in the solution are $\\text{Cl}^-(aq)$ and $\\text{H}_2\\text{O}(l)$. In a CONCENTRATED chloride solution, chloride ions are preferentially oxidised to chlorine gas over water: $2\\text{Cl}^-(aq) \\rightarrow \\text{Cl}_2(g) + 2e^-$. Options A and B are reduction half-reactions that take place at the cathode.",
    final_answer="D"
)

# ==============================================================================
# QUESTION 2 (10 items, 16 marks total)
# ==============================================================================

q2_passage = (
    "[TABLE: Organic compounds A to H | "
    "A: Heptanoic acid; "
    "B: CH3(CH2)3COOCH3; "
    "C: 4-ethyl-3,3-difluorohexane; "
    "D: Hexanoic acid; "
    "E: [DIAGRAM: Structural formula | CH3-CH(CH3)-C(=CH2)-CH3]; "
    "F: [DIAGRAM: Structural formula | CH3-CH(CH3)-C(=O)-CH2-CH3]; "
    "G: [DIAGRAM: Structural formula | (CH3)2C(CH2CH3)-COOH, i.e. 2,2-dimethylbutanoic acid]; "
    "H: [DIAGRAM: Structural formula | CH3-CH2-C(=O)-CH3, i.e. butan-2-one]]"
)

add_item(
    ref="2.1",
    marks=1,
    topic="Organic Chemistry - Definition of Organic Compound",
    passage=q2_passage,
    question="Define the term organic compound.",
    memo="Molecules/compounds containing carbon (atoms). $\\checkmark$\n(Molekule/verbinding wat koolstof(atome) bevat.)",
    final_answer="Molecules containing carbon atoms"
)

add_item(
    ref="2.2.1",
    marks=2,
    topic="Organic Chemistry - IUPAC Naming of Alkenes",
    passage=q2_passage,
    question="Write down the IUPAC name of compound E.",
    memo="2,3-dimethylbut-1-ene $\\checkmark\\checkmark$ / 2,3-dimethyl-1-butene\n(2,3-dimetielbut-1-een / 2,3-dimetiel-1-buteen)\n\nMarking criteria:\n- Correct stem i.e. but-1-ene $\\checkmark$\n- IUPAC name completely correct including numbering, sequence, hyphens and commas $\\checkmark$",
    final_answer="2,3-dimethylbut-1-ene"
)

add_item(
    ref="2.2.2",
    marks=2,
    topic="Organic Chemistry - IUPAC Naming of Ketones",
    passage=q2_passage,
    question="Write down the IUPAC name of compound H.",
    memo="Butan-2-one / 2-butanone / butanone $\\checkmark\\checkmark$\n(Butan-2-oon / 2-butanoon / butanoon)\n\nMarking criteria:\n- Correct chain length, i.e. But $\\checkmark$\n- Everything else correct: IUPAC name completely correct including numbering, sequence, hyphens and commas $\\checkmark$",
    final_answer="Butan-2-one"
)

add_item(
    ref="2.3.1",
    marks=2,
    topic="Organic Chemistry - Structural Formula of Esters",
    passage=q2_passage,
    question="Write down the STRUCTURAL formula of compound B.",
    memo="Marking criteria:\n- Functional group correct ($-\\text{C}(=\\text{O})-\\text{O}-$) $\\checkmark$\n- Whole structure correct $\\checkmark$\n\nStructural representation of methyl pentanoate:\n$$\\text{H}-\\text{C}(\\text{H})_2-\\text{C}(\\text{H})_2-\\text{C}(\\text{H})_2-\\text{C}(\\text{H})_2-\\text{C}(=\\text{O})-\\text{O}-\\text{C}(\\text{H})_3$$\n\nNotes:\n- If more than one functional group / wrong functional group: 0/2.\n- If condensed structural formulae used: Max 1/2.",
    final_answer="CH3-CH2-CH2-CH2-COO-CH3"
)

add_item(
    ref="2.3.2",
    marks=3,
    topic="Organic Chemistry - Structural Formula of Haloalkanes",
    passage=q2_passage,
    question="Write down the STRUCTURAL formula of compound C.",
    memo="Marking criteria:\n- Six C atoms in longest chain $\\checkmark$\n- Two F atoms on third C atom $\\checkmark$\n- Ethyl substituent on fourth C atom $\\checkmark$\n\nStructural representation of 4-ethyl-3,3-difluorohexane:\n$$\\text{CH}_3-\\text{CH}_2-\\text{C}(\\text{F})_2-\\text{CH}(\\text{CH}_2\\text{CH}_3)-\\text{CH}_2-\\text{CH}_3$$\n(In full structural formula, all 6 carbon atoms of the parent chain are drawn with explicit single bonds to hydrogens, two fluorine atoms on carbon 3, and an ethyl group $-\\text{CH}_2-\\text{CH}_3$ on carbon 4).\n\nNotes:\n- If H-atom or bond omitted: Max 2/3.\n- If condensed structural formulae used: Max 2/3.",
    final_answer="CH3-CH2-CF2-CH(CH2CH3)-CH2-CH3"
)

add_item(
    ref="2.3.3",
    marks=1,
    topic="Organic Chemistry - General Formula of Alkenes",
    passage=q2_passage,
    question="Write down the General formula of the homologous series to which compound E belongs.",
    memo="$\\text{C}_n\\text{H}_{2n} \\checkmark$\n(Compound E is an alkene)",
    final_answer="C_n H_2n"
)

add_item(
    ref="2.3.4",
    marks=1,
    topic="Organic Chemistry - Structural Formula of Ketone Functional Group",
    passage=q2_passage,
    question="Write down the STRUCTURAL formula of the FUNCTIONAL group of compound F.",
    memo="Structural formula of carbonyl group bonded to two carbon atoms:\n$$-\\text{C}-\\text{C}(=\\text{O})-\\text{C}- \\quad \\text{or} \\quad >\\text{C}=\\text{O} \\quad \\text{or} \\quad -\\text{C}(=\\text{O})- \\checkmark$$\nACCEPT:\n$$\\text{R}-\\text{C}(=\\text{O})-\\text{R}'$$",
    final_answer="-C(=O)-"
)

add_item(
    ref="2.3.5",
    marks=2,
    topic="Organic Chemistry - Alcohol Reagent in Esterification",
    passage=q2_passage,
    question="Write down the IUPAC name of the alcohol needed to produce compound B.",
    memo="Methanol / Metanol $\\checkmark\\checkmark$\n\nNOTE: 1-methanol / methan-1-ol: Max 1/2.",
    final_answer="Methanol"
)

add_item(
    ref="2.4.1",
    marks=1,
    topic="Organic Chemistry - Functional Isomers",
    passage=q2_passage,
    question="Write down the letter(s) of the compound(s) that: Is a FUNCTIONAL isomer of compound G.",
    memo="B $\\checkmark$\n(Compound G is a carboxylic acid, 2,2-dimethylbutanoic acid $\\text{C}_6\\text{H}_{12}\\text{O}_2$. Compound B is an ester, methyl pentanoate $\\text{C}_6\\text{H}_{12}\\text{O}_2$. Carboxylic acids and esters are functional isomers).",
    final_answer="B"
)

add_item(
    ref="2.4.2",
    marks=1,
    topic="Organic Chemistry - Chain Isomers",
    passage=q2_passage,
    question="Write down the letter(s) of the compound(s) that: Are CHAIN isomers of each other.",
    memo="D and G $\\checkmark$\n(Compound D is hexanoic acid, a straight-chain carboxylic acid with 6 carbons, and compound G is 2,2-dimethylbutanoic acid, a branched-chain carboxylic acid with 6 carbons. Both have the same molecular formula $\\text{C}_6\\text{H}_{12}\\text{O}_2$).",
    final_answer="D and G"
)

# ==============================================================================
# QUESTION 3 (8 items, 15 marks total)
# ==============================================================================

q3_passage = (
    "[DIAGRAM: Graph of Boiling Point versus Molecular Mass | "
    "Y-axis: Boiling point ($^\\circ\\text{C}$), scaled from 0 to 250 in steps of 50 (minor grid = 10 $^\\circ\\text{C}$). "
    "X-axis: Molecular mass ($\\text{g}\\cdot\\text{mol}^{-1}$), scaled from 30 to 130 in steps of 20 (minor grid = 2 $\\text{g}\\cdot\\text{mol}^{-1}$). "
    "Three curves are obtained for straight chain molecules of aldehydes, carboxylic acids and primary alcohols: "
    "Curve P (dashed line, highest boiling points: carboxylic acids; points plotted at molecular masses 46, 60, 74, 88, 102, 116 with boiling points approximately 101, 118, 141, 164, 186, 205 $^\\circ\\text{C}$); "
    "Curve R (solid line, intermediate boiling points: primary alcohols; points plotted at molecular masses 46, 60, 74, 88, 102, 116 with boiling points approximately 78, 97, 118, 138, 157, 176 $^\\circ\\text{C}$); "
    "Curve S (dash-dot line, lowest boiling points: aldehydes; points plotted at molecular masses 44, 58, 72, 86, 100, 114 with boiling points approximately 21, 48, 75, 103, 130, 153 $^\\circ\\text{C}$)]"
)

add_item(
    ref="3.1",
    marks=2,
    topic="Physical Properties - Definition of Boiling Point",
    passage=q3_passage,
    question="Define the term boiling point.",
    memo="The temperature at which the vapour pressure of a substance equals atmospheric pressure. $\\checkmark\\checkmark$\n(Die temperatuur waarby die dampdruk van die stof gelyk is aan atmosferiese druk.)\n\nMarking criteria:\nIf any one of the underlined key phrases (temperature / vapour pressure / atmospheric pressure) in the correct context is omitted, deduct 1 mark.",
    final_answer="The temperature at which the vapour pressure of a substance equals atmospheric pressure."
)

add_item(
    ref="3.2",
    marks=2,
    topic="Physical Properties - Conclusion from Boiling Point Curve",
    passage=q3_passage,
    question="Write down the conclusion that can be made for curve P.",
    memo="OPTION 1:\nMarking criteria:\n- Dependent and independent variables correctly identified $\\checkmark$\n- Correct relationship between dependent and independent variables stated $\\checkmark$\n\nThe higher the molecular mass the higher the boiling point. $\\checkmark\\checkmark$\nOR: As the molecular mass increases the boiling point increases.\nOR: The longer the C-chain the higher boiling point.\nOR: The boiling point and the molecular mass are proportional.\n(Note: If 'Directly proportional': Max 1/2)\n\nOPTION 2:\nCurve P represents carboxylic acids. $\\checkmark\\checkmark$\nOR: For every molar mass, P has the highest boiling point.",
    final_answer="The higher the molecular mass the higher the boiling point"
)

add_item(
    ref="3.3",
    marks=2,
    topic="Physical Properties - Explaining Boiling Point Trend in Terms of Structure",
    passage=q3_passage,
    question="Explain the answer to QUESTION 3.2 in terms of the structures of the compounds.",
    memo="Marking criteria:\n- Strength of intermolecular forces $\\checkmark$\n- Energy required to overcome intermolecular forces $\\checkmark$\n\nOPTION 1 (corresponding to Option 1 in 3.2):\n- Strength of the intermolecular forces increases / More sites for London forces with increase of molar mass/chain length/surface area. $\\checkmark$\n- More energy is needed to overcome/break intermolecular forces. $\\checkmark$\n\nOPTION 2 (corresponding to Option 2 in 3.2):\n- Curve P/carboxylic acids has strongest intermolecular forces. $\\checkmark$\n- Most energy is needed to overcome/break intermolecular forces. $\\checkmark$",
    final_answer="With increasing molecular mass/chain length, surface area increases, strength of intermolecular forces increases, and more energy is required to overcome the intermolecular forces."
)

add_item(
    ref="3.4.1",
    marks=1,
    topic="Physical Properties - Identifying Homologous Series from Boiling Points",
    passage=q3_passage,
    question="Curve R represents the alcohols. Which homologous series is represented by curve S?",
    memo="Aldehyde / Aldehiede $\\checkmark$",
    final_answer="Aldehydes"
)

add_item(
    ref="3.4.2",
    marks=2,
    topic="Physical Properties - Intermolecular Forces in Aldehydes",
    passage=q3_passage,
    question="Explain the answer to QUESTION 3.4.1 by referring to the strength of intermolecular forces.",
    memo="Marking criteria:\n- Comparing the strength of intermolecular forces of aldehydes/S with alcohols/R and/or carboxylic acids/P $\\checkmark$\n- Linking the intermolecular forces to boiling point/energy needed $\\checkmark$\n\nFull Solution:\n- Aldehydes/S have the weakest/weaker intermolecular forces (dipole-dipole forces). $\\checkmark$\n- Therefore, aldehydes/S have the lowest/lower boiling points / least/lower energy needed to overcome/break intermolecular forces. $\\checkmark$\n\nOR:\n- The strength of the intermolecular forces in aldehydes/S is weaker than in alcohols/R / carboxylic acids/P. $\\checkmark$\n- Therefore, aldehydes/S have lower boiling points / need less energy than alcohols/carboxylic acids to overcome/break intermolecular forces. $\\checkmark$\n\nOR:\n- Carboxylic acids/P and alcohols/R have stronger intermolecular forces (hydrogen bonds) than aldehydes/S. $\\checkmark$\n- Therefore, carboxylic acids/P and/or alcohols/R have higher boiling points / need more energy than aldehydes to overcome/break intermolecular forces. $\\checkmark$",
    final_answer="Aldehydes have weaker intermolecular forces (dipole-dipole forces) than alcohols and carboxylic acids (hydrogen bonding), so less energy is needed to overcome intermolecular forces, resulting in lower boiling points."
)

add_item(
    ref="3.5.1",
    marks=1,
    topic="Physical Properties - Molecular Mass from Boiling Point Curve",
    passage=q3_passage,
    question="For curve R, write down the: Molecular mass of the compound with a boiling point of $97\\,^\\circ\\text{C}$.",
    memo="$60\\text{ (g}\\cdot\\text{mol}^{-1}\\text{)} \\checkmark$\nRange: 58 - 62 $\\text{g}\\cdot\\text{mol}^{-1}$",
    final_answer="60"
)

add_item(
    ref="3.5.2",
    marks=2,
    topic="Physical Properties - IUPAC Naming of Primary Alcohols",
    passage=q3_passage,
    question="For curve R, write down the: IUPAC name of the compound in QUESTION 3.5.1.",
    memo="Propan-1-ol / 1-propanol $\\checkmark\\checkmark$\n\nMarking criteria:\n- Correct stem of alcohol, i.e. Propanol $\\checkmark$\n- Correct position of functional group and everything else correct: IUPAC name completely correct including numbering and hyphens $\\checkmark$",
    final_answer="Propan-1-ol"
)

add_item(
    ref="3.6",
    marks=3,
    topic="Physical Properties - Comparing Hydrogen Bonding in Alcohols and Carboxylic Acids",
    passage=q3_passage,
    question="Two compounds, A and B, used in this investigation have a molecular mass of $74\\text{ g}\\cdot\\text{mol}^{-1}$. A has a boiling point of $118\\,^\\circ\\text{C}$ and B a boiling point of $142\\,^\\circ\\text{C}$. Explain the difference in these boiling points by referring to the structures of these compounds.",
    memo="Marking criteria:\n- State that carboxylic acids have two sites for hydrogen bonding $\\checkmark$\n- State that alcohols have one site for hydrogen bonding $\\checkmark$\n- Comparing the strength of IMFs / the energy needed to overcome IMFs $\\checkmark$\n\nFull Solution:\n- Carboxylic acids / B / Propanoic acid have, (in addition to London forces and dipole-dipole forces), two sites for hydrogen bonding between molecules $\\checkmark$ (OR: can form dimers due to strong hydrogen bonding between molecules).\n- Alcohols / A / Butan-1-ol have, (in addition to London forces and dipole-dipole forces), one site for hydrogen bonding between molecules. $\\checkmark$\n- Intermolecular forces in carboxylic acids are stronger $\\checkmark$ (OR: More energy is needed to overcome/break intermolecular forces in carboxylic acid/B/propanoic acid).",
    final_answer="Carboxylic acid B has two sites for hydrogen bonding (forms dimers), whereas alcohol A has only one site for hydrogen bonding; intermolecular forces in B are stronger, requiring more energy to overcome."
)

# ==============================================================================
# QUESTION 4 (10 items, 19 marks total)
# ==============================================================================

q4_passage = (
    "[TABLE: Reactions I to III | "
    "Reaction I: CH3CH2CH=CHCH3 + HCl -> A + B; "
    "Reaction II: A + H2O (with heat, Delta) -> CH3CH2CH2CH(OH)CH3 + X; "
    "Reaction III: CH3CH2CH2CH(OH)CH3 -> CH3CH2CH=CHCH3 + H2O. "
    "A and B represent organic compounds that are POSITIONAL ISOMERS. X is an inorganic product.]"
)

add_item(
    ref="4.1.1",
    marks=2,
    topic="Organic Reactions - Definition of Cracking",
    passage="Consider the cracking reaction below:\n$$\\text{C}_{16}\\text{H}_{34} \\rightarrow \\text{C}_6\\text{H}_{14} + \\text{C}_6\\text{H}_x + 2\\text{C}_y\\text{H}_z$$",
    question="Define cracking.",
    memo="The chemical process/reaction in which longer chain hydrocarbon/alkane molecules are broken down to shorter (more useful) molecules. $\\checkmark\\checkmark$\n(Die chemiese proses/reaksie waarin langer kettingkoolwaterstof/alkaan-molekule afgebreek word in korter (meer bruikbare) molekules.)\n\nMarking criteria:\nIf any one of the underlined key phrases (chemical process / longer chain hydrocarbons broken down / shorter molecules) in the correct context is omitted, deduct 1 mark.",
    final_answer="The chemical process in which longer chain hydrocarbons are broken down into shorter molecules."
)

add_item(
    ref="4.1.2",
    marks=3,
    topic="Organic Reactions - Balancing Cracking Equation",
    passage="Consider the cracking reaction below:\n$$\\text{C}_{16}\\text{H}_{34} \\rightarrow \\text{C}_6\\text{H}_{14} + \\text{C}_6\\text{H}_x + 2\\text{C}_y\\text{H}_z$$",
    question="Write down the values represented by x, y and z in the equation above.",
    memo="$x = 12 \\checkmark$\n$y = 2 \\checkmark$\n$z = 4 \\checkmark$\n\nACCEPT:\n$$\\text{C}_{16}\\text{H}_{34} \\rightarrow \\text{C}_6\\text{H}_{14} + \\text{C}_6\\text{H}_{12} + 2\\text{C}_2\\text{H}_4$$",
    final_answer="x = 12, y = 2, z = 4"
)

add_item(
    ref="4.1.3",
    marks=3,
    topic="Organic Reactions - Complete Combustion of Alkanes",
    passage="Compound $\\text{C}_6\\text{H}_{14}$ undergoes complete combustion.",
    question="Using MOLECULAR FORMULAE, write down the balanced equation for this reaction.",
    memo="$$2\\text{C}_6\\text{H}_{14} + 19\\text{O}_2 \\checkmark \\rightarrow 12\\text{CO}_2 + 14\\text{H}_2\\text{O} \\checkmark \\quad \\text{Bal } \\checkmark$$\n\nMarking criteria:\n- $\\text{O}_2 \\checkmark$\n- Products $\\checkmark$\n- Balancing $\\checkmark$\n\nNotes:\n- Ignore double arrows and phases.\n- If condensed structural formulae used: Max 2/3.",
    final_answer="2C6H14 + 19O2 -> 12CO2 + 14H2O"
)

add_item(
    ref="4.2.1",
    marks=2,
    topic="Organic Chemistry - Definition of Positional Isomers",
    passage=q4_passage,
    question="Write down the: Definition of positional isomers",
    memo="Compounds with the same molecular formula, but different positions of the side chain / substituents / functional groups on the parent chain. $\\checkmark\\checkmark$\n(Verbindings met dieselfde molekulêre formule, maar verskillende posisies van die syketting / substituente / funksionele groepe op die stamketting.)\n\nMarking criteria:\nIf any one of the underlined key phrases (same molecular formula / different positions / functional groups or substituents on parent chain) in the correct context is omitted, deduct 1 mark.",
    final_answer="Compounds with the same molecular formula but different positions of functional groups or substituents on the parent chain."
)

add_item(
    ref="4.2.2",
    marks=1,
    topic="Organic Reactions - Hydrohalogenation Addition Reaction",
    passage=q4_passage,
    question="Write down the: Type of reaction represented by reaction I",
    memo="Addition / hydrohalogenation / hydrochlorination $\\checkmark$\n(Addisie / hidrohalogenering / hidrochlorinering)",
    final_answer="Addition (Hydrohalogenation)"
)

add_item(
    ref="4.2.3",
    marks=3,
    topic="Organic Reactions - Structural Formula of Haloalkane Positional Isomer",
    passage=q4_passage,
    question="Write down the: STRUCTURAL formula of compound B",
    memo="Marking criteria:\n- Chlorine atom bonded to any C-atom $\\checkmark$\n- Correct functional group on third C-atom (3-chloropentane) $\\checkmark$\n- Whole structure correct $\\checkmark$\n\nStructural representation of 3-chloropentane:\n$$\\text{H}-\\text{C}(\\text{H})_2-\\text{C}(\\text{H})_2-\\text{C}(\\text{H})(\\text{Cl})-\\text{C}(\\text{H})_2-\\text{C}(\\text{H})_3$$\n(In full structural formula, a 5-carbon straight chain with all H atoms shown with single bonds, and chlorine atom bonded to carbon 3).",
    final_answer="CH3-CH2-CH(Cl)-CH2-CH3"
)

add_item(
    ref="4.2.4",
    marks=1,
    topic="Organic Reactions - Inorganic Reaction Byproduct",
    passage=q4_passage,
    question="Write down the: Formula of X",
    memo="$\\text{HCl} \\checkmark$",
    final_answer="HCl"
)

add_item(
    ref="4.2.5",
    marks=1,
    topic="Organic Reactions - Acid Catalyst for Dehydration of Alcohols",
    passage=q4_passage,
    question="Write down the: Inorganic reagent for reaction III",
    memo="(Concentrated / conc.) $\\text{H}_2\\text{SO}_4$ / sulphuric acid / $\\text{H}_3\\text{PO}_4$ / phosphoric acid $\\checkmark$\n(Gekonsentreerde / gek. $\\text{H}_2\\text{SO}_4$ / swawelsuur / $\\text{H}_3\\text{PO}_4$ / fosforsuur)\n\nNote: If 'Dilute': 0/1.",
    final_answer="Concentrated H2SO4"
)

add_item(
    ref="4.2.6",
    marks=1,
    topic="Organic Reactions - Reaction Conditions for Dehydrohalogenation",
    passage=q4_passage,
    question="Compound A can be converted directly to the organic product of reaction III. Besides heat, write down the reaction condition needed for this conversion.",
    memo="Concentrated strong base $\\checkmark$\nOR: Concentrated $\\text{NaOH}$ / $\\text{KOH}$ / $\\text{LiOH}$ / sodium hydroxide / potassium hydroxide / lithium hydroxide\nOR: Strong base / $\\text{NaOH}$ / $\\text{KOH}$ / $\\text{LiOH}$ in ethanol\n(Gekonsentreerde sterk basis / gekonsentreerde $\\text{NaOH}$ / ens.)",
    final_answer="Concentrated strong base (e.g. concentrated NaOH in ethanol)"
)

add_item(
    ref="4.2.7",
    marks=2,
    topic="Organic Reactions - Reaction Types (Elimination and Dehydrohalogenation)",
    passage=q4_passage,
    question="Write down TWO terms that describe this type of reaction.",
    memo="- Elimination $\\checkmark$\n- Dehydrohalogenation / dehydrochlorination $\\checkmark$\n(Eliminasie $\\checkmark$, Dehidrohalogenering / dehidrochlorinering $\\checkmark$)",
    final_answer="Elimination, Dehydrohalogenation"
)

# ==============================================================================
# QUESTION 5 (6 items, 19 marks total)
# ==============================================================================

q5_passage = (
    "[TABLE: Reaction conditions and results for reaction: Na2S2O3(aq) + 2HCl(aq) -> 2NaCl(aq) + S(s) + H2O(l) + SO2(g) | "
    "Concentration of HCl(aq) used is 1 mol·dm^-3. The same volume of HCl(aq) is used in each run. "
    "The time taken for the cross on the paper under the flask to become invisible is measured. "
    "Run 1: Volume Na2S2O3 = 50 cm^3, Volume H2O added = 0 cm^3, Concentration Na2S2O3 = 0,13 mol·dm^-3, Time = 20,4 s; "
    "Run 2: Volume Na2S2O3 = 40 cm^3, Volume H2O added = 10 cm^3, Concentration Na2S2O3 = 0,10 mol·dm^-3, Time = 26,7 s; "
    "Run 3: Volume Na2S2O3 = 30 cm^3, Volume H2O added = 20 cm^3, Concentration Na2S2O3 = P, Time = 33,3 s.]\n"
    "[DIAGRAM: Conical flask containing Na2S2O3(aq) + HCl(aq) resting on a sheet of white paper marked with a cross (+).]"
)

add_item(
    ref="5.1",
    marks=2,
    topic="Reaction Kinetics - Definition of Reaction Rate",
    passage=q5_passage,
    question="Define reaction rate.",
    memo="ANY ONE:\n- Change in concentration $\\checkmark$ of products/reactants per (unit) time. $\\checkmark$\n- Change in amount/number of moles/volume/mass of products or reactants per (unit) time. $\\checkmark\\checkmark$\n- Amount/number of moles/volume/mass of products formed/reactants used per (unit) time. $\\checkmark\\checkmark$\n- Rate of change in concentration/amount/number of moles/volume/mass. $\\checkmark\\checkmark$ (2 or 0)\n\n(Verandering in konsentrasie van produkte/reaktanse per (eenheid) tyd.)",
    final_answer="Change in concentration of products or reactants per unit time."
)

add_item(
    ref="5.2",
    marks=1,
    topic="Reaction Kinetics - Identification of Independent Variable",
    passage=q5_passage,
    question="Write down the independent variable for this investigation.",
    memo="Concentration (of $\\text{Na}_2\\text{S}_2\\text{O}_3$) $\\checkmark$\n(Konsentrasie (van $\\text{Na}_2\\text{S}_2\\text{O}_3$))",
    final_answer="Concentration of Na2S2O3"
)

add_item(
    ref="5.3",
    marks=3,
    topic="Reaction Kinetics - Concentration Calculation after Dilution",
    passage=q5_passage,
    question="Calculate the value of P in the table.",
    memo="Marking criteria:\n- Substitute 0,03 and 0,13 OR 30 and 0,13 $\\checkmark$\n- Substitute 0,05 OR 50 $\\checkmark$\n- Final correct answer: $0{,}078\\text{ mol}\\cdot\\text{dm}^{-3} \\checkmark$ (Range: 0,075 to 0,08 $\\text{mol}\\cdot\\text{dm}^{-3}$)\n\nOPTION 1 (Using dilution formula):\n$$c_1 V_1 = c_2 V_2$$\n$$(0{,}13)(30) \\checkmark = c_2 (50) \\checkmark$$\n$$c_2 = 0{,}078\\text{ mol}\\cdot\\text{dm}^{-3} \\checkmark$$\n\nOPTION 2 (Using moles):\n$$n = cV = (0{,}13)(0{,}03) = 3{,}9 \\times 10^{-3}\\text{ mol}$$\n$$c = \\frac{n}{V} = \\frac{3{,}9 \\times 10^{-3}}{0{,}05} = 0{,}078\\text{ mol}\\cdot\\text{dm}^{-3}$$\n\nOPTION 3 (Using Run 2):\n$$(0{,}10)(40) = c_2 (50) \\implies c_2 = 0{,}075\\text{ mol}\\cdot\\text{dm}^{-3} \\checkmark$$\n\nOPTION 4 (Ratio):\n$$\\frac{30}{50} \\times 0{,}13 = 0{,}078\\text{ mol}\\cdot\\text{dm}^{-3}$$",
    final_answer="0.078"
)

add_item(
    ref="5.4",
    marks=5,
    topic="Reaction Kinetics - Quantitative Average Reaction Rate Calculation",
    passage=q5_passage,
    question="When $0{,}21\\text{ g}$ of sulphur has formed in Run 1, the cross becomes invisible. Calculate the average reaction rate with respect to sodium thiosulphate, $\\text{Na}_2\\text{S}_2\\text{O}_3(aq)$, in $\\text{g}\\cdot\\text{s}^{-1}$.",
    memo="Marking criteria:\n- Substitute $M = 32\\text{ g}\\cdot\\text{mol}^{-1}$ in formula $n(\\text{S}) = \\frac{m}{M} \\checkmark$\n- Use mol ratio: $n(\\text{S}) = n(\\text{Na}_2\\text{S}_2\\text{O}_3) \\checkmark$\n- Substitute $M = 158\\text{ g}\\cdot\\text{mol}^{-1}$ in formula $n(\\text{Na}_2\\text{S}_2\\text{O}_3) = \\frac{m}{M} \\checkmark$\n- Divide by $20{,}4\\text{ s} \\checkmark$\n- Final correct answer: $0{,}051\\text{ g}\\cdot\\text{s}^{-1} \\checkmark$ (Range: 0,048 to 0,080 $\\text{g}\\cdot\\text{s}^{-1}$)\n\nOPTION 1:\n$$n(\\text{S}) = \\frac{m}{M} = \\frac{0{,}21}{32} \\checkmark = 0{,}00656\\text{ mol}$$\n$$n(\\text{Na}_2\\text{S}_2\\text{O}_3) = n(\\text{S}) = 0{,}00656\\text{ mol} \\checkmark$$\n$$m(\\text{Na}_2\\text{S}_2\\text{O}_3) = n \\times M = (0{,}00656)(158) \\checkmark = 1{,}04\\text{ g}$$\n$$\\text{Rate} = \\frac{\\Delta m}{\\Delta t} = \\frac{1{,}04}{20{,}4} \\checkmark = 0{,}051\\text{ g}\\cdot\\text{s}^{-1} \\checkmark$$\n\nOPTION 2 (Using molar mass ratio):\n$$158\\text{ g Na}_2\\text{S}_2\\text{O}_3 \\checkmark \\rightarrow 32\\text{ g S} \\checkmark$$\n$$m(\\text{Na}_2\\text{S}_2\\text{O}_3) = \\frac{0{,}21 \\times 158}{32} = 1{,}04\\text{ g}$$\n$$\\text{Rate} = \\frac{1{,}04}{20{,}4} \\checkmark = 0{,}051\\text{ g}\\cdot\\text{s}^{-1} \\checkmark$$",
    final_answer="0.051"
)

add_item(
    ref="5.5",
    marks=4,
    topic="Reaction Kinetics - Maxwell-Boltzmann Distribution Curves at Different Temperatures",
    passage="Another investigation is performed at different temperatures.",
    question="Sketch the Maxwell-Boltzmann distribution curve for the reaction at $20\\,^\\circ\\text{C}$. Label this curve as A. On the same set of axis, draw the curve that will be obtained at $35\\,^\\circ\\text{C}$ and label it as B.",
    memo="[DIAGRAM: Maxwell-Boltzmann distribution curves at two temperatures | Y-axis: Number of particles (or Number of molecules), X-axis: Kinetic energy. Both curves start at origin (0,0). Curve A (at $20\,^\circ\text{C}$) has a higher peak located further to the left. Curve B (at $35\,^\circ\text{C}$) has a lower peak shifted to the right, and is higher than curve A at high kinetic energy values beyond the intersection point.]\n\nMarking criteria:\n- Both axes labelled correctly (Number of particles vs Kinetic energy) $\checkmark$\n- Both curves start at origin and have correct shape $\checkmark$\n- Peak of curve B must be lower than curve A $\checkmark$\n- Curve B must have higher kinetic energy than curve A from the peak up to end of curve B (shifted right / higher tail) $\checkmark$\n\nNotes:\n- If both curves end on the x-axis then B has to end to the right of A: Max 3/4.\n- Curves not labelled: Max 3/4.",
    final_answer="Graph sketch showing curve B with a lower, right-shifted peak and a higher tail than curve A."
)

add_item(
    ref="5.6",
    marks=4,
    topic="Reaction Kinetics - Collision Theory Explanation of Temperature Effect",
    passage="",
    question="Explain the effect of temperature on reaction rate in terms of the collision theory.",
    memo="OPTION 1:\n- At a higher temperature particles move faster / have higher kinetic energy. $\\checkmark$\n- More molecules have enough/sufficient kinetic energy for an effective collision (OR: more molecules have kinetic energy $E_k \\ge E_A$, activation energy). $\\checkmark$\n- More effective collisions per unit time/second (OR: Frequency of effective collisions increases). $\\checkmark$\n- Reaction rate increases. $\\checkmark$\n\nOPTION 2:\n- At a lower temperature particles move slower / have lower kinetic energy. $\\checkmark$\n- Less molecules have enough/sufficient kinetic energy for an effective collision (OR: $E_k \\ge E_A$). $\\checkmark$\n- Less effective collisions per unit time/second (OR: Frequency of effective collisions decreases). $\\checkmark$\n- Reaction rate decreases. $\\checkmark$",
    final_answer="At higher temperature, particles have higher average kinetic energy; more molecules have kinetic energy equal to or greater than the activation energy; frequency of effective collisions increases; reaction rate increases."
)

# ==============================================================================
# QUESTION 6 (8 items, 19 marks total)
# ==============================================================================

q6_passage = (
    "[DIAGRAM: Graph of Number of moles (mol) versus Time (s) for reaction: 2AB(g) <=> A2(g) + B2(g) in a 4 dm^3 closed container at $150\,^\circ\text{C}$ | "
    "X-axis: Time (s), scaled from 0 to 160 in increments of 20 (grid lines every 10 s). "
    "Three curves are shown: "
    "AB(g) (dashed line): starts at 13 mol at t = 0 s, decreases to 6 mol at t = 40 s and remains at 6 mol until t = 80 s (first equilibrium). From t = 80 s to 100 s, increases to 10 mol and remains at 10 mol until t = 130 s (second equilibrium). From t = 130 s to 140 s, increases to 12 mol and remains at 12 mol until 160 s (third equilibrium). "
    "A2(g) (solid line): starts at 0 mol at t = 0 s, increases to 4 mol at t = 40 s and remains at 4 mol until t = 80 s (first equilibrium). At t = 80 s, spikes vertically from 4 mol to 10 mol (disturbance: addition of A2). Between t = 80 s and 100 s, decreases to 8 mol and remains at 8 mol until t = 130 s (second equilibrium). Between t = 130 s and 140 s, decreases to 7 mol and remains at 7 mol until 160 s (third equilibrium). "
    "B2(g) (dash-dot line): starts at 0 mol at t = 0 s, increases to 4 mol at t = 40 s and remains at 4 mol until t = 80 s (first equilibrium). From t = 80 s to 100 s, decreases to 2 mol and remains at 2 mol until t = 130 s (second equilibrium). Between t = 130 s and 140 s, decreases to 1 mol and remains at 1 mol until 160 s (third equilibrium).]"
)

add_item(
    ref="6.1",
    marks=1,
    topic="Chemical Equilibrium - Meaning of Reversible Reaction",
    passage=q6_passage,
    question="Consider the following hypothetical reaction reaching equilibrium in a $4\\text{ dm}^3$ closed container at $150\\,^\\circ\\text{C}$:\n$$2\\text{AB}(g) \\rightleftharpoons \\text{A}_2(g) + \\text{B}_2(g)$$\n\nWrite down the meaning of the term reversible reaction.",
    memo="A reaction where products can be converted back to reactants $\\checkmark$ (and vice versa).\nOR: Both forward and reverse reactions can take place.\nOR: A reaction which can take place in both directions.\nOR: Products can be converted back to reactants.",
    final_answer="A reaction where products can be converted back to reactants."
)

add_item(
    ref="6.2",
    marks=2,
    topic="Chemical Equilibrium - Statement of Le Chatelier's Principle",
    passage=q6_passage,
    question="State Le Chatelier's principle.",
    memo="When the equilibrium in a closed system is disturbed, the system will re-instate a new equilibrium by favouring the reaction that will cancel/oppose the disturbance. $\\checkmark\\checkmark$\n(Wanneer die ewewig in 'n geslote sisteem versteur word, sal die sisteem 'n nuwe ewewig instel deur die reaksie te bevoordeel wat die versteuring kanselleer/teenwerk.)\n\nMarking criteria:\nIf any one of the underlined key phrases (equilibrium in closed system disturbed / reinstate new equilibrium / favouring reaction opposing disturbance) in correct context is omitted, deduct 1 mark.",
    final_answer="When the equilibrium in a closed system is disturbed, the system will reinstate a new equilibrium by favouring the reaction that opposes the disturbance."
)

add_item(
    ref="6.3.1",
    marks=1,
    topic="Chemical Equilibrium - Identification of Concentration Disturbance",
    passage=q6_passage,
    question="A change was made to the equilibrium mixture at $t = 80\\text{ s}$. Write down the change made at $t = 80\\text{ s}$.",
    memo="The amount/concentration of $\\text{A}_2(g)$ was increased / $\\text{A}_2$ was added to the container. $\\checkmark$\n(Die hoeveelheid/konsentrasie $\\text{A}_2(g)$ is verhoog / $\\text{A}_2$ is bygevoeg tot die houer.)",
    final_answer="Addition of A2(g)"
)

add_item(
    ref="6.3.2",
    marks=2,
    topic="Chemical Equilibrium - Le Chatelier Explanation of Disturbance Response",
    passage=q6_passage,
    question="Use Le Chatelier's principle to explain how the system reacts to this change.",
    memo="- Increase in $\\text{A}_2$ / concentration favours the reaction that uses or decreases the amount/concentration of $\\text{A}_2$. $\\checkmark$\n- The reverse reaction is favoured. $\\checkmark$\nOR: Amount or concentration of products decreases / Amount or concentration of reactants increases.",
    final_answer="The increase in [A2] favours the reaction that decreases [A2], so the reverse reaction is favoured."
)

add_item(
    ref="6.4",
    marks=4,
    topic="Chemical Equilibrium - Quantitative Calculation of Equilibrium Constant Kc",
    passage=q6_passage,
    question="Calculate the equilibrium constant, $K_c$, at $t = 120\\text{ s}$.",
    memo="OPTION 1 (Using concentration formula):\n$$K_c = \\frac{[\\text{A}_2][\\text{B}_2]}{[\\text{AB}]^2} \\checkmark$$\n$$K_c = \\frac{\\left(\\frac{8}{4}\\right)\\left(\\frac{2}{4}\\right)}{\\left(\\frac{10}{4}\\right)^2} \\checkmark\\checkmark = 0{,}16 \\checkmark$$\n\nOPTION 2 (Direct concentrations):\n$$[\\text{A}_2] = \\frac{8}{4} = 2\\text{ mol}\\cdot\\text{dm}^{-3}$$\n$$[\\text{B}_2] = \\frac{2}{4} = 0{,}5\\text{ mol}\\cdot\\text{dm}^{-3}$$\n$$[\\text{AB}] = \\frac{10}{4} = 2{,}5\\text{ mol}\\cdot\\text{dm}^{-3}$$\n$$K_c = \\frac{(2)(0{,}5)}{(2{,}5)^2} \\checkmark\\checkmark = 0{,}16 \\checkmark$$\n\nOPTION 3 / 4 (If candidate used first equilibrium at t = 40 to 80 s):\n$$K_c = \\frac{[\\text{A}_2][\\text{B}_2]}{[\\text{AB}]^2} = \\frac{(1)(1)}{(1{,}5)^2} = 0{,}44$$\n\nNotes:\n- Wrong $K_c$ expression: Max 2/4.\n- No $K_c$ expression: Max 3/4.",
    final_answer="0.16"
)

add_item(
    ref="6.5.1",
    marks=3,
    topic="Chemical Equilibrium - Potential Energy Diagram for Endothermic Reaction",
    passage="At $t = 130\\text{ s}$ the temperature of the system is decreased to $100\\,^\\circ\\text{C}$.",
    question="Draw a potential energy diagram for this reaction.",
    memo="[DIAGRAM: Potential energy profile of an endothermic reaction | Y-axis: Potential energy (or Ep), X-axis: Course of reaction (or Time). Reactants start at a lower energy level, rise over an activation energy peak, and finish at a higher energy level for products ($E_{\\text{products}} > E_{\\text{reactants}}$, $\\Delta H > 0$).]\n\nMarking criteria:\n- Both axes correctly labelled (Potential energy vs Course of reaction / Time) and shape of $E_p$ curve $\\checkmark$\n- Shape of $E_p$ curve for endothermic reaction as shown ($E_{\\text{products}} > E_{\\text{reactants}}$) $\\checkmark\\checkmark$",
    final_answer="Endothermic potential energy diagram where products have higher potential energy than reactants."
)

add_item(
    ref="6.5.2",
    marks=3,
    topic="Chemical Equilibrium - Temperature Dependence of Equilibrium Constant",
    passage="",
    question="Will the equilibrium constant, $K_c$, at $100\\,^\\circ\\text{C}$ be GREATER THAN, LESS THAN or EQUAL TO the $K_c$ at $150\\,^\\circ\\text{C}$? Explain the answer.",
    memo="- Less than $\\checkmark$\n- Explanation:\nAmount/concentration of products / $\\text{B}_2$ / $\\text{A}_2$ decreases. $\\checkmark\\checkmark$\nOR: Amount/concentration of reactants / $\\text{AB}$ increases.\nOR: The reverse reaction is favoured / Equilibrium (position) shifts to the left.",
    final_answer="Less than"
)

add_item(
    ref="6.6",
    marks=3,
    topic="Chemical Equilibrium - Effect of Catalyst on Equilibrium Rates",
    passage=q6_passage,
    question="The initial reaction now takes place in the presence of a catalyst at $150\\,^\\circ\\text{C}$. Describe the changes that will be observed on the graph between $t = 0\\text{ s}$ and $t = 60\\text{ s}$.",
    memo="Gradients (of all three curves) will be steeper $\\checkmark\\checkmark$ and reach the same equilibrium $\\checkmark$ values.\nOR: Gradients of curves become zero $\\checkmark$ at same equilibrium $\\checkmark$ values before $40\\text{ s} \\checkmark$.\nOR: The curves are horizontal at same equilibrium values before $40\\text{ s}$ / reaches same equilibrium sooner / less than $40\\text{ s}$.\n\nNote:\nIf curves are identified, all three must be named.",
    final_answer="Gradients of all curves will be steeper and equilibrium is reached sooner (before 40 s) at the same equilibrium values."
)

# ==============================================================================
# QUESTION 7 (4 items, 18 marks total)
# ==============================================================================

q7_passage = (
    "To identify metal M in an unknown metal carbonate, $\\text{MCO}_3$, the following procedure is carried out:\n\n"
    "Step 1: $0{,}198\\text{ g}$ of IMPURE $\\text{MCO}_3$ is reacted with $25\\text{ cm}^3$ of $0{,}4\\text{ mol}\\cdot\\text{dm}^{-3}$ nitric acid, $\\text{HNO}_3(aq)$.\n\n"
    "Step 2: The EXCESS $\\text{HNO}_3(aq)$ is then neutralised with $20\\text{ cm}^3$ of $0{,}15\\text{ mol}\\cdot\\text{dm}^{-3}$ barium hydroxide, $\\text{Ba(OH)}_2(aq)$.\n\n"
    "Assume that the volumes are additive.\n\n"
    "The following reactions take place:\n"
    "$$2\\text{HNO}_3(aq) + \\text{MCO}_3(s) \\rightarrow \\text{M(NO}_3)_2(aq) + \\text{CO}_2(g) + \\text{H}_2\\text{O}(l)$$\n"
    "$$2\\text{HNO}_3(aq) + \\text{Ba(OH)}_2(aq) \\rightarrow \\text{Ba(NO}_3)_2(aq) + 2\\text{H}_2\\text{O}(l)$$"
)

add_item(
    ref="7.1",
    marks=2,
    topic="Acids and Bases - Definition of Strong Base",
    passage=q7_passage,
    question="Define the term strong base.",
    memo="A strong base (ionises) dissociates completely $\\checkmark$ in water to form a high concentration of $\\text{OH}^-$ ions. $\\checkmark$\n(‘n Sterk basis ioniseer/dissosieer volledig in water om 'n hoë konsentrasie $\\text{OH}^-$-ione te vorm.)\n\nACCEPT:\nA strong base (ionises) dissociates completely $\\checkmark$ in water. $\\checkmark$",
    final_answer="A base that dissociates completely in water to form a high concentration of OH- ions."
)

add_item(
    ref="7.2.1",
    marks=3,
    topic="Acids and Bases - Stoichiometric Moles of Base in Titration",
    passage=q7_passage,
    question="Calculate the: Number of moles of $\\text{Ba(OH)}_2(aq)$ that reacted with the excess $\\text{HNO}_3(aq)$",
    memo="$$n(\\text{Ba(OH)}_2) = cV \\checkmark$$\n$$= (0{,}15)(0{,}02) \\checkmark$$\n$$= 0{,}003\\text{ mol} \\checkmark$$",
    final_answer="0.003"
)

add_item(
    ref="7.2.2",
    marks=5,
    topic="Acids and Bases - Calculation of pH of Unreacted Acid Solution",
    passage=q7_passage,
    question="Calculate the: pH of the solution after Step 1",
    memo="POSITIVE MARKING FROM QUESTION 7.2.1\n\nMarking criteria:\n(a) Use ratio: $n(\\text{HNO}_3) = 2 n(\\text{Ba(OH)}_2) \\checkmark$\n(b) Substitute $n(\\text{H}_3\\text{O}^+)$ or $n(\\text{HNO}_3)$ and $0{,}025\\text{ dm}^3$ in $c = \\frac{n}{V} \\checkmark$\n(c) Formula: $\\text{pH} = -\\log[\\text{H}_3\\text{O}^+] \\checkmark$\n(d) Substitute $[\\text{H}_3\\text{O}^+]$ in pH formula $\\checkmark$\n(e) Final correct answer: $0{,}62 \\checkmark$\n\nOPTION 1:\n$$n(\\text{HNO}_3)_{\\text{excess}} = 2 n(\\text{Ba(OH)}_2) = 2(0{,}003) = 0{,}006\\text{ mol} \\checkmark(a)$$\n$$n(\\text{H}_3\\text{O}^+) = n(\\text{HNO}_3) = 0{,}006\\text{ mol}$$\n$$[\\text{H}_3\\text{O}^+] = \\frac{n}{V} = \\frac{0{,}006}{0{,}025} \\checkmark(b) = 0{,}24\\text{ mol}\\cdot\\text{dm}^{-3}$$\n$$\\text{pH} = -\\log[\\text{H}_3\\text{O}^+] \\checkmark(c)$$\n$$\\text{pH} = -\\log(0{,}24) \\checkmark(d) = 0{,}62 \\checkmark(e)$$\n\nOPTION 2:\n$$[\\text{HNO}_3] = \\frac{n}{V} = \\frac{0{,}006}{0{,}025} = 0{,}24\\text{ mol}\\cdot\\text{dm}^{-3} \\checkmark(b)$$\n$$\\text{pH} = -\\log(0{,}24) = 0{,}62 \\checkmark(e)$$",
    final_answer="0.62"
)

add_item(
    ref="7.3",
    marks=8,
    topic="Acids and Bases - Sample Purity and Identification of Unknown Metal Carbonate",
    passage=q7_passage,
    question="The percentage purity of the $\\text{MCO}_3(s)$ in the sample is 85%. Identify metal M.",
    memo="POSITIVE MARKING FROM QUESTION 7.2.2\n\nMarking criteria:\n(a) Substitute $[\\text{HNO}_3] = 0{,}4\\text{ mol}\\cdot\\text{dm}^{-3}$ and $0{,}025\\text{ dm}^3 \\checkmark$\n(b) Subtract: $n(\\text{HNO}_3)_{\\text{ini}} - n(\\text{HNO}_3)_{\\text{excess}}$ OR $[\\text{HNO}_3]_{\\text{ini}} - [\\text{HNO}_3]_{\\text{excess}} \\checkmark\\checkmark$\n(c) Use of ratio: $n(\\text{MCO}_3) = \\frac{1}{2} n(\\text{HNO}_3) \\checkmark$\n(d) Calculate the pure mass $m(\\text{MCO}_3) \\checkmark$\n(e) Substitute $n(\\text{MCO}_3)$ and $m(\\text{MCO}_3)$ in $n = \\frac{m}{M} \\checkmark$\n(f) Subtraction of $60\\text{ g}\\cdot\\text{mol}^{-1}$ from molar mass $\\checkmark$\n(g) Correct answer: Mg $\\checkmark$\n\nOPTION 1:\n$$n(\\text{HNO}_3)_{\\text{ini}} = cV = (0{,}4)(0{,}025) \\checkmark(a) = 0{,}01\\text{ mol}$$\n$$n(\\text{HNO}_3)_{\\text{reacted}} = n(\\text{HNO}_3)_{\\text{ini}} - n(\\text{HNO}_3)_{\\text{excess}} = 0{,}01 - 0{,}006 \\checkmark\\checkmark(b) = 0{,}004\\text{ mol}$$\n$$n(\\text{MCO}_3) = \\frac{1}{2} n(\\text{HNO}_3) = \\frac{1}{2}(0{,}004) \\checkmark(c) = 0{,}002\\text{ mol}$$\n$$m(\\text{MCO}_3)_{\\text{pure}} = \\frac{85}{100} \\times 0{,}198 \\checkmark(d) = 0{,}1683\\text{ g}$$\n$$n(\\text{MCO}_3) = \\frac{m}{M} \\implies 0{,}002 = \\frac{0{,}1683}{M} \\checkmark(e) \\implies M(\\text{MCO}_3) = 84{,}15\\text{ g}\\cdot\\text{mol}^{-1}$$\n$$\\text{Molar mass of M} = 84{,}15 - 60 \\checkmark(f) = 24{,}15\\text{ g}\\cdot\\text{mol}^{-1}$$\n$$\\text{Therefore metal M is Magnesium (Mg)} \\checkmark(g)$$\n\nOPTION 2:\n$$[\\text{HNO}_3]_{\\text{reacted}} = 0{,}4 - 0{,}24 = 0{,}16\\text{ mol}\\cdot\\text{dm}^{-3} \\checkmark\\checkmark(b)$$\n$$n(\\text{HNO}_3)_{\\text{reacted}} = (0{,}16)(0{,}025) = 0{,}004\\text{ mol} \\checkmark(a)$$\n$$n(\\text{MCO}_3) = 0{,}002\\text{ mol} \\checkmark(c)$$\n$$m(\\text{pure}) = 0{,}1683\\text{ g} \\checkmark(d)$$\n$$M(\\text{MCO}_3) = 84{,}15\\text{ g}\\cdot\\text{mol}^{-1} \\checkmark(e)$$\n$$M = 84{,}15 - 60 = 24{,}15\\text{ g}\\cdot\\text{mol}^{-1} \\checkmark(f)$$\n$$\\text{Therefore, metal M is Mg} \\checkmark(g)$$",
    final_answer="Mg"
)

# ==============================================================================
# QUESTION 8 (7 items, 12 marks total)
# ==============================================================================

q8_passage_1 = (
    "A cleaned pure copper strip, $\\text{Cu}(s)$, is placed in a beaker containing a colourless "
    "silver nitrate solution, $\\text{AgNO}_3(aq)$, at $25\\,^\\circ\\text{C}$, as shown below.\n\n"
    "[DIAGRAM: Single cell / beaker experiment | A beaker containing colourless AgNO3(aq) at $25\,^\circ\text{C}$ with a pure copper strip (Cu(s)) placed inside it]\n\n"
    "[DIAGRAM: Single cell / beaker experiment | A beaker containing colourless AgNO3(aq) at $25\,^\circ\text{C}$ with a pure copper strip (Cu(s)) placed inside it]\n\n"
)

q8_passage_2 = (
    "A galvanic cell is now set up using Cu and Ag strips as electrodes. A simplified diagram of the cell is shown below.\n\n"
    "[DIAGRAM: Galvanic cell | Left half-cell contains an electrode immersed in electrolyte solution B, connected via an inverted U-tube salt bridge to the right half-cell. Right half-cell contains electrode A(s) immersed in Ag+(aq) solution. Both electrodes are connected externally through a voltmeter (V)]"
)

add_item(
    ref="8.1.1",
    marks=1,
    topic="Electrochemical Cells - Observable Change in Spontaneous Redox Reaction",
    passage=q8_passage_1,
    question="Write down: ONE other OBSERVABLE change, besides the solution turning blue",
    memo="Copper strip becomes thinner / corrodes / decreases in mass / solid / silver coloured particles in solution / the copper becomes plated with silver $\\checkmark$\n(Koper plaatjie word dunner / korrodeer / massa neem af / vaste stof / silwer-kleurige deeltjies in oplossing.)\n\nNote: If 'Rust': 0/1.",
    final_answer="Copper strip becomes thinner (or silver coating forms on the copper strip)"
)

add_item(
    ref="8.1.2",
    marks=1,
    topic="Electrochemical Cells - Identification of Oxidising Agent",
    passage=q8_passage_1,
    question="Write down: The NAME or FORMULA of the oxidising agent",
    memo="$\\text{Ag}^+$ (ion) / Silver ion / $\\text{AgNO}_3$ / silver nitrate $\\checkmark$\n(Silwernitraat / Silwer-ioon)",
    final_answer="Ag+"
)

add_item(
    ref="8.2",
    marks=3,
    topic="Electrochemical Cells - Explanation Using Standard Reduction Potentials",
    passage=q8_passage_1,
    question="Explain the answer to QUESTION 8.1.1 by referring to the relative strengths of the oxidising agents or reducing agents.",
    memo="$\\text{Ag}^+$ (ion) is a stronger oxidising agent $\\checkmark$ than $\\text{Cu}^{2+}$ ion $\\checkmark$ and will oxidise $\\text{Cu} \\checkmark$ to $\\text{Cu}^{2+}$ ion.\n\nOR:\n$\\text{Cu}^{2+}$ (ion) is a weaker oxidising agent $\\checkmark$ than $\\text{Ag}^+$ ion $\\checkmark$ and $\\text{Cu}$ will be oxidised $\\checkmark$ to $\\text{Cu}^{2+}$ ion.\n\nOR:\n$\\text{Cu}$ / Copper is a stronger reducing agent $\\checkmark$ than $\\text{Ag}$ / Silver $\\checkmark$ and will reduce silver ions $\\checkmark$ to silver.",
    final_answer="Ag+ is a stronger oxidising agent than Cu2+ and oxidises Cu to Cu2+."
)

add_item(
    ref="8.3.1",
    marks=1,
    topic="Galvanic Cells - Identification of Cathode Electrode",
    passage=q8_passage_2,
    question="Write down the: NAME or FORMULA of electrode A",
    memo="Silver / $\\text{Ag}$ / Silwer $\\checkmark$",
    final_answer="Ag"
)

add_item(
    ref="8.3.2",
    marks=1,
    topic="Galvanic Cells - Identification of Anode Electrolyte",
    passage=q8_passage_2,
    question="Write down the: NAME or FORMULA of solution B",
    memo="$\\text{CuSO}_4$ / $\\text{Cu}^{2+}$ / Copper (II) ions / copper(II) sulphate $\\checkmark$\n(Koper(II)-ione / koper(II)sulfaat)\n\nACCEPT:\nAny soluble copper(II) salt e.g. $\\text{Cu(NO}_3)_2$",
    final_answer="CuSO4"
)

add_item(
    ref="8.3.3",
    marks=3,
    topic="Galvanic Cells - Overall Balanced Net Cell Reaction",
    passage=q8_passage_2,
    question="Write down the: Overall (net) balanced equation for the cell reaction",
    memo="$$2\\text{Ag}^+(aq) + \\text{Cu}(s) \\checkmark \\rightarrow 2\\text{Ag}(s) + \\text{Cu}^{2+}(aq) \\checkmark \\quad \\text{Bal } \\checkmark$$\n\nMarking criteria:\n- Reactants $\\checkmark$\n- Products $\\checkmark$\n- Balancing $\\checkmark$\n\nNotes:\n- Ignore double arrows.\n- Ignore phases.",
    final_answer="2Ag+(aq) + Cu(s) -> 2Ag(s) + Cu2+(aq)"
)

add_item(
    ref="8.4",
    marks=2,
    topic="Galvanic Cells - Function of Salt Bridge and Direction of Ion Migration",
    passage=q8_passage_2,
    question="The salt bridge contains potassium nitrate, $\\text{KNO}_3(aq)$.\n\nWrite down the FORMULA of the ion in the salt bridge that will move into the silver ion solution. Choose from $\\text{K}^+(aq)$ or $\\text{NO}_3^-(aq)$.\n\nGive a reason for the answer.",
    memo="$\\text{K}^+ \\checkmark$\n\nReason:\n$[\\text{Ag}^+]$ decreases $\\checkmark$\nOR: In silver half-cell concentration of positive ions decreases.\nOR: The silver half-cell becomes negative.\nACCEPT: Maintain the ion balance / electrical neutrality.",
    final_answer="K+"
)

# ==============================================================================
# QUESTION 9 (5 items, 12 marks total)
# ==============================================================================

q9_passage = (
    "An electrolytic cell is set up to purify a piece of copper that contains silver and zinc as impurities. "
    "A simplified diagram of the cell is shown below. Electrode R is impure copper.\n\n"
    "[DIAGRAM: Electrolytic cell for copper purification | A container holding an electrolyte solution with two electrodes connected to an external DC power source. "
    "Electrode Q (left) is a regular rectangular block (pure copper cathode). "
    "Electrode R (right) is an irregularly shaped block labeled 'impure copper' (anode). "
    "At the bottom of the container below electrode R is an anode sludge/deposit labeled 'Silver'.]"
)

add_item(
    ref="9.1",
    marks=2,
    topic="Electrolytic Cells - Definition of Electrolysis",
    passage=q9_passage,
    question="Define the term electrolysis.",
    memo="ANY ONE:\n- The chemical process in which electrical energy is converted to chemical energy. $\\checkmark\\checkmark$ (2 or 0)\n- The use of electrical energy to produce a chemical change. $\\checkmark\\checkmark$\n- Decomposition of an ionic compound by means of electrical energy. $\\checkmark\\checkmark$\n- The process during which an electric current passes through a solution / ionic liquid / molten ionic compound. $\\checkmark\\checkmark$\n\n(Die chemiese proses waarin elektriese energie omgeskakel word na chemiese energie.)",
    final_answer="The chemical process in which electrical energy is converted to chemical energy."
)

add_item(
    ref="9.2",
    marks=2,
    topic="Electrolytic Cells - Reduction Half-reaction at Cathode",
    passage=q9_passage,
    question="Write down the reaction taking place at electrode Q.",
    memo="$$\\text{Cu}^{2+}(aq) + 2e^- \\rightarrow \\text{Cu}(s) \\checkmark\\checkmark$$\n\nACCEPT:\nReduction (reaction): 1/2.\n\nMarking criteria:\n- $\\text{Cu}(s) \\leftarrow \\text{Cu}^{2+}(aq) + 2e^-$: 2/2\n- $\\text{Cu}^{2+}(aq) + 2e^- \\rightleftharpoons \\text{Cu}(s)$: 1/2\n- $\\text{Cu}(s) \\rightleftharpoons \\text{Cu}^{2+}(aq) + 2e^-$: 0/2\n- $\\text{Cu}^{2+}(aq) + 2e^- \\leftarrow \\text{Cu}(s)$: 0/2\n- Ignore if charge omitted on electron.\n- If charge (+) omitted on $\\text{Cu}^{2+}$: Max 1/2.\n- Ignore phases.",
    final_answer="Cu2+(aq) + 2e- -> Cu(s)"
)

add_item(
    ref="9.3",
    marks=1,
    topic="Electrolytic Cells - Direction of Electron Flow in External Circuit",
    passage=q9_passage,
    question="In which direction do the electrons flow in the external circuit? Choose from Q to R or R to Q.",
    memo="R to/na Q $\\checkmark$",
    final_answer="R to Q"
)

add_item(
    ref="9.4",
    marks=5,
    topic="Electrolytic Cells - Quantitative Calculation of Current (Faraday and Charge)",
    passage=q9_passage,
    question="Calculate the current needed to form $16\\text{ g}$ of copper when the cell operates for five hours.",
    memo="Marking criteria:\n(a) Substitution of 63,5 into $n = \\frac{m}{M} \\checkmark$\n(b) Substitute $6{,}02 \\times 10^{23}\\text{ mol}^{-1} \\checkmark$\n(c) $n(\\text{electrons}) = N(\\text{Cu atoms}) \\times 2$ OR $n(\\text{electrons}) = N(\\text{Cu atoms}) \\times 1 \\checkmark$\n(d) Calculate $t = (5)(60)(60) = 18\\,000\\text{ s} \\checkmark$\n(e) Final correct answer: $2{,}68\\text{ A} \\checkmark$ (Range: 1,34 to 2,70 A)\n\nUSING $\\text{Cu}^{2+}$:\n$$n(\\text{Cu}) = \\frac{m}{M} = \\frac{16}{63{,}5} \\checkmark(a) = 0{,}25197\\text{ mol}$$\n$$N(\\text{Cu atoms}) = n \\times N_A = (0{,}25197)(6{,}02 \\times 10^{23}) \\checkmark(b) = 1{,}517 \\times 10^{23}\\text{ atoms}$$\n$$N(\\text{electrons}) = (1{,}517 \\times 10^{23})(2) \\checkmark(c) = 3{,}034 \\times 10^{23}\\text{ electrons}$$\n$$Q = N(\\text{electrons}) \\times q_e = (3{,}034 \\times 10^{23})(1{,}6 \\times 10^{-19}) = 48\\,160\\text{ C} \\quad (\\text{or } 48\\,544\\text{ C})$$\n$$t = (5)(60)(60) = 18\\,000\\text{ s} \\checkmark(d)$$\n$$I = \\frac{Q}{\\Delta t} = \\frac{48\\,160}{18\\,000} = 2{,}68\\text{ A} \\checkmark(e)$$\n\nUSING $\\text{Cu}^+$:\n$$N(\\text{electrons}) = (1{,}517 \\times 10^{23})(1) \\implies Q = 24\\,080\\text{ C}$$\n$$I = \\frac{24\\,080}{18\\,000} = 1{,}34\\text{ A}$$",
    final_answer="2.68 A"
)

add_item(
    ref="9.5",
    marks=2,
    topic="Electrolytic Cells - Relative Reducing Strengths and Anode Sludge Formation",
    passage=q9_passage,
    question="During this electrolysis, only copper and zinc are oxidised. Give a reason why the silver is not oxidised.",
    memo="Ag/silver is a weaker reducing agent $\\checkmark$ than Cu/copper or Zn/zinc $\\checkmark$ and will not be oxidised.\n\nOR:\nCu/copper or Zn/zinc is a stronger reducing agent $\\checkmark$ than Ag/silver $\\checkmark$ and Ag will not be oxidised.\n\nOR:\nVoltage of power source is not effective enough (to oxidise Ag/silver). $\\checkmark\\checkmark$",
    final_answer="Silver is a weaker reducing agent than copper and zinc and will not be oxidised."
)

# ==============================================================================
# VALIDATION AND WRITING
# ==============================================================================

total_marks = sum(item["marks"] for item in items)
print(f"Total items extracted: {len(items)}")
print(f"Total marks: {total_marks} / 150")

assert len(items) == 68, f"Expected 68 items, got {len(items)}"
assert total_marks == 150, f"Expected 150 marks, got {total_marks}"

# Validate schema keys
REQUIRED_KEYS = [
    "item_id", "source_id", "pair_source_id", "subject", "grade",
    "language", "track", "kind", "question_ref", "marks", "topic",
    "passage", "question", "memo", "final_answer", "needs_review",
    "licence", "attribution"
]

for idx, it in enumerate(items):
    for key in REQUIRED_KEYS:
        assert key in it, f"Item {idx} ({it['item_id']}) missing key {key}"
    assert it["marks"] > 0, f"Item {idx} has invalid marks {it['marks']}"
    assert it["track"] == TRACK
    assert it["subject"] == SUBJECT
    assert it["grade"] == 12
    assert it["language"] == "en"

# Validate KaTeX dollars
for idx, it in enumerate(items):
    for field in ["question", "memo", "passage"]:
        content = it[field]
        # Count non-escaped single and double dollars
        # Replace display math $$ first
        without_display = re.sub(r'\$\$.*?\$\$', '', content, flags=re.DOTALL)
        single_dollars = len(re.findall(r'(?<!\\)\$', without_display))
        if single_dollars % 2 != 0:
            print(f"WARNING: Unbalanced single dollar in {it['item_id']} field {field}")
            print(content)
            sys.exit(1)

# Check for banned patterns
for idx, it in enumerate(items):
    for field in ["question", "memo", "passage"]:
        content = it[field]
        if "\\text{^\\circ C}" in content:
            print(f"ERROR: Invalid degree Celsius in {it['item_id']} field {field}")
            sys.exit(1)

print("All KaTeX and schema validations passed successfully!")

# Write dual output files
path1 = "sa-tutor-kit/sa-tutor-kit/workspace/items/physical_sciences/dbe-physical_sciences-g12-p2-2023-nov.jsonl"
path2 = "sa-tutor-kit/sa-tutor-kit/workspace/items/dbe-physical_sciences-g12-p2-2023-nov.jsonl"

for path in [path1, path2]:
    with open(path, "w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")
    print(f"Successfully wrote {len(items)} items to {path}")
