import time
from random import randint
from mote import Mote

mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

full_brightness = 40

class Icicle:
    def __init__(self, channel):
        self.channel = channel

        # The icicle has a random "virtual" length, which is longer than the physical
        # number of pixels.
        # Each frame, the drip progresses along the virtual length,
        # until it reaches the end of the virtual icicle.
        self.current_pixel = None
        self.pixel_length = None
        self.start_random_wait_for_next_drip()
        
        # To avoid all 4 icicles starting at the same time, for this first cycle only,
        # start the loop below the end of the icicle, so that we just see a wait
        # until the end of the virtual icicle
        self.current_pixel = 20
        assert(self.current_pixel < self.pixel_length)

    def step(self):
        # Dim or turn off previous pixels
        self.set_pixel_brightness(self.current_pixel - 3, 0.0)
        self.set_pixel_brightness(self.current_pixel - 2, 0.1)
        self.set_pixel_brightness(self.current_pixel - 1, 0.2)
        self.set_pixel_brightness(self.current_pixel, 1.0)

        # Advance pixel number, ready for next frame
        self.current_pixel += 1

        # If the next pixel will be zero, set up a random wait before starting the
        # next cycle:
        if self.current_pixel == self.pixel_length:
            self.start_random_wait_for_next_drip()

    def set_pixel_brightness(self, pixel, brightness_fraction):
        if not self.valid_pixel(pixel):
            return
        brightness = int(brightness_fraction * full_brightness)
        mote.set_pixel(self.channel, pixel, brightness, brightness, brightness)

    def valid_pixel(self, pixel):
        return pixel >=0 and pixel <= 15

    def start_random_wait_for_next_drip(self):
        self.current_pixel = 0
        self.pixel_length = randint(25, 50)


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
