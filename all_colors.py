"""Ejemplo que teóricamente usa todos los colores para iluminar un
led multicolor, pero no da suficiente tiempo a apreciar la variación,
por lo que es mejor usar rainbow.py
"""
import machine

red = machine.PWM(machine.Pin(12))
green = machine.PWM(machine.Pin(14))
blue = machine.PWM(machine.Pin(4))
red.freq(1000)
green.freq(1000)
blue.freq(1000)


def set_color(r, g, b):
    red.duty(r * 4); green.duty(g * 4); blue.duty(b * 4)


for i in range(0xffffff + 1):
    r, g, b = i // (256 ** 2), (i // 256) % 256, i % 256
    set_color(r, g, b)
