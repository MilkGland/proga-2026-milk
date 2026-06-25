import pygame

# Инициализация
pygame.init()

# Создание окна
screen = pygame.display.set_mode((400, 400))


# Прорисовка фигур
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


def background(window_parameter: tuple, color: tuple=(255,255,255)):
    pygame.draw.rect(screen, color, (0, 0, window_parameter[0],
                                           window_parameter[1]))


def angry_smiley():
    # Body
    pygame.draw.circle(screen, (255, 255, 0), (200, 200), 150)

    # Right eye
    pygame.draw.circle(screen, (255, 0, 0), (260, 160), 15)

    # Left eye
    pygame.draw.circle(screen, (255, 0, 0), (125, 160), 25)

    # Right pupil
    pygame.draw.circle(screen, (0, 0, 0), (260, 160), 5)

    # Left pupil
    pygame.draw.circle(screen, (0, 0, 0), (125, 160), 8)

    # Mouth
    pygame.draw.rect(screen, (0, 0, 0), (125, 260, 135, 35))

    # Right brow
    pygame.draw.line(screen, (0, 0, 0), (350, 100), (240, 150), 12)

    # Left brow
    pygame.draw.line(screen, (0, 0, 0), (50, 100), (150, 150), 18)


background((400, 400))
angry_smiley()

# Обновление экрана для отображения нарисованного
pygame.display.update()
clock = pygame.time.Clock()

# Основной цикл, в котором будут отслеживаться происходящие события
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.K_q:
            pygame.quit()
