import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("workspace/text/dbe-physical_sciences-g12-p1-2021-nov.txt", "r", encoding="utf-8") as f:
    text = f.read()

# find where QUESTION 10 appears
pos = text.find("QUESTION 10")
print(text[pos:pos+2500])
