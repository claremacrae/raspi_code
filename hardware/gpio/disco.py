from gpiozero import LED
import time

# GPIO 24 ... LED ... 470 ohm resistor ... GND

def cycle( light, repetitions, duration):
    #print repetitions
    #print duration
    #print '-----'
    for x in range(repetitions):
        #print x
        light.on()
        time.sleep(duration)
        light.off()
        time.sleep(duration)

def all_off():
    r.off()
    a.off()
    g.off()

def cycle_all(repetitions, duration):
    cycle( r, repetitions, duration)
    cycle( a, repetitions, duration)
    cycle( g, repetitions, duration)
    cycle( a, repetitions, duration)

r = LED(17)
a = LED(27)
g = LED(22)
all_off()

try:
    while True:
        cycle_all( 2, 0.5)
        cycle_all( 2, 0.25)
        cycle_all( 4, 0.25 / 2.0)
        cycle_all( 8, 0.25 / 4.0)
    
except KeyboardInterrupt:
    all_off()
print "done"
