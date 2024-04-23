import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((2000, 1000))


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()
finished = False

k = 0.84012
with open('input18.txt', 'r') as file:
    R, n = map(int, file.readline().strip().split())
    x0 = R + 100
    y0 = R+100
    circle(screen, RED, (x0, y0), R)
    line(screen, YELLOW, (0, R+100), (2 * R + 200, R+100))
    for _ in range(n):
        x, y, v = map(int, file.readline().strip().split())
        circle(screen, BLUE, (x0 + x, y0 + y), v * k)

pygame.display.update()

# Основной цикл, в котором отслеживаются события
while not finished:
    # В главном цикле добавляем работу с определенным FPS
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


