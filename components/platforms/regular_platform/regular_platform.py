from pathlib import Path
from random import randint
import pygame

from constants import SCREEN_HEIGHT, JUMP_HEIGHT, SCREEN_WIDTH

dir_path = Path(__file__).parent.absolute()


class RegularPlatform(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(str(dir_path / 'regular_platform.png'))
        self.rect = self.image.get_rect()

    def intersects_with(self, *groups) -> bool:
        """
        Проверяет пересечение self-спрайта с группами спрайтов
        :param groups: группы спрайтов
        :return: bool
        """
        for group in groups:
            if pygame.sprite.spritecollideany(self, group):
                return True

        return False

    def update(self) -> None:
        if self.rect.centery > SCREEN_HEIGHT:
            self.kill()

    def generate_position(self, *groups, y_limits):
        """
        Генерирует постоянную позицию платформы на экране
        :param y_limits: границы генерации платформы по оси Y
        :param groups: группы, относительно спрайтов которых будет
        генерироваться позиция текущей платформы
        :return: None
        """
        while True:
            self.rect.x = randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = randint(*y_limits)

            if not self.intersects_with(*groups) and self.is_possible_delta_dist(*groups):
                break

    def is_possible_delta_dist(self, *groups):
        """
        Проверяет расстояние между самым высоким спрайтом в группах и self.спрайтом.
        :param groups: группы спрайтов
        :return: bool
        """
        max_top = min([sprite.rect.top for group in groups for sprite in group.sprites()])
        if max_top - self.rect.top > JUMP_HEIGHT:
            return False

        return True
