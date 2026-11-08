# Eishkom Stage 1 — Developer Execution Guide

> **Release Cycle:** Stage 1  
> **Workflow:** End-to-End Pipeline from Raw DBE PDFs to Fine-Tuned GGUF Models & Cloud Run Hosting

---

## Quick Reference Command Cheatsheet

```bash
# ==============================================================================
# PHASE 1: COLLECT SOURCES (ALREADY COMPLETED & VERIFIED)
# ==============================================================================
python pipeline/download_dbe.py --dry-run
python pipeline/download_dbe.py

# ==============================================================================
# PHASE 2: MULTIMODAL VISION INGESTION & TWO-PASS VERIFICATION (COMPLETED)
# ==============================================================================
python pipeline/ingest_vision.py --pipeline-order
python pipeline/sanitize_text.py
python pipeline/verify_extractions.py

# ==============================================================================
# PHASE 2.5: ITEM EXTRACTION (QUESTIONS & MEMOS) — 100% COMPLETED
# ==============================================================================
python pipeline/extract_items.py --source <source_id>

# ==============================================================================
# PHASE 3: HELD-OUT EVALUATION BENCHMARK (QUARANTINED)
# ==============================================================================
python pipeline/build_eval.py --year 2024 --session nov --grade 12

# ==============================================================================
# PHASE 4: TEACHER GENERATION & SAMPLES EXPANSION (2,000+ SAMPLES REACHED)
# ==============================================================================
python tools/run_wave3_turbo.py

# ==============================================================================
# PHASE 5: CONVERT ITEMS TO FULL SOLUTIONS (1:2 MULTI-TASK RATIO)
# ==============================================================================
python tools/convert_raw_items_to_full_solutions.py

# ==============================================================================
# PHASE 6: SFT DATASET PACKAGING
# ==============================================================================
python tools/package_all_verified_sft.py
python sa-tutor-kit/sa-tutor-kit/tutor_data.py build workspace/verified/train_master_combined.jsonl --out workspace/build/r1 --val 0.15

# ==============================================================================
# PHASE 7 & 8: VERTEX AI COLAB ENTERPRISE SFT & GGUF EXPORT
# (Execute inside colab/sa_tutor_colab.ipynb on NVIDIA L4 Spot VM)
# ==============================================================================
# koeberg-stage-1 (27B) -> koeberg-stage-1-UD-Q4_K_XL.gguf
# kendal-stage-1 (4B)   -> kendal-stage-1-Q6_K.gguf & kendal-flash-stage-1-Q4_K_M.gguf
# gariep-stage-1 (2B)   -> gariep-stage-1-Q6_K.gguf

# ==============================================================================
# PHASE 9: DEPLOY KOEBERG-STAGE-1 TO GOOGLE CLOUD RUN (SCALE-TO-ZERO)
# ==============================================================================
gcloud run deploy koeberg-stage-1 \
  --image gcr.io/$PROJECT_ID/koeberg-stage-1:latest \
  --gpu 1 --gpu-type nvidia-l4 --cpu 8 --memory 32Gi \
  --min-instances 0 --max-instances 1 --concurrency 10
```

---

## Detailed Step-by-Step Instructions

### Step 0: Environment Pre-Flight
1. Verify Python 3.12: `python --version`.
2. Install SymPy if missing: `pip install sympy`.
3. Check teacher API key in `.env`: `TEACHER_API_KEY=...`.
4. Run verification tests:
   ```bash
   python answers.py
   python board.py
   python tools_sim.py
   python retrieval.py test
   python llm.py test
   python tutor_data.py validate examples/examples.jsonl
   ```

### Step 1: Raw Exam Papers & Memorandums (Completed)
- 600 PDFs downloaded into `workspace/raw/dbe/` covering Grades 10–12 Mathematics, Physical Sciences, English, and Afrikaans.
- All documents paired in `workspace/sources/sources.csv`.

### Step 2: Multimodal Vision Ingestion & Two-Pass Verification (Completed & Audited)
- **Vision Extraction:** Ingested all 600 exam documents into `workspace/text/` using Gemini Multimodal Vision (**11,310,442 characters**, 354 KaTeX LaTeX documents, 1,005 geometric diagrams).
- **Deterministic KaTeX Sanitizer:** Cleaned 137 files via `pipeline/sanitize_text.py`, eliminating empty `$$ $$` blocks and closing unclosed environments in 0.5s.
- **Two-Pass Verification Audit:** Audited all 301 exam pairs via `pipeline/verify_extractions.py`, achieving **287 / 301 clean structural passes (95.3%)**, **47,299 KaTeX formulas**, and **1,005 verified diagrams**. Report persisted in `workspace/reports/extraction_verification_report.json`.

### Step 3: Segment into Structured Question-and-Answer Items (Phase 2.5 — 100% Completed)
- **Status:** **Completed 100%** (265 / 265 verified papers extracted, 13,168 atomic items, 31,278 marks accounted for, 0 KaTeX delimiter errors).
- **Autonomous Multi-Lane Fleet Extraction:**
  - Multi-lane turbo workers executed parallel code-style extraction with AI Studio (`gemini-3.5-flash-lite`) and OpenRouter models.
  - Live progress tracked in `workspace/EXTRACTION_TRACKER.md` across all 301 exam pairs (33 held-out benchmarks quarantined).
  - Sync tracker status anytime: `python workspace/tools/sync_tracker.py`.
- **Universal Extraction Standards (UDVES):**
  - **Mathematical Equations:** Standardized into LaTeX inside `$..$` (inline) or `$$..$$` (display block) with `$0{,}1$` comma spacing.
  - **Text-Describable Diagrams (~20%):** Geometry circles, triangles, circuits, coordinate graphs have spatial relations written into `"passage"`.
  - **Chemistry & Sciences:** Standardized into condensed IUPAC formulas (e.g. $\text{CH}_3\text{CH}_2\text{OH}$) with reaction coordinates; zero fragile 2D matrices.
  - **Languages & Visual Literacy:** Full reading passages, frame-by-frame cartoon descriptions, and advertising layouts preserved in `"passage"`.
  - **Pure Visual Figures:** Flagged `"needs_review": true`, excluded from text SFT, preserved for multimodal training on `LiquidAI/LFM3-VL-2B` (`gariep-flash-stage-1`).

### Step 4: Reserve the 2024 Benchmark
- The November 2024 Grade 12 items are compiled into `workspace/eval/eval_items.jsonl`.
- These items are never exposed during training (0% contamination benchmark).

### Step 5: Distill Socratic Dialogues & Multi-Task Curriculum (2,000+ SAMPLES)
- Multi-model teacher fleet: OpenAI (`gpt-6-luna`, `xhigh` reasoning), Google AI Studio (Gemini 3.5 & 3.1 Flash Lite, 24k thinking budget), OpenRouter (Nemotron Ultra), and Intern-AI (DeepSeek V4.1).
- **Pedagogical Standards:**
  - **Socratic Hint Ladder:** Do not give the answer away immediately. Diagnose misconception first, offer small clues, ask one question at a time and wait.
  - **Frustrated Learners:** Validate learner emotion, de-escalate anxiety ("Take a deep breath, let's break this down"), reduce cognitive load.
  - **Short-Answer Learners:** Provide punchy, concise single-question prompts that match the student's brief interaction style.
  - **Mnemonics & Memory Aids:** Ground abstract concepts in memorable rules (e.g., 'V' points down so vertical means up-and-down; 4IR letters).
- **Embedded Tool-Calling Procedure:**
  - In calculation subjects (Maths, Wiskunde, Physical Sciences), the model embeds explicit calculator checks into its private reasoning:
    `[TOOL CHECK: calculator(expression="...") -> result]`
  - Trains the model to verify calculations with tools rather than hallucinating multi-digit arithmetic.
- **Multi-Task Curriculum Ratio (1:2):**
  - Balance 1 structured full worked solution (`answer_policy: "full_solution"`) per 2 Socratic hint dialogues (`answer_policy: "guided"`).
  - Grounded in official DBE mark schemes while anchoring conversational behavior in Socratic patience.

### Step 5b: Pedagogical Styles in Stage 1 vs Stage 2 Strategy Permutation (v2 Roadmap)

#### How Teaching Styles Work in Stage 1:
- **It is NOT 1 generic style for all subjects.** The teacher model trains on **different pedagogical styles adapted to the cognitive demands of each subject**:
  1. **Mathematics & Wiskunde:**
     - Uses **Polya's 4-step problem solving** (`understand_problem`, `devise_plan`, `carry_out_plan`, `look_back`).
     - Employs **factor-pair search**, **check by substitution**, and explicit **`[TOOL CHECK: calculator(...)]`** in private chain-of-thought so arithmetic is verified rather than guessed.
  2. **Physical Sciences & Fisiese Wetenskappe:**
     - Uses **concept mapping** and **formula-selection-first**.
     - Enforces **units checks** (e.g. converting $\text{km/h}$ to $\text{m/s}$, checking SI units $\text{N}$, $\text{J}$, $\text{W}$), identifying force directions (perpendicular normal force, frictional opposing force), and tool-checked arithmetic.
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
- In Stage 2 (v2 of the models), the exact same 265 core DBE question papers will be systematically re-prompted across multiple pedagogical styles:
  1. `step_walkthrough` (Standard Socratic hint ladder)
  2. `worked_example` (Full modelled problem followed by a parallel problem)
  3. `mnemonic_memory_hook` (Focus on cognitive memory aids and analogies)
  4. `faded_example` (Partially worked problem with missing blanks for the learner)
  5. `frustrated_learner_de-escalation` (Emotional regulation and confidence rebuilding)
  6. `rapid_short_prompt` (Ultra-concise Q&A for mobile micro-learning)
- This multiplies the corpus 4x–5x (10,000+ samples) purely from verified DBE past papers, achieving stylistic versatility with zero unverified external data.

### Step 6: Verify and Filter
- Run automated verification against SymPy and official DBE memorandums with forensic South African decimal comma normalization (`$13{,}32$` -> `13.32`).
- Rejects any generated dialogue where the mathematical calculation disagrees with SymPy or the official memo.

### Step 7: SFT Training in Vertex AI Colab Enterprise
- Open `colab/sa_tutor_colab.ipynb` inside Google Cloud Console.
- Choose **NVIDIA L4 GPU (24GB VRAM)** with **Spot VM** enabled (~$0.32/hr).
- Fine-tune unquantized base Hugging Face repositories using Unsloth QLoRA.
- Checkpoints saved after each epoch to Google Drive (`--resume` protects against spot preemption).
- Export GGUF binaries (`UD-Q4_K_XL`, `Q6_K`, `Q4_K_M`) via `training/export_gguf.py`.

### Step 8: Deploy Koeberg to Cloud Run
- Deploy `koeberg-stage-1` containerized to Google Cloud Run with scale-to-zero (`--min-instances 0`).
- Idle cost: $0.00/hour.
- Active cost: ~$0.015/minute.
