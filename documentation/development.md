# Developing for AdaptBoard-keypad

AdaptBoard software is written in CircuitPython, a subset of Python 3. It is designed to be easy to use and to run on microcontrollers with small amounts of RAM and flash memory. CircuitPython is open source and available on [GitHub](https://github.com/adafruit/circuitpython).
[CircuitPython tricks](https://github.com/todbot/circuitpython-tricks)

## Getting Started

To get started, you'll need to install the latest version of CircuitPython for your board. Please follow the instructions in the [KB2040 docs](https://learn.adafruit.com/adafruit-kb2040/circuitpython) to install CircuitPython on your board.

## Dependencies

The following libraries are required for the AdaptBoard-keypad to work:

- adafruit_display_text
- adafruit_hid
- adafruit_pixelbuf.mpy
- neopixel.mpy


## Developing

**⚠️ Warning**

> Adafruit recommends their Mu editor for CircuitPython development, because other IDE may save the files corrupted. However, you can use your IDE of choice and the copy the files onto the board.

copying files to the board

```bash
cp -r main.py /media/$USER/CIRCUITPY/
```

## Debugging

programs for displaying output from serial port:
- Linux **screen** or **minicom**
- Windows **PuTTY**

### Steps
- Connect the board to your computer using a USB cable.
- The board should appear as a USB drive named CIRCUITPY.
- Find the serial port for the board.
    - On Windows, you can use the Device Manager to find the serial port.

    - On Linux, you can use the following command to list the serial ports:

    ```bash
    ls /dev/ttyACM*
    ``` 

- Connect to the serial port using the serial terminal program.
    - On Windows, you can use PuTTY to connect to the serial port.

    - On Linux, you can use the screen command to connect to the serial port.
    ```bash
    sudo screen /dev/ttyACM0 # replace with your port
    ```
