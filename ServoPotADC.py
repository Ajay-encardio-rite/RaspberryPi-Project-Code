import RPi.GPIO as GPIO
import ADC0834
from time import sleep
dt=.1
pwmPin=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwmPin,GPIO.OUT)
pwm=GPIO.PWM(pwmPin,50)
pwm.start(0)
ADC0834.setup()
try:
    while True:
        PotVal=ADC0834.getResult(0)   
        pwmPercent=10/255*(PotVal)+2
        print(PotVal)
        pwm.ChangeDutyCycle(pwmPercent)
        sleep(dt)
    
except KeyboardInterrupt: 
    GPIO.cleanup()
    print('GPIO Good to Go')