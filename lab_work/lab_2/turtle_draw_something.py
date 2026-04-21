import turtle

turtle.shape('turtle')


def draw_regular_polygon(count_side, length):
    """
    Функция, рисующая любой правильный многоугольник
    :param count_side: количество углов многоугольника
    :param length: длина стороны многоугольника
    :return: None
    """
    for side in range(count_side):
        turtle.forward(length)
        turtle.left(360 // count_side)


def draw_circle(size):
    #FIXME
    """
    Функция, рисующая окружность, которая представляет из себя многоугольник с множеством углов
    :param size: диаметр окружности
    :return: None
    """
    for _ in range(360 // 5): # Определение градусной меры окружности с учетом фиксированого параметра
        turtle.forward(size)
        turtle.right(5) # Фиксированый параметр, влияющий на количество углов в данном многоугольнике
                        # Чем он больше, тем меньше углов в многоугольнике
                        # Чем он меньше, тем медленнее черепаха рисует многоугольник


def draw_nested_square(count_square, length, indent):
    #FIXME
    """
    Функция, рисующая произвольное количество вложеных правильных квадратов
    :param count_square: количество квадратов
    :param length: длина стороны квадрата
    :param indent: размер отступа между квадратами
    :return: None
    """
    x = indent # Координата перемещения черепхи по оси X
    y = indent # Координата перемещения черепхи по оси Y
    for square in range(count_square):
        draw_regular_polygon(4, length)
        length += indent * 2

        turtle.penup()
        turtle.goto(-x, -y)
        x += indent
        y += indent
        turtle.pendown()

