Leds
####

Encender y apagar leds
======================
.. code-block::

    import machine
    p4 = machine.Pin(4, machine.Pin.OUT)
    p4.high()  # Entender
    p4.low()  # Apagar


Parpadear led
=============
.. code-block::

    import time
    import machine
    p4 = machine.Pin(4, machine.Pin.OUT)
    for i in range(100):
        p4.value(i % 2); time.sleep(.5)
    
    
