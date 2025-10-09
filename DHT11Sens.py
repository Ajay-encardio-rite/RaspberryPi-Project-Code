import time
import board
import adafruit_dht

# Use GPIO17 (BCM numbering)
dhtDevice = adafruit_dht.DHT11(board.D17)

try:
    while True:     
            temperature = dhtDevice.temperature
            humidity = dhtDevice.humidity
            if temperature is not None and humidity is not None:
                print(f"Temp: {temperature:.1f}°C | Humidity: {humidity:.1f}%")
            time.sleep(.2)    
except KeyboardInterrupt:
    print("\nProgram stopped by user.")
