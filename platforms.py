import pygame
import random
from constants import *


class RegularPlatform(pygame.sprite.Sprite):
    image = pygame.image.load('data/img/platforms/regular_platform.png')

    def __init__(self, rect, *groups):
        super().__init__(*groups)
        self.rect = rect

    def generate_position(self, *groups) -> None:
        while True:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
            if not self.intersects_with(*groups):
                break

    def intersects_with(self, *groups) -> bool:
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

    def update(self) -> None:
        if self.rect.centery > SCREEN_HEIGHT:
            self.kill()
