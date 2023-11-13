def SetDigitalPin(pin: digitalio.DigitalInOut, value: bool):
    pin.value = value

def SetUpPinsForMCP(mcp_pins: tuple[microcontroller.Pin]):
    """
    Sets up the specified pins for the analog multiplexer.

    This function takes a tuple of Pin objects, sets each one as a digital output pin, and returns a tuple of the configured pins.

    Args:
        mcp_pins (tuple[Pin]): A tuple of Pin objects to be set up for the multiplexer.

        !!! note
            The number of pins must be exactly 4.

            Pins must be in order from least significant bit to most significant bit.

    Returns:
        tuple[DigitalInOut]: A tuple of DigitalInOut objects corresponding to the pins that have been set up.

    """
    import digitalio

    output_pins = tuple(digitalio.DigitalInOut(pin) for pin in mcp_pins)
    for pin in output_pins:
        pin.direction = digitalio.Direction.OUTPUT

    return output_pins

def SetChannel(channel: int, mpc_pins: tuple[digitalio.DigitalInOut]):
    """
    Sets the channel for a 4-pin digital output device.

    This function takes an integer representing the channel number, converts it to binary, and sets each of the 4 digital pins to the corresponding binary digit.

    Args:
        channel (int): The channel number to set. Must be between 0 and 15 (inclusive).
        mpc_pins (list[digitalio.DigitalInOut]): The list of digital pins to set. Must be of length 4.

    Raises:
        ValueError: If the channel number is not between 0 and 15.
    """

    if not 0 <= channel <= 15:
        raise ValueError("Channel must be between 0 and 15")
    

    binary_channel = bin(channel)[2:]
    binary_channel = '0' * (4 - len(binary_channel)) + binary_channel
    binary_channel = "".join(reversed(binary_channel))   # Reverse the string

    SetDigitalPin(mpc_pins[0], binary_channel[0] == '1')
    SetDigitalPin(mpc_pins[1], binary_channel[1] == '1')
    SetDigitalPin(mpc_pins[2], binary_channel[2] == '1')
    SetDigitalPin(mpc_pins[3], binary_channel[3] == '1')

def LogChannel(mpc_pins: tuple[digitalio.DigitalInOut]):
    """
    Logs the current channel to the console.

    This function reads the current channel of the multiplexer and prints it to the console.

    Args:
        mpc_pins (list[digitalio.DigitalInOut]): The list of digital pins to read. Must be of length 4.
    """
    channel = 0
    for i in range(4):
        channel += mpc_pins[i].value * 2**i
    print(channel)

def LogCpuInfo():
    """
    Logs CPU information to the console.

    This function prints the CPU frequency, temperature, and voltage to the console.
    """
    import microcontroller

    cpus = microcontroller.cpus

    for cpu in cpus:
        print("CPU frequency: " + str(cpu.frequency))
        print("Temperature: " + str(cpu.temperature))
        print("Voltage: " + str(cpu.voltage))
        print()