#!/usr/bin/python

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
while 1:
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(24,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(24,GPIO.LOW)
    time.sleep(1)

