import pygame
from settings import *
from level import *

pygame.init()
clk = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

level = Level(level_map, screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    level.run()
    clk.tick(fps)
    pygame.display.update()