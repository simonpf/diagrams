"""
Tests for the diagrams.procedural.components module.
"""
from diagrams.procedural.components import *


def test_rectangle():
    rectangle = create_rectangle((100, 100), (100, 100), "red")
    assert rectangle["type"] == ComponentType.RECTANGLE


def test_text():
    text = create_text((100, 100), "text", "black")
    assert text["type"] == ComponentType.TEXT


def test_arrow():
    arrow = create_arrow((100, 100), (200, 200), "black")
    assert arrow["type"] == ComponentType.ARROW


def test_rectangular_node():
    node = create_rectangular_node((100, 100), (200, 200), "Node 1", "red", "black")
    assert node["type"] == ComponentType.RECTANGULAR_NODE
