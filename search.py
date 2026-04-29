"""
CS 5060 Adv Evolutionary Robotics
Spiderbot Final Project

Alexander Schaefer
"""

import os
from simulation import SIMULATION

# hill climber and PHC code retained from Assignment 10
from hillclimber import HILL_CLIMBER
from parallelHillClimber import PARALLEL_HILL_CLIMBER

phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()

phc.Show_Best()
