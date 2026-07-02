import pygame
from pygame.draw import *
import random

pygame.init()

'''
1 Сделать код читабельным и документированным.
2 Реализовать подсчёт очков.
3 Сделать шарики двигающимися со случайным отражением от стен.
4 Реализовать одновременное присутствие нескольких шариков на экране.
5 Добавить второй тип мишени со своей формой и своим специфическим харктером движения.
6 Выдавать за эти мишени другое количество очков.
7 Сделать таблицу лучших игроков, автоматически сохраняющуюся в файл.
'''

_ALL_POINTS = 0
FPS = 1
screen = pygame.display.set_mode((600, 600))

def print_number_of_point(point=0):
    """
    Функция, выводящая текущее количество очков
    :return: None
    """

    global _ALL_POINTS
    _ALL_POINTS += point

    font = pygame.font.Font(None, 24)
    point_printer = font.render("Number of points: " +
                                 str(_ALL_POINTS),
                                 True, (255, 255, 255))

    screen.blit(point_printer, (25, 25))


def point_counter():
    """
    Функция, подсчитывающая количество очков, которые получил
    игрок за попадание в цель
    :return: None
    """

    max_radius = 75
    quantity_point = round(max_radius / r)

    print_number_of_point(quantity_point)


def set_random_color():
    """
    Функция, задающая случайный цвет каждому новому созданному шарику
    :return: random color
    """

    red = (255, 0, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    magenta = (255, 0, 255)
    cyan = (0, 255, 255)

    colors = [red, blue, green, yellow, magenta, cyan]

    return colors[random.randint(0, 5)]


def create_new_ball():
    """
    Функция, создающая новый шарик со случайными радиусом r (от 10 до 100)
    и координатами x, y (от 100 до 500)
    :return: x, y, r
    """

    global x, y, r

    x = random.randint(100, 475)
    y = random.randint(100, 475)
    r = random.randint(15, 75)

    circle(screen, set_random_color(), (x, y), r)


def check_click_hit(event, x, y, r):
    """
    Функция, проверяющая, попал ли пользователь кликом мышки по шарику.
    :param x: координата x центра шарика
    :param y: координата y центра шарика
    :param r: радиус шарика
    :return: None
    """
    click_x_coord = event.pos[0]
    click_y_coord = event.pos[1]

    click_distance = ((click_x_coord - x)**2 +
                      (click_y_coord - y)**2) ** 0.5

    if click_distance <= r:
        point_counter()


def ball_move():
    """
    Функция, определяющая скорость и движение шарика в границе и
    очищающая шарик с экрана, если его время жизни истекает
    :return: None
    """
    pass


def draw_area():
    """
    Функция, риующая границу, в которой
    шарики будут отскакивать от стены
    :return: None
    """

    line(screen, (255, 255, 255), (550, 550), (550, 50))
    line(screen, (255, 255, 255), (550, 50), (50, 50))
    line(screen, (255, 255, 255), (50, 50), (50, 550))
    line(screen, (255, 255, 255), (50, 550), (550, 550))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_click_hit(event, x, y, r)

    draw_area()
    print_number_of_point()
    create_new_ball()
    pygame.display.update()

    screen.fill('black')

pygame.quit()
