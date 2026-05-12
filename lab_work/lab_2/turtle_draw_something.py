import turtle
import math

turtle.speed(1)
turtle.shape('turtle')


def draw_regular_polygon(quantity_side, side_length):
    """
    Функция, рисующая любой правильный многоугольник
    :param quantity_side: количество углов многоугольника
    :param side_length: длина стороны многоугольника
    :return: None
    """
    for side in range(quantity_side):
        turtle.forward(side_length)
        turtle.left(360 / quantity_side) # Определение величины угла
                                         # правильного многоугольника


def draw_circle(radius, angle=360):
    """
    Функция, рисующая окружность, которая представляет из себя
    многоугольник с множеством углов
    :param radius: радиус окружности (многоугольника) в пикселях
    :param angle: количество углов многоугольника. Чем меньше углов,
                  тем меньше многоугольник походит на окружность
    :return: None
    """
    circle_length = 2 * math.pi * radius # Определение длины окружности
    length = circle_length / angle # Длина одной стороны многоугольника

    draw_regular_polygon(angle, length)


def draw_nested_square(number_of_square, length, indent=5):
    """
    Функция, рисующая произвольное количество вложеных квадратов
    :param number_of_square: количество квадратов
    :param length: длина стороны квадрата
    :param indent: размер отступа между квадратами
                   (по коорданитам x, y)
    :return: None
    """
    x = indent # Координата перемещения черепхи по оси X
    y = indent # Координата перемещения черепхи по оси Y

    for square in range(number_of_square):
        draw_regular_polygon(4, length)

        length += indent * 2 # Вычисление длины стороны
                             # следующего по величине квадрата

        turtle.penup()
        turtle.goto(-x, -y) # Перемещение черепахи за пределы нарисо
                            # ваного квадрата на расстояние indent
        x += indent
        y += indent
        turtle.pendown()


def draw_spider(number_of_legs, length):
    """
    Функция, рисующая произвольное количество ног (лучей) паучка
    :param number_of_legs: количество исходящих из центра лучей,
                           которые представляют ноги паука
    :param length: длина ног (лучей)
    :return: None
    """
    for leg in range(number_of_legs):
        turtle.forward(length)
        turtle.stamp()
        turtle.right(360 // number_of_legs) # Определение величины угла
                                            # между лучами
        turtle.goto(0, 0)


def draw_spiral(radius, angle=360):
    #FIXME
    #TODO: move up

    degree = 300 # Начальная градусная мера
    x0 = 0
    y0 = radius

    circle_length = 2 * math.pi * radius
    length = circle_length / angle

    for side in range(angle):
        x = x0 + radius * math.cos(math.radians(degree))
        y = y0 + radius * math.sin(math.radians(degree))

        if degree == 360:
            degree = 0

        turtle.forward(length)
        turtle.left(360 / angle)

        turtle.goto(x, y)

        degree += 1
        radius += ((x-x0)**2 + (y-y0)**2) ** 0.5


def draw_square_spiral(quantity_side, length, indent=5):
    """
    Функция, рисующая квадратную "спираль",
    которая представляет из себя длинную ломаную
    :param quantity_side: количество сторон ломаной
    :param length: длина стороны ломаной
    :param indent: отступ между ломаными (по коорданитам x, y)
    :return: None
    """
    for side in range(quantity_side):
        turtle.forward(length)
        turtle.left(90)

        length += indent


def draw_nested_regular_polygon(number_of_square, length, angle, indent=5):
    #FIXME
    #TODO: indent

    """
    Функция, рисующая произвольное количество
    вложеных правильных многоугольников
    :param number_of_square: количество многоугольников
    :param length:  длина стороны многоугольника
    :param angle: количество углов рисуемого многоугольника
    :param indent: размер отступа между многоугольниками
    :return: None
    """

    for polygon in range(number_of_square):
        radius = length / (2 * math.sin(math.radians(180/angle)))

        draw_regular_polygon(angle, length)

        turtle.penup()
        turtle.back(radius / 2)
        turtle.right(90)
        turtle.forward(radius / 2)
        turtle.left(90)
        turtle.pendown()

        angle += 1
        length += radius


def draw_flower(radius, number_of_petals, angle=360):
    """
    Функция, рисующая цветочек, представляющий из себя совокупность
    произвольного количества двух симметрично расположенных
    окружностей (многоугольников)
    :param radius: радиус окружности (лепестка)
    :param number_of_petals: количество лепестков
    :param angle: количество углов многоугольника. Чем меньше углов,
                  тем меньше многоугольник походит на окружность
    :return: None
    """

    for petals in range(number_of_petals // 2):
        # Количества рисуемых лепестков с учетом симметрии
        for petal in range(2):
            draw_circle(radius, angle)
            turtle.right(180)

        turtle.right(360 / number_of_petals) # Определение величины
                                             # угла между лепестками


def draw_butterfly(radius, design, angle=360):
    """
    Функция, рисующая бабочку, представляющую из себя две окружности
    (два крыла), внутрь которых вложено произвольное количество
    окружностей (узоров крыла)
    :param radius: радиус окружности (крыла)
    :param design: количество узоров на крыле (вложенных в
                   крыло окружностей)
    :param angle: количество углов многоугольника. Чем меньше углов,
                  тем меньше многоугольник походит на окружность
    :return: None
    """

    turtle.right(90) # Становление бабочки вертикально-вверх
    peace_of_wing = radius // design # Определение радиуса
                                     # вложенной окружности

    for wings in range(radius // design):
        for wing in range(2): # Задание количества рисуемых крыльев,
                              # с учетом симметрии
            draw_circle(peace_of_wing, angle)
            turtle.right(180)

        peace_of_wing += radius // design


def draw_spring(number_of_turns, long):
    """
    Функция, рисующая пружину с произвольным количеством виктов,
    которая представляет из себя совокупность произвольного количества
    двух разных окружностей

    :param number_of_turns: количество витков пружины
    :param long: длина пружины
    :return: None
    """

    turtle.left(90) # Становление черепахи вертикально-вверх

    piece_of_length = long / 1 + number_of_turns # Длина пружины до витка
    length_of_turns = piece_of_length / 3 # Длина витка

    radius_piece_of_length = piece_of_length / 2 * math.pi
    # Радиус окружности, представляющей длину до витка

    radius_length_of_turns = length_of_turns / 2 * math.pi
    # Радиус окружности, представляющей длину витка

    turtle.circle(radius_piece_of_length, 180)
    for turns in range(number_of_turns):
        turtle.circle(radius_length_of_turns, 180)
        turtle.circle(radius_piece_of_length, 180)


def draw_smiley_face(radius, body_color='yellow',
                     eye_color='blue', color_of_smile='red'):
    #FIXME
    #TODO: refactoring

    """
    Функция, рисующая смайлик
    :param radius: радиус окружности тела смайлика
    :param body_color: цвет тела смайлика
    :param eye_color: цвет глаз смайлика
    :param color_of_smile: цвет улыбки смайлика
    :return: None
    """
    turtle.penup()
    turtle.goto(0, radius)
    turtle.left(180)
    turtle.pendown()

    body_radius = radius
    eye_radius = body_radius / 8
    smile_radius = body_radius * 2/3
    nose_size = body_radius / 7


    turtle.fillcolor(body_color)
    turtle.begin_fill()
    turtle.circle(body_radius)
    turtle.end_fill()


    turtle.penup()
    turtle.goto(body_radius / 2, body_radius * 2/3)
    turtle.pendown()

    turtle.fillcolor(eye_color)
    turtle.begin_fill()
    turtle.circle(eye_radius)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-body_radius / 2, body_radius * 2/3)
    turtle.pendown()

    turtle.fillcolor(eye_color)
    turtle.begin_fill()
    turtle.circle(eye_radius)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, nose_size / 2)
    turtle.left(90)
    turtle.pendown()
    turtle.width(10)
    turtle.forward(nose_size)

    turtle.pencolor(color_of_smile)
    turtle.penup()
    turtle.goto(-smile_radius, 0)
    turtle.pendown()
    turtle.width(10)
    turtle.circle(smile_radius, 180)


def draw_star(nodes, length):
    #FIXME
    #TODO: more choice of angles
    """
    Функция, рисующая правильную звезду с 5 и 11 вершинами
    :param nodes: количество вершин звезды
    :param length: длина стороны звезды
    :return: None
    """

    turtle.left(180)

    if nodes == 11:
        step = 5
    else:
        nodes = 5
        step = 2


    angle = 180 * (nodes - 2*step) / nodes
    for node in range(nodes):
        turtle.forward(length)
        turtle.left(180 - angle)


draw_spiral(50)
