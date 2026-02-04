import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")

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


    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    

    def Act(self, t):
        for m in self.motors.values():
            m.Set_Value(self.robotId, t)
    

    def Save_Values(self):
        # save sensor values
        for s in self.sensors.values():
            with open(f"data/{s.linkName}SensorValues.npy") as f:
                np.save(f, str(s.values))
            
        # save motor values
        for m in self.motors.values():
            with open(f"data/{m.jointName}MotorValues.npy") as f:
                np.save(f, str(m.values))