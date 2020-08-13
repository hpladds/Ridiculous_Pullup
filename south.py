import RPi.GPIO as GPIO
import time
import sys
import math
#from  math import cos, sin, radians, sqrt, pow
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
coil_A_1_pin1 = 27 #orange  
coil_A_2_pin1 = 22 #yellow
coil_B_1_pin1 = 10 #pink
coil_B_2_pin1 = 9  #blue

coil_A_1_pin3 = 21 #orange
coil_A_2_pin3 = 20 #yellow
coil_B_1_pin3 = 16 #purple/pink
coil_B_2_pin3 = 12 #blue

coil_A_1_pin4 = 7 #orange
coil_A_2_pin4 = 8 #yellow
coil_B_1_pin4 = 25 #purple/pink
coil_B_2_pin4 = 24 #blue

delay = float(1)#Can't be smaller than 1 or miss steps. If increase, slows down movements
stepSize = 0.005737 #inches per step-- need to change this if change spool size on steppers
xHome = 4.9125 #inches-- home (center of triangle)
yHome = 2.9375 #inches-- home (center of triangle)
x = xHome
y = yHome
X3 = 5.01 #position of stepper3
Y3 = 8.69 #position of stepper3
X4 = 9.825 #position of stepper4
step1Leftover = 0
step3Leftover = 0
step4Leftover = 0

#if you run file without current_coords.txt in folder (or not accurate)
#comment out from here
F = open("/home/pi/Ridiculous/current_coords.txt","r")
x = float(F.readline())
y = float(F.readline())
step1Leftover = float(F.readline())
step3Leftover = float(F.readline())
step4Leftover = float(F.readline())

F.close()
#to here -- then uncomment for further runs


#distance = float(sys.argv [1]) #inches
#angle = float(sys.argv [2]) #degrees
#delay = float (sys.argv [1])
#steps = sys.argv [2]

GPIO.setup(coil_A_1_pin1, GPIO.OUT)
GPIO.setup(coil_A_2_pin1, GPIO.OUT)
GPIO.setup(coil_B_1_pin1, GPIO.OUT)
GPIO.setup(coil_B_2_pin1, GPIO.OUT)
GPIO.setup(coil_A_1_pin3, GPIO.OUT)
GPIO.setup(coil_A_2_pin3, GPIO.OUT)
GPIO.setup(coil_B_1_pin3, GPIO.OUT)
GPIO.setup(coil_B_2_pin3, GPIO.OUT)
GPIO.setup(coil_A_1_pin4, GPIO.OUT)
GPIO.setup(coil_A_2_pin4, GPIO.OUT)
GPIO.setup(coil_B_1_pin4, GPIO.OUT)
GPIO.setup(coil_B_2_pin4, GPIO.OUT)

#deltaX = distance*math.cos(math.radians(angle))
#deltaY = distance*math.sin(math.radians(angle))
#deltaL1 = deltaX*sqrt(1+pow((deltaY/deltaX),2))
#if (deltaX == 0)
#deltaL1 = deltaX*math.sqrt(1+math.pow((deltaX/deltaY),2))
#The problem here  seems to be in the square root and syntax for float vs int.

#print deltaX
#print deltaY
#print deltaL1

def moveStep(delay, step1, step3, step4):  
  if step1 == 1:
    setStep1(1, 0, 0, 0)
  else:
    if step1 == -1:
      setStep1(1, 0, 0, 1)
  if step3 == 1:
    setStep3(1, 0, 0, 0)
  else:
    if step3 == -1:
      setStep3(1, 0, 0, 1)
  if step4 == 1:
    setStep4(1, 0, 0, 0)
  else:
    if step4 == -1:
      setStep4(1, 0, 0, 1)
    #first step done
  time.sleep(delay)
  if step1 == 1:
    setStep1(1, 1, 0, 0)
  else:
    if step1 == -1:
      setStep1(0, 0, 0, 1)
  if step3 == 1:      
    setStep3(1, 1, 0, 0)
  else:
    if step3 == -1:
      setStep3(0, 0, 0, 1)  
  if step4 == 1:
    setStep4(1, 1, 0, 0)
  else:
    if step4 == -1:
      setStep4(0, 0, 0, 1)
    #second step done
  time.sleep(delay)
  if step1 == 1:
    setStep1(0, 1, 0, 0)
  else:
    if step1 == -1:
      setStep1(0, 0, 1, 1)
  if step3 == 1:
    setStep3(0, 1, 0, 0)
  else:
    if step3 == -1:
      setStep3(0, 0, 1, 1)      
  if step1 == 1:
    setStep1(0, 1, 0, 0)
  else:
    if step1 == -1:
      setStep1(0, 0, 1, 1)
    #third step done
  time.sleep(delay)
  if step1 == 1:
    setStep1(0, 1, 1, 0)
  else:
    if step1 == -1:
      setStep1(0, 0, 1, 0)
  if step3 == 1:
    setStep3(0, 1, 1, 0)
  else:
    if step3 == -1:
      setStep3(0, 0, 1, 0)      
  if step4 == 1:
    setStep4(0, 1, 1, 0)
  else:
    if step4 == -1:
      setStep4(0, 0, 1, 0)
    #fourth step done
  time.sleep(delay)
  if step1 == 1:
    setStep1(0, 0, 1, 0)
  else:
    if step1 == -1:
      setStep1(0, 1, 1, 0)
  if step3 == 1:
    setStep3(0, 0, 1, 0)
  else:
    if step3 == -1:
      setStep3(0, 1, 1, 0)      
  if step4 == 1:
    setStep4(0, 0, 1, 0)
  else:
    if step4 == -1:
      setStep4(0, 1, 1, 0)
    #fifth step done
  time.sleep(delay)
  if step1 == 1:
    setStep1(0, 0, 1, 1)
  else:
    if step1 == -1:
      setStep1(0, 1, 0, 0)
  if step3 == 1:
    setStep3(0, 0, 1, 1)
  else:
    if step3 == -1:
      setStep3(0, 1, 0, 0)
  if step4 == 1:
    setStep4(0, 0, 1, 1)
  else:
    if step4 == -1:
      setStep4(0, 1, 0, 0)
    #sixth step done
  time.sleep(delay)
  if step1 == 1:
    setStep1(0, 0, 0, 1)
  else:
    if step1 == -1:
      setStep1(1, 1, 0, 0)
  if step3 == 1:
    setStep3(0, 0, 0, 1)
  else:
    if step3 == -1:
      setStep3(1, 1, 0, 0)      
  if step4 == 1:
    setStep4(0, 0, 0, 1)
  else:
    if step4 == -1:
      setStep4(1, 1, 0, 0)
    #seventh step done
  time.sleep(delay)
  if step1 == 1:
    setStep1(1, 0, 0, 1)
  else:
    if step1 == -1:
      setStep1(1, 0, 0, 0)
  if step3 == 1:
    setStep3(1, 0, 0, 1)
  else:
    if step3 == -1:
      setStep3(1, 0, 0, 0)      
  if step4 == 1:
    setStep4(1, 0, 0, 1)
  else:
    if step4 == -1:
      setStep4(1, 0, 0, 0)
    #eigth step done
  time.sleep(delay)

def setStep1(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin1, w1) # blue
  GPIO.output(coil_A_2_pin1, w2) # pink/purple
  GPIO.output(coil_B_1_pin1, w3) # yellow
  GPIO.output(coil_B_2_pin1, w4) # orange

def setStep3(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin3, w1) # blue
  GPIO.output(coil_A_2_pin3, w2) # pink/purple
  GPIO.output(coil_B_1_pin3, w3) # yellow
  GPIO.output(coil_B_2_pin3, w4) # orange

def setStep4(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin4, w1) # blue
  GPIO.output(coil_A_2_pin4, w2) # pink/purple
  GPIO.output(coil_B_1_pin4, w3) # yellow
  GPIO.output(coil_B_2_pin4, w4) # orange

def moveLine (distance, angle):
  #steps = int(distance/stepSize) #need to add the remainder to loffsets for next move
  distance = float(distance)
  angle = float(angle)
  steps = int(abs(distance/stepSize))
  deltaX = distance*math.cos(math.radians(angle))
  deltaY = distance*math.sin(math.radians(angle))
  global x
  global y
  global step1Leftover
  global step3Leftover
  global step4Leftover
  
  for i in range(0, steps):
    step1 = 0
    step3 = 0
    step4 = 0
    deltaL1 = (x/math.sqrt(math.pow(x,2)+math.pow(y,2)))*(deltaX/steps)+(y/math.sqrt(math.pow(x,2)+math.pow(y,2)))*((deltaY/steps))

    deltaL1 = deltaL1+step1Leftover
    #print "Delta1: "
    #print deltaL1
    #print "step1Leftover: "
    #print step1Leftover
    if deltaL1 >= stepSize:
      step1 = 1
      step1Leftover = deltaL1-stepSize #deltaL1%stepSize
    elif deltaL1 <= -stepSize:
      step1 = -1
      step1Leftover = deltaL1+stepSize #deltaL1%-stepSize
    else:
      step1Leftover = deltaL1
      #print "1 didn't move"
      
    deltaL3 = -((X3-x)/math.sqrt(math.pow(x,2)-2*X3*x+math.pow(y,2)-2*Y3*y+math.pow(X3,2)+math.pow(Y3,2)))*(deltaX/steps)-((Y3-y)/math.sqrt(math.pow(x,2)-2*X3*x+math.pow(y,2)-2*Y3*y+math.pow(X3,2)+math.pow(Y3,2)))*(deltaY/steps)
    #print "Delta3: "
    #print deltaL3
    deltaL3 = deltaL3+step3Leftover

    if deltaL3 >= stepSize:
      step3 = 1
      step3Leftover = deltaL3-stepSize #deltaL3%stepSize
    elif deltaL3 <= -stepSize:
        step3 = -1
        step3Leftover = deltaL3+stepSize #deltaL3%-stepSize
    else:
      step3Leftover = deltaL3
      #print "3 didn't move"
      
    deltaL4 = -((X4-x)/math.sqrt(math.pow(x,2)-2*X4*x+math.pow(y,2)+math.pow(X4,2)))*(deltaX/steps)+(y/(math.sqrt(math.pow(x,2)-2*X4*x+math.pow(y,2)+math.pow(X4,2))))*(deltaY/steps)
    #print "Delta4: "
    #print deltaL4
    deltaL4 = deltaL4+step4Leftover

    if deltaL4 >= stepSize:
      step4 = 1
      step4Leftover = deltaL4-stepSize #deltaL4%stepSize
    #need to add code to update loffsets if deltaL1 < 0 or if there is a remainder
    elif deltaL4 <= -stepSize:
        step4 = -1
        step4Leftover = deltaL4+stepSize #deltaL4%-stepSize
         #need to add code to update loffsets if deltaL1 < 0 or if there is a remainder
    else:
      step4Leftover = deltaL4
      #print "4 didn't move"
      
    moveStep(float(delay)/1000.0, step1, step3, step4)
    #print "x: "
    #print x
    #print "y: "
    #print y
    x = x + deltaX/steps
    y = y + deltaY/steps

def moveCircle(degrees):
  
  global x
  global y
  global step1Leftover
  global step3Leftover
  global step4Leftover
  radius = math.sqrt(math.pow((x-xHome),2)+math.pow((y-yHome),2))
  startAngle = 0
  if y >= yHome:
    startAngle = math.acos((x-xHome)/radius)*180/math.pi #degrees
  elif y < yHome:
    startAngle = 360 - math.acos((x-xHome)/radius)*180/math.pi #degrees
  angle = startAngle
  degrees = float(degrees)
  steps = int(abs(((degrees/360)*2*math.pi*radius)/stepSize))
  
  for i in range(0, steps):
    step1 = 0
    step3 = 0
    step4 = 0

    deltaX = radius*math.cos((angle+degrees/steps)*math.pi/180)-radius*math.cos((angle)*math.pi/180)
    deltaY = radius*math.sin((angle+degrees/steps)*math.pi/180)-radius*math.sin((angle)*math.pi/180) 

    deltaL1 = (x/math.sqrt(math.pow(x,2)+math.pow(y,2)))*(deltaX)+(y/math.sqrt(math.pow(x,2)+math.pow(y,2)))*((deltaY))

    deltaL1 = deltaL1+step1Leftover
    if deltaL1 >= stepSize:
      step1 = 1
      step1Leftover = deltaL1-stepSize #deltaL1%stepSize
    elif deltaL1 <= -stepSize:
      step1 = -1
      step1Leftover = deltaL1+stepSize #deltaL1%-stepSize
    else:
      step1Leftover = deltaL1
      #print "1 didn't move"
      
    deltaL3 = -((X3-x)/math.sqrt(math.pow(x,2)-2*X3*x+math.pow(y,2)-2*Y3*y+math.pow(X3,2)+math.pow(Y3,2)))*(deltaX)-((Y3-y)/math.sqrt(math.pow(x,2)-2*X3*x+math.pow(y,2)-2*Y3*y+math.pow(X3,2)+math.pow(Y3,2)))*(deltaY)

    deltaL3 = deltaL3+step3Leftover

    if deltaL3 >= stepSize:
      step3 = 1
      step3Leftover = deltaL3-stepSize #deltaL3%stepSize
    elif deltaL3 <= -stepSize:
        step3 = -1
        step3Leftover = deltaL3+stepSize #deltaL3%-stepSize
    else:
      step3Leftover = deltaL3
      #print "3 didn't move"
      
    deltaL4 = -((X4-x)/math.sqrt(math.pow(x,2)-2*X4*x+math.pow(y,2)+math.pow(X4,2)))*(deltaX)+(y/(math.sqrt(math.pow(x,2)-2*X4*x+math.pow(y,2)+math.pow(X4,2))))*(deltaY)

    deltaL4 = deltaL4+step4Leftover

    if deltaL4 >= stepSize:
      step4 = 1
      step4Leftover = deltaL4-stepSize #deltaL4%stepSize
    #need to add code to update loffsets if deltaL1 < 0 or if there is a remainder
    elif deltaL4 <= -stepSize:
        step4 = -1
        step4Leftover = deltaL4+stepSize #deltaL4%-stepSize
         #need to add code to update loffsets if deltaL1 < 0 or if there is a remainder
    else:
      step4Leftover = deltaL4
      #print "4 didn't move"
      
    moveStep(float(delay)/1000.0, step1, step3, step4)


    angle = angle + degrees/steps
    x = x + deltaX
    y = y + deltaY

def moveCircle2(radius2, degrees):
  
  global x
  global y
  global step1Leftover
  global step3Leftover
  global step4Leftover
  #radius = math.sqrt(math.pow((x-xHome),2)+math.pow((y-yHome),2))
  startAngle = 0
  radius = math.sqrt(math.pow((x-xHome),2)+math.pow((y-yHome),2))

  if y >= yHome:
    startAngle = math.acos((x-xHome)/radius)*180/math.pi #degrees
  elif y < yHome:
    startAngle = 360 - math.acos((x-xHome)/radius)*180/math.pi #degrees
  angle = startAngle
  degrees = float(degrees)
  steps = int(abs(((degrees/360)*2*math.pi*radius2)/stepSize))
  
  for i in range(0, steps):
    step1 = 0
    step3 = 0
    step4 = 0

    deltaX = radius2*math.cos((angle+degrees/steps)*math.pi/180)-radius2*math.cos((angle)*math.pi/180)
    deltaY = radius2*math.sin((angle+degrees/steps)*math.pi/180)-radius2*math.sin((angle)*math.pi/180) 

    deltaL1 = (x/math.sqrt(math.pow(x,2)+math.pow(y,2)))*(deltaX)+(y/math.sqrt(math.pow(x,2)+math.pow(y,2)))*((deltaY))

    deltaL1 = deltaL1+step1Leftover
    if deltaL1 >= stepSize:
      step1 = 1
      step1Leftover = deltaL1-stepSize #deltaL1%stepSize
    elif deltaL1 <= -stepSize:
      step1 = -1
      step1Leftover = deltaL1+stepSize #deltaL1%-stepSize
    else:
      step1Leftover = deltaL1
      #print "1 didn't move"
      
    deltaL3 = -((X3-x)/math.sqrt(math.pow(x,2)-2*X3*x+math.pow(y,2)-2*Y3*y+math.pow(X3,2)+math.pow(Y3,2)))*(deltaX)-((Y3-y)/math.sqrt(math.pow(x,2)-2*X3*x+math.pow(y,2)-2*Y3*y+math.pow(X3,2)+math.pow(Y3,2)))*(deltaY)

    deltaL3 = deltaL3+step3Leftover

    if deltaL3 >= stepSize:
      step3 = 1
      step3Leftover = deltaL3-stepSize #deltaL3%stepSize
    elif deltaL3 <= -stepSize:
        step3 = -1
        step3Leftover = deltaL3+stepSize #deltaL3%-stepSize
    else:
      step3Leftover = deltaL3
      #print "3 didn't move"
      
    deltaL4 = -((X4-x)/math.sqrt(math.pow(x,2)-2*X4*x+math.pow(y,2)+math.pow(X4,2)))*(deltaX)+(y/(math.sqrt(math.pow(x,2)-2*X4*x+math.pow(y,2)+math.pow(X4,2))))*(deltaY)

    deltaL4 = deltaL4+step4Leftover

    if deltaL4 >= stepSize:
      step4 = 1
      step4Leftover = deltaL4-stepSize #deltaL4%stepSize
    #need to add code to update loffsets if deltaL1 < 0 or if there is a remainder
    elif deltaL4 <= -stepSize:
        step4 = -1
        step4Leftover = deltaL4+stepSize #deltaL4%-stepSize
         #need to add code to update loffsets if deltaL1 < 0 or if there is a remainder
    else:
      step4Leftover = deltaL4
      #print "4 didn't move"
      
    moveStep(float(delay)/1000.0, step1, step3, step4)


    angle = angle + degrees/steps
    x = x + deltaX
    y = y + deltaY

def moveCircle3(radius3, degrees, dirCtrAngle):
  #This makes direction the direction from  current position the center should be 1 radius3 away in the direction dirCtrAngle
  
  global x
  global y
  global step1Leftover
  global step3Leftover
  global step4Leftover
  #radius = math.sqrt(math.pow((x-xHome),2)+math.pow((y-yHome),2))
  startAngle = 0
  #radius = math.sqrt(math.pow((x-xHome),2)+math.pow((y-yHome),2))

  if 0 <= dirCtrAngle < 180:
    startAngle = dirCtrAngle + 180 #degrees
  elif 180 <= dirCtrAngle < 360 :
    startAngle = dirCtrAngle - 180 #degrees
  angle = startAngle
  degrees = float(degrees)
  steps = int(abs(((degrees/360)*2*math.pi*radius3)/stepSize))
  
  for i in range(0, steps):
    step1 = 0
    step3 = 0
    step4 = 0

    deltaX = radius3*math.cos((angle+degrees/steps)*math.pi/180)-radius3*math.cos((angle)*math.pi/180)
    deltaY = radius3*math.sin((angle+degrees/steps)*math.pi/180)-radius3*math.sin((angle)*math.pi/180) 

    deltaL1 = (x/math.sqrt(math.pow(x,2)+math.pow(y,2)))*(deltaX)+(y/math.sqrt(math.pow(x,2)+math.pow(y,2)))*((deltaY))

    deltaL1 = deltaL1+step1Leftover
    if deltaL1 >= stepSize:
      step1 = 1
      step1Leftover = deltaL1-stepSize #deltaL1%stepSize
    elif deltaL1 <= -stepSize:
      step1 = -1
      step1Leftover = deltaL1+stepSize #deltaL1%-stepSize
    else:
      step1Leftover = deltaL1
      #print "1 didn't move"
      
    deltaL3 = -((X3-x)/math.sqrt(math.pow(x,2)-2*X3*x+math.pow(y,2)-2*Y3*y+math.pow(X3,2)+math.pow(Y3,2)))*(deltaX)-((Y3-y)/math.sqrt(math.pow(x,2)-2*X3*x+math.pow(y,2)-2*Y3*y+math.pow(X3,2)+math.pow(Y3,2)))*(deltaY)

    deltaL3 = deltaL3+step3Leftover

    if deltaL3 >= stepSize:
      step3 = 1
      step3Leftover = deltaL3-stepSize #deltaL3%stepSize
    elif deltaL3 <= -stepSize:
        step3 = -1
        step3Leftover = deltaL3+stepSize #deltaL3%-stepSize
    else:
      step3Leftover = deltaL3
      #print "3 didn't move"
      
    deltaL4 = -((X4-x)/math.sqrt(math.pow(x,2)-2*X4*x+math.pow(y,2)+math.pow(X4,2)))*(deltaX)+(y/(math.sqrt(math.pow(x,2)-2*X4*x+math.pow(y,2)+math.pow(X4,2))))*(deltaY)

    deltaL4 = deltaL4+step4Leftover

    if deltaL4 >= stepSize:
      step4 = 1
      step4Leftover = deltaL4-stepSize #deltaL4%stepSize
    #need to add code to update loffsets if deltaL1 < 0 or if there is a remainder
    elif deltaL4 <= -stepSize:
        step4 = -1
        step4Leftover = deltaL4+stepSize #deltaL4%-stepSize
         #need to add code to update loffsets if deltaL1 < 0 or if there is a remainder
    else:
      step4Leftover = deltaL4
      #print "4 didn't move"
      
    moveStep(float(delay)/1000.0, step1, step3, step4)


    angle = angle + degrees/steps
    x = x + deltaX
    y = y + deltaY



def goHome():
  global x
  global y
  global step1Leftover
  global step3Leftover
  global step4Leftover
  radius = math.sqrt(math.pow((x-xHome),2)+math.pow((y-yHome),2))
  startAngle = 0
  if y >= yHome:
    startAngle = math.acos((x-xHome)/radius)*180/math.pi #degrees
  elif y < yHome:
    startAngle = 360 - math.acos((x-xHome)/radius)*180/math.pi #degrees
  moveLine(radius,180+startAngle)
  
while True:
#distance = 2.5 #inches
# angle = 60 #degrees

  moveLine(.0625, 270)

  F = open("/home/pi/Ridiculous/current_coords.txt","w")
  F.write(str(x))
  F.write("\n")
  F.write(str(y))
  F.write("\n")
  F.write(str(step1Leftover))
  F.write("\n")
  F.write(str(step3Leftover))
  F.write("\n")
  F.write(str(step4Leftover))
  F.close()
  break
