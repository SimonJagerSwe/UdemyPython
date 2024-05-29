########## IMAGES ##########
from PIL import Image

img = Image.open('./images/pikachu.jpg')
print(img)
print(img.format)
print(img.size)