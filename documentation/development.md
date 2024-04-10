# Developing for AdaptBoard-keypad

AdaptBoard software is written in CircuitPython 8.2.7, a subset of Python 3. It is designed to be easy to use and to run on microcontrollers with small amounts of RAM and flash memory. CircuitPython is open source and available on [GitHub](https://github.com/adafruit/circuitpython).
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

## Enabling and disabling CircuitPython devices

CircuitPython has support for a number of devices. You can enable or disable these devices by editing the `boot.py` file on the CIRCUITPY drive.

```python
import usb_midi # type: ignore
usb_midi.disable()
```

[Adafruit device docs](https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial)

If you disabled `'storage.disable_usb_drive()'` in boot.py, you can enable it by entering safe mode. To enter safe mode, press the reset button twice.

When in safe mode **no code will be executed** and the CIRCUITPY drive will be mounted and you can edit the `boot.py` file.

**⚠️ Warning**

>**`boot.py` is only executed after a hard reset or a power cycle**

[Adafruit safe mode docs](https://learn.adafruit.com/circuitpython-safe-mode/overview)


## Debugging

programs for displaying output from serial port:
- Linux **screen** or **minicom**
- Windows **PuTTY**

### Steps
- Connect the board to your computer using a USB cable.
- The board should appear as a USB drive named CIRCUITPY.
    > If not you can enable it in safe mode by pressing the reset button twice. For more information see [Enabling and disabling CircuitPython devices](#enabling-and-disabling-circuitpython-devices)
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
