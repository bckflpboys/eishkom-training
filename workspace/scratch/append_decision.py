# -*- coding: utf-8 -*-
decision = '''

---

### Phase 2 Wave 9 Extraction: dbe-afrikaans_hl-g12-p1-2019-nov (November 2019 Afrikaans Huistaal V1)
- **Status:** COMPLETED & VERIFIED
- **Source ID:** dbe-afrikaans_hl-g12-p1-2019-nov
- **Paired Memo ID:** dbe-afrikaans_hl-g12-p1-2019-nov-memo
- **Subject:** afrikaans_hl | **Grade:** 12 | **Language:** af | **Track:** languages_hl
- **Output Files:**
  - `workspace/items/afrikaans_hl/dbe-afrikaans_hl-g12-p1-2019-nov.jsonl`
  - `workspace/items/dbe-afrikaans_hl-g12-p1-2019-nov.jsonl`
- **Reconciliation & Visual Recovery:**
  - **Afdeling A (Leesbegrip - 30 punte):**
    - **TEKS A (Artikel):** "IS AFRIKAANSE MUSIEK REGTIG SO VROT?" deur Johan Myburg. All 9 paragraphs captured verbatim. Underlined portion identified on official exam PDF page 3 for question 1.6: *"En nou, sewe jaar later, word steeds briewe hieroor geskryf,"*.
    - **TEKS B (Visuele Teks / Spotprent):** Visual description of the cartoon singer with microphone, musical notes, "EK [hartjie] AFRIKAANS" T-shirt, Spraakborrel 1 ("Jou oë is so blou, my baby, jou soene is so flou, my lovie ...") and Spraakborrel 2 ("Goeie musiek móét rym en 'n lewendige ritme hê en móét vol metafore wees!").
    - **Questions 1.1 to 1.16:** Atomic breakdown, including 1.8.1 and 1.8.2 split, totaling 30 marks.
  - **Afdeling B (Opsomming - 10 punte):**
    - **TEKS C:** "OOM OLIFANT, JOU REUSEDIER" (Hennie van Deventer). Full reading text provided, with 7 facts (7 marks) + language (3 marks) rubrics and criteria, plus sample 78-word summary in final_answer.
  - **Afdeling C (Taalstrukture en -konvensies - 30 punte):**
    - **Vraag 3 (Advertensie - TEKS D):** 8 items (3.1 to 3.8) = 10 marks (2 + 1 + 1 + 1 + 1 + 1 + 1 + 2). Reconstructed all line numbers (1–20) and verified underlined words (*verandering*, *KIES*).
    - **Vraag 4 (Strokiesprent - TEKS E):** 8 items (4.1 to 4.8) = 10 marks (2 + 1 + 1 + 2 + 1 + 1 + 1 + 1). Reconstructed dialogue across all 8 frames for Jerome and his mother/Ravi, with all underlined targets (*ek sit met 'n truksvy!*, *ek tel jou op vir 'n koffietjie*, *Ravi, jy klink anders.*, *Dit laat jou stem eggo.*, *skoorsoek*, *Geniet*).
    - **Vraag 5 (Artikel - TEKS F):** 8 items (5.1 to 5.8) = 10 marks (1 + 1 + 1 + 1 + 1 + 2 + 2 + 1). Full 9-paragraph text with underlined features (*vierpotige*, *Ek verorber álles.*, *eetding*, *deur die bank*, *wagwoord*).
- **Verification Metrics:**
  - **Total Items Extracted:** 42 atomic items.
  - **Total Marks Verified:** Exactly 70 / 70 marks (30 + 10 + 30 = 70).
  - **KaTeX Syntax:** 0 unclosed dollar signs across all fields. Strict balanced $..$ delimiters.
  - **Needs Review:** 0 items flagged needs_review: false.
  - **Dual Mirror:** Persisted to both subject-specific folder and flat root items folder.
'''

with open('workspace/DECISIONS.md', 'a', encoding='utf-8') as f:
    f.write(decision)

print('Successfully appended to DECISIONS.md!')
