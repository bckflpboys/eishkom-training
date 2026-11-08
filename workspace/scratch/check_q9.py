import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("workspace/text/dbe-physical_sciences-g12-p1-2021-nov-memo.txt", "r", encoding="utf-8") as f:
    memo_lines = f.readlines()

for i, line in enumerate(memo_lines[1870:1925], 1871):
    print(f"{i}: {line}", end="")
