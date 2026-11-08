entry = """

### 2026-11-05: Extraction of DBE English Home Language Grade 12 Paper 2 November 2025 (UDVES Standard)
- **Document Pair:** `dbe-english_hl-g12-p2-2025-nov` / `dbe-english_hl-g12-p2-2025-nov-memo`.
- **Subject / Track:** `english_hl` / `languages_hl` (Grade 12 Literature: Prescribed Poetry, Unseen Poetry, Novel, Drama).
- **Core Principles & Comprehensive Literary Preservation:**
  - **100% Faithfulness & Memorandum Ground Truth:** Sliced questions at atomic subquestion levels across all 15 questions and elective setworks (Questions 1 to 15), covering prescribed poems ('Solitude', 'It is a Beauteous Evening, Calm and Free', 'Poem of Return', 'This Winter Coming'), unseen poem ('The Trees'), novels (*The Picture of Dorian Gray*, *Life of Pi*), and dramas (*Hamlet*, *Othello*, *The Crucible*).
  - **Self-Contained Literary Passages:** Every atomic contextual question embeds the complete verbatim extract (Extracts A to J) with contextual header, line numbers, and scene/chapter attribution. Every poetry item embeds the full poem text.
  - **Literary Essay Rubrics & Detailed Marking Guidance:** Every literary essay question (Questions 1, 6, 8, 10, 12, 14) embeds the essay prompt, context, full bulleted marking points (Valid / Invalid arguments), and official DBE assessment rubrics (Poetry 10-mark rubric, Novel & Drama 25-mark rubric with Content and Structure & Language criteria).
  - **Full Document Recovery via PyMuPDF Inspection:** Truncated legacy text files (`dbe-english_hl-g12-p2-2025-nov.txt` cut off at Q13 and `dbe-english_hl-g12-p2-2025-nov-memo.txt` cut off at Q11.6) were fully recovered by rendering all 28 pages of the official Question Paper PDF and all 27 pages of the Marking Guidelines PDF, restoring all missing questions (11.7–11.10, Q12, Q13, Q14, Q15). Full text files saved to `workspace/text/dbe-english_hl-g12-p2-2025-nov-full.txt` and `workspace/text/dbe-english_hl-g12-p2-2025-nov-memo-full.txt`.
  - **Strict KaTeX & Standards Compliance:**
    - Standardized KaTeX notation throughout.
    - 0 unclosed dollar delimiters, 0 syntax errors.
- **Section & Question Breakdown (77 Atomic Items, 300 Marks Total Available Across All Electives, Exactly 80 Marks Official Candidate Requirement):**
  - **Section A: Poetry (50 marks available, candidate chooses 2 prescribed + 1 compulsory unseen = 30 marks, 22 items):**
    - Question 1: 'Solitude' (Ella Wheeler Wilcox) — Literary Essay (10 marks, 1 item).
    - Question 2: 'It is a Beauteous Evening, Calm and Free' (William Wordsworth) — Contextual (10 marks, 5 items): 2.1 (2), 2.2 (2), 2.3.1 (1), 2.3.2 (2), 2.4 (3).
    - Question 3: 'Poem of Return' (Jofre Rocha) — Contextual (10 marks, 5 items): 3.1 (2), 3.2 (2), 3.3.1 (1), 3.3.2 (2), 3.4 (3).
    - Question 4: 'This Winter Coming' (Karen Press) — Contextual (10 marks, 5 items): 4.1 (2), 4.2 (2), 4.3.1 (1), 4.3.2 (2), 4.4 (3).
    - Question 5: 'The Trees' (Philip Larkin) — Unseen Poetry Contextual (10 marks, 6 items): 5.1 (2), 5.2 (2), 5.3.1 (1), 5.3.2 (2), 5.4.1 (1), 5.4.2 (2).
  - **Section B: Novel (100 marks available, candidate chooses 1 question = 25 marks, 22 items):**
    - Question 6: *The Picture of Dorian Gray* (Oscar Wilde) — Literary Essay (25 marks, 1 item).
    - Question 7: *The Picture of Dorian Gray* — Contextual (Extracts A & B) (25 marks, 10 items): 7.1 (2), 7.2 (2), 7.3 (2), 7.4 (3), 7.5 (3), 7.6 (2), 7.7 (2), 7.8 (3), 7.9 (3), 7.10 (3).
    - Question 8: *Life of Pi* (Yann Martel) — Literary Essay (25 marks, 1 item).
    - Question 9: *Life of Pi* — Contextual (Extracts C & D) (25 marks, 10 items): 9.1 (2), 9.2 (2), 9.3 (2), 9.4 (3), 9.5 (3), 9.6 (2), 9.7 (2), 9.8 (3), 9.9 (3), 9.10 (3).
  - **Section C: Drama (150 marks available, candidate chooses 1 question = 25 marks, 33 items):**
    - Question 10: *Hamlet* (William Shakespeare) — Literary Essay (25 marks, 1 item).
    - Question 11: *Hamlet* — Contextual (Extracts E & F) (25 marks, 10 items): 11.1 (2), 11.2 (2), 11.3 (2), 11.4 (3), 11.5 (3), 11.6 (2), 11.7 (2), 11.8 (3), 11.9 (3), 11.10 (3).
    - Question 12: *Othello* (William Shakespeare) — Literary Essay (25 marks, 1 item).
    - Question 13: *Othello* — Contextual (Extracts G & H) (25 marks, 10 items): 13.1 (2), 13.2 (2), 13.3 (2), 13.4 (3), 13.5 (3), 13.6 (2), 13.7 (2), 13.8 (3), 13.9 (3), 13.10 (3).
    - Question 14: *The Crucible* (Arthur Miller) — Literary Essay (25 marks, 1 item).
    - Question 15: *The Crucible* — Contextual (Extracts I & J) (25 marks, 10 items): 15.1 (2), 15.2 (2), 15.3 (2), 15.4 (3), 15.5 (3), 15.6 (2), 15.7 (2), 15.8 (3), 15.9 (3), 15.10 (3).
- **Verification Metrics:**
  - **Total Items Extracted:** Exactly 77 atomic items.
  - **Official Candidate Exam Total:** Exactly 80 marks ($30 + 25 + 25 = 80$). Total marks across all available curriculum electives: 300 marks.
  - **Needs Review:** 0 items flagged `needs_review: true`.
  - **KaTeX Syntax:** 0 delimiter errors, 100% balanced `$`.
- **Storage:** Dual-mirrored across:
  - `sa-tutor-kit/sa-tutor-kit/workspace/items/english_hl/dbe-english_hl-g12-p2-2025-nov.jsonl`
  - `sa-tutor-kit/sa-tutor-kit/workspace/items/dbe-english_hl-g12-p2-2025-nov.jsonl`
  - `workspace/items/english_hl/dbe-english_hl-g12-p2-2025-nov.jsonl`
  - `workspace/items/dbe-english_hl-g12-p2-2025-nov.jsonl`
"""

paths = [
    'sa-tutor-kit/sa-tutor-kit/workspace/DECISIONS.md',
    'workspace/DECISIONS.md'
]

for p in paths:
    with open(p, 'a', encoding='utf-8') as f:
        f.write(entry)
    print(f"Appended to {p}")
