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
FPS = 25
SCREEN_PARAMETER = (600, 600)
screen = pygame.display.set_mode(SCREEN_PARAMETER)


def set_random_color():
    """
    Функция, задающая случайный из 5 цветов каждому
    новому созданному шарику
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


class Ball:
    def __init__(self):
        self.x = random.randint(100, 475)
        self.y = random.randint(100, 475)
        self.r = random.randint(15, 75)
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)

        self.color = set_random_color()
        self.life_duration = FPS * 5
        self.is_alive = True
        self.balls = []

    def move(self):
        screen.fill('black')

        circle(screen, self.color,
               (self.x, self.y),
               self.r)

        self.x += self.speed_x
        self.y += self.speed_y

    def is_clicked(self, event_):
        click_x_coord = event_.pos[0]
        click_y_coord = event_.pos[1]

        click_distance = ((click_x_coord - self.x)**2 +
                          (click_y_coord - self.y)**2) ** 0.5

        if click_distance <= self.r:
            points.point_counter()

class ScoreTable:
    _max_radius = 75

    def __init__(self):
        self.points = 0

    def print_number_of_point(self, point=0):
        self.points += point

        font = pygame.font.Font(None, 24)
        point_printer = font.render("Number of points: " +
                                     str(self.points),
                                     True, (255, 255, 255))

        screen.blit(point_printer, (25, 25))

    def point_counter(self):
        quantity_point = round(self._max_radius / ball.r)

        self.print_number_of_point(quantity_point)


class Area:
    indent = 50

    @staticmethod
    def get_parameter():
        x_parameter = {"left-hand limit": Area.indent,
                        "right-hand limit": SCREEN_PARAMETER[0] -
                                             Area.indent}

        y_parameter = {"lower limit": Area.indent,
                        "upper limit": SCREEN_PARAMETER[1] -
                                        Area.indent}

        return x_parameter, y_parameter

    @staticmethod
    def draw():
        width_end_pos = SCREEN_PARAMETER[0] - Area.indent
        height_end_pos = SCREEN_PARAMETER[1] - Area.indent
        width_start_pos = Area.indent
        height_start_pos = Area.indent

        line(screen, (255, 255, 255),
             (width_end_pos, height_end_pos),
             (width_end_pos, height_start_pos))

        line(screen, (255, 255, 255),
             (width_end_pos, height_start_pos),
             (width_start_pos, height_start_pos))

        line(screen, (255, 255, 255),
             (width_start_pos, height_start_pos),
             (width_start_pos, height_end_pos))

        line(screen, (255, 255, 255),
             (width_start_pos, height_end_pos),
             (width_end_pos, height_end_pos))


class Manager:
    @staticmethod
    def check_collation():
        x_area_param, y_area_param = Area.get_parameter()

        if (ball.x - ball.r <= x_area_param["left-hand limit"] or
             ball.x + ball.r >= x_area_param["right-hand limit"]):
            ball.speed_x = -ball.speed_x

        elif (ball.y - ball.r < y_area_param["lower limit"] or
             ball.y + ball.r > y_area_param["upper limit"]):
            ball.speed_y = -ball.speed_y


clock = pygame.time.Clock()
ball = Ball()
points = ScoreTable()
manager = Manager()
finished = False
pygame.display.update()


while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            ball.is_clicked(event)

    ball.move()
    manager.check_collation()
    Area.draw()
    points.print_number_of_point()
    pygame.display.update()

pygame.quit()
