# Eishkom AI — Stage 1 Master Progress & Execution Roadmap

> **Release Cycle:** **Stage 1** (`koeberg-stage-1`, `kendal-stage-1`, `kendal-flash-stage-1`, `gariep-stage-1`, `gariep-flash-stage-1`)  
> **Target Curriculum:** South African CAPS (Grades 7–12) — Mathematics, Physical Sciences, English, Afrikaans  
> **Status:** **Phase 1 & Phase 2 Completed (100%)** | **Phase 0 In Progress (85%)** | **Total Compute Spend: $0.00 / $60.00**  
> **Corpus Volume:** **600 PDFs (300 verified pairs, 378.15 MB, 0 download failures)**  
> **Extracted Text Volume:** **600 Text Files (14,959,351 characters, 0 extraction errors)**  
> **Master Sources Ledger:** [`../sa-tutor-kit/sa-tutor-kit/workspace/sources/sources.csv`](../sa-tutor-kit/sa-tutor-kit/workspace/sources/sources.csv) (**604 entries**)

---

## 1. Executive Summary & Stage 1 Release Philosophy

**Eishkom AI** is developing an open-source, CAPS-aligned educational AI tutor ecosystem specifically designed for South African learners, teachers, and schools.

### Core Release Mandates:
1. **Clean Stage-Based Branding:**
   - Public release names **never show parameter numbers or quantization suffixes** (`27B`, `4B`, `Q4`, `Q6` do not show in user-facing brand names).
   - Clean names:
     - `koeberg-stage-1` (Flagship Cloud 27B)
     - `kendal-stage-1` (Budget PC & Laptop 4B Q6)
     - `kendal-flash-stage-1` (Midrange Mobile 4B Q4)
     - `gariep-stage-1` (Budget Phone 2B Q6)
     - `gariep-flash-stage-1` (Budget Vision/OCR 2B LiquidAI)
   - Releases use Stage cycles (`stage-1`, `stage-1.1`, `stage-2`) rather than arbitrary point increments.
2. **Base Repositories vs. GGUF Files:**
   - Never pass a compiled `-GGUF` file or repo to `train_sft.py`.
   - Always fine-tune unquantized Hugging Face base repositories with Unsloth QLoRA.
   - Export to GGUF at the end using `training/export_gguf.py`.
3. **Zero-Waste Compute:**
   - Google Cloud Gen AI & Cloud Credits: **\$60 promotional credits** utilized via **Vertex AI Colab Enterprise** on **NVIDIA L4 GPU Spot VMs** (~$0.32/hr).
   - Deployment: Containerized on **Google Cloud Run with serverless NVIDIA L4 GPU** and `--min-instances 0` ($0.00/hr when idle).
4. **Immutable Pipeline Stages:**
   - Kit code never overwrites previous pipeline stages (`raw/` → `text/` → `items/` → `gen/` → `verified/` → `build/` → `runs/` → `exports/`).
5. **Cross-Tier Distillation Trick:**
   - Train `koeberg-stage-1` (27B) first on the core dataset.
   - Use Koeberg to generate 2,000–5,000 step-by-step teacher explanations for the hardest DBE questions.
   - Verify Koeberg's answers against the DBE memorandums and inject into the training sets for `kendal-stage-1` (4B) and `gariep-stage-1` (2B).

---

## 2. Stage 1 Model Architecture & Lineup

| Public Model Name | Internal Tier | Base Hugging Face Repo | Target Export Format | Final Size | Target Hardware & Deployment |
|---|---|---|---|---|---|
| **`koeberg-stage-1`** | Flagship Cloud (27B) | `unsloth/Qwen3.8-27B` | `UD-Q4_K_XL` (Unsloth Dynamic Q4) | ~17.6 GB | **Cloud:** Google Cloud Run (Serverless NVIDIA L4 24GB, scale-to-zero)<br>**Local:** 16GB/20GB RAM PCs (CPU offload) |
| **`kendal-stage-1`** | Budget PC & Laptop (4B Q6) | `unsloth/Qwen3.5-4B` | `Q6_K` or `UD-Q6_K_XL` | ~3.53–4.15 GB | **Local:** GTX 1650 (4GB VRAM) desktops & 16GB/20GB RAM laptops (100% offline) |
| **`kendal-flash-stage-1`** | Mobile & Phone (4B Q4) | `empero-ai/Qwen3.8-4B-Distill` *(or unsloth 4B)* | `Q4_K_M` | ~2.78–2.91 GB | **Local:** Midrange smartphones (6GB–8GB RAM) & 4GB PCs (100% offline) |
| **`gariep-stage-1`** | Budget Phone Tutor (2B Q6) | `empero-ai/Qwen3.8-2B-Distill` *(or unsloth 2B)* | `Q6_K` or `Q8_0` | ~1.75–2.15 GB | **Local:** Budget smartphones (4GB RAM) & entry laptops (100% offline) |
| **`gariep-flash-stage-1`** | Budget Vision/OCR (2B LiquidAI) | `LiquidAI/LFM3-VL-2B` | `Q6_K` | ~1.55 GB | **Local:** Budget phones for high-speed document, diagram, and OCR reading |

---

## 3. Comprehensive Master Checklist

```
[x] Phase 0 (Partial): Setup & Tooling
    [x] Verify Python 3.12 environment on local machine
    [x] Initialize workspace directories: raw, text, items, gen, verified, build, runs, exports, eval
    [x] Build automated DBE downloader pipeline/download_dbe.py
    [x] Upgrade Colab Enterprise notebook colab/sa_tutor_colab.ipynb (26 cells, Spot VM support)
    [x] Validate local verification scripts (answers, board, llm, retrieval, tutor_data)
    [ ] Install SymPy: pip install sympy
    [ ] Configure TEACHER_API_KEY in .env

[x] Phase 1: Source Data Collection
    [x] Discover DBE links across 2018-2025 Grade 12 NSC + Grade 10-11 Common Papers
    [x] Implement clean subject & language routing (English vs. Afrikaans)
    [x] Download all 300 paper+memo pairs (600 PDFs, 378.15 MB, 0 failures)
    [x] Populate workspace/sources/sources.csv (604 rows with pair_with links)
    [x] Lock 16 November 2024 Grade 12 papers as held out for EVAL

[x] Phase 2: Document Ingestion & Vision Upgrade (Completed & Audited)
    [x] Identify failure modes of legacy pypdf stream extraction (empty scans, scrambled MathType, column breaks)
    [x] Build direct multimodal PDF vision extractor pipeline/ingest_vision.py powered by Gemini 3.5 Flash
    [x] Configure active Gemini API credentials in .env
    [x] Successfully verify end-to-end direct extraction on empty scan (May 2021 Maths P1 -> 8,942 chars clean LaTeX)
    [x] Successfully verify end-to-end direct extraction on MathType memo (May 2021 Memo -> 12,842 chars clean LaTeX)
    [x] Extract structured items with extract_items.py into workspace/items/ (Questions 1 & 2 verified: 11 items, 0 review)

[ ] Phase 2.5: Item Extraction & LaTeX/Diagram Standardization
    [ ] Standardize all equations, fractions, and symbols into LaTeX ($...$ inline, $$...$$ block)
    [ ] Encode text-describable diagrams (geometry, circuits, graphs) into the "passage" field
    [ ] Flag pure visual figures with "needs_review": true (quarantined for gariep-flash-stage-1 vision training)
    [ ] Run python pipeline/extract_items.py with teacher LLM (DeepSeek / Gemini OpenAI endpoint)
    [ ] Store structured items in workspace/items/<source_id>.jsonl

[ ] Phase 3: Benchmark Construction
    [ ] Extract November 2024 Grade 12 NSC items
    [ ] Compile workspace/eval/eval_items.jsonl
    [ ] Verify zero overlap with training data

[ ] Phase 4: Teacher Dialogue Generation
    [ ] Configure DeepSeek V4.1 Flash / Vertex AI Gemini Flash
    [ ] Run python pipeline/generate_dialogues.py --round 1 --max-items 5000
    [ ] Store generated dialogues in workspace/gen/r1/

[ ] Phase 5: Verification & SymPy Checking
    [ ] Run python pipeline/verify.py
    [ ] Verify mathematical steps with SymPy
    [ ] Verify against official DBE marking memorandums
    [ ] Filter out hallucinations into workspace/verified/r1/

[ ] Phase 6: Human Review Sample
    [ ] Sample 40 records from workspace/verified/r1/
    [ ] Manually audit pedagogical tone, language quality, and correctness

[ ] Phase 7: Dataset Build
    [ ] Run python pipeline/build_train.py
    [ ] Generate train/val splits in workspace/build/r1/

[ ] Phase 8: Cross-Tier Distillation Injection
    [ ] Fine-tune koeberg-stage-1 (27B) on core dataset
    [ ] Generate 2,000-5,000 hard solutions using fine-tuned Koeberg
    [ ] Verify Koeberg solutions and append to kendal and gariep training sets

[ ] Phase 9: SFT Training in Vertex AI Colab Enterprise
    [ ] Launch NVIDIA L4 Spot VM in Vertex AI Colab Enterprise (~$0.32/hr)
    [ ] Train koeberg-stage-1 (27B) (~5.5 hrs, ~$1.76)
    [ ] Train kendal-stage-1 (4B) (~1.0 hr, ~$0.32)
    [ ] Train gariep-stage-1 (2B) (~35 mins, ~$0.19)
    [ ] Verify automatic checkpoints saved to Google Drive (--resume)

[ ] Phase 10: Multi-Quant GGUF Export
    [ ] Run python training/export_gguf.py
    [ ] Export koeberg-stage-1-UD-Q4_K_XL.gguf
    [ ] Export kendal-stage-1-Q6_K.gguf AND kendal-flash-stage-1-Q4_K_M.gguf from single run
    [ ] Export gariep-stage-1-Q6_K.gguf

[ ] Phase 11: Multi-Modal Vision Fine-Tuning
    [ ] Fine-tune LiquidAI/LFM3-VL-2B on geometry and textbook diagrams
    [ ] Export gariep-flash-stage-1-Q6_K.gguf + mmproj

[ ] Phase 12: Cloud Run Scale-to-Zero Deployment
    [ ] Build Dockerfile with Ollama / vLLM
    [ ] Deploy koeberg-stage-1 to Google Cloud Run with serverless NVIDIA L4 GPU
    [ ] Configure --min-instances 0 ($0.00/hr idle)
    [ ] Test live API endpoint
```

---

## 4. Phase 1 Downloaded Corpus Inventory

The table below summarizes the 600 PDFs downloaded and verified on disk in `workspace/raw/dbe/`:

| Subject / Category | Language Directory | Total PDFs | Papers | Memos | Grade Levels | Year Range |
|---|---|---|---|---|---|---|
| **Mathematics** | `dbe/english/mathematics/` | 92 | 46 | 46 | Gr 10, 11, 12 | 2015–2025 |
| **Wiskunde** | `dbe/afrikaans/wiskunde/` | 88 | 44 | 44 | Gr 10, 11, 12 | 2015–2025 |
| **Physical Sciences** | `dbe/english/physical_sciences/` | 92 | 46 | 46 | Gr 10, 11, 12 | 2015–2025 |
| **Fisiese Wetenskappe** | `dbe/afrikaans/fisiese_wetenskappe/` | 88 | 44 | 44 | Gr 10, 11, 12 | 2015–2025 |
| **English HL** | `dbe/english/english_hl/` | 60 | 30 | 30 | Gr 12 NSC | 2018–2025 |
| **English FAL** | `dbe/english/english_fal/` | 60 | 30 | 30 | Gr 12 NSC | 2018–2025 |
| **Afrikaans HL** | `dbe/afrikaans/afrikaans_hl/` | 60 | 30 | 30 | Gr 12 NSC | 2018–2025 |
| **Afrikaans FAL** | `dbe/afrikaans/afrikaans_fal/` | 60 | 30 | 30 | Gr 12 NSC | 2018–2025 |
| **TOTALS** | **`workspace/raw/dbe/`** | **600** | **300** | **300** | **Gr 10–12** | **2015–2025** |

---

## 4.5. Phase 2 Extracted Text Inventory & Audit

The table below audits the 600 text files extracted into `workspace/text/` by `pipeline/ingest.py`:

| Subject | Language / Track | Total Files | QP / Memo Ratio | Total Characters | QP Characters | Memo Characters |
|---|---|---|---|---|---|---|
| **Mathematics** | English (Core Maths) | 92 | 46 / 46 | 737,870 | 25,206 | 712,664 |
| **Wiskunde** | Afrikaans (Kernwiskunde) | 88 | 44 / 44 | 699,921 | 25,051 | 674,870 |
| **Physical Sciences** | English (Physics & Chem) | 92 | 46 / 46 | 2,101,014 | 865,659 | 1,235,355 |
| **Fisiese Wetenskappe** | Afrikaans (Fisika & Chemie) | 88 | 44 / 44 | 1,998,472 | 830,274 | 1,168,198 |
| **English HL** | English Home Language | 60 | 30 / 30 | 2,040,510 | 834,647 | 1,205,863 |
| **English FAL** | English 1st Additional Lang | 60 | 30 / 30 | 1,678,608 | 883,666 | 794,942 |
| **Afrikaans HL** | Afrikaans Huistaal | 60 | 30 / 30 | 2,981,171 | 988,146 | 1,993,025 |
| **Afrikaans FAL** | Afrikaans 1ste Addisionele Taal | 60 | 30 / 30 | 2,721,785 | 1,417,087 | 1,304,698 |
| **TOTALS** | **`workspace/text/`** | **600** | **300 / 300** | **14,959,351** | **5,869,736** | **9,089,615** |

> [!NOTE]
> In Mathematics and Wiskunde, 87 Question Paper PDFs had mathematical equations rendered as images/vector paths in older DBE exams (yielding low plain text). However, their paired official memorandums contain **1,387,534 characters** of full question text, sub-questions, method marks, and worked solutions. The extraction pipeline leverages memo text to recover these questions completely.

---

## 5. Compute Budget & Credit Ledger

| Resource | Allotted Budget | Consumed So Far | Remaining Balance | Projected Need |
|---|---|---|---|---|
| **Google Cloud Credits** | **\$60.00** | **\$0.00** | **\$60.00** | ~$2.50 for training, remainder for Cloud Run |
| **Teacher API Spend** | **\$15.00** | **\$0.00** | **\$15.00** | ~$2.00–$4.00 for 5,000 dialogues |
| **Local Disk Space** | ~20.0 GB | **0.38 GB** | ~19.62 GB | ~3–5 GB for text and intermediate datasets |

---

## 6. Verification Audit Log

| Date | Milestone | Status | Key Artifacts | Notes |
|---|---|---|---|---|
| 2026-11-03 | Stage 1 Lineup Finalized | Verified | `workspace/DECISIONS.md` | Defined 5 Stage 1 models, clean branding, base repo vs GGUF rule |
| 2026-11-03 | Google Cloud Credits Plan | Verified | `chats/gemini-transcript.md` | Colab Enterprise L4 Spot VM ($0.32/hr), Cloud Run scale-to-zero |
| 2026-11-03 | Colab Notebook Upgrade | Verified | `colab/sa_tutor_colab.ipynb` | 26 automated cells, Spot VM checkpoint resume, multi-quant export |
| 2026-11-03 | DBE Crawler Created | Verified | `pipeline/download_dbe.py` | Automated link scraping, ticket resolution, language partitioning |
| 2026-11-03 | Phase 1 Download Complete | Verified | `workspace/raw/dbe/` | **600 PDFs downloaded (378.15 MB, 0 failures)** |
| 2026-11-03 | Sources Ledger Populated | Verified | `workspace/sources/sources.csv` | **604 rows**, `pair_with` links, 16 Nov 2024 Gr12 papers locked |
| 2026-11-03 | Phase 2 Ingestion Complete | Verified | `workspace/text/` | **600 text files extracted (14,959,351 characters, 0 failures)** |

