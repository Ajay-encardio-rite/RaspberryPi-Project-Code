import RPi.GPIO as GPIO
import ADC0834
from time import sleep
dt=.2
GPIO.setmode(GPIO.BCM)

LEDred=16
LEDgreen=20
LEDblue=21
GPIO.setup(LEDred,GPIO.OUT)
GPIO.setup(LEDgreen,GPIO.OUT)
GPIO.setup(LEDblue,GPIO.OUT)

myPWMred=GPIO.PWM(LEDred,1000)
myPWMgreen=GPIO.PWM(LEDgreen,1000)
myPWMblue=GPIO.PWM(LEDblue,1000)
myPWMred.start(0)
myPWMgreen.start(0)
myPWMblue.start(0)
ADC0834.setup()
try:
    while True:
        analogred=ADC0834.getResult(0)
        analoggreen=ADC0834.getResult(1)
        analogblue=ADC0834.getResult(2)
        print('Rawred= ',analogred, 'Rawgreen= ',analoggreen, 'Rawgblue= ',analogblue)
        DCred=analogred*100/255
        DCgreen=analoggreen*100/255
        DCblue=analogblue*100/255
        if DCred<=3:
            DCred=0
        if DCgreen<=3:
            DCgreen=0
        if DCblue<=3:
            DCblue=0
        myPWMred.ChangeDutyCycle(DCred)
        myPWMgreen.ChangeDutyCycle(DCgreen)
        myPWMblue.ChangeDutyCycle(DCblue)
        sleep(dt)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go')