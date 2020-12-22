import pygame
import random
from constants import *


class RegularPlatform(pygame.sprite.Sprite):
    image = pygame.image.load('data/img/platforms/regular_platform.png')

    def __init__(self, *groups):
        super().__init__()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.generate_position(*groups)
        self.add(*groups)

    def generate_position(self, *groups):
        while True:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
            if not self.intersects_with(*groups):
                break

    def intersects_with(self, *groups):
        """
        Проверяет пересечение self-спрайта с группами спрайтов по маске
        :param groups: группы спрайтов
        :return: bool
        """
        for group in groups:
            for sprite in group:
                if pygame.sprite.collide_mask(self, sprite):
                    return True
        return False
