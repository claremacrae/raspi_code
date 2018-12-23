import time
import threading
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
    def run(self):
        while True:
            for pixel in range(16):
                brightness = max_brightness -(2*pixel)
                mote.set_pixel(self.channel, pixel, brightness, brightness, brightness)
                mote.show()
                time.sleep(0.05)
                mote.set_pixel(self.channel, pixel, 0, 0, 0)
            time.sleep(random() * 3.0)

def thread_icicle1():
    icicle = Icicle(1)
    icicle.run()

def thread_icicle2():
    icicle = Icicle(2)
    icicle.run()

def thread_icicle3():
    icicle = Icicle(3)
    icicle.run()

def thread_icicle4():
    icicle = Icicle(4)
    icicle.run()

if __name__ == "__main__":
    mote.clear()

    t1 = threading.Thread(name="Hello1", target=thread_icicle1)
    t1.start()

    t2 = threading.Thread(name="Hello2", target=thread_icicle2)
    t2.start()

    t3 = threading.Thread(name="Hello3", target=thread_icicle3)
    t3.start()

    t4 = threading.Thread(name="Hello4", target=thread_icicle4)
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
