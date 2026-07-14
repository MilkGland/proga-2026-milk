import turtle
import random

number_of_turtles = 5
pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]


#TODO: class
def draw_area(height: int, width: int):
    """
    Функция, рисующая область, ограничивающая движение шарика
    :param height: высота области
    :param width: ширина области
    :return: None
    """

    cursor = turtle.Turtle()
    cursor.hideturtle()
    cursor.speed(0)
    cursor.pensize(5)

    cursor.penup()
    cursor.goto(height, width)
    cursor.pendown()

    cursor.goto(-height, width)
    cursor.goto(-height, -width)
    cursor.goto(height, -width)
    cursor.goto(height, width)


def spawn():
    for unit in pool:
        unit.hideturtle()
        unit.penup()
        unit.shapesize(0.5)
        unit.shape('circle')
        unit.speed(50)
        unit.goto(random.randint(-200, 200), random.randint(-200, 200))
        unit.showturtle()


def move(vx: int, vy: int):
    spawn()

    while True:
        for unit in pool:
            x, y = unit.position()

            if y <= -300 or y >= 300:
                vy = -vy

            if x <= -300 or x >= 300:
                vx = -vx

            unit.goto(x + vx, y + vy)


draw_area(300, 300)
move(2, 3)
turtle.forward(12213)
