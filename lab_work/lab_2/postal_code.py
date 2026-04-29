import turtle

turtle.shape('turtle')
turtle.speed(5)
turtle.pensize(5)


def draw_code(code: list):
    """
    Функция, рисующая цифры почтового индекса по
    переданному списку чисел
    :param code: список из чисел почтового индекса
    :return: None
    """

    side = 25
    diagonal = (side ** 2 + side ** 2) ** 0.5
    x = 0
    y = side

    for elements in code:
        turtle.penup()
        turtle.goto(x, y) # Перемещение в точку начала рисования
        turtle.pendown()

        x += side * 2 # Отступ между числами

        if elements == 0:
            turtle.forward(side)
            turtle.right(90)
            turtle.forward(side * 2)
            turtle.right(90)
            turtle.forward(side)
            turtle.right(90)
            turtle.forward(side * 2)

            turtle.right(90) # Исходное положение

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
            pass

        elif elements == 3:
            pass

        elif elements == 4:
            turtle.right(90)
            turtle.forward(side)
            turtle.left(90)
            turtle.forward(side)
            turtle.left(90)
            turtle.forward(side)
            turtle.right(90 + 90)
            turtle.forward(side * 2)

            turtle.left(90) # Исходное положение

        elif elements == 5:
            pass

        elif elements == 6:
            pass

        elif elements == 7:
            turtle.forward(side)
            turtle.right(45 + 90)
            turtle.forward(diagonal)
            turtle.left(45)
            turtle.forward(side)

            turtle.left(90) # Исходное положение

        elif elements == 8:
            pass

        elif elements == 9:
            pass



draw_code([1, 4, 1, 7, 0, 0])
