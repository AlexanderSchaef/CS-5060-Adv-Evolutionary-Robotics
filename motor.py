import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()


    def Prepare_To_Act(self):

        self.amplitude = c.amplitude
        # self.frequency = c.frequency_frontLeg
        print(self.jointName)
        if self.jointName == b"Torso_FrontLeg":
            print("hi")
            self.frequency = c.frequency_frontLeg / 2
        else:
            self.frequency = c.frequency_frontLeg
        self.offset = c.phaseOffset_frontLeg
        self.values = self.amplitude * np.sin([self.frequency * i/c.numSteps + self.offset for i in range(c.numSteps)])


    def Set_Value(self, robotId, t):
        pyrosim.Set_Motor_For_Joint(
                bodyIndex = robotId,
                jointName = self.jointName,
                controlMode = p.POSITION_CONTROL,
                targetPosition = self.values[t],
                maxForce = 20.0)