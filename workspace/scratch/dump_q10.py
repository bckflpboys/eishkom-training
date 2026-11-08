import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("workspace/scratch/memo_dump.txt", "r", encoding="utf-8") as f:
    memo = f.read()

pos1_m = memo.find("QUESTION 10/VRAAG 10")
print("=== QUESTION 10 MEMO ===")
print(memo[pos1_m:])
