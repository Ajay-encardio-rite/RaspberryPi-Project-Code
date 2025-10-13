from gpiozero import PWMOutputDevice
import time

buzzPin = 17
buzz = PWMOutputDevice(buzzPin)
buzz.value = 0.5

try:
    while True:
        for freq in range(150, 2001):
            buzz.frequency = freq
            time.sleep(0.001)
        
        for freq in range(2000, 149):
            buzz.frequency = freq
            time.sleep(0.001)
except KeyboardInterrupt:
    buzz.off()
