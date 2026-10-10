import pygame
import config
import utils
import random

class Nibble(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=config.NIBBLE_SPEED, size=config.NIBBLE_SIZE):
        super().__init__()
        self.images = {
            'front': utils.load_scaled_image(config.NIBBLE_FRONT_IMG, size),
            'back': utils.load_scaled_image(config.NIBBLE_BACK_IMG, size),
            'left': utils.load_scaled_image(config.NIBBLE_LEFT_IMG, size),
            'right': utils.load_scaled_image(config.NIBBLE_RIGHT_IMG, size),
        }
        self.image = self.images['front']
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.speed = speed
        self.direction = pygame.math.Vector2(0,1)
        self.x = x
        self.y = y

    def move(self, delta_time):
            keypressed = pygame.key.get_pressed()
            distance = self.speed * (delta_time / 1000)
            if keypressed[pygame.K_UP]:
                self.rect.y -= distance
                self.image = self.images['back']
                self.direction = pygame.math.Vector2(0, -1)
            if keypressed[pygame.K_DOWN]:
                self.rect.y += distance
                self.image = self.images['front']
                self.direction = pygame.math.Vector2(0, 1)
            if keypressed[pygame.K_RIGHT]:
                self.rect.x += distance
                self.image = self.images['right']
                self.direction = pygame.math.Vector2(1, 0)
            if keypressed[pygame.K_LEFT]:
                self.rect.x -= distance
                self.image = self.images['left']
                self.direction = pygame.math.Vector2(-1, 0)

    def shoot(self):
        return Bit(self.rect.centerx, self.rect.centery, self.direction)

class Bit(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, distance=1000, speed=2):
        super().__init__()
        bit_font = pygame.font.Font(config.FONT_BITS, 15)
        self.char = str(random.randint(0,1))
        self.image = bit_font.render(self.char, True, '#f5cf65')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.speed = speed
        self.pos = pygame.math.Vector2(x, y)
        self.endPosition = self.pos + direction.normalize() * distance
        self.index = 0

    def update(self, board_rect):
        direction = self.endPosition - self.pos
        if board_rect.contains(self.rect) == False:
            self.kill()
        if direction.length() > self.speed:
            self.pos += direction.normalize() * self.speed
        else:
            self.pos = self.endPosition
            self.kill()
        self.rect.topleft = (self.pos.x, self.pos.y)