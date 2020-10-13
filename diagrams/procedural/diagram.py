"""
diagrams.procedural.diagram
==============================

This module provides functions related to the drawing of diagram components.
"""
import tkinter
import numpy as np
from diagrams.procedural.coordinates import add_coordinates, scale_coordinates
from diagrams.procedural.components import ComponentType

_ROOT = None
_CANVAS = None


def create_canvas(width, height):
    """
    Create a global canvas object.

    Args:
        width(int): The width in pixels.
        height(int): The height in pixels.
    """
    global _ROOT
    global _CANVAS
    _ROOT = tkinter.Tk()
    _CANVAS = tkinter.Canvas(_ROOT, bg="white", height=height, width=width)


def show():
    """
    Displays the canvas.
    """
    _CANVAS.pack()
    _ROOT.mainloop()

def draw_rectangle(component):
    """
    Draw rectangle on canvas.

    Args:
        component(``dict``): The rectangle created using the create_rectangle
            function.
    """
    global _CANVAS
    canvas = _CANVAS
    position = component["position"]
    dimensions = component["dimensions"]
    color = component["color"]
    lower_right = add_coordinates(position, dimensions)
    canvas.create_rectangle(
        position[0], position[1], lower_right[0], lower_right[1], fill=color
    )

def draw_circle(component):
    """
    Draw circle on canvas.

    Args:
        component(``dict``): The rectangle created using the create_circle
            function.
    """
    global _CANVAS
    canvas = _CANVAS
    position = component["position"]
    radius = component["radius"]
    color = component["color"]
    x_1 = position[0] - radius
    y_1 = position[1] - radius
    x_2 = position[0] + radius
    y_2 = position[1] + radius
    canvas.create_oval(x_1, y_1, x_2, y_2, fill=color)

def draw_text(component):
    """
    Draw text on canvas.

    Args:
        component(``dict``): The text created using the create_text
            function.
    """
    global _CANVAS
    canvas = _CANVAS
    position = component["position"]
    text = component["text"]
    color = component["color"]
    canvas.create_text(position[0], position[1], text=text, fill=color)

def draw_arrow(component):
    """
    Draw arrow on canvas.

    Args:
        component(``dict``): The arrow created using the create_arrow
            function.
    """
    global _CANVAS
    canvas = _CANVAS
    start = component["start"]
    end = component["end"]
    color = component["color"]
    head_size = component["head_size"]
    canvas.create_line(start[0], start[1], end[0], end[1], fill=color)
    angle = np.pi + np.arctan2(end[1] - start[1], end[0] - start[0])
    x_1 = end[0] + head_size * np.cos(angle + np.pi / 6)
    y_1 = end[1] + head_size * np.sin(angle + np.pi / 6)
    x_2 = end[0] + head_size * np.cos(angle - np.pi / 6)
    y_2 = end[1] + head_size * np.sin(angle - np.pi / 6)
    coordinates = [end[0], end[1], x_1, y_1, x_2, y_2]
    canvas.create_polygon(coordinates, outline=color, fill=None)

def draw_rectangular_node(component):
    """
    Draw rectangular node on canvas.

    Args:
        component(``dict``): The rectangular node created using the
            create_rectangular_node function.
    """
    global _CANVAS
    canvas = _CANVAS
    position = component["position"]
    dimensions = component["dimensions"]
    background_color = component["background_color"]
    text = component["text"]
    text_color = component["text_color"]
    lower_right = add_coordinates(position, dimensions)
    canvas.create_rectangle(
        position[0],
        position[1],
        lower_right[0],
        lower_right[1],
        fill=background_color,
    )
    text_position = add_coordinates(position, scale_coordinates(dimensions, 0.5))
    canvas.create_text(
        text_position[0], text_position[1], text=text, fill=text_color
    )

def draw(component):
    """
    Draw component on the current canvas.

    Args:
        component(``dict``): A dictionary representing the component
            to be drawn.
    """
    component_type = component["type"]
    if component_type == ComponentType.RECTANGLE:
        draw_rectangle(component)
    elif component_type == ComponentType.CIRCLE:
        draw_circle(component)
    elif component_type == ComponentType.TEXT:
        draw_text(component)
    elif component_type == ComponentType.ARROW:
        draw_arrow(component)
    elif component_type == ComponentType.RECTANGULAR_NODE:
        draw_rectangular_node(component)
