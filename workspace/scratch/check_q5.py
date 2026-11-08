with open('build_p2_2023_may.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the missing dollar in Q5_PASSAGE
fixed_text = text.replace(r"$(700, 60)]", r"$(700, 60)$]")
if fixed_text != text:
    print("Replaced $(700, 60)] with $(700, 60)$]")
    with open('build_p2_2023_may.py', 'w', encoding='utf-8') as f:
        f.write(fixed_text)
else:
    print("Target string not found!")
