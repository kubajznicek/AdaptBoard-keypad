# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: Unlicense
# kbd.send(Keycode.SHIFT, Keycode.X)
# layout.write("Lukas\n")


import board  # type: ignore
import digitalio  # type: ignore
import neopixel  # type: ignore
import time
import analogio  # type: ignore

# for writing a Keycode
import usb_hid  # type: ignore
from adafruit_hid.keyboard import Keyboard  # type: ignore
from adafruit_hid.keycode import Keycode  # type: ignore

# for writing a text
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS  # type: ignore

# variable for a keyboard
kbd = Keyboard(usb_hid.devices)
# layout, for writing a text by button
layout = KeyboardLayoutUS(kbd)

# variable increase a volume
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

cc = ConsumerControl(usb_hid.devices)

# initialize a led on board with variable to address it
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

# variable for a digital pin on board
button_2 = digitalio.DigitalInOut(board.D2)
button_3 = digitalio.DigitalInOut(board.D3)
button_2.switch_to_input(pull=digitalio.Pull.UP)
button_3.switch_to_input(pull=digitalio.Pull.UP)

analog_pin = analogio.AnalogIn(board.A3)

lastPosition = analog_pin.value

while True:
    # volume pin A3
    threshold = 150
    position = analog_pin.value
    if abs(lastPosition - position) > threshold:
        if lastPosition < position:
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        else:
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)
    lastPosition = position

    # buttons on pin 2 and 3
    if not button_2.value:
        pixel.fill((0, 255, 0))
        kbd.send(Keycode.LEFT_CONTROL, Keycode.V)
        time.sleep(0.5)
    elif not button_3.value:
        pixel.fill((0, 0, 255))
        kbd.send(Keycode.LEFT_CONTROL, Keycode.C)
        time.sleep(0.5)
    else:
        pixel.fill((0, 0, 0))
