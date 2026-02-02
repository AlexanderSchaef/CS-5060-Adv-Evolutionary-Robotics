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
import numpy as np
import random


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
backLegSensorValues = np.zeros(numSteps)
frontLegSensorValues = np.zeros(numSteps)

# motor sine waves

amplitude_frontLeg = np.pi / 4
frequency_frontLeg = 2 * 30
phaseOffset_frontLeg = 1
targetAngles_frontLeg = amplitude_frontLeg * np.sin([frequency_frontLeg * i/numSteps + phaseOffset_frontLeg for i in range(numSteps)])

amplitude_backLeg = np.pi / 4
frequency_backLeg = 2 * 30
phaseOffset_backLeg = 0
targetAngles_backLeg = amplitude_frontLeg * np.sin([frequency_frontLeg * i/numSteps + phaseOffset_frontLeg for i in range(numSteps)])

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
    # motors
    pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = b"Torso_BackLeg",
            controlMode = p.POSITION_CONTROL,
            targetPosition = targetAngles_frontLeg[i],
            maxForce = 20.0)
    pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = b"Torso_FrontLeg",
            controlMode = p.POSITION_CONTROL,
            targetPosition = targetAngles_backLeg[i],
            maxForce = 20.0)


    time.sleep(0.01) 

# save the values of backLegSensorValues
with open('data/backLegSensorValues.npy', 'wb') as f:
    np.save(f, backLegSensorValues)
with open('data/frontLegSensorValues.npy', 'wb') as f:
    np.save(f, frontLegSensorValues)
with open('data/motor_frontLeg.npy', 'wb') as f:
    np.save(f, targetAngles_frontLeg)
with open('data/motor_backLeg.npy', 'wb') as f:
    np.save(f, targetAngles_backLeg)

p.disconnect()

# print(backLegSensorValues)
