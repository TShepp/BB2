# Tests smooth motion of camera servo
#!/usr/home/pi

import pigpio
import time

pi = pigpio.pi() # Connect to local Pi

pi.set_servo_pulsewidth(17, 1100)
time.sleep(1)
pi.set_servo_pulsewidth(17, 1500)
time.sleep(1)
pi.set_servo_pulsewidth(17, 2000)
time.sleep(1)
pi.set_servo_pulsewidth(17, 1500)

pi.stop()