import displayio # type: ignore
import terminalio # type: ignore

# lib imports
import adafruit_displayio_ssd1306 # type: ignore
from adafruit_display_text import label # type: ignore


class ssd1306_display:
    def __init__(self, i2c: busio.I2C, I2C_ADDRESS: hex, DISPLAY_CONFIG: dict) -> None:
        try:
            display_bus = displayio.I2CDisplay(i2c, device_address=I2C_ADDRESS)
        except ValueError:
            print(f"Error: No display found at address {I2C_ADDRESS}")
            display_bus = None
            return
        
        display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=DISPLAY_CONFIG["WIDTH"], height=DISPLAY_CONFIG["HEIGHT"])
        sprites = displayio.Group()
        display.root_group = sprites
        
        self.display_bus = display_bus
        self.sprites = sprites

    def __str__(self) -> str:
        return f"SSD1306 Display: \n {self.display_bus}"
    
    def clear(self) -> None:
        """
        Clears the display.
        """
        self.sprites.clear()

    def render_text(self, text: str, x: int, y: int) -> None:
        """
        Renders text to the display.

        Parameters
        ----------
            text (str): The text to be rendered.

            x (int): The x coordinate of the text.

            y (int): The y coordinate of the text.
        """
        text_area = label.Label(
            terminalio.FONT, text=text, color=0xFFFFFF, x=x, y=y
        )
        self.sprites.append(text_area)

    def render_image(self, image: str) -> None:
        """
        Renders an image to the display.

        Parameters
        ----------
            image (displayio.Bitmap): The image to be rendered.

            x (int): The x coordinate of the image.

            y (int): The y coordinate of the image.
        """
        odb = displayio.OnDiskBitmap(image)
        image_sprite = displayio.TileGrid(odb, pixel_shader=displayio.ColorConverter())
        self.sprites.append(image_sprite)
