import time
import board # type: ignore
import neopixel # type: ignore
import analogio # type: ignore
import usb_hid  # type: ignore

from adafruit_hid.consumer_control import ConsumerControl # type: ignore
from adafruit_hid.consumer_control_code import ConsumerControlCode # type: ignore

from functions import SetChannel, SetUpPinsForMCP, LogChannel


pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
analog_pin = analogio.AnalogIn(board.A0)

mcp_pins = SetUpPinsForMCP((board.D0, board.D1, board.D2, board.D3))

cc = ConsumerControl(usb_hid.devices)


    
SetChannel(10, mcp_pins)
threshold = 160
position = analog_pin.value
lastPosition = position

while True:
    LogChannel(mcp_pins)
    print("cisty signal", analog_pin.value)
    
    position = analog_pin.value
    if abs(lastPosition - position) > threshold:
        if lastPosition < position:
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        else:
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)

    lastPosition = position

    time.sleep(0.1)