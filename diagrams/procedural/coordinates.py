"""
diagrams.procedural.coordinates
===============================

This module provides functions for manipulating 2D coordinates represented
as length-2 tuples.
"""
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
    """
    Compute the left anchor of a component.

    Args:
        component(``dict``): Dictionary representing a diagram component
            created using a suitable ``create_<component_name>`` function.

    Return:
        Length-2 ``tuple`` holding the coordinates of the anchor to the
        left of the component.
    """
    component_type = component["type"]
    if component_type in [ComponentType.RECTANGLE, ComponentType.RECTANGULAR_NODE]:
        position = component["position"]
        dimensions = component["dimensions"]
        return add_coordinates(position, (0, dimensions[1] / 2.0))
    else:
        raise ValueError(
            f"Component type {component_type} is not a known" "component type."
        )


def top_left(component):
    """
    Compute the top-left anchor of a component.

    Args:
        component(``dict``): Dictionary representing a diagram component
            created using a suitable ``create_<component_name>`` function.

    Return:
        Length-2 ``tuple`` holding the coordinates of the anchor to the
        top-left of the component.
    """
    component_type = component["type"]
    if component_type in [ComponentType.RECTANGLE, ComponentType.RECTANGULAR_NODE]:
        position = component["position"]
        return position
    else:
        raise ValueError(
            f"Component type {component_type} is not a known" "component type."
        )


def top(component):
    """
    Compute the top anchor of a component.

    Args:
        component(``dict``): Dictionary representing a diagram component
            created using a suitable ``create_<component_name>`` function.

    Return:
        Length-2 ``tuple`` holding the coordinates of the anchor to the
        top of the component.
    """
    component_type = component["type"]
    if component_type in [ComponentType.RECTANGLE, ComponentType.RECTANGULAR_NODE]:
        position = component["position"]
        dimensions = component["dimensions"]
        return add_coordinates(position, (dimensions[0] / 2.0, 0))
    else:
        raise ValueError(
            f"Component type {component_type} is not a known" "component type."
        )


def top_right(component):
    """
    Compute the top-right anchor of a component.

    Args:
        component(``dict``): Dictionary representing a diagram component
            created using a suitable ``create_<component_name>`` function.

    Return:
        Length-2 ``tuple`` holding the coordinates of the anchor to the
        top-right of the component.
    """
    component_type = component["type"]
    if component_type in [ComponentType.RECTANGLE, ComponentType.RECTANGULAR_NODE]:
        position = component["position"]
        dimensions = component["dimensions"]
        return add_coordinates(position, (dimensions[0], 0))
    else:
        raise ValueError(
            f"Component type {component_type} is not a known" "component type."
        )


def right(component):
    """
    Compute the right anchor of a component.

    Args:
        component(``dict``): Dictionary representing a diagram component
            created using a suitable ``create_<component_name>`` function.

    Return:
        Length-2 ``tuple`` holding the coordinates of the anchor to the
        right of the component.
    """
    component_type = component["type"]
    if component_type in [ComponentType.RECTANGLE, ComponentType.RECTANGULAR_NODE]:
        position = component["position"]
        dimensions = component["dimensions"]
        return add_coordinates(position, (dimensions[0], dimensions[1] / 2.0))
    else:
        raise ValueError(
            f"Component type {component_type} is not a known" "component type."
        )


def bottom_right(component):
    """
    Compute the bottom-right anchor of a component.

    Args:
        component(``dict``): Dictionary representing a diagram component
            created using a suitable ``create_<component_name>`` function.

    Return:
        Length-2 ``tuple`` holding the coordinates of the anchor to the
        bottom-right of the component.
    """
    component_type = component["type"]
    if component_type in [ComponentType.RECTANGLE, ComponentType.RECTANGULAR_NODE]:
        position = component["position"]
        dimensions = component["dimensions"]
        return add_coordinates(position, (dimensions[0], dimensions[1]))
    else:
        raise ValueError(
            f"Component type {component_type} is not a known" "component type."
        )


def bottom(component):
    """
    Compute the bottom anchor of a component.

    Args:
        component(``dict``): Dictionary representing a diagram component
            created using a suitable ``create_<component_name>`` function.

    Return:
        Length-2 ``tuple`` holding the coordinates of the anchor to the
        bottom of the component.
    """
    component_type = component["type"]
    if component_type in [ComponentType.RECTANGLE, ComponentType.RECTANGULAR_NODE]:
        position = component["position"]
        dimensions = component["dimensions"]
        return add_coordinates(position, (dimensions[0] / 2, dimensions[1]))
    else:
        raise ValueError(
            f"Component type {component_type} is not a known" "component type."
        )


def bottom_left(component):
    """
    Compute the bottom-left anchor of a component.

    Args:
        component(``dict``): Dictionary representing a diagram component
            created using a suitable ``create_<component_name>`` function.

    Return:
        Length-2 ``tuple`` holding the coordinates of the anchor to the
        bottom-left of the component.
    """
    component_type = component["type"]
    if component_type in [ComponentType.RECTANGLE, ComponentType.RECTANGULAR_NODE]:
        position = component["position"]
        dimensions = component["dimensions"]
        return add_coordinates(position, (0, dimensions[1]))
    else:
        raise ValueError(
            f"Component type {component_type} is not a known" "component type."
        )
