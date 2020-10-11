import tkinter

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
