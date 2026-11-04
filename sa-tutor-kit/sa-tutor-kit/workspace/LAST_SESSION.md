# Eishkom AI — Session Handoff & Continuity Ledger

> **File Name:** `LAST_SESSION.md`  
> **Last Session Date:** 2026-11-04  
> **Last Active Conversation ID:** `d2778b60-aafe-484e-9103-c5715596acbe`  
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

---

## 2. Exhaustive Timeline of Work Completed

### Phase 0: Setup & Infrastructure Optimization
- Initialized immutable workspace pipeline: `raw/` → `text/` → `items/` → `gen/` → `verified/` → `build/` → `runs/` → `exports/` → `eval/`.
- Configured **Vertex AI Colab Enterprise** on **NVIDIA L4 GPU Spot VMs** (~$0.32/hr) to consume promotional Google Cloud credits ($10/month rolling grants, up to $60 balance) down to $0.00 cash spend.
- Architected **Google Cloud Run** deployment with serverless NVIDIA L4 GPU and `--min-instances 0` ($0.00/hr when idle).
- Configured Git security: `.env` is strictly excluded from Git tracking via `.gitignore`, and `.env.example` is provided for public repo clones.

### Phase 1: Source Data Collection
- Implemented automated crawler `pipeline/download_dbe.py`.
- Downloaded a **sample/test corpus of 600 PDFs (300 pairs, 378.15 MB, 0 errors)** covering Grades 10–12 Mathematics, Physical Sciences, English, and Afrikaans (2015–2025).
- Recorded all sources with paired links (`pair_with`) in `workspace/sources/sources.csv`.
- **Benchmark Quarantine:** Locked 16 Grade 12 November 2024 past papers as held-out evaluation benchmarks (`held out for EVAL`) in `workspace/sources/sources.csv` to ensure zero training data contamination.
- *Note:* This initial batch was a representative sample for designing the workflow; future expansion can download the entire past paper archive from the DBE website.

### Phase 2: Multimodal Document Vision Ingestion & Quality Audit
- Replaced legacy PyMuPDF text stream extraction with direct multimodal vision extraction via **Gemini Vision** (`pipeline/ingest_vision.py`).
- Extracted all 600 documents into **11,310,442 characters of clean KaTeX LaTeX and Markdown**, 354 LaTeX documents, and 1,005 geometric diagram notes.
- Engineered intelligent multi-model rotation pool with persistent daily quota tracking (`.quota_exhausted.json`) and automatic midnight (12:00 AM) resets.
- Handled Google API copyright filters (`finishReason: "RECITATION"`) on question papers by leveraging **Memo-First Question Recovery** from official marking memorandums.
- Built deterministic two-pass automated quality audit (`pipeline/verify_extractions.py`):
  - Audited all 301 pairs: **287 / 301 clean structural passes (95.3%)**, **47,312 KaTeX equations verified**, **1,004 structured diagrams verified**.
- Built deterministic KaTeX syntax sanitizer (`pipeline/sanitize_text.py`):
  - Sanitized 137 documents in 0.5s ($0.00 spend), eliminating empty `$$ $$` blocks and closing unclosed environments.

### Forensic Evaluation & Universal Standard Formulation
- User performed an independent forensic comparison between the raw PDF and extracted text for Physical Sciences Grade 12 Paper 2:
  - **Verified 100% Faithful:** All questions (1.1 to 9.2.3), text wording, data numbers, and mark allocations were completely intact and summed to exactly **150 / 150**.
  - **Vision Extraction Blindspots Identified:**
    1. 2D branching organic chemistry molecules drawn as ASCII/LaTeX matrices (`\begin{matrix}` with `\quad`) lose branches and double bonds.
    2. Vision models describe graphs qualitatively (e.g. "curve decreases") rather than extracting the exact coordinates needed for calculations (e.g. at $t=10\text{ s}, [\text{O}_2]=0,15\text{ mol}\cdot\text{dm}^{-3}$).
    3. LaTeX syntax errors like `\text{^\circ C}` (invalid KaTeX superscript nesting).
- **Decisions Taken:**
  1. **Do NOT hand-edit 600 raw intermediate text files.** `workspace/text/` is a raw staging folder. In Phase 2.5 (`extract_items.py`), the model reads the Question Paper and Marking Memorandum simultaneously; the memorandum provides authoritative ground truth (exact calculation numbers, method marks, IUPAC names).
  2. **Codified the Universal Document & Visual Extraction Standard (UDVES):**
     - Master specification saved in `workspace/config/UNIVERSAL_EXTRACTION_STANDARD.md`.
     - Embedded directly into `pipeline/ingest_vision.py`.
     - Covers **all subjects**: EGD (1st/3rd angle orthographic, isometric, section A-A, PCD, threads), Civil Tech (floor plans, plumbing, electrical), Electrical Tech (schematics, logic gates, waveforms), Mechanical Tech (gears, cams, hydraulics), Mathematics (Euclidean geometry, functions, asymptotes, box-and-whisker), Sciences (rate curves, IUPAC condensed chemical formulas), Languages (cartoons frame-by-frame, adverts, infographics), Commercials (accounting balance sheets with blanks, economics curves), Geography (topo maps, synoptic weather charts), History, IT, and CAT.

---

## 3. Strict Operational Rules (Must Be Followed in Every Chat)

1. **NEVER COMMIT WITHOUT ASKING:**
   - **Do not run `git commit` under any circumstances unless the user explicitly commands it.** Keep changes unstaged or staged in the working tree for user review.
2. **DOCUMENTATION MAINTENANCE MANDATE:**
   - Whenever an important milestone, decision, or verified procedure occurs, immediately record it in `workspace/DECISIONS.md`, `GUIDE.md`, `README.md`, and `PROGRESS.md`.
   - Keep root files and `sa-tutor-kit/sa-tutor-kit/` mirrors synchronized.
3. **NEVER TRAIN ON GGUF FILES:**
   - Base Hugging Face repositories only (`unsloth/Qwen3.8-27B`, `unsloth/Qwen3.5-4B`, `empero-ai/Qwen3.8-4B-Distill`, `LiquidAI/LFM3-VL-2B`). Export to GGUF at the end.
4. **BENCHMARK INTEGRITY:**
   - November 2024 Grade 12 NSC papers must remain 100% quarantined in `workspace/eval/` and NEVER enter training sets.

---

## 4. Current State & What is Left to Do

### What is Completed:
- [x] Phase 0: Workspace, tooling, Spot VM & Cloud Run configs, Git security.
- [x] Phase 1: 600 PDFs downloaded, paired, and cataloged.
- [x] Phase 2: 11.3M characters extracted via Gemini Vision, two-pass audit executed, KaTeX sanitized.
- [x] Universal Extraction Standard (UDVES) codified across all curriculum subjects.

### What is Left to Do (Immediate Next Steps):
- [ ] **Phase 2.5: Item Extraction (`pipeline/extract_items.py`):**
  - Slice the extracted text into atomic question + memo items in `workspace/items/<source_id>.jsonl`.
  - Reconcile chemistry structures and graph calculation coordinates using paired DBE memorandums.
  - Flag complex visual figures with `"needs_review": true`.
- [ ] **Phase 3: Held-Out Benchmark Quarantine Lock (`eval/make_eval_from_items.py`):**
  - Compile the 16 held-out November 2024 Grade 12 exam papers into `workspace/eval/eval_items.jsonl`.
  - Run baseline teacher model evaluation to set the benchmark score.
- [ ] **Phase 4: Teacher Dialogue Generation (`pipeline/generate_dialogues.py`):**
  - Generate multi-turn Socratic tutoring dialogues with hint ladders in `workspace/gen/r1/`.
- [ ] **Phase 5: SymPy Arithmetic & Rubric Verification (`pipeline/verify.py`):**
  - Verify math steps against DBE marking guidelines and SymPy to filter hallucinations into `workspace/verified/r1/`.
- [ ] **Phase 6: Human Review Sample (40 records):**
  - Audit tone, bilingual quality (English/Afrikaans), and pedagogical fidelity.
- [ ] **Phase 7–12: Dataset Build, Cross-Tier Distillation, SFT Training, GGUF Export, and Cloud Run Deployment.**

---

## 5. Master Context Files to Read for Complete Understanding

When a new assistant opens this workspace, they must read these files in order:
1. `workspace/LAST_SESSION.md` (this file — continuity handoff)
2. `workspace/DECISIONS.md` (all 14 architectural decisions and rationale)
3. `workspace/config/UNIVERSAL_EXTRACTION_STANDARD.md` (the universal visual extraction standard)
4. `stage-1/PROGRESS.md` (phase checklist and execution status)
5. `GUIDE.md` (developer execution manual)
6. `stage-1/MODELS.md` (model hardware tiers, quantization, and distillation plan)

