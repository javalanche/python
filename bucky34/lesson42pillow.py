from PIL import Image

img = Image.open("279.jpg")
print(img.size)
print(img.format)

#img.show()

area = (100,100,300, 375)

cropped_img = img.crop(area)
cropped_img.show()
