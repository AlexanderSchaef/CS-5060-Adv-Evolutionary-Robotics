"""
CS 5060 Adv Evolutionary Robotics
Assignment 1

Alexander Schaefer
"""

from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1] 
solutionID = sys.argv[2]

simulation = SIMULATION(directOrGUI, solutionID)

simulation.Run()

simulation.Get_Fitness(solutionID=solutionID)

