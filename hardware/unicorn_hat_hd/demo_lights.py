#!/usr/bin/env python
import unicornhathd
import os
from time import sleep

class Point:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def turn_on(self):
        unicornhathd.set_pixel(self.x, self.y, 255, 255, 255)

    def turn_off(self):
        unicornhathd.set_pixel(self.x, self.y, 0, 0, 0)
    
    def move(self):
        self.turn_off()
        self.x, self.dx = self.move_one_axis(self.x, self.dx)
        self.y, self.dy = self.move_one_axis(self.y, self.dy)
        self.turn_on()

    def move_one_axis(self, x_or_y, dx_or_dy):
        x_or_y += dx_or_dy
        if x_or_y < 0 or x_or_y > 15:
            dx_or_dy = dx_or_dy * -1
            x_or_y += dx_or_dy
        return x_or_y, dx_or_dy

print("Press <CTRL+C> to exit...")

unicornhathd.off()

# Bounce backwards and forwards along each edge:
p1 = Point(0, 0, 0, 1)
p2 = Point(0, 15, 1, 0)
p3 = Point(15, 0, -1, 0)
p4 = Point(15, 15, 0, -1)
p1.turn_on()
p2.turn_on()
p3.turn_on()
p4.turn_on()
unicornhathd.show()

try:
    while True:
        p1.move()
        p2.move()
        p3.move()
        p4.move()
        unicornhathd.show()
        sleep(0.1)
except KeyboardInterrupt:
    pass

unicornhathd.off()
