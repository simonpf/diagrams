from enum import Enum

class ComponentType(Enum):
    RECTANGLE = 1
    TEXT = 2
    ARROW = 3
    NODE = 4

def create_rectangle(position,
                     dimensions,
                     color="red"):
    return {"type": ComponentType.RECTANGLE,
            "position": position,
            "dimensions": dimensions,
            "color": color}

def create_text(position,
                text,
                color="red"):
    return {"type": ComponentType.TEXT,
            "position": position,
            "text": text,
            "color": color}

def create_arrow(start,
                 end,
                 color="black",
                 head_size=10):
    return {"type": ComponentType.ARROW,
            "start": start,
            "end": end,
            "color": color,
            "head_size": 10}

def create_node(position,
                dimensions,
                text,
                background_color="red",
                text_color="black"):
    return {"type": ComponentType.NODE,
            "position": position,
            "dimensions": dimensions,
            "text": text,
            "background_color": background_color,
            "text_color": text_color}
