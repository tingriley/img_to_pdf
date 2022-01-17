from PIL import Image
imagelist = []
im1 = []
for i in range(1, 10):
    name = "img" + str(i) + ".png" 
    image1 = Image.open(name)
    print(name)
    im1 = image1.convert('RGB')

    imagelist.append(im1)

im1.save('mergePDF.pdf',save_all=True, append_images=imagelist)
