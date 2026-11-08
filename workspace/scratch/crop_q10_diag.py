from PIL import Image

im = Image.open("workspace/scratch/page_17.png")
w, h = im.size
crop_q10 = im.crop((0, int(h * 0.05), w, int(h * 0.55)))
crop_q10.save("workspace/scratch/crop_q10.png")
print("Cropped Q10")
