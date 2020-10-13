"""
Test for the diagrams.procedural.diagram module.
"""

from diagrams.procedural.diagram import create_canvas, draw, show


def test_diagram():
    create_canvas(200, 200)
    show()
