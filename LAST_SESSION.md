# Eishkom AI — Session Handoff & Continuity Ledger

> **File Name:** `LAST_SESSION.md`  
> **Last Session Date:** 2026-11-14  
> **Repository Branch:** `main` (clean working tree, zero unauthorized git commits)  
> **Purpose:** Master continuity bridge for moving across chat sessions without loss of context, history, or engineering decisions.

---

## 1. Executive Summary & Model Fleet Status

**Eishkom AI** is building a family of open-source, South African CAPS curriculum-aligned AI tutor models (Grades 7–12 & TVET) designed for high pedagogical quality (Socratic hint ladders, diagnostic questioning, English and Afrikaans support).

### Clean Model Branding (Mandatory Rule):
Public model names **never display parameter numbers or quantization suffixes** (`27B`, `4B`, `Q4`, `Q6` are strictly hidden from brand names):
1. **`koeberg-stage-1`**: Flagship Cloud Tutor (unsloth/Qwen3.8-27B, `UD-Q4_K_XL`, ~17.6 GB) — Google Cloud Run (Serverless NVIDIA L4, scale-to-zero).
2. **`kendal-stage-1`**: Budget PC & Laptop Tutor (unsloth/Qwen3.5-4B, `Q6_K` / `UD-Q6_K_XL`, ~3.40 GB) — **TRAINED & EXPORTED** (870 steps, loss 0.34, 100% offline).
3. **`kendal-flash-stage-1`**: Midrange Mobile & Phone Tutor (empero-ai/Qwen3.8-4B-Distill, `Q4_K_M`, ~2.65 GB) — **EXPORTED** (100% offline).
4. **`gariep-stage-1`**: Budget Phone Tutor (empero-ai/Qwen3.8-2B-Distill, `Q8_0` / `Q6_K` / `Q4_K` / `Q4_K_M`, ~1.35–2.15 GB) — **TRAINED & EXPORTED** (3 epochs, 100% offline).
5. **`gariep-flash-stage-1`**: Budget Vision/OCR Tutor (LiquidAI/LFM3-VL-2B or Qwen2-VL-2B, `Q6_K` + `mmproj`, ~1.55 GB) — **Architecture finalized for Page-Worker pipeline**.
6. **`baby-jake-stage-3`** *(or `atom-stage-3`)*: Ultra-Budget Celeron & Entry Phone Tutor (1B, Q4_K_M ~650–850 MB) — Scheduled for Stage 3 via local self-distillation.

---

## 2. Historic Milestones & Architectural Breakthroughs (Nov 13–14, 2026)

### 1. Stage 2 Dedicated Fleet 100% Complete (23,503 Records):
- The dedicated Stage 2 generation daemon completed all 224 exam papers with exit code 0.
- Master verified corpus: **23,503 canonical records** across Mathematics, Physical Sciences, Natural Sciences, English (HL & FAL), and Afrikaans (Huistaal & EAT).
  - **Socratic Multi-Turn Lessons:** **10,591 records** (averaging 2–5 turns each across 10 teaching styles).
  - **Full Step-by-Step Solutions:** **12,912 records**.
- Schema repair and `tutor_data.py build` validation achieved a **99.99% pass rate** (23,500 of 23,503 valid).
- Compiled SFT datasets in `workspace/build/`:
  - `workspace/build/r2/` (Master Combined): **32,351 training samples** (81.3 MB), 5,853 validation, 2,037 test. Total: **40,241 SFT samples** (~28.5M tokens).
  - `workspace/build/r2_socratic/`: **21,999 training samples** (57.4 MB).
  - `workspace/build/r2_fullsol/`: **10,352 training samples** (23.9 MB).

### 2. Phase 2.5: Agentic Teacher & Study Coach Expansion:
- User supplied 4 design files: `conversation and idea for the agentic teacher.txt`, `stage2_agentic_mix_calculator.xlsx`, `eishkom_agentic_and_study_teacher_prompts.md`, and `sampler_agentic.py`.
- **Target Audience:** Small on-device models ($\le 4\text{B}$, e.g. `kendal-stage-1` 4B, `gariep-stage-1` 2B) running offline on budget phones and laptops.
- **Architectural Guardrails Established:**
  1. *Stateless Atomic Roles:* Decouple into **Page Worker** (single-page OCR notes with KV-cache purge after every page) and **Synthesiser / Coach** (dialogue grounded purely in notes and code-computed metrics). Prevents KV-cache explosion on mobile devices.
  2. *Deterministic Code Computation:* Models NEVER do math, date calculation, mark totals, or topic ranking. Python functions (`build_schedule()`, `rank_weak_topics()`, `time_plan()`, `aggregate_notes()`) calculate all numbers; the model only reads and explains them.
  3. *Exposure Budget Guardrail (< 20%):* Target **3,000 – 4,500 unique agentic samples** trained for 2 epochs = **6,000 – 9,000 exposures** (~11%–15% of total dataset exposures). Protects math/science reasoning core from dilution.
  4. *South African Wellbeing Protocol (`distress_signal`):* 2% of training data covers crisis de-escalation with verified South African helplines (SADAG: 0800 567 567 / 0800 456 789; Childline: 116; LifeLine: 0861 322 322).
  5. *Real Exam Item Grounding:* Revision sessions and study guides pull authentic questions and rubrics from our 265 DBE item files in `workspace/items/*.jsonl`.
- **Code Assets Created:**
  - `stage-2/agentic/sampler_agentic.py`: Spec builders, CAPS curriculum taxonomies, helpline directory, and arithmetic engines.
  - `stage-2/agentic/run_agentic_fleet.py`: Multi-provider generator connecting Google AI Studio, Groq, Cohere, OpenRouter, and NVIDIA NIM with retry backoff and tool call verification.

### 3. Phase 2.6: Context Compaction (Session Summaries) & Operations Engine:
- User integrated `sampler_ops.py` for on-device context compaction, state resumption, and reply budgets.
- **Architectural Tenet:** Code owns the facts and thresholds (token counters, ledger, when to compact); the model owns language judgment only (writing 5 strict state fields: `narrative`, `misconceptions`, `current`, `next`, `learner_notes`).
- **Exposure Target:** 10%–15% exposure share for all non-school tasks combined (page worker, study tasks, synthesiser, compaction, resume), strictly respecting the $\le 20\%$ ceiling.
- **Agentic Fleet Status:** Paused per user directive until new API keys and routes for superior models are provided.

### 4. Stage 2 Pass 2: Multi-Strategy Socratic Permutation Fleet (RUNNING & SCALING):
- Active background generation daemon (`python stage-2/run_stage2_fleet.py --pass 2`).
- **Pass 2 Verified Lessons:** **2,013 lessons** across 8 alternate pedagogical strategies (`step_walkthrough`: 253, `error_analysis`: 245, `exam_technique`: 243, `socratic_hints`: 228, `analogy_real_world`: 214, `worked_example`: 210, `faded_example`: 208, `mnemonic`: 207).
- **Total Project Socratic Lessons:** **12,604 lessons** (84.0% of 15,000 goal).
- **Total Project Corpus:** **25,516 records** (~45,200+ SFT samples / ~32M tokens).
- Output destinations: `workspace/verified/stage2_pass2/` and `stage-2/progress_pass2.json`.

---

## 3. Critical Notes for the Next Agent

> [!IMPORTANT]
> **Instructions for the Next Agent picking up this conversation:**
> 1. **Do NOT run `git commit` without explicit authorization from the user.**
> 2. **Pass 2 Multi-Strategy Fleet is ACTIVE in background:** Do not launch duplicate `run_stage2_fleet.py` processes. Check progress with `python stage-2/run_stage2_fleet.py --status`.
> 3. **Agentic Fleet on Hold:** Await user's new API keys and model routes before running `stage-2/agentic/run_agentic_fleet.py`.
> 4. **Master Corpus Ready:** `workspace/build/r2/` contains 40,241 SFT samples (~28.5M tokens) ready for Colab Enterprise training.
> 5. **Quad-Mirror Maintenance:** Keep all documentation synchronized between root `files/` and `sa-tutor-kit/sa-tutor-kit/`.

---

## 4. Key File Paths

| File | Location | Purpose |
| :--- | :--- | :--- |
| **Stage 2 Master Dataset (r2)** | `workspace/build/r2/` | 40,241 SFT samples (`train.jsonl`, `val.jsonl`, `test.jsonl`, ~28.5M tokens) |
| **Socratic Split (r2_socratic)** | `workspace/build/r2_socratic/` | 21,999 Socratic training samples |
| **Full Solutions Split (r2_fullsol)**| `workspace/build/r2_fullsol/` | 10,352 full solution training samples |
| **Agentic Sampler & Math Engine**| `stage-2/agentic/sampler_agentic.py` | Deterministic scheduling, ranking, time planning, and spec sampling |
| **Agentic Fleet Generator** | `stage-2/agentic/run_agentic_fleet.py` | Multi-provider LLM generation fleet for the 9 agentic task families |
| **Master Decisions Ledger** | `workspace/DECISIONS.md` | Chronological record of all architectural milestones |
| **Live Execution Tracker** | `PROGRESS.md` | Master execution roadmap and phase status |
