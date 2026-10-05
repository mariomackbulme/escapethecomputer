import pygame
import config

class Nibble(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=config.NIBBLE_SPEED, size=config.NIBBLE_SIZE):
        super().__init__()
        self.images = {
            'front': pygame.transform.smoothscale(
                pygame.image.load(config.NIBBLE_FRONT_IMG).convert_alpha(), size),
            'back': pygame.transform.smoothscale(
                pygame.image.load(config.NIBBLE_BACK_IMG).convert_alpha(), size),
            'left': pygame.transform.smoothscale(
                pygame.image.load(config.NIBBLE_LEFT_IMG).convert_alpha(), size),
            'right': pygame.transform.smoothscale(
                pygame.image.load(config.NIBBLE_RIGHT_IMG).convert_alpha(), size),
        }
        self.image = self.images['front']
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.speed = speed

    def move(self, delta_time):
            keypressed = pygame.key.get_pressed()
            distance = self.speed * (delta_time / 1000)
            if keypressed[pygame.K_UP]:
                self.rect.y -= distance
                self.image = self.images['back']
            if keypressed[pygame.K_DOWN]:
                self.rect.y += distance
                self.image = self.images['front']
            if keypressed[pygame.K_RIGHT]:
                self.rect.x += distance
                self.image = self.images['right']
            if keypressed[pygame.K_LEFT]:
                self.rect.x -= distance
                self.image = self.images['left']

    def update(self):
        self.rect.x += self.speed