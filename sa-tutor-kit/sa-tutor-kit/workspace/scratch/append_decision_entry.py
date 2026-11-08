# -*- coding: utf-8 -*-
import sys

entry = '''
## 2026-11-05: Extraction of DBE Afrikaans Huistaal Graad 12 Vraestel 2 November 2025 (UDVES Standard)
- **Document Pair:** `dbe-afrikaans_hl-g12-p2-2025-nov` / `dbe-afrikaans_hl-g12-p2-2025-nov-memo`.
- **Subject / Track:** `afrikaans_hl` / `languages_hl` (Graad 12 Letterkunde: Voorgeskrewe Poësie, Ongesiene Poësie, Roman, Drama).
- **Core Principles & Comprehensive Literary Preservation:**
  - **100% Faithfulness & Memorandum Ground Truth:** Sliced questions at atomic subquestion levels across all 17 questions and elective setworks (Questions 1 to 17), covering prescribed poems ('27 april 1994', 'Briefie aan Madiba', ''n Paternoster vir Suid-Afrika', 'Suiwer wiskunde'), unseen poem ('Ek is my ma se kind'), novels (*Onderwêreld*, *Manaka Plek van die Horings*, *Vatmaar*, *Die kwart-voor-sewe-lelie*), and dramas (*Krismis van Map Jacobs*, *Mis*).
  - **Self-Contained Literary Passages:** Every atomic contextual question embeds the complete verbatim extract (Tekste A tot L) with contextual header, line numbers, and scene/chapter attribution. Every poetry item embeds the full poem text with original line numbers.
  - **Literary Essay Rubrics & Detailed Marking Guidance:** Every literary essay question (Questions 1, 6, 8, 10, 12, 14, 16) embeds the essay prompt, context, full bulleted marking points (argumente, motiverings, aanhalings en bladsyverwysings), and official DBE assessment rubrics (Poësie 10-punt rubriek, Roman & Drama 25-punt rubriek met Inhoud en Struktuur & Taal kriteria).
  - **Full Document Recovery via PyMuPDF Inspection:** Truncated legacy text files (`dbe-afrikaans_hl-g12-p2-2025-nov.txt` cut off at Q9 and `dbe-afrikaans_hl-g12-p2-2025-nov-memo.txt` cut off at Q6) were fully recovered by rendering all 31 pages of the official Question Paper PDF and all 52 pages of the Marking Guidelines PDF, restoring all missing questions (Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17). Full text files saved to `workspace/text/dbe-afrikaans_hl-g12-p2-2025-nov-full.txt` and `workspace/text/dbe-afrikaans_hl-g12-p2-2025-nov-memo-full.txt`.
  - **Strict KaTeX & Standards Compliance:**
    - Standardized KaTeX notation throughout; checkmarks formatted as `$\\checkmark$`.
    - 0 unclosed dollar delimiters, 0 syntax errors.
- **Section & Question Breakdown (104 Atomic Items, 350 Marks Total Available Across All Electives, Exactly 80 Marks Official Candidate Requirement):**
  - **Afdeling A: Poësie (50 punte beskikbaar, kandidaat kies 2 gesiene gedigte + 1 verpligte ongesiene gedig = 30 punte, 25 items):**
    - Vraag 1: "27 april 1994" (Vincent Oliphant) – Literêre Opstel (10 punte, 1 item).
    - Vraag 2: "Briefie aan Madiba" (Sandra O'Kelly) – Kontekstueel (10 punte, 6 items): 2.1 (3), 2.2.1 (1), 2.2.2 (2), 2.3 (2), 2.4 (1), 2.5 (1).
    - Vraag 3: "'n Paternoster vir Suid-Afrika" (Lina Spies) – Kontekstueel (10 punte, 6 items): 3.1 (1), 3.2 (2), 3.3 (2), 3.4 (1), 3.5 (1), 3.6 (3).
    - Vraag 4: "Suiwer wiskunde" (N.P. van Wyk Louw) – Kontekstueel (10 punte, 6 items): 4.1 (2), 4.2 (1), 4.3 (2), 4.4 (3), 4.5 (1), 4.6 (1).
    - Vraag 5: "Ek is my ma se kind" (Danelle Jacobs) – Ongesiene Poësie Kontekstueel (10 punte, 6 items): 5.1 (2), 5.2 (3), 5.3 (1), 5.4 (2), 5.5 (1), 5.6 (1).
  - **Afdeling B: Roman (200 punte beskikbaar, kandidaat kies 1 vraag = 25 punte, 51 items):**
    - Vraag 6: *Onderwêreld* (Fanie Viljoen) – Literêre Opstel (25 punte, 1 item).
    - Vraag 7: *Onderwêreld* – Kontekstueel (Tekste A & B) (25 punte, 11 items): 7.1 (2), 7.2 (4), 7.3 (3), 7.4 (3), 7.5 (2), 7.6 (1), 7.7.1 (3), 7.7.2 (2), 7.8 (1), 7.9 (2), 7.10 (2).
    - Vraag 8: *Manaka Plek van die Horings* (Pieter Pieterse) – Literêre Opstel (25 punte, 1 item).
    - Vraag 9: *Manaka Plek van die Horings* – Kontekstueel (Tekste C & D) (25 punte, 11 items): 9.1 (1), 9.2 (4), 9.3 (2), 9.4 (3), 9.5 (2), 9.6 (3), 9.7 (2), 9.8 (1), 9.9 (3), 9.10 (2), 9.11 (2).
    - Vraag 10: *Vatmaar* (A.H.M. Scholtz) – Literêre Opstel (25 punte, 1 item).
    - Vraag 11: *Vatmaar* – Kontekstueel (Tekste E & F) (25 punte, 13 items): 11.1 (2), 11.2.1 (2), 11.2.2 (3), 11.3 (2), 11.4 (1), 11.5 (1), 11.6 (3), 11.7 (2), 11.8 (2), 11.9 (1), 11.10 (4), 11.11 (1), 11.12 (1).
    - Vraag 12: *Die kwart-voor-sewe-lelie* (Eleanor Baker) – Literêre Opstel (25 punte, 1 item).
    - Vraag 13: *Die kwart-voor-sewe-lelie* – Kontekstueel (Tekste G & H) (25 punte, 12 items): 13.1 (1), 13.2 (2), 13.3 (3), 13.4.1 (3), 13.4.2 (3), 13.5 (2), 13.6 (1), 13.7.1 (2), 13.7.2 (1), 13.8 (4), 13.9 (2), 13.10 (1).
  - **Afdeling C: Drama (100 punte beskikbaar, kandidaat kies 1 vraag = 25 punte, 28 items):**
    - Vraag 14: *Krismis van Map Jacobs* (Adam Small) – Literêre Opstel (25 punte, 1 item).
    - Vraag 15: *Krismis van Map Jacobs* – Kontekstueel (Tekste I & J) (25 punte, 14 items): 15.1 (1), 15.2 (1), 15.3.1 (1), 15.3.2 (2), 15.4 (2), 15.5 (2), 15.6.1 (2), 15.6.2 (1), 15.7 (2), 15.8 (1), 15.9 (1), 15.10 (2), 15.11 (4), 15.12 (3).
    - Vraag 16: *Mis* (Reza de Wet) – Literêre Opstel (25 punte, 1 item).
    - Vraag 17: *Mis* – Kontekstueel (Tekste K & L) (25 punte, 12 items): 17.1 (1), 17.2 (1), 17.3.1 (1), 17.3.2 (2), 17.4 (2), 17.5 (3), 17.6 (1), 17.7 (4), 17.8 (3), 17.9.1 (2), 17.9.2 (2), 17.10 (3).
- **Verification Metrics:**
  - **Total Items Extracted:** Exactly 104 atomic items.
  - **Official Candidate Exam Total:** Exactly 80 marks (Afdeling A: 30 + Afdeling B: 25 + Afdeling C: 25 = 80). Total marks across all elective options: 350 marks.
  - **Needs Review:** 0 items flagged `needs_review: true`.
  - **KaTeX Syntax:** 0 delimiter errors, 100% balanced `$`.
- **Storage:** Dual-mirrored across:
  - `sa-tutor-kit/sa-tutor-kit/workspace/items/afrikaans_hl/dbe-afrikaans_hl-g12-p2-2025-nov.jsonl`
  - `sa-tutor-kit/sa-tutor-kit/workspace/items/dbe-afrikaans_hl-g12-p2-2025-nov.jsonl`
  - `workspace/items/afrikaans_hl/dbe-afrikaans_hl-g12-p2-2025-nov.jsonl`
  - `workspace/items/dbe-afrikaans_hl-g12-p2-2025-nov.jsonl`
'''

for dec_file in [
    'sa-tutor-kit/sa-tutor-kit/workspace/DECISIONS.md',
    'workspace/DECISIONS.md'
]:
    with open(dec_file, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'dbe-afrikaans_hl-g12-p2-2025-nov' not in content:
        with open(dec_file, 'a', encoding='utf-8') as f:
            f.write(entry)
        print(f'Appended to {dec_file}')
    else:
        print(f'Already present in {dec_file}')
