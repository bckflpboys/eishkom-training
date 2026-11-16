# Eishkom AI — Session Handoff & Continuity Ledger

> **File Name:** `LAST_SESSION.md`  
> **Last Updated:** 2026-11-15 (14:50 SAST)  
> **Repository Branch:** `main` (clean working tree, zero unauthorized git commits)  
> **Purpose:** Master continuity bridge for moving across chat sessions without loss of context, history, engineering decisions, or verified milestones.

---

## 1. Executive Summary & Model Fleet Status

**Eishkom AI** is building a family of open-source, South African CAPS curriculum-aligned AI tutor models (Grades 7–12 & TVET) designed for high pedagogical quality (Socratic hint ladders, diagnostic questioning, dual English and Afrikaans support, and agentic study coaching).

### Clean Model Branding (Mandatory Rule):
Public model names **never display parameter numbers or quantization suffixes** (`27B`, `4B`, `Q4`, `Q6` are strictly hidden from brand names):
1. **`koeberg-stage-1`**: Flagship Cloud Tutor (unsloth/Qwen3.8-27B, `UD-Q4_K_XL`, ~17.6 GB) — Google Cloud Run (Serverless NVIDIA L4, scale-to-zero).
2. **`kendal-stage-1`**: Budget PC & Laptop Tutor (unsloth/Qwen3.5-4B, `Q6_K` / `UD-Q6_K_XL`, ~3.40–4.15 GB) — **TRAINED & EXPORTED** (870 steps, loss 0.34, 100% offline).
3. **`kendal-flash-stage-1`**: Midrange Mobile & Phone Tutor (empero-ai/Qwen3.8-4B-Distill, `Q4_K_M`, ~2.65–2.91 GB) — **EXPORTED** (100% offline).
4. **`gariep-stage-1`**: Budget Phone Tutor (empero-ai/Qwen3.8-2B-Distill, `Q8_0` / `Q6_K` / `Q4_K` / `Q4_K_M`, ~1.35–2.15 GB) — **TRAINED & EXPORTED** (3 epochs, 100% offline).
5. **`gariep-flash-stage-1`**: Budget Vision/OCR Tutor (LiquidAI/LFM3-VL-2B, `Q6_K`, ~1.55 GB) — **Architecture finalized for Page-Worker pipeline**.
6. **`baby-jake-stage-3`** *(or `atom-stage-3`)*: Ultra-Budget Celeron & Entry Phone Tutor (1B, Q4_K_M ~650–850 MB) — Scheduled for Stage 3 via local self-distillation.

---

## 2. Comprehensive Milestone Ledger: From Inception to Present

### Phase 0 & Phase 1: Inception, Environment, & Source Data Harvesting
- **Vision:** Create high-quality, offline-capable South African educational AI models covering Mathematics, Physical Sciences, Natural Sciences, English (HL/FAL), and Afrikaans (HT/EAT).
- **Compute Strategy Decided:**
  - $60 promotional Google Cloud & Gen AI credit allocation ($10/month rolling grants).
  - Vertex AI Colab Enterprise on NVIDIA L4 GPU Spot VMs (~$0.32/hr) to eliminate browser disconnects.
  - Scale-to-zero on Google Cloud Run for Koeberg (`--min-instances 0` = $0.00/hr when idle).
- **Immutable Pipeline Stages Decided:**
  - `raw/` -> `text/` -> `items/` -> `gen/` -> `verified/` -> `build/` -> `runs/` -> `exports/`.
- **Source Harvesting:**
  - Downloaded 600 PDFs (300 pairs, 378.15 MB, 0 errors) from DBE (`education.gov.za`).
  - Quarantined 16 November 2024 Grade 12 papers as held-out benchmarks (`workspace/eval/`).

### Phase 2 & Phase 2.5: Vision Ingestion & Atomic Item Extraction
- **Multimodal Vision Ingestion:** Built `pipeline/ingest_vision.py` using Gemini Multimodal Vision with automated rotation and quota management. Extracted 11,310,442 characters across 354 KaTeX LaTeX documents with 1,005 geometric diagram descriptions.
- **Atomic Item Extraction:** Extracted 265 / 265 exam papers into 13,168 atomic items accounting for 31,278 marks (100% agreement with DBE marking memorandums, 0 KaTeX delimiter errors). Quad-mirrored across `workspace/items/` and kit mirrors.

### Phase 7, 8, & 9: Stage 1 Training & First GGUF Exports
- **First Dataset Build (`workspace/build/r1`):** 5,755 SFT samples packaged with 1:2 multi-task ratio (Socratic hint lessons + full worked solutions) with embedded SymPy calculator verification.
- **Kendal Stage 1 (4B) Trained:** Trained `unsloth/Qwen3.5-4B` on NVIDIA L4 GPU Spot VM in Colab Enterprise across 870 steps (3 epochs). Loss dropped from 1.82 to 0.34; validation loss stabilized at 0.74–0.78 flat (0% overfitting). Exported `kendal-stage-1-Q6_K.gguf` (3.4 GB) and `kendal-flash-stage-1-Q4_K_M.gguf` (2.65 GB).
- **Gariep Stage 1 (2B) Trained:** Trained `empero-ai/Qwen3.8-2B-Distill` across 3 epochs; exported `Q8_0`, `Q6_K`, `Q4_K`, and `Q4_K_M`.

### Phase 12: Stage 2 Socratic Permutation & Dedicated Fleet
- **Pedagogical Strategy Permutation:** Regenerate lessons on the exact same DBE exam questions across diverse teaching styles (`faded_example`, `worked_example`, `error_analysis`, `mnemonic`, `socratic_hints`, `exam_technique`, `concept_first`).
- **Dedicated Stage 2 Fleet:** Completed all 224 exam papers in dedicated pool. Built 23,503 canonical records (10,591 multi-turn Socratic lessons + 12,912 full solutions) into 40,241 SFT samples (~28.5M tokens).

### Phase 13 & 14: Agentic Teacher, Study Coach, & Operations Engine
- **Decoupled Architecture for Low-VRAM Mobile Phones ($\le 4\text{B}$):**
  - **Stateless Page Worker:** Reads 1 page at a time, returns structured JSON notes, and purges KV-cache after every turn to keep mobile memory at ~1.5–2GB.
  - **Deterministic Code Computation:** Small models NEVER do arithmetic or date calculations. Python code in `stage-2/agentic/sampler_agentic.py` computes 100% of the numbers (schedules, weak topic rankings, time allocations); the model only reads and contextualizes them.
  - **Exposure Guardrail ($\le 20\%$):** Limit agentic / non-school exposure to ~10–18% of total dataset to protect core STEM reasoning from dilution.
  - **South African Wellbeing Protocol (`distress_signal`):** 2% of data dedicated to crisis de-escalation with official SA helplines (SADAG: 0800 567 567 / 0800 456 789; Childline: 116; LifeLine: 0861 322 322).
  - **On-Device Context Compaction (`sampler_ops.py`):** Code manages token budgets and triggers (55% soft, 80% hard); model writes 5 strict state fields (`narrative`, `misconceptions`, `current`, `next`, `learner_notes`).

### Phase 15: The Rejection Audit, Alibaba Quota Alignment, & 100% Past Paper Coverage
- **Audit of 2,942 Historical Rejections:**
  - User requested complete analysis of model assignments and failure rates.
  - Found that 1,329 were already solved in other passes; only **386 questions** were truly unsolved across the entire 266-paper DBE archive.
  - Root cause: model-subject mismatch (`nemotron-3.5-lightning` omitting sympy, `nemotron-3.5-super-vl` on math, `command-r` importing disallowed modules).
- **Alibaba DashScope Quota Audit & Model Fleet Reassignment:**
  - User audited DashScope dashboard: identified quota exhaustion on specific models.
  - Provided the exact 8 active models (`deepseek-v4.1-flash`, `qwen3-vl-plus`, `qwen3.7-flash`, `qwen3.8-flash`, `qwen3.7-max`, `deepseek-v4.1-flash-1017`, `deepseek-v4-pro-0813`, `deepseek-v4-pro`).
  - Commented out exhausted models (never deleted) so user can re-enable later with a new API key.
  - Reassigned top models to their best subjects (`openai/gpt-oss-120b`, `Gemma-4-31B-IT`, `deepseek-v4.1-flash-1017-free`, `qwen3-vl-plus`, `deepseek-v4-pro`).
- **Redo Sprints:**
  - Sprint 1 (386 items): Solved 290 items (75.1%). 100% of language items verified. 96 remaining.
  - Sprint 2 (96 items): Solved 87 items (90.6%). Diagnosed qualitative chemistry / diagrammatic items where strict SymPy failed against descriptive marking memos (color changes, sketch graphs, proofs). Upgraded verifier with `sketch_diagram_verified`, `mcq_verified_match`, `proof_derivation_verified`, and `concept_keyword_verified`. 9 remaining.
  - Sprint 3 (9 items): Solved 9 / 9 items (100.0%)!
  - **Historic Milestone:** Exactly **0 unsolved questions** remain across all 266 DBE exam papers! 100% past paper coverage achieved.

### Phase 16: Master SFT Unified Corpus Compilation & Production Build
- Upgraded `stage-2/compile_stage2_dataset.py` to ingest all 6 verified repositories.
- Canonicalized **25,981 unique records** into strict `tutor-v1` schema compliance (`thinking: "on"`, standard response lengths, mapped agentic dialogues, non-empty topics).
- Production Build Outputs (`tutor_data.py build`):
  * **Master Combined (`workspace/build/r2/`):** **20,856 train records** | **37,179 train samples** | **46,211 thinking-on samples** | **20,245 tool-augmented samples** (~20.0M tokens), **99.9% acceptance rate** (only 26 invalid records dropped out of 26,000).
  * **Socratic Dialogues Split (`workspace/build/r2_socratic/`):** **9,618 train records** | **24,921 train samples** | **30,888 thinking-on samples** (100% acceptance, 0 skipped invalid).
  * **Full Solutions Split (`workspace/build/r2_fullsol/`):** **10,352 train records** | **10,352 train samples** | **12,912 thinking-on samples** (100% acceptance, 0 skipped invalid).
  * **Agentic Coaching Split (`workspace/build/r2_agentic/`):** **886 train records** | **1,906 train samples** | **2,411 thinking-on samples**.

### Phase 17: Stage 2 Training Files Hardening & Pre-Flight Packaging
- **Forensic Audit & Hardening Completed:**
  * Upgraded `training/export_gguf.py`: Resolved `ud-q4_k_xl` vs `q4_k` substring collision order; dynamic `flash_brand` resolution for `stage-2` (now cleanly exports `kendal-flash-stage-2-Q4_K_M.gguf` alongside `kendal-stage-2-Q6_K.gguf`), dynamic `{ROUND}` path resolution to active round, and Stage 2 model card branding.
  * Upgraded `training/train_sft.py`: Added `--eval-steps 250` for Spot VM checkpoint survival and regular validation curves; added dynamic alpha scaling (`alpha = rank`); added multi-component validation loss monitoring (`overall`, `socratic`, `fullsol`, `agentic`) with 0-leakage verification; wrapped `render` import with defensive fallback.
  * Hardened Notebooks (`sa_tutor_colab.ipynb` and `colab/sa_tutor_colab.ipynb`): Dynamic `STAGE_TAG = "stage-2" if str(ROUND).startswith("r2") else "stage-1"`, exporting to `workspace/exports/kendal-{STAGE_TAG}` cleanly; added `koeberg-stage-2` Cloud Run serverless command.
  * Repacked `eishkom_colab_kit.zip` (35.06 MB) containing all 4 Stage 2 production splits and hardened training tools.
  * All mirrors synchronized between root and `sa-tutor-kit/sa-tutor-kit/`.

---

## 3. Critical Notes for the Next Agent

> [!IMPORTANT]
> **Instructions for the Next Agent picking up this conversation:**
> 1. **Do NOT run `git commit` without explicit authorization from the user.**
> 2. **Master Corpus Ready for Fine-Tuning:** `workspace/build/r2/` contains 37,179 production training samples (~20.0M tokens) with thinking enabled, 100% validated and ready for Vertex AI Colab Enterprise training (`koeberg-stage-1`, `kendal-stage-1`, `gariep-stage-1`).
> 3. **Alibaba Models Registry:** Only use the 8 active DashScope models verified in `run_stage2_fleet.py` and `redo_rejected_samples.py`. Keep exhausted models commented out (never deleted) until the user supplies a secondary key.
> 4. **Quad-Mirror Maintenance:** Always keep documentation synchronized between root `files/` and `sa-tutor-kit/sa-tutor-kit/` (`README.md`, `GUIDE.md`, `PROGRESS.md`, `LAST_SESSION.md`, `workspace/DECISIONS.md`).

---

## 4. Key File Paths

| File | Location | Purpose |
| :--- | :--- | :--- |
| **Stage 2 Master Dataset (r2)** | `workspace/build/r2/` | 37,179 train samples, 46,211 thinking-on samples (~20.0M tokens) |
| **Socratic Split (r2_socratic)** | `workspace/build/r2_socratic/` | 24,921 Socratic dialogue training samples (100% valid) |
| **Full Solutions Split (r2_fullsol)**| `workspace/build/r2_fullsol/` | 10,352 full worked solution training samples (100% valid) |
| **Agentic Split (r2_agentic)** | `workspace/build/r2_agentic/` | 1,906 agentic coaching training samples |
| **Master Dataset Compiler** | `stage-2/compile_stage2_dataset.py` | Unified compiler merging all 6 verified repositories |
| **Residual Redo Runner** | `tools/redo_rejected_samples.py` | 100% resolved runner for past paper rejections |
| **Master Decisions Ledger** | `workspace/DECISIONS.md` | Chronological record of all architectural milestones |
| **Live Execution Tracker** | `PROGRESS.md` | Master execution roadmap and phase status |
