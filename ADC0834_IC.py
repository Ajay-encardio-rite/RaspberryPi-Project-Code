#!/usr/bin/env python3
# ADC0834 module for gpiozero with bidirectional DIO pin

from gpiozero import DigitalOutputDevice, DigitalInputDevice
import time

# --- Default GPIO pins ---
ADC_CS  = 17
ADC_CLK = 18
ADC_DIO = 27

# --- Device objects ---
cs = None
clk = None
dio = None  # Will be DigitalOutputDevice or DigitalInputDevice

def setup(cs_pin=17, clk_pin=18, dio_pin=27):
    """
    Initialize ADC0834 pins
    """
    global ADC_CS, ADC_CLK, ADC_DIO, cs, clk, dio
    ADC_CS = cs_pin
    ADC_CLK = clk_pin
    ADC_DIO = dio_pin

    cs = DigitalOutputDevice(ADC_CS)
    clk = DigitalOutputDevice(ADC_CLK)
    dio = DigitalOutputDevice(ADC_DIO)  # Start as output

def destroy():
    """
    Cleanup all GPIOs
    """
    cs.close()
    clk.close()
    dio.close()

# --- Helper functions to switch DIO direction ---
def dio_to_input():
    global dio
    dio.close()
    dio = DigitalInputDevice(ADC_DIO)

def dio_to_output():
    global dio
    dio.close()
    dio = DigitalOutputDevice(ADC_DIO)

# --- Get ADC value from channel 0-3 ---
def get_result(channel=0):
    sel = int((channel > 1) & 1)
    odd = channel & 1

    # Start communication
    dio_to_output()
    cs.off()
    clk.off()
    dio.on()
    time.sleep(0.000002)
    clk.on()
    time.sleep(0.000002)

    # Single-ended mode
    clk.off()
    dio.on()
    time.sleep(0.000002)
    clk.on()
    time.sleep(0.000002)

    # ODD bit
    clk.off()
    if odd:
        dio.on()
    else:
        dio.off()
    time.sleep(0.000002)
    clk.on()
    time.sleep(0.000002)

    # Select bit
    clk.off()
    if sel:
        dio.on()
    else:
        dio.off()
    time.sleep(0.000002)
    clk.on()
    time.sleep(0.000002)
    clk.off()
    time.sleep(0.000002)

    # --- Read data ---
    dat1 = 0
    dio_to_input()  # Switch DIO to input
    for i in range(8):
        clk.on(); time.sleep(0.000002)
        clk.off(); time.sleep(0.000002)
        dat1 = (dat1 << 1) | dio.value

    dat2 = 0
    for i in range(8):
        dat2 |= (dio.value << i)
        clk.on(); time.sleep(0.000002)
        clk.off(); time.sleep(0.000002)

    cs.on()
    dio_to_output()  # Switch back to output

    if dat1 == dat2:
        return dat1
    else:
        return 0

# --- Convenience function for channel 1 ---
def get_result1():
    return get_result(1)

# --- Optional loop for testing ---
def loop():
    while True:
        for i in range(4):
            res = get_result(i)
            print(f"res{i} = {res}")
            time.sleep(0.1)
        time.sleep(1)

# --- Run test loop if module executed directly ---
if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        print("GPIO cleanup done.")
