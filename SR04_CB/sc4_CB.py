#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER_1 = 6
GPIO_ECHO_1 = 12

GPIO_TRIGGER_2 = 13
GPIO_ECHO_2 = 16
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER_1, GPIO.OUT)
GPIO.setup(GPIO_ECHO_1, GPIO.IN)
GPIO.setup(GPIO_TRIGGER_2, GPIO.OUT)
GPIO.setup(GPIO_ECHO_2, GPIO.IN)
 
def distance(PIN_TRIG, PIN_ECHO):
    # set Trigger to HIGH
    GPIO.output(PIN_TRIG, True) 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(PIN_TRIG, False) 
    StartTime = time.time()
    StopTime = time.time() 
    # save StartTime
    while GPIO.input(PIN_ECHO) == 0:
        StartTime = time.time() 
    # save time of arrival
    while GPIO.input(PIN_ECHO) == 1:
        StopTime = time.time() 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    if 0 < distance  < 10:
        return True
    else:
        return False
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance(GPIO_TRIGGER_1,GPIO_ECHO_1)
            if dist == True :
                print ('Co vat can 1')
            time.sleep(1)
            dist2 = distance(GPIO_TRIGGER_2,GPIO_ECHO_2)
            if dist2 == True :
                print ('Co vat can 2')

 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
