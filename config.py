from adafruit_hid.consumer_control_code import ConsumerControlCode # type: ignore
from adafruit_hid.keycode import Keycode # type: ignore

MATRIX_ACTIONS = {
    0: lambda cc, kbd: cc.send(ConsumerControlCode.PLAY_PAUSE),
    1: lambda cc, kbd: cc.send(ConsumerControlCode.MUTE),
    2: lambda cc, kbd: cc.send(ConsumerControlCode.SCAN_NEXT_TRACK),
    # 3: lambda cc: cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK),
    3: lambda cc, kbd: kbd.send(Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, Keycode.PAGE_DOWN),
}

ANALOG_ACTIONS = {
    10: {
        True: lambda cc: cc.send(ConsumerControlCode.VOLUME_INCREMENT),
        False: lambda cc: cc.send(ConsumerControlCode.VOLUME_DECREMENT),
    },
}