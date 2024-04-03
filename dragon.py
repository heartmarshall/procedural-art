import turtle

def dragon_curve(turtle, order, length, direction):
    if order == 0:
        turtle.forward(length)
        return
    else:
        turtle.left(45 * direction)
        dragon_curve(turtle, order - 1, length / (2 ** 0.5), 1)
        turtle.right(90 * direction)
        dragon_curve(turtle, order - 1, length / (2 ** 0.5), -1)
        turtle.left(45 * direction)


# Создаем экран и черепаху
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")
t = turtle.Turtle()
t.goto(0,0)

t.speed(0)  # Устанавливаем максимальную скорость

# Перемещаем черепаху в начальную позицию
t.penup()
t.goto(-300, 0)
t.pendown()

# Рисуем фрактальный дракон
dragon_curve(t, 12, 600, 1)

# Закрытие окна при клике
screen.exitonclick()