"""
CS 5060 Adv Evolutionary Robotics
Assignment 1
01/15/26

Alexander Schaefer
"""

import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy


numSteps = 1000 # how many frames the program will iterate

physicsClient = p.connect(p.GUI)

# Set the path for built in objects, like plane
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Set the gravity
p.setGravity(0,0,-9.8) # 1 G

# Load the floor
planeID = p.loadURDF("plane.urdf")

# Load the world link
p.loadSDF("world.sdf")
robotId = p.loadURDF("body.urdf")

# Set up for the sensors
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(numSteps)
frontLegSensorValues = numpy.zeros(numSteps)

# Run simulation for n timesteps
for i in range(numSteps):
    # print(i)
    
    p.stepSimulation()
    
    # sensors:
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    # print(backLegTouch)
    backLegSensorValues[i] = backLegTouch
    frontLegSensorValues[i] = frontLegTouch

    time.sleep(0.01) 

# save the values of backLegSensorValues
with open('data/backLegSensorValues.npy', 'wb') as f:
    numpy.save(f, backLegSensorValues)
with open('data/frontLegSensorValues.npy', 'wb') as f:
    numpy.save(f, frontLegSensorValues)

p.disconnect()

# print(backLegSensorValues)
