import sys
import os
from PIL import Image

# Grab first and second argument (JPGtoPNGconverter.py\[0] Pokedex\[1] new\[2])
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# Check if /new exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through /Pokedex and convert images to PNG
for filename in os.listdir(image_folder):
    # This gets the file in the image_folder location, but the files have the .jpg extension, which we need to remove
    img = Image.open(f'{image_folder}{filename}')
    # Remove the .jpg extension - splitext splits the text from the extension and puts them in a tuple
    # We them want the first item in the tuple
    clean_name = os.path.splitext(filename)[0]
    # Save to the /new location
    img.save(f'{output_folder}{clean_name}.png', 'png')

# Finally, we run the command python JPGtoPNGconverter.py pokedex/ new/
