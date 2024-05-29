########## IMAGES ##########
from PIL import Image, ImageFilter

# Some methods
img = Image.open('./images/pikachu.jpg')
print(img)
print(img.format)
print(img.size)
print(img.mode)
print(dir(img))


# Using filter
filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save('blur.png', 'png')