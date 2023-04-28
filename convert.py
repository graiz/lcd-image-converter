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
filename = filename.rsplit('/', 1)[-1].rsplit('.', 1)[0]

# Convert the image to RGB mode
rgb_im = image.convert('RGB')

# Get the image width and height
width, height = rgb_im.size

# Calculate the number of frames
frames = width // height

# Iterate through each frame
for frame in range(frames):
    # Create an empty list to store the pixel values
    pixel_values = []

    # Loop through the image pixels and get the RGB values for the current frame
    for y in range(height):
        row = []
        for x in range(frame * height, (frame + 1) * height):
            r, g, b = rgb_im.getpixel((x, y))
            hexrgb = rgb2hex(r, g, b)
            row.append("0x" + hexrgb[1:])
        if ((y % 2) == 0):
            row = list(reversed(row))
        pixel_values = pixel_values + row

    # Print the list of pixel values for the current frame
    print("const long " + filename + str(frame) + "[] PROGMEM = {", end='')
    for i, z in enumerate(pixel_values):
        print(z, end='')
        if i < len(pixel_values) - 1:
            print(',', end='')

    print("};")