#!/usr/bin/python

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
print "Lights on"
GPIO.output(23,GPIO.HIGH)
GPIO.output(24,GPIO.HIGH)
