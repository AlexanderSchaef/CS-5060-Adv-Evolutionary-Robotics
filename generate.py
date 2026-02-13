"""
CS 5060 Adv Evolutionary Robotics
Assignment 2
01/16/26

Alexander Schaefer
"""

import pyrosim.pyrosim as pyrosim
import random


def Create_World():
    pyrosim.Start_SDF("world.sdf")

    pyrosim.Send_Cube(name="Box", pos=[2,2,0.5], size=[1,1,1])

    pyrosim.End()


def Create_Robot():
    x = 0
    y = 0
    z = 1.5
    Generate_Body(x,y,z)
    # print("Brain")
    Generate_Brain()



def Generate_Body(x,y,z):

    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Torso", pos=[x,y,z], size=[1,1,1])
    
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                       type="revolute", position=[x-0.5,y,z-0.5])
    
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1])

    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                       type="revolute", position=[x+0.5,y,z-0.5])

    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])

    pyrosim.End()


def Generate_Brain():

    pyrosim.Start_NeuralNetwork("brain.nndf")
    sensorNames = ['Torso', 'FrontLeg', 'BackLeg']
    motorNames = ['Torso_BackLeg', 'Torso_FrontLeg']

    pyrosim.Send_Sensor_Neuron(name = 0, linkName = sensorNames[0])
    pyrosim.Send_Sensor_Neuron(name = 1, linkName = sensorNames[1])
    pyrosim.Send_Sensor_Neuron(name = 2, linkName = sensorNames[2])

    pyrosim.Send_Motor_Neuron(name = 3, jointName = motorNames[0])
    pyrosim.Send_Motor_Neuron(name = 4, jointName = motorNames[1])

    num_neurons = len(sensorNames) + len(motorNames)
    for i in range(num_neurons):
        for j in range(num_neurons):
            if i != j:
                pyrosim.Send_Synapse(sourceNeuronName = i, targetNeuronName = j, weight = random.uniform(-1,1))


    pyrosim.End()


Create_World()

Create_Robot()

