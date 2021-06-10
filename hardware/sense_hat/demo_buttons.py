#!/usr/bin/env python

# from https://pythonhosted.org/sense-hat/api/#joystick

from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause

x = 3
y = 3
sense = SenseHat()

color1 = [255, 255, 255]
color2 = [255, 0, 0]
current_color = color1

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def pushed_up(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y - 1)

def pushed_down(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y + 1)

def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x - 1)

def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x + 1)

def pushed_middle(event):
    global current_color
    if event.action != ACTION_RELEASED:
        if current_color == color1:
            current_color = color2
        else:
            current_color = color1

def refresh():
    sense.clear()
    sense.set_pixel(x, y, current_color[0], current_color[1], current_color[2])

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_middle
sense.stick.direction_any = refresh
refresh()
pause()
