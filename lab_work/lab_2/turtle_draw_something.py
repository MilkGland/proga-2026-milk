import turtle
import math

turtle.speed(1)
turtle.shape('turtle')


def draw_regular_polygon(length, quantity_side):
    """
    Функция, рисующая любой правильный многоугольник
    :param quantity_side: количество углов многоугольника
    :param length: длина стороны многоугольника
    :return: None
    """
    for side in range(quantity_side):
        turtle.forward(length)
        turtle.left(360 / quantity_side)


def draw_circle(radius, angle=360):
    """
    Функция, рисующая окружность, которая представляет из себя многоугольник
    с множеством углов
    :param radius: радиус окружности (многоугольника) в пикселях
    :param angle: количество углов многоугольника. Чем меньше углов, тем меньше
    многоугольник походит на окружность
    :return: None
    """
    circle_length = 2 * math.pi * radius # Определение длины окружности
    length = circle_length / angle # Длина одной стороны многоугольника

    draw_regular_polygon(length, angle)


def draw_nested_square(length, number_of_square, indent=5):
    """
    Функция, рисующая произвольное количество вложеных правильных квадратов
    :param number_of_square: количество квадратов
    :param length: длина стороны квадрата
    :param indent: размер отступа между квадратами
    :return: None
    """
    x = indent # Координата перемещения черепхи по оси X
    y = indent # Координата перемещения черепхи по оси Y

    for square in range(number_of_square):
        draw_regular_polygon(4, length)

        length += indent * 2 # Вычисление длины стороны следующего по велечине квадрата

        turtle.penup()
        turtle.goto(-x, -y) # Перемещение черепахи за пределы нарисованого
                            # квадрата на растояние indent
        x += indent
        y += indent
        turtle.pendown()


def draw_spider(number_of_legs, length):
    """
    Функция, рисующая произвольное количество ног паучку (лучей)
    :param number_of_legs: количество исходящих из центра лучей, которые представляют ноги паука
    :param length: длина ног (лучей)
    :return: None
    """
    for leg in range(number_of_legs):
        turtle.forward(length)
        turtle.stamp()
        turtle.right(360 // number_of_legs) # Определение величины угла между лучами
        turtle.goto(0, 0)


def draw_spiral(radius, angle=360):
    #FIXME

    #TODO:
    # 1. Программа должна учитывать знак функций в четвертях
    # 2. Посмотреть значения переменных через breakpoint
    # и, если нужно, исправить формулы их вычисления
    degree = 300 # Начальная градусная мера
    x0 = 0
    y0 = 50

    circle_length = 2 * math.pi * radius
    length = circle_length / angle

    for side in range(angle):
        x = x0 + radius * math.cos(degree)
        y = y0 + radius * math.sin(degree)

        if degree == 360:
            degree = 0

        turtle.forward(length)
        turtle.left(360 / angle)

        turtle.goto(x, y)

        degree += 1
        radius += ((x-x0)**2 + (y-y0)**2) ** 0.5


draw_spiral(50)
