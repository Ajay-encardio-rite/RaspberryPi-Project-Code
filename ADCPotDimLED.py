import RPi.GPIO as GPIO
import ADC0834
from time import sleep
dt=.1
redPin=23
DC=0
GPIO.setmode(GPIO.BCM)
ADC0834.setup()
GPIO.setup(redPin,GPIO.OUT)
myPWM=GPIO.PWM(redPin,1000)
myPWM.start(DC)
try:
    while True:
        PotVal=ADC0834.getResult(0)
        DC=(100/255)*PotVal
        if DC>99:
            DC=99
        myPWM.ChangeDutyCycle(DC)    
        print(PotVal)
        sleep(dt)
    
except KeyboardInterrupt:
    myPWM.stop()  
    GPIO.cleanup()
    print('GPIO Good to Go')