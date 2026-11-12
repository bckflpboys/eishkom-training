# Eishkom AI — Session Handoff & Continuity Ledger

> **File Name:** `LAST_SESSION.md`  
> **Last Session Date:** 2026-11-12  
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

## 2. Exhaustive Timeline of Decisions & Architectural Breakthroughs (Nov 10–12, 2026)

### 1. Training Runs & Multi-Quant Exports Verified:
- **Kendal Stage 1 (4B):** Completed 3 epochs (870 steps, loss down to 0.34). Exported `kendal-stage-1-Q6_K.gguf` (3.4 GB), `kendal-flash-stage-1-Q4_K_M.gguf` (2.65 GB), and pure `Q4_K`.
- **Gariep Stage 1 (2B):** Completed 3 epochs across 5,755 SFT samples. Exported all 4 mandated formats: `Q8_0` (high reasoning), `Q6_K` (budget PC), pure `Q4_K` (pure-K benchmarking), and `Q4_K_M` (mobile phone ~1.3 GB).
- Both runs packaged into clean `.zip` archives with automated cloud storage synchronization (`gs://${PROJECT}-models`).

### 2. Multi-Model Single-GPU Training Pipeline (Colab Queueing):
- Clarified that running multiple training processes concurrently on a single GPU triggers memory fragmentation, CUDA OOM, and Triton compiler deadlocks.
- Designed an automated sequential chaining pipeline that runs 1B, 2B, and 4B back-to-back in a single Colab runtime session, automatically releasing 100% of VRAM between models.

### 3. Native Application Architecture: Transient Chunked Page-Worker Pattern (Map-Reduce):
- **The Problem:** Ingesting multi-page exams (5–15 pages) directly into a local 2B or 4B Vision-Language Model triggers severe **KV-Cache explosion** (~1,000+ visual tokens per page = 10,000+ tokens), which leads to immediate CUDA Out-Of-Memory (OOM) or extreme token-generation throttling on 4GB RAM phones and budget laptops.
- **The Solution:**
  1. **Application Layer (Orchestrator):** Renders input PDFs or camera photos into individual 300 DPI PNG page screenshots. Dispatches one page at a time to a transient Vision Worker. Stitches transcripts together and resolves cross-page question continuity.
  2. **Transient Vision Worker (`gariep-flash-stage-1`):** Specializes in **pure high-fidelity digitization and transcription** (not problem-solving or tutoring). Focuses 100% of its visual attention on one page, transcribing printed text, student handwriting, KaTeX formulas, and diagram annotations (`[DIAGRAM: ...]`).
  3. **Zero-Retention Memory Purge:** Immediately after each page, the vision worker's KV-cache and VRAM are purged (`torch.cuda.empty_cache()` / context termination), keeping client VRAM usage flat (~1.5–2GB) regardless of document length.
  4. **Central Tutor Agent (`kendal-stage-1` 4B / `gariep-stage-1` 2B):** Conducts Socratic tutoring dialogues exclusively on the clean aggregated text. Runs 10x faster with zero vision overhead and minimal battery drain.

### 4. Vision Model Training Protocol:
- **Synthetic Ground-Truth Pipeline:** High-capacity teacher models (Gemini Flash Multimodal Vision) generate structured KaTeX/markdown transcripts from past exam pages and student handwritten homework.
- **Verification:** Transcripts are reconciled against official DBE marking memorandums for mathematical and rubric accuracy.
- **Handwritten Sample Collection:** 200–500 photographed student homework solutions on lined paper in varied lighting conditions and phone camera angles to train the vision model on real-world classroom pencil work.
- **Dataset Schema:** Vision multi-turn JSONL formatted with `[{"type": "image", "image": "..."}, {"type": "text", "text": "..."}]`.
- **Fine-Tuning:** Trained using Unsloth `FastVisionModel` with 4-bit QLoRA and exported to GGUF + `mmproj-*.gguf`.

### 5. Custom Architecture Branding Strategy:
- **Execution vs Branding Separation:** In local GGUF binaries, standard execution kernels (`general.architecture = "qwen2"`) are retained to preserve native C++/CUDA hardware acceleration in llama.cpp, Ollama, and LM Studio.
- **Hugging Face Custom Architecture:** Custom `model_type: "eishkom"` registered with `configuration_eishkom.py` and `modeling_eishkom.py` (`trust_remote_code=True`).
- **Client App UI Insulation:** The custom desktop/mobile app encapsulates all technical kernel details, exposing unified Eishkom AI brand identity.

---

## 3. Critical Notes for the Next Agent

> [!IMPORTANT]
> **Instructions for the Next Agent picking up this conversation:**
> 1. **Do NOT run `git commit` without explicit authorization from the user.**
> 2. **Current Completed Models:**
>    - `kendal-stage-1` (4B) & `kendal-flash-stage-1` (4B) — Completed & exported (Q6_K, Q4_K_M, pure Q4_K).
>    - `gariep-stage-1` (2B) — Completed & exported (Q8_0, Q6_K, pure Q4_K, Q4_K_M).
> 3. **Next Target:** Prepare the vision dataset and fine-tune `gariep-flash-stage-1` (2B Vision/OCR) using Unsloth `FastVisionModel` for the Transient Page-Worker pipeline.
> 4. **Application Pipeline Architecture:** The application must decouple page digitization (transient vision worker) from Socratic tutoring (central text model).
> 5. **Quad-Mirror Maintenance:** Keep all documentation in sync between root `files/` and `sa-tutor-kit/sa-tutor-kit/`.

---

## 4. Key File Paths

| File | Location | Purpose |
| :--- | :--- | :--- |
| **Colab TPU v5e Notebook** | `sa_tutor_colab_tpu_v5e.ipynb` | Specialized notebook for Cloud TPU v5e-1 (16GB HBM) |
| **Colab Research Notebook** | `sa_tutor_colab_research.ipynb` | Specialized notebook for T4 GPU in `colab.research.google.com` |
| **Colab Research Kit** | `gariep_colab_research_kit.zip` | Standalone 1.57 MB zip with dataset and training code for Gariep 2B |
| **Enterprise Colab Notebook** | `sa_tutor_colab.ipynb` | Vertex AI Colab Enterprise runner for L4 GPU Spot VM |
| **Enterprise Colab Kit** | `eishkom_colab_kit.zip` | Master 1.57 MB zip for Vertex AI Colab Enterprise |
| **Training Engine** | `sa-tutor-kit/sa-tutor-kit/training/train_sft.py` | SFT trainer with CUDA and TPU v5e auto-scaler and clean console logging |
| **GGUF Multi-Quant Exporter** | `sa-tutor-kit/sa-tutor-kit/training/export_gguf.py` | Exports Q8_0, Q6_K, pure Q4_K, and Q4_K_M from trained adapter |
| **Master Dataset (r1)** | `workspace/build/r1/` | 5,755 SFT samples (`train.jsonl`, `val.jsonl`, `test.jsonl`) |
| **Master Decisions Ledger** | `workspace/DECISIONS.md` | Chronological record of all project architectural decisions |
