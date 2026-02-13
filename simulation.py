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
        # TOGGLE FOR VISIBLE WINDOW
        # self.physicsClient = p.connect(p.GUI)
        self.physicsClient = p.connect(p.DIRECT)


        # Set the path for built in objects, like plane
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # Set the gravity
        p.setGravity(0,0,-9.8) # 1 G

        self.world = WORLD()
        self.robot = ROBOT()

    

    def Run(self):
        # Run simulation for n timesteps
        for t in range(c.numSteps):
            # print(t)
            
            p.stepSimulation()

            self.robot.Sense(t)

            self.robot.Think()

            self.robot.Act(t)
            
            time.sleep(0.01) 



    def Get_Fitness(self):
        self.robot.Get_Fitness()


    def __del__(self):
        # self.robot.Save_Values()
        p.disconnect()
