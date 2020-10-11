import tkinter
import numpy as np
from diagrams.procedural.coordinates import add_coordinates, scale_coordinates
from diagrams.procedural.components import ComponentType

_ROOT = None
_CANVAS = None

def create_canvas(width,
                  height):
    global _ROOT
    global _CANVAS
    _ROOT = tkinter.Tk()
    _CANVAS = tkinter.Canvas(_ROOT,
                             bg="white",
                             height=height,
                             width=width)

def show():
    _CANVAS.pack()
    _ROOT.mainloop()

def draw(component):
    global _CANVAS
    canvas = _CANVAS
    component_type = component["type"]
    if component_type == ComponentType.RECTANGLE:
        position = component["position"]
        dimensions = component["dimensions"]
        color = component["color"]
        lower_right = add_coordinates(position, dimensions)
        canvas.create_rectangle(position[0],
                                position[1],
                                lower_right[0],
                                lower_right[1],
                                fill=color)
    elif component_type == ComponentType.TEXT:
        position = component["position"]
        text = component["text"]
        color = component["color"]
        canvas.create_text(position[0],
                           position[1],
                           text=text,
                           fill=color)
    elif component_type == ComponentType.ARROW:
        start = component["start"]
        end = component["end"]
        color = component["color"]
        head_size = component["head_size"]
        canvas.create_line(start[0],
                        start[1],
                        end[0],
                        end[1],
                        fill=color)
        angle = np.pi + np.arctan2(end[1] - start[1],
                                end[0] - start[0])
        x_1 = end[0] + head_size * np.cos(angle + np.pi / 6)
        y_1 = end[1] + head_size * np.sin(angle + np.pi / 6)
        x_2 = end[0] + head_size * np.cos(angle - np.pi / 6)
        y_2 = end[1] + head_size * np.sin(angle - np.pi / 6)
        coordinates = [end[0], end[1], x_1, y_1, x_2, y_2]
        canvas.create_polygon(coordinates, outline=color, fill=None)
    elif component_type == ComponentType.NODE:
        position = component["position"]
        dimensions = component["dimensions"]
        background_color = component["background_color"]
        text = component["text"]
        text_color = component["text_color"]
        lower_right = add_coordinates(position, dimensions)
        canvas.create_rectangle(position[0],
                                position[1],
                                lower_right[0],
                                lower_right[1],
                                fill=background_color)
        text_position = add_coordinates(position, scale_coordinates(dimensions, 0.5))
        canvas.create_text(text_position[0],
                           text_position[1],
                           text=text,
                           fill=text_color)
