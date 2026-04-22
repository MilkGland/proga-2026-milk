import turtle
import math

turtle.speed(1)
turtle.shape('turtle')


def draw_regular_polygon(quantity_side, length):
    """
    Функция, рисующая любой правильный многоугольник
    :param quantity_side: количество углов многоугольника
    :param length: длина стороны многоугольника
    :return: None
    """
    for side in range(quantity_side):
        turtle.forward(length)
        turtle.left(360 // quantity_side)


def draw_circle(length):
    """
    Функция, рисующая окружность, которая представляет из себя многоугольник с множеством углов
    :param length: длина окружности
    :return: None
    """
    for polygon in range(360 // 5): # Определение длины окружности с учетом фиксированого параметра
        turtle.forward(length)
        turtle.right(5) # Фиксированый параметр, влияющий на количество углов в данном многоугольнике
                        # Чем он больше, тем меньше углов в многоугольнике
                        # Чем он меньше, тем медленнее черепаха рисует многоугольник


def draw_nested_square(number_of_square, length, indent=5):
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
        length += indent * 2

        turtle.penup()
        turtle.goto(-x, -y)
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


def draw_spiral(n, length):
    #FIXME
    # 1. угол в начальный момент времени - 85 градусов, а формула вычисления расчитана на 5 градусов
    # 2. параметр n_ не предполагает, что градусная мера угла будет и уменьшаться и увеличиваться
    # 3. поменять положение черепахи в начальный момент рисования окружности,
    # чтобы она начинала рисовать ее с точки 0 градусов
    # и двигалась по положительному направлению оси

    #r = 68
    #n_ = n

    #turtle.penup()
    #turtle.goto(0, 68)
    #turtle.pendown()

    for polygon in range(360 // n):
        turtle.forward(length)
        turtle.right(n)

        #x = (math.cos(n_) + 1) * length
        #y = r * math.sin(n_)
        #turtle.goto(x, r+y)
        #r += y
        #n_ += n



draw_spiral(5, 5)
