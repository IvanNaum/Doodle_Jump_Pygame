from pathlib import Path
import pygame

dir_path = Path(__file__).parent.absolute()


class Score(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.font = pygame.font.Font(
            str(dir_path / 'al_seana.ttf'),
            36
        )
        self.value = 0

        self.image = self.render()
        self.rect = pygame.Rect(10, 10, *self.image.get_size())

    def __iadd__(self, value):
        self.value += value
        self.image = self.render()
        self.rect.size = self.image.get_size()
        return self

    def render(self):
        return self.font.render(
            str(self.value), True, pygame.color.Color('black')
        )
