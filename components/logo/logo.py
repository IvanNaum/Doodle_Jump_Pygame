from pathlib import Path

import pygame

dir_path = Path(__file__).parent.absolute()


class Logo(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(str(dir_path / 'logo.png'))
        self.rect = self.image.get_rect()
