# Run with sudo python3
# Flash a single LED on and then off, every 1 second
# From Adventures in Raspberry Pi
#
# GPIO 24 ... LED ... 330 ohm resistor ... GND

import RPi.GPIO as GPIO
import time

# Enabl BroadCoM number of GPIO ports:
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24, GPIO.OUT)

while True:
    GPIO.output(24, True)
    time.sleep(1)
    GPIO.output(24, False)
    time.sleep(1)

