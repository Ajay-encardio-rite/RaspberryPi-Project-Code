import RPi.GPIO as GPIO
from time import sleep
dt=.1
b1=40
b2=38
b1State=1
b1StateOld=1
b2State=1
b2StateOld=1
LEDPin=37
DC=99
GPIO.setmode(GPIO.BOARD)
GPIO.setup(b1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(b2,GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(LEDPin,GPIO.OUT)
myPWM=GPIO.PWM(LEDPin,100)
myPWM.start(DC)
try:
    while True:
       b1State=GPIO.input(b1)
       b2State=GPIO.input(b2)
       if b1StateOld==0 and b1State==1:
             DC=DC/2
             print('Dim Event')
       if b2StateOld==0 and b2State==1:
             DC=DC*2
             print('Bright Event')
       if DC>99:
              DC=99
       if DC<0:
              DC=0
       myPWM.ChangeDutyCycle(int(DC))
       b1StateOld=b1State
       b2StateOld=b2State
       sleep(dt)
except KeyboardInterrupt :
             myPWM.stop()
             GPIO.cleanup()
             print('GPIO GOOD TO GO')

