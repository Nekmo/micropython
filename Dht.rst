Dht
###
Los pines son, respectivamente: *VCC*, *Data*, *NC*, *Gnd*. El tercero no se usa, 
el primero es la entrada de 3-5V, el segundo es para datos. Tras ello, podemos empezar
a usar el módulo.

.. code-block::

    import dht
    d = dht.DHT11(machine.Pin(4))
    d.measure()
    d.temperature()  # 23
    d.humidity()  # 37
    
Hay 2 módulos posibles: DHT11 y DTH22. La diferencia entre ambos radica en su precio y 
precisión, siendo el segundo el mejor y más caro.

DTH11 vs DTH22
==============

DHT11
-----
* Muy bajo costo
* 3-5V alimentación y datos
* 2.5mA máximo mientras se piden datos.
* Lectura entre el 20-80% de humedad con una exactitud de 5%.
* Lee una temperatura entre 0 y 50°C con una exactitud de ±2°C.
* Frecuencia máxima 1 Hz (una lectura por segundo)
* Tamaño: 15.5mm x 12mm x 5.5mm

DHT22
-----
* Bajo costo
* 3-5V alimentación y datos
* 2.5mA máximo mientras se piden datos.
* Lectura entre el 0-100% de humedad con una exactitud de 2-5%.
* Lee una temperatura entre -40 y 125°C con una exactitud de ±0.5°C.
* Frecuencia máxima 0.5 Hz (una lectura por cada 2 segundos)
* Tamaño: 15.1mm x 25mm x 7.7mm

Fuente: https://learn.adafruit.com/dht/overview
