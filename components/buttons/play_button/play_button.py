from pathlib import Path
import pygame

from constants import PLAY_BUTTON_PRESSED

dir_path = Path(__file__).parent.absolute()


class PlayButton(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(str(dir_path / 'play_button.png'))
        self.rect = self.image.get_rect()

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(*event.pos):
                # вызывает собственное событие
                pygame.event.post(pygame.event.Event(PLAY_BUTTON_PRESSED))
