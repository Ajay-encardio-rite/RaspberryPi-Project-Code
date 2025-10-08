import RPi.GPIO as GPIO
import time

motionPin = 18   
ledPin = 26      

GPIO.setmode(GPIO.BCM)
GPIO.setup(motionPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

time.sleep(5)  

try:
    while True:
        motion = GPIO.input(motionPin)
        if motion:  
            print("Motion detected!")
            GPIO.output(ledPin, GPIO.HIGH) 
            time.sleep(0.5)
            GPIO.output(ledPin, GPIO.LOW)  
            time.sleep(0.5)
        else:
            GPIO.output(ledPin, GPIO.LOW)  
            print("No motion")
            time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program stopped")
