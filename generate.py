"""
CS 5060 Adv Evolutionary Robotics
Assignment 2
01/16/26

Alexander Schaefer
"""

import pyrosim.pyrosim as pyrosim


def Create_World():
    pyrosim.Start_SDF("world.sdf")

    pyrosim.Send_Cube(name="Box", pos=[0,0,0.5], size=[1,1,1])

    pyrosim.End()


def Create_Robot():
    length = 1
    width = 1
    height = 1
    x, y, z, = 0, 0, 0.5

    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Torso", pos=[x,y,z], size=[length,width,height])

    pyrosim.End()



Create_World()
Create_Robot()
