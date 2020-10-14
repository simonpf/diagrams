from diagrams.object_oriented import Diagram, Circle, Arrow, Coordinates, Color

#
# Create diagram components.
#

circle_1 = Circle((100, 100), 50, Color.green())
circle_2 = Circle((250, 100), 50, Color.blue())
arrow = Arrow(circle_1.right, circle_2.left)

#
# Create diagram and add components.
#

diagram = Diagram(350, 200)
diagram.add(circle_1)
diagram.add(circle_2)
diagram.add(arrow)
diagram.draw()
diagram.show()
