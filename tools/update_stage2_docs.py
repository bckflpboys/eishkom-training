"""
Update GUIDE.md, README.md, and PROGRESS.md with the detailed breakdown of:
1. Stage 1 Subject-Adaptive Teaching Styles & Multi-Task Curriculum
2. Stage 2 (v2 Models) Strategy Permutation Architecture
"""

from pathlib import Path

# 1. Update GUIDE.md
guide_p = Path('GUIDE.md')
guide_text = guide_p.read_text(encoding='utf-8')

stage2_guide_section = """
### Step 5b: Pedagogical Styles in Stage 1 vs Stage 2 Strategy Permutation (v2 Roadmap)

#### How Teaching Styles Work in Stage 1:
- **It is NOT 1 generic style for all subjects.** The teacher model trains on **different pedagogical styles adapted to the cognitive demands of each subject**:
  1. **Mathematics & Wiskunde:**
     - Uses **Polya's 4-step problem solving** (`understand_problem`, `devise_plan`, `carry_out_plan`, `look_back`).
     - Employs **factor-pair search**, **check by substitution**, and explicit **`[TOOL CHECK: calculator(...)]`** in private chain-of-thought so arithmetic is verified rather than guessed.
  2. **Physical Sciences & Fisiese Wetenskappe:**
     - Uses **concept mapping** and **formula-selection-first**.
     - Enforces **units checks** (e.g. converting $\\text{km/h}$ to $\\text{m/s}$, checking SI units $\\text{N}$, $\\text{J}$, $\\text{W}$), identifying force directions (perpendicular normal force, frictional opposing force), and tool-checked arithmetic.
  3. **Languages (English & Afrikaans HL / FAL):**
     - Uses **context clues**, **quote extraction**, **paraphrasing**, and **mark-per-point** scoring.
     - Guides visual literacy (frame-by-frame cartoon body language, font emphasis, advertising target audiences).
  4. **Adaptive Student Personas Across All Subjects:**
     - **Frustrated / Anxious Learners:** Validates emotions first (*"Take a deep breath, let's break this into one small piece"*), lowers cognitive anxiety, and gives micro-clues.
     - **Short-Answer Learners:** Matches students who only reply with 1-3 words by providing tight, punchy, single-question nudges instead of lecturing.
     - **Memory Mnemonics & Analogies:** Uses memory hooks (e.g. '$V$' points down so vertical means up-and-down; '$H$' is flat like the horizon; 4IR initials for Fourth Industrial Revolution).
- **Multi-Task Curriculum Ratio (1:2):** 1 structured full worked solution demonstration (`answer_policy: "full_solution"`) per 2 Socratic hint dialogues (`answer_policy: "guided"`).

#### Stage 2 (v2 Models) Architecture: Strategy Permutation
> [!IMPORTANT]
> **Stage 2 (v2) Permutation Architecture:**
> In Stage 2 (v2 of the models), we will be retraining on the **exact same 265 question papers but across systematically rotated teaching styles**.
> For example:
> - If **November 2021 Mathematics P1** was trained using `step_walkthrough` (standard Socratic hint ladder) in Stage 1:
> - In Stage 2, that **same exam paper** will be regenerated and retrained under alternate pedagogical styles:
>   1. `worked_example`: The tutor provides a fully solved parallel problem first, then asks the student to solve the DBE question.
>   2. `mnemonic_memory_hook`: The tutor focuses heavily on cognitive memory tricks, analogies, and visual metaphors.
>   3. `faded_example`: The tutor provides a partially completed solution with key operational blanks for the student to complete.
>   4. `frustrated_learner_recovery`: Explicit training on emotional de-escalation and building learner confidence.
>   5. `rapid_short_prompt`: Ultra-concise, rapid-fire Q&A optimized for mobile chat.
> - **The Result:** This multiplies our training corpus **4x–5x (10,000+ to 15,000+ SFT samples)** entirely from our verified 265 DBE exam papers, giving the Stage 2 models unprecedented stylistic versatility without needing external or unverified question papers.
"""

if "### Step 5b: Stage-2 Strategy Permutation Architecture (v2 Roadmap)" in guide_text:
    guide_text = guide_text.replace(
        "### Step 5b: Stage-2 Strategy Permutation Architecture (v2 Roadmap)",
        stage2_guide_section.strip()
    )
elif "### Step 5b:" not in guide_text:
    guide_text = guide_text.replace("### Step 6: Verify and Filter", stage2_guide_section + "\n### Step 6: Verify and Filter")

for p in [Path('GUIDE.md'), Path('sa-tutor-kit/sa-tutor-kit/GUIDE.md')]:
    p.write_text(guide_text, encoding='utf-8')
    print(f'Updated {p}')

# 2. Update README.md
readme_p = Path('README.md')
readme_text = readme_p.read_text(encoding='utf-8')
stage2_readme_note = """
- **Pedagogical Strategy & Stage 2 (v2) Roadmap:**
  - **Stage 1 (Current):** Employs **subject-adaptive teaching styles** (Polya 4-step & substitution check for Maths; concept mapping & SI units for Physics; context clues & visual literacy for Languages; frustrated learner de-escalation & mnemonics across all subjects) balanced in a **1:2 Multi-Task Curriculum Ratio** (1 full solution demonstration per 2 Socratic hint dialogues).
  - **Stage 2 (v2 Models):** Will execute the **Strategy Permutation Architecture**: retraining on the **exact same 265 question papers** across systematically rotated teaching styles (`worked_example`, `mnemonic_memory_hook`, `faded_example`, `frustrated_learner_recovery`, `rapid_short_prompt`). This scales the corpus 4x–5x (10,000+ samples) completely organically from verified DBE past papers.
"""

if "Stage 2 (v2 Models):" not in readme_text:
    readme_text = readme_text.replace("## Quick Navigation", stage2_readme_note + "\n## Quick Navigation")
    for p in [Path('README.md'), Path('sa-tutor-kit/sa-tutor-kit/README.md')]:
        p.write_text(readme_text, encoding='utf-8')
        print(f'Updated {p}')

# 3. Update PROGRESS.md
prog_p = Path('PROGRESS.md')
prog_text = prog_p.read_text(encoding='utf-8')
stage2_prog_section = """
### 1.5. Stage 2 (v2 Models) Architectural Roadmap: Pedagogical Strategy Permutation

> [!NOTE]
> **Stage 2 Sidenote & Strategic Permutation Policy:**
> In Stage 2 (v2 of the models), we will be training on the **exact same 265 question papers across different pedagogical teaching styles**.
> - In Stage 1: Each paper is trained on subject-adaptive Socratic guidance (`step_walkthrough`) paired with formal full worked solutions (`full_solution`) in a 1:2 ratio.
> - In Stage 2: The exact same question papers will be regenerated and retrained under alternate teaching styles:
>   - `worked_example` (Modelled parallel problem followed by learner execution)
>   - `mnemonic_memory_hook` (Cognitive memory aids, visual analogies like $V$ for vertical lines, and conceptual hooks)
>   - `faded_example` (Partially worked solutions with fill-in-the-blank steps)
>   - `frustrated_learner_de-escalation` (Emotional validation, confidence building, and micro-clues)
>   - `rapid_short_prompt` (Ultra-concise Q&A for mobile micro-tutoring)
> - This strategy multiplies the corpus 4x–5x (**10,000+ to 15,000+ verified SFT samples**) without requiring new exam papers, guaranteeing that the Stage 2 tutor can seamlessly pivot its teaching style based on what works best for each individual student.
"""

if "### 1.5. Stage 2 (v2 Models)" not in prog_text:
    prog_text = prog_text.replace("## 2. Stage 1 Model Architecture & Lineup", stage2_prog_section + "\n## 2. Stage 1 Model Architecture & Lineup")
    for p in [Path('PROGRESS.md'), Path('sa-tutor-kit/sa-tutor-kit/PROGRESS.md')]:
        p.write_text(prog_text, encoding='utf-8')
        print(f'Updated {p}')

print('All documentation successfully updated and synchronized across all mirrors!')

