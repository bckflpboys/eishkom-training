# restore_memo_text.py
import json

with open("sa-tutor-kit/sa-tutor-kit/workspace/items/mathematics/dbe-mathematics-g12-p2-2025-may.jsonl", "r", encoding="utf-8") as f:
    items = [json.loads(line) for line in f]

header = """# NATIONAL SENIOR CERTIFICATE / NASIONALE SENIOR SERTIFIKAAT

**GRADE 12 / GRAAD 12**

## MATHEMATICS P2 / WISKUNDE V2
**MAY/JUNE 2025**
**MARKING GUIDELINES / NASIENRIGLYNE**

**MARKS / PUNTE: 150**

---

### NOTE:
* If a candidate answers a question TWICE, only mark the FIRST attempt.
* If a candidate has crossed out an attempt of a question and not redone the question, mark the crossed-out version.
* Consistent accuracy applies in ALL aspects of the Marking Guidelines. Stop marking at the second calculation error.
* Assuming answers/values in order to solve a problem is NOT acceptable.

---

| GEOMETRY • MEETKUNDE |
| :--- |
| **S** | A mark for a correct statement (independent of a reason) |
| **R** | A mark for the correct reason (may only be awarded if statement is correct) |
| **S/R** | Award a mark if statement AND reason are both correct |

---
"""

content = header

curr_q = None
for item in items:
    q_num = item["question_ref"].split(".")[0]
    if q_num != curr_q:
        curr_q = q_num
        content += f"\n## QUESTION {curr_q}\n\n"
    
    content += f"### {item['question_ref']} ({item['marks']} mark{'s' if item['marks'] > 1 else ''})\n\n"
    if item["passage"]:
        content += f"**Passage / Context:**\n{item['passage']}\n\n"
    content += f"**Question:**\n{item['question']}\n\n"
    content += f"**Marking Guideline:**\n{item['memo']}\n\n"
    content += f"**Final Answer:** {item['final_answer']}\n\n"
    content += "---\n\n"

memo_path = "sa-tutor-kit/sa-tutor-kit/workspace/text/dbe-mathematics-g12-p2-2025-may-memo.txt"
with open(memo_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Restored {memo_path} ({len(content)} characters, {len(content.splitlines())} lines)")
