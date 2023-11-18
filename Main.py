import time
import board # type: ignore
import keypad  # type: ignore
import microcontroller # type: ignore
from micropython import const # type: ignore


import neopixel # type: ignore
import usb_hid  # type: ignore

from adafruit_hid.consumer_control import ConsumerControl # type: ignore
from adafruit_hid.consumer_control_code import ConsumerControlCode # type: ignore

from functions import log_cpu_info
from AnalogSignalProcessor import AnalogSignalProcessor

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)


my_analog = AnalogSignalProcessor(board.A0, (board.D0, board.D1, board.D2, board.D3))
matrix = keypad.KeyMatrix([board.D5, board.D6], [board.D7, board.D8])

cc = ConsumerControl(usb_hid.devices)

threshold = 190


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

    if keyEvent and keyEvent.pressed:
        print("event info", keyEvent.key_number)
        print("action", matrix_actions[keyEvent.key_number])
        cc.send(matrix_actions[keyEvent.key_number])


    #region Analog Read
    # import time


    for channel in range(0, 16):
        my_analog.set_channel(channel)
        my_analog.read_analog()








    # start_time = time.time()
    # for i in range(0, 1000):
        # for channel in range(0, 16):
            # my_analog.set_channel(channel)
            # my_analog.read_analog()
    # end_time = time.time()
    # print(f"The code took {end_time - start_time} seconds to run.")




    # print("cisty signal", my_analog.read_analog())

    #endregion

    
    # time.sleep(0.06)