from gpiozero import RGBLED
from time import sleep
led = RGBLED(red=17, green=18, blue=19)
delay = 0.02

while True:
    for x in range(100):
        led.red = x/100
        sleep(delay)
    for x in range(100, -1, -1):
        led.red = x/100
        sleep(delay)

    for x in range(100):
        led.green = x/100
        sleep(delay)
    for x in range(100, -1, -1):
        led.green = x/100
        sleep(delay)

    for x in range(100):
        led.blue = x/100
        sleep(delay)
    for x in range(100, -1, -1):
        led.blue = x/100
        sleep(delay)

