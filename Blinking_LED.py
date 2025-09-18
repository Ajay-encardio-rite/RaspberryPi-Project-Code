import RPi.GPIO as GPIO
import time

# Use physical board pin numbering
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as output
GPIO.setup(11, GPIO.OUT)

try:
    while True:
        GPIO.output(11, True)   # LED ON
        time.sleep(1)           # wait 1 second
        GPIO.output(11, False)  # LED OFF
        time.sleep(1)           # wait 1 second
except KeyboardInterrupt:
    # Stop with Ctrl+C
    print("Exiting program...")
finally:
    GPIO.cleanup()  # Reset GPIO settings
