import turtle


def draw_rectangle(t: turtle.Turtle, width, height, color):
    t.up()
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()


turtle.colormode(255)
t = turtle.Turtle()

turtle.setworldcoordinates(-10, -10, 270, 270)
r = 0
g = 100
b = 100
t.speed('fastest')
t.pencolor('white')
start_pos = (0, 0)
row = 1
for i in range(0, 255, 15):
    print(i)
    for j in range(i, i+17):
        r = j
        draw_rectangle(t, 10, 10, (r, g, b))
        t.forward(10)
    t.goto(0, row*10)
    row += 1
i = int(input("Enter"))