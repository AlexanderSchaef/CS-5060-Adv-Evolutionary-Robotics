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

hc.Show_Best()

