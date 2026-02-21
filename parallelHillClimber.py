from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        # self.parent = SOLUTION()
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
        os.system("del brain*.nndf")
        os.system("del fitness*.nndf")
        
    
    def Evolve(self):
        # print("\nGeneration 0-------")
        # self.parent.Evaluate("GUI")
        self.Evaluate(self.parents)
        for i in range(c.numberOfGenerations):
            print(f"\nGeneration {i+1}-------")
            self.Evolve_For_One_Generation()



    def Evaluate(self, solutions):
        print("Evaluating one parent")
        for solution in solutions:
            solutions[solution].Start_Simulation("DIRECT")
        print()
        for solution in solutions:
            solutions[solution].Wait_For_Simulation_To_End()
            print("FITNESS: " + str(solutions[solution].fitness))


    def Show_Best(self):
        index_found = 0
        index_fitness = self.parents[index_found].fitness
        for i in self.parents.keys():
            if self.parents[i].fitness < self.parents[index_found].fitness:
                # then it was better at moving left
                index_found = i
                index_fitness = self.parents[i].fitness
        print(f"BEST SOLUTION: fitness {index_fitness} at index {index_found}")
        self.parents[index_found].Evaluate(directOrGUI="GUI")


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
    

    def Spawn(self):
        self.children = {}
        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1


    def Mutate(self):
        for i in self.children.keys():
            self.children[i].Mutate()
        # self.child.Mutate()


    def Select(self):
        # print("Select: weights")
        # print(self.parent.weights)
        # print(self.child.weights)
        for i in self.parents.keys():
            if self.parents[i].fitness > self.children[i].fitness:
                # parent underperformed child
                # child survives
                self.parents[i] = self.children[i]
                print("CHILD Selected")
            else:
                # parent outperformed child
                # parent survives
                print("PARENT Selected")


    def Print(self):
        print("PRINTING PARENT | CHILD")
        for i in self.parents.keys():
            print(f"{self.parents[i].fitness} | {self.children[i].fitness}")
        print()
        # print(f"\n\n{self.parent.fitness} | {self.child.fitness}\n")