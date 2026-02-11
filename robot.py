import numpy as np
import pybullet as p


import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c

from sensor import SENSOR
from motor import MOTOR


class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")


        pyrosim.Prepare_To_Simulate(self.robotId)

        self.Prepare_To_Sense()
        self.Prepare_To_Act()


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
        self.nn.Print()


    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode('UTF-8')
                desiredAngle = self.nn.Get_Value_Of(neuronName)

                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

                print(f"MOTOR {neuronName}")
                print(f"JOINT: {jointName.decode('UTF-8')}")
                print(f"Desired Angle: {desiredAngle}")
        # for m in self.motors.values():
        #     print("m: ", m)
        #     m.Set_Value(self.robotId, t)
    

    def Save_Values(self):
        # save sensor values
        for s in self.sensors.values():
            with open(f"data/{s.linkName}SensorValues.npy") as f:
                np.save(f, str(s.values))
            
        # save motor values
        for m in self.motors.values():
            with open(f"data/{m.jointName}MotorValues.npy") as f:
                np.save(f, str(m.values))