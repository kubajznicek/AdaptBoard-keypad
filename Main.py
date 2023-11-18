import time
import board # type: ignore
import keypad  # type: ignore
import microcontroller # type: ignore
from micropython import const # type: ignore


import neopixel # type: ignore
import analogio # type: ignore
import usb_hid  # type: ignore

from adafruit_hid.consumer_control import ConsumerControl # type: ignore
from adafruit_hid.consumer_control_code import ConsumerControlCode # type: ignore

from functions import log_cpu_info
from AnalogSignalProcessor import AnalogSignalProcessor

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
analog_pin = analogio.AnalogIn(board.A0)

my_analog = AnalogSignalProcessor((board.D0, board.D1, board.D2, board.D3))
matrix = keypad.KeyMatrix([board.D5, board.D6], [board.D7, board.D8])

cc = ConsumerControl(usb_hid.devices)


    
my_analog.set_channel(0)
threshold = 190
position = analog_pin.value
lastPosition_1 = position
lastPosition = position

my_analog.log_channel()


matrix_actions = {
    0: ConsumerControlCode.PLAY_PAUSE,
    1: ConsumerControlCode.MUTE,
    2: ConsumerControlCode.SCAN_NEXT_TRACK,
    3: ConsumerControlCode.SCAN_PREVIOUS_TRACK,
}

print("Ready!")
while True:
    keyEvent = matrix.events.get()
    # print("events", keyEvent)

    if keyEvent and keyEvent.pressed:
        print("event info", keyEvent.key_number)
        print("action", matrix_actions[keyEvent.key_number])
        cc.send(matrix_actions[keyEvent.key_number])


    # print("cisty signal", analog_pin.value)
    
    #region Analog Read
    #TODO: Make this a function
    #TODO: mozna kontrolovat treba 3 cykly dozadu (kdyz clovek posune rychle, tak se to nezaregistruje)
    my_analog.set_channel(10)
    position = analog_pin.value
    if abs(lastPosition_1 - position) > threshold:
        if lastPosition_1 < position:
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        else:
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)

    lastPosition_1 = position


    my_analog.set_channel(0)
    position = analog_pin.value
    if abs(lastPosition - position) > threshold:
        if lastPosition < position:
            cc.send(ConsumerControlCode.BRIGHTNESS_DECREMENT)
        else:
            cc.send(ConsumerControlCode.BRIGHTNESS_INCREMENT )

    lastPosition = position
    #endregion

    
    time.sleep(0.06)