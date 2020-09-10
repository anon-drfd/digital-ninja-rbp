""" 
led-test.py 
Switches green LED for 5 seconds
then switches Red LED on for 5 seconds
"""
import RPi.GPIO as GPIO
import time

#Set GPIO pins as outputs
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#Switch Green LED GPIO pin ON
GPIO.output(16, True)
#Wait 5 seconds
time.sleep(5)
#Switch Green GPIO pins OFF
GPIO.output(16, False)

#Switch Red LED GPIO pin ON
GPIO.output(18, True)
#Wait 5 seconds
time.sleep(5)
#Switch Red GPIO pins OFF
GPIO.output(18, False)

#Reset GPIO pins to their default state
GPIO.cleanup()

