########## IMAGES ##########
from PIL import Image, ImageFilter

# Some methods
img = Image.open('./images/pikachu.jpg')
print(img)
print(img.format)
print(img.size)
print(img.mode)
# print(dir(img))


# Using BLUR filter
filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save('blur.png', 'png')


# Converting
grey_img = img.convert('L')
grey_img.save('grey.png', 'png')


# Showing
filtered_image.show()


# Rotating
crooked_img = grey_img.rotate(90)
crooked_img.save('crooked.png', 'png')
crooked_img.show()