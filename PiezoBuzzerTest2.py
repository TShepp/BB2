import sys
import RPi.GPIO as GPIO
from time import sleep
triggerPIN = 25
#Disable warnings (optional)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPIN,GPIO.OUT)
buzzer = GPIO.PWM(triggerPIN, 2000) #Set frequency to 1Khz
buzzer.start(10) #Set duty cycle to 10
sleep(1)
#buzzer.ChangeFrequency(500)


while True:
    buzzer.ChangeFrequency(440)
    sleep(0.1)
    buzzer.ChangeFrequency(494)
    sleep(0.1)
    buzzer.ChangeFrequency(523)
    sleep(0.1)
    buzzer.ChangeFrequency(587)
    sleep(0.1)
    buzzer.ChangeFrequency(659)
    sleep(0.1)
    buzzer.ChangeFrequency(698)
    sleep(0.1)
    buzzer.ChangeFrequency(784)
    sleep(0.1)
