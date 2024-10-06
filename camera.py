#! /usr/bin/python

import time
from datetime import datetime
import os
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import st7789
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
import libcamera


buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

spi = board.SPI()

disp = st7789.ST7789(
    spi,
    cs=digitalio.DigitalInOut(board.CE0),
    dc=digitalio.DigitalInOut(board.D25),
    rst=None,
    baudrate=64000000,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

height = disp.height
width = disp.width
image = Image.new("RGB", (width, height))
rotation = 0

draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
padding = -2
top = padding
bottom = height - padding
x = 0

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

picam2 = Picamera2()
video_config = picam2.create_video_configuration(main={"size": (1600, 1200)})
video_config["transform"] = libcamera.Transform(hflip=1, vflip=1)
encoder = H264Encoder(10000000)
still_config = picam2.create_still_configuration(main={"size": (2592, 1944)})
still_config["transform"] = libcamera.Transform(hflip=1, vflip=1)
recording = False
last_picture = "none"

try:
    while not (not buttonA.value and not buttonB.value):
        if not buttonA.value:
            if not recording:
                picam2.configure(video_config)
                recording = True
                picam2.start_recording(encoder, f'/home/curt/Videos/{datetime.now().strftime("%Y.%m.%d.%H.%M.%S")}.h264')
            else:
                recording = False
                picam2.stop_recording()

        if not buttonB.value:
            picam2.configure(still_config)
            picam2.start()
            last_picture = str(datetime.now().strftime("%Y.%m.%d.%H.%M.%S"))
            picam2.capture_file(f'/home/curt/Pictures/{last_picture}.jpg')
            picam2.stop()

        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        y = top
        lines = ['record:', str(recording)," ", "last pic:", last_picture[:10], last_picture[11:], " ", " ", str(buttonB.value)]

        for line in lines:
            draw.text((x, y), line, font=font, fill="#FFFFFF")
            y += font.getbbox(line)[-1]

        disp.image(image, rotation)
        time.sleep(0.1)
    os.system("sudo shutdown now")


except KeyboardInterrupt:
    backlight.value = False
    print()
