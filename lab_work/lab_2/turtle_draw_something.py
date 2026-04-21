import turtle
turtle.speed(1)
turtle.shape('turtle')

def draw_regular_polygon(count_side, length):
    for side in range(count_side):
        turtle.forward(length)
        turtle.right(360 // count_side)


def draw_circle():
    for radius in range(360 // 5):
        turtle.forward(5)
        turtle.right(5)


def draw_ten_nested_square(length):
    for square in range(10):
        draw_regular_polygon(4, length)
        length += 10

        turtle.penup()
        turtle.left(90)
        turtle.forward(5)
        turtle.right(90)
        turtle.back(5)
        turtle.pendown()



draw_ten_nested_square(50)
