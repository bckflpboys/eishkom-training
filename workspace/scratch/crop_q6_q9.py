from PIL import Image

im9 = Image.open("workspace/scratch/page_15.png")
w, h = im9.size
crop_q9 = im9.crop((0, int(h * 0.05), w, int(h * 0.6)))
crop_q9.save("workspace/scratch/crop_q9.png")

im6 = Image.open("workspace/scratch/page_12.png")
w, h = im6.size
crop_q6 = im6.crop((0, int(h * 0.05), w, int(h * 0.5)))
crop_q6.save("workspace/scratch/crop_q6.png")
print("Cropped Q9 and Q6")
