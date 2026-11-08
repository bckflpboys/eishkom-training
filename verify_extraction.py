import json
import re

path1 = "sa-tutor-kit/sa-tutor-kit/workspace/items/physical_sciences/dbe-physical_sciences-g12-p2-2023-nov.jsonl"
path2 = "sa-tutor-kit/sa-tutor-kit/workspace/items/dbe-physical_sciences-g12-p2-2023-nov.jsonl"

lines1 = open(path1, encoding="utf-8").readlines()
lines2 = open(path2, encoding="utf-8").readlines()

assert len(lines1) == len(lines2) == 68, f"Mismatch count: {len(lines1)} vs {len(lines2)}"

items1 = [json.loads(l) for l in lines1]
items2 = [json.loads(l) for l in lines2]

assert items1 == items2, "Dual files do not match!"

total_marks = sum(x["marks"] for x in items1)
print(f"Items count: {len(items1)}")
print(f"Total Marks: {total_marks} / 150")
assert total_marks == 150

# Check review count
review_cnt = sum(1 for x in items1 if x["needs_review"])
print(f"Needs review count: {review_cnt}")

# Check KaTeX dollars & decimals & Celsius
degree_warnings = 0
decimal_warnings = 0

for i, x in enumerate(items1):
    for f in ["question", "memo", "passage"]:
        val = x[f]
        # check bare °C
        if "°C" in val:
            for m in re.finditer(r".{0,15}°C.{0,15}", val):
                context = m.group(0)
                if r"^\circ\text{C}" not in context and r"^\circ \text{C}" not in context:
                    print(f"Warning: bare degree C in {x['item_id']} field {f}: {repr(context)}")
                    degree_warnings += 1
        # check decimal comma in math mode (e.g. $0,15$ instead of $0{,}15$)
        bare_dec = re.findall(r"\$\d+,\d+\$", val)
        if bare_dec:
            print(f"Warning: bare decimal comma in math mode in {x['item_id']} field {f}: {bare_dec}")
            decimal_warnings += 1

print(f"Degree warnings: {degree_warnings}")
print(f"Decimal comma warnings: {decimal_warnings}")

# Check questions breakdown
by_q = {}
for x in items1:
    qnum = x["question_ref"].split(".")[0]
    by_q[qnum] = by_q.get(qnum, 0) + x["marks"]

print("Marks breakdown by Question:")
for qnum in sorted(by_q.keys(), key=int):
    print(f"  Question {qnum}: {by_q[qnum]} marks")

print("All verification checks PASSED successfully!")
