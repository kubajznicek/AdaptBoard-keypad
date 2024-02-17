import gc
import os
import time
import microcontroller # type: ignore

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

def set_neopixel_color(pixel: neopixel.NeoPixel, color: Tuple[int, int, int]) -> None:
    """
    Sets the color of the neopixel.

    This function takes a neopixel object and a tuple of RGB values and sets the color of the neopixel to the specified color.

    Parameters
    ----------
        pixel (neopixel.NeoPixel): The neopixel object to set the color of.
        color (Tuple[int, int, int]): A tuple of RGB values representing the color to set the neopixel to.

    """
    pixel.fill(color)

def start_up_blink(pixel: neopixel.NeoPixel):
    """
    Blinks the neopixel on startup.

    This function blinks the neopixel on startup to indicate that the device is ready to use.

    Parameters
    ----------
        pixel (neopixel.NeoPixel): The neopixel object to blink.
    """
    set_neopixel_color(pixel, (0, 0, 120))
    time.sleep(0.1)
    set_neopixel_color(pixel, (0, 0, 0))
    time.sleep(0.1)
    set_neopixel_color(pixel, (0, 0, 120))
    time.sleep(0.1)
    set_neopixel_color(pixel, (0, 0, 0))
