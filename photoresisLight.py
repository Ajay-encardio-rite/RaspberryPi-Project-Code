from gpiozero import Device
import ADC0834_IC
import time

# --- ADC0834 Setup ---
ADC0834_IC.setup()

try:
    while True:
        analogVal = ADC0834_IC.get_result()
        print("Light value is:", analogVal)
        time.sleep(0.1)

except KeyboardInterrupt:
    time.sleep(0.2)
    print("GPIO good to go")
