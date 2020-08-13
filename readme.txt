# PourOver

The code for the Automated Pourover Coffee Machine consists of nine python scripts and one Bash script.

Eight of the python scripts control the 4 (model 28BY3-48) stepper motors. A pair of python scripts control each motor: one script (with the "cw" designation) turns the motorshaft in a clockwise direction, the second script (with a ccw designation) turns the motorshaft in a counterclockwise direction.

For example: 
Script "1_cw.py" turns the shaft of motor 1 in a clockwise direction.
Script "1_ccw.py" turns the motorshaft in a counterclockwise direction.
Script "2_cw.py" turns the shaft of motor 2 in a clockwise direction.
Script "2_ccw.py" turns the motorshaft in a counterclockwise direction, and so on.

From the Linux command line the following will rotate the motor's shaft at a rate of 1 step/millisecond for 10 steps:

$ python 1_cw.py 1 10

Each motor is fitted with a pulley gear wound with a cable. As the motorshaft rotates, the cable reels in or out depending upon the direction of the rotatation. In this way each motor works as a cable actuator. Three of these cable actuators are connected to central "effector" thereby creating a "Cable Robot."

The python script, "move_dist.py" coordinates the actions of the three stepper motors (the cable actuators) so as to control the movement of the "effector." Movement of the coffee cup is acheived by placing it upon the effector and executing the move_dist.py script.

The script move_dist.py coordinates the movement of all the motors. There are many variants of the moveLine.py script. Each variant directs a movement routine for the effector. For example, the following code...   
