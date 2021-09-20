from mote import Mote
import atexit
import colorsys
import time


mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)


def animate():
    mote.clear()
    # r = 0
    # g = 0
    # b = 255
    # cycle_pixels_3_times_one_color(r, g, b)
    cycle_pixels_through_hue()


def cycle_pixels_3_times_one_color(r, g, b):
    for i in range(3):
        for pixel in range(16):
            mote.clear()
            set_pixel_rgb(pixel, r, g, b)
            mote.show()
            time.sleep(0.05)

def cycle_pixels_through_hue():
    for i in range(3):
        hue_loop()
        # for pixel in range(16):
        #     mote.clear()
        #     set_pixel_rgb(pixel, r, g, b)
        #     mote.show()
        #     time.sleep(0.05)

def set_pixel_rgb(pixel, r, g, b):
    set_4_pixels_one_rgb_color(pixel, r, g, b)


def set_4_pixels_one_rgb_color(pixel, r, g, b):
    for channel in range(1, 5):
        mote.set_pixel(channel, pixel, r, g, b)


def hue_loop():
    lightness = 0.2
    saturation = 1
    for hue in range(0, 360, 1):
        # print(hue)
        # mote.clear()
        (r, g, b) = colorsys.hls_to_rgb(hue / 360.0, lightness, saturation)
        for pixel in range(16):
            set_4_pixels_one_rgb_color(pixel, int(255 * r), int(255 * g), int(255 * b))
        mote.show()
        time.sleep(0.01)


#@atexit.register
def turn_off_lights():
    print("off")
    mote.clear()
    mote.show()

# atexit.register(turn_off_lights)

animate()
turn_off_lights()
