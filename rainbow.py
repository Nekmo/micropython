"""Alterna entre los 7 colores del arcoiris continuamente
en un intervalo de 1 segundo. Es necesario además, tras haber
cargado el módulo, ejecutar start().
"""
import machine
import time

red = machine.PWM(machine.Pin(12))
green = machine.PWM(machine.Pin(14))
blue = machine.PWM(machine.Pin(4))
red.freq(1000)
green.freq(1000)
blue.freq(1000)

RAINBOW = [
    (148, 0, 211),  # Violet
    (75, 0, 130),  # Indigo
    (0, 0, 255),  # Blue
    (0, 255, 0),  # Green
    (255, 255, 0),  # Yellow
    (255, 127, 0),  # Orange
    (255, 0 , 0),  # Red
]


def set_color(r, g, b):
    red.duty(r * 4); green.duty(g * 4); blue.duty(b * 4)
 

def start():
    """Start rainbow
    """
    i = 0
    while True:
        color = RAINBOW[i % len(RAINBOW)]
        set_color(*color)
        time.sleep(1)
        i += 1
