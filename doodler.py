import pygame
from constants import *


class Doodler(pygame.sprite.Sprite):
    right_image = pygame.image.load('data/img/doodler/right.png')
    left_image = pygame.image.load('data/img/doodler/left.png')
    VY0 = -15  # начальная скорость по оси Y при отскоке, px/s
    AY = 20  # ускорение по оси Y, px/s²
    VX = 5  # постоянная скорость по оси X, px/s

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = self.right_image
        self.rect = self.image.get_rect()
        self.cur_vy = 0  # текущая скорость по оси Y

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.step_left()
        elif keys[pygame.K_RIGHT]:
            self.step_right()

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.cur_vy = self.VY0

        self.cur_vy += self.AY / FPS
        self.rect.top += self.cur_vy

        if self.rect.left >= SCREEN_WIDTH:
            self.rect.left = 0
        if self.rect.right <= 0:
            self.rect.right = SCREEN_WIDTH

    def step_right(self):
        self.rect.left += self.VX
        self.image = self.right_image

    def step_left(self):
        self.rect.left -= self.VX
        self.image = self.left_image
