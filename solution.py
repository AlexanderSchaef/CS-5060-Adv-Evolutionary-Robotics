import numpy as np
import random
import pyrosim.pyrosim as pyrosim
import os
import time
import thread
from thread import Thread, ConcurrentProcessing
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        z = np.zeros((c.numSensorNeurons,c.numMotorNeurons))
        for i in range(c.numSensorNeurons):
            for j in range(c.numMotorNeurons):
                z[i][j] = random.random()
        self.weights = z * 2 - 1


    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

    
    def Evaluate(self, directOrGUI):
        self.Start_Simulation(directOrGUI)
        self.Wait_For_Simulation_To_End(self)


    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Robot()

        print(f"Starting Simulation for robot {self.myID} ")
        os.system(f"python3 simulate.py {directOrGUI} {str(self.myID)} 2>&1 &")


    def Wait_For_Simulation_To_End(self):
        fitnessFile = f"fitness{self.myID}.txt"
        while not os.path.exists(fitnessFile):
            time.sleep(0.01)
        with open(fitnessFile, "r") as file:
            self.fitness = float(file.read().strip())
        os.system(f"del {fitnessFile}")


    def Create_World(self):
        filename = "world.sdf"
        pyrosim.Start_SDF(filename)

        pyrosim.Send_Cube(name="Box", pos=[2,2,0.5], size=[1,1,1])

        pyrosim.End()
        while not os.path.exists("world.sdf"):
            time.sleep(0.01)



    def Create_Robot(self):
        x = 0
        y = 0
        z = 1
        self.Generate_Body(x,y,z)
        self.Generate_Brain()


    def Generate_Body(self, x,y,z):
        filename = "body.urdf"
        pyrosim.Start_URDF(filename)

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 2, 1])


        spacing = 1
        for i in range(1, 5):
            # Left Legs
            pyrosim.Send_Cube(name=f"LeftLeg{i}", pos=[-0.5, spacing, 0], size=[1, 0.2, 0.2])
            pyrosim.Send_Joint(name=f"Torso_LeftLeg{i}", parent="Torso", child=f"LeftLeg{i}", position=[-0.5, 0, 1],
                            type="revolute", jointAxis="1 1 0 ")
            pyrosim.Send_Cube(name=f"LeftLowerLeg{i}", pos=[0, spacing, -0.5], size=[0.2, 0.2, 1])
            pyrosim.Send_Joint(name=f"LeftLeg_LeftLowerLeg{i}", parent=f"LeftLeg{i}", child=f"LeftLowerLeg{i}", position=[-1, 0, 0],
                            type="revolute", jointAxis="1 1 0 ")

            # Right Legs
            pyrosim.Send_Cube(name=f"RightLeg{i}", pos=[0.5, spacing, 0], size=[1, 0.2, 0.2])
            pyrosim.Send_Joint(name=f"Torso_RightLeg{i}", parent="Torso", child=f"RightLeg{i}", position=[0.5, 0, 1],
                            type="revolute", jointAxis="1 1 0 ")
            pyrosim.Send_Cube(name=f"RightLowerLeg{i}", pos=[0, spacing, -0.5], size=[0.2, 0.2, 1])
            pyrosim.Send_Joint(name=f"RightLeg_RightLowerLeg{i}", parent=f"RightLeg{i}", child=f"RightLowerLeg{i}", position=[1, 0, 0],
                            type="revolute", jointAxis="1 1 0 ")
            
            # to deal with the 0.01
            if i == 4:
                spacing -= 0.66
            else:
                spacing -= 0.67
            
        pyrosim.End()
        while not os.path.exists("body.urdf"):
            time.sleep(0.01)



    def Generate_Brain(self):
        print(f"Generating brain{self.myID}")
        filename = f"brain{self.myID}.nndf"
        pyrosim.Start_NeuralNetwork(filename)


        name = 0
        for i in range(name, c.numSensorNeurons):
            pyrosim.Send_Sensor_Neuron(name = name, linkName = c.sensorNames[name])
            name += 1
        for i in range(name, c.numMotorNeurons + c.numSensorNeurons):
            pyrosim.Send_Motor_Neuron(name = name, jointName = c.motorNames[name - c.numSensorNeurons])
            name += 1
        # pyrosim.Send_Motor_Neuron(name = 3, jointName = motorNames[0])
        # pyrosim.Send_Motor_Neuron(name = 4, jointName = motorNames[1])

        num_neurons = len(c.sensorNames) + len(c.motorNames)
        currentColumn = len(self.weights[0])
        currentRow = len(self.weights)
        for currentColumn in range(len(self.weights[0])):
            for currentRow in range(len(self.weights)):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+3, weight = self.weights[currentRow][currentColumn])

        pyrosim.End()
        while not os.path.exists(f"brain{self.myID}.nndf"):
            print(f"Waiting on brain{self.myID}")
            time.sleep(0.01)


    def Mutate(self):
        row = random.randint(0, c.numSensorNeurons - 1)
        col = random.randint(0, c.numMotorNeurons - 1)
        self.weights[row, col] = (random.random() * 2) - 1