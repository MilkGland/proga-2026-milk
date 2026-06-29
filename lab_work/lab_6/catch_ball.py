import pygame
from pygame.draw import *
from random import randint
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


def set_color():
    """
    Функция, задающая случайный цвет каждому новому созданному шарику
    :return: color
    """
    pass


def new_ball():
    """
    Функция, создающая новый шарик со случайным радиусом и координатами
    :return: None
    """
    pass


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
            click()


    new_ball()
    pygame.display.update()
    screen.fill('black')

pygame.quit()
