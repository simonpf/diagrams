"""
diagrams.procedural.components
==============================

This module provides functions to create diagram components.
"""
from enum import Enum

class ComponentType(Enum):
    """
    Enum class representing the component type.
    """
    RECTANGLE = 1
    TEXT = 2
    ARROW = 3
    RECTANGULAR_NODE = 4
    CIRCULAR_NODE = 5

def create_rectangle(position,
                     dimensions,
                     color="red"):
    """
    Create a filled rectangle.

        Args:
            position(``tuple``): The position of the upper left corner of the
                rectangle.
            dimensions(``tuple``): Tuple containing the horizontal and
                vertical extent of the rectangle.
            color(``str``): The fill color for the rectangle given as
                ``tkinter``-compatible color string.

        Return:
            ``dict`` representing the diagram component.
    """
    return {"type": ComponentType.RECTANGLE,
            "position": position,
            "dimensions": dimensions,
            "color": color}

def create_text(position,
                text,
                color="red"):
    """
    Create text component.

        Args:
            position(``tuple``): The position of the upper left corner of the
                rectangle.
            text(``str``): The text to draw.
            color(``str``): The text color given as ``tkinter``-compatible
                color string.

        Return:
            ``dict`` representing the diagram component.

    """
    return {"type": ComponentType.TEXT,
            "position": position,
            "text": text,
            "color": color}

def create_arrow(start,
                 end,
                 color="black",
                 head_size=10):
    """
    Draw arrow between two positions.

        Args:
            start(``tuple``): The start position of the arrow.
            end(``tuple``): Position of the arrow tip.
            color(``str``): The arrow color given as ``tkinter``-compatible
                            color string.

        Return:
            ``dict`` representing the diagram component.

    """
    return {"type": ComponentType.ARROW,
            "start": start,
            "end": end,
            "color": color,
            "head_size": 10}

def create_rectangular_node(position,
                            dimensions,
                            text,
                            background_color="red",
                            text_color="black"):
    """
    A rectangular diagram node is a rectangular shape with a centered text.

        Args:
            position(``tuple``): Position of the upper left corner of the rectangle.
            dimensions(``tuple``): Horizontal and vertical extent of the rectangle.
            text(``str``): The text to render inside the node.
            background_color(``str``): The color of the rectangle given as
                ``tkinter``-compatible color.
            text_color(``str``): The color of the text given as
                ``tkinter``-compatible color.

        Return:
            ``dict`` representing the diagram component.
    """
    return {"type": ComponentType.RECTANGULAR_NODE,
            "position": position,
            "dimensions": dimensions,
            "text": text,
            "background_color": background_color,
            "text_color": text_color}
