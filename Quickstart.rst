Guía básica
###########

Instalar
========

.. code-block::

  pip install esptool


.. code-block::

  sudo esptool.py --port /dev/ttyUSB0 erase_flash


Descarga firmware: http://micropython.org/download#esp8266

.. code-block::

  sudo esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 /tmp/esp8266-*.bin

Tras esto estará la red Wifi ``MicroPython-******`` disponible.

