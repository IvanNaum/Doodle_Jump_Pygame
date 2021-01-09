import sys
import pygame

from screen import screen
from camera import Camera
from constants import SCREEN_HEIGHT, SCREEN_HALF_WIDTH, JUMP_HEIGHT, FPS

from components.backgrounds.regular_background import RegularBackground
from components.doodler import Doodler
from components.platforms.regular_platform import RegularPlatform
from components.score import Score

from views.end_view import end_view


class GameView:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.camera = Camera()

        # ----- группы спрайтов ----- #
        self.base_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()
        self.doodler_group = pygame.sprite.Group()
        self.static_group = pygame.sprite.Group()
        self.dynamic_group = pygame.sprite.Group()
        # /----- группы спрайтов ----- #

        # ----- компоненты ----- #
        self.background = RegularBackground(self.static_group, self.base_group)
        self.doodler = Doodler(self.doodler_group, self.dynamic_group, self.base_group)
        self.score = Score(self.static_group, self.base_group)
        # /----- компоненты ----- #

    def run(self):
        # ----- генерация платформ ----- #
        platform1 = RegularPlatform(
            self.platform_group, self.dynamic_group, self.base_group
        )
        platform1.rect.midtop = SCREEN_HALF_WIDTH, SCREEN_HEIGHT - 50

        platform2 = RegularPlatform(
            self.platform_group, self.dynamic_group, self.base_group
        )
        platform2.rect.midtop = platform1.rect.centerx, platform1.rect.top - JUMP_HEIGHT
        # /----- генерация платформ ----- #

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.doodler.fell():
                toggle_to_end_view()
                return

            self.doodler.update(self.platform_group)
            self.platform_group.update()

            self.base_group.draw(screen)
            self.doodler_group.draw(screen)  # перемещаем дудлера на передний план

            self.camera.update(self.doodler)
            self.camera.apply(self.dynamic_group)

            self.score += self.camera.dy

            pygame.display.flip()
            self.clock.tick(FPS)


def toggle_to_end_view():
    end_view.run()


game_view = GameView()
