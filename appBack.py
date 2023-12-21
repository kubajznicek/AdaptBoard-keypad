import autopep8


def main():
    # default import
    default = "from adafruit_hid.consumer_control_code import ConsumerControlCode # type: ignore\nfrom adafruit_hid.keycode import Keycode # type: ignore\nfrom micropython import const # type: ignore\n\n"
    with open("app.py", "w") as f:
        # write into the file
        f.write(default)

        # reformating a string and then creating a file
        nl = "\n"
        lambdaKdb = ": lambda cc, kbd:"
        content = ""

        # array of contents of the Matrix function
        matrixArr = [
            "MATRIX_ACTIONS = {",
            nl,
            0,
            lambdaKdb,
            " cc.send(ConsumerControlCode.PLAY_PAUSE),",
            nl,
            1,
            lambdaKdb,
            " cc.send(ConsumerControlCode.MUTE),",
            nl,
            2,
            lambdaKdb,
            "cc.send(ConsumerControlCode.SCAN_NEXT_TRACK),",
            nl,
            3,
            lambdaKdb,
            "kbd.send(Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, Keycode.PAGE_DOWN),",
            nl,
            "}",
        ]
        for i in matrixArr:
            content += str(i)

        # rewrite the content of the file to python syntax using 'autopep8'
        content = autopep8.fix_code(content)
        f.write(content)


main()
