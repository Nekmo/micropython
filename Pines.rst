Pines
#####

Los pines usables para IO son::

    0,2,4,5,12,13,14,15,16

Puede comprobar qué pin de la placa corresponde con qué numeración de Micropython usando un led conectado entre el pin y Ground::

    import time
    for i in [0,2,4,5,12,13,14,15,16]:
        print('Pin {}'.format(i))
        Pin(i, Pin.OUT, value=1)
        time.sleep(2)
        Pin(i, Pin.OUT, value=0)


Pines ESP-12E WeMos D1
======================

===========  ======   ===
Micropython  Placa    PWM
-----------  ------   ---
4            4        Sí
14           D13/D5   Sí
12           D12/D6   Sí
===========  ======   ===
