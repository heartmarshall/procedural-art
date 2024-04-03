import turtle
from helper import drawSquare, drawDiamond

turtle.speed(0)
turtle.hideturtle()  # hides the turtle
turtle.tracer(15,
              0)  # sets the turtle to draw almost instantaneously. At (0,0) crashes on my PC :( Not sure what's up with that. Will update with more info

hasDrawn = False


# Defines how to draw a primrose - 4 diamonds at different angles
def drawPrimrose(x, y, size, colour):
    drawDiamond(turtle, x, y, size, colour, angle=0)
    drawDiamond(turtle, x, y, size, colour, angle=90)
    drawDiamond(turtle, x, y, size, colour, angle=180)
    drawDiamond(turtle, x, y, size, colour, angle=270)


gridSize = 45
gridColour1 = "#59b983"
gridColour2 = "#a4d443"


def draw():
    global hasDrawn
    if not hasDrawn:

        # Drawing background
        drawSquare(turtle, -7 * gridSize, -7 * gridSize, 15 * gridSize, gridColour1)

        # Draws the light green squares in a grid
        for x in range(-7, 8, 2):
            for y in range(-7, 8, 2):
                drawSquare(turtle, gridSize * x, gridSize * y, gridSize, gridColour2)

        # Draws more light green squares in the same pattern to form a checkerboard grid
        for x in range(-6, 8, 2):
            for y in range(-6, 8, 2):
                drawSquare(turtle, gridSize * x, gridSize * y, gridSize, gridColour2)

        # Draws Primroses
        primroseSize = 6
        primroseColour1 = "white"
        primroseColour2 = "#c81d97"
        pattern = [primroseColour1, primroseColour2, primroseColour2, primroseColour1, primroseColour2, primroseColour1,
                   primroseColour1, primroseColour2]

        for y in range(-6, 8, 1):
            for x in range(-6, 8, 1):
                drawPrimrose(gridSize * x, gridSize * y, primroseSize, pattern[(x + y - 1) % 8])

        hasDrawn = True

    else:
        turtle.penup()
        turtle.goto(0, 0)


while True:

    try:
        draw()
    except turtle.Terminator:
        print("Goodbye")
        break
