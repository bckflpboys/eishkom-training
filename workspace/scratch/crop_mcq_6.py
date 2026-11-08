from PIL import Image

im = Image.open("workspace/scratch/page_6.png")
w, h = im.size
crop_1_7_8 = im.crop((0, int(h * 0.05), w, int(h * 0.95)))
crop_1_7_8.save("workspace/scratch/crop_1_7_8.png")
print("Cropped 1.7 and 1.8")
