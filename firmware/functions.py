import microcontroller # type: ignore
import json

def set_digital_pin(pin: digitalio.DigitalInOut, value: bool):
    pin.value = value

def log_cpu_info():
    """
    Logs CPU information to the console.

    This function prints the CPU frequency, temperature, and voltage to the console.
    """

    CPUS = microcontroller.cpus

    for cpu in CPUS:
        print("CPU frequency: " + str(cpu.frequency))
        print("Temperature: " + str(cpu.temperature))
        print("Voltage: " + str(cpu.voltage))
        print()

def read_matrix_config(file_name: str) -> dict:
    """
    Reads the matrix configuration from the config file.

    This function reads the matrix configuration from the config file and returns it as a dictionary.

    Parameters
    ----------
    file_name : str
        The name of the config file.

    Returns
    -------
    dict
        The matrix configuration.
    """

    with open(file_name, "r") as config_file:
        config = json.load(config_file)
        # stri away any comments beginning with __
        config = {k: v for k, v in config.items() if not k.startswith("__")}
        # convert dict keys to int
        config = {int(k): v for k, v in config.items()}


    return config
    