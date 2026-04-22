import pybullet as p
import random
import numpy as np

class WORLD:
    def __init__(self):
        # # Load the floor plane
        # self.planeID = p.loadURDF("plane.urdf")

        # Randomly generate a world plane for the robot to stand on
        # for testing, random will be seeded
        # random.seed(10)

        heightRange = 0.05
        numHeightfieldRows = 100
        numHeightfieldColumns = 100
        heightfieldData = np.zeros(
            shape=[numHeightfieldColumns, numHeightfieldRows], dtype=float)

        # Calculate vertices accumutively
        for i in range(int(numHeightfieldColumns/2)):
            for j in range(int(numHeightfieldRows)):
                n1 = 0
                n2 = 0
                if j > 0:
                    n1 = heightfieldData[i, j-1]
                if i > 0:
                    n2 = heightfieldData[i-1, j]
                else:
                    n2 = n1
                noise = random.uniform(-heightRange,
                                        heightRange)
                heightfieldData[i, j] = (n1+n2)/2 + noise

        heightfieldData_inv = heightfieldData[::-1,:]
        heightfieldData_2 = np.concatenate((heightfieldData_inv, heightfieldData))
        # print(heightfieldData_2)

        col,row = heightfieldData_2.shape
        heightfieldData_2 = heightfieldData_2.reshape(-1)

        terrainShape = p.createCollisionShape(shapeType=p.GEOM_HEIGHTFIELD, heightfieldData=heightfieldData_2, meshScale=[0.5,0.5,1],
                                                numHeightfieldRows=row, numHeightfieldColumns=col)
        terrain = p.createMultiBody(0, terrainShape)
        p.resetBasePositionAndOrientation(terrain, [0, 0, 0], [0, 0, 0, 1])

        # Load the world link
        p.loadSDF("world.sdf")