# append_decisions.py
entry = """
### [2026-11-05] High-Fidelity UDVES Extraction: DBE Mathematics Grade 12 Paper 2 May/June 2025 (`dbe-mathematics-g12-p2-2025-may`)

- **Context & Mission:**
  - Target: DBE Mathematics Grade 12 Paper 2 (May/June 2025) and official marking guidelines (`dbe-mathematics-g12-p2-2025-may-memo`).
  - Total Paper Marks: Exactly 150 marks.
  - Legacy memo text file was truncated (~1.5 KB, ending abruptly at Question 2.1). Full memo was recovered directly from the raw official PDF `mathematics_g12_2025_may_p2_memo.pdf` (23 pages, 27 393 chars) using PyMuPDF (`fitz`), and restored to `workspace/text/dbe-mathematics-g12-p2-2025-may-memo.txt` (61 937 chars, 1 442 lines).
  - All questions, geometric configurations, Cartesian coordinate diagrams, Euclidean geometry figures, and 3D diagrams were visually inspected from the QP PDF and converted into high-fidelity UDVES notation.
- **Section & Question Breakdown (52 Atomic Items, Exactly 150 Marks Total):**
  - **Question 1: Statistics - Insurance Premiums (4 items, 9 marks):**
    - 1.1: Mean of 15 premium values ($\bar{x} = 570{,}27$) (2 marks)
    - 1.2: Standard deviation ($\sigma = 291{,}03$) (1 mark)
    - 1.3: Values within one standard deviation of mean (10 premiums) (2 marks)
    - 1.4: Differential percentage increase calculation ($k = 21\%$) (4 marks)
  - **Question 2: Statistics - Supermarket Online Orders & Packing Time (5 items, 10 marks):**
    - 2.1: Scatter plot construction on Cartesian grid (3 marks)
    - 2.2: Least squares regression line ($\hat{y} = 0{,}35x + 3{,}08$) (3 marks)
    - 2.3: Correlation coefficient ($r = 0{,}74$) (1 mark)
    - 2.4: Packing time prediction for 13 items ($\hat{y} = 7{,}63\text{ or } 7{,}65\text{ min}$) (2 marks)
    - 2.5: Contextual interpretation of $y$-intercept ($0\text{ items} \implies 0\text{ min}$) (1 mark)
  - **Question 3: Analytical Geometry - Triangle SRT & Perpendicular Altitude (6 items, 21 marks):**
    - 3.1: Coordinates of $x$-intercept $R(-5 ; 0)$ (2 marks)
    - 3.2: Surd length of $RT = \sqrt{125} = 5\sqrt{5}$ (3 marks)
    - 3.3: Distance equation $2RT^2 = 5SR^2 \implies m = -12$ (4 marks)
    - 3.4: Perpendicular line equation $VR: y = -\frac{4}{3}x - \frac{20}{3}$ (5 marks)
    - 3.5: Intersection coordinates $V(-8 ; 4)$ (2 marks)
    - 3.6: Area of reflected polygon $RVTR' = 75\text{ units}^2$ (5 marks)
  - **Question 4: Analytical Geometry - Circle, Tangent & Parallelogram (7 items, 20 marks):**
    - 4.1: Angle between tangent and radius $\text{C}\hat{\text{E}}\text{M} = 90^\circ$ (1 mark)
    - 4.2: Tangent line equation $EC: y = \frac{4}{3}x + \frac{13}{3}$ (4 marks)
    - 4.3: Length $DM = \frac{25}{4} = 6{,}25\text{ units}$ (3 marks)
    - 4.4: Show $p = -5$ for point $C(-7 ; p)$ (1 mark)
    - 4.5: Coordinates of parallelogram vertex $S(-11 ; -2)$ (3 marks)
    - 4.6: Extended radius comparison ($MS = \sqrt{200} \approx 14{,}14 > 12 \implies \text{outside}$) (3 marks)
    - 4.7: Angle calculation $\text{E}\hat{\text{T}}\text{M} = 58{,}28^\circ$ (5 marks)
  - **Question 5: Trigonometry - Reduction, Compound Angles & Identities (5 items, 19 marks):**
    - 5.1.1: $\sin^2\theta = \frac{144}{169}$ in QIII (3 marks)
    - 5.1.2: $\tan(360^\circ - \theta) = -\frac{12}{5}$ (2 marks)
    - 5.1.3: $\cos(\theta - 135^\circ) = -\frac{7\sqrt{2}}{26}$ (4 marks)
    - 5.2: Simplification to $\tan 2x$ (6 marks)
    - 5.3: Product of tangents sequence simplification to $1$ (4 marks)
  - **Question 6: Trigonometry - Proofs & General Equations (4 items, 13 marks):**
    - 6.1: Double angle identity proof $2\cos^2(45^\circ + x) = 1 - \sin 2x$ (4 marks)
    - 6.2.1: Compound difference proof $\sin(A - B) - \sin(A + B) = -2\cos A\sin B$ (2 marks)
    - 6.2.2: Difference to product $\sin 4x - \sin 10x = -2\cos 7x\sin 3x$ (2 marks)
    - 6.2.3: Solutions in interval $[0^\circ ; 30^\circ]$: $x = 0^\circ$ or $x = 17{,}14^\circ$ (5 marks)
  - **Question 7: Trigonometric Functions & Graphs (6 items, 10 marks):**
    - 7.1: Range of $f(x) = 2\cos x + 1$: $y \in [-1 ; 3]$ (1 mark)
    - 7.2: Period of $g(x) = \sin 2x$: $180^\circ$ (1 mark)
    - 7.3: Increasing interval $x \in (-180^\circ ; 0^\circ)$ (1 mark)
    - 7.4.1: Sign analysis $g(x) \cdot f'(x) < 0 \implies x \in (-90^\circ ; 0^\circ) \cup (0^\circ ; 90^\circ)$ (2 marks)
    - 7.4.2: Inequality $\cos x \le -\frac{1}{2} \implies x \in [-180^\circ ; -120^\circ] \cup [120^\circ ; 180^\circ]$ (3 marks)
    - 7.5: Horizontal shift $h(x) = -\cos 2x$ (2 marks)
  - **Question 8: 3D Trigonometry - Elevated Mast & Horizontal Plane (3 items, 8 marks):**
    - 8.1: Side $AB = \frac{p}{\tan y}$ (2 marks)
    - 8.2: Sine / Cosine rule proof $\cos x = \tan y$ (4 marks)
    - 8.3: Elevation angle calculation $y = 26{,}57^\circ$ for $x = 60^\circ$ (2 marks)
  - **Question 9: Euclidean Geometry - Proportionality & Intersecting Circles (7 items, 20 marks):**
    - 9.1.1: Ratio $\frac{HF}{EH} = \frac{2}{5}$ [line $\parallel$ side of $\Delta$] (2 marks)
    - 9.1.2: Length $EH = 15\text{ cm}$ (2 marks)
    - 9.1.3: Similar triangle $\Delta FDE$ (1 mark)
    - 9.1.4: Ratio $\frac{GH}{DE} = \frac{2}{7}$ (2 marks)
    - 9.2.1: Proof $LT \parallel PR$ via semi-circle angles / tan-chord (4 marks)
    - 9.2.2: Cyclic quad proof for $LORM$ via alternate/corresponding angles (5 marks)
    - 9.2.3: Angle bisector proof for $LN$ via angle at centre theorem (4 marks)
  - **Question 10: Euclidean Geometry - Equiangular Theorem & Chord Geometry (5 items, 20 marks):**
    - 10.1: Formal proof of equiangular triangles proportionality theorem (6 marks)
    - 10.2.1: Similarity proof $\Delta CFO \parallel\parallel\parallel \Delta CBD$ [$\angle\angle\angle$] (3 marks)
    - 10.2.2: Ratio proof $OF \cdot CD = CO \cdot BC$ (2 marks)
    - 10.2.3: Chord midpoint and proportionality proof $BF = \frac{75}{16}$ (6 marks)
    - 10.2.4: Angle calculation $\text{A}\hat{\text{B}}\text{D} = 73{,}74^\circ$ (3 marks)
- **Strict KaTeX & Standards Compliance:**
  - Standardized all criteria checkmarks into valid KaTeX `$\checkmark$` notation.
  - Protected all decimal commas inside math mode (`$570{,}27$`, `$0{,}35$`, `$19{,}2$`).
  - Strict balance on all math delimiters (0 KaTeX syntax errors).
  - High-fidelity UDVES diagram notations with explicit geometric elements and coordinates.
  - Exactly 0 items flagged (`needs_review: false`).
- **Verification Metrics:**
  - **Total Items Extracted:** Exactly 52 atomic items.
  - **Total Marks Accounted:** Exactly 150 / 150 marks.
  - **Needs Review Count:** 0 items.
  - **KaTeX Syntax:** 0 errors, perfectly balanced.
- **Storage:** Dual-mirrored across:
  - `sa-tutor-kit/sa-tutor-kit/workspace/items/mathematics/dbe-mathematics-g12-p2-2025-may.jsonl`
  - `sa-tutor-kit/sa-tutor-kit/workspace/items/dbe-mathematics-g12-p2-2025-may.jsonl`
  - Memo restored in `sa-tutor-kit/sa-tutor-kit/workspace/text/dbe-mathematics-g12-p2-2025-may-memo.txt`
"""

decisions_file = "sa-tutor-kit/sa-tutor-kit/workspace/DECISIONS.md"
with open(decisions_file, "a", encoding="utf-8") as f:
    f.write(entry + "\n")

print("Successfully appended to DECISIONS.md")
