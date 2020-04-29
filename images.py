from PIL import Image, ImageFilter

# Get the image and save it in a variable
img = Image.open('./pokedex/pikachu.jpg')
# Add the relevant effect to it using ImageFilter
filtered_img = img.filter(ImageFilter.BLUR)
# Rotate the image
crooked = filtered_img.rotate(90)
# Resize the image - the dimensions should be passed in as a tuple
resized = filtered_img.resize((300, 300))
# Crop images - specify the regions where we want to crop
box = (100, 100, 400, 400)
cropped = filtered_img.crop(box)
# Save it - specify the filename followed by the format
filtered_img.save('pikachu-blur.png', 'png')
# Resize but keep the aspect ratio - just call thumbnail on the img, but don't save in a variable
img.thumbnail((400, 400))
img.save('thumbnail.jpg', 'jpg')
