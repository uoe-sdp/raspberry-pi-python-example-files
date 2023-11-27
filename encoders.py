#standalone encoders NOT pi lab encoders

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) 
GPIO.setup(16, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(19, GPIO.IN)

if GPIO.input(16):
    print("Pin 16 is HIGH")
else:
    print("Pin 16 is LOW")
if GPIO.input(17):
    print("Pin 17 is HIGH")
else:
    print("Pin 17 is LOW")
if GPIO.input(18):
    print("Pin 18 is HIGH")
else:
    print("Pin 18 is LOW")
if GPIO.input(19):
    print("Pin 19 is HIGH")
else:
    print("Pin 19 is LOW")

sleep(0.25)

GPIO.cleanup()
