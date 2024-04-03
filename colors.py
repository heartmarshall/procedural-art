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
turtle.tracer(5, 0)
turtle.setworldcoordinates(-10, -10, 270, 270)
r = 0
g = 50
b = 100
t.speed('fastest')
t.pencolor('white')
start_pos = (0, 0)
row = 1
for i in range(0, 255, 17):
    print(i)
    for j in range(i, i+15):
        r = j
        draw_rectangle(t, 10, 10, (r % 256, g, b))
        t.forward(10)
    t.goto(0, row*10)
    row += 1
i = int(input("Enter"))