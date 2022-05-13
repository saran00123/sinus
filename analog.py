from machine import Pin 
import utime

but = Pin(0, Pin.IN, Pin.PULL_DOWN)

while True:
    print("ADC:  ar0: ",but.value())
    utime.sleep(1)