from PIL import Image
from pdf2image import convert_from_path

print("Welcome to PDF Thresholder!")

print("you should locate the target pdf file with the python script!")
name = input("please enter the name of pdf file without extension:") + ".pdf"
threshold = 140 #input("enter the threshold value (140 is recommended): ")
dpi = 200

cols = 2
rows = 4

images = convert_from_path(name, dpi=dpi, grayscale=True)

width = images[0].size[0]
height = images[0].size[1]

np = int(len(images)/8)
if(len(images)%8 > 0):
    np += 1

pgs = []
im = 0

for p in range(np):
    pgs.append(Image.new(mode="RGB", size=(cols * width, rows * height), color=(255, 255, 255)))

while im < len(images):
    images[im] = images[im].point( lambda p: 255 if p> 130 else 0)
    pgs[int(im/8)].paste(images[im],((int(im%cols))*width,(int(im/cols)%rows)*height))

    im +=1

pgs[0].save("outputs/" + name, save_all=True, append_images=pgs[1:])
