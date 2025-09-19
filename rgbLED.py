import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
rPin=37
gPin=35
bPin=33
GPIO.setup(rPin,GPIO.OUT)
GPIO.setup(gPin,GPIO.OUT)
GPIO.setup(bPin,GPIO.OUT)
try:
   while True:

        GPIO.output(rPin,1)
        print("Red is on")
        time.sleep(.1)
        GPIO.output(rPin,0)
        print("Red is off")
        time.sleep(.1)
        GPIO.output(gPin,1)
        print("Green is on")
        time.sleep(.1)
        GPIO.output(gPin,0)
        print("Green is off")
        time.sleep(.1)
        GPIO.output(bPin,1)
        print("Blue is on")
        time.sleep(.1)
        GPIO.output(bPin,0)
        print("Blue is off")
        time.sleep(.1)
except KeyboardInterrupt:
      print("....program complete")
finally: 
       GPIO.cleanup()
