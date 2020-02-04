import turtle

# Creates an instance (object) of the turtle

yurtle = turtle.Turtle()

yurtle.speed(0)

yurtle.color("Blue")
"""
# draw a square

for i in range(4):
    yurtle.forward(200)  # move 200
    yurtle.left(90)  # Turn 90 degree
"""
ANGLE = 15
REPEAT = int(360/ANGLE)
SIZE = 200

"""
# draw a donut

for i in range(REPEAT):
    yurtle.circle(SIZE)
    yurtle.left(ANGLE)
"""
# draw a snail shell

for i in range(REPEAT):
    yurtle.circle(SIZE + 4*i)
    yurtle.left(ANGLE)

turtle.done()
