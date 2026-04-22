# CS-5060-Adv-Evolutionary-Robotics Final Project: Spiderbot
## Overall objective:
To create a spider-like robot, capable of moving 'fluently' in arbitrary terrain, with a brain capable of understanding it's environment, towards an arbitrary objective.

## Subcomponents:
- The Spiderbot
    - composed of at minimum 8 legs and a body.
        - Each leg will have 2 leg sections, upper and lower, and will come equipped with sensors, joints, and motors.
    - Body sensors:
        - Leg segment position/angle relative to body segment
        - A limbic system, consisting of the robot's internal orientation of it's body cube. How upright the robot is.
    - Environmental sensors:
        - If body segments touching the ground
        - Segment height from the terrain
        - If there is time, vision (difficult)
- Randomized environment 
    - Reasonable slope ranges. 
        - This will likely be composed with controlled random noise, or potentially Perlin noise, to generate the environment.
    - 'Fluent' proficiency in the environment
        - Defined by never letting it's body touch the ground and a heuristic "is the robot moving quickly enough in the environment" evaluation metric by the end of the robot's evolution.
- A goal post within the environment. 
    - This will either take the form of:
        - a set of coordinates for the robot to path towards (if there's time, coordinates set by the cursor's ray traced to a point on the environment)
        - a cube in the environment that can be moved. (The robot will either need to acquire and keep vision of the cube, or be given the cube's position in a set of sensor neurons.)
    - This goal post will be able to be moved within one iteration of the simulation, an arbitrary number of times, and the robot will attempt to pathfind to the new goal.

## Milestone 1:
Deadline: 04/07/2026

1st milestone: I will create the Spiderbot in simulation, and prove that it is capable of locomotion.

### Goals:
- [x] Spiderbot body is assembled
    - [x] Body segment
    - [x] 8 legs
        - [x] 2 leg segments per leg
    - [x] Sensor neurons for each
        - To be expanded upon later, for now, a simple "is touching the ground" will suffice
    - [x] Motor neurons for each


Proof of goals:
- [x] Record a video of the Spiderbot after evolving locomotion in a direction.

Hard-coded body is OK, because the robot will not be evolving its body. Hard-coded synapse connectivity also OK, will presume fully connected layers. (Only sensor and motor needed for this demonstration, hidden neurons will be for the following milestone)

Currently, the bottleneck in Spiderbot evolution is that it cannot move its legs forward and backwards, how a spider would actually move. The joints will need to be modified to allow more degrees of freedom for future tests.

## Milestone 2:
Deadline: 04/14/2026

2nd milestone: I will improve the Spiderbot's brain to include hidden neurons, and show proof that hidden neurons are included in the neural net, and that the neuron values and synapse weights are updated across evolution steps.

### Goals:
- [x] Implement hidden neurons into the neural net
    - [x] Dynamic sizing of hidden neurons (as many as needed)
    - [x] Connectivity to Sensor neurons
    - [x] Connectivity to Motor neurons
    - [x] Implementation of at least one layer of hidden neurons
    - [ ] Optional: Support for multiple layers of hidden neurons
    - [ ] Optional: Support for 'memory' synapse connections, synapses that start and end on the same layer

## Milestone 3:
Deadline: 04/21/2026

3rd milestone: I will create a randomly generated environment for the Spiderbot to inhabit. I will prove that the Spiderbot is capable of locomotion without it's body touching the ground in this environment and, if possible, navigation. Locomotion being defined as successful movement to the right in a straight-ish line, navigation being defined as choosing a path around obstacles that improves navigation time.

- [ ] Random environment generation
    - [ ] some randomly generated environmental terrain
    - [ ] traversable by the spiderbot (spiderbot still needs some work to get moving well)
    - [ ] Optional: spiderbot body and sensor  modification to allow for better traversal

References: I found [this](https://www.youtube.com/watch?v=8V1ZrdBZvXg) helpful YouTube video, with associated [GitHub](https://github.com/liusida/learning_pybullet/blob/master/examples/mesh/floor.py) that helped to explain the problem. 


## Milestone 4:
Deadline: 04/28/2026

4th milestone: I will create a `goal post`, either a random coordinate or a cube in the environment, that the Spiderbot will attempt to move towards rather than a hard-coded direction. I will show proof that the Spiderbot moves towards this `goal post` regardless of where it is positioned. This will be demonstrated either through repeated trials or, if possible, through moving the `goal post` and verifying that the Spiderbot changes to move towards it's new position.

- [ ] Random goal
    - [ ] Minimum implementation: goal coordinates are fed in as sensor input and given to the robot
    - [ ] If there is time, a goal object
    - [ ] If there is time, a goal object that resets to a new position in the world after the robot approaches it