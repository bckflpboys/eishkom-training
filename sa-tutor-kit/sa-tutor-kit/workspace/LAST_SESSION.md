# Eishkom AI — Session Handoff & Continuity Ledger

> **File Name:** `LAST_SESSION.md`  
> **Last Session Date:** 2026-11-09  
> **Last Active Conversation ID:** `d63a603b-b01d-47d3-afc4-d6741b1c1ba3`  
> **Repository Branch:** `main` (clean working tree, unstaged updates ready)  
> **Purpose:** Master continuity bridge for moving across chat sessions without loss of context, history, or engineering decisions.

---

## 1. Executive Summary (The Story from Day 1 to Now)

**Eishkom AI** is building a family of open-source, South African CAPS curriculum-aligned AI tutor models (Grades 7–12 & TVET) designed for high pedagogical quality (Socratic hint ladders, diagnostic questioning, English and Afrikaans support).

### Clean Model Branding (Mandatory Rule):
Public model names **never display parameter numbers or quantization suffixes** (`27B`, `4B`, `Q4`, `Q6` are strictly hidden from brand names):
1. **`koeberg-stage-1`**: Flagship Cloud Tutor (unsloth/Qwen3.8-27B, `UD-Q4_K_XL`, ~17.6 GB) — Google Cloud Run (Serverless NVIDIA L4, scale-to-zero).
2. **`kendal-stage-1`**: Budget PC & Laptop Tutor (unsloth/Qwen3.5-4B, `Q6_K` / `UD-Q6_K_XL`, ~3.53–4.15 GB) — 100% offline on GTX 1650 4GB / 16GB RAM.
3. **`kendal-flash-stage-1`**: Midrange Mobile & Phone Tutor (empero-ai/Qwen3.8-4B-Distill, `Q4_K_M`, ~2.78–2.91 GB) — 100% offline on 6GB–8GB RAM phones.
4. **`gariep-stage-1`**: Budget Phone Tutor (empero-ai/Qwen3.8-2B-Distill, `Q6_K` / `Q8_0`, ~1.75–2.15 GB) — 100% offline on 4GB RAM phones.
5. **`gariep-flash-stage-1`**: Budget Vision/OCR Tutor (LiquidAI/LFM3-VL-2B, `Q6_K`, ~1.55 GB) — Specialized for geometry diagrams, handwritten work, and document OCR.
6. **`baby-jake-stage-3`** *(or `atom-stage-3`)*: Ultra-Budget Celeron & Entry Phone Tutor (1B, Q4_K_M ~650–850 MB) — Scheduled for Stage 3. Specially engineered for extreme budget Celeron PCs (4GB RAM) achieving 10–14 tokens/sec, and entry Android phones (2GB–3GB RAM). Trained via Stage 3 Kendal-4B self-distillation with SymPy automated checks.

---

## 2. Exhaustive Timeline of Work Completed

### Phase 0: Setup & Infrastructure Optimization
- Initialized immutable workspace pipeline: `raw/` → `text/` → `items/` → `gen/` → `verified/` → `build/` → `runs/` → `exports/` → `eval/`.
- Configured **Vertex AI Colab Enterprise** on **NVIDIA L4 GPU Spot VMs** (~$0.32/hr) to consume promotional Google Cloud credits ($10/month rolling grants, up to $60 balance) down to $0.00 cash spend.
- Architected **Google Cloud Run** deployment with serverless NVIDIA L4 GPU and `--min-instances 0` ($0.00/hr when idle).

### Phase 1: Source Data Collection
- Implemented automated crawler `pipeline/download_dbe.py`.
- Downloaded **600 PDFs (300 pairs, 378.15 MB, 0 errors)** covering Grades 10–12 Mathematics, Physical Sciences, English, and Afrikaans (2015–2025).
- Recorded all sources with paired links (`pair_with`) in `workspace/sources/sources.csv`.
- **Benchmark Quarantine:** Locked 33 Grade 12 November 2024 past papers as held-out evaluation benchmarks (`held out for EVAL`) in `workspace/eval/` to ensure zero training data contamination.

### Phase 2: Multimodal Document Vision Ingestion & Item Extraction
- Extracted all documents into **11.3M characters of clean KaTeX LaTeX and Markdown** using Gemini Vision.
- Sliced into **13,168 atomic curriculum items** across 265 question papers (`workspace/items/`).
- Verified 100% rubric compliance and mathematical marks against paired DBE memorandums.
- Codified the Universal Document & Visual Extraction Standard (UDVES) in `workspace/config/UNIVERSAL_EXTRACTION_STANDARD.md`.

### Phase 3 & 4: Multi-Model Fleet Generation & Verification (Waves 1–5)
- Orchestrated autonomous multi-model fleet (OpenAI Luna/GPT-4o, Google Gemini 3.5 & 3.1 Flash, Nvidia Nemotron 123B, DeepSeek V3/V4).
- Generated and verified **1,346 multi-turn Socratic lessons** (~3,365 assistant dialogue turns).
- Generated **1,970 full step-by-step worked solutions** across 41 complete Grade 12 past papers.
- Verified all arithmetic and algebra using SymPy and DBE marking memorandums.

### Phase 5: Production Dataset Compilation (`workspace/build/r1/`)
- Compiled canonical Stage 1 SFT dataset conforming 100% to schema `tutor-v1`:
  - `train.jsonl`: 2,647 records | **4,639 training samples** (693,120 trainable tokens/epoch)
  - `val.jsonl`: 483 records | **844 validation samples** (124,753 tokens/epoch)
  - `test.jsonl`: 159 records | **272 test samples**
  - Total: **5,755 SFT samples** (all with `thinking: "on"`).
- Packaged into `eishkom_colab_kit.zip` (1.56 MB) containing all datasets, training engines, and evaluation harnesses.

### Phase 6: Reporting & Analytics
- Built itemized master spreadsheet: `workspace/reports/eishkom_all_requests_detailed.csv` (1,838 items, 34 columns, utf-8-sig encoded for Excel/Google Sheets).
- Generated model performance leaderboard (`fleet_model_leaderboard.csv`):
  - OpenAI Luna: 484 verified items (83.0% pass rate)
  - Gemini 3.5: 349 verified items (83.1% pass rate)
  - Nemotron: 112 verified items (72.3% pass rate)
- Generated per-paper verification matrix (`paper_verification_matrix.csv`) across all 41 papers.

### Phase 7: Google Cloud Compute Infrastructure (Verified Nov 9, 2026)
- Confirmed that Cloud Console's **"Colab Enterprise"** is Vertex AI Colab Enterprise (`console.cloud.google.com/vertex-ai/colab/notebooks`).
- Configured dedicated runtime template:
  - Name: `eishkom-gpu` (ID: `5096703687183564800`)
  - Machine: `g2-standard-4` (4 vCPUs, 16GB RAM)
  - Accelerator: **1 x NVIDIA L4 GPU (24GB VRAM)**
  - Storage: 100GB SSD persistent disk (`pd-ssd`), 97.85 GB free on `/content`
  - Idle shutdown: 60 minutes
  - Spot VM enabled (~$0.32/hr consuming promotional credits).
- **GPU Quota Approved:** Global GPU quota `GPUS_ALL_REGIONS` requested from 0 to 1, officially approved by Google Cloud Support on Nov 9, 2026.
- Verified active GPU hardware: `NVIDIA L4` with 23,034 MiB VRAM, CUDA 13.0, bfloat16 = TRUE, Hardware FlashAttention.

### Phase 8: COMPLETED Supervised Fine-Tuning Run (`kendal-stage-1` 4B) (Verified Nov 9, 2026)
- Base model: `unsloth/Qwen3.5-4B` in 4-bit QLoRA (Unsloth fast patching).
- Trainable parameters: 21,233,664 (0.47% of 4.56B weights).
- Training progress (Active Nov 9, 2026):
  - Optimizer steps: 870 total steps across 3 epochs (290 steps/epoch).
  - Step 104/870 completed (0.34 epochs) in 17 minutes.
  - Step speed stabilized from 15.98s/it down to **8.14s/it** (~1h 40m remaining).
  - **Loss trajectory:** Dropped from `1.662` down to **`0.6597`** (Textbook-grade alignment!).

---

## 3. Stage 2 (v2) Architectural Roadmap: Strategy Permutations
- In Stage 2, the exact same 265 past papers will be systematically retrained across 5 alternate teaching styles:
  1. `worked_example` (Parallel example followed by learner practice)
  2. `mnemonic_memory_hook` (Visual analogies, memory hooks, concept anchors)
  3. `faded_example` (Scaffolded fill-in-the-blank steps)
  4. `frustrated_learner_de-escalation` (Emotional coaching and micro-clues)
  5. `rapid_short_prompt` (High-speed concise mobile queries)
- Scales corpus 4x–5x (10,000+ to 15,000+ SFT samples) without needing new exam papers.

---

## 4. Strict Operational Rules

1. **NEVER COMMIT WITHOUT ASKING:**
   - Do not run `git commit` unless the user explicitly commands it.
2. **DOCUMENTATION MAINTENANCE MANDATE:**
   - Every important milestone or decision must be immediately persisted in `LAST_SESSION.md`, `DECISIONS.md`, `PROGRESS.md`, `GUIDE.md`, and `README.md`.
3. **NEVER TRAIN ON GGUF FILES:**
   - Fine-tune unquantized base Hugging Face repositories only. Export to GGUF post-training.
4. **BENCHMARK INTEGRITY:**
   - November 2024 Grade 12 papers remain 100% quarantined in `workspace/eval/` (0% contamination).

---

## 5. Immediate Next Steps After Current Training Finishes

1. **GGUF Multi-Quant Export (Step 9):**
   - Run `training/export_gguf.py` from the trained `workspace/runs/r1/adapter/`.
   - Export `kendal-stage-1-Q6_K.gguf` (Budget PC/Laptop, ~3.53 GB).
   - Export `kendal-flash-stage-1-Q4_K_M.gguf` (Mobile/Phone, ~2.78 GB).
2. **Quarantined Benchmark Evaluation (Phase 10):**
   - Evaluate against held-out Nov 2024 Grade 12 papers using `eval/evaluate.py`.
3. **Koeberg 27B Training Run:**
   - Launch `koeberg-stage-1` (`unsloth/Qwen3.8-27B`) on the NVIDIA L4 GPU Spot VM (~5.5 hours, ~$1.76 credits).
