#!/usr/bin/env python3

"""Example that rotates servos on every channel to 180 and then back to 0."""
import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
kit = ServoKit(channels=16)

while True:
    for i in range(len(kit.servo)):
        kit.servo[i].angle = 180
    time.sleep(0.5)

    for i in range(len(kit.servo)):
        kit.servo[i].angle = 0
    time.sleep(5)
