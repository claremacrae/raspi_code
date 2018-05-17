from gpiozero import RGBLED
from time import sleep
led = RGBLED(red=17, green=18, blue=19)
delay = 0.02

while True:
    led.blink(on_time=0, off_time=0, \
              fade_in_time=2, fade_out_time=2, \
              on_color=(1,0,0), off_color=(0,0,0))
    sleep(4)

    led.blink(on_time=0, off_time=0, \
              fade_in_time=2, fade_out_time=2, \
              on_color=(0,1,0), off_color=(0,0,0))
    sleep(4)

    led.blink(on_time=0, off_time=0, \
              fade_in_time=2, fade_out_time=2, \
              on_color=(0,0,1), off_color=(0,0,0))
    sleep(4)
