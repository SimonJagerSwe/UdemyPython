########## IMAGE CONVERTER ##########
import sys
import os
from PIL import Image

# Grabbing two arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# Check if \new exists, if not, create it 
# print(os.path.exists(output_folder))
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through Images
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    # print(clean_name)

# Convert to png
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('All done!')