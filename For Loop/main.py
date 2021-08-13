from machine import Pin
import time

led = [32,33,25,26,27,14,12,13]


while True:
    for i in led:
        i = Pin(i, Pin.OUT)
        i.on()
        time.sleep(0.5)
        i.off()
        if (i == 13):
            break

    for i in led[::-1]:
        i = Pin(i, Pin.OUT)
        i.on()
        time.sleep(0.5)
        i.off()
        if (i == 32):
            break
