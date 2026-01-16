"""
CS 5060 Adv Evolutionary Robotics
Assignment 2
01/16/26

Alexander Schaefer
"""

import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

pyrosim.Send_Cube(name="Box", pos=[0,0,0.5], size=[1,1,1])

pyrosim.End()
