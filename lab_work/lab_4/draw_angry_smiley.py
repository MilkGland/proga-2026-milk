import pygame
import math

pygame.init()
screen = pygame.display.set_mode((400, 400))


def net(window_parameter: tuple, indent: int,
         color: tuple=(255,255,255)):
    """
    Функция, рисующая симметричную сетку из квадратиков
    :param window_parameter: размер окна модуля pygame (x, y)
    :param indent: отступ между линиями (длина и ширина
                    квадратика в сетке)
    :param color: цвет сетки (R, G, B)
    :return: None
    """
    window_size = {'width': window_parameter[0],
                   'height': window_parameter[1]}
    number_of_line_y = window_size.get('height') // indent
    number_of_line_x = window_size.get('width') // indent

    x = indent
    y = indent

    for _ in range(number_of_line_x):
        pygame.draw.line(screen, color, (x, 0), (x, 400))
        x += indent

    for _ in range(number_of_line_y):
        pygame.draw.line(screen, color, (0, y), (400, y))
        y += indent


def background(window_parameter: tuple, color: tuple=(127,127,127)):
    pygame.draw.rect(screen, color, (0, 0, window_parameter[0],
                                           window_parameter[1]))


def angry_smiley(surface, x, y, radius):
    #FIXME
    #TODO: (x, y) coordinates
    """
    Функция, рисующая злой смайлик в виде окружности в точке (x, y),
    которая находится в цетре окружности
    :param surface: поверхность, на которой наноситься рисунок
    :param x: координата x центра окружности
    :param y: координата y центра окружности
    :param radius: радиус окружности
    :return: None
    """

    body_radius = radius
    right_eye_radius = radius / 10
    left_eye_radius = radius / 6
    mouth_width = (27 / 7 * math.pi * body_radius ** 2 * 21 / 314) ** 0.5
    mouth_height = mouth_width * 7 / 27
    right_brow_thickness = math.ceil(right_eye_radius / 3 * 2)
    left_brow_thickness = math.ceil(left_eye_radius / 3 * 2)

    right_eye_x = x * 1.3
    right_eye_y = y * 0.8
    left_eye_x = x * 0.625
    left_eye_y = y * 0.8
    mouth_x = x * 0.625
    mouth_y = y * 1.3
    right_brow_x1 = x * 1.75
    right_brow_x2 = x * 1.2
    right_brow_y1 = y * 0.5
    right_brow_y2 = y * 0.75
    left_brow_x1 = x * 0.25
    left_brow_x2 = x * 0.75
    left_brow_y1 = y * 0.5
    left_brow_y2 = y * 0.75

    draw_body(surface, x, y, body_radius)
    draw_eye(surface, right_eye_x, right_eye_y, right_eye_radius)
    draw_eye(surface, left_eye_x, left_eye_y, left_eye_radius)
    draw_mouth(surface, mouth_x, mouth_y, mouth_width, mouth_height)
    draw_brow(surface, right_brow_x1, right_brow_y1,
               right_brow_x2, right_brow_y2, right_brow_thickness)
    draw_brow(surface, left_brow_x1, left_brow_y1,
               left_brow_x2, left_brow_y2, left_brow_thickness)

def draw_body(surface, x, y, radius):
    """
    Функция, рисующая тело смайлика в виде окружности в точке (x, y),
    которая находится в цетре окружности
    :param surface: поверхность, на которой наноситься рисунок
    :param x: координата x центра окружности
    :param y: координата y центра окружности
    :param radius: радиус окружности
    :return: None
    """

    pygame.draw.circle(surface, (255, 255, 0), (x, y), radius)


def draw_eye(surface, x, y, radius):
    """
    Функция, рисующая глаза смайлика в виде окружности в точке (x, y)
    :param surface: поверхность, на которой наноситься рисунок
    :param x: координата x глаза на окружности
    :param y: координата y глаза на окружности
    :param radius: радиус окружности
    :return: None
    """

    pygame.draw.circle(surface, (255, 0, 0), (x, y), radius)
    pygame.draw.circle(surface, (0, 0, 0), (x, y), radius/3)


def draw_mouth(surface, x, y, width, height):
    """
    Функция, рисующая рот смайлика в виде прямоугольника в точке (x, y)
    :param surface: поверхность, на которой наноситься рисунок
    :param x: координата x левого верхнего угла прямоугольника
    :param y: координата y левого верхнего угла прямоугольника
    :param width: ширина прямоугольника от точки (x, y)
    :param height: высота прямоугольника от точки (x, y)
    :return: None
    """

    pygame.draw.rect(surface, (0, 0, 0), (x, y, width, height))


def draw_brow(surface, x1, y1, x2, y2, thickness):
    """
    Функция, рисующая брови смайлика в виде линии из точки (x1, y1)
    в точку (x2, y2)
    :param surface: поверхность, на которой наноситься рисунок
    :param x1: координата x исходной точки линии
    :param y1: координата y исходной точки линии
    :param x2: координата x конечной точки линии
    :param y2: координата y конечной точки линии
    :param thickness: ширина линии
    :return: None
    """

    pygame.draw.line(surface, (0, 0, 0), (x1, y1), (x2, y2), thickness)


background((400, 400))
angry_smiley(screen, 200, 200, 150)

pygame.display.update()
clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.K_q:
            pygame.quit()
