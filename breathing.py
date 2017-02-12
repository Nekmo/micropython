"""Asciende y desciende la luz de forma progresiva, como
si fuese una respiración
"""
import time
import machine

pin = machine.PWM(machine.Pin(14))
pin.freq(1000)


def breathing(pin, wait=.005):
    i = 0
    while True:
        r = range(1024)
        r = reversed(r) if i % 2 else r
        for x in r:
            pin.duty(x)
            time.sleep(wait)
        i += 1

breathing(pin)
