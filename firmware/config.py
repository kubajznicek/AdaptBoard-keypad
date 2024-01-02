from adafruit_hid.consumer_control_code import ConsumerControlCode # type: ignore
from adafruit_hid.keycode import Keycode # type: ignore
from micropython import const # type: ignore

MATRIX_ACTIONS = {
    0: lambda cc, kbd: cc.send(ConsumerControlCode.PLAY_PAUSE),
    1: lambda cc, kbd: cc.send(ConsumerControlCode.MUTE),
    2: lambda cc, kbd: kbd.send(Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, Keycode.PAGE_UP),
    3: lambda cc, kbd: kbd.send(Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, Keycode.PAGE_DOWN),
}

ANALOG_ACTIONS = {
    10: {
        True: lambda cc: cc.send(ConsumerControlCode.VOLUME_INCREMENT),
        False: lambda cc: cc.send(ConsumerControlCode.VOLUME_DECREMENT),
    },
    7: {
        True: lambda cc: print("channel 7 increased"),
        False: lambda cc: print("channel 7 decreased"),
    },
}

ANALOG_THRESHOLD:int = const(300) # optimal value for Windows 10 is around 200
DEBUG:bool = const(True)