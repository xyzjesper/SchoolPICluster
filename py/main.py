import time
import sys
import os
from pathlib import Path
from time import gmtime, strftime
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'drive')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging    
from drive import SSD1305

from PIL import Image,ImageDraw,ImageFont

import subprocess

# 128x32 display with hardware SPI:
disp = SSD1305.SSD1305()


# Initialize library.
disp.Init()

# Clear display.
logging.info("clear display")
disp.clear()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 0
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
#font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype('/root/display/04B_08__.TTF', size=16)
try:
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
        
    nameTXT = Path("/home/pi/name.txt")
    if (nameTXT.exists()):
        draw.text((x, top),     str(nameTXT.read_text()), font=font, fill=255)
        draw.text((x, top+16),       str(IP.decode('utf-8')),  font=font, fill=255)
    else:
        draw.text((x, top+16),       str(IP.decode('utf-8')),  font=font, fill=255)

    # Write two lines of text.
        

    # Display image.
    disp.getbuffer(image)
    disp.ShowImage()
    time.sleep(1)
except(KeyboardInterrupt):
    print("\n")
