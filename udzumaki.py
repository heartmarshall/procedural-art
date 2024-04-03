import turtle

# Создаем экран и черепаху
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)  # Устанавливаем максимальную скорость

# Рисуем спираль
for i in range(100):
    t.forward(5 + i*2)
    t.right(90)

# Закрытие окна при клике
screen.exitonclick()