import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("workspace/text/dbe-physical_sciences-g12-p1-2021-nov.txt", "r", encoding="utf-8") as f:
    qp_lines = f.readlines()

for i, line in enumerate(qp_lines[710:760], 711):
    print(f"{i}: {line}", end="")
