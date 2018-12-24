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
    def __init__(self, channel):
        self.channel = channel
        self.current_pixel = 0

    def step(self):
        # Turn off previous pixel
        mote.set_pixel(self.channel, self.previous_pixel(), 0, 0, 0)
        
        # Advance to next pixel
        brightness = max_brightness -(2*self.current_pixel)
        mote.set_pixel(self.channel, self.current_pixel, brightness, brightness, brightness)

        # Advance pixel number, ready for next frame
        self.current_pixel = self.next_pixel()
        
    def next_pixel(self):
        if self.current_pixel < 15:
            return self.current_pixel + 1
        else:
            return 0
    
    def previous_pixel(self):
        if self.current_pixel > 0:
            return self.current_pixel - 1
        else:
            return 15


if __name__ == "__main__":
    mote.clear()
    
    icicles = [
        Icicle(1), 
        Icicle(2), 
        Icicle(3), 
        Icicle(4)
        ]

    while True:
        for icicle in icicles:
            icicle.step()
        mote.show()
        time.sleep(0.2)
