# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Update EXTRACTION_TRACKER.md
tracker_path = "workspace/EXTRACTION_TRACKER.md"
with open(tracker_path, "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace(
    "| **Wave 5 (Page 5)** | **IN FLIGHT (3/4 Done)** | Maths P1, Physics P1, English HL P1, Afrikaans HL P1 (2021) |",
    "| **Wave 5 (Page 5)** | **100% COMPLETE** | Maths P1, Physics P1, English HL P1, Afrikaans HL P1 (2021) |"
)
text = text.replace(
    "| **Total Extracted Items** | **1032 Items** | KaTeX formatted, UDVES standardized, atomic multiple choice |",
    "| **Total Extracted Items** | **1088 Items** | KaTeX formatted, UDVES standardized, atomic multiple choice |"
)
text = text.replace(
    "| **Total Marks Accounted** | **2211 Marks** | 100% agreement with DBE official memorandums |",
    "| **Total Marks Accounted** | **2361 Marks** | 100% agreement with DBE official memorandums |"
)
text = text.replace(
    "| [ ] | `dbe-physical_sciences-g12-p1-2021-nov` | physical | Gr 12 | 2021 Nov | - | -/150 | - | - | - |",
    "| [x] | `dbe-physical_sciences-g12-p1-2021-nov` | physical | Gr 12 | 2021 Nov | **56** | **150/150** | 0 | 0 | Yes |"
)

with open(tracker_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated EXTRACTION_TRACKER.md successfully")

# Append to DECISIONS.md
decisions_path = "workspace/DECISIONS.md"
decision_entry = """
### Phase 2 Wave 5 Extraction: `dbe-physical_sciences-g12-p1-2021-nov` (November 2021 Physical Sciences P1)
- **Status:** COMPLETED & VERIFIED
- **Source ID:** `dbe-physical_sciences-g12-p1-2021-nov`
- **Paired Memo ID:** `dbe-physical_sciences-g12-p1-2021-nov-memo`
- **Subject:** `physical_sciences` | **Grade:** 12 | **Language:** en | **Track:** `physical_sciences`
- **Output Files:**
  - `workspace/items/physical_sciences/dbe-physical_sciences-g12-p1-2021-nov.jsonl`
  - `workspace/items/dbe-physical_sciences-g12-p1-2021-nov.jsonl`
- **Reconciliation & Visual Context Recovery:**
  - **Question 1 (Multiple Choice - 20 marks):**
    - Extracted 10 atomic items (1.1 to 1.10) at 2 marks each.
    - Encoded complete physical descriptions and LaTeX formatting for:
      - 1.3: Momentum-time graph piecewise linear intervals ($0-1\\text{ s}, 1-2\\text{ s}, 2-3\\text{ s}, 3-4\\text{ s}$), verifying slope $F_{\\text{net}} = \\frac{\\Delta p}{\\Delta t}$ reaches maximum magnitude $30\\text{ N}$ in $3-4\\text{ s}$.
      - 1.4: Mechanical energy vs time graphs for elastic bouncing ball.
      - 1.5: Atomic emission/absorption line spectra demonstrating red shift.
      - 1.6: Combined electric field lines between spheres P (positive) and Q (negative).
      - 1.7: Electrostatic interaction forces ($F$) obeying Newton's Third Law.
      - 1.8: Resistor network potential distribution ($V_1 = \\frac{2}{3}\\varepsilon$ vs $V_2 = V_3 = V_4 = \\frac{1}{3}\\varepsilon$).
  - **Question 2 (Newton's Laws & Friction - 16 marks):**
    - Extracted 5 atomic subquestions (2.1 to 2.5).
    - Encoded $20\\text{ kg}$ block moving at constant velocity $2\\text{ m}\\cdot\\text{s}^{-1}$ up a $30^\\circ$ incline with $18\\text{ N}$ friction; full free-body diagram criteria (4 forces); applied force $F = 116\\text{ N}$; net force $116\\text{ N}$ down incline after removal of $F$; stopping distance $\\Delta x = 0{,}34\\text{ m}$.
  - **Question 3 (Vertical Projectile Motion - 18 marks):**
    - Extracted 5 atomic subquestions (3.1, 3.2.1, 3.2.2, 3.2.3, 3.3).
    - Encoded hot-air balloon moving upwards at constant speed; stone A dropped at $200\\text{ m}$ height striking ground at $62{,}68\\text{ m}\\cdot\\text{s}^{-1}$; stone B dropped $5\\text{ s}$ later.
    - Speed of balloon $2{,}96\\text{ m}\\cdot\\text{s}^{-1}$; time for stone A to strike ground $6{,}70\\text{ s}$; distance between balloon and stone B at $t = 6{,}70\\text{ s}$ is $14{,}16\\text{ m}$; dual position-time graph specs (straight line for balloon, parabola for stone A).
  - **Question 4 (Momentum & Impulse - 10 marks):**
    - Extracted 3 atomic subquestions (4.1 to 4.3).
    - Encoded elastic collision between ball X ($10\\text{ kg}$, $2\\text{ m}\\cdot\\text{s}^{-1}$ east) and ball Y ($2\\text{ kg}$, $v_Y$); ball X comes to rest, ball Y moves east with $36\\text{ J}$; $v_Y = 4\\text{ m}\\cdot\\text{s}^{-1}$ west; contact time $0{,}1\\text{ s}$ yielding average contact force $200\\text{ N}$.
  - **Question 5 (Work, Energy and Power - 14 marks):**
    - Extracted 4 atomic subquestions (5.1 to 5.4).
    - Encoded $2\\text{ kg}$ box released from rest at $5\\text{ m}$ height on curved track PQ; speed at Q is $9{,}90\\text{ m}\\cdot\\text{s}^{-1}$; $10\\text{ m}$ rough surface to barrier at R at $4\\text{ m}\\cdot\\text{s}^{-1}$; average friction $8{,}20\\text{ N}$; barrier impulse $14\\text{ N}\\cdot\\text{s}$ to the left yielding rebound velocity $-3\\text{ m}\\cdot\\text{s}^{-1}$ and $\\Delta E_k = -7\\text{ J}$.
  - **Question 6 (Doppler Effect - 12 marks):**
    - Extracted 5 atomic subquestions (6.1 to 6.4).
    - Encoded stationary ambulance siren ($680\\text{ Hz}$, $v = 340\\text{ m}\\cdot\\text{s}^{-1}$, wavelength $\\lambda = 0{,}5\\text{ m}$); wavelength shift $\\Delta\\lambda = 0{,}05\\text{ m}$ towards observer; ambulance speed $v_s = 34\\text{ m}\\cdot\\text{s}^{-1}$.
  - **Question 7 (Electrostatics - 14 marks):**
    - Extracted 5 atomic subquestions (7.1.1 to 7.2).
    - Encoded sphere gaining charge $-1{,}95 \\times 10^{-6}\\text{ C}$ ($1{,}22 \\times 10^{13}$ electrons added); electric field at $0{,}5\\text{ m}$ ($7{,}02 \\times 10^4\\text{ N}\\cdot\\text{C}^{-1}$); two charges $q_1 < 0$ and $q_2$ separated by $0{,}02\\text{ m}$ with net force $1{,}38\\text{ N}$ west on point P ($0{,}03\\text{ m}$ east of $q_2$), yielding $q_2 = 1{,}11 \\times 10^{-7}\\text{ C}$.
  - **Question 8 (Electric Circuits - 19 marks):**
    - Extracted 7 atomic subquestions (8.1.1 to 8.6).
    - Encoded battery emf $12\\text{ V}$, internal resistance $r$; open circuit voltages ($V_1 = 12\\text{ V}, V_2 = 0\\text{ V}$); closed circuit current $1{,}2\\text{ A}$, resistor X power $5{,}76\\text{ W} \\implies R_X = 4\\ \\Omega$; parallel combination of $6\\ \\Omega$ and $(2{,}4 + 6 = 8{,}4\\ \\Omega) \\implies R_{\\text{ext}} = 7{,}5\\ \\Omega$; voltmeter reading $V_2 = 3\\text{ V}$; short circuiting P to Q causes total resistance decrease, current increase, internal voltage drop increase, and terminal voltage ($V_1$) decrease.
  - **Question 9 (Electrodynamics / AC Generator - 15 marks):**
    - Extracted 6 atomic subquestions (9.1 to 9.6).
    - Encoded AC generator with slip rings, rotating anticlockwise; induced current in section XY from Y to X via Fleming's Right-Hand Rule; $V_{\\text{rms}} = 70{,}71\\text{ V}, I_{\\text{rms}} = 2{,}83\\text{ A}, P_{\\text{ave}} = 200\\text{ W}$; doubled rotational speed doubles peak voltage to $200\\text{ V}$ and halves period to $0{,}05\\text{ s}$ (2 cycles in $0{,}1\\text{ s}$).
  - **Question 10 (Photoelectric Effect - 12 marks):**
    - Extracted 6 atomic subquestions (10.1 to 10.4.3).
    - Encoded frequency vs $E_{k(\\text{max})}$ graphs for cathodes M ($f_0 = 10{,}40 \\times 10^{14}\\text{ Hz}$) and N ($f_0 = 5{,}16 \\times 10^{14}\\text{ Hz}$); $E_{k(\\text{max})}$ for N is greater than M; calculation of $f_x = 4{,}51 \\times 10^{15}\\text{ Hz}$; higher light intensity effects: y-intercept unchanged (no effect), rate of emission increases, maximum kinetic energy unchanged (no effect).
- **Verification Metrics:**
  - **Total Items Extracted:** 56 atomic items (Q1: 10, Q2: 5, Q3: 5, Q4: 3, Q5: 4, Q6: 5, Q7: 5, Q8: 7, Q9: 6, Q10: 6).
  - **Total Marks Verified:** Exactly 150 / 150 marks ($20 + 16 + 18 + 10 + 14 + 12 + 14 + 19 + 15 + 12 = 150$).
  - **KaTeX Delimiters:** 0 unclosed dollar signs across all fields. Balanced `$..$` and `$$..$$`.
  - **Needs Review:** 0 items flagged `needs_review: true`.
  - **Corpus Milestone:** Cumulative verified items increased to **1,088 items** across **22 papers** (**2,361 total marks verified**).
"""

with open(decisions_path, "a", encoding="utf-8") as f:
    f.write(decision_entry)

print("Appended to DECISIONS.md successfully")
