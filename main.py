import board # type: ignore
import keypad  # type: ignore
import busio # type: ignore
import array

# lib imports
import neopixel # type: ignore
import usb_hid  # type: ignore
from adafruit_hid.consumer_control import ConsumerControl # type: ignore
from adafruit_hid.keyboard import Keyboard  # type: ignore

# local imports
from functions import log_cpu_info
from config import MATRIX_ACTIONS, ANALOG_ACTIONS, ANALOG_THRESHOLD, DEBUG
from analog_signal_processor import AnalogSignalProcessor



my_analog = AnalogSignalProcessor(board.A0, (board.D10, board.MOSI, board.MISO, board.SCK))

# https://docs.circuitpython.org/en/latest/shared-bindings/keypad/index.html#keypad.KeyMatrix
matrix = keypad.KeyMatrix([board.D5, board.D6], [board.D7, board.D8])

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
# https://docs.circuitpython.org/en/latest/shared-bindings/busio/index.html
# i2c_pokus = busio.I2C(board.A3, board.A2)
cc = ConsumerControl(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)


analog_values = array.array("H", [0]*16)



# fill analog_values with initial values
# this is done to prevent false positives on startup
for channel in range(0, 16):
    my_analog.set_channel(channel)
    analog_values[channel] = my_analog.read_analog()

if DEBUG:
    print()
    print()
    log_cpu_info()
    print("Ready!")

while True:
    key_event = matrix.events.get()

    if key_event and key_event.pressed:
        if DEBUG:
            print("pressed key number:", key_event.key_number)
        MATRIX_ACTIONS[key_event.key_number](cc, kbd)


    #region Analog Read

    # NOTE with triggered count
    # for channel in range(0, 16):
    #     my_analog.set_channel(channel)
    #     difference = abs(analog_values[channel] - my_analog.read_analog())
    #     if difference > ANALOG_THRESHOLD:
    #         triggered = round(difference/ANALOG_THRESHOLD)
    #         increased = analog_values[channel] < my_analog.read_analog()
    #         # print("channel", channel, "difference", difference, "triggered", triggered)
    #         for i in range(0, triggered):
    #             ANALOG_ACTIONS[channel][increased](cc)


    for channel in range(0, 16):
        my_analog.set_channel(channel)
        difference = abs(analog_values[channel] - my_analog.read_analog())
        if difference > ANALOG_THRESHOLD:
            if DEBUG:
                print("channel", channel, "difference", difference)
            increased = analog_values[channel] < my_analog.read_analog()
            ANALOG_ACTIONS[channel][increased](cc)

        analog_values[channel] = my_analog.read_analog()
    #endregion