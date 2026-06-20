import turtle

ball = turtle.Turtle()
ball.shape('circle')
ball.shapesize(0.5)


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

    def return_param(height, width):
        return height, width

    return return_param


def set_start(x: int, y: int):
    """
    Функция, задающая начальное положение шарика строго внутри нарисованной области
    :param x: положение мяча по координате x
    :param y: положение мяча по координате y
    :return: None
    """

    if abs(x) >= 300:

        if x < 0:
            x = -299
        else:
            x = 299

    if abs(y) >= 300:
        if y < 0:
            y = -299
        else:
            y = 299

    ball.penup()
    ball.goto(x, y)
    ball.pendown()


def material_point(vx: int, vy: int):
    """
    Функция, задающая движение шарику (материальной точке)
    :param vx: скорость шарика по координате x
    :param vy: скорость шарика по координате y
    :return: None
    """

    while True:
        x, y = ball.position()

        if y <= -300 or y >= 300:
            vy = -vy

        if x <= -300 or x >= 300:
            vx = -vx

        vy -= 0.1
        ball.goto(x + vx, y + vy)


if __name__ == '__main__':
    draw_area(300, 300)
    set_start(-300, -300)
    material_point(1, 4)
