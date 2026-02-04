"""
CS 5060 Adv Evolutionary Robotics
Assignment 1

Alexander Schaefer
"""


# # save the values of backLegSensorValues
# with open('data/backLegSensorValues.npy', 'wb') as f:
#     np.save(f, backLegSensorValues)
# with open('data/frontLegSensorValues.npy', 'wb') as f:
#     np.save(f, frontLegSensorValues)
# with open('data/motor_frontLeg.npy', 'wb') as f:
#     np.save(f, targetAngles_frontLeg)
# with open('data/motor_backLeg.npy', 'wb') as f:
#     np.save(f, targetAngles_backLeg)

# p.disconnect()

# print(backLegSensorValues)


from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()

