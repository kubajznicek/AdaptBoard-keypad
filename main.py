import time
import board # type: ignore
import neopixel # type: ignore
import analogio # type: ignore

from functions import SetChannel, SetUpPinsForMCP


pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
analog_pin = analogio.AnalogIn(board.A0)

mcp_pins = SetUpPinsForMCP((board.D0, board.D1, board.D2, board.D3))

print(mcp_pins)



    
SetChannel(0, mcp_pins)

while True:
    print("cisty signal", analog_pin.value)
    print()
    time.sleep(0.1)