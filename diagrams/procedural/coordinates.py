from diagrams.procedural.components import ComponentType

def add_coordinates(coord_1, coord_2):
    """
    Adds two coordinates.

    Args:
        coord_1(``tuple``): 2-tuple ``(x, y)`` containing the horizontal and
            vertical coordinates.
        coord_2(``tuple``): 2-tuple ``(x, y)`` containing the horizontal and
            vertical coordinates.

    Return:
        The component wise sum of the coordinates.
    """
    return (coord_1[0] + coord_2[0], coord_1[1] + coord_2[1])

def scale_coordinates(coord, c):
    """
    Scale coordinates.

    Args:
        coord(``tuple``): The coordinates to scale.
        coord_2(``float``): The scaling factor.

    Return:
        The coordinate scaled by the given scaling factor.
    """
    return (coord[0] * c, coord[1] * c)

def left(component):
    component_type = component["type"]
    if component_type in [ComponentType.RECTANGLE, ComponentType.NODE]:
        position = component["position"]
        dimensions = component["dimensions"]
        return add_coordinates(position, (0, dimensions[1] / 2.0))
    else:
        raise ValueError(f"Component type {component_type} is not a known"
                         "component type.")


def top_left(component):
    component_type = component["type"]
    if component_type in [ComponentType.RECTANGLE, ComponentType.NODE]:
        position = component["position"]
        return position
    else:
        raise ValueError(f"Component type {component_type} is not a known"
                         "component type.")

def top(component):
    component_type = component["type"]
    if component_type in [ComponentType.RECTANGLE, ComponentType.NODE]:
        position = component["position"]
        dimensions = component["dimensions"]
        return add_coordinates(position, (dimensions[0] / 2.0, 0))
    else:
        raise ValueError(f"Component type {component_type} is not a known"
                         "component type.")

def top_right(component):
    component_type = component["type"]
    if component_type in [ComponentType.RECTANGLE, ComponentType.NODE]:
        position = component["position"]
        dimensions = component["dimensions"]
        return add_coordinates(position, (dimensions[0], 0))
    else:
        raise ValueError(f"Component type {component_type} is not a known"
                         "component type.")

def right(component):
    component_type = component["type"]
    if component_type in [ComponentType.RECTANGLE, ComponentType.NODE]:
        position = component["position"]
        dimensions = component["dimensions"]
        return add_coordinates(position, (dimensions[0], dimensions[1] / 2.0))
    else:
        raise ValueError(f"Component type {component_type} is not a known"
                         "component type.")

def bottom_right(component):
    component_type = component["type"]
    if component_type in [ComponentType.RECTANGLE, ComponentType.NODE]:
        position = component["position"]
        dimensions = component["dimensions"]
        return add_coordinates(position, (dimensions[0], dimensions[1]))
    else:
        raise ValueError(f"Component type {component_type} is not a known"
                         "component type.")

def bottom(component):
    component_type = component["type"]
    if component_type in [ComponentType.RECTANGLE, ComponentType.NODE]:
        position = component["position"]
        dimensions = component["dimensions"]
        return add_coordinates(position, (dimensions[0] / 2, dimensions[1]))
    else:
        raise ValueError(f"Component type {component_type} is not a known"
                         "component type.")

def bottom_left(component):
    component_type = component["type"]
    if component_type in [ComponentType.RECTANGLE, ComponentType.NODE]:
        position = component["position"]
        dimensions = component["dimensions"]
        return add_coordinates(position, (0, dimensions[1]))
    else:
        raise ValueError(f"Component type {component_type} is not a known"
                         "component type.")
