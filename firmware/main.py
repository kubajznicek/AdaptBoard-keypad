import board # type: ignore
import keypad  # type: ignore
import busio # type: ignore
import displayio # type: ignore

# lib imports
import neopixel # type: ignore
import usb_hid  # type: ignore
from adafruit_hid.consumer_control import ConsumerControl # type: ignore
from adafruit_hid.keyboard import Keyboard  # type: ignore
from adafruit_hid.mouse import Mouse  # type: ignore
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS # type: ignore

# local imports
from config import MATRIX_ACTIONS, ANALOG_ACTIONS, DISPLAY_CONFIG
from functions import start_up_blink
from analog_signal_processor import AnalogSignalProcessor
if DISPLAY_CONFIG["present"]:
    from ssd1306_display import ssd1306_display as display


displayio.release_displays()

matrix = keypad.KeyMatrix([board.D0, board.D1, board.D2, board.D3, board.D4], [board.D5, board.D6, board.D7, board.D8])   # https://docs.circuitpython.org/en/latest/shared-bindings/keypad/index.html#keypad.KeyMatrix
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)   # https://learn.adafruit.com/adafruit-kb2040/neopixel-led
cc = ConsumerControl(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
mouse = Mouse(usb_hid.devices)
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

print("Starting main loop")
start_up_blink(pixels)
while True:
    # scan the keypad matrix
    key_event = matrix.events.get()

    if key_event and key_event.pressed:
        key_action = MATRIX_ACTIONS.get(key_event.key_number, False)
        if key_action:
            key_action(cc, kbd, layout)
        else:
            print(f"WARNING!  -  Key {key_event.key_number} not configured")
        # if key_event.key_number == 4: # ! for development purposes only
            # layout.write("!@#$%^&*2š()_++}{';/./<?>:[}321654987*/-*/+00|\}]{[::??>><<~12]}]}")


    #region Analog Read
    for channel in CHANNELS:
        my_analog.set_channel(channel)
        current_value = my_analog.read_analog()

        # process the new reading
        smoothed_value = my_analog.process_new_reading(channel, current_value)
        current_step = my_analog.calculate_current_step(channel, smoothed_value)

        # check if the step has changed
        if my_analog.channel_state[channel] == current_step:
            continue

        # if the step has changed, perform the action
        increased = my_analog.channel_state[channel] < current_step
        ANALOG_ACTIONS[channel][increased](cc, mouse, 0)

        # update the channel state
        my_analog.channel_state[channel] = current_step
    #endregion