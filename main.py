import time
import board # type: ignore
import keypad  # type: ignore
import microcontroller # type: ignore

import neopixel # type: ignore
import analogio # type: ignore
import usb_hid  # type: ignore

from adafruit_hid.consumer_control import ConsumerControl # type: ignore
from adafruit_hid.consumer_control_code import ConsumerControlCode # type: ignore

from functions import SetChannel, SetUpPinsForMCP, LogChannel, LogCpuInfo


pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
analog_pin = analogio.AnalogIn(board.A0)

mcp_pins = SetUpPinsForMCP((board.D0, board.D1, board.D2, board.D3))
matrix = keypad.KeyMatrix([board.D5, board.D6], [board.D7, board.D8])

cc = ConsumerControl(usb_hid.devices)


    
SetChannel(10, mcp_pins)
threshold = 170
position = analog_pin.value
lastPosition = position


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
    position = analog_pin.value
    if abs(lastPosition - position) > threshold:
        if lastPosition < position:
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        else:
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)

    lastPosition = position
    #endregion

    
    time.sleep(0.1)