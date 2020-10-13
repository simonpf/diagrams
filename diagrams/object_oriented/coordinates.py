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

    def __init__(self, *args):
        """
        Create new coordinate pair.

        Args:
            args: A 1- or 2-element list containing either
                - An existing Coordinates object to copy
                - An iterable of length 2 containing the two coordinates.
                - The two coordinates separately.
        """
        if len(args) > 2:
            raise ValueError(
                "The Coordinate constructor takes either one or" " two parameters"
            )
        if len(args) == 1:
            arg = args[0]
            if type(arg) == Coordinates:
                self.x = arg.x
                self.y = arg.y
            else:
                try:
                    coords = list(arg)
                    self.x = float(coords[0])
                    self.y = float(coords[1])
                except:
                    raise ValueError(
                        "Single argument provided to Coordinates"
                        "constructor should be Coordinates object"
                        "or iterable of length 2 with elements"
                        " that can be converted to float."
                    )
        else:
            try:
                x, y = args
                self.x = float(x)
                self.y = float(y)
            except:
                raise ValueError(
                    "The two arguments provided to the Coordinates"
                    "constructor muse be convertible to float."
                )

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
