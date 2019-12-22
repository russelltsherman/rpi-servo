#!/usr/bin/env python3

"""Example that iterates through a servo on every channel, sets each to 180 and then back to 0."""
import time
from adafruit_servokit import ServoKit
from random import seed
from random import randint
seed(1)

# Set channels to the number of servo channels on your kit.
kit = ServoKit(channels=16)

while True:
    start = 0
    end = randint(0, 180)

    for i in range(len(kit.servo)):
        if i % 2 == 0: 
            kit.servo[i].angle = randint(0, 180)
            time.sleep(0.5)
            kit.servo[i].angle = 0
            time.sleep(0.5)
        else:
            kit.servo[i].angle = 0
            time.sleep(0.5)
            kit.servo[i].angle = randint(0, 180)
            time.sleep(0.5)
