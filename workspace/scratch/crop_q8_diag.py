from PIL import Image

im = Image.open("workspace/scratch/page_14.png")
w, h = im.size
crop_q8 = im.crop((0, int(h * 0.05), w, int(h * 0.55)))
crop_q8.save("workspace/scratch/crop_q8.png")
print("Cropped Q8")
