#Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
#[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
#Type "help", "copyright", "credits" or "license()" for more information.

#!/usr/bin/Python3

import time
import os
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)

DEBUG=1 #To see debug warnings set to "1" otherwise "0"
Btime=500 # This sets the debounce time in milliseconds.

northButton=14
powerButton=4
westButton=15
southButton=18
eastButton=23

GPIO.setup(powerButton,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(powerButton, GPIO.FALLING, bouncetime=Btime) # GPIO might need to be switched to RISING to prevent bounceing. 

GPIO.setup(northButton,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(northButton, GPIO.FALLING, bouncetime=Btime)

GPIO.setup(westButton,GPIO.IN,pull_up_down = GPIO.PUD_UP)
WEST = GPIO.add_event_detect(westButton, GPIO.FALLING, bouncetime=Btime)

GPIO.setup(southButton,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(southButton, GPIO.FALLING, bouncetime=Btime)

GPIO.setup(eastButton,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(eastButton, GPIO.FALLING, bouncetime=Btime)

def zeroMode():
    if GPIO.event_detected(northButton):
        if(DEBUG):print("North button accidentally pressed")
                 
    if GPIO.event_detected(westButton):
        if(DEBUG):print("West button accidentally pressed")
      
    if GPIO.event_detected(eastButton):
        if(DEBUG):print("East button accidentally pressed")

    if GPIO.event_detected(southButton):
        if(DEBUG):print("South button accidentally pressed") 
        
    if GPIO.event_detected(powerButton):
        if(DEBUG):print("Power button accidentally pressed")

def cable():
    while True:
        if GPIO.event_detected(northButton):
            print("Motor 1 selected in cable mode.")
            motor1_spin()

        if GPIO.event_detected(westButton):
            print("Motor 2 selected in cable mode.")
            motor2_spin()
                
        if GPIO.event_detected(southButton):
            print("Motor 3 selected in cable mode.")
            motor3_spin()
                
        if GPIO.event_detected(eastButton):
            print("Motor 4 selected in cable mode.")
            motor4_spin()
            
        if GPIO.event_detected(powerButton):
            print("Exiting cable.")
            os.system('/home/pi/vibrate.sh') # Effector movement to signal user of exit. 
            main()
            
def motor1_spin():                
    while True:
        if GPIO.event_detected(northButton):
            print("void")
            
        if GPIO.event_detected(westButton):
            print("Motor 1 clock.")
            os.system('/home/pi/1_cw.sh')
                
        if GPIO.event_detected(southButton):
            print("void")
                
        if GPIO.event_detected(eastButton):
            print("Motor 1 counter.")
            os.system('/home/pi/1_ccw.sh')
        
        if GPIO.event_detected(powerButton):
            print("cable")
            cable()
            
def motor2_spin():
    while True:
        if GPIO.event_detected(northButton):
            print("void")
            
        if GPIO.event_detected(westButton):
            print("Motor 2 clock.")
            os.system('/home/pi/2_cw.sh')
                
        if GPIO.event_detected(southButton):
            print("void")
                
        if GPIO.event_detected(eastButton):
            print("Motor 2 counter.")
            os.system('/home/pi/2_ccw.sh')
        
        if GPIO.event_detected(powerButton):
            print("cable")
            cable()
         
def motor3_spin():
    while True:
        if GPIO.event_detected(northButton):
            print("void")
            
        if GPIO.event_detected(westButton):
            print("Motor 3 clock.")
            os.system('/home/pi/3_cw.sh')
                
        if GPIO.event_detected(southButton):
            print("void")
                
        if GPIO.event_detected(eastButton):
            print("Motor 3 counter.")
            os.system('/home/pi/3_ccw.sh')
        
        if GPIO.event_detected(powerButton):
            print("cable")
            cable()
    
def motor4_spin():
    while True:
        if GPIO.event_detected(northButton):
            print("void")
            
        if GPIO.event_detected(westButton):
            print("Motor 4 clock.")
            os.system('/home/pi/4_cw.sh')
                
        if GPIO.event_detected(southButton):
            print("void")
                
        if GPIO.event_detected(eastButton):
            print("Motor 4 counter.")
            os.system('/home/pi/4_ccw.sh')
        
        if GPIO.event_detected(powerButton):
            print("cable")
            cable()
         
def boo():
    if GPIO.event_detected(powerButton): 
        if(DEBUG):print("Wait 2 seconds")
        time.sleep (2) #After button press wait 2 seconds

        if GPIO.input(powerButton): #Test for continued button press. If not pressed run brew script.
            if(DEBUG):print("Run Brew script")
            os.system('/home/pi/brew.sh') # Execute the brew.sh bash script.
            zeroMode() # Clear the accidental button presses. 

        elif GPIO.input(powerButton) == False: # If button press continues, wait 3 more seconds.
            if(DEBUG):print("Waiting 2 more")
            os.system('/home/pi/vibrate.sh') # Effector movement to signal that the \
            zeroMode()
            time.sleep (2)
            if GPIO.input(powerButton): #If button press does not continue, run the cable function.
                if(DEBUG):print("Clearing zero position")
                os.system('/home/pi/clear_coordinates.sh') # Execute the brew.sh bash script.
            	os.system('/home/pi/all_tighten.sh')
                zeroMode()

        if GPIO.input(powerButton) == False: # If button press continues, wait 3 more seconds.
            if(DEBUG):print("Waiting another 2 seconds.")
            os.system('/home/pi/vibrate.sh') # Effector movement to signal that the \
            zeroMode()
            time.sleep (2)

            if GPIO.input(powerButton): #If button press does not continue, run the cable function.
                if(DEBUG):print("Going into cable")
                cable()

            elif GPIO.input(powerButton) == False: #If button press still continues, run shutdown script.
                if(DEBUG):print("Shutting Down")
                os.system('/home/pi/vibrate.sh') # Effector movement to signal that the \
                time.sleep (2)
                os.system('sudo shutdown -h now') # Execute the brew.sh bash script.

    if GPIO.event_detected(northButton):
        if(DEBUG):print("North button pressed")
        os.system('/home/pi/north.sh') #Moves effector "north" by a step number specified in "north.sh"
                 
    if GPIO.event_detected(westButton):
        if(DEBUG):print("West button pressed")
        os.system('/home/pi/west.sh')  #Moves effector "west" by a step number specified in "west.sh"     
      
    if GPIO.event_detected(eastButton):
        if(DEBUG):print("East button pressed")
        os.system('/home/pi/east.sh')  #Moves effector "east" by a step number specified in "east.sh"     

    if GPIO.event_detected(southButton):
        if(DEBUG):print("South button pressed")
        os.system('/home/pi/south.sh') #Moves effector "south" by a step number specified in "south.sh"

def main():
    while True:
        boo()
        
try:
    main()
    
except KeyboardInterrupt:
    print ("ctrl+c pressed, exiting Event.py")    
  
finally:
    GPIO.cleanup()

#End
