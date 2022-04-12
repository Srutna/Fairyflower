import pygame
from tiles import Tile
from settings import *
from player import  Player

class Level:
    def __init__(self, level_data, surface):
        self.surface = surface
        self.screen_row = 12
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        index = (len(layout) - self.screen_row) * (-1)
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * 50
                y = index * 50
                if cell == "X":
                    tile = Tile((x, y), tile_width, tile_height)
                    self.tiles.add(tile)
                if cell == "P":
                    print(x,y)
                    temp = Player((x, y))
                    self.player.add(temp)
            index += 1

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        player_y = player.rect.centery
        direction_x = player.direction.x
        direction_y = player.direction.y

        if player_y < screen_height / 3 and direction_y < 0:
            self.world_shift = 4
            player.speed = 0
        elif player_y > screen_height - 100 and direction_y > 0:
            self.world_shift = -4
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 4

        if player_x < 100 and direction_x < 0:
            player.speed = 0
        elif player_x > 500 and direction_x > 0:
            player.speed = 0
        else:
            player.speed = 4

    def horizontal_movement_collision(self):
        player = self.player.sprite

        player.rect.x += player.direction.x * player.speed
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        #level
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.surface)
        self.scroll_x()

        #player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.surface)