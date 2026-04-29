import numpy as np
import pybullet as p
import os
from math import dist


import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c
from sensor import SENSOR
from motor import MOTOR


class ROBOT:
    def __init__(self, simulationID):
        self.robot = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK(f"brain{simulationID}.nndf")

        pyrosim.Prepare_To_Simulate(self.robot)

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        os.system(f"del brain{simulationID}.nndf")


    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            # print(linkName)
            self.sensors[linkName] = SENSOR(linkName)
    
    
    def Sense(self, t):
        for s in self.sensors.values():
            s.Get_Value(t)


    def Think(self):
        self.nn.Update()
        # self.nn.Print()


    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode('UTF-8')
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange

                self.motors[jointName].Set_Value(self.robot, desiredAngle)

                # print(f"MOTOR {neuronName}")
                # print(f"JOINT: {jointName.decode('UTF-8')}")
                # print(f"Desired Angle: {desiredAngle}")
    

    def Get_Fitness(self, solutionID):
        # GET FITNESS MODIFIED
        # From moving to the right, to moving towards the cube

        print()

        stateOfLinkZero = p.getLinkState(self.robot,0)
        # print(stateOfLinkZero)
        positionOfLinkZero = stateOfLinkZero[0]
        # print(positionOfLinkZero)
        xCoordinateOfLinkZero = positionOfLinkZero[0] 
        yCoordinateOfLinkZero = positionOfLinkZero[1] 
        zCoordinateOfLinkZero = positionOfLinkZero[2] 

        print(stateOfLinkZero)
        print(xCoordinateOfLinkZero, yCoordinateOfLinkZero, zCoordinateOfLinkZero)

        # Fitness metric for moving in the x direction
        # with open(f"tmp{str(solutionID)}.txt", "w") as file:
        #     file.write(str(xCoordinateOfLinkZero))
        # os.system(f"rename tmp{str(solutionID)}.txt fitness{solutionID}.txt")

        fitness = dist([xCoordinateOfLinkZero, yCoordinateOfLinkZero, zCoordinateOfLinkZero], 
                       [c.goal_x, c.goal_y, c.goal_z])
        
        with open(f"tmp{str(solutionID)}.txt", "w") as file:
            file.write(str(fitness))
        os.system(f"rename tmp{str(solutionID)}.txt fitness{solutionID}.txt")



    def Save_Values(self):
        # save sensor values
        for s in self.sensors.values():
            with open(f"data/{s.linkName}SensorValues.npy") as f:
                np.save(f, str(s.values))
            
        # save motor values
        for m in self.motors.values():
            with open(f"data/{m.jointName}MotorValues.npy") as f:
                np.save(f, str(m.values))