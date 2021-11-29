import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, "color_values.py")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/color_values.py", color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402

HEX_VALUES = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 9,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        self.rgb = COLOR_NAMES.get(color.upper(), None)

    @staticmethod
    def hex2rgb(hex: str):
        """Class method that converts a hex value into an rgb one"""
        hex = hex.lstrip("#").upper()
        if len(hex) != 6:
            raise ValueError
        # hex_list = list(hex)
        if any([value not in HEX_VALUES.keys() for value in hex]):
            raise ValueError
        return tuple([int(hex[i : i + 2], 16) for i in range(0, len(hex), 2)])

    @staticmethod
    def rgb2hex(rgb: tuple):
        """Class method that converts an rgb value into a hex one"""
        if len(rgb) != 3:
            raise ValueError
        if any([(value < 0) | (value > 255) for value in list(rgb)]):
            raise ValueError
        return "#%02x%02x%02x" % rgb

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        if self.rgb is None:
            return "Unknown"
        else:
            return str(self.rgb)
