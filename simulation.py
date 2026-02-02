import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import time

from world import WORLD
from robot import ROBOT
import constants as c



class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)

        # Set the path for built in objects, like plane
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # Set the gravity
        p.setGravity(0,0,-9.8) # 1 G

        self.world = WORLD()
        self.robot = ROBOT()

        # Set up for the sensors
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
    

    def Run(self):
        # Run simulation for n timesteps
        backLegSensorValues = np.zeros(c.numSteps)
        frontLegSensorValues = np.zeros(c.numSteps)
        for i in range(c.numSteps):
            print(i)
            
            # p.stepSimulation()
            
            # sensors:
            backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            # print(backLegTouch)
            backLegSensorValues[i] = backLegTouch
            frontLegSensorValues[i] = frontLegTouch
            # motors
            
            pyrosim.Set_Motor_For_Joint(
                    bodyIndex = self.robot.robotId,
                    jointName = b"Torso_BackLeg",
                    controlMode = p.POSITION_CONTROL,
                    targetPosition = c.targetAngles_frontLeg[i],
                    maxForce = 20.0)
            pyrosim.Set_Motor_For_Joint(
                    bodyIndex = self.robot.robotId,
                    jointName = b"Torso_FrontLeg",
                    controlMode = p.POSITION_CONTROL,
                    targetPosition = c.targetAngles_backLeg[i],
                    maxForce = 20.0)
            
            # time.sleep(0.01) 

