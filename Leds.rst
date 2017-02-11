Leds digital
############
Los pines disponibles son el 0, 1*, 2, 3*, 4, 5, 12, 13, 14, 15, 16. El 1 y el 3 son utilizados por el REPL, así que puede ser problemático utilizarlos sobre todo en desarrollo.

Encender y apagar leds
======================
.. code-block::

    import machine
    p4 = machine.Pin(4, machine.Pin.OUT)
    p4.high()  # Entender
    p4.low()  # Apagar


Parpadear led (digital)
=======================
.. code-block::

    import time
    import machine
    p4 = machine.Pin(4, machine.Pin.OUT)
    for i in range(100):
        p4.value(i % 2); time.sleep(.5)
    
Leds analógico
##############
Puede usarse en todos los pines del digital excepto el 16.

Activación y desactivación
==========================
Con lo siguiente activamos el modo "analógico" (PWM) en el pin 4. Es necesario remarcar que el PWM de Arduino/ESP8266 no es realmente analógico, sino una simulación, y por tanto no puede usarse para modular el voltaje de salida, por lo que puede quemar con un 5V algo que como máximo acepta 3V. Más información: https://www.luisllamas.es/salidas-analogicas-pwm-en-arduino/

.. code-block::

    import machine
    pwm4 = machine.PWM(machine.Pin(4))
    
Para desactivarlo:

.. code-block::

    pwm4.deinit()

Frequency y duty
================
En el modo PWM podemos variar 2 cosas: ``frequency`` y ``duty``. El primero en el led determina la frecuencia entre apagado y encendido, y el segundo la itensidad. El primero acepta valores de 1 a 1000 (está en Hz) y el segundo de 0 a 1023. Todos inclusive. Ambos valores se encuentran relacionados, y el de uno afectará al otro.

En el siguiente caso parapadea con intensidad media, visible al ojo humano, en intervalos de aproximadamente medio segundo:

.. code-block::

    import machine
    pwm4 = machine.PWM(machine.Pin(4))
    pwm4.freq(1)
    pwm4.duty(500)
    
Intensidad media con parpadeos rápidos, pero visibles al ojo humano:

.. code-block::

    pwm4.freq(10)
    pwm4.duty(500)
    
Intensidad media con parpadeos muy rápidos, casi indistinguibles, pero visibles al ojo humano:

.. code-block::

    pwm4.freq(40)
    pwm4.duty(500)

Fogonazos instantáneos:

.. code-block::

    pwm4.freq(1)
    pwm4.duty(50)
    
Frecuencia máxima (invisible ojo humano), intensidad baja:

.. code-block::

    pwm4.freq(1000)
    pwm4.duty(2)

Led 4 pines (multicolor)
########################
El anodo (el pin más largo) va a tierra, y los otros 3 a otros pines. Teniendo en cuenta el ánodo, los pines corresponden a: ``R - A - G - B``, donde *R* es Red, *A* en Ánodo, *G* es Green y *B* es Blue.

Para iniciarlos:

.. code-block::

    red = machine.PWM(machine.Pin(12))
    green = machine.PWM(machine.Pin(14))
    blue = machine.PWM(machine.Pin(4))
    red.freq(500)
    green.freq(500)
    blue.freq(500)
    
Colores básicos:
    
.. code-block::

    # Rojo
    red.duty(1000); green.duty(0); blue.duty(0)
    # Verde
    red.duty(0); green.duty(1000); blue.duty(0)
    # Azul
    red.duty(0); green.duty(0); blue.duty(1000)


