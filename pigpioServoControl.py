# similar code to online angleServoCtrl but with pigpio smoother movement

from time import sleep
import pigpio
def setServoAngle(servo, angle):
    #pwm = GPIO.PWM(servo, 50)
    pi = pigpio.pi()
    
    #pwm.start(8)
    pi.set_servo_pulsewidth(servo, 1800)
    
    #dutyCycle = angle / 18. + 3.
    dutyCycle = ((270. - 6. * angle) / 540.) + 21
    
    #pwm.ChangeDutyCycle(dutyCycle)
    pi.set_servo_pulsewidth(servo, dutyCycle)
    
    sleep(0.3)
    #pwm.stop()
    pi.stop()
    
if __name__ == '__main__':
    import sys
    servo = int(sys.argv[1])
    #GPIO.setup(servo, GPIO.OUT)
    setServoAngle(servo, int(sys.argv[2]))
    #GPIO.cleanup()