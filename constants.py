"""
CS 5060 Adv Evolutionary Robotics
Assignment 6

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

numberOfGenerations = 10