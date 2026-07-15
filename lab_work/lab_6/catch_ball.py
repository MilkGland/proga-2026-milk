import pygame
from pygame.draw import *
import random

pygame.init()

'''
7 Сделать таблицу лучших игроков, автоматически сохраняющуюся в файл.
'''


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
        self.x = random.randint(125, 450)
        self.y = random.randint(125, 450)
        self.radius = random.randint(15, 75)
        self.speed_x = random.choice([-5, -4, -3, -2, -1,
                                       5, 4, 3, 2, 1])
        self.speed_y = random.choice([-5, -4, -3, -2, -1,
                                       5, 4, 3, 2, 1])

        self.color = set_random_color()
        self.life_duration = FPS * 15

    def move(self):
        circle(screen, self.color,
               (self.x, self.y),
               self.radius)

        self.x += self.speed_x
        self.y += self.speed_y
        self.life_duration -= 1

    def is_collided(self):
        x_area_param, y_area_param = Area.get_parameter()

        if (self.x - self.radius <= x_area_param["left-hand limit"] or
             self.x + self.radius >= x_area_param["right-hand limit"]):
            self.speed_x = -self.speed_x

        elif (self.y - self.radius < y_area_param["lower limit"] or
              self.y + self.radius > y_area_param["upper limit"]):
            self.speed_y = -self.speed_y

    @staticmethod
    def is_clicked(ball, event_):
        click_x_coord = event_.pos[0]
        click_y_coord = event_.pos[1]

        click_distance = ((click_x_coord - ball.x) ** 2 +
                          (click_y_coord - ball.y) ** 2) ** 0.5

        if click_distance <= ball.radius:
            points.ball_point_counter(ball)
            balls.remove(ball)


class Cube:
    def __init__(self):
        self.x = random.randint(100, 450)
        self.y = random.randint(100, 450)
        self.width = random.randint(15, 45)
        self.height = self.width
        self.speed_x = random.choice([-5, -4, -3, 3, 4, 5])

        self.color = set_random_color()
        self.life_duration = FPS * 15

    def move(self):
        rect(screen, self.color, (self.x, self.y,
                                        self.width, self.height))

        self.x += self.speed_x
        self.life_duration -= 1

    def is_collided(self):
        x_area_param, y_area_param = Area.get_parameter()

        if (self.x < x_area_param["left-hand limit"] or
                self.x + self.width > x_area_param["right-hand limit"]):
            self.speed_x = -self.speed_x

    @staticmethod
    def is_clicked(cube, event_):
        click_x_coord = event_.pos[0]
        click_y_coord = event_.pos[1]

        if (cube.x <= click_x_coord and not
            cube.x + cube.width <= click_x_coord):

            if (cube.y <= click_y_coord and not
                cube.y + cube.height <= click_y_coord):

                points.cube_point_counter(cube)
                cubes.remove(cube)


class ScoreTable:
    _max_radius = 75
    _max_perimeter = (45 + 45) * 2

    def __init__(self):
        self.points = 0

    def print_number_of_point(self, point=0):
        self.points += point

        font = pygame.font.Font(None, 24)
        point_printer = font.render("Number of points: " +
                                     str(self.points),
                                     True, (255, 255, 255))

        screen.blit(point_printer, (50, 25))

    def ball_point_counter(self, ball):
        quantity_point = round(self._max_radius / ball.radius)

        self.print_number_of_point(quantity_point)

    def cube_point_counter(self, cube):
        quantity_point = int(self._max_perimeter / (cube.width +
                                                      cube.height) * 2)

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

    @staticmethod
    def add_cube():
        Manager.time_between_additions += 1

        if Manager.time_between_additions == FPS * 5:
            cubes.append(Cube())
            Manager.time_between_additions = 0

    @staticmethod
    def cube_is_alive(cube):
        if cube.life_duration <= 0:
            cubes.remove(cube)


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
        Area.draw()
        points.print_number_of_point()
        random.choice([Manager.add_ball(), Manager.add_cube()])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for ball in balls:
                    Ball.is_clicked(ball, event)

                for cube in cubes:
                    Cube.is_clicked(cube, event)

        if cubes:
            for cube in cubes:
                Manager.cube_is_alive(cube)
                cube.move()
                cube.is_collided()

        if balls:
            for ball in balls:
                Manager.ball_is_alive(ball)
                ball.move()
                ball.is_collided()

        else:
            Area.draw()
            points.print_number_of_point()
            pygame.display.update()

        pygame.display.update()


FPS = 25
SCREEN_PARAMETER = (600, 600)
screen = pygame.display.set_mode(SCREEN_PARAMETER)

cubes = [Cube()]
balls = [Ball()]
clock = pygame.time.Clock()
points = ScoreTable()
pygame.display.update()

main()
pygame.quit()
