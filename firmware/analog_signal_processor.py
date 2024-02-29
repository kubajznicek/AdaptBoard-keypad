import digitalio # type: ignore
from micropython import const # type: ignore
from analogio import AnalogIn # type: ignore

#local imports
from functions import set_digital_pin
from config import ANALOG_ACTIONS, ANALOG_THRESHOLD

class AnalogSignalProcessor:
    def __init__(self, analog_pin: microcontroller.Pin, mpc_pins: tuple[microcontroller.Pin],channels_to_scan: list, window_size:int = 5) -> None:
        self.__analog_pin = AnalogIn(analog_pin)
        self.__mpc_pins = const(self.set_up_pins_for_mpc(mpc_pins))
        self.__channel_settings = ANALOG_ACTIONS
        self.__channels_to_scan = channels_to_scan

        self.channel_state = [0 for _ in range(0, 16)]
        self.window_size = window_size
        self.analog_values = [[] for _ in range(0, 16)]  # list of past readings for each channel

        # calculate step size for each channel
        for channel in self.__channels_to_scan:
            self.__channel_settings[channel]["step_size"] = self.calculate_step_size(channel)

        # fill the analog values with initial values
        self.fill_analog_values()

        # calculate the initial step for each channel
        for channel in self.__channels_to_scan:
            moving_average = sum(self.analog_values[channel]) / len(self.analog_values[channel])
            self.channel_state[channel] = round(moving_average / self.__channel_settings[channel]["step_size"]) * self.__channel_settings[channel]["step_size"]

    def set_up_pins_for_mpc(self, mpc_pins: tuple[microcontroller.Pin]) -> tuple[digitalio.DigitalInOut]:
        """
        Sets up the specified pins for the analog multiplexer.

        This function takes a tuple of Pin objects, sets each one as a digital output pin, and returns a tuple of the configured pins.

        Parameters
        ----------
            mpc_pins (tuple[Pin]): A tuple of Pin objects to be set up for the multiplexer.

            !!! note
                The number of pins must be exactly 4.

                Pins must be in order from least significant bit to most significant bit.

        Returns
        -------
            tuple[DigitalInOut]: A tuple of DigitalInOut objects corresponding to the pins that have been set up.

        """


        output_pins = tuple(digitalio.DigitalInOut(pin) for pin in mpc_pins)
        for pin in output_pins:
            pin.direction = digitalio.Direction.OUTPUT

        return output_pins
    
    def calculate_step_size(self, channel: int) -> int:
        """
        Calculates the step size for a given channel.

        This function takes a channel number and returns the step size for that channel.

        Parameters
        ----------
            channel (int): The channel number for which to calculate the step size.

        Returns
        -------
            int: The step size for the specified channel.

        """

        return int(65535 / self.__channel_settings[channel]["steps"])

    def log_values(self) -> None:
        """
        Logs the current values to the console.

        This function reads the current values of the multiplexer and prints them to the console.
        """
        for channel in self.__channels_to_scan:
            print(f"Channel {channel}: {self.analog_values[channel]}")

    def set_channel(self, channel: int) -> None:
        """
        Sets the channel for a 4-pin digital output device.

        This function takes an integer representing the channel number, converts it to binary, and sets each of the 4 digital pins to the corresponding binary digit.

        Parameters
        ----------
            channel (int): The channel number to set. Must be between 0 and 15 (inclusive).

        Raises
        ------
            ValueError: If the channel number is not between 0 and 15.
        """

        if not 0 <= channel <= 15:
            raise ValueError("Channel must be between 0 and 15")

        mpc_pins = self.__mpc_pins

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
    
    def fill_analog_values(self) -> None:
        """
        Fills the analog values with initial values.

        This function fills the list of analog values with initial values to prevent false positives on startup.
        """

        for channel in self.__channels_to_scan:
            for i in range(0, self.window_size - 1):
                self.set_channel(channel)
                self.analog_values[channel].append(self.read_analog())

    def calculate_current_step(self, channel: int, current_value: int) -> int:
        """
        Calculates the current step for a given channel.

        This function takes a channel number and a current value, and returns the current step for that channel.

        Parameters
        ----------
            channel (int): The channel number for which to calculate the current step.
            current_value (int): The current value for the specified channel.

        Returns
        -------
            int: The current step for the specified channel.

        """

        # current_step = (current_value // self.channel_settings[channel]["step_size"]) * self.channel_settings[channel]["step_size"]
        
        # print("current_value", current_value, "channel_state", self.channel_state[channel], "step_size")
        # print(current_value > (self.channel_state[channel] + self.channel_settings[channel]["step_size"]/2) + ANALOG_THRESHOLD)

        # print("current_value", current_value, "channel_state", self.channel_state[channel], (self.channel_state[channel] + self.channel_settings[channel]["step_size"]/2) - ANALOG_THRESHOLD, (self.channel_state[channel] + self.channel_settings[channel]["step_size"]/2) + ANALOG_THRESHOLD)

        if current_value > (self.channel_state[channel] + self.__channel_settings[channel]["step_size"]/2) + ANALOG_THRESHOLD:
            return self.channel_state[channel] + self.__channel_settings[channel]["step_size"]
        
        elif current_value < (self.channel_state[channel] - self.__channel_settings[channel]["step_size"]/2) - ANALOG_THRESHOLD:
            return self.channel_state[channel] - self.__channel_settings[channel]["step_size"]
        
        else:
            return self.channel_state[channel]  # 0 - 65535
        
    def calculate_joystick_value(self, value: int) -> int:
        """
        Calculates the joystick value for a given channel.

        This function takes a value and returns the calculated joystick value.

        -100 to 100 (% of the maximum joystick movement)

        with 0 being the center (default) position, -100 being the maximum left position, and 100 being the maximum right position.

        Parameters
        ----------
            value (int): The value to calculate the joystick value for.

        Returns
        -------
            int: The calculated joystick value.

        """

        # Shift the range from [0, 65535] to [-32768, 32767]
        shifted_value = value - 32768

        # Scale the range from [-32768, 32767] to [-100, 100]
        scaled_value = shifted_value / 327.68

        # Apply an exponential scale
        exponent = 2  # Adjust this value as needed
        sign = -1 if scaled_value < 0 else 1  # Store the sign of the value
        exponential_value = sign * (abs(scaled_value) / 100) ** exponent * 100

        return int(exponential_value)
    
    def range_map(self, value:int, in_min=0 , in_max=65535, out_min=-127, out_max=127, deadzone_threshold=5) -> int:
        """
        Maps a value from one range to another.

        This function takes a value and maps it from one range to another.

        Parameters
        ----------
            x (int): The value to map.
            in_min (int): The lower bound of the input range.
            in_max (int): The upper bound of the input range.
            out_min (int): The lower bound of the output range.
            out_max (int): The upper bound of the output range.
            deadzone_threshold (int): The threshold for the joystick deadzone.

        Returns
        -------
            int: The mapped value.

        """
        # Map the value from the input range to the output range
        mapped_value = (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

        # If the mapped value is within the deadzone, return the center value
        if abs(mapped_value) < deadzone_threshold:
            return 0

        return mapped_value

    def process_new_reading(self, channel: int, current_value: int) -> int:
        """
        Processes a new reading for a given channel.

        This function takes a channel number and a current value and processes the new reading for that channel. Filters out noise and returns the smoothed value.

        Parameters
        ----------
            channel (int): The channel number for which to process the new reading.
            current_value (int): The current value for the specified channel.

        Returns
        -------
            int: The smoothed value for the specified channel.

        """

        # Add the current reading to the list of recent readings for this channel
        self.analog_values[channel].append(current_value)

        # If we have more than N readings, remove the oldest one
        if len(self.analog_values[channel]) > self.window_size:
            self.analog_values[channel].pop(0)

        # Calculate the moving average of the recent readings
        moving_average = sum(self.analog_values[channel]) / len(self.analog_values[channel])

        return moving_average