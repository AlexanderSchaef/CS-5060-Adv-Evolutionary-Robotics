"""
CS 5060 Adv Evolutionary Robotics
Assignment 9

Alexander Schaefer
"""

import os
from simulation import SIMULATION
from hillclimber import HILL_CLIMBER

hc = HILL_CLIMBER()

hc.Evolve()


# for i in range(5):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")

