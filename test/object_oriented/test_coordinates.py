"""
Test for the diagrams.object_oriented.coordinates module.
"""
import pytest
from diagrams.object_oriented.coordinates import Coordinates

def test_constructor():
    """
    Test constructor for different input types and assert that
    invalid constructor arguments are caught.
    """
    Coordinates(1, 2)
    Coordinates((1, 2))
    Coordinates(Coordinates(1, 2))

    with pytest.raises(ValueError):
        Coordinates(1, 2, 3)
    with pytest.raises(ValueError):
        Coordinates(1)
    with pytest.raises(ValueError):
        Coordinates('a', 'b')

def test_arithmetic():
    """
    Test that addition and scaling of coordinates works.
    """
    coord_1 = Coordinates(1, 2)
    coord_2 = Coordinates((1, 2))
    coord_3 = coord_1 + coord_2
    coord_4 = coord_1 * 2.0
    assert coord_3 == coord_4
