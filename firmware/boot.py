# boot.py runs only after a hard reset. So if you change boot.py, you'll need to reset the board to have it re-run.
# Just editing boot.py or typing ctrl-D in the REPL will not cause it to re-run again.
# Make sure your changes are completely written out before you reset, to avoid confusion and filesystem corruption.

# https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial


import usb_midi # type: ignore
import storage # type: ignore

usb_midi.disable()
# storage.disable_usb_drive()