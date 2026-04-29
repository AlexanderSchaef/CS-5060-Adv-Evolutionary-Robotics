"""
CS 5060 Adv Evolutionary Robotics
Spiderbot Final Project

Alexander Schaefer
"""

import numpy as np
import random

numSteps = 1000 # how many frames the program will iterate

backLegSensorValues = np.zeros(numSteps)
frontLegSensorValues = np.zeros(numSteps)

# motor sine waves
amplitude = np.pi / 4

frequency_frontLeg = 2 * 30
phaseOffset_frontLeg = 1

frequency_backLeg = 2 * 30
phaseOffset_backLeg = 0

targetAngles_frontLeg = amplitude * np.sin([frequency_frontLeg * i/numSteps + phaseOffset_frontLeg for i in range(numSteps)])
targetAngles_backLeg = amplitude * np.sin([frequency_frontLeg * i/numSteps + phaseOffset_frontLeg for i in range(numSteps)])

numberOfGenerations = 2
populationSize = 4


sensorNames = []

for i in range(1, 5):
    sensorNames.append(f'LeftLowerLeg{i}')
    sensorNames.append(f'RightLowerLeg{i}')

# GOAL POST SENSOR NEURONS
# sensorNames.append('goal_x')
# sensorNames.append('goal_y')
# sensorNames.append('goal_z')


motorNames = []

for i in range(1, 5):
    motorNames.append(f'Torso_LeftLeg{i}')
    motorNames.append(f'Torso_RightLeg{i}')
    motorNames.append(f'LeftLeg_LeftLowerLeg{i}')
    motorNames.append(f'RightLeg_RightLowerLeg{i}')

numSensorNeurons = len(sensorNames)
numMotorNeurons = len(motorNames)
numHiddenNeurons = 8

motorJointRange = 0.25

# goal_x = random.randint(-15, 15)
# goal_y = random.randint(-15, 15)
goal_x = 15
goal_y = 15
goal_z = 1.5
