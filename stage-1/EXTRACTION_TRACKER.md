# Eishkom AI — Universal Item Extraction Tracker & Queue

> **Stage 1 Release Cycle:** `koeberg-stage-1`, `kendal-stage-1`, `kendal-flash-stage-1`, `gariep-stage-1`, `gariep-flash-stage-1`  
> **Master Corpus:** **301 Exam Pairs (602 DBE PDFs)**  
> **Quarantined for EVAL:** **33 Papers (Strictly held out)**  
> **Training Target:** **268 Papers**  
> **Verified Extracted Items:** **435 atomic items** across **9 papers** (941 total marks verified)  

---

## 1. Executive Status Board

| Metric | Status | Description |
|---|---|---|
| **Pilot Wave (Page 1)** | **4/4 COMPLETE** | 4/4 Core Subjects verified (Maths P1, Physics P2, English HL, Afrikaans HL) |
| **Active Wave (Page 2)** | **100% COMPLETE** | Maths P2, Physics P1, English FAL P1, Afrikaans FAL P1 |
| **Next Wave (Page 3)** | **ACTIVE QUEUE** | Grade 12 Nov 2022 Core STEM |
| **Total Extracted Items** | **435 Items** | KaTeX formatted, UDVES standardized, atomic multiple choice |
| **Total Marks Accounted** | **941 Marks** | 100% agreement with DBE official memorandums |
| **Quarantined Benchmark** | **33 Papers** | Locked in `workspace/eval/` — 0% training contamination |

---

## 2. Page 1: Pilot Wave (Completed & Verified)

| Status | Source ID | Subject | Grade | Session | Items | Marks | KaTeX Errors | Flagged Review | Dual Mirror |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [x] | `dbe-mathematics-g12-p1-2023-nov` | mathematics | Gr 12 | 2023 Nov | **51** | **150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p2-2025-nov` | physical | Gr 12 | 2025 Nov | **68** | **150** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p1-2023-nov` | english | Gr 12 | 2023 Nov | **35** | **70** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p1-2023-nov` | afrikaans | Gr 12 | 2023 Nov | **41** | **70** | 0 | 0 | Yes |

---

## 3. Page 2: Wave 2 (Grade 12 Nov 2023 Wave)

| Status | Source ID | Subject | Grade | Session | Items | Marks | KaTeX Errors | Flagged Review | Dual Mirror |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [x] | `dbe-mathematics-g12-p2-2023-nov` | mathematics | Gr 12 | 2023 Nov | **53** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p1-2023-nov` | physical | Gr 12 | 2023 Nov | **61** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p1-2023-nov` | english | Gr 12 | 2023 Nov | **47** | **80/80** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p1-2023-nov` | afrikaans | Gr 12 | 2023 Nov | **68** | **80/80** | 0 | 0 | Yes |

---

## 4. Page 3: Wave 3 (Upcoming Batch Queue)

| Status | Source ID | Paired Memo ID | Subject | Expected Marks | Batch |
|:---:|---|---|---|:---:|:---:|
| [ ] | `dbe-mathematics-g12-p1-2022-nov` | `dbe-mathematics-g12-p1-2022-nov-memo` | mathematics | 150 | Wave 3 |
| [ ] | `dbe-mathematics-g12-p2-2022-nov` | `dbe-mathematics-g12-p2-2022-nov-memo` | mathematics | 150 | Wave 3 |
| [ ] | `dbe-physical_sciences-g12-p1-2022-nov` | `dbe-physical_sciences-g12-p1-2022-nov-memo` | physical | 150 | Wave 3 |
| [ ] | `dbe-physical_sciences-g12-p2-2022-nov` | `dbe-physical_sciences-g12-p2-2022-nov-memo` | physical | 150 | Wave 3 |

---

## 5. Evaluation Benchmark Quarantine (Held-Out)

> [!IMPORTANT]
> The following 17 papers are strictly locked in `workspace/eval/` and NEVER processed into training datasets:

| Status | Source ID | Subject | Year | Notes |
|:---:|---|---|:---:|---|
| [LOCKED] | `dbe-maths-g12-p1-2024-nov` | mathematics | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-afrikaans_fal-g12-p1-2024-nov` | afrikaans | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-afrikaans_fal-g12-p2-2024-nov` | afrikaans | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-afrikaans_hl-g12-p1-2024-nov` | afrikaans | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-afrikaans_hl-g12-p2-2024-nov` | afrikaans | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-english_fal-g12-p1-2024-nov` | english | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-english_fal-g12-p2-2024-nov` | english | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-english_hl-g12-p1-2024-nov` | english | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-english_hl-g12-p2-2024-nov` | english | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-mathematics-g12-p1-2024-nov` | mathematics | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-wiskunde-g12-v1-2024-nov` | wiskunde | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-mathematics-g12-p2-2024-nov` | mathematics | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-wiskunde-g12-v2-2024-nov` | wiskunde | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-physical_sciences-g12-p1-2024-nov` | physical | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-fisiese_wetenskappe-g12-v1-2024-nov` | fisiese | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-physical_sciences-g12-p2-2024-nov` | physical | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-fisiese_wetenskappe-g12-v2-2024-nov` | fisiese | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-afrikaans_fal-g12-p1-2024-may` | afrikaans | 2024 | `` |
| [LOCKED] | `dbe-afrikaans_fal-g12-p2-2024-may` | afrikaans | 2024 | `` |
| [LOCKED] | `dbe-afrikaans_hl-g12-p1-2024-may` | afrikaans | 2024 | `` |
| [LOCKED] | `dbe-afrikaans_hl-g12-p2-2024-may` | afrikaans | 2024 | `` |
| [LOCKED] | `dbe-english_fal-g12-p1-2024-may` | english | 2024 | `` |
| [LOCKED] | `dbe-english_fal-g12-p2-2024-may` | english | 2024 | `` |
| [LOCKED] | `dbe-english_hl-g12-p1-2024-may` | english | 2024 | `` |
| [LOCKED] | `dbe-english_hl-g12-p2-2024-may` | english | 2024 | `` |
| [LOCKED] | `dbe-mathematics-g12-p1-2024-may` | mathematics | 2024 | `` |
| [LOCKED] | `dbe-wiskunde-g12-v1-2024-may` | wiskunde | 2024 | `` |
| [LOCKED] | `dbe-mathematics-g12-p2-2024-may` | mathematics | 2024 | `` |
| [LOCKED] | `dbe-wiskunde-g12-v2-2024-may` | wiskunde | 2024 | `` |
| [LOCKED] | `dbe-physical_sciences-g12-p1-2024-may` | physical | 2024 | `` |
| [LOCKED] | `dbe-fisiese_wetenskappe-g12-v1-2024-may` | fisiese | 2024 | `` |
| [LOCKED] | `dbe-physical_sciences-g12-p2-2024-may` | physical | 2024 | `` |
| [LOCKED] | `dbe-fisiese_wetenskappe-g12-v2-2024-may` | fisiese | 2024 | `` |
