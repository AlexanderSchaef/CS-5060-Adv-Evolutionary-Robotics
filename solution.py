import numpy as np
import random
import pyrosim.pyrosim as pyrosim
import os

class SOLUTION:
    def __init__(self):
                
        z = np.zeros((3,2))
        for i in range(3):
            for j in range(2):
                z[i][j] = random.random()
        self.weights = z * 2 - 1

    
    def Evaluate(self):
        self.Create_World()

        self.Create_Robot()

        os.system("python3 simulate.py")
        fitnessFile = "fitness.txt"
        with open("fitness.txt", "r") as file:
            self.fitness = float(file.read().strip())



    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        pyrosim.Send_Cube(name="Box", pos=[2,2,0.5], size=[1,1,1])

        pyrosim.End()


    def Create_Robot(self):
        x = 0
        y = 0
        z = 1.5
        self.Generate_Body(x,y,z)
        self.Generate_Brain()


    def Generate_Body(self, x,y,z):

        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[x,y,z], size=[1,1,1])
        
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                        type="revolute", position=[x-0.5,y,z-0.5])
        
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1])

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                        type="revolute", position=[x+0.5,y,z-0.5])

        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])

        pyrosim.End()


    def Generate_Brain(self):

        pyrosim.Start_NeuralNetwork("brain.nndf")

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


    def Mutate(self):
        row = random.randint(0, 2)
        col = random.randint(0, 1)
        self.weights[row, col] = random.random() * 2 - 1