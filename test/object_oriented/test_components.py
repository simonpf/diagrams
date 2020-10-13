"""
Tests for the diagrams.object_oriented.components module.
"""
from diagrams.object_oriented.components import (Text, Rectangle, Arrow,
                                                 RectangularNode, Color)

def test_text():
    """
    Test create of text component.
    """
    text = Text("hi", (0, 0), Color.red())

def test_rectangle():
    """
    Test creation of rectangle component.
    """
    rectangle = Rectangle((0, 0), (100, 100), Color.red())

def test_arrow():
    """
    Test creation of arrow component.
    """
    arrow = Arrow((0, 0), (100, 100))

def test_node():
    """
    Test creation of node component.
    """
    node = RectangularNode((0, 0), (100, 100), "Node 1")
