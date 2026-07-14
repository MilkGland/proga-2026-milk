import pygame
from pygame.draw import *
import random

pygame.init()

'''
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
        self.x = random.randint(100, 450)
        self.y = random.randint(100, 450)
        self.radius = random.randint(15, 75)
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)

        self.color = set_random_color()
        self.life_duration = FPS * 30

    def move(self):
        circle(screen, self.color,
               (self.x, self.y),
               self.radius)

        self.x += self.speed_x
        self.y += self.speed_y
        self.life_duration -= 1

    @staticmethod
    def is_clicked(ball, event_):
        click_x_coord = event_.pos[0]
        click_y_coord = event_.pos[1]

        click_distance = ((click_x_coord - ball.x)**2 +
                          (click_y_coord - ball.y)**2) ** 0.5

        if click_distance <= ball.radius:
            points.point_counter(ball)
            balls.remove(ball)

    def is_collided(self):
        x_area_param, y_area_param = Area.get_parameter()

        if (self.x - self.radius <= x_area_param["left-hand limit"] or
             self.x + self.radius >= x_area_param["right-hand limit"]):
            self.speed_x = -self.speed_x

        elif (self.y - self.radius < y_area_param["lower limit"] or
              self.y + self.radius > y_area_param["upper limit"]):
            self.speed_y = -self.speed_y

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

        screen.blit(point_printer, (50, 25))

    def point_counter(self, ball):
        quantity_point = round(self._max_radius / ball.radius)

        self.print_number_of_point(quantity_point)


class Manager:
    time_between_additions = 0

    @staticmethod
    def add_ball():
        Manager.time_between_additions += 1

        if Manager.time_between_additions == FPS * 5:
            balls.append(Ball())
            Manager.time_between_additions = 0

    @staticmethod
    def ball_is_alive(ball):
        if ball.life_duration <= 0:
            balls.remove(ball)


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


def main():
    finished = False
    while not finished:
        clock.tick(FPS)
        screen.fill('black')
        Manager.add_ball()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for ball in balls:
                    Ball.is_clicked(ball, event)

        if balls:
            for ball in balls:
                Manager.ball_is_alive(ball)
                ball.move()
                ball.is_collided()
                Area.draw()
                points.print_number_of_point()

        else:
            Area.draw()
            points.print_number_of_point()
            pygame.display.update()

        pygame.display.update()


balls = [Ball()]
clock = pygame.time.Clock()
points = ScoreTable()
pygame.display.update()

main()
pygame.quit()
