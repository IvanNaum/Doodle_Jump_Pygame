import sys

import pygame

from camera import Camera
from constants import *
from doodler import Doodler
from platforms import RegularPlatform


def terminate():
    pygame.quit()
    sys.exit()


class App:
    def __init__(self):
        # ----- настройка окна ----- #
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Doodle Jump')
        icon = pygame.image.load('data/img/doodler/right.png')
        pygame.display.set_icon(icon)
        # /----- настройка окна ----- #

        self.background = pygame.transform.scale(
            pygame.image.load('data/img/background.png'), (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        self.camera = Camera()
        self.clock = pygame.time.Clock()

        # ----- группы спрайтов ----- #
        self.main_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()
        self.doodler_group = pygame.sprite.Group()
        # /----- группы спрайтов ----- #

        self.doodler = Doodler(self.doodler_group, self.main_group)

    def run(self):
        rect = pygame.Rect((0, 0), RegularPlatform.image.get_size())
        rect.centerx = SCREEN_HALF_WIDTH
        rect.bottom = SCREEN_HEIGHT - 50
        RegularPlatform(
            rect, self.platform_group, self.main_group
        )

        rect2 = rect.copy()
        rect2.top -= JUMP_HEIGHT
        RegularPlatform(
            rect2, self.platform_group, self.main_group
        )

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if self.doodler.check_fall():
                pygame.mixer.music.load('data/sounds/fall_down.mp3')
                pygame.mixer.music.play()
                running = False

            self.screen.blit(self.background, (0, 0))
            self.doodler.update(self.platform_group)
            self.platform_group.update()
            self.main_group.draw(self.screen)
            self.doodler_group.draw(self.screen)  # перемещаем дудлера на передний план
            self.camera.update(self.doodler)
            self.camera.apply(self.main_group)
            pygame.display.flip()
            self.clock.tick(FPS)

        terminate()


if __name__ == '__main__':
    app = App()
    app.run()
