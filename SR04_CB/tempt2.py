#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
trigger = [6,13,19,26]
echo = [12,16,20,21]
 
#set GPIO direction (IN / OUT)
for i in range(len(echo)):
    GPIO.setup(trigger[i],GPIO.OUT)
    GPIO.setup(echo[i],GPIO.IN)

 
def Check_distance_SCR(number):
    global trigger, echo
    # set Trigger to HIGH
    GPIO.output(trigger[number-1], True)
    MaxTime = 0.04
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(trigger[number-1], False)
 
    StartTime = time.time()
    TimeOut = StartTime + MaxTime
    # save StartTime
    while GPIO.input(echo[number-1]) == 0: # tai sao ko dung if
        if(StartTime <= TimeOut):
            StartTime = time.time()
        else:
            return False
    TimeEnd = 0.04
    StopTime = time.time()
    TimeEnd = StopTime + TimeEnd
    # save time of arrival
    while GPIO.input(echo[number-1]) == 1:
        if(StopTime <= TimeEnd):
            StopTime = time.time()
        else:
            return False
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    # Viet ham check distance 
    if 0 < distance <= 10: # co vat can 
        return True
    else: 
        return False  
 
if __name__ == '__main__':
    try:
        while True:
            dist = Check_distance_SCR(1)
            print (dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
        
