# Universal Document & Visual Extraction Standard (UDVES)
## South African Curriculum (CAPS Grades 7–12 & TVET Colleges)

> **Document Status:** Active Standard (Stage 1 & Future Expansion)  
> **Target Models:** Multimodal Vision Ingestors (`Gemini Vision`, `LiquidAI LFM3-VL`, `Gemma Vision`) & Reasoning Engines  
> **Scope:** All South African Subjects, Languages, Exam Papers, Marking Memorandums, Technical Blueprints, and Textbooks.

---

## 1. Executive Mandate & Purpose

When extracting learning documents (past exam papers, marking guidelines, textbooks, workbooks), multimodal vision models must transcribe **100% of text verbatim** and convert all visual, diagrammatic, and graphical information into structured, unambiguous, quantitative representations.

A tutor model cannot explain a question if the visual elements are reduced to a vague summary. The transcription must be granular enough that a text-only language model can reconstruct the exact problem, perform the required calculations, and teach the student step-by-step.

---

## 2. Subject-by-Subject Visual & Technical Standards

### A. Engineering Graphics & Design (EGD) & Technical Technologies

Engineering drawings contain dense spatial and geometric data. Vision extractors must transcribe all views, dimensions, scales, projections, and annotations:

1. **Orthographic Projections (1st Angle & 3rd Angle):**
   - Identify projection system: First Angle ($X$-symbol / left-to-right) or Third Angle ($Y$-symbol / right-to-left).
   - Label views explicitly: Front View (FV), Top View / Plan (TV), Left/Right Elevation / Side View (LSV/RSV).
   - Identify cutting planes: Cutting Plane $A-A$, direction of sight arrows, sectioned hatching (e.g. $45^\circ$ cast iron hatching).
   - Hidden detail: Transcribe dashed lines indicating internal cavities, bores, or counterbores.
2. **Mechanical Drawings & Assemblies:**
   - Transcribe Title Block / Nameplate: Title, Drawing Number, Scale (e.g. $1:1$, $1:2$, $2:1$), Projection Symbol, Tolerances ($\pm 0,05\text{ mm}$).
   - Bill of Materials / Parts List: Table containing Item No., Part Name, Quantity, Material (e.g. Mild Steel, Brass, Cast Iron).
   - Dimensions & Features: Pitch Circle Diameter (PCD), metric thread callouts (e.g. $\text{M}16 \times 2$), chamfers ($2 \times 45^\circ$), radii ($R25$), diameters ($\varnothing 50$), keyways, fillets.
3. **Civil Technology & Architectural Drawings:**
   - Floor Plans & Site Plans: Room labels, dimensions (room widths, wall thicknesses e.g. $220\text{ mm}$ exterior, $110\text{ mm}$ interior).
   - Architectural Symbols: Doors (swing direction, single/double), windows (sill heights, sash types), sanitary fittings (WC, WHB, shower, bath, gully).
   - Electrical & Plumbing Layout: Lighting points, two-way switches, wall sockets, distribution board (DB), sewer lines, inspection eyes (IE), invert levels.
   - Elevation & Roof Trusses: North/South/East/West elevations, pitch angles (e.g. $25^\circ$), roof covering type (IBR, corrugated iron, concrete tiles), floor-to-ceiling heights.
4. **Electrical Technology (Electronics, Digital & Power Systems):**
   - Circuit Schematics: Component types and values (resistors in $\Omega/\text{k}\Omega/\text{M}\Omega$, capacitors in $\mu\text{F}/\text{nF}/\text{pF}$, inductors in $\text{mH}/\text{H}$).
   - Active Components: Transistors (BJT: NPN/PNP; FET: N-channel/P-channel, JFET/MOSFET), operational amplifiers (741 pinouts, inverting/non-inverting inputs, feedback loops).
   - Logic Gates & Truth Tables: Logic gates (AND, OR, NOT, NAND, NOR, XOR, XNOR), logic states ($0/1$), boolean expressions.
   - Waveforms & Oscilloscope Displays: Peak voltage ($V_p$), peak-to-peak ($V_{p-p}$), RMS voltage ($V_{\text{rms}}$), time base / period ($T$), frequency ($f$), duty cycle (%).
   - Transformers & Motors: Primary/secondary turns ($N_p, N_s$), voltages ($V_p, V_s$), star/delta wiring diagrams.
5. **Mechanical Technology (Automotive & Manufacturing):**
   - Gears & Pulleys: Number of teeth ($T_A, T_B$), gear pitch diameters, gear ratios, compound gear trains.
   - Cams & Followers: Cam profile displacement diagrams, follower types (knife-edge, roller, flat), lift/stroke ($\text{mm}$), dwell angles, rise/fall angles.
   - Hydraulic & Pneumatic Systems: Cylinder bore sizes, stroke lengths, piston areas ($A_1, A_2$), pressures ($P = F/A$), valve symbols (3/2-way, 4/3-way directional valves).

---

### B. Mathematics, Technical Mathematics & Mathematical Literacy

1. **Euclidean Geometry:**
   - List every lettered vertex and point in the figure.
   - Circle features: Center point ($O$), radii ($OA = OB$), diameter, chord, tangent line and exact point of contact, secant.
   - Geometric markings: Arrows denoting parallel lines ($AB \parallel CD$), single/double tick marks denoting equal lengths ($AB = BC$), right-angle squares ($90^\circ$).
   - Explicit angles: Transcribe all marked angle variables (e.g. $\hat{A}_1 = x$, $\hat{B}_2 = 35^\circ$).
   - Theorems marked: Cyclic quadrilaterals, alternate angles, corresponding angles, co-interior angles, tangents from common point.
2. **Analytical (Coordinate) Geometry:**
   - Cartesian axes with origin $(0, 0)$.
   - Every labeled point with coordinates: $A(x_1, y_1)$, $B(-2, 5)$, $C(k, 3)$.
   - Line segments: Inclination angle ($\theta$), midpoint ($M$), gradient ($m$), $y$-intercept ($c$).
   - Circles: Center $(a, b)$, radius ($r$), equation $(x-a)^2 + (y-b)^2 = r^2$, tangent equations.
3. **Functions & Differential Calculus:**
   - Function names and labels: $f(x) = ax^2 + bx + c$, $g(x) = \frac{a}{x-p} + q$, $h(x) = a \cdot b^{x-p} + q$.
   - Intercepts: All $x$-intercepts (roots) and $y$-intercepts.
   - Asymptotes: Vertical asymptote equation ($x = p$), horizontal asymptote equation ($y = q$).
   - Stationary / Turning Points: Local maximum/minimum $(x, y)$, point of inflection.
   - Domains and ranges; shaded areas between intersecting curves.
4. **Trigonometry:**
   - Cartesian planes with terminal arms in quadrants (CAST diagram).
   - Right-angled triangles with labeled opposite, adjacent, hypotenuse, and reference angle ($\theta$ or $\alpha$).
   - 3D Trigonometry figures: Horizontal plane vs. vertical plane, line of sight, angle of elevation, angle of depression.
   - Sinusoidal & Cosine Curves: Amplitude, period, phase shift, vertical shift, intercepts, peak/trough coordinates.
5. **Statistics & Data Handling:**
   - Box-and-Whisker Plots: Five-number summary clearly identified: Minimum, Lower Quartile ($Q_1$), Median ($Q_2$), Upper Quartile ($Q_3$), Maximum, and any plotted outliers.
   - Ogives (Cumulative Frequency Curves): Axis scales, points plotted $(x_i, F_i)$, median line and quartiles.
   - Histograms & Frequency Polygons: Class intervals, frequencies, bin widths.
   - Scatter plots: Points plotted, line of best fit (least squares regression line) with equation $\hat{y} = a + bx$, correlation coefficient ($r$).
6. **Mathematical Literacy:**
   - Till slips, invoices, and bank statements: Header, date, itemized list, subtotal, VAT (15%), total, change, account numbers (masked).
   - Tariffs & Municipal Bills: Stepped block tariff tables (water/electricity consumption tiers: $0–6\text{ kL}$, $6–12\text{ kL}$, etc.).
   - Assembly Plans & Maps: Strip charts, floor plans, compass directions, layout diagrams, packaging configurations (boxes in a crate).

---

### C. Physical Sciences (Physics & Chemistry)

1. **Mechanics & Vectors:**
   - Free-Body Diagrams (FBD) & Force Diagrams: Every force vector with labeled arrow, name, and direction (e.g. $F_g$ / $w$ downwards, $F_N$ normal perpendicular to surface, $f_k$ kinetic friction opposing motion, $F_{\text{applied}}$ at angle $\theta$ to horizontal).
   - Motion Graphs: $v-t$ (velocity-time), $s-t$ (position-time), $a-t$ (acceleration-time) graphs with exact coordinates at critical timestamps, slopes, areas under curve.
   - Ticker-Timer Tapes: Direction of motion, distance between dots ($\text{cm}$ or $\text{mm}$), timer frequency (e.g. $50\text{ Hz} \implies 0,02\text{ s}$ per dot).
2. **Waves, Sound & Light:**
   - Doppler Effect: Stationary vs. moving source, wave fronts (compressed in front, stretched behind), observer position, velocity vectors ($v_s, v_L$).
   - Photoelectric Effect: Graph of Maximum Kinetic Energy ($E_{k(\text{max})}$) vs. Frequency ($f$), threshold frequency ($f_0$ $x$-intercept), work function ($W_0$ $y$-intercept), Planck's constant ($h$ slope).
3. **Electricity & Magnetism:**
   - Circuit Schematics: EMF ($\mathcal{E}$), internal resistance ($r$), parallel branches, series resistors, rheostats, open/closed switch states ($S_1, S_2$), ammeters, voltmeters.
   - Alternating Current (AC): Generators vs. electric motors (split-ring commutator vs. slip rings), magnetic field pole orientation ($\text{N}$ to $\text{S}$), direction of coil rotation.
   - Electrostatics: Charged spheres ($Q_1, Q_2$), distances ($r$), field line patterns, point charges.
4. **Chemistry & Organic Reactions:**
   - **Organic Chemical Formulae Standard:**
     - **NEVER use fragile ASCII/LaTeX matrices** (`\begin{matrix}` with `\quad`) to draw 2D branching molecular trees.
     - **Always use standardized IUPAC condensed structural formulae** (e.g. $\text{CH}_3\text{COCH(CH}_3)\text{CH}_3$, $\text{CH}_3\text{CCl(CH}_3)\text{CH}_2\text{CH}_2\text{CH(CH}_3)\text{CH(Cl)CH}_3$).
     - Supplement with an explicit textual description detailing:
       - Parent carbon chain length (e.g. 7 carbons $\implies$ heptane stem).
       - Positions of all double or triple bonds (e.g. hex-2-ene).
       - All functional groups and substituent branches with exact carbon numbering (e.g. 2,6-dichloro, 2,5-dimethyl).
   - **Reaction Rate & Equilibrium Curves:**
     - Must transcribe exact coordinates: initial concentration at $t = 0$, intermediate points required for rate calculations (e.g. $t = 10\text{ s}, [\text{O}_2] = 0,15\text{ mol}\cdot\text{dm}^{-3}$), and equilibrium plateau values.
     - Differentiate line styles: solid vs. dashed lines, forward vs. reverse rate curves.
     - Potential Energy Profiles: Reactant energy level, product energy level, activated complex peak, activation energy for forward reaction ($E_{af}$), reverse reaction ($E_{ar}$), heat of reaction ($\Delta H$).
   - **Electrochemical Cells:**
     - Galvanic vs. Electrolytic cell classification.
     - Half-cells: Anode (-) and Cathode (+), electrode materials (e.g. $\text{Zn}$, $\text{Cu}$, $\text{Pt}$), electrolyte solutions and concentrations ($1\text{ mol}\cdot\text{dm}^{-3}$).
     - Salt bridge, external circuit electron flow direction, voltmeter reading ($E^\circ_{\text{cell}}$).

---

### D. Life Sciences (Biology) & Natural Sciences

1. **Anatomical & Cellular Structures:**
   - Label pointers: Every letter or numbered pointer ($A, B, C$ or $1, 2, 3$) mapped to the exact part of the organ or tissue.
   - Cross-sections: Nephron, reflex arc, human ear, human eye, heart chambers/valves, brain parts, chloroplast, mitochondrion.
   - Microscopic / Histological diagrams: Layers identified (epidermis, cortex, xylem, phloem).
2. **Genetics & Heredity:**
   - Pedigree Diagrams: Generations labeled by Roman numerals (I, II, III), individuals numbered left to right ($1, 2, 3$).
   - Shape code: Squares = males, Circles = females; Shaded = affected, Unshaded = unaffected, Half-shaded = carrier.
   - Punnett Squares & Karyotypes: Complete gamete alleles and offspring genotype grid; autosome pairs (1–22) and sex chromosomes ($XX$ or $XY$).
3. **Ecology & Environmental Studies:**
   - Food Webs: Every organism named, arrows pointing in direction of energy transfer from producer to tertiary consumer.
   - Population Curves: Lag phase, exponential (log) growth phase, deceleration phase, carrying capacity ($K$ asymptote).

---

### E. Languages & Visual Literacy (English, Afrikaans, African Languages)

Visual literacy contributes up to 40% of marks in Paper 1 Language exams:

1. **Editorial Cartoons & Comic Strips (Visual Irony & Satire):**
   - Transcribe frame-by-frame: `[CARTOON: FRAME 1] ... [CARTOON: FRAME 2] ...`.
   - Characters: Physical depiction, posture, size comparison, clothing, cultural signifiers.
   - Facial Expressions & Emotions: Eyes (wide, squinting, rolled), mouth (gaping, smiling, grimacing), eyebrows.
   - Body Language & Actions: Pointing, running, slouching, hand gestures, sweat drops / motion lines.
   - Verbal Elements: Speech bubbles, thought bubbles, shouting text (capitalization, bold fonts), sound effects (onomatopoeia).
   - Visual Satire / Irony: Metaphors (e.g. sinking ship representing failing company, oversized shadow).
2. **Advertisements & Media Studies:**
   - Headlines & Slogans: Verbatim text, font style, sizing relative to page.
   - Body Copy: Full promotional paragraph transcribed word-for-word.
   - Visual Layout & Focal Point: What element the eye is drawn to first, rule of thirds, contrast.
   - Persuasive Techniques: Emotional appeal, scientific/statistical claims, celebrity endorsement, fear of missing out (FOMO).
   - Call to Action & Commercial Details: Logo, website, telephone number, terms & conditions, fine print.
3. **Infographics in Comprehension Texts:**
   - Title, subtitle, source, publisher.
   - Every graph, data card, percentage icon, and explanatory text box transcribed into structured markdown.

---

### F. Commercial Subjects (Accounting, Business Studies, Economics)

1. **Accounting Formats & Ledger Tables:**
   - Financial Statements: Standard CAPS layout (Balance Sheet, Statement of Comprehensive Income, Cash Flow Statement, Notes to Financial Statements).
   - Column layout: Distinct columns for Details, Workings/Calculations, Amount ($\text{R}$), and inner/outer totals.
   - Fill-in-the-blank exam sheets: Incomplete ledger accounts must clearly indicate blank cells with placeholder question numbers (e.g. `[1.1.1]`, `[1.1.2]`) so students can calculate missing figures.
   - General Ledger Accounts: T-account format with Debit (left) and Credit (right), including Date, Details, Folio, Amount.
2. **Economics & Business Studies:**
   - Economic Graphs: Supply and demand curves, market equilibrium ($P_e, Q_e$), curve shifts ($S \to S_1$, $D \to D_1$), price elasticity, price ceilings/floors.
   - Circular flow diagrams, Business Cycle phases (prosperity, recession, depression, recovery).
   - Business Studies: Organograms (hierarchy of management), SWOT and PESTLE matrices.

---

### G. Geography, History & Social Sciences

1. **Geography:**
   - Topographical Maps (1:50 000) & Orthophoto Maps (1:10 000):
     - Scale, contour interval ($20\text{ m}$ for topo, $5\text{ m}$ for orthophoto).
     - Spot heights (e.g. $\cdot 1420$), trigonometric stations (e.g. $\triangle 214$), bench marks.
     - Grid coordinates: Latitude and Longitude to degrees, minutes, and seconds ($33^\circ 55' 30''\text{S}, 18^\circ 25' 15''\text{E}$).
     - Drainage density, river patterns (dendritic, trellis, radial), landform features (spurs, valleys, mesas, buttes).
   - Synoptic Weather Charts:
     - Isobars (labeled with pressure in $\text{hPa}$, e.g. $1016, 1020$).
     - High pressure cells (South Atlantic High, South Indian High, Kalahari High) and Low pressure cells.
     - Frontal systems: Cold front (spikes pointing in direction of travel), warm front.
     - Weather station model symbols: Cloud cover (octas), wind speed/direction (feathers on shaft), air temperature, dew point temperature, precipitation symbols.
2. **History:**
   - Primary Source Photographs: Description of depicted individuals, background setting, crowd reactions, historical uniforms/banners.
   - Propaganda Posters: Slogans, caricature depictions of enemies, national symbols, color symbolism, target audience message.
   - Historical Maps: Territorial boundaries, military movement arrows, conquered zones, treaty borders.

---

### H. Information Technology (IT) & Computer Applications Technology (CAT)

1. **Information Technology (Software & Database Design):**
   - UML Class Diagrams:
     - Class Name (e.g. `TStudent`).
     - Attributes with visibility markers: `+` (public), `-` (private), `#` (protected), with data types (`- fName : String`, `- fMark : Integer`).
     - Methods: `+ getAverage() : Real`, `+ setMark(pMark : Integer) : Void`.
     - Relationships: Inheritance (open triangle arrow), Association, Composition (filled diamond), Aggregation (open diamond).
   - Database Entity Relationship Diagrams (ERD): Entities, primary keys (PK), foreign keys (FK), cardinalities ($1:1$, $1:N$, $M:N$).
   - Flowcharts: Standard ANSI shapes: Terminator (oval), Process (rectangle), Decision (diamond with Yes/No branches), Input/Output (parallelogram).
2. **Computer Applications Technology (CAT):**
   - Software UI Screenshots: Transcribe ribbon tabs, active dialog boxes, font selection menus, page layout settings.
   - Spreadsheet Tables: Explicit row numbers (1, 2, 3...) and column letters (A, B, C...) with cell values and formulas (`=VLOOKUP(...)`, `=COUNTIF(...)`).
   - Network Topologies: Star, Bus, Ring, Mesh diagrams with labeled hubs, switches, routers, workstations, servers.

---

## 3. Mathematical & KaTeX Syntax Guardrails (Universal)

To guarantee that KaTeX parsers, math rendering engines, and LLM tokenizers never crash:

1. **Strict Degree Celsius Formatting:**
   - **CORRECT:** `$25\,^\circ\text{C}$` or `^\circ\text{C}` or `$^\circ\text{C}$`
   - **FORBIDDEN:** `\text{^\circ C}` (superscripts inside `\text{}` are invalid KaTeX and trigger fatal render errors).
2. **Decimal Separators in KaTeX:**
   - In South African curriculum, commas are standard decimal separators (e.g. $0,15$).
   - Inside math mode, write `$0{,}15$` or `$12{,}5$` with braces around the comma so KaTeX treats it as a decimal separator rather than a list punctuation mark (preventing unwanted whitespace like `0, 15`).
3. **Display Equations:**
   - Each major formula must sit on its own dedicated display line (`$$ ... $$`).
   - Never smash multiple distinct equations into a single `$$` line. If steps belong together, use `\begin{aligned} ... \end{aligned}` with line breaks `\\`.
4. **Fractions & Radicals:**
   - Always verify balanced braces: `\frac{numerator}{denominator}` and `\sqrt{radicand}`.
   - Never write bare `\frac` without braces.

---

## 4. Transcription Schema & Tags

All visual descriptions must follow this standardized tagging contract:

```markdown
[DIAGRAM: <Discipline Type> | <Key Details> | <Coordinates / Ratings / Specifics>]
```

### Examples of Compliant Transcriptions:

- **EGD Mechanical Assembly:**
  ```markdown
  [DIAGRAM: EGD 3rd Angle Orthographic Projection | Assembly of Shaft Coupling | Front View full section on cutting plane A-A showing M20 hex bolt, lock washer, and 8 mm square key; Right Elevation showing 120 mm pitch circle diameter with 4 x 18 mm clearance holes; Scale 1:1; All dimensions in mm]
  ```
- **Physics Reaction Kinetics:**
  ```markdown
  [DIAGRAM: Physical Sciences Kinetics Graph | Concentration of O₂(g) vs Time (s) | Curve starts at (0 s, 0,27 mol·dm⁻³), decreases non-linearly passing through (10 s, 0,15 mol·dm⁻³), (20 s, 0,09 mol·dm⁻³), (30 s, 0,05 mol·dm⁻³), and levels off at equilibrium at (52 s to 60 s, 0,025 mol·dm⁻³); Solid line on sealed 3 dm³ system]
  ```
- **Organic Chemistry Molecule:**
  ```markdown
  [DIAGRAM: Organic Chemistry Structural Formula | 2,6-dichloro-2,5-dimethylheptane | Condensed formula CH₃-CCl(CH₃)-CH₂-CH₂-CH(CH₃)-CH(Cl)-CH₃ | 7-carbon main chain with chlorine and methyl substituents at carbon 2, methyl substituent at carbon 5, and chlorine substituent at carbon 6]
  ```
- **Language Cartoon:**
  ```markdown
  [DIAGRAM: Language Cartoon | Madam & Eve by Francis & Dugmore | 3 Frames |
  FRAME 1: Eve standing with broom looking shocked, mouth wide open with speech bubble: "Did you see the electricity bill?!"; Madam sitting at kitchen table holding coffee cup looking nonchalant.
  FRAME 2: Madam takes sip of coffee with calm half-smile, speech bubble: "I switched off the geyser."
  FRAME 3: Wide shot showing entire kitchen plunged into darkness with only two pairs of eyes visible, speech bubble from Madam: "...and the main breaker."]
  ```
- **Mathematics Euclidean Geometry:**
  ```markdown
  [DIAGRAM: Euclidean Geometry | Circle Center O with Cyclic Quad ABCD | Tangent EF touches circle at point B; Chord BD connects to circumference; Chord AC intersects BD at point P; Given angle EBA = 42°, angle CBD = 38°; Parallel lines AB || DC indicated by single arrows; Angle BDC marked as x]
  ```

