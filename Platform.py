import pygame
from constants import *


class PlatformSprite(pygame.sprite.Sprite):
    image = pygame.image.load('data/img/platforms/regular_platform.png')

    def __init__(self, *groups):
        super(PlatformSprite, self).__init__(*groups)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, pos):
        self.rect.topleft = pos
