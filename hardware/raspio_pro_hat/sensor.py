from gpiozero import LightSensor
from time import sleep
ldr = LightSensor(21)
while True:
    if ldr.light_detected:
        print("Light")
    else:
        print("Dark")
    sleep(0.1)

