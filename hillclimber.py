from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    
    def Evolve(self):
        print("\nGeneration 0-------")
        self.parent.Evaluate()
        for i in range(c.numberOfGenerations):
            print(f"\nGeneration {i+1}-------")
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Print()
        self.Select()
    

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)


    def Mutate(self):
        self.child.Mutate()


    def Select(self):
        # print("Select: weights")
        # print(self.parent.weights)
        # print(self.child.weights)
        if self.parent.fitness < self.child.fitness:
            self.parent = self.child
            print("CHILD Selected")
        else:
            print("PARENT Selected")


    def Print(self):
        print(f"\n\n{self.parent.fitness} | {self.child.fitness}\n")