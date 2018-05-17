from gpiozero import PWMLED
from time import sleep
red = PWMLED(5)
while True:
    for x in range(101):
        red.value = x * 0.01
        sleep(0.02)
    for x in range(100, -1, -1):
        red.value = x * 0.01
        sleep(0.02)
