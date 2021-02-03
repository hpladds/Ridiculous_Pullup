#! /bin/bash
sleep 1.5 
python /home/pi/Ridiculous/2_ccw.py 1 30 #to build additional momentum. 
python /home/pi/Ridiculous/2_ccw.py 4 60 #to build additional momentum. 
echo 1
python /home/pi/Ridiculous/2_ccw.py 80 40
echo 2 
python /home/pi/Ridiculous/2_cw.py 1 130 
echo return
sleep 55 
python /home/pi/Ridiculous/2_ccw.py 5 130 
echo reset pour height  
python /home/pi/Ridiculous/2_ccw.py 3 20
echo 1 
python /home/pi/Ridiculous/2_ccw.py 79.6875 20
echo 2 
python /home/pi/Ridiculous/2_ccw.py 75 20 
echo 3 
python /home/pi/Ridiculous/2_ccw.py 70.3125 20
echo 4 
python /home/pi/Ridiculous/2_ccw.py 65.625 20
echo 5
python /home/pi/Ridiculous/2_ccw.py 60.9375 20
echo 6 
python /home/pi/Ridiculous/2_ccw.py 56.25 20
echo 7
python /home/pi/Ridiculous/2_ccw.py 51.5625 20
echo 8
python /home/pi/Ridiculous/2_ccw.py 46.875 20 
echo 9
python /home/pi/Ridiculous/2_ccw.py 42.1875 20 
echo 10
python /home/pi/Ridiculous/2_ccw.py 37.5 20
echo 11
python /home/pi/Ridiculous/2_ccw.py 33.125 20 
echo 12
python /home/pi/Ridiculous/2_ccw.py 28.125 20 
echo 13
python /home/pi/Ridiculous/2_ccw.py 23.438 20
echo 14
python /home/pi/Ridiculous/2_ccw.py 18.75 20 
echo 15
python /home/pi/Ridiculous/2_ccw.py 14.0625 20
echo 16
python /home/pi/Ridiculous/2_cw.py 9.375 450
