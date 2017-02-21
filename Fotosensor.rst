Fotosensor
##########
Los fotosensores permiten distinguir la cantidad de luz en el ambiente, pudiéndose usar 
para detectar obstáculos entre el sensor y la luz, o para saber cuando ya no hay iluminación.
Se trata resistencia que permitirá pasar la electricidad con luz, y no la dejará pasar cuando
no la haya, teniendo una amplia variación entre ambos estados. Además, son sumamente económicos.

Aunque pueden usarse los pines digitales, lo mejor es utilizar el pin analógico de entrada
(en Wemos D1, el pin A0) para poder detectar un gran espectro de cambios.

.. code-block::

    from machine import ADC
    adc = ADC(0)
    adc.read()  # 1024 con habitación iluminada
    adc.read()  # 744 habitación mal iluminada
    adc.read()  # 318 habitación iluminada por los monitores
    adc.read()  # 30 como en el anterior, pero además tapando el sensor
