import random

   from m5stack import M5Led
from m5stack import btnA
import time
from m5stack import speaker

import imu

import esp32 


def set_screen_color(r, g, b):
    print("Screen color set to {},{},{}".format(r, g, b))


def read_accelerometer(normalized=False):
    return random.random(), random.random(), random.random()


def print_to_screen(msg, x, y):
   output_msg = "Printing {} at {}, {}" .format(msg, x, y)
   print(output_msg) 


lcd.orient(lcd.LANDSCAPE)
width, height = lcd.screensize()
lcd.clear()
lcd.font(lcd.FONT_DejaVu56)
lcd.text (0, 0, str(width))
lcd.pixel(50, 50, 0x00FF00)

speaker.setVolume(20)
speaker.sing(220, 1)

stick_IMU = imu.IMU()

ax, ay, az = stick_IMU.acceleration
gx, gy, gz = stick_IMU.gyro

lcd.text(0, 100, str(ax))
lcd.text(0, 200, str(ax))

data = esp32.raw_temperature()


lcd.test(0, 75, str(data))
