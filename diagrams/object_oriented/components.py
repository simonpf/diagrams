"""
diagram.object_oriented.components
==================================

Provides the component classes that can be used to construct
diagrams.
"""
from abc import ABC, abstractproperty
import numpy as np

from diagrams.object_oriented.color import Color
from diagrams.object_oriented.coordinates import Coordinates
from diagrams.object_oriented.diagram import DiagramComponent

###############################################################################
# Connectable
###############################################################################


class Connectable(ABC):
    """
    Abstract base class for object that can be connected with other object using
    arrows.
    """

    @abstractproperty
    def left(self):
        """
        ``Coordinates`` object representing the position located left of the
        diagram component.
        """

    @abstractproperty
    def top_left(self):
        """
        ``Coordinates`` object representing the position located upper left of
        the diagram component.
        """

    @abstractproperty
    def top(self):
        """
        ``Coordinates`` object representing the position located above of the
        diagram component.
        """

    @abstractproperty
    def top_right(self):
        """
        ``Coordinates`` object representing the position located to the upper
        right of the diagram component.
        """

    @abstractproperty
    def right(self):
        """
        ``Coordinates`` object representing the position located to the
        right of the diagram component.
        """

    @abstractproperty
    def bottom_right(self):
        """
        ``Coordinates`` object representing the position located at the
        bottom right of the diagram component.
        """

    @abstractproperty
    def bottom(self):
        """
        ``Coordinates`` object representing the position located below the
        diagram component.
        """

    @abstractproperty
    def bottom_left(self):
        """
        ``Coordinates`` object representing the position located at the
        bottom left of the diagram component.
        """


###############################################################################
# ComponentBase
###############################################################################


class ComponentBase(DiagramComponent):
    """
    Base class for diagram components.

    Attributes:
        position(Coordinates): The component's position represented as
            as Coordinates object.
        color(Color): The components color represented as Color
            as Color object.
    """

    def __init__(self, position, color):
        """
        Create diagram component.

        Args:
            position(Coordinates): The position of the object
            color(Color): The color of the object.
        """
        self.position = position
        self.color = color

    def translate(self, delta):
        """
        Translate object by given direction.

        Args:
            delta(Coordinates): Coordinates object representing the direction
                step by which to translate the object.
        """
        self.position = self.position + delta

    def set_color(self, new_color):
        """
        Set color of component.

        Args:
            new_color(Color): The new color of the component.
        """
        self.color = new_color


###############################################################################
# Text
###############################################################################


class Text(ComponentBase):
    """
    A colored text in a diagram.
    """

    def __init__(self, text, position, color=Color.black()):
        """
        Create text object.

        Args:
            text(str): The text
            position(Coordinates): Position around which to center the text.
            color(Color): The fill color to use for the text.
        """
        super().__init__(Coordinates(position), color)
        self.text = text

    def draw(self, canvas, offset=Coordinates(0, 0)):
        """
        Draw text on canvas.

        Uses the ``ipycanvas`` API to draw  filled text on the given HTML5 canvas
        object.

        Args:
            canvas(ipycanvas.Canvas): Canvas to draw the rectangle on.
        """
        position = self.position + offset
        canvas.create_text(position.x, position.y, text=self.text, fill=str(self.color))


###############################################################################
# Arrow
###############################################################################


class Arrow(ComponentBase):
    """
    An arrow in a diagram.

    Attributes:
        end(Coorinates): End position of the arrow.
    """

    def __init__(self, start, end, color=Color.black(), head_size=10):
        """
        Create arrow.

        Args:
            start(Coordinates): Start position of arrow.
            end(Coordinates): End position of arrow.
            color(Color): Arrow color.
            head_size(int): Size of arrow head in pixels.
        """
        super().__init__(Coordinates(start), color)
        self.end = Coordinates(end)
        self.head_size = head_size

    def draw(self, canvas, offset=Coordinates(0, 0)):
        """
        Draw arrow on canvas.

        Uses the ``ipycanvas`` API to draw  arrow text on the given HTML5 canvas
        object.

        Args:
            canvas(ipycanvas.Canvas): Canvas to draw the rectangle on.
        """
        position = self.position + offset
        end = self.end + offset

        canvas.create_line(position.x, position.y, end.x, end.y, fill=str(self.color))

        angle = np.pi + np.arctan2(
            self.end.y - self.position.y, self.end.x - self.position.x
        )
        x_1 = self.end.x + self.head_size * np.cos(angle + np.pi / 6)
        y_1 = self.end.y + self.head_size * np.sin(angle + np.pi / 6)
        x_2 = self.end.x + self.head_size * np.cos(angle - np.pi / 6)
        y_2 = self.end.y + self.head_size * np.sin(angle - np.pi / 6)
        coordinates = [end.x, end.y, x_1, y_1, x_2, y_2]
        canvas.create_polygon(coordinates, outline=str(self.color), fill=None)


###############################################################################
# Rectangle
###############################################################################


class Rectangle(ComponentBase, Connectable):
    """
    A filled rectangle.

    Attributes:
        dimensions(Coordinates): Coordinates object holding the width
            and height of the rectangle.
    """

    def __init__(self, position, dimensions, color=Color.red()):
        """
        Create rectangle.

            Args:
                position(Coordinates): The position of the upper left corner of the
                    rectangle.
                dimensions(Coordinates): Coordinates object holding the horizontal
                    and vertical extent of the rectangle
                color(Color): The color with which to fill rectangle
        """
        super().__init__(position, color)
        self.dimensions = dimensions

    def draw(self, canvas, offset=Coordinates(0, 0)):
        """
        Draw rectangle on canvas.

        Uses the ``ipycanvas`` API to draw a filled rectangle on the given HTML5 canvas
        object.

        Args:
            canvas(ipycanvas.Canvas): Canvas to draw the rectangle on.
        """
        position = self.position + offset
        lower_right = position + self.dimensions
        canvas.create_rectangle(
            position.x, position.y, lower_right.x, lower_right.y, fill=str(self.color)
        )

    @property
    def left(self):
        """
        ``Coordinates`` object representing the position located left of the
        diagram component.
        """
        return self.position + Coordinates(0, self.dimensions.y / 2)

    @property
    def top_left(self):
        """
        ``Coordinates`` object representing the position located upper left of
        the diagram component.
        """
        return self.position

    @property
    def top(self):
        """
        ``Coordinates`` object representing the position located above of the
        diagram component.
        """
        return self.position + Coordinates(self.dimensions.x / 2, 0)

    @property
    def top_right(self):
        """
        ``Coordinates`` object representing the position located to the upper
        right of the diagram component.
        """
        return self.position + Coordinates(self.dimensions.x, 0)

    @property
    def right(self):
        """
        ``Coordinates`` object representing the position located to the
        right of the diagram component.
        """
        return self.position + Coordinates(self.dimensions.x, self.dimensions.y / 2)

    @property
    def bottom_right(self):
        """
        ``Coordinates`` object representing the position located at the
        bottom right of the diagram component.
        """
        return self.position + Coordinates(self.dimensions.x, self.dimensions.y)

    @property
    def bottom(self):
        """
        ``Coordinates`` object representing the position located below the
        diagram component.
        """
        return self.position + Coordinates(self.dimensions.x / 2, self.dimensions.y)

    @property
    def bottom_left(self):
        """
        ``Coordinates`` object representing the position located at the
        bottom left of the diagram component.
        """
        return self.position + Coordinates(0, self.dimensions.y)


###############################################################################
# RectangularNode
###############################################################################


class RectangularNode(ComponentBase, Connectable):
    """
    A node is a rectangular shape with a centered text.

    Attributes:
        text(Text): The text component of the node.
    """

    def __init__(self, position, dimensions, text, color=Color.red()):
        """
        Create new node.

        Args:
            position(Coordinates): The position of the node.
            dimensions(Coordinates): The dimensions of the node.
            text(str): The text to print in the node.
            color(Color): Color of node background.
        """
        position = Coordinates(position)
        dimensions = Coordinates(dimensions)
        super().__init__(position, color)
        self.rectangle = Rectangle(Coordinates(0, 0), dimensions)
        self.text = Text(text, dimensions * 0.5, color=Color.black())

    def draw(self, canvas, offset=Coordinates(0, 0)):
        """
        Draw node on canvas.

        Uses the ``ipycanvas`` API to node on the given HTML5 canvas
        object.

        Args:
            canvas(ipycanvas.Canvas): Canvas to draw the rectangle on.
        """
        # Need to update position and color of rectangle and
        # position of text to make sure they are consistent with
        # the attributes inherited from the DiagramComponent class.
        # THIS IS A DESIGN FLAW.
        absolute_position = offset + self.position
        self.rectangle.draw(canvas, offset=absolute_position)
        self.text.draw(canvas, offset=absolute_position)

    @property
    def left(self):
        """
        ``Coordinates`` object representing the position located left of the
        diagram component.
        """
        return self.rectangle.left + self.position

    @property
    def top_left(self):
        """
        ``Coordinates`` object representing the position located upper left of
        the diagram component.
        """
        return self.rectangle.top_left + self.position

    @property
    def top(self):
        """
        ``Coordinates`` object representing the position located above of the
        diagram component.
        """
        return self.rectangle.top + self.position

    @property
    def top_right(self):
        """
        ``Coordinates`` object representing the position located to the upper
        right of the diagram component.
        """
        return self.rectangle.top_right + self.position

    @property
    def right(self):
        """
        ``Coordinates`` object representing the position located to the
        right of the diagram component.
        """
        return self.rectangle.right + self.position

    @property
    def bottom_right(self):
        """
        ``Coordinates`` object representing the position located at the
        bottom right of the diagram component.
        """
        return self.rectangle.bottom_right + self.position

    @property
    def bottom(self):
        """
        ``Coordinates`` object representing the position located below the
        diagram component.
        """
        return self.rectangle.bottom + self.position

    @property
    def bottom_left(self):
        """
        ``Coordinates`` object representing the position located at the
        bottom left of the diagram component.
        """
        return self.rectangle.bottom_left + self.position
