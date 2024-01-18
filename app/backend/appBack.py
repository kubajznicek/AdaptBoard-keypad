import autopep8


def main():
    default = "from adafruit_hid.consumer_control_code import ConsumerControlCode # type: ignore\nfrom adafruit_hid.keycode import Keycode # type: ignore\nfrom micropython import const # type: ignore\n\n"
    matrixInput = [
        [0, "PLAY_PAUSE"],
        [1, "MUTE"],
        [2, "CONTROL", "ALT", "SHIFT", "PAGE_UP"],
        [3, "CONTROL", "ALT", "SHIFT", "PAGE_DOWN"],
    ]
    # [["port index", "true", "false"]]
    analogInput = [[10, "VOLUME_INCREMENT", "VOLUME_DECREMENT"]]

    with open("app.py", "w") as f:
        # write into the file
        f.write(default)

        nl = "\n"
        lambdaKdb = ": lambda cc, kbd:"
        lambdaCc = "lambda cc:"
        cc = "cc.send("
        ccCode = "ConsumerControlCode."
        kdb = "kdb.send("
        kCode = "Keycode."
        content = ""

        # create a matrix actions
        matrixArr = []
        matrixArr.append("MATRIX_ACTIONS = {\n")
        for x in matrixInput:
            matrixArr.append(x[0])
            if len(x) == 2:
                matrixArr.append((lambdaKdb + cc + ccCode + x[1] + "),"))
            else:
                matrixArr.append((lambdaKdb + kdb))
                for i in range(len(x) - 1):
                    matrixArr.append((kCode + x[i + 1]))
                    if i < len(x) - 2:
                        matrixArr.append(",")
                    else:
                        matrixArr.append("),")
            matrixArr.append(nl)

        matrixArr.append("}\n\n")

        # import the content of the array to a one "content" string
        for i in matrixArr:
            content += str(i)

        # create analog actions contents
        analogArr = []
        analogArr.append("ANALOG_ACTIONS = {\n")
        for x in analogInput:
            analogArr.append((str(x[0]) + ": {" + nl))
            analogArr.append(("True:" + lambdaCc + cc + ccCode + x[1] + "),\n"))
            analogArr.append(("False:" + lambdaCc + cc + ccCode + x[2] + "),\n"))
            analogArr += "},\n"
        analogArr += "}"

        # import the content of the array to a one "content" string
        for i in analogArr:
            content += str(i)

        # rewrite the content of the file to python syntax using 'autopep8'
        content = autopep8.fix_code(content)
        f.write(content)


main()
