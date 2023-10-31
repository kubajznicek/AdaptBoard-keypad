# Developing for AdaptBoard-keypad

AdaptBoard software is written in CircuitPython, a subset of Python 3. It is designed to be easy to use and to run on microcontrollers with small amounts of RAM and flash memory. CircuitPython is open source and available on [GitHub](https://github.com/adafruit/circuitpython).

## Getting Started

To get started, you'll need to install the latest version of CircuitPython for your board. Please follow the instructions in the [KB2040 docs](https://learn.adafruit.com/adafruit-kb2040/circuitpython) to install CircuitPython on your board.

## Dependencies

The following libraries are required for the AdaptBoard-keypad to work:

XXXXXXXXXXXXXXX
doplnit co je potreba
XXXXXXXXXXXXXXX

program for displaying output from serial port
- Linux **screen** or **minicom**
- Windows **PuTTY**


## Developing

**⚠️ Warning**

> Adafruit recommends their Mu editor for CircuitPython development, because other IDE may save the files corrupted. However, you can use your IDE of choice and the copy the files onto the board.

copying files to the board

```bash
cp -r main.py /media/$USER/CIRCUITPY/
```

## Debugging

To debug your code, you can use the serial output. You can use the following command to display the output:

```bash
sudo screen /dev/ttyACM0
```


