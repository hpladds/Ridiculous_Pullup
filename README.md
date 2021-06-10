# Ridiculous_Pullup

The code for the Ridiculous Coffee Machine consists of python scripts that control and coordinate the movement of the (model 28BY3-48) stepper motors, and a bash script that calls those python scripts in a specified sequence.

Two python scripts control each motor: scripts with a "cw" designation turn the motorshaft in a clockwise direction. Scripts with the "ccw" designation turn it in a counterclockwise direction.

For example: 
Script "1_cw.py" turns the shaft of motor 1 in a clockwise direction.
Script "1_ccw.py" turns the motorshaft in a counterclockwise direction.

From the Linux command line the following will rotate the motor's shaft in a clockwise direction at a rate of 1 step/millisecond for 10 steps:

$ python 1_cw.py 1 10

Each motor is fitted with a pulley gear wound with a cable. As the motorshaft rotates the cable reels in or out thereby creating a cable actuator. Three of these actuators are connected to central "effector" creating a "cable robot."

The python script, "move_dist.py" coordinates the movements of the actuators and directs the movement of the "effector." Movement of the coffee cup is acheived by placing it upon the effector. A fourth actuator controls the rate at which boiling water is poured from a kettle over coffee grinds and into a cup below.
