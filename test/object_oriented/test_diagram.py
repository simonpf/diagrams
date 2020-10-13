"""
Tests for the diagrams.object_oriented.diagram module.
"""
from diagrams.object_oriented.color import Color
from diagrams.object_oriented.components import RectangularNode, Arrow
from diagrams.object_oriented.diagram import Diagram

def test_diagram():
    """
    Creates a diagram with specific width and height and asserts that attributes
    are set correctly. Adds component to diagram and asserts that it is added to
    the components attribute.
    """
    diagram = Diagram(350, 200)
    node_1 = RectangularNode((50, 50),
                             (100, 100),
                             "Node 1")
    node_2 = RectangularNode((200, 50),
                             (100, 100),
                             "Node 2")
    node_2.rectangle.set_color(Color.blue())
    arrow = Arrow(node_1.right, node_2.left)

    diagram.add(node_1)
    diagram.add(node_2)
    diagram.add(arrow)
    diagram.draw()

    assert diagram.width == 350
    assert diagram.height == 200
    assert len(diagram.components) == 3
