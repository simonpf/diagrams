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
    def Black():
        """The color black."""
        return Color("#000000")

    @staticmethod
    def Red():
        """The color red."""
        return Color("#FF0000")

    @staticmethod
    def Green():
        """The color green."""
        return Color("#00FF00")

    @staticmethod
    def Blue():
        """The color blue."""
        return Color("#0000FF")

    def __init__(self, color_code):
        """ Create color from given color code. """
        self.color_code = color_code

    def __str__(self):
        return self.color_code
