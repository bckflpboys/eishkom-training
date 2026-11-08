import io, os

with open('workspace/EXTRACTION_TRACKER.md', 'r', encoding='utf-8') as f:
    tracker = f.read()

# Update header counts
tracker = tracker.replace(
    "**Verified Extracted Items:** **617 atomic items** across **13 papers** (1381 total marks verified)",
    "**Verified Extracted Items:** **665 atomic items** across **14 papers** (1461 total marks verified)"
)
tracker = tracker.replace(
    "| **Total Extracted Items** | **617 Items** |",
    "| **Total Extracted Items** | **665 Items** |"
)
tracker = tracker.replace(
    "| **Total Marks Accounted** | **1381 Marks** |",
    "| **Total Marks Accounted** | **1461 Marks** |"
)

# Update Wave 4 section
old_wave4_table = """## 5. Page 4: Wave 4 (Upcoming Lane Queue)

| Status | Source ID | Paired Memo ID | Subject | Expected Marks | Lane |
|:---:|---|---|---|:---:|:---:|
| [ ] | `dbe-mathematics-g12-p2-2022-nov` | `dbe-mathematics-g12-p2-2022-nov-memo` | mathematics | 150 | Lane Queue |
| [ ] | `dbe-physical_sciences-g12-p2-2022-nov` | `dbe-physical_sciences-g12-p2-2022-nov-memo` | physical | 150 | Lane Queue |
| [ ] | `dbe-english_hl-g12-p2-2022-nov` | `dbe-english_hl-g12-p2-2022-nov-memo` | english | 70 | Lane Queue |
| [ ] | `dbe-afrikaans_hl-g12-p2-2022-nov` | `dbe-afrikaans_hl-g12-p2-2022-nov-memo` | afrikaans | 70 | Lane Queue |"""

new_wave4_table = """## 5. Page 4: Wave 4 (Grade 12 Nov 2022 Additional Queue & Completed Lanes)

| Status | Source ID | Subject | Grade | Session | Items | Marks | KaTeX Errors | Flagged Review | Dual Mirror |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [x] | `dbe-english_fal-g12-p1-2022-nov` | english_fal | Gr 12 | 2022 Nov | **48** | **80/80** | 0 | 0 | Yes |

### Upcoming Wave 4 Lane Queue:
| Status | Source ID | Paired Memo ID | Subject | Expected Marks | Lane |
|:---:|---|---|---|:---:|:---:|
| [ ] | `dbe-mathematics-g12-p2-2022-nov` | `dbe-mathematics-g12-p2-2022-nov-memo` | mathematics | 150 | Lane Queue |
| [ ] | `dbe-physical_sciences-g12-p2-2022-nov` | `dbe-physical_sciences-g12-p2-2022-nov-memo` | physical | 150 | Lane Queue |
| [ ] | `dbe-english_hl-g12-p2-2022-nov` | `dbe-english_hl-g12-p2-2022-nov-memo` | english | 70 | Lane Queue |
| [ ] | `dbe-afrikaans_hl-g12-p2-2022-nov` | `dbe-afrikaans_hl-g12-p2-2022-nov-memo` | afrikaans | 70 | Lane Queue |"""

tracker = tracker.replace(old_wave4_table, new_wave4_table)

with open('workspace/EXTRACTION_TRACKER.md', 'w', encoding='utf-8') as f:
    f.write(tracker)
print("Updated EXTRACTION_TRACKER.md")

# Also update DECISIONS.md
with open('workspace/DECISIONS.md', 'r', encoding='utf-8') as f:
    decisions = f.read()

decision_addition = """
---

## 30. Wave 4 Extraction Milestone: English FAL P1 November 2022
- **Source ID:** `dbe-english_fal-g12-p1-2022-nov`
- **Paired Memo ID:** `dbe-english_fal-g12-p1-2022-nov-memo`
- **Subject / Track:** `english_fal` / `languages_fal`
- **Grade:** 12
- **Extraction Summary:**
  - **Section A (Comprehension):** 17 items (1.1.1 to 1.13), total 30 marks. Full Text A and Text B (Social Media Use bar graph + Wi-Fi symbol + laptop hashtag illustration) embedded in `passage`.
  - **Section B (Summary):** 1 item (Question 2), total 10 marks. Full Text C embedded in `passage`, quotation vs own words marking grid, and model 7-point summary (62 words) in `final_answer`.
  - **Section C (Language Structures and Conventions):** 30 items, total 40 marks:
    - **Question 3 (Advertisement):** 7 items (3.1 to 3.7), 10 marks. Cadbury Dairy Milk Bubbly parachute rabbit visual, body copy, and Joyville slogan in `passage`.
    - **Question 4 (Cartoon):** 7 items (4.1 to 4.7), 10 marks. Matt Against the World (6 frames) comprehensive panel-by-panel descriptions in `passage`.
    - **Question 5 (Language & Editing Skills):** 16 items (5.1.1a–d, 5.1.2–5.1.8, 5.2.1–5.2.5), 20 marks. Siya Kolisi text and Coffee Facts infographic in `passage`. Critical recovery: Question 5.1.6 underlined words verified via vector line analysis of raw PDF to be `team` and `and`, matching the official memo.
- **Verification Metrics:**
  - **Total Items Extracted:** 48 atomic items.
  - **Total Marks Verified:** Exactly 80 / 80 marks ($30 + 10 + 10 + 10 + 20 = 80$).
  - **KaTeX Delimiters:** 0 unclosed dollar signs across all fields.
  - **Needs Review:** 0 items flagged.
  - **Corpus Milestone:** Cumulative verified items increased to **665 items** across **14 papers** (**1,461 total marks verified**).
"""

if "Wave 4 Extraction Milestone: English FAL P1 November 2022" not in decisions:
    decisions += decision_addition
    with open('workspace/DECISIONS.md', 'w', encoding='utf-8') as f:
        f.write(decisions)
    print("Updated DECISIONS.md")

# Ensure internal mirrors are updated if they exist
internal_decisions = "sa-tutor-kit/sa-tutor-kit/workspace/DECISIONS.md"
if os.path.exists(internal_decisions) and not os.path.samefile("workspace/DECISIONS.md", internal_decisions):
    with open(internal_decisions, 'w', encoding='utf-8') as f:
        f.write(decisions)
    print("Updated internal DECISIONS.md")
