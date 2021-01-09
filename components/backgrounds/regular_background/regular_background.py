from pathlib import Path
import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

dir_path = Path(__file__).parent.absolute()


class RegularBackground(pygame.sprite.Sprite):
    def __init__(self, *groups, **size):
        super().__init__(*groups)

        width = size.get('width', SCREEN_WIDTH)
        height = size.get('height', SCREEN_HEIGHT)

        self.image = pygame.transform.scale(
            pygame.image.load(str(dir_path / 'regular_background.png')),
            (width, height)
        )
        self.rect = self.image.get_rect()
