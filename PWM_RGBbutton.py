import RPi.GPIO as GPIO
from time import sleep
dt=.1

rPin=37
gPin=35
bPin=33

rBut=11
gBut=13
bBut=15

rButState=1
rButStateOld=1

gButState=1
gButStateOld=1

bButState=1
bButStateOld=1

GPIO.setmode(GPIO.BOARD)

GPIO.setup(rPin,GPIO.OUT)
GPIO.setup(gPin,GPIO.OUT)
GPIO.setup(bPin,GPIO.OUT)
GPIO.setup(rBut, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(gBut, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(bBut, GPIO.IN,pull_up_down=GPIO.PUD_UP)

myPWMr=GPIO.PWM(rPin,100)
myPWMg=GPIO.PWM(gPin,100)
myPWMb=GPIO.PWM(bPin,100)

Dcr=.99
Dcg=.99
Dcb=.99

myPWMr.start(int(Dcr))
myPWMg.start(int(Dcg))
myPWMb.start(int(Dcb))


try:
    while True:
        rButState=GPIO.input(rBut)
        gButState=GPIO.input(gBut)
        bButState=GPIO.input(bBut)
        print('button',rButState,gButState,bButState)
        if rButState==1 and rButStateOld==0:
            Dcr=Dcr*1.58
            print("Red button is register")
            if Dcr>99:
                 Dcr=.99
            myPWMr.ChangeDutyCycle(int(Dcr))     
            
        if gButState==1 and gButStateOld==0:
            Dcg=Dcg*1.58
            print("Green button is register")
            if Dcg>99:
                 Dcg=.99
            myPWMg.ChangeDutyCycle(int(Dcg))

        if bButState==1 and bButStateOld==0:
            Dcb=Dcb*1.58
            print("Blue button is register")
            if Dcb>99:
                 Dcb=.99
            myPWMb.ChangeDutyCycle(int(Dcb))

        rButStateOld=rButState
        gButStateOld=gButState
        bButStateOld=bButState
        sleep(dt)
except KeyboardInterrupt:
       GPIO.cleanup()
       print("All good to go")
