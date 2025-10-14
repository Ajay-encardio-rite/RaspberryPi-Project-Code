from gpiozero import Button, Buzzer
import ADC0834_IC
import time

# --- Pin Setup ---
motionPin = 23
buzzPin = 26

# --- Device Initialization ---
motion = Button(motionPin, pull_up=False)
buzzer = Buzzer(buzzPin)

# Initialize ADC0834
ADC0834_IC.setup()
time.sleep(0.2)

try:
    while True:
        # Read motion and light values
        motion_state = not motion.is_pressed  # True when motion detected
        analogVal = ADC0834_IC.get_result()
        print("Light value is:", analogVal, "Motion:", int(motion_state))

        # Decision logic
        if motion_state and analogVal <= 140:
            buzzer.off()
            print("All clear!")
        else:
            buzzer.on()
            print("Alert!: Deploy Countermeasure")
            

        time.sleep(0.2)

except KeyboardInterrupt:
    time.sleep(0.2)
    buzzer.off()
    print("GPIO good to go")
