#!/usr/bin/env python

import dothat.lcd as lcd
import dothat.backlight as backlight
from time import sleep

lcd.set_cursor_position(0, 1)
lcd.write('Happy Christmas!')

#for x in range(50):
#    backlight.hue(x / 50.0)
#    sleep(0.05)

backlight.rgb(0, 255, 0)
