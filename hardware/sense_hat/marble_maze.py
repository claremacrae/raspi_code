# based on https://www.raspberrypi.org/learning/sense-hat-marble-maze/worksheet/

from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

time.sleep(0.5)

r = (255, 0, 0 )
b = (0,0,0)

maze = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,r,r,b,r,b,b,r],
        [r,b,r,b,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,b,r,r,r,r,b,r],
        [r,b,b,r,b,b,b,r],
        [r,r,r,r,r,r,r,r]]

sense.set_pixels(sum(maze,[]))
