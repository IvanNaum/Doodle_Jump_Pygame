from pathlib import Path
import pygame

from constants import SCREEN_HEIGHT

dir_path = Path(__file__).parent.absolute()


class RegularPlatform(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(str(dir_path / 'regular_platform.png'))
        self.rect = self.image.get_rect()

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
