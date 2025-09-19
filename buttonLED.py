from time import sleep
import RPi.GPIO as GPIO

delay=1
inPin=40
outPin=38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin,GPIO.IN)
GPIO.setup(outPin,GPIO.OUT)
try:
    while True:
         readVal=GPIO.input(inPin)
         if readVal==1:
                GPIO.output(outPin,1)
         if readVal==0:
            GPIO.output(outPin,0)
except KeyboardInterrupt:
         GPIO.cleanup()
         print('Successfully working')
