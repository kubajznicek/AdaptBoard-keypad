from adafruit_hid.consumer_control_code import ConsumerControlCode # type: ignore
from adafruit_hid.keycode import Keycode # type: ignore
from micropython import const # type: ignore

# config for the matrix keys
MATRIX_ACTIONS = {
    1: lambda cc, kbd, layout: cc.send(ConsumerControlCode.MUTE), # send consumer control code
    2: lambda cc, kbd, layout: kbd.send(Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, Keycode.PAGE_DOWN), # press key combination
    3: lambda cc, kbd, layout: layout.write("Hello, World!"), # write a string
}

# config for the analog modules
ANALOG_ACTIONS = {
    11: {
        True: lambda cc, kbd, mouse: cc.send(ConsumerControlCode.VOLUME_DECREMENT),
        False: lambda cc, kbd, mouse: cc.send(ConsumerControlCode.VOLUME_INCREMENT),
        "steps": 18, # number of segments
        "type": "rotational", # doesn't do anything yet (don't tell anyone :) )
    },
}

DISPLAY_CONFIG = {
    "present": const(False),
    "WIDTH": const(128),
    "HEIGHT": const(32),
}

# I guessed this number, it's the threshold for the analog signal used in the moving average filter
ANALOG_THRESHOLD = const(100)