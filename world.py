import pybullet as p

class WORLD:
    def __init__(self):
        # Load the floor plane
        self.planeID = p.loadURDF("plane.urdf")
        # Load the world link
        p.loadSDF("world.sdf")