"""
CS 5060 Adv Evolutionary Robotics
Assignment 1
01/15/26

Alexander Schaefer
"""

import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)

# Set the path for built in objects, like plane
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Set the gravity
p.setGravity(0,0,-9.8) # 1 G

# Load the floor
planeID = p.loadURDF("plane.urdf")

# Load the world link
p.loadSDF("world.sdf")
p.loadURDF("body.urdf")

# Run simulation for n timesteps
for i in range(10000):
    print(i)
    p.stepSimulation()
    time.sleep(0.01) 

p.disconnect()
