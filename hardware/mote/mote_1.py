from mote import Mote

# Based on https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-mote

mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

def run1():
    mote.clear()
    mote.set_pixel(1, 0, 255, 0, 0)
    mote.show()
#run1()

def run2():
    mote.clear()
    for channel in range(1, 5):
        for pixel in range(16):
            mote.set_pixel(channel, pixel, 0, 0, 255)
    mote.show()
#run2()

def animate():
    import time
    mote.clear()
    while True:
        for channel in range(1, 5):
            for pixel in range(16):
                mote.clear()
                mote.set_pixel(channel, pixel, 0, 0, 255)
                mote.show()
                time.sleep(0.05)
animate()
