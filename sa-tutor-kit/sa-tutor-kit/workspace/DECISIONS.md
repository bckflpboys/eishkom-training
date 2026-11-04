# Eishkom Stage 1 — Architectural & Model Decisions

**Date:** November 2026  
**Project:** Eishkom AI — South African CAPS Tutor Family  
**Release Cycle:** Stage 1 (`koeberg-stage-1`, `kendal-stage-1`, `kendal-flash-stage-1`, `gariep-stage-1`, `gariep-flash-stage-1`)  
**Stage 1 Hub:** [`../stage-1/`](../stage-1/) | **Live Tracker:** [`../PROGRESS.md`](../PROGRESS.md)

---

## 1. Finalized Model Lineup & Target Deployments

| Public Release Name | Internal Tier | Trainable Base Repo (Hugging Face) | GGUF Reference / Export Quant | Final File Size | Target Hardware & Deployment |
|---|---|---|---|---|---|
| **`koeberg-stage-1`** | Flagship Cloud (27B) | `unsloth/Qwen3.8-27B` | `UD-Q4_K_XL` (`unsloth/Qwen3.8-27B-GGUF`) | ~17.6 GB | **Cloud:** Google Cloud Run (Serverless NVIDIA L4 24GB, scale-to-zero)<br>**Local:** 16GB/20GB RAM PCs (CPU offload) |
| **`kendal-stage-1`** | Budget PC & Laptop (4B Q6) | `unsloth/Qwen3.5-4B` | `Q6_K` or `UD-Q6_K_XL` (`unsloth/Qwen3.5-4B-GGUF`) | ~3.53–4.15 GB | **Local:** GTX 1650 (4GB VRAM) desktops & 16GB/20GB RAM laptops (100% offline) |
| **`kendal-flash-stage-1`** | Mobile & Phone (4B Q4) | `empero-ai/Qwen3.8-4B-Distill` *(or unsloth 4B)* | `Q4_K_M` (`empero-ai/Qwen3.8-4B-Distill-GGUF`) | ~2.78–2.91 GB | **Local:** Midrange smartphones (6GB–8GB RAM) & 4GB PCs (100% offline) |
| **`gariep-stage-1`** | Budget Phone Tutor (2B Q6) | `empero-ai/Qwen3.8-2B-Distill` *(or unsloth 2B)* | `Q6_K` or `Q8_0` (`empero-ai/Qwen3.8-2B-Distill-GGUF`) | ~1.75–2.15 GB | **Local:** Budget smartphones (4GB RAM) & low-spec PCs (100% offline) |
| **`gariep-flash-stage-1`** | Budget Vision/OCR (2B LiquidAI) | `LiquidAI/LFM3-VL-2B` | `Q6_K` (`LiquidAI/LFM3-VL-2B-GGUF`) | ~1.55 GB | **Local:** Budget phones for high-speed document, diagram, and OCR reading |

---

## 2. Brand Identity & Release Naming Rules
- **Stage-Based Versioning:** We release as `stage-1`, `stage-1.1`, `stage-2` rather than arbitrary version increments.
- **Clean Branding:** Public model names **never** expose parameter counts or quantization suffixes. The public sees `koeberg-stage-1` (not `koeberg-27b-q4`), preserving an enterprise-grade, clean user experience.

---

## 3. Training & Compute Infrastructure
- **Google Cloud & Gen AI Credits:** Leveraging **\$60 in promotional Google Cloud billing credits** ($10/month rolling grants).
- **Vertex AI Colab Enterprise:** Training on **NVIDIA L4 GPUs (24GB VRAM)** using **Spot VM instances** (~$0.32/hr) to avoid browser disconnects and enable 27B model fine-tuning.
- **GPU Quota:** NVIDIA L4 GPU quota increased to 1 in `IAM & Admin > Quotas`.
- **Cloud Run Hosting (Scale-to-Zero):** For `koeberg-stage-1`, deploy containerized Ollama/vLLM on Google Cloud Run with an NVIDIA L4 GPU. Configured with `--min-instances 0` so it scales down to \$0.00/hr when idle, only drawing credit during active chat queries (~$0.015/min).

---

## 4. Base Models vs. GGUF Files
- **Rule:** Never pass a compiled `-GGUF` repository to `train_sft.py`.
- **Action:** Fine-tune unquantized Transformers base repos using Unsloth QLoRA (4-bit base weights + 16-bit LoRA adapters).
- **Multi-Quant Export:** Compile to `.gguf` at the end using `training/export_gguf.py`. Export both `kendal-stage-1` (Q6) and `kendal-flash-stage-1` (Q4) from a single 4B training run.

---

## 5. Cross-Tier Knowledge Distillation
- Train `koeberg-stage-1` (27B) first on the core South African CAPS dataset.
- Use Koeberg to solve 2,000–5,000 of the hardest DBE exam questions (Grade 11–12 Mathematics Paper 2, Physical Sciences, and Afrikaans grammar).
- Verify Koeberg's answers against the DBE memorandums and add them into `dataset.jsonl` to train Kendal (4B) and Gariep (2B).

---

## 6. Pedagogical Defaults & Policies
- **Thinking Default:** Enabled for Mathematics and Physical Sciences; disabled by default on phone profiles for fast turnaround.
- **Maths Notation:** LaTeX rendered via KaTeX in the user app.
- **Decimal Convention:** Decimal point (2.5) for internal consistency and tool communication; accepts decimal comma (2,5) from South African learners.
- **Teacher API:** DeepSeek V4.1 Flash 1017 (MIT License, legally safe for distillation) and Google Gemini Flash via Vertex AI.

---

## 7. Data Collection & Raw Storage Hierarchy (Phase 1)
- **Status:** **COMPLETED & VERIFIED (Nov 2026)**
- **Source Authority:** Department of Basic Education (DBE) past exam papers & official marking memorandums (`education.gov.za`).
- **Crawler Tool:** `pipeline/download_dbe.py` with automated table extraction, URL decoding, and paper-memo pairing.
- **Downloaded Corpus:**
  - **Total Files:** 600 PDFs (300 verified question paper + memorandum pairs).
  - **Total Disk Volume:** 378.15 MB.
  - **English PDFs:** 304 files (`mathematics`: 92, `physical_sciences`: 92, `english_hl`: 60, `english_fal`: 60).
  - **Afrikaans PDFs:** 296 files (`wiskunde`: 88, `fisiese_wetenskappe`: 88, `afrikaans_hl`: 60, `afrikaans_fal`: 60).
  - **Download Success Rate:** 100% (300/300 pairs succeeded, 0 failed).
- **Directory Structure:**
  - `workspace/raw/dbe/english/<subject>/<year>/`
  - `workspace/raw/dbe/afrikaans/<subject>/<year>/`
- **Subjects Collected:**
  - Mathematics (`mathematics` in English, `wiskunde` in Afrikaans, P1 & P2, 2015–2025)
  - Physical Sciences (`physical_sciences` in English, `fisiese_wetenskappe` in Afrikaans, P1 & P2, 2015–2025)
  - English (`english_hl`, `english_fal`, P1 & P2, 2018–2025)
  - Afrikaans (`afrikaans_hl`, `afrikaans_fal`, P1 & P2, 2018–2025)
  - Grade 10 & 11 Common Papers (2015–2018)
- **Held-out Benchmark:** Grade 12 NSC November 2024 is strictly reserved as `held out for EVAL (do not train on it)` (16 papers flagged in `sources.csv`).
- **Sources Ledger:** All documents logged in `workspace/sources/sources.csv` (604 total rows) with paper-to-memo pairing via `pair_with`.

---

## 8. Phase 2 Ingestion Audit & Diagram/Equation Strategy

### Ingestion Audit Results (Nov 2026):
- **Total Ingested Files:** 600 text files generated in `workspace/text/` from 600 downloaded PDFs.
- **Multimodal Vision Upgrade:** Replaced naive `pypdf` stream dump with **Gemini Vision Direct Ingestion** (`pipeline/ingest_vision.py` using `gemini-3.5-flash`).
- **Fixed Failures:**
  1. **Scanned Image PDFs (e.g. May 2021 Maths P1):** Read visual pixels directly via Gemini Vision, extracting 8,942 characters of complete questions and formulas from a document that yielded 0 chars with pypdf.
  2. **MathType Formulas:** Reconstructed 100% of scrambled equations ($x^2 - 2x - 24 = 0$, $2\sqrt{x+6} + 2 = x$, simultaneous equations, cubic functions) into valid KaTeX LaTeX ($...$ inline, $$...$$ display block).
  3. **Multi-Column Alignment:** Repaired 2-column instruction tables and question numbering.
  4. **Font/Bullet De-corrupting:** Converted Wingdings/Symbol font codes (\uf06c, \uf0b7) to clean Markdown bullets.
  5. **Diagram Descriptions:** Encoded geometry and function plots (e.g. parabola/line intersections, semicircles, Venn diagrams) as structured [DIAGRAM: ...] text for language model comprehension.
- **DOCX Auto-Routing:** Magic byte sniffing (`PK\x03\x04`) successfully detected and routed 4 DOCX papers misnamed as `.pdf` (May 2019 Mathematics P1/P2 and Wiskunde V1/V2) to `read_docx()`.
- **Character Breakdown by Subject:**
  - `afrikaans_fal`: 60 files | 2,721,785 chars (QP: 1,417,087 \| Memo: 1,304,698)
  - `afrikaans_hl`: 60 files | 2,981,171 chars (QP: 988,146 \| Memo: 1,993,025)
  - `english_fal`: 60 files | 1,678,608 chars (QP: 883,666 \| Memo: 794,942)
  - `english_hl`: 60 files | 2,040,510 chars (QP: 834,647 \| Memo: 1,205,863)
  - `fisiese_wetenskappe`: 88 files | 1,998,472 chars (QP: 830,274 \| Memo: 1,168,198)
  - `physical_sciences`: 92 files | 2,101,014 chars (QP: 865,659 \| Memo: 1,235,355)
  - `mathematics`: 92 files | 737,870 chars (QP: 25,206 \| Memo: 712,664)
  - `wiskunde`: 88 files | 699,921 chars (QP: 25,051 \| Memo: 674,870)

### Diagram, Picture & Mathematical Equation Strategy:
1. **Mathematical & Scientific Equations:**
   - Standardized into KaTeX-compliant LaTeX syntax: `$..$` for inline math, `$$..$$` for display equations.
   - Preserves DBE formula sheet notations ($v_f^2 = v_i^2 + 2a\Delta x$, $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$, etc.).
2. **Text-Describable Diagrams & Geometry (~20% of questions):**
   - For Euclidean geometry circles, coordinate graphs, electric circuits, and motion diagrams where relations are clearly structured:
   - Encoded directly into the `"passage"` field of the item schema (e.g., `"passage": "In the diagram, circle with centre O passes through points A, B, and C. Line AT is tangent to circle at A. Chord BC is parallel to AT. Angle BAC = 64°."`).
   - Enables pure text models (`koeberg-stage-1`, `kendal-stage-1`, `gariep-stage-1`) to tutor geometry with full context.
3. **Pure Visual / Complex Non-Text Diagrams (~10% of questions):**
   - Flagged with `"needs_review": true` during item extraction so they are excluded from pure text fine-tuning datasets.
   - Rendered to high-resolution PNG page images in `workspace/images/` and reserved for multimodal vision fine-tuning on `LiquidAI/LFM3-VL-2B` (`gariep-flash-stage-1`).
4. **Self-Contained Symbolic & Text Questions (~70% of questions):**
   - Algebra, calculus, trigonometry, financial maths, probability, organic chemistry, acid-base reactions, language comprehension, and literature. Extracted directly into structured items with full marking memo step criteria.
5. **Memo-First Question Recovery:**
   - For the 87 Mathematics question papers where equations were rasterized in the QP PDF, the DBE marking memorandums contain the questions, sub-question numbers, steps, method marks, and answers in full digital text (over 1.38M characters combined across math memos). The pipeline uses memo text to reconstruct questions and solutions seamlessly.

---

## 9. Extraction Manifest, Model Provenance & Verification Strategy
- **Extraction Audit Manifest (`workspace/text/manifest.jsonl`):**
  - Records granular provenance for every single document in the corpus:
    - `source_id`: Unique identifier (e.g. `dbe-afrikaans_fal-g12-p2-2025-nov`)
    - `model_used`: Exact vision model that performed transcription (`gemini-3.5-flash-lite`, `gemini-3.1-flash-lite`, etc.)
    - `char_count`: Total high-fidelity character count
    - `has_katex_latex`: KaTeX equation presence flag
    - `diagram_annotations`: Count of structured `[DIAGRAM: ...]` blocks
    - `duration_sec`: Request latency in seconds
    - `status`: Completion status (`COMPLETED`, `SHORT_OR_EMPTY`, `QUEUED`, `FAILED`)
- **Automated Verification Script (`pipeline/verify_extractions.py`):**
  - Cross-references the extracted `.txt` file against original raw `.pdf`:
    - Question sequence and completeness check (`QUESTION 1` to `QUESTION 10`, `VRAAG 1` to `VRAAG 10`, sub-questions).
    - Mark allocation reconciliation (sums sub-questions against paper total `[150]`).
    - LaTeX syntax integrity (balanced `$` and `$$`, valid fraction/radical syntax).
    - Diagram coverage audit.
  - Generates model performance scorecards: tracks accuracy, character yields, and defect rates by model.

---

## 10. Multi-Model Ingestion Pool & Persistent Daily Quota Memory
- **Persistent Quota State (`workspace/text/.quota_exhausted.json`):**
  - Remembers which models have exhausted their free-tier daily request limits (HTTP 429) on the current date (`YYYY-MM-DD`).
  - Automatically resets at midnight (12:00 AM) when the local date changes.
  - Completely eliminates redundant failing calls to exhausted models.
- **Dynamic Failover Priority Pool:**
  1. `gemini-3.1-flash-lite` (Primary high-throughput, 500 requests/day)
  2. `gemini-3.8-flash` (Flagship Flash)
  3. `gemini-3-flash-preview` (Preview Flash)
  4. `gemini-flash-latest` (General Flash fallback)
- **Zero-Stall Error Handling:**
  - On HTTP 503 or transient rate limits, the extractor immediately hands off to the next model in the pool instead of waiting on long backoff pauses.
  - Copyright filter blocks (`finishReason: "RECITATION"`) on question papers are caught immediately and handled gracefully via the DBE marking memorandum without stalling the pipeline.
- **Phase 2 Completion Milestone:**
  - All 4 curriculum stages (Mathematics/Wiskunde, English, Afrikaans, Physical Sciences/Fisiese Wetenskappe) completed with 11,310,442 characters, 354 KaTeX LaTeX documents, and 1,005 diagram descriptions.





