"""
CS 5060 Adv Evolutionary Robotics
01/27/26

Alexander Schaefer"""

import numpy as np
import matplotlib.pyplot as plot

backLegSensorValues = np.load("data/backLegSensorValues.npy")
print(backLegSensorValues)

frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
print(frontLegSensorValues)

motorValues = np.load("data/motor.npy")

# plot.plot(backLegSensorValues, linewidth=4, label="Back Leg")
# plot.plot(frontLegSensorValues, label="Front Leg")
plot.plot(motorValues, label="Motors") # both legs are symmetric in motor signals


plot.legend()
plot.show()
