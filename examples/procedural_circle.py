from diagrams.procedural import (create_canvas,
                                 draw,
                                 show,
                                 create_circle,
                                 create_arrow,
                                 left,
                                 right)

#
# Create diagram components.
#

circle_1 = create_circle((100, 100), 50, "green")
circle_2 = create_circle((250, 100), 50, "blue")
arrow = create_arrow(right(circle_1), left(circle_2))

#
# Create canvas and add components.
#

create_canvas(350, 200)
draw(circle_1)
draw(circle_2)
draw(arrow)
show()
