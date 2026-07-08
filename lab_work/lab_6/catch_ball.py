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
screen = pygame.display.set_mode((600, 600))


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


class GameObject:
    def __init__(self):
        self.x = random.randint(100, 475)
        self.y = random.randint(100, 475)
        self.r = random.randint(15, 75)
        self.balls = []


class Ball(GameObject):

    def __init__(self):
        super().__init__()

    def create(self):

        ball = {
            "color": set_random_color(),
            "x_coord": self.x,
            "y_coord": self.y,
            "radius": self.r,
            "life_duration": FPS * 5,
            "is_alive": True
        }

        self.balls.append(ball)


    def move(self):

        if len(self.balls) == 0:
            self.create()

        for ball in self.balls:
            circle(screen, ball["color"],
                    (ball["x_coord"], ball["y_coord"]),
                     ball["radius"])

            screen.fill('black')

            speed_x = random.randint(-5, 5)
            speed_y = random.randint(-5, 5)
            ball["x_coord"] += speed_x
            ball["y_coord"] += speed_y

            circle(screen, ball["color"],
                   (ball["x_coord"], ball["y_coord"]),
                   ball["radius"])


class Points(GameObject):
    max_radius = 75

    def __init__(self):
        super().__init__()
        self.points = 0

    def print_number_of_point(self, point=0):
        """
        Функция, выводящая текущее количество очков
        :return: None
        """

        self.points += point

        font = pygame.font.Font(None, 24)
        point_printer = font.render("Number of points: " +
                                     str(self.points),
                                     True, (255, 255, 255))

        screen.blit(point_printer, (25, 25))


    def point_counter(self):
        quantity_point = round(self.max_radius / self.r)

        self.print_number_of_point(quantity_point)


class Manager(GameObject):
    def __init__(self):
        super().__init__()
        self.event = event

    def check_click_hit(self, event, x, y, r):
        """
        Функция, проверяющая, попал ли пользователь кликом мышки по шарику.
        :param x: координата x центра шарика
        :param y: координата y центра шарика
        :param r: радиус шарика
        :return: None
        """
        click_x_coord = self.event.pos[0]
        click_y_coord = self.event.pos[1]

        click_distance = ((click_x_coord - self.x)**2 +
                          (click_y_coord - self.y)**2) ** 0.5

        if click_distance <= r:
            pass #TODO: point_counter


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
ball = Ball()
cur_point = Points()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass #TODO

    draw_area()
    cur_point.print_number_of_point()
    ball.move()
    pygame.display.update()

pygame.quit()
