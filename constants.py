"""
CS 5060 Adv Evolutionary Robotics
Spiderbot Final Project

Alexander Schaefer
"""

import numpy as np

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

numberOfGenerations = 15
populationSize = 20


sensorNames = []

for i in range(1, 5):
    sensorNames.append(f'LeftLowerLeg{i}')
    sensorNames.append(f'RightLowerLeg{i}')

motorNames = []

for i in range(1, 5):
    motorNames.append(f'Torso_LeftLeg{i}')
    motorNames.append(f'Torso_RightLeg{i}')
    motorNames.append(f'LeftLeg_LeftLowerLeg{i}')
    motorNames.append(f'RightLeg_RightLowerLeg{i}')

numSensorNeurons = len(sensorNames)
numMotorNeurons = len(motorNames)

motorJointRange = 0.25
