from grove.grove_ws2813_rgb_led_strip import GroveWS2813RgbStrip
from rpi_ws281x import Color
import time

PIN, COUNT = 18,30
strip = GroveWS2813RgbStrip(PIN, COUNT)


def colorWipe(strip, color, wait_ms=140):
    """Wipe color across display a pixel at a time."""
    for i in range(25, strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

# uv is ... ulra-violet
color = Color(62,6,148)

while True:
    colorWipe(strip, color)
    colorWipe(strip, Color(0, 0, 0))
