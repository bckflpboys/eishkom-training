from PIL import Image

im = Image.open("workspace/scratch/page_5.png")
w, h = im.size
crop_1_5 = im.crop((0, int(h * 0.1), w, int(h * 0.52)))
crop_1_5.save("workspace/scratch/crop_1_5.png")

crop_1_6 = im.crop((0, int(h * 0.52), w, h))
crop_1_6.save("workspace/scratch/crop_1_6.png")
print("Cropped 1.5 and 1.6")
