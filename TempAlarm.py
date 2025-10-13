from gpiozero import Button, Buzzer
import ADC0834_IC
import LCD1602
import time
import board
import adafruit_dht

# --- Pin Setup ---
buzzPin = 22
tempPin = 26
buttonPin = 24

# --- Device Initialization ---
dhtDevice = adafruit_dht.DHT11(board.D26)
buzzer = Buzzer(buzzPin)
button = Button(buttonPin, pull_up=True)
ADC0834_IC.setup()
LCD1602.init(0x27, 1)

# --- Initial States ---
buttonState = 1
buttonStateOld = 1
setMode = True
buzzVal = 85

try:
    while True:
        # --- Button Handling ---
        buttonState = button.is_pressed
        if buttonState == False and buttonStateOld == True:
            setMode = not setMode
        print("setmode is :", setMode)
        buttonStateOld = buttonState
        time.sleep(0.2)

        # --- Mode 1: Set Trip Temperature ---
        if setMode == True:
            analogVal = ADC0834_IC.get_result()
            buzzVal = int((analogVal * 100) / 255)
            LCD1602.write(0, 0, 'Set Trip Temp:')
            LCD1602.write(0, 1, str(buzzVal))
            time.sleep(0.25)
            LCD1602.clear()
            buzzer.off()

        # --- Mode 2: Monitor Temperature & Humidity ---
        if setMode == False:
            try:
                tempC = dhtDevice.temperature
                humid = dhtDevice.humidity
            except RuntimeError:
                # DHT sensors sometimes fail to read — just skip this cycle
                print("DHT read error, retrying...")
                time.sleep(0.2)
                continue

            if tempC is not None and humid is not None:
                tempF = tempC * 1.8 + 32
                tempF = round(tempF, 1)
                print("buzzVal:", buzzVal)

                if tempF < buzzVal:
                    buzzer.off()
                    LCD1602.write(0, 0, 'Temp: ')
                    LCD1602.write(6, 0, str(tempF))
                    LCD1602.write(11, 0, 'F')
                    LCD1602.write(0, 1, 'Humidity: ')
                    LCD1602.write(10, 1, str(round(humid, 1)))
                    LCD1602.write(14, 1, '%')
                else:
                    buzzer.on()
                    LCD1602.write(0, 0, 'Temp: ')
                    LCD1602.write(6, 0, str(tempF))
                    LCD1602.write(11, 0, 'F')
                    LCD1602.write(0, 1, 'ALERT: High Temp!')

            time.sleep(0.2)

except KeyboardInterrupt:
    buzzer.off()
    LCD1602.clear()
    print("System Good to Go")
