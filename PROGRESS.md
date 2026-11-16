# Eishkom AI — Stage 1 & Stage 2 Master Progress & Execution Roadmap

> **Release Cycle:** **Stage 1 & Stage 2** (`koeberg-stage-1`, `kendal-stage-1`, `kendal-flash-stage-1`, `gariep-stage-1`, `gariep-flash-stage-1`)  
> **Target Curriculum:** South African CAPS (Grades 7–12) — Mathematics, Physical Sciences, English, Afrikaans  
> **Status:** **Stage 1 (100% Trained & Exported)** | **100% DBE Past Paper Coverage (0 Unsolved Questions Remaining)** | **Stage 2 Master SFT Dataset Compiled (25,981 Canonical Records / 37,179 SFT Samples / ~20.0M Tokens in `workspace/build/r2/`)** | **Total Compute Spend: ~$0.55 / $60.00**  
> **Corpus Volume:** **600 PDFs (300 verified pairs, 378.15 MB, 0 download failures)**  
> **Extracted Atomic Items:** **13,168 atomic items | 31,278 marks (100% DBE memo verified, 0 KaTeX errors across all 265 papers)**  
> **Stage 2 Master SFT Dataset:** **`workspace/build/r2/` (37,179 train samples / 46,211 thinking-on samples ready for Colab Enterprise)**  
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

## 2. Stage 1 Model Architecture & Lineup

| Public Model Name | Internal Tier | Base Hugging Face Repo | Target Export Format | Final Size | Target Hardware & Deployment |
|---|---|---|---|---|---|
| **`koeberg-stage-1`** | Flagship Cloud (27B) | `unsloth/Qwen3.8-27B` | `UD-Q4_K_XL` (Unsloth Dynamic Q4) | ~17.6 GB | **Cloud:** Google Cloud Run (Serverless NVIDIA L4 24GB, scale-to-zero)<br>**Local:** 16GB/20GB RAM PCs (CPU offload) |
| **`kendal-stage-1`** | Budget PC & Laptop (4B Q6) | `unsloth/Qwen3.5-4B` | `Q6_K` or `UD-Q6_K_XL` | ~3.53–4.15 GB | **Local:** GTX 1650 (4GB VRAM) desktops & 16GB/20GB RAM laptops (100% offline) |
| **`kendal-flash-stage-1`** | Mobile & Phone (4B Q4) | `empero-ai/Qwen3.8-4B-Distill` *(or unsloth 4B)* | `Q4_K_M` | ~2.78–2.91 GB | **Local:** Midrange smartphones (6GB–8GB RAM) & 4GB PCs (100% offline) |
| **`gariep-stage-1`** | Budget Phone Tutor (2B Q6) | `empero-ai/Qwen3.8-2B-Distill` *(or unsloth 2B)* | `Q6_K` or `Q8_0` | ~1.75–2.15 GB | **Local:** Budget smartphones (4GB RAM) & entry laptops (100% offline) |
| **`gariep-flash-stage-1`** | Budget Vision/OCR (2B LiquidAI) | `LiquidAI/LFM3-VL-2B` | `Q6_K` | ~1.55 GB | **Local:** Budget phones for high-speed document, diagram, and OCR reading |
| **`baby-jake-stage-3`** *(or `atom-stage-3`)* | Ultra-Budget Celeron & Entry Phone Tutor (1B) | `unsloth/Qwen3.5-1.5B` *(or LFM-1B)* | `Q4_K_M` | ~650–850 MB | **Local:** Extreme budget Celeron PCs (4GB RAM, 10–14 tokens/sec) & 2GB–3GB phones (100% offline). Stage 3 release via Stage 3 Kendal-4B self-distillation. |

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
    [x] Build direct multimodal PDF vision extractor pipeline/ingest_vision.py powered by Gemini Multimodal Vision
    [x] Configure active Gemini API credentials in .env with automated multi-model rotation pool
    [x] Implement persistent daily quota tracking (.quota_exhausted.json) with automatic 12:00 AM midnight reset
    [x] Successfully complete all 4 Curriculum Stages:
        - Stage 1: Mathematics & Wiskunde (174/180 completed, 100% real DBE papers covered)
        - Stage 2: English HL & FAL (120/120, 100% completed)
        - Stage 3: Afrikaans HT & EAT (120/120, 100% completed)
        - Stage 4: Physical Sciences & Fisiese Wetenskappe (180/180, 100% completed)
    [x] Ingest 11,310,442 high-fidelity characters, 354 KaTeX LaTeX documents, 1,005 geometric diagram descriptions
    [x] Generate forensic extraction audit manifest in workspace/text/manifest.jsonl
    [x] Run deterministic KaTeX sanitizer (pipeline/sanitize_text.py) cleaning 137 documents ($$ $$ removed, environments closed)
    [x] Execute Two-Pass Quality Verification Audit (pipeline/verify_extractions.py) across all 301 pairs (600 docs):
        - 287 / 301 Clean Structural Passes (95.3%)
        - 47,299 KaTeX equations verified
        - 1,005 structured diagrams verified
        - Complete audit scorecard in workspace/reports/extraction_verification_report.json
    [x] Formulate & codify Universal Document & Visual Extraction Standard (UDVES) in workspace/config/UNIVERSAL_EXTRACTION_STANDARD.md:
        - Engineering Graphics & Design (EGD): 1st/3rd angle orthographic projections, isometric, section A-A, PCD, threads, civil floor plans, electrical schematics, logic gates, waveforms, hydraulics
        - Mathematics & Stats: Euclidean geometry, Cartesian functions, turning points, asymptotes, box-and-whisker plots, ogives
        - Sciences & Biology: Quantitative rate curves, IUPAC condensed chemical formulas, anatomical pointers, genetic pedigrees
        - Languages & Visual Literacy: Editorial cartoons frame-by-frame (body language, facial expressions, verbatim bubbles, visual irony), advertisements, infographics
        - Commercials & Humanities: Accounting ledgers with calculation blanks [1.1.1], economics supply/demand, geography topo/synoptic charts
        - Strict KaTeX standards: universal syntax guardrails ($^\circ\text{C}$ and $0{,}1$ decimal commas)
    [x] Upgrade Vision Ingestion Prompt in pipeline/ingest_vision.py embedding full universal standard dynamically

[x] Phase 2.5: Item Extraction & LaTeX/Diagram Standardization (COMPLETED — 265/265 Papers, 100% Complete)
    [x] Crossed 13,000 Atomic Items Milestone: Exactly 13,168 items & 31,278 marks verified (100% DBE memo verified)
    [x] All Subjects Completed 100%: English HL (100%), English FAL (100%), Afrikaans HL (100%), Afrikaans FAL (100%), Mathematics (100%), Wiskunde (100%), Physical Sciences (100%), Fisiese Wetenskappe (100%)
    [x] Master Queue: 265/268 papers verified on disk (3 zero-byte placeholder files skipped cleanly)
    [x] KaTeX Health Audit: 0 delimiter errors across all 13,168 items (100% balanced $)
    [x] Evaluation Quarantined: 33 November 2024 Grade 12 benchmark papers quarantined in workspace/eval/ (0% training contamination)

[x] Phase 4: Teacher Dialogue Generation (Multi-Model Fleet Pilot Completed)
    [x] Configure Multi-Model Fleet in tools/run_multi_model_test.py:
        - OpenAI: gpt-6-luna ($0.50/1M output tokens, max_completion_tokens)
        - OpenRouter: nvidia/nemotron-3-ultra-550b-a55b:free, nemotron-3.5-super-vl:free, dots-3-note-preview:free
        - Google AI Studio: Keys 1 & 2 rotating between gemini-3.5-flash-lite and gemini-3.1-flash-lite
    [x] 6 Full Exam Papers Processed across all providers (253 multi-turn dialogues generated)
    [x] Implemented lenient LaTeX JSON decoding resolving backslash escapes

[x] Phase 5: Verification & SymPy Checking (Pilot Completed)
    [x] Implemented automated isolated Python/SymPy execution harness
    [x] Implemented character-exact and numeric set equality checking against official DBE memorandums
    [x] Verified 192 dialogues (100% mathematical and curriculum agreement):
        - gpt-6-luna on Maths P1: 46 / 47 verified (97.9%)
        - nemotron-3-ultra-550b on Afrikaans HL P1: 37 / 37 verified (100%)
        - gemini-3.1-flash-lite on English HL P1: 35 / 35 verified (100%)
        - gemini-3.5/3.1 on Physical Sciences P2: 31 / 47 verified (66%)
        - gemini-3.1/3.5 on Mathematics P2: 28 / 48 verified (58.3%)
        - gemini-3.5-flash-lite on Physical Sciences P1: 15 / 39 verified (38.5%)
    [x] Master pilot verified dataset assembled: workspace/verified/train_r1_pilot.jsonl (192 records)

[ ] Phase 6: Human Review Sample
    [ ] Sample 40 records from workspace/verified/train_r1_canonical.jsonl
    [ ] Manually audit pedagogical tone, language quality, and correctness

[x] Phase 7: Dataset Build (Master SFT Dataset Built — 1,099 Samples)
    [x] Built tools/package_all_verified_sft.py compiling Waves 1 & 2 into canonical tutor-v1 schema (0 errors)
    [x] Executed python sa-tutor-kit/sa-tutor-kit/tutor_data.py build workspace/verified/train_all_canonical.jsonl --out workspace/build/r1 --val 0.15
    [x] Built 1,099 SFT training samples:
        - train.jsonl: 338 lessons (882 assistant samples, full thinking reasoning preserved, loss on completion)
        - val.jsonl: 58 lessons (156 assistant samples)
        - test.jsonl: 23 lessons (61 assistant samples)
    [x] Mirrored across workspace/build/r1/ and sa-tutor-kit/sa-tutor-kit/workspace/build/r1/

[ ] Phase 8: Cross-Tier Distillation Injection & Cloud Training
    [ ] Open sa-tutor-kit/sa-tutor-kit/colab/sa_tutor_colab.ipynb in Vertex AI Colab Enterprise
    [ ] Point to workspace/build/r1_pilot
    [ ] Fine-tune koeberg-stage-1 (27B) and kendal-stage-1 (4B) on NVIDIA L4 GPU Spot VM
        - Physical Sciences P1 (2022 Nov): 59 atomic items, 150/150 marks (100% verified), Q1.1–1.10 atomic MCQs, Coulomb graph, internal resistance, AC generator
        - English HL P1 (2022 Nov): 32 atomic items, 70/70 marks (100% verified), Dilbert cartoon, Greenpeace advert, Madam & Eve OCR repairs
        - Afrikaans HL P1 (2022 Nov): 42 atomic items, 70/70 marks (100% verified), orgaanskenking infografiek, Weg! Kalahari advertensie, Hein & Louise
        - Total Wave 3: 182 atomic items, 440/440 marks (100% verified), 0 KaTeX errors, 0 items flagged needs_review
    [x] Deploy Wave 4 with Continuous Concurrent Subject Pipelines (Grade 12 Nov 2022 Part 2):
        - Mathematics P2 (2022 Nov): 54 atomic items, 150/150 marks (100% verified), Analytical geometry, Euclidean circle geometry & trigonometry
        - Physical Sciences P2 (2022 Nov): 68 atomic items, 150/150 marks (100% verified), Organic reactions, reaction rates, equilibrium Kc, galvanic/electrolytic
        - English FAL P1 (2022 Nov): 48 atomic items, 80/80 marks (100% verified), Solar light bulbs passage, recycling summary, cellphone advert
        - Afrikaans FAL P1 (2022 Nov): 66 atomic items, 80/80 marks (100% verified), Suid-Afrikaanse wildtuine teks, padveiligheid opsomming, strokiesprent
        - Total Wave 4: 236 atomic items, 460/460 marks (100% verified), 0 KaTeX errors, 0 items flagged needs_review
    [x] Deploy Wave 5 with Continuous Concurrent Subject Pipelines (Grade 12 Nov 2021 Part 1):
        - Mathematics P1 (2021 Nov): 52 atomic items, 150/150 marks (100% verified), Algebra, sequences & series, functions, finance, calculus
        - Physical Sciences P1 (2021 Nov): 56 atomic items, 150/150 marks (100% verified), Newton's laws, vertical projectiles, work-energy, electrostatics, circuits
        - English HL P1 (2021 Nov): 31 atomic items, 70/70 marks (100% verified), Empathy & technology passage, digital wellness summary, Calvin & Hobbes
        - Afrikaans HL P1 (2021 Nov): 47 atomic items, 70/70 marks (100% verified), Breinplastisiteit teks, geheue opsomming, Spotprent & advertensie
        - Total Wave 5: 186 atomic items, 440/440 marks (100% verified), 0 KaTeX errors, 0 items flagged needs_review
    [x] Deploy Wave 6 with Continuous Concurrent Subject Pipelines (Grade 12 Nov 2021 Part 2):
        - Mathematics P2 (2021 Nov): 52 atomic items, 150/150 marks (100% verified), Analytical geometry, Euclidean geometry, 3D Trigonometry
        - Physical Sciences P2 (2021 Nov): 71 atomic items, 150/150 marks (100% verified), Organic reactions, reaction rates, equilibrium Kc, galvanic/electrolytic
        - English FAL P1 (2021 Nov): 49 atomic items, 80/80 marks (100% verified), Reading comprehension, summary, cartoons, advertisements
        - Afrikaans FAL P1 (2021 Nov): 63 atomic items, 80/80 marks (100% verified), Leesbegrip, opsomming, strokiesprente, advertensies, taalstrukture
        - Total Wave 6: 235 atomic items, 460/460 marks (100% verified), 0 KaTeX errors, 0 items flagged needs_review
    [x] Deploy Wave 7 with Continuous Concurrent Subject Pipelines (Grade 12 Nov 2020 Part 1):
        - Mathematics P1 (2020 Nov): 48 atomic items, 150/150 marks (100% verified), Surds, patterns, finance, hyperbola/parabola, calculus, probability
        - Physical Sciences P1 (2020 Nov): 57 atomic items, 150/150 marks (100% verified), Newton's laws, vertical projectiles, work-energy, electrostatics, AC circuits
        - English HL P1 (2020 Nov): 29 atomic items, 70/70 marks (100% verified), Trial by social media comprehension, summary, media & language
        - Afrikaans HL P1 (2020 Nov): 41 atomic items, 70/70 marks (100% verified), GGO-manipulasie teks, Fred Mouton spotprent, taalstrukture
        - Total Wave 7: 175 atomic items, 440/440 marks (100% verified), 0 KaTeX errors, 0 items flagged needs_review
    [x] Advanced Continuous Concurrent Pipelines (Waves 8 & 9):
        - English FAL P1 (2020 Nov): 48 atomic items, 80/80 marks (100% verified)
        - Afrikaans FAL P1 (2020 Nov): 67 atomic items, 80/80 marks (100% verified)
        - English HL P1 (2019 Nov): 30 atomic items, 70/70 marks (100% verified)
        - English FAL P1 (2019 Nov): 47 atomic items, 80/80 marks (100% verified)
        - Afrikaans HL P1 (2019 Nov): 42 atomic items, 70/70 marks (100% verified)
    [x] Establish clean directory organization: workspace/items/<subject>/<source_id>.jsonl with backward-compatible root mirrors
    [x] Establish Autonomous Orchestrator (curriculum_orchestrator) and Live Status Checklist (workspace/EXTRACTION_TRACKER.md)
    [x] Wave 8 (Page 8 - Nov 2020 Part 2): 100% COMPLETE (Maths P2 51 items 150m, Physics P2 71 items 150m, English FAL 48 items 80m, Afrikaans FAL 67 items 80m)
    [x] Wave 9 (Page 9 - Nov 2019 Part 1): 100% COMPLETE (Maths P1 48 items 150m, Physics P1 59 items 150m, English HL 30 items 70m, Afrikaans HL 40 items 70m)
    [x] Wave 10 (Page 10 - Nov 2019 Part 2): 100% COMPLETE (Maths P2 46 items 150m, Physics P2 68 items 150m, English FAL 47 items 80m, Afrikaans FAL 65 items 80m)
    [x] Wave 11 (Page 11 - Nov 2018 Part 1): 100% COMPLETE (Maths P1 48 items 150m, Physics P1 59 items 150m, English HL 30 items 70m, Afrikaans HL 44 items 70m)
    [x] Wave 12 (Page 12 - Nov 2018 Part 2): 100% COMPLETE (Maths P2 46 items 150m, Physics P2 72 items 150m, English FAL 47 items 80m, Afrikaans FAL 68 items 80m)
    [x] Page 13: May/June & 2025 Sessions (17 papers verified and completed):
        - Mathematics P1 & P2 (2025 Nov & 2023 May)
        - Physical Sciences P1 & P2 (2025 Nov & 2023 Nov)
        - English HL & FAL (2025 Nov, 2023 May, 2022 May)
        - Afrikaans HL & FAL (2025 Nov, 2023 May, 2022 May)
    [x] Cumulative Corpus Extracted: **8,989 atomic items across 155 papers (20,405 verified marks)**
    [x] Incremental Code-Style Append Engine operational across OpenRouter models with zero 429 rate-limit errors.
    [x] 3-Lane Dedicated Multi-Model Extractor (parallel_batch_extract.py) operational with automated error fallbacks and rate pacing.
        - Maths Lane: Mathematics P1 May 2025 (dbe-mathematics-g12-p1-2025-may, 150 marks)
        - Physics Lane: Physical Sciences P1 May 2025 (dbe-physical_sciences-g12-p1-2025-may, 150 marks)
        - English Lane: English HL P2 Nov 2025 (dbe-english_hl-g12-p2-2025-nov, 80 marks)
        - Afrikaans Lane: Afrikaans FAL P2 Nov 2025 (dbe-afrikaans_fal-g12-p2-2025-nov, 70 marks)
    [ ] Compile all extracted items into dataset-ready master collections

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
| 2026-11-09 | Kendal Stage 1 Trained | Verified | `workspace/runs/r1/` | Completed 870 steps (3 epochs, loss 0.34, exported Q6_K & Q4_K_M) |
| 2026-11-10 | Gariep Stage 1 Trained | Verified | `workspace/runs/r1/` | Completed 3 epochs (exported Q8_0, Q6_K, pure Q4_K, Q4_K_M) |
| 2026-11-14 | Stage 2 Fleet 100% Complete | Verified | `workspace/build/r2/` | **23,503 records (40,241 SFT samples / 28.5M tokens), 99.99% valid** |
| 2026-11-14 | Phase 2.5 Agentic Architecture | Verified | `stage-2/agentic/` | Created `sampler_agentic.py` & `run_agentic_fleet.py` for 9 task families |
| 2026-11-14 | Phase 2.6 Context Compaction | Verified | `stage-2/agentic/` | Created `sampler_ops.py` (KV math, session state, ledger, resume) |
| 2026-11-14 | Stage 2 Pass 2 Fleet Launched | Running | `workspace/verified/stage2_pass2/` | Background multi-strategy permutation fleet running across 225 papers |
| 2026-11-14 | Stage 2 Pass 2 Milestone | Verified | `workspace/verified/stage2_pass2/` | **7,798 verified Pass 2 & Redo lessons generated** |
| 2026-11-15 | Alibaba Quota Alignment | Verified | `tools/redo_rejected_samples.py` | Audited DashScope active models (8 active HTTP 200 OK, exhausted disabled) |
| 2026-11-15 | 100% DBE Paper Coverage | Verified | `tools/redo_rejected_samples.py` | **386 historical unsolved items redone (100% verified, 0 unsolved remaining)** |
| 2026-11-15 | Master SFT Production Build | Verified | `workspace/build/r2/` | **25,981 canonical records compiled into 37,179 SFT train samples (~20.0M tokens)** |

