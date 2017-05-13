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

Consola por USB
===============

Usando **Picocom**::

    sudo picocom -b 115200 /dev/ttyUSB0

Usando **mpfshell**::

    mpfshell -c "open ttyUSB0; repl"
   
Trabajando con archivos
=======================
Para subir y trabajar con los archivos dentro del dispositivo, puede utilizarse **mpfshell**::

    mpfshell -c "open ttyUSB0"
    
También es posible conectarse vía Websockets::

    mpfshell -c "open ws:192.168.1.1,python"
    
Tras activar el modo shell, los comandos más relevantes son::

    put "main.py"  # Subir archivo (uno o varios)
    get "boot.py"  # Descargar archivo (uno o varios)
    rm "main.py"  # Borrar archivo remoto
    mput/mget/mrm .*\.py  # los 3 anteriores, pero usando regex
    ls  # Listar archivos en el directorio remoto
    cd  # Ir al directorio, en remoto
    pwd  # Mostrar la ruta dle directorio actual
    lls/lcd/lpwd  # Igual que los 3 anteriores, pero en local
    md "directory"  # Crear un directorio remoto
