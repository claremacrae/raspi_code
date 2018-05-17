from gpiozero import PWMLED
from signal import pause
red = PWMLED(5)
red.blink(on_time=1, off_time=1, fade_in_time=1, fade_out_time=1)
pause()

