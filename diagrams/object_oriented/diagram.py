"""
diagrams.object_oriented.diagram
================================

Provides the diagram class, which acts as a container for diagram components
and draws them onto an canvas.
"""
from abc import ABC, abstractmethod
import tkinter
from diagrams.object_oriented.coordinates import Coordinates

###############################################################################
# DiagramComponent ABC
###############################################################################

class DiagramComponent(ABC):
    """
    The basic interface for components that can be added to and drawn as
    parts of a diagram.
    """
    @abstractmethod
    def draw(self, canvas, offset=Coordinates(0, 0)):
        """
        This method is called by the main diagram object or a another component
        that contains this one. When called, it should draw the component on the
        given canvas relative to the given offset.

        Params:
            canvas: ``tkinter.Canvas`` object onto which to draw the component.
            offset: Offset to calculate the absolute position at which to
                draw the component.
        """

###############################################################################
# Diagram class
###############################################################################

class Diagram:
    """
    The diagram class contains diagram components and draws them
    onto a canvas.
    """
    def __init__(self, width, height):
        """
        Create diagram.

        Args:
            width(int): The width of the diagram canvas in pixels.
            height(int): The height of the diagram canvas in pixels.
        """
        self.width = width
        self.height = height
        self.components = []

    def add(self, component):
        """Add component to diagram. """
        if not isinstance(component, DiagramComponent):
            raise TypeError("Given component does not implement the"
                            " DiagramComponent interface.")
        self.components.append(component)

    def draw(self):
        """
        Draws diagram components on HTML5 canvas.

        Return:
            Canvas with all diagram components drawn onto.
        """
        root = tkinter.Tk()
        canvas = tkinter.Canvas(root,
                                bg="white",
                                height=self.height,
                                width=self.width)
        for component in self.components:
            component.draw(canvas)

        canvas.pack()
        root.mainloop()
