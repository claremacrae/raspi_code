from gpiozero import LightSensor, PWMLED
from signal import pause
sensor = LightSensor(21)
led = PWMLED(5)
led.source = sensor.values
pause()
