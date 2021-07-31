import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
coil_A_1_pin = 4
coil_A_2_pin = 26
coil_B_1_pin = 23
coil_B_2_pin = 24

coil2_A_1_pin = 16
coil2_A_2_pin = 22
coil2_B_1_pin = 27
coil2_B_2_pin = 20
 
# adjust if different
StepCount=8
Seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
    ]

############################################
# Setup the pins on the drive stepper motors
# First stepper motor
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# Second stepper motor
GPIO.setup(coil2_A_1_pin, GPIO.OUT)
GPIO.setup(coil2_A_2_pin, GPIO.OUT)
GPIO.setup(coil2_B_1_pin, GPIO.OUT)
GPIO.setup(coil2_B_2_pin, GPIO.OUT)
 
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)
    
    GPIO.output(coil2_A_1_pin, w1)
    GPIO.output(coil2_A_2_pin, w2)
    GPIO.output(coil2_B_1_pin, w3)
    GPIO.output(coil2_B_2_pin, w4)
 
def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
 
def backwards(delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
 
if __name__ == '__main__':
    while True:
        delay = input("Time Delay (ms)?")
        #delay = 7
        steps = input("How many steps forward? ")
        #steps = 500
        forward(int(delay) / 10000.0, int(steps))
        steps = input("How many steps backwards? ")
        backwards(int(delay) / 10000.0, int(steps))