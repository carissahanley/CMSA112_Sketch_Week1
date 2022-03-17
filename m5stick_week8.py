import m5ui

from m5stack import lcd
from m5ui import setScreenColor
import imu

   from m5stack import M5Led
from m5stack import btnA
import time
from m5stack import speaker

import imu

import esp32 

my_imu = imu.IMU()

#public functions

def read_accelerometer(normalized=False):
    x, y, z = my_imu.acceleration
    if normalized: # defaults range from -1.0 to 1.0 but sometimes exceed this boundary
        x = (x + 1.0) / 2.0
        y = (y + 1.0) / 2.0
        z = (z + 1.0) / 2.0
        x = _clamp(x, 0.0, 1.0)
        y = _clamp(y, 0.0, 1.0)
        z = _clamp(z, 0.0, 1.0)
    return x, y, z



def set_screen_color(r, g, b):
    hex_color = '%02x%02x%02x' % (r, g, b)
    screen_color = int('0x' + (hex_color))
    setScreenColor(screen_color)
