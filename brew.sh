#! /bin/bash

/home/pi/Ridiculous/brew_flow.sh & #Kettle pour for bloom
python /home/pi/Ridiculous/cup_movement.py  #cup movement for bloom
python /home/pi/Ridiculous/cup_movement1.py
sleep 1
python /home/pi/Ridiculous/go_home.py
