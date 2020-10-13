from diagrams.object_oriented import Diagram, RectangularNode, Arrow, Coordinates, Color

#
# Create diagram components.
#

node_1 = RectangularNode((50, 50),
                         (100, 100),
                         "Node 1",
                         Color.red())
node_2 = RectangularNode((200, 50),
                         (100, 100),
                         "Node 2",
                         Color.blue())
arrow = Arrow(node_1.right, node_2.left)

#
# Create diagram and add components.
#

diagram = Diagram(350, 200)
diagram.add(node_1)
diagram.add(node_2)
diagram.add(arrow)
diagram.draw()
diagram.show()
