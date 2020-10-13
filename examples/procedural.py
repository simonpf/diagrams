from diagrams.procedural import (create_canvas,
                                 draw,
                                 show,
                                 create_rectangular_node,
                                 create_arrow,
                                 left,
                                 right)

#
# Create diagram components.
#

node_1 = create_rectangular_node((50, 50),
                                 (100, 100),
                                 "node 1")
node_2 = create_rectangular_node((300, 50),
                                 (100, 100),
                                 "node 1",
                                 "blue")
arrow = create_arrow(right(node_1),
                     left(node_2))

#
# Create canvas and add components.
#

create_canvas(450, 200)
draw(node_1)
draw(node_2)
draw(arrow)
show()
