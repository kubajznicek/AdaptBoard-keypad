from adafruit_hid.consumer_control_code import ConsumerControlCode # type: ignore
from adafruit_hid.keycode import Keycode # type: ignore
from micropython import const # type: ignore

MATRIX_ACTIONS = {
    0: lambda cc, kbd: cc.send(ConsumerControlCode.PLAY_PAUSE),
    1: lambda cc, kbd: cc.send(ConsumerControlCode.MUTE),
    2: lambda cc, kbd: kbd.send(Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, Keycode.PAGE_UP),
    3: lambda cc, kbd: kbd.send(Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, Keycode.PAGE_DOWN),
    19: lambda cc, kbd: kbd.send(Keycode.A, Keycode.B),
}

ANALOG_ACTIONS = {
    7: {
        True: lambda cc: cc.send(ConsumerControlCode.VOLUME_INCREMENT),
        False: lambda cc: cc.send(ConsumerControlCode.VOLUME_DECREMENT),
    },
}

DISPLAY_CONFIG = {
    "WIDTH": const(128),
    "HEIGHT": const(32),
}

ANALOG_THRESHOLD:int = const(250) # optimal value for Windows 10 is around 200
DEBUG:bool = const(True)