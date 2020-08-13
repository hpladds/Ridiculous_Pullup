#! /bin/bash

/home/pi/brew_flow.sh & #Kettle pour for bloom
python /home/pi/cup_movement.py  #cup movement for bloom
python /home/pi/cup_movement1.py
sleep 10
python /home/pi/go_home.py
