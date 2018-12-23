import time
from random import random, randint
from mote import Mote

mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

max_brightness = 40

class Icicle:
    def __init__(self, channnel):
        self.channel = channel
    def run(self):
        for pixel in range(16):
            mote.clear()
            brightness = max_brightness -(2*pixel)
            mote.set_pixel(channel, pixel, brightness, brightness, brightness)
            mote.show()
            time.sleep(0.05)
            mote.set_pixel(channel, pixel, 0, 0, 0)

mote.clear()

while True:
    channel = randint(1, 4)
    icicle = Icicle(channel)
    icicle.run()
    mote.show()
    time.sleep(random() * 3.0)
