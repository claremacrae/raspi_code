from gpiozero import LED
import time

# GPIO 24 ... LED ... 470 ohm resistor ... GND

led = LED(24)
try:
    led.blink()
    time.sleep(20)
except KeyboardInterrupt:
    led.off()
print "done"
