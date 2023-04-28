# lcd-image-converter
Convert Images Into Hex

This is a program that takes an image file and converts it to a hex image format. If you're programming an Arduino and use a 256 RGB LEDs Matrix or something similar you may want to display images or even animations. 

In Arduino you can declare a costant array such as:
 > const long Marioc[] PROGMEM =  {0x000000,0x000000,0x000000, ... }

Then using the FastLED library you can load this into the screen. The probelm is that most images, png's, jpgs aren't in hex format and most editing tools won't output this format either. In particular the LCD matrix will wind back and forth meaning that every other row has to be reversed. 

This python file does exactly that. It reads a file as a parameter, opens the file, converts it to hex and flips every other row. 

This will produce the images for the pac1.png sample. 
> python convert.py pac1.png

This will also work for a sprite sheet that contains multiple images
> python convert.py pac123.png > samplefile.txt 

