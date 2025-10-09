import LCD1602
import adafruit_dht
import board
import time
from gpiozero import Button

dhtDevice = adafruit_dht.DHT11(board.D17)
LCD1602.init(0x27, 1)

button = Button(21, pull_up=True)
buttonState = 1
buttonStateOld = 1
tempMode = True

try:
    while True:
        if button.is_pressed:
            buttonState = 0
        else:
            buttonState = 1

        if buttonState == 1 and buttonStateOld == 0:
            tempMode = not tempMode
        print(tempMode)
        buttonStateOld = buttonState

        tempC = dhtDevice.temperature
        tempF = tempC * 1.8 + 32
        humid = dhtDevice.humidity

        if tempC is not None and humid is not None:
            if tempMode == True:
                LCD1602.write(0, 0, 'Temp: ')
                LCD1602.write(6, 0, str(round(tempF, 1)))
                LCD1602.write(11, 0, 'F')
                LCD1602.write(0, 1, 'Humidity: ')
                LCD1602.write(10, 1, str(round(humid, 1)))
                LCD1602.write(14, 1, '%')
            if tempMode == False:
                LCD1602.write(0, 0, 'Temp: ')
                LCD1602.write(6, 0, str(round(tempC, 1)))
                LCD1602.write(11, 0, 'C')
                LCD1602.write(0, 1, 'Humidity: ')
                LCD1602.write(10, 1, str(round(humid, 1)))
                LCD1602.write(14, 1, '%')
        time.sleep(.5)

except KeyboardInterrupt:
    time.sleep(0.2)
    LCD1602.clear()
