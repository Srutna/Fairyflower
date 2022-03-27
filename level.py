import pygame
from tiles import Tile
from settings import *
from player import  *

class Level:
    def __init__(self, level_data, surface):
        self.surface = surface
        self.screen_row = 12
        self.setup_level(level_data)
        self.world_shift = 1

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        index = (len(layout) - self.screen_row) * (-1)
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == "X":
                    x = col_index * 50
                    y = index * 50
                    tile = Tile((x, y), tile_width, tile_height)
                    self.tiles.add(tile)
                if cell == "P":
                    x = col_index * 50
                    y = index * 50
                    print(x,y)
                    temp = Player((x, y))
                    self.player.add(temp)
            index += 1

    def scroll_x(self):
        player = self.player.sprite
        player.y = player.rect.centery
        direction_y = player.


    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.surface)

        self.player.update()
        self.player.draw(self.surface)