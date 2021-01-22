from pathlib import Path

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

dir_path = Path(__file__).parent.absolute()


class Mark(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(str(dir_path / 'mark.png'))
        self.rect = self.image.get_rect()

    def set_position(self, score):
        self.rect.right = SCREEN_WIDTH + 20
        self.rect.top = SCREEN_HEIGHT // 2 - score
