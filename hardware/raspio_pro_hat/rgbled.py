from gpiozero import RGBLED
from time import sleep
led = RGBLED(red=17, green=18, blue=19)

# Change red brightness
led.red = 1
sleep(0.5)

led.red = 0.5
sleep(0.5)

led.red = 0.0
sleep(0.5)

# Change green brightness
led.green = 1
sleep(0.5)

led.green = 0.5
sleep(0.5)

led.green = 0.0
sleep(0.5)

# Change blue brightness
led.blue = 1
sleep(0.5)

led.blue = 0.5
sleep(0.5)

led.blue = 0.0
sleep(0.5)
