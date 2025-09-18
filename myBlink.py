import RPi.GPIO as GPIO
import time
cont='Y'
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
while cont=='Y':
       numBlink=int(input("How Many Blink Do you you Wish For: "))
       for i in range(0,numBlink):
             GPIO.output(11,True)
             time.sleep(1)
             GPIO.output(11,False)
             time.sleep(1)
       cont=input('Do You Want to Continue: (Y for Yes and N for No): ')      
GPIO.cleanup()
     
