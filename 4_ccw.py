import RPi.GPIO as GPIO
import time
import sys
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
#enable_pin = 18 #L293D Driver IC only
coil_A_1_pin = 7 #orange
coil_A_2_pin = 8 #yellow
coil_B_1_pin = 25 #pink
coil_B_2_pin = 24 #blue

delay = float (sys.argv [1]) 
steps = int  (sys.argv [2]) 

#GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
 
#GPIO.output(enable_pin, 1)

def backwards(delay, steps):  
  for i in range(0, steps):
    setStep(1, 0, 0, 1)
    time.sleep(delay)
    setStep(0, 0, 0, 1)
    time.sleep(delay)
    setStep(0, 0, 1, 1)
    time.sleep(delay)
    setStep(0, 0, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 0, 0)
    time.sleep(delay)
    setStep(1, 1, 0, 0)
    time.sleep(delay)
    setStep(1, 0, 0, 0)
    time.sleep(delay)

def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1) # blue
  GPIO.output(coil_A_2_pin, w2) # pink/purple
  GPIO.output(coil_B_1_pin, w3) # yellow
  GPIO.output(coil_B_2_pin, w4) # orange
 
while True:
  backwards (float(delay)/1000.0, int(steps))
  break
