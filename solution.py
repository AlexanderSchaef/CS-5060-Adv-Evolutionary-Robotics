import numpy as np
import random
import pyrosim.pyrosim as pyrosim
import os
import time
import thread
from thread import Thread, ConcurrentProcessing

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        z = np.zeros((3,2))
        for i in range(3):
            for j in range(2):
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
        os.system(f"python3 simulate.py {directOrGUI} {str(self.myID)} --disable-gil &")


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
        z = 1.5
        self.Generate_Body(x,y,z)
        self.Generate_Brain()


    def Generate_Body(self, x,y,z):
        filename = "body.urdf"
        pyrosim.Start_URDF(filename)

        pyrosim.Send_Cube(name="Torso", pos=[x,y,z], size=[1,1,1])
        
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                        type="revolute", position=[x-0.5,y,z-0.5])
        
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1])

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                        type="revolute", position=[x+0.5,y,z-0.5])

        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])

        pyrosim.End()
        while not os.path.exists("body.urdf"):
            time.sleep(0.01)



    def Generate_Brain(self):
        print(f"Generating brain{self.myID}")
        filename = f"brain{self.myID}.nndf"
        pyrosim.Start_NeuralNetwork(filename)

        sensorNames = ['Torso', 'FrontLeg', 'BackLeg']
        motorNames = ['Torso_BackLeg', 'Torso_FrontLeg']
        pyrosim.Send_Sensor_Neuron(name = 0, linkName = sensorNames[0])
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = sensorNames[1])
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = sensorNames[2])

        pyrosim.Send_Motor_Neuron(name = 3, jointName = motorNames[0])
        pyrosim.Send_Motor_Neuron(name = 4, jointName = motorNames[1])

        num_neurons = len(sensorNames) + len(motorNames)
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
        row = random.randint(0, 2)
        col = random.randint(0, 1)
        self.weights[row, col] = random.random() * 2 - 1