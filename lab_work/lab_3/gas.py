import turtle
import random
from material_point import draw_area

number_of_turtles = 5
pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]


def is_in_area(x, y):
    pass


def move():
    for unit in pool:
        unit.hideturtle()
        unit.penup()
        unit.speed(0)
        unit.goto(random.randint(-200, 200), random.randint(-200, 200))
        unit.showturtle()

    while True:
        for unit in pool:
            x, y = unit.position()
            is_in_area(x, y)
            unit.forward(2)


if __name__ == '__main__':
    draw_area(300, 300)
    move()
