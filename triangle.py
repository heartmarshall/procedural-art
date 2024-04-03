import turtle


def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.right(120)


def main():
    turtle.speed(100)
    side_length = int(input("Введите длину стороны треугольника: "))
    draw_triangle(side_length)
    turtle.done()
    ex = input()
    exit()


if __name__ == "__main__":
    main()
