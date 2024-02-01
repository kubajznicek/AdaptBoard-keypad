import board # type: ignore
import keypad  # type: ignore
import busio # type: ignore
import displayio # type: ignore
import terminalio # type: ignore
import adafruit_displayio_ssd1306 # type: ignore
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
from ssd1306_display import ssd1306_display as display
if DEBUG:
    from functions import log_cpu_info, print_storage_info, print_ram_info, no_action


displayio.release_displays()

matrix = keypad.KeyMatrix([board.D0, board.D1, board.D2, board.D3, board.D4], [board.D5, board.D6, board.D7, board.D8])   # https://docs.circuitpython.org/en/latest/shared-bindings/keypad/index.html#keypad.KeyMatrix
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)   # https://learn.adafruit.com/adafruit-kb2040/neopixel-led
i2c = busio.I2C(board.A3, board.A2)     # https://docs.circuitpython.org/en/latest/shared-bindings/busio/index.html
cc = ConsumerControl(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)

my_analog = AnalogSignalProcessor(board.A0, (board.D10, board.MOSI, board.MISO, board.SCK))
my_display = display(i2c, 0x3C, DISPLAY_CONFIG)

# BORDER = 5
# WIDTH = DISPLAY_CONFIG["WIDTH"]
# HEIGHT = DISPLAY_CONFIG["HEIGHT"]
# color_bitmap = displayio.Bitmap(DISPLAY_CONFIG["WIDTH"], DISPLAY_CONFIG["HEIGHT"], 1)
# color_palette = displayio.Palette(1)
# color_palette[0] = 0xFFFFFF  # White

# bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
# splash.append(bg_sprite)

# # Draw a smaller inner rectangle
# inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
# inner_palette = displayio.Palette(1)
# inner_palette[0] = 0x000000  # Black
# inner_sprite = displayio.TileGrid(
#     inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
# )
# splash.append(inner_sprite)

# # Draw a label
# text = "Hello World!"
# text_area = label.Label(
#     terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=HEIGHT // 2 - 1
# )
# splash.append(text_area)

# my_display.render_text("Hello World!", 28, DISPLAY_CONFIG["HEIGHT"] // 2 - 1)
my_display.render_image("./test.bmp")

analog_values = array.array("H", [0]*16)
CHANNELS = []
for key in ANALOG_ACTIONS.keys():
    CHANNELS.append(key)







# fill analog_values with initial values
# this is done to prevent false positives on startup
for channel in range(0, 16):
    my_analog.set_channel(channel)
    analog_values[channel] = my_analog.read_analog()

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
        # MATRIX_ACTIONS.get(key_event.key_number, no_action(key_event.key_number))(cc, kbd) # nefunguje
        MATRIX_ACTIONS[key_event.key_number](cc, kbd) # TODO at to nepada kdyz tam neni definovana klavesa (pokus o radek vys)


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
        my_analog.set_channel(channel)
        current_value = my_analog.read_analog()
        difference = abs(analog_values[channel] - current_value)
        # print(f"channel {channel} value {current_value}")
        if difference > ANALOG_THRESHOLD:
            # print("channel", channel, "difference", difference)
            increased = analog_values[channel] < current_value
            ANALOG_ACTIONS[channel][increased](cc)

        analog_values[channel] = current_value
    #endregion