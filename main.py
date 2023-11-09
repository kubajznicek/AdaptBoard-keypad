# blink example

import time
import board # type: ignore
import neopixel # type: ignore

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
print("hello filip")

while True:
    pixels.fill((255, 0, 0))
    time.sleep(0.5)
    pixels.fill((0, 0, 255))
    time.sleep(0.5)