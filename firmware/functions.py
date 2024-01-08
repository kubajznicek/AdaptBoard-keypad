import gc
import os
import microcontroller # type: ignore
import json

def set_digital_pin(pin: digitalio.DigitalInOut, value: bool) -> None:
    pin.value = value

def log_cpu_info() -> None:
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

def print_storage_info():
    """
    Prints storage information to the console.
    """
    s = os.statvfs('/')
    total_space = s[0] * s[2]
    free_space = s[0] * s[3]
    used_space = total_space - free_space

    print('Total storage: ', total_space)
    print('Used storage: ', used_space)
    print('Free storage: ', free_space)
    

def print_ram_info():
    """
    Prints RAM information to the console.
    """
    gc.collect()  # run the garbage collector to free up as much RAM as possible
    total_ram = gc.mem_alloc() + gc.mem_free()
    used_ram = gc.mem_alloc()
    free_ram = gc.mem_free()

    print('Total RAM: ', total_ram)
    print('Used RAM: ', used_ram)
    print('Free RAM: ', free_ram)