# CS-5060-Adv-Evolutionary-Robotics Final Project: Spiderbot
## Overall objectives:
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
- [ ] Spiderbot body is assembled
    - [x] Body segment
    - [ ] 8 legs
        - [ ] 2 leg segments per leg
    - [ ] Sensor neurons for each
        - To be expanded upon later, for now, a simple "is touching the ground" will suffice
    - [ ] Motor neurons for each
    - [ ] Robot must successfully for this demonstration evolve movement to the right without falling over (the precise "negative reward if body touching the ground" implementation will be for a later milestone)

Proof of goals:
- [] Record a video of the Spiderbot before and after evolving locomotion in a direction.

Hard-coded body is OK, because the robot will not be evolving its body. Hard-coded synapse connectivity also OK, will presume fully connected layers. (Only sensor and motor needed for this demonstration, hidden neurons will be for the following milestone)

## Milestone 2:
Deadline: 04/14/2026

2nd milestone: I will improve the Spiderbot's brain to include hidden neurons, and show proof that hidden neurons are included in the neural net, and that the neuron values and synapse weights are updated across evolution steps.

## Milestone 3:
Deadline: 04/21/2026

3rd milestone: I will create a randomly generated environment for the Spiderbot to inhabit. I will prove that the Spiderbot is capable of locomotion without it's body touching the ground in this environment and, if possible, navigation. Locomotion being defined as successful movement to the right in a straight-ish line, navigation being defined as choosing a path around obstacles that improves navigation time.

## Milestone 4:
Deadline: 04/28/2026

4th milestone: I will create a `goal post`, either a random coordinate or a cube in the environment, that the Spiderbot will attempt to move towards rather than a hard-coded direction. I will show proof that the Spiderbot moves towards this `goal post` regardless of where it is positioned. This will be demonstrated either through repeated trials or, if possible, through moving the `goal post` and verifying that the Spiderbot changes to move towards it's new position.