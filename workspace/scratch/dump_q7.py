import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("workspace/scratch/qp_dump.txt", "r", encoding="utf-8") as f:
    qp = f.read()

with open("workspace/scratch/memo_dump.txt", "r", encoding="utf-8") as f:
    memo = f.read()

pos1 = qp.find("QUESTION 7 (Start")
pos2 = qp.find("QUESTION 8 (Start")
print("=== QUESTION 7 QP ===")
print(qp[pos1:pos2])

pos1_m = memo.find("QUESTION 7/VRAAG 7")
pos2_m = memo.find("QUESTION 8/VRAAG 8")
print("=== QUESTION 7 MEMO ===")
print(memo[pos1_m:pos2_m])
