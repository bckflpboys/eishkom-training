from PIL import Image

for p, name in [(9, "crop_q3"), (10, "crop_q4"), (11, "crop_q5")]:
    im = Image.open(f"workspace/scratch/page_{p}.png")
    w, h = im.size
    crop = im.crop((0, int(h * 0.05), w, int(h * 0.55)))
    crop.save(f"workspace/scratch/{name}.png")
print("Cropped Q3, Q4, Q5")
