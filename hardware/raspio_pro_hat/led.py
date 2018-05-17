from gpiozero import LED
from time import sleep
red = LED(5)
red.on()
sleep(2)
red.off()

