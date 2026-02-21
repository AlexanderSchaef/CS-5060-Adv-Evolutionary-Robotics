"""
CS 5060 Adv Evolutionary Robotics
Assignment 9

Alexander Schaefer
"""

import os
from simulation import SIMULATION
from hillclimber import HILL_CLIMBER
from parallelHillClimber import PARALLEL_HILL_CLIMBER

phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()

phc.Show_Best()

