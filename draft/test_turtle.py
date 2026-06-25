import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
color = (255, 255, 255)





indent = 50
window_size = {'width': 400, 'height': 400}
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


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
