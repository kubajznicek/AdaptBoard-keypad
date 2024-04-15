from adafruit_hid.consumer_control_code import ConsumerControlCode # type: ignore
from adafruit_hid.keycode import Keycode # type: ignore
from micropython import const # type: ignore

MATRIX_ACTIONS = {
    0: lambda cc, kbd, layout: cc.send(ConsumerControlCode.PLAY_PAUSE),
    1: lambda cc, kbd, layout: cc.send(ConsumerControlCode.MUTE),
    2: lambda cc, kbd, layout: kbd.send(Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, Keycode.PAGE_UP),
    3: lambda cc, kbd, layout: kbd.send(Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, Keycode.PAGE_DOWN),
    4: lambda cc, kbd, layout: layout.write("Hello, World!"),
}

ANALOG_ACTIONS = {
    11: {
        True: lambda cc, mouse: cc.send(ConsumerControlCode.VOLUME_DECREMENT),
        False: lambda cc, mouse: cc.send(ConsumerControlCode.VOLUME_INCREMENT),
        "steps": 18,
        "type": "rotational",
    },
}

DISPLAY_CONFIG = {
    "present": const(False),
    "WIDTH": const(128),
    "HEIGHT": const(32),
}

ANALOG_THRESHOLD = const(100) # spocitat (jaky noise ma moving_average + kus pro jistotu)