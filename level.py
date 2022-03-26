import pygame
from tiles import Tile
from settings import *

class Level:
    def __init__(self, level_data, surface):
        self.surface = surface
        self.setup_level(level_data)
        self.world_shift = 1

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == "X":
                    x = col_index * tile_width
                    y = row_index * tile_height
                    tile = Tile((x, y), tile_width, tile_height)
                    self.tiles.add(tile)


    def run(self):
        #self.tiles.update(self.world_shift)
        self.tiles.draw(self.surface)