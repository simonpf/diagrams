"""
Tests for the diagrams.object_oriented.color module.
"""
import pytest
from diagrams.object_oriented.color import Color

def test_color():
    """
    Test that creating of colors works and that conversion to string
    yiels the HEX color code.
    """
    color = Color("#000000")

    with pytest.raises(TypeError):
        color = Color(0)

    with pytest.raises(ValueError):
        color = Color("abc")

    assert str(color) == "#000000"

def test_mix():
    """
    Test that mixing of colors works.
    """
    color_1 = Color("#FF0000")
    color_2 = Color("#00FF00")
    color_3 = color_1 + color_2
    assert color_3.color_code == "#FFFF00"

    color_4 = color_1 + color_1
    assert color_4.color_code == color_1.color_code
