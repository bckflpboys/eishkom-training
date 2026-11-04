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
# PHASE 2: INGESTION (PDF -> TEXT)
# ==============================================================================
python pipeline/ingest.py

# ==============================================================================
# PHASE 2.5: ITEM EXTRACTION (QUESTIONS & MEMOS)
# ==============================================================================
python pipeline/extract_items.py

# ==============================================================================
# PHASE 3: HELD-OUT EVALUATION BENCHMARK
# ==============================================================================
python pipeline/build_eval.py --year 2024 --session nov --grade 12

# ==============================================================================
# PHASE 4: TEACHER GENERATION (ROUND 1)
# ==============================================================================
python pipeline/generate_dialogues.py --round 1 --max-items 5000

# ==============================================================================
# PHASE 5: AUTOMATED VERIFICATION & SYMPY ARITHMETIC CHECKING
# ==============================================================================
python pipeline/verify.py --in workspace/gen/r1/ --out workspace/verified/r1/

# ==============================================================================
# PHASE 6: HUMAN AUDIT (40 RECORD SAMPLE)
# ==============================================================================
python pipeline/human_review.py --in workspace/verified/r1/ --sample 40

# ==============================================================================
# PHASE 7: DATASET PACKAGING
# ==============================================================================
python pipeline/build_train.py --in workspace/verified/r1/ --out workspace/build/r1/

# ==============================================================================
# PHASE 8: CROSS-TIER DISTILLATION
# ==============================================================================
python pipeline/distill_hard_items.py --teacher koeberg-stage-1 --out workspace/gen/r2/

# ==============================================================================
# PHASE 9 & 10: VERTEX AI COLAB ENTERPRISE SFT & GGUF EXPORT
# (Execute inside colab/sa_tutor_colab.ipynb on NVIDIA L4 Spot VM)
# ==============================================================================
# koeberg-stage-1 (27B) -> koeberg-stage-1-UD-Q4_K_XL.gguf
# kendal-stage-1 (4B)   -> kendal-stage-1-Q6_K.gguf & kendal-flash-stage-1-Q4_K_M.gguf
# gariep-stage-1 (2B)   -> gariep-stage-1-Q6_K.gguf

# ==============================================================================
# PHASE 12: DEPLOY KOEBERG-STAGE-1 TO GOOGLE CLOUD RUN (SCALE-TO-ZERO)
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

### Step 2: Multimodal Document Vision Extraction (Completed & Audited)
- Run `python pipeline/ingest_vision.py --pipeline-order`.
- Ingested all 600 exam documents into `workspace/text/` (**11,310,442 characters**, 354 KaTeX LaTeX documents, 1,005 geometric diagram descriptions, 0 failures).
- Uses Gemini Multimodal Vision with automated multi-model pool failover (`gemini-3.1-flash-lite`, `gemini-3.8-flash`, `gemini-3-flash-preview`).
- Daily quota tracking persisted in `.quota_exhausted.json` with automatic midnight (12:00 AM) reset.
- Forensic audit manifest generated at `workspace/text/manifest.jsonl`.
- Two-Pass quality verification architecture: Gemini 3.1 Flash Lite (visual layout) + Gemma 4 (curriculum memo cross-referencing).

### Step 3: Segment into Structured Question-and-Answer Items
- Run `python pipeline/extract_items.py --source <source_id>`.
- Dry-run estimate test: `python pipeline/extract_items.py --source <source_id> --dry-run`.
- **Mathematical Equations:** Standardized into LaTeX inside `$..$` (inline) or `$$..$$` (display block).
- **Text-Describable Diagrams (~20%):** Geometry circles, triangles, circuits, coordinate graphs have their spatial relations written in the `"passage"` field so pure text models can reason about them.
- **Pure Visual Figures (~10%):** Flagged `"needs_review": true`, excluded from text SFT, rendered to `workspace/images/` for multimodal training on `LiquidAI/LFM3-VL-2B` (`gariep-flash-stage-1`).
- **Memo-First Question Recovery:** For Mathematics question papers with rasterized formulas, question wording and step criteria are extracted directly from the paired DBE memorandum.
- Stores items in `workspace/items/<source_id>.jsonl`.

### Step 4: Reserve the 2024 Benchmark
- The November 2024 Grade 12 items are compiled into `workspace/eval/eval_items.jsonl`.
- These items are never exposed during training.

### Step 5: Distill Socratic Dialogues
- Using DeepSeek V4.1 Flash (MIT License) or Vertex AI Gemini Flash, generate multi-turn tutoring interactions.
- Socratic rules:
  - Do not give the answer away immediately.
  - Diagnose the student's misconception first.
  - Present a hint ladder (subtle hint → medium hint → full breakdown).
  - Ask one question at a time and wait for learner response.

### Step 6: Verify and Filter
- Run `pipeline/verify.py`.
- Rejects any generated dialogue where the mathematical calculation disagrees with SymPy or the official DBE memo answer.

### Step 7: SFT Training in Vertex AI Colab Enterprise
- Open `colab/sa_tutor_colab.ipynb` inside Google Cloud Console.
- Choose **NVIDIA L4 GPU (24GB VRAM)** with **Spot VM** enabled (~$0.32/hr).
- Training saves checkpoints after each epoch to Google Drive.
- Export GGUF binaries at the end of the run.

### Step 8: Deploy Koeberg to Cloud Run
- Deploy `koeberg-stage-1` containerized to Google Cloud Run with scale-to-zero.
- Idle cost: $0.00/hour.
- Active cost: ~$0.015/minute.

