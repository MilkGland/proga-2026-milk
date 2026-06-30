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

FPS = 2
screen = pygame.display.set_mode((500, 500))


def point_counter():
    """
    Функция, подсчитывающая и выводящая на экран количество очков,
    которые получил игрок за попадание в цель
    :return: None
    """
    pass


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
    Функция, создающая новый шарик со случайными радиусом (от 10 до 100)
     и координатами x, y (от 100 до 400)
    :return: None
    """
    global x, y, r
    x = random.randint(100, 500)
    y = random.randint(100, 500)
    r = random.randint(15, 75)

    circle(screen, set_random_color(), (x, y), r)


def click(x, y, r):
    """
    Функция, проверяющая, попал ли пользователь кликом мышки по шарику.
    :param x: координата x центра шарика
    :param y: координата y центра шарика
    :param r: радиус шарика
    :return: None
    """
    pass


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(x, y, r)


    create_new_ball()
    pygame.display.update()
    screen.fill('black')

pygame.quit()
