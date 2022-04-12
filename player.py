import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((30,30))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft = pos)

        #player movement
        self.direction = pygame.math.Vector2((0,0))
        self.speed = 4
        self.gravity = 0.4
        self.jump_speed = -8

    def get_input(self):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_LEFT]:
            self.direction.x = -1
        elif key_pressed[pygame.K_RIGHT]:
            self.direction.x = 1
        elif key_pressed[pygame.K_SPACE]:
            self.jump()
        # elif key_pressed[pygame.K_UP]:
        #     self.direction.y = -1
        # elif key_pressed[pygame.K_DOWN]:
        #     self.direction.y = 1
        else:
            self.direction.x = 0
            #self.direction.y = 0

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        #self.rect.y += self.direction.y * self.speed
