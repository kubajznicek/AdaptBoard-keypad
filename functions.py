import microcontroller # type: ignore


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