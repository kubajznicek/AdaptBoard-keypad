import board # type: ignore
import keypad  # type: ignore
import busio # type: ignore
import displayio # type: ignore
import array

# lib imports
import neopixel # type: ignore
import usb_hid  # type: ignore
from adafruit_hid.consumer_control import ConsumerControl # type: ignore
from adafruit_hid.keyboard import Keyboard  # type: ignore
from adafruit_display_text import label # type: ignore

# local imports
from config import MATRIX_ACTIONS, ANALOG_ACTIONS, DISPLAY_CONFIG, ANALOG_THRESHOLD, DEBUG
from analog_signal_processor import AnalogSignalProcessor
if DISPLAY_CONFIG["present"]:
    from ssd1306_display import ssd1306_display as display
if DEBUG:
    from functions import log_cpu_info, print_storage_info, print_ram_info


displayio.release_displays()

matrix = keypad.KeyMatrix([board.D0, board.D1, board.D2, board.D3, board.D4], [board.D5, board.D6, board.D7, board.D8])   # https://docs.circuitpython.org/en/latest/shared-bindings/keypad/index.html#keypad.KeyMatrix
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)   # https://learn.adafruit.com/adafruit-kb2040/neopixel-led
cc = ConsumerControl(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)
if DISPLAY_CONFIG["present"]:
    i2c = busio.I2C(board.A3, board.A2)     # https://docs.circuitpython.org/en/latest/shared-bindings/busio/index.html
    my_display = display(i2c, 0x3C, DISPLAY_CONFIG)



if DISPLAY_CONFIG["present"]:
    my_display.render_text("Hello World!", 28, DISPLAY_CONFIG["HEIGHT"] // 2 - 1)
    # my_display.render_image("./test.bmp")

CHANNELS = []   # list of channels to be scanned
for key in ANALOG_ACTIONS.keys():
    CHANNELS.append(key)

my_analog = AnalogSignalProcessor(board.A0, (board.D10, board.MOSI, board.MISO, board.SCK), CHANNELS, 4)


if DEBUG:
    print()
    log_cpu_info()
    print()
    print_storage_info()
    print()
    print_ram_info()
    print("Ready!")

while True:
    key_event = matrix.events.get()

    if key_event and key_event.pressed:
        # print("pressed key number:", key_event.key_number)
        is_configured = MATRIX_ACTIONS.get(key_event.key_number, False)
        if is_configured:
            is_configured(cc, kbd)
        if key_event.key_number == 15: # ! for development purposes only
            triggered = 0
        else:
            print(f"WARNING!  -  Key {key_event.key_number} not configured")


    #region Analog Read

    # NOTE with triggered count
    # for channel in CHANNELS:
    #     my_analog.set_channel(channel)
    #     difference = abs(analog_values[channel] - my_analog.read_analog())
    #     if difference > ANALOG_THRESHOLD:
    #         triggered = round(difference/ANALOG_THRESHOLD)
    #         increased = analog_values[channel] < my_analog.read_analog()
    #         # print("channel", channel, "difference", difference, "triggered", triggered)
    #         for i in range(0, triggered):
    #             ANALOG_ACTIONS[channel][increased](cc)


    for channel in CHANNELS:
        if my_analog.channel_states[channel]["cool_down"] > 0:
            my_analog.channel_states[channel]["cool_down"] -= 1
            continue
        my_analog.set_channel(channel)
        current_value = my_analog.read_analog()
        # filter for noise

        # Add the current reading to the list of recent readings for this channel
        my_analog.analog_values[channel].append(current_value)

        # If we have more than N readings, remove the oldest one
        if len(my_analog.analog_values[channel]) > my_analog.window_size:
            my_analog.analog_values[channel].pop(0)

        # Calculate the moving average of the recent readings
        moving_average = sum(my_analog.analog_values[channel]) / len(my_analog.analog_values[channel])


        difference = abs(moving_average - current_value)
        # print(f"channel {channel} value {current_value}")

        if difference > ANALOG_THRESHOLD:
            # print("channel", channel, "difference", difference)
            increased = moving_average < current_value
            ANALOG_ACTIONS[channel][increased](cc)
            my_analog.channel_states[channel]["cool_down"] = my_analog.channel_settings[channel]["cool_down"]

        # analog_values[channel] = current_value
    #endregion