from gpiozero import TrafficLights
import time

def british_lights_cycle(lights, cycle_time):
    lights.off()

    # Red
    lights.red.on()
    time.sleep(cycle_time)

    # Red and Amber
    lights.amber.on()
    time.sleep(cycle_time)

    # Green
    lights.red.off()
    lights.amber.off()
    lights.green.on()
    time.sleep(cycle_time)

    # Amber
    lights.green.off()
    lights.amber.on()
    time.sleep(cycle_time)

    # Red
    lights.amber.off()
    lights.red.on()
    time.sleep(cycle_time)


lights = TrafficLights(17, 23, 25)

british_lights_cycle(lights, 2)

lights.off()

print "done!"
