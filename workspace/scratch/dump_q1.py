import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("workspace/scratch/qp_dump.txt", "r", encoding="utf-8") as f:
    qp = f.read()

pos1 = qp.find("QUESTION 1")
pos2 = qp.find("QUESTION 2 (Start")
print(f"pos1={pos1}, pos2={pos2}")
print(qp[pos1:pos2])
