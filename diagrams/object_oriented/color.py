"""
diagram.object_oriented.color
=============================

Provides the color class representing colors of diagram components.
"""
class Color:
    """
    The color of diagram components.

    Attributes:
        color_code(``str``): The color represented in HTML HEX string format.
    """
    @staticmethod
    def black():
        """The color black."""
        return Color("#000000")

    @staticmethod
    def red():
        """The color red."""
        return Color("#FF0000")

    @staticmethod
    def green():
        """The color green."""
        return Color("#00FF00")

    @staticmethod
    def blue():
        """The color blue."""
        return Color("#0000FF")

    def __init__(self, color_code):
        """
        Create color from given color code.

        Args:
            color_code(``str``): HEX string specifying the color.
        """
        if not isinstance(color_code, str):
            raise TypeError("The given color code must be of type str.")
        if not color_code[0] == "#" or len(color_code) != 7:
            raise ValueError("The given color code does must match the format"
                             "'#xxxxxx'")
        self.color_code = color_code

    def __add__(self, other):
        """
        Mixes two colors by adding the respective RGB components.
        """
        r_self = int(self.color_code[1:3], 16)
        g_self = int(self.color_code[3:5], 16)
        b_self = int(self.color_code[5:7], 16)
        r_other = int(other.color_code[1:3], 16)
        g_other = int(other.color_code[3:5], 16)
        b_other = int(other.color_code[5:7], 16)
        r = min(r_self + r_other, 255)
        g = min(g_self + g_other, 255)
        b = min(b_self + b_other, 255)
        return Color(f"#{r:02X}{g:02X}{b:02X}")

    def __repr__(self):
        return f"Color({str(self)})"

    def __str__(self):
        return self.color_code
