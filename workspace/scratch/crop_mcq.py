from PIL import Image

im = Image.open("workspace/scratch/page_4.png")
# Let's crop question 1.3
# page dimensions
w, h = im.size
crop_1_3 = im.crop((0, int(h * 0.1), w, int(h * 0.55)))
crop_1_3.save("workspace/scratch/crop_1_3.png")

crop_1_4 = im.crop((0, int(h * 0.55), w, h))
crop_1_4.save("workspace/scratch/crop_1_4.png")
print("Cropped 1.3 and 1.4")
