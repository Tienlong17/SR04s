# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import math 
from board import SCL, SDA
import busio

# Import the PCA9685 module. Available in the bundle and here:
#   https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)
# You can optionally provide a finer tuned reference clock speed to improve the accuracy of the
# timing pulses. This calibration will be specific to each board and its environment. See the
# calibration.py example in the PCA9685 driver.
# pca = PCA9685(i2c, reference_clock_speed=25630710)
pca.frequency = 50

# To get the full range of the servo you will likely need to adjust the min_pulse and max_pulse to
# match the stall points of the servo.
# This is an example for the Sub-micro servo: https://www.adafruit.com/product/2201
# servo1 = servo.Servo(pca.channels[7], min_pulse=580, max_pulse=2350)
# This is an example for the Micro Servo - High Powered, High Torque Metal Gear:
#   https://www.adafruit.com/product/2307
# servo1 = servo.Servo(pca.channels[7], min_pulse=500, max_pulse=2600)
# This is an example for the Standard servo - TowerPro SG-5010 - 5010:
#   https://www.adafruit.com/product/155
# servo1 = servo.Servo(pca.channels[7], min_pulse=400, max_pulse=2400)
# This is an example for the Analog Feedback Servo: https://www.adafruit.com/product/1404
# servo1 = servo.Servo(pca.channels[7], min_pulse=600, max_pulse=2500)
# This is an example for the Micro servo - TowerPro SG-92R: https://www.adafruit.com/product/169
# servo1 = servo.Servo(pca.channels[7], min_pulse=500, max_pulse=2400)

# The pulse range is 750 - 2250 by default. This range typically gives 135 degrees of
# range, but the default is to use 180 degrees. You can specify the expected range if you wish:
# servo1 = servo.Servo(pca.channels[7], actuation_range=135)
servo0 = servo.Servo(pca.channels[0], min_pulse=440, max_pulse=2400)
servo1 = servo.Servo(pca.channels[1], min_pulse=440, max_pulse=2400)
servo2 = servo.Servo(pca.channels[2], min_pulse=440, max_pulse=2400)
servo3 = servo.Servo(pca.channels[3], min_pulse=440, max_pulse=2400)

servo4 = servo.Servo(pca.channels[4], min_pulse=440, max_pulse=2400)
servo5 = servo.Servo(pca.channels[5], min_pulse=440, max_pulse=2400)
servo6 = servo.Servo(pca.channels[6], min_pulse=440, max_pulse=2400)
servo7 = servo.Servo(pca.channels[7], min_pulse=440, max_pulse=2400)

servo8 = servo.Servo(pca.channels[8], min_pulse=440, max_pulse=2400)
servo9 = servo.Servo(pca.channels[9], min_pulse=440, max_pulse=2400)
servo10 = servo.Servo(pca.channels[10], min_pulse=440, max_pulse=2400)
servo11 = servo.Servo(pca.channels[11], min_pulse=440, max_pulse=2400)

servo12 = servo.Servo(pca.channels[12], min_pulse=440, max_pulse=2400)
servo13 = servo.Servo(pca.channels[13], min_pulse=440, max_pulse=2400)
servo14 = servo.Servo(pca.channels[14], min_pulse=440, max_pulse=2400)
servo15 = servo.Servo(pca.channels[15], min_pulse=440, max_pulse=2400)
# We sleep in the loops to give the servo time to move into position.

def Rot_Angle(a, b):
    a.angle = b
    time.sleep(0.03)
    
def Controll_1(a,B):
    for i in range(0,B):
        a.angle = i
        time.sleep(0.05)
    for i in range(0,B):
        a.angle = B - i
        time.sleep(0.05)
def Controll_2(a, b , c):
    for i in range(0,180):
        a.angle = i
        b.angle = i
        c.angle = i
        time.sleep(0.05)
    for i in range(0,180): 
        a.angle = 180 - i
        b.angle = 180 - i
        c.angle = 180 - i
        time.sleep(0.05)
def Controll_Forward(a,b,c):
    print('batdau di toi')
    for i in range(b,c):
        a.angle = i
        time.sleep(0.03)
    print('ketthuc ')
def Controll_Backward(servo0,b,c):
    for i in range(0,b):
        servo0.angle = b - i
        t = b-i
        time.sleep(0.05)
        if(t == c):
            break
def Controll_Standup():
    t = 0
    spam_time = 0.05
    for i in range(0,60,5):
        # khau 2
        servo1.angle = 180 - i # tuc la chay toi 120 do
        servo5.angle = i
        time.sleep(spam_time)
        servo9.angle = 180 - i
        servo13.angle = i
        time.sleep(spam_time)
        # khau 3
        servo2.angle = 2*i
        servo6.angle = 180 - 2*i
        time.sleep(spam_time)
        servo10.angle = 2*i
        servo14.angle = 180 - 2*i
        time.sleep(spam_time)
def Default_legs_1():
    Rot_Angle(servo0,90)
    time.sleep(0.05)
    Rot_Angle(servo4,90)
    time.sleep(0.05)
    Rot_Angle(servo8,90)
    time.sleep(0.05)
    Rot_Angle(servo12,90)
    time.sleep(0.05)
def Default_legs_2():
    Rot_Angle(servo1,180)
    time.sleep(0.05)
    Rot_Angle(servo5,0)
    time.sleep(0.05)
    Rot_Angle(servo9,180)
    time.sleep(0.05)
    Rot_Angle(servo13,0)
    time.sleep(0.05)
def Default_legs_3():
    Rot_Angle(servo2,0)
    time.sleep(0.05)
    Rot_Angle(servo6,180)
    time.sleep(0.05)
    Rot_Angle(servo10,0)
    time.sleep(0.05)
    Rot_Angle(servo14,180)
    time.sleep(0.05)
def Stand():
    # dua cac chan 1 ve khong do  
    # dua cac chan ve goc chuan
    Default_legs_1()
    Default_legs_2()
    Default_legs_3() 
    # dua cac chan ve trang thai
    Controll_Standup()
def main():
    print('batdau')
    i = 1
    while (i):
        Stand()
        #Rot_Angle(servo10,180)
        #Controll_Forward(servo10,0,180)
        #Controll_Backward(servo9,180,0)
        #Rot_Angle(servo13,180-20) 
        #Controll_Forward(servo0,0,180)
        
        i = 0
if __name__ == '__main__':
    main()
# You can also specify the movement fractionally.
'''
fraction = 0.5
while fraction <= 1:
    servo0.fraction = fraction
    fraction += 0.01
    time.sleep(0.03)'''

print("complete")
pca.deinit()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        