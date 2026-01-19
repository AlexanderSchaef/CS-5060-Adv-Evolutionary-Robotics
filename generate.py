"""
CS 5060 Adv Evolutionary Robotics
Assignment 2
01/16/26

Alexander Schaefer
"""

import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z = height / 2

scaling_factor = 0.9
current_scale = 1

for i in range(10):
    # make a box
    name = f"Box{i+1}"
    pyrosim.Send_Cube(name=name, pos=[x,y,z], size=[length,width,height])
    
    # update the height of the next box
    z = z + height/2 + height*scaling_factor/2

    # update the size of the next box
    length *= scaling_factor
    width *= scaling_factor
    height *= scaling_factor


    # update current_scale
    current_scale *= scaling_factor

pyrosim.End()
