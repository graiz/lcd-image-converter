# Import the required modules
import sys
from PIL import Image
from colormap import rgb2hex

# Open the image file
try:
    image = Image.open(sys.argv[1])
except:
    print("Failed to open image file")
    sys.exit(1)

# Get the filename without the extension
filename = sys.argv[1].split('.')[0]


# Convert the image to RGB mode
rgb_im = image.convert('RGB')

# Get the image width and height
width, height = rgb_im.size

# Create an empty list to store the pixel values
pixel_values = []

r, g, b = rgb_im.getpixel((0, 0))
#print("red :" + str(r))
#print(str(int(f"{r:02x}{g:02x}", 16)))


# Loop through the image pixels and get the RGB values
for y in range(height):
    row = []
    for x in range(width):
        r, g, b = rgb_im.getpixel((x, y))
        hexrgb = rgb2hex(r,g,b)
        row.append("0x" + hexrgb[1:])
    if ((y % 2) == 0):
        row = list(reversed(row))
    pixel_values = pixel_values + row 

# Print the list of pixel values
print("const long " + filename + "[] PROGMEM = {", end='')
for i, z in enumerate(pixel_values):
    print(z, end='')
    if i < len(pixel_values) - 1:
        print(',', end='')

print("};")
