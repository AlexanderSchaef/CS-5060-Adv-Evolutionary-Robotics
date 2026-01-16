"""
CS 5060 Adv Evolutionary Robotics
Assignment 1
01/15/26

Alexander Schaefer
"""

import pybullet as p
import time

physicsClient = p.connect(p.GUI)

for i in range(1000):
    print(i)
    p.stepSimulation()
    time.sleep(1)
    

p.disconnect()
