import time
import board # type: ignore
import keypad  # type: ignore
import digitalio # type: ignore
import array
from micropython import const # type: ignore


import neopixel # type: ignore
import usb_hid  # type: ignore
from adafruit_hid.consumer_control import ConsumerControl # type: ignore
from adafruit_hid.consumer_control_code import ConsumerControlCode # type: ignore

from functions import log_cpu_info
from AnalogSignalProcessor import AnalogSignalProcessor



pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
my_analog = AnalogSignalProcessor(board.A0, (board.D10, board.MOSI, board.MISO, board.SCK))
matrix = keypad.KeyMatrix([board.D5, board.D6], [board.D7, board.D8])
cc = ConsumerControl(usb_hid.devices)

ANALOG_THRESHOLD = const(300)

MATRIX_ACTIONS = {
    0: ConsumerControlCode.PLAY_PAUSE,
    1: ConsumerControlCode.MUTE,
    2: ConsumerControlCode.SCAN_NEXT_TRACK,
    3: ConsumerControlCode.SCAN_PREVIOUS_TRACK,
}

analog_values = array.array("H", [0]*16)


# fill analog_values with initial values
# this is done to prevent false positives on startup
for channel in range(0, 16):
    my_analog.set_channel(channel)
    analog_values[channel] = my_analog.read_analog()

log_cpu_info()
print("Ready!")
while True:
    key_event = matrix.events.get()

    if key_event and key_event.pressed:
        print("event info", key_event.key_number)
        print("action", MATRIX_ACTIONS[key_event.key_number])
        cc.send(MATRIX_ACTIONS[key_event.key_number])


    #region Analog Read

    # for channel in range(0, 16):
    #     my_analog.set_channel(channel)
    #     difference = abs(analog_values[channel] - my_analog.read_analog())
    #     if difference > ANALOG_THRESHOLD:
    #         triggered = round(difference/ANALOG_THRESHOLD)
    #         increased = analog_values[channel] < my_analog.read_analog()
    #         # print("channel", channel, "difference", difference, "triggered", triggered)
    #         for i in range(0, triggered):
    #             if increased:
    #                 cc.send(ConsumerControlCode.VOLUME_INCREMENT)
    #             else:
    #                 cc.send(ConsumerControlCode.VOLUME_DECREMENT)


    for channel in range(0, 16):
        my_analog.set_channel(channel)
        difference = abs(analog_values[channel] - my_analog.read_analog())
        if difference > ANALOG_THRESHOLD:
            print("channel", channel, "difference", difference)

        

            # increased = analog_values[channel] < my_analog.read_analog()
            # # print("channel", channel, "difference", difference, "triggered", triggered)
            # if increased:
            #     cc.send(ConsumerControlCode.VOLUME_INCREMENT)
            # else:
            #     cc.send(ConsumerControlCode.VOLUME_DECREMENT)




        analog_values[channel] = my_analog.read_analog()








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