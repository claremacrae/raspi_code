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
        self.current_pixel = 0
        self.start_random_wait_for_next_drip()

    def step(self):
        # Turn off previous pixel
        mote.set_pixel(self.channel, self.previous_pixel(), 0, 0, 0)
        
        # Check if we are pausing between drips
        if self.frames_to_wait > 0:
            self.frames_to_wait -= 1
            return
        
        # Advance to next pixel
        brightness = full_brightness
        mote.set_pixel(self.channel, self.current_pixel, brightness, brightness, brightness)

        # Advance pixel number, ready for next frame
        self.current_pixel = self.next_pixel()

        # If the next pixel will be zero, set up a random wait before starting the
        # next cycle:
        if self.current_pixel == 0:
            self.start_random_wait_for_next_drip()

    def next_pixel(self, delta = 1):
        new_pixel = self.current_pixel + delta
        if not self.valid_pixel(new_pixel):
            new_pixel -= 16
        return new_pixel
    
    def previous_pixel(self, delta = 1):
        new_pixel = self.current_pixel - delta
        if not self.valid_pixel(new_pixel):
            new_pixel += 16
        return new_pixel

    def valid_pixel(self, pixel):
        return pixel >=0 and pixel <= 15

    def start_random_wait_for_next_drip(self):
        self.frames_to_wait = randint(15, 30)


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
