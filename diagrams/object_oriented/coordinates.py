"""
diagram.object_oriented.coordinates
===================================

Provides the ``Coordinates`` class representing coordinates in a 2D
Cartesian space.
"""
class Coordinates:
    """
    The Coordinates class represents a pair of 2D Cartesian coordinates.

    Attributes:
        self.x(float): The horizontal coordinate.
        self.y(float): The vertical coordinate.
    """
    def __init__(self, x, y):
        """
        Create new coordinate pair.

        Args:
            x(float): The horizontal coordinate.
            y(float): The vertical coordinate.
        """
        self.x = x
        self.y = y

    def __add__(self, other):
        """Component-wise addition of coordinates."""
        return Coordinates(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        """Component-wise multiplication by scalar"""
        return Coordinates(self.x * other, self.y * other)

    def __eq__(self, other):
        """Comparse horizontal and vertical components."""
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        """Prints components."""
        return f"Coordinates({self.x}, {self.y})"
