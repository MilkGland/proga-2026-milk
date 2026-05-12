import turtle

turtle.shape('turtle')
turtle.speed(5)
turtle.pensize(5)


def _window_parameter(code: list, side: int):
    #FIXME
    #TODO: right window size

    display_resolution = {'width': 1920, 'height': 1080}
    window_resolution = (display_resolution['width'] * 0.5,
                         display_resolution['height'] * 0.75)

    text_width = len(code) * side*2 - side
    text_height = side * 2

    width_indentation = (window_resolution[0] - text_width) / 2
    height_indentation = (window_resolution[1] - text_height) / 2

    return width_indentation, height_indentation


def draw_code(code: list):
    """
    Функция, рисующая цифры почтового индекса по
    переданному списку чисел
    :param code: список из чисел почтового индекса
    :return: None
    """

    side = 20
    diagonal = (side ** 2 + side ** 2) ** 0.5

    indent = _window_parameter(code, side)

    x = -indent[0]
    y = 0

    for elements in code:
        turtle.penup()
        turtle.goto(x, y) # Перемещение в точку начала рисования
        turtle.pendown()

        x += side * 2 # Отступ между числами

        if elements == 0:
            for _ in range(2):
                turtle.forward(side)
                turtle.right(90)
                turtle.forward(side * 2)
                turtle.right(90)

        elif elements == 1:
            turtle.penup()
            turtle.right(90)
            turtle.forward(side)
            turtle.pendown()

            turtle.left(90 + 45)
            turtle.forward(diagonal)
            turtle.right(45 + 90)
            turtle.forward(side * 2)

            turtle.left(90) # Исходное положение

        elif elements == 2:
            turtle.forward(side)
            turtle.right(90)
            turtle.forward(side)
            turtle.right(45)
            turtle.forward(diagonal)
            turtle.left(45 + 90)
            turtle.forward(side)

        elif elements == 3:
            for _ in range(2):
                turtle.forward(side)
                turtle.right(45 + 90)
                turtle.forward(diagonal)
                turtle.left(45 + 90)

        elif elements == 4:
            turtle.right(90)
            turtle.forward(side)

            for _ in range(2):
                turtle.left(90)
                turtle.forward(side)

            turtle.right(90 + 90)
            turtle.forward(side * 2)

            turtle.left(90) # Исходное положение

        elif elements == 5:
            turtle.forward(side)
            turtle.right(90 + 90)
            turtle.forward(side)

            for _ in range(2):
                turtle.left(90)
                turtle.forward(side)

            for _ in range(2):
                turtle.right(90)
                turtle.forward(side)

            turtle.right(90 + 90) # Исходное положение

        elif elements == 6:
            turtle.penup()
            turtle.forward(side)
            turtle.pendown()

            turtle.right(45 + 90)
            turtle.forward(diagonal)
            turtle.left(45 + 90)

            for _ in range(4):
                turtle.forward(side)
                turtle.right(90)

        elif elements == 7:
            turtle.forward(side)
            turtle.right(45 + 90)
            turtle.forward(diagonal)
            turtle.left(45)
            turtle.forward(side)

            turtle.left(90) # Исходное положение

        elif elements == 8:
            for _ in range(4):
                turtle.forward(side)
                turtle.right(90)

            turtle.right(90)
            turtle.forward(side)
            turtle.left(90)

            for _ in range(4):
                turtle.forward(side)
                turtle.right(90)

        elif elements == 9:
            for _ in range(4):
                turtle.forward(side)
                turtle.right(90)

            turtle.right(90)
            turtle.forward(side)
            turtle.left(90)
            turtle.forward(side)
            turtle.right(45 + 90)
            turtle.forward(diagonal)

            turtle.left(45 + 90) # Исходное положение


draw_code([1, 4, 1, 7, 0, 0])
