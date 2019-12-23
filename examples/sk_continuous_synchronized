#!/usr/bin/env python3

"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
kit = ServoKit(channels=16)

while True:
    for i in range(len(kit.servo)):
        kit.continuous_servo[i].throttle = 1
    time.sleep(5)

    for i in range(len(kit.servo)):
        kit.continuous_servo[i].throttle = 0
    time.sleep(5)

    for i in range(len(kit.servo)):
        kit.continuous_servo[i].throttle = -1
    time.sleep(5)

    for i in range(len(kit.servo)):
        kit.continuous_servo[i].throttle = 0
    time.sleep(5)
