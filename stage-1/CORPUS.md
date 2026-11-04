# Eishkom Stage 1 — Phase 1 Corpus Inventory & Audit

> **Dataset Phase:** Phase 1 (Raw Sources Collection)  
> **Source Authority:** Department of Basic Education (DBE), Republic of South Africa (`education.gov.za`)  
> **Audit Date:** November 3, 2026  
> **Verification Status:** **100% Verified on Disk**  
> **Total Files:** **600 PDFs** (300 Question Paper + Memorandum Pairs)  
> **Total Disk Footprint:** **378.15 MB**  
> **Sources Ledger:** [`../sa-tutor-kit/sa-tutor-kit/workspace/sources/sources.csv`](../sa-tutor-kit/sa-tutor-kit/workspace/sources/sources.csv) (**604 entries**)

---

## 1. Corpus Architecture & Distribution

The raw PDFs are structured into strictly isolated language trees to ensure clean data segregation and prevent cross-contamination during parsing:

```
workspace/raw/dbe/
├── english/                         # 304 PDFs (152 Paper + Memo Pairs)
│   ├── english_fal/                 # 60 PDFs (Grade 12 NSC FAL P1 & P2, 2018–2025)
│   ├── english_hl/                  # 60 PDFs (Grade 12 NSC HL P1 & P2, 2018–2025)
│   ├── mathematics/                 # 92 PDFs (Grade 10–12 P1 & P2, 2015–2025)
│   └── physical_sciences/           # 92 PDFs (Grade 10–12 P1 & P2, 2015–2025)
└── afrikaans/                       # 296 PDFs (148 Paper + Memo Pairs)
    ├── afrikaans_fal/               # 60 PDFs (Graad 12 NSS EAT V1 & V2, 2018–2025)
    ├── afrikaans_hl/                # 60 PDFs (Graad 12 NSS HT V1 & V2, 2018–2025)
    ├── fisiese_wetenskappe/         # 88 PDFs (Graad 10–12 V1 & V2, 2015–2025)
    └── wiskunde/                    # 88 PDFs (Graad 10–12 V1 & V2, 2015–2025)
```

---

## 2. Subject Breakdown Table

| Subject (English / Afrikaans) | Grade Levels | Sessions Covered | English Files | Afrikaans Files | Total PDFs |
|---|---|---|---|---|---|
| **Mathematics / Wiskunde** | Grades 10, 11, 12 | Nov & May/June (2015–2025) | 92 | 88 | **180** |
| **Physical Sciences / Fisiese Wetenskappe** | Grades 10, 11, 12 | Nov & May/June (2015–2025) | 92 | 88 | **180** |
| **English Home Language / Huistaal** | Grade 12 NSC | Nov & May/June (2018–2025) | 60 | 60 | **120** |
| **English First Additional / EAT** | Grade 12 NSC | Nov & May/June (2018–2025) | 60 | 60 | **120** |
| **TOTALS** | **Grades 10–12** | **2015–2025** | **304** | **296** | **600** |

---

## 3. Paper-to-Memorandum Pairing Rules

In accordance with curriculum standards:
- **STEM Memos (Mathematics & Physical Sciences):** Memorandums are typically published bilingually (`Memo 1 (Afrikaans & English)`).
  - The English tree stores the memo as `<subject>_g<grade>_<year>_<session>_p<num>_memo.pdf`.
  - The Afrikaans tree stores the memo as `<af_sub>_g<grade>_<year>_<session>_v<num>_memo.pdf`.
  - Both language folders are completely standalone and self-contained.
- **Language Papers:** English HL, English FAL, Afrikaans HT, and Afrikaans EAT each pair their own distinct language question papers and marking guidelines.
- **Exclusion of Paper 3:** In accordance with the tutor specification, Paper 3 (creative writing / opstelle) is excluded, focusing models strictly on comprehension, language rules, literature analysis, mathematics, and science reasoning.

---

## 4. Evaluation Benchmark Lock (Zero Data Contamination)

To ensure trustworthy, scientifically sound evaluation of Stage 1 models:
- **All 16 question papers and memorandums from the November 2024 Grade 12 NSC examination session are strictly quarantined.**
- In [`sources.csv`](../sa-tutor-kit/sa-tutor-kit/workspace/sources/sources.csv), they are marked:
  ```csv
  notes: "held out for EVAL (do not train on it)"
  ```
- **Quarantined Papers:**
  1. `dbe-mathematics-g12-p1-2024-nov` (Mathematics P1 English)
  2. `dbe-mathematics-g12-p2-2024-nov` (Mathematics P2 English)
  3. `dbe-wiskunde-g12-v1-2024-nov` (Wiskunde V1 Afrikaans)
  4. `dbe-wiskunde-g12-v2-2024-nov` (Wiskunde V2 Afrikaans)
  5. `dbe-physical_sciences-g12-p1-2024-nov` (Physical Sciences P1 English)
  6. `dbe-physical_sciences-g12-p2-2024-nov` (Physical Sciences P2 English)
  7. `dbe-fisiese_wetenskappe-g12-v1-2024-nov` (Fisiese Wetenskappe V1 Afrikaans)
  8. `dbe-fisiese_wetenskappe-g12-v2-2024-nov` (Fisiese Wetenskappe V2 Afrikaans)
  9. `dbe-english_hl-g12-p1-2024-nov` (English HL P1)
  10. `dbe-english_hl-g12-p2-2024-nov` (English HL P2)
  11. `dbe-english_fal-g12-p1-2024-nov` (English FAL P1)
  12. `dbe-english_fal-g12-p2-2024-nov` (English FAL P2)
  13. `dbe-afrikaans_hl-g12-p1-2024-nov` (Afrikaans HL V1)
  14. `dbe-afrikaans_hl-g12-p2-2024-nov` (Afrikaans HL V2)
  15. `dbe-afrikaans_fal-g12-p1-2024-nov` (Afrikaans FAL V1)
  16. `dbe-afrikaans_fal-g12-p2-2024-nov` (Afrikaans FAL V2)
- None of these questions or marking guidelines will ever enter `workspace/build/` or be seen during fine-tuning. They are reserved exclusively for `workspace/eval/eval_items.jsonl`.

---

## 5. Phase 2 Ingested Text Corpus & Extraction Strategy

### Ingested Text Volumes (`workspace/text/`)

| Subject | Files | QP Chars | Memo Chars | Total Characters |
|---|---|---|---|---|
| **Mathematics** | 92 | 25,206 | 712,664 | 737,870 |
| **Wiskunde** | 88 | 25,051 | 674,870 | 699,921 |
| **Physical Sciences** | 92 | 865,659 | 1,235,355 | 2,101,014 |
| **Fisiese Wetenskappe** | 88 | 830,274 | 1,168,198 | 1,998,472 |
| **English Home Language** | 60 | 834,647 | 1,205,863 | 2,040,510 |
| **English First Additional** | 60 | 883,666 | 794,942 | 1,678,608 |
| **Afrikaans Huistaal** | 60 | 988,146 | 1,993,025 | 2,981,171 |
| **Afrikaans 1ste Addisionele** | 60 | 1,417,087 | 1,304,698 | 2,721,785 |
| **TOTALS** | **600** | **5,869,736** | **9,089,615** | **14,959,351** |

### Mathematical Equations & Diagrams Handling:
1. **Equations:** Formatted in LaTeX syntax inside `$..$` (inline) and `$$..$$` (display block).
2. **Text-Describable Diagrams (~20%):** Geometry circles, triangles, circuits, coordinate graphs are written out in the `"passage"` field (e.g. geometric points, parallel chords, tangent relationships).
3. **Pure Visual Diagrams (~10%):** Flagged `"needs_review": true`, excluded from text SFT, rendered to PNG images in `workspace/images/` for multimodal vision fine-tuning on `LiquidAI/LFM3-VL-2B` (`gariep-flash-stage-1`).
4. **Memo-First Question Recovery:** For the 87 Mathematics question papers where equations were rasterized in the QP PDF, the DBE marking memorandums contain the questions, sub-question numbers, steps, method marks, and answers in full digital text (over 1.38M characters combined). The extraction pipeline leverages memo text to recover these questions completely.


