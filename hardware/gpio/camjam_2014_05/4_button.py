#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(18,GPIO.IN)

GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

print("-------------")
print("Button + GPIO")
print("-------------")

print GPIO.input(18)
while True:
    if ( GPIO.input(18) == False ):
        print( "Button pressed")
        os.system('date')
        print GPIO.input(18)
        time.sleep(1)
    else:
        os.system('clear')
        print("Waiting for you to press a button")
    time.sleep(0.5)

