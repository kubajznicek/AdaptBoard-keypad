from micropython import const # type: ignore
import digitalio # type: ignore
from analogio import AnalogIn # type: ignore

from functions import set_digital_pin

class AnalogSignalProcessor:
    def __init__(self, analog_pin: microcontroller.Pin, mpc_pins: tuple[microcontroller.Pin]):
        self.__analog_pin = AnalogIn(analog_pin)
        self.__mpc_pins = const(self.set_up_pins_for_mpc(mpc_pins))
        self.channel = 0
        self.set_channel(0)


    def __str__(self) -> str:
        return f"AnalogSignalProcessor: \n Current channel is {self.channel}."


    def set_up_pins_for_mpc(self, mpc_pins: tuple[microcontroller.Pin]) -> tuple[digitalio.DigitalInOut]:
        """
        Sets up the specified pins for the analog multiplexer.

        This function takes a tuple of Pin objects, sets each one as a digital output pin, and returns a tuple of the configured pins.

        Args:
            mpc_pins (tuple[Pin]): A tuple of Pin objects to be set up for the multiplexer.

            !!! note
                The number of pins must be exactly 4.

                Pins must be in order from least significant bit to most significant bit.

        Returns:
            tuple[DigitalInOut]: A tuple of DigitalInOut objects corresponding to the pins that have been set up.

        """


        output_pins = tuple(digitalio.DigitalInOut(pin) for pin in mpc_pins)
        for pin in output_pins:
            pin.direction = digitalio.Direction.OUTPUT

        return output_pins
    
    def log_channel(self):
        """
        Logs the current channel to the console.

        This function reads the current channel of the multiplexer and prints it to the console.
        """
        print("Multiplexer set to channel", self.channel)
    
    def log_values(self):
        """
        Logs the current values to the console.

        This function reads the current values of the multiplexer and prints them to the console.
        """
        for channel in self.values:
            print(f"Channel {channel}: {self.values[channel]}")

    def set_channel(self, channel: int):
        """
        Sets the channel for a 4-pin digital output device.

        This function takes an integer representing the channel number, converts it to binary, and sets each of the 4 digital pins to the corresponding binary digit.

        Args:
            channel (int): The channel number to set. Must be between 0 and 15 (inclusive).

        Raises:
            ValueError: If the channel number is not between 0 and 15.
        """

        if not 0 <= channel <= 15:
            raise ValueError("Channel must be between 0 and 15")

        mpc_pins = self.__mpc_pins
        self.channel = channel

        binary_channel = bin(channel)[2:]
        binary_channel = '0' * (4 - len(binary_channel)) + binary_channel
        binary_channel = "".join(reversed(binary_channel))   # Reverse the string

        set_digital_pin(mpc_pins[0], binary_channel[0] == '1')
        set_digital_pin(mpc_pins[1], binary_channel[1] == '1')
        set_digital_pin(mpc_pins[2], binary_channel[2] == '1')
        set_digital_pin(mpc_pins[3], binary_channel[3] == '1')

    def read_analog(self) -> int:
        """
        Reads the analog value from the multiplexer.

        This function reads the analog value from the multiplexer and returns it as an integer.
        """

        # jak dlouho cte signal nez to digitalizuje

        return self.__analog_pin.value