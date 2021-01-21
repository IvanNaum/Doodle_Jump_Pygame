import sys

import pygame

from components.backgrounds.regular_background import RegularBackground
from components.buttons.play_button import PlayButton
from components.doodler import Doodler
from components.enemies.hole import Hole
from components.enemies.ufo import Ufo
from components.logo import Logo
from components.platforms.regular_platform import RegularPlatform
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAY_BUTTON_PRESSED, FPS
from screen import screen


class StartView:
    def __init__(self):
        self.clock = pygame.time.Clock()

        # ----- группы спрайтов ----- #
        self.base_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()
        # /----- группы спрайтов ----- #

        # ----- компоненты ----- #
        self.background = RegularBackground(self.base_group)

        self.play_button = PlayButton(self.base_group)
        self.play_button.rect.topleft = SCREEN_WIDTH * 0.16, SCREEN_HEIGHT * 0.28

        self.logo = Logo(self.base_group)
        self.logo.rect.topleft = SCREEN_WIDTH * 0.04, SCREEN_HEIGHT * 0.1

        self.ufo = Ufo(self.base_group)
        self.ufo.rect.topleft = SCREEN_WIDTH * 0.73, SCREEN_HEIGHT * 0.07

        self.hole = Hole(self.base_group)
        self.hole.rect.topleft = SCREEN_WIDTH * 0.69, SCREEN_HEIGHT * 0.45

        self.platform = RegularPlatform(self.platform_group, self.base_group)
        self.platform.rect.topleft = SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.85

        self.doodler = Doodler(self.base_group)
        self.doodler.rect.midbottom = self.platform.rect.centerx, self.platform.rect.top
        # /----- компоненты ----- #

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == PLAY_BUTTON_PRESSED:
                    return

                self.play_button.update(event)

            self.doodler.update(self.platform_group, listen_key=False)

            self.base_group.draw(screen)

            pygame.display.flip()
            self.clock.tick(FPS)


start_view = StartView()
