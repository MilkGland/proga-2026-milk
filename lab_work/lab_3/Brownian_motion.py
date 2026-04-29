import turtle
import random

turtle.speed(10)

def draw_motion():
    """
    Функция, рисующая имитацию Броуновского движения
    :return: None
    """
    while True:
        number = random.random()

        if number <= 0.5:
            number_of_action = random.randint(0,
                                              25)
            turtle.forward(number_of_action)

        elif number > 0.5:
            number_of_action = random.randint(0,
                                              360)
            number_ = random.random()

            if number_ <= 0.5:
                turtle.left(number_of_action)
            elif number_ > 0.5:
                turtle.right(number_of_action)


draw_motion()
