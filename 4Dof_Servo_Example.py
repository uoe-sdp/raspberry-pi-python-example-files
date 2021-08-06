From PCA9685 import PCA9685 
import time

pwm = PCA9685() 

pwm.setServoPulse(0,500) 
time.sleep(0.5)
pwm.setServoPulse(1,1000) 
time.sleep(0.5)
pwm.setServoPulse(2,1500) 
time.sleep(0.5)
pwm.setServoPulse(3,2000) 
time.sleep(0.5)
pwm.setServoPulse(4,2500) 
time.sleep(0.5)

#servo port numbers available = 0-15
#500 = 0 degrees, 1000 = 45 degrees, 1500 = 90 degrees, 2000 = 135 degrees, 2500 = 180 degrees 