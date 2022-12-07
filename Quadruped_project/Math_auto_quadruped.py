from array import array
from math import degrees, pi, sin, cos, sin, asin, acos, atan, atan2, sqrt, radians
import numpy as np
import time
import PCA_servo_control
number_round = 0
delta_y = 0
delta_z = -2
spam_time = 0.08
def IK(x: float, y: float , z: float, L1: float, L2: float, L3: float, H: float):
    theta = []
    try:
        if x > 0:
            f11 = ( -atan(y/x) - atan(sqrt(x**2 + y**2  - L1**2)/L1))
        else:
            f11 = ( atan(y/x) - atan(sqrt(x**2 + y**2  - L1**2)/L1))
        theta_11 = round(degrees(f11), number_round) #lam tron 2 chu so
        
        try:
            f13 = acos((x**2 + y**2 + z**2 - L1**2 - L2**2 - L3**2)/(2*L2*L3))       
        except:
            f13 = 0
        theta_13 = round(degrees(f13),number_round)

        f12 = atan(z/(sqrt(x**2 + y**2 + z**2 - L1**2))) - atan((L3*sin(radians(theta_13)))/(L2 + L3*cos(radians(theta_13))))
        theta_12 = round(degrees(f12),number_round)
        theta = [theta_11, theta_12, theta_13]
        print('Chan truoc: goc1 =',90 - theta_11,'Chan truoc: goc1 =',90 - theta_12,'Chan truoc: goc1 =',180 - theta_13)
        return theta

    except:
        print("Viet ham dua cac chan de robot 4 chan dung im")

    
    return(theta)
def Standup(L1, L2, L3, H):
    for i in np.arange(2,H + 0.2, 0.2):
        RF_Servo(-L1,-i,0, L1, L2, L3, H)

def Type_Trot(direction, TM, s, h, sampling_time, L1, L2, L3, H):
    if direction == 1 or direction == 5:
        G0_Forward_Trot(s, h, L1, L2, L3, H)
    elif direction == 3:
        Go_Backward_Trot(s, h, L1, L2, L3, H)
    elif direction == 2 or direction == 5:
        Go_Rightward_Trot(s, h, L1, L2, L3, H)
    elif direction == 4 or direction == 0:
        Go_Lefttward_Trot(s, h, L1, L2, L3, H)
    else:
        print("Dung im")
def G0_Forward_Trot(s, h, L1, L2, L3, H):
    #dua cac chan ve vi tri ban dau
    RF_Servo(-L1,-H + delta_y,- delta_z,L1, L2, L3, H)
    time.sleep(spam_time)    
    LH_Servo(+L1,-H + delta_y,- delta_z,L1, L2, L3, H)
    time.sleep(spam_time)
    RF_Servo(-L1,-H + delta_y,- delta_z,L1, L2, L3, H)
    time.sleep(spam_time)
    LH_Servo(-L1,-H + delta_y,- delta_z,L1, L2, L3, H)
    time.sleep(spam_time)
    #chuyen toa do
    theta = IK(-L1,-H+h + delta_y,(s/2)- delta_z,L1, L2, L3, H) #Cap chan di dau tien di len
    PCA_servo_control.Rot_Arm_RF_2(theta[1], theta[2])
    time.sleep(spam_time)
    PCA_servo_control.Rot_Arm_LH_2(theta[1], theta[2])
    time.sleep(spam_time)
    
    theta = IK(-L1,-H + delta_y, -s - delta_z, L1, L2, L3, H) # Cap chan di sau day phia sau
    PCA_servo_control.Rot_Arm_LF_2(theta[1], theta[2])
    time.sleep(spam_time)
    PCA_servo_control.Rot_Arm_RH_2(theta[1], theta[2])
    time.sleep(spam_time)
    
    theta = IK(-L1,-H + delta_y,s - delta_z,L1, L2, L3, H) #Cap chan di dau tien di xuong
    PCA_servo_control.Rot_Arm_RF_2(theta[1], theta[2])
    time.sleep(spam_time)
    PCA_servo_control.Rot_Arm_LH_2(theta[1], theta[2])
    time.sleep(spam_time)
    
    time.sleep(0.1)
    
    theta = IK(-L1,-H+h + delta_y,-s/2 - delta_z, L1, L2, L3, H) # Cap chan di sau di len
    PCA_servo_control.Rot_Arm_LF_2(theta[1], theta[2])
    time.sleep(spam_time)
    PCA_servo_control.Rot_Arm_RH_2(theta[1], theta[2])
    time.sleep(spam_time)
    
    theta = IK(-L1,-H + delta_y,- delta_z,L1, L2, L3, H) #Cap chan di dau tien day ra sau
    PCA_servo_control.Rot_Arm_RF_2(theta[1], theta[2])
    time.sleep(spam_time)
    PCA_servo_control.Rot_Arm_LH_2(theta[1], theta[2])
    time.sleep(spam_time)
    
    theta = IK(-L1,-H + delta_y,- delta_z, L1, L2, L3, H) # Cap chan di sau di len
    PCA_servo_control.Rot_Arm_LF_2(theta[1], theta[2])
    time.sleep(spam_time)
    PCA_servo_control.Rot_Arm_RH_2(theta[1], theta[2])
    time.sleep(spam_time)

def Type_Crawl(direction, TM, s, h, L1, L2, L3, H):
    if direction == 1 or direction == 5:
        G0_Forward_Crawl(s, h, L1, L2, L3, H)
    elif direction == 3:
        Go_Backward_Crawl(s, h, L1, L2, L3, H)
    elif direction == 2 or direction == 5:
        Go_Rightward_Crawl(s, h, L1, L2, L3, H)
    elif direction == 4 or direction == 0:
        Go_Lefttward_Crawl(s, h, L1, L2, L3, H)
    else:
        print("Dung im")
def RF_Servo(x1,y1,z1, L1, L2, L3, H): # quay toi goc dua vao toa do nhap vao
    theta = IK(x1, y1, z1, L1, L2, L3, H)
    PCA_servo_control.Rot_Arm_RF(theta[0], theta[1], theta[2])
    time.sleep(spam_time)
    
def LH_Servo(x1,y1,z1, L1, L2, L3, H):
    theta = IK(x1, y1, z1, L1, L2, L3, H)
    PCA_servo_control.Rot_Arm_LH(theta[0], theta[1], theta[2])
    time.sleep(spam_time)
    
def RH_Servo(x1,y1,z1, L1, L2, L3, H):
    beta = IK(x1, y1, z1, L1, L2, L3, H)
    PCA_servo_control.Rot_Arm_RH(beta[0], beta[1], beta[2])
    time.sleep(spam_time)
    
def LF_Servo(x1,y1,z1, L1, L2, L3, H):
    beta = IK(x1,y1,z1, L1, L2, L3, H)
    PCA_servo_control.Rot_Arm_LF(beta[0], beta[1], beta[2])
    time.sleep(spam_time)
def G0_Forward_Crawl(s, h, L1, L2, L3, H):
    #chan 1 vs chan 4 di cung luc 
    RF_Servo(-L1,-H + delta_y,- delta_z,L1, L2, L3, H)    
    LH_Servo(+L1,-H + delta_y,- delta_z,L1, L2, L3, H)

    RF_Servo(-L1,-H+h + delta_y,(s/2)- delta_z,L1, L2, L3, H)
    LH_Servo(+L1,-H+h + delta_y,(s/2)- delta_z,L1, L2, L3, H)
    
    RF_Servo(-L1,-H + delta_y,s - delta_z,L1, L2, L3, H)
    LH_Servo(-L1,-H + delta_y,s - delta_z,L1, L2, L3, H)
    
    #chan 2 va chan 3 di cung luc   
    LF_Servo(L1,-H + delta_y,-delta_z,L1, L2, L3, H)
    RH_Servo(-L1,-H + delta_y,- delta_z,L1, L2, L3, H)
    
    LF_Servo(L1,-H+h + delta_y,(s/2) - delta_z,L1, L2, L3, H)
    RH_Servo(-L1,-H+h + delta_y,(s/2)- delta_z,L1, L2, L3, H)
    
    LF_Servo(L1,-H + delta_y,s - delta_z,L1, L2, L3, H)
    RH_Servo(-L1,-H + delta_y,s - delta_z,L1, L2, L3, H)
    global spam_time
    spam_time = 0
    for i in np.arange(0,s + 0.5, 0.5):
        RF_Servo(-L1, -H + delta_y, s - delta_z -i, L1, L2, L3, H)
        LH_Servo(-L1, -H + delta_y, s - delta_z -i, L1, L2, L3, H)
        LF_Servo(-L1, -H + delta_y, s - delta_z -i, L1, L2, L3, H)
        RH_Servo(-L1, -H + delta_y, s - delta_z -i, L1, L2, L3, H)
    time.sleep(0.08)
def Go_Backward_Crawl(s, h, L1, L2, L3, H):
    RF_Servo(-L1,-H + delta_y,- delta_z,L1, L2, L3, H)   
    LH_Servo(+L1,-H + delta_y,- delta_z,L1, L2, L3, H)
    
    RF_Servo(-L1,-H+h + delta_y, -(s/2),L1, L2, L3, H)
    LH_Servo(+L1,-H+h + delta_y, -(s/2),L1, L2, L3, H)
    
    
    RF_Servo(-L1,-H + delta_y, -s - delta_z,L1, L2, L3, H)
    LH_Servo(-L1,-H + delta_y, -s - delta_z,L1, L2, L3, H)
    time.sleep(0.1)
     
    #chan 2 va chan 3 di cung luc 
    LF_Servo(L1,-H + delta_y,-delta_z,L1, L2, L3, H)
    RH_Servo(-L1,-H + delta_y,- delta_z,L1, L2, L3, H)
    
    LF_Servo(L1,-H+h + delta_y, -(s/2) ,L1, L2, L3, H)
    RH_Servo(-L1,-H+h + delta_y, -(s/2),L1, L2, L3, H)
    
    LF_Servo(L1,-H + delta_y, -s - delta_z,L1, L2, L3, H)
    RH_Servo(-L1,-H + delta_y, -s - delta_z,L1, L2, L3, H)
    global spam_time
    spam_time = 0
    for i in np.arange(0,s + 0.5, 0.5):
        RF_Servo(-L1, -H + delta_y, -s - delta_z +i, L1, L2, L3, H)
        LH_Servo(-L1, -H + delta_y, -s - delta_z +i, L1, L2, L3, H)
        LF_Servo(-L1, -H + delta_y, -s - delta_z +i, L1, L2, L3, H)
        RH_Servo(-L1, -H + delta_y, -s - delta_z +i, L1, L2, L3, H)
    time.sleep(0.08)
def Go_Rightward_Crawl(s, h, L1, L2, L3, H):
    #chan 1 vs chan 4 di cung luc 
    spam_time = 0.15
    RF_Servo(-L1, -H + delta_y, -delta_z, L1, L2, L3, H)
    LH_Servo(L1, -H + delta_y, -delta_z, L1, L2, L3, H)
    
    RF_Servo(-L1-s/2, -H+h + delta_y,- delta_z,L1, L2, L3, H)
    LH_Servo(L1-s/2,-H+h + delta_y, -delta_z,L1, L2, L3, H)
    
    
    RF_Servo(-L1-s,-H + delta_y,- delta_z,L1, L2, L3, H)
    LH_Servo(L1-s,-H + delta_y,- delta_z,L1, L2, L3, H)
    time.sleep(0.1)
     
    #chan 2 va chan 3 di cung luc 
    LF_Servo(L1,-H + delta_y,-delta_z,L1, L2, L3, H)
    RH_Servo(-L1,-H + delta_y,-delta_z,L1, L2, L3, H)
    
    LF_Servo(L1 -s/2,-H+h + delta_y,-delta_z,L1, L2, L3, H)
    RH_Servo(-L1 -s/2,-H+h + delta_y,-delta_z,L1, L2, L3, H)
    
    LF_Servo(L1-s,-H + delta_y,- delta_z,L1, L2, L3, H)
    RH_Servo(-L1-s,-H + delta_y,- delta_z,L1, L2, L3, H)
    global spam_time
    spam_time = 0
    for i in np.arange(0,s + 0.5, 0.5):
        RF_Servo(-L1 -s +i, -H + delta_y, - delta_z, L1, L2, L3, H)
        LH_Servo(L1 -s +i, -H + delta_y, - delta_z, L1, L2, L3, H)
        LF_Servo(L1 -s +i, -H + delta_y, - delta_z, L1, L2, L3, H)
        RH_Servo(-L1 -s +i, -H + delta_y, - delta_z, L1, L2, L3, H)
    time.sleep(0.08)
def Go_Lefttward_Crawl(s, h, L1, L2, L3, H):
    #chan 1 vs chan 4 di cung luc 
    spam_time = 0.15
    RF_Servo(-L1, -H + delta_y, -delta_z, L1, L2, L3, H)
    LH_Servo(L1, -H + delta_y, -delta_z, L1, L2, L3, H)
    
    RF_Servo(-L1+s/2, -H+h + delta_y,- delta_z,L1, L2, L3, H)
    LH_Servo(L1+s/2,-H+h + delta_y, -delta_z,L1, L2, L3, H)
    
    
    RF_Servo(-L1+s,-H + delta_y,- delta_z,L1, L2, L3, H)
    LH_Servo(L1+s,-H + delta_y,- delta_z,L1, L2, L3, H)
    time.sleep(0.1)
     
    #chan 2 va chan 3 di cung luc 
    LF_Servo(L1,-H + delta_y,-delta_z,L1, L2, L3, H)
    RH_Servo(-L1,-H + delta_y,-delta_z,L1, L2, L3, H)
    
    LF_Servo(L1 +s/2,-H+h + delta_y,-delta_z,L1, L2, L3, H)
    RH_Servo(-L1 +s/2,-H+h + delta_y,-delta_z,L1, L2, L3, H)
    
    LF_Servo(L1+s,-H + delta_y,- delta_z,L1, L2, L3, H)
    RH_Servo(-L1+s,-H + delta_y,-delta_z,L1, L2, L3, H)
    global spam_time
    spam_time = 0
    for i in np.arange(0,s + 0.5, 0.5):
        RF_Servo(-L1+s -i, -H + delta_y,- delta_z, L1, L2, L3, H)
        LH_Servo(L1+s -i, -H + delta_y,- delta_z, L1, L2, L3, H)
        LF_Servo(L1+s -i, -H + delta_y, - delta_z, L1, L2, L3, H)
        RH_Servo(-L1+s -i, -H + delta_y,- delta_z, L1, L2, L3, H)
    time.sleep(0.08)
