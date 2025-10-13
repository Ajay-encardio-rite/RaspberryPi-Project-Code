from gpiozero import Buzzer
import time

buzzPin = 17
buzzer = Buzzer(buzzPin)

try:
    while True:
        buzzer.on()
        time.sleep(0.1)
        buzzer.off()
        time.sleep(0.1)
except KeyboardInterrupt:
    buzzer.off()

