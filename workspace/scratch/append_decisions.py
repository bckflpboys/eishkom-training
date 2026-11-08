entry = """
---

### Phase 2 Wave 5 Extraction: `dbe-english_hl-g12-p1-2021-nov` (November 2021 English Home Language P1)
- **Status:** COMPLETED & VERIFIED
- **Source ID:** `dbe-english_hl-g12-p1-2021-nov`
- **Paired Memo ID:** `dbe-english_hl-g12-p1-2021-nov-memo`
- **Subject:** `english_hl` | **Grade:** 12 | **Language:** en | **Track:** `languages_hl`
- **Output Files:**
  - `workspace/items/english_hl/dbe-english_hl-g12-p1-2021-nov.jsonl`
  - `workspace/items/dbe-english_hl-g12-p1-2021-nov.jsonl`
- **Reconciliation & Visual Context Recovery:**
  - **Section A (Comprehension - 30 marks):**
    - Extracted 11 atomic items (1.1 to 1.11).
    - Embedded complete Text A ("The Old Have Made a Mess of the World. The Young Will Save Us.") with full paragraphs 1–9 and glossary.
    - Recovered detailed visual and political context for Text B (Zapiro satirical cartoon from Daily Maverick): David vs Goliath composition featuring a determined Greta Thunberg with slingshot armed with `#Action!` striking the towering, suit-wearing corporate giant labeled "GLOBAL ESTABLISHMENT" with the `#How Dare You!` projectile, causing him to topple over the cracked brink of the earth.
  - **Section B (Summary - 10 marks):**
    - Extracted 1 atomic item (Question 2) for 10 marks.
    - Embedded complete Text C ("Why Fake News on Social Media Travels Faster Than the Truth").
    - Reconciled 11 core summary points in memo table, official paragraph-form model summary (84 words), and strict marking grid for point allocation (7 marks), language distribution (3 marks), and verbatim quote penalties.
  - **Section C: Language in Context (30 marks):**
    - **Question 3 (Analysing Advertising - 10 marks):** 5 atomic items (3.1 to 3.5). Embedded complete Text D: Alpha Hospitals anti-bullying campaign ("Spot it and Stop it!"), headline, copy, white-on-dark action steps, and visual illustration description (silhouette employee cutting puppeteer strings to reclaim autonomy).
    - **Question 4 (Understanding Other Aspects of the Media - 10 marks):** 4 atomic items (4.1 to 4.4). Embedded complete Text E (Curtis 8-frame comic strip by Ray Billingsley with panel-by-panel descriptions of Curtis using deep voice, receiving rebuke, father explaining pandemic visiting policies, Curtis's forced optimism, and Frame 8 tearful hug) and Text F (Rogers single-panel cartoon satirizing narcissistic self-absorption on porch swing with hand mirror).
    - **Question 5 (Using Language Correctly - 10 marks):** 10 atomic items (5.1 to 5.10). Embedded complete Text G ("Instagram: Friend or Faux?") covering homophones, passive voice conversion, redundancy removal, acronym expansion, morphological derivation ('muscular'), past counterfactual tense correction, compound adjective hyphens, concord error correction ('are' to 'is'), apostrophe misuse, and formal register rewrite ('get real').
- **Verification Metrics:**
  - **Total Items Extracted:** 31 atomic items.
  - **Total Marks Verified:** Exactly 70 / 70 marks ($30 + 10 + 10 + 10 + 10 = 70$).
  - **KaTeX Delimiters:** 0 unclosed dollar signs across all fields.
  - **Needs Review:** 0 items flagged `needs_review: true`.
  - **Corpus Milestone:** Cumulative verified items increased to **830 items** across **17 papers** (**1,761 total marks verified**).
"""

with open("workspace/DECISIONS.md", "a", encoding="utf-8") as f:
    f.write(entry)
print("DECISIONS.md updated successfully.")
