"""
Tests for the diagrams.procedural.coordinates module.
"""
from diagrams.procedural.coordinates import *
from diagrams.procedural.components import create_rectangle

def test_add_coordinates():
    coord_1 = (100, 200)
    coord_2 = (200, 300)
    coord_3 = add_coordinates(coord_1, coord_2)
    assert coord_3[0] == 300
    assert coord_3[1] == 500

def test_scale_coordinates():
    coord_1 = (200, 300)
    coord_2 = scale_coordinates(coord_1, 0.5)
    assert coord_2[0] == 100
    assert coord_2[1] == 150

def test_anchors():
    rectangle = create_rectangle((100, 100), (100, 100))
    left(rectangle)
    top_left(rectangle)
    top(rectangle)
    top_right(rectangle)
    right(rectangle)
    bottom_right(rectangle)
    bottom(rectangle)
    bottom_left(rectangle)


