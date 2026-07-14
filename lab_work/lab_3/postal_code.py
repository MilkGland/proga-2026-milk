import turtle

turtle.shape('turtle')
turtle.speed(5)
turtle.pensize(5)


def _window_parameter(code: tuple, side: int):
    #TODO: indent to window size

    return 250


def draw_code(code: tuple):
    """
    Функция, рисующая цифры почтового индекса по
    переданному списку чисел
    :param code: список из чисел почтового индекса
    :return: None
    """

    side = 20
    diagonal = (side ** 2 + side ** 2) ** 0.5

    indent = _window_parameter(code, side)

    x = -indent
    y = 0

    for tuples in code:
        for elements in tuples:
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


draw_code([(1, 4, 1, 7, 0, 0), (5, 8, 9, 9, 2, 1)])
