# CS-5060-Adv-Evolutionary-Robotics Final Project: Spiderbot
## Overall objectives:
To create a spider-like robot, capable of moving 'fluently' in arbitrary terrain, with a brain capable of understanding it's environment, towards an arbitrary objective.

## Subcomponents:
- The spiderbot
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

### Goals:
- [ ] Spiderbot body is assembled
    - [x] Body segment
    - [ ] 8 legs
        - [ ] 2 leg segments per leg
    - [ ] Sensor neurons for each
        - To be expanded upon later, for now, a simple "is touching the ground" will suffice
    - [ ] Motor neurons for each
    - [ ] Robot must successfully for this demonstration evolve movement to the right without falling over (the precise "negative reward if body touching the ground" implementation will be for a later milestone)

Proof of goals:
- [] Record a video of the spiderbot before and after evolving locomotion in a direction.

Hard-coded body is OK, because the robot will not be evolving its body. Hard-coded synapse connectivity also OK, will presume fully connected layers. (Only sensor and motor needed for this demonstration, hidden neurons will be for the following milestone)