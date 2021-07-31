'''
Object detection and tracking with OpenCV
    ==> Real Time tracking with Pan-Tilt servos and Stepper motors
    Pan-Tilt based on original tracking object code developed by Adrian Rosebrock
    Visit original post: https://www.pyimagesearch.com/2016/05/09/opencv-rpi-gpio-and-gpio-zero-on-the-raspberry-pi/
    Stepper motor based on Adafruit code developed by Simon Monk
    Visit original post: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-10-stepper-motors/overview
Developed by Tyler Schoeppner - tyler.schoeppner.com @ 7Oct2020 
'''

# import the necessary packages
from __future__ import print_function
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import os
import RPi.GPIO as GPIO
os.system('sudo pigpiod')
import pigpio
import board
import busio as io
import adafruit_ht16k33.matrix
from test_LEDmatrix import ledsoff, neutralexp, surpriseexp, joyexp, angerexp, tiredexp

# setup for LED matrix
i2c = io.I2C(board.SCL, board.SDA)
matrix = adafruit_ht16k33.matrix.Matrix16x8(i2c)

# define Servos GPIOs
#tiltServo = 17

# turn on movement for the camera servo
#pi = pigpio.pi()

# setup wheel servo motors
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#coil_A_1_pin = 4
#coil_A_2_pin = 26
#coil_B_1_pin = 23
#coil_B_2_pin = 24

#coil2_A_1_pin = 16
#coil2_A_2_pin = 22
#coil2_B_1_pin = 27
#coil2_B_2_pin = 20

#StepCount=8
#Seq = [
#  [1,0,0,0],
#  [1,1,0,0],
#  [0,1,0,0],
#  [0,1,1,0],
#  [0,0,1,0],
#  [0,0,1,1],
#  [0,0,0,1],
#  [1,0,0,1]
#    ]

# define wheel speed
#delay = 8
#speed = delay / 10000.0

# setup the pins on the drive stepper motors
# first stepper motor
#GPIO.setup(coil_A_1_pin, GPIO.OUT)
#GPIO.setup(coil_A_2_pin, GPIO.OUT)
#GPIO.setup(coil_B_1_pin, GPIO.OUT)
#GPIO.setup(coil_B_2_pin, GPIO.OUT)

# second stepper motor
#GPIO.setup(coil2_A_1_pin, GPIO.OUT)
#GPIO.setup(coil2_A_2_pin, GPIO.OUT)
#GPIO.setup(coil2_B_1_pin, GPIO.OUT)
#GPIO.setup(coil2_B_2_pin, GPIO.OUT)
 
#def setStepleft(w1, w2, w3, w4):
#    GPIO.output(coil_A_1_pin, w1)
#    GPIO.output(coil_A_2_pin, w2)
#    GPIO.output(coil_B_1_pin, w3)
#    GPIO.output(coil_B_2_pin, w4)
    
#def setStepright(k1, k2, k3, k4):
#    GPIO.output(coil2_A_1_pin, k1)
#    GPIO.output(coil2_A_2_pin, k2)
#    GPIO.output(coil2_B_1_pin, k3)
#    GPIO.output(coil2_B_2_pin, k4)
            
#def spinleft(speed, steps):
#    for i in range(steps):
#        for j in range(StepCount):
#            setStepright(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
#            time.sleep(speed)
#        for j in reversed(range(StepCount)):
#            setStepleft(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
#            time.sleep(speed)
            
#def spinright(speed, steps):
#    for i in range(steps):
#        for j in range(StepCount):
#            setStepleft(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
#            time.sleep(speed)
#        for j in reversed(range(StepCount)):
#            setStepright(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
#            time.sleep(speed)
    
# position servos to present object at center of the frame
#def mapServoPosition (x, y):
#    global tiltAngle
#    global spinAngle
#    if (x < 100):
#        spinAngle = 50
#        spinleft(speed, spinAngle)
#        print("spinleft")
        
#    if (x > 400):
#        spinAngle = 50
#        spinright(speed, spinAngle)
#        print("spinright")
    
#    if (y < 110):
#        tiltAngle -= 33
#        if tiltAngle < 1100:
#            tiltAngle = 1100
#        pi.set_servo_pulsewidth(tiltServo, tiltAngle)
 
#    if (y > 200):
#        tiltAngle += 33
#        if tiltAngle > 2100:
#            tiltAngle = 2100
#        pi.set_servo_pulsewidth(tiltServo, tiltAngle)
        
# initialize the video stream and allow the camera sensor to warmup
print("[INFO] waiting for camera to warmup...")
vs = VideoStream(0).start()
time.sleep(2.0)

# define the lower and upper boundaries of the object
# to be tracked in the HSV color space
colorLower = (70, 70, 25)
colorUpper = (174, 255, 255)

# Initialize servos
#tiltAngle = 1800
#spinAngle = 0

# positioning Tilt servos at initial position
#pi.set_servo_pulsewidth(tiltServo, tiltAngle)

# initial expression
# possible exp: neutralexp, surpriseexp, joyexp, angerexp, tiredexp

tiredexp()
time.sleep(5)
surpriseexp()
time.sleep(5)
ledsoff()

#foundobject = False
    
# loop over the frames from the video stream
while True:
    # grab the next frame from the video stream, Invert 180o, resize the
    # frame, and convert it to the HSV color space
    frame = vs.read()
    frame = imutils.resize(frame, width=500)
    frame = imutils.rotate(frame, angle=180)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # construct a mask for the object color, then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    mask = cv2.inRange(hsv, colorLower, colorUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # find contours in the mask and initialize the current
    # (x, y) center of the object
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        #foundobject = True

        # only proceed if the radius meets a minimum size
        if radius > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),
                (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            #neutralexp()
            #print(center)
            
            # position Servo at center of circle
            #mapServoPosition(int(x), int(y))

    # show the frame to our screen
    cv2.imshow("Frame", frame)
    
    # if [ESC] key is pressed, stop the loop
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
            break

# do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff \n")
pi.set_servo_pulsewidth(tiltServo, 1800)
matrix.fill(0)
cv2.destroyAllWindows()
vs.stop()
    
    
    
    
    
    