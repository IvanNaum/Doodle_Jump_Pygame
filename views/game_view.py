import sys

import pygame

from camera import Camera
from components.backgrounds.regular_background import RegularBackground
from components.doodler import Doodler
from components.mark.mark import Mark
from components.platforms.regular_platform import RegularPlatform
from components.score import Score
from constants import SCREEN_HEIGHT, SCREEN_HALF_WIDTH, FPS
from database import data_base
from screen import screen


class GameView:
    GENERATE_ON_SCREEN = 0
    GENERATE_ABOVE_SCREEN = 1

    def __init__(self):
        self.clock = pygame.time.Clock()

        self.camera = Camera()

        # ----- группы спрайтов ----- #
        self.base_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()
        self.doodler_group = pygame.sprite.Group()
        self.topbar_group = pygame.sprite.Group()
        self.static_group = pygame.sprite.Group()
        self.dynamic_group = pygame.sprite.Group()
        self.marks_group = pygame.sprite.Group()
        # /----- группы спрайтов ----- #

        # ----- компоненты ----- #
        self.background = RegularBackground(self.static_group, self.base_group)
        self.doodler = Doodler(self.doodler_group, self.dynamic_group, self.base_group)
        self.score = Score(self.topbar_group, self.static_group, self.base_group)
        # /----- компоненты ----- #

        self.platforms_density = 10

    def run(self):
        # Заполнение группы меток
        self.fill_marks_group()

        start_platform = RegularPlatform(
            self.platform_group, self.dynamic_group, self.base_group
        )
        start_platform.rect.midbottom = SCREEN_HALF_WIDTH, SCREEN_HEIGHT
        self.generate_platforms(mode=self.GENERATE_ON_SCREEN)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    data_base.add_score(self.score.get_value())
                    pygame.quit()
                    sys.exit()

            if self.doodler.fell():
                data_base.add_score(self.score.get_value())
                return

            self.generate_platforms()

            self.doodler.update(self.platform_group)
            self.platform_group.update()

            self.base_group.draw(screen)
            self.doodler_group.draw(screen)  # перемещаем дудлера на передний план
            self.marks_group.draw(screen)

            # перемещаем элементы верхней панели на передний план
            self.topbar_group.draw(screen)

            self.camera.update(self.doodler)
            self.camera.apply(self.dynamic_group)

            self.score += self.camera.dy

            pygame.display.flip()
            self.clock.tick(FPS)

    def generate_platforms(self, mode=GENERATE_ABOVE_SCREEN):
        if mode == self.GENERATE_ON_SCREEN:
            y_limits = (0, SCREEN_HEIGHT)
        else:
            y_limits = (-SCREEN_HEIGHT, 0)

        while self.platforms_count(y_limits) < self.platforms_density:
            platform = RegularPlatform()
            platform.generate_position(self.platform_group, y_limits=y_limits)
            platform.add(
                self.platform_group, self.dynamic_group, self.base_group
            )

    def platforms_count(self, y_limits):
        return len(tuple(filter(
            lambda sprite: sprite.rect.top in range(*y_limits),
            self.platform_group.sprites()
        )))

    def fill_marks_group(self):
        for score in data_base.get_all_scores():
            mark = Mark(self.dynamic_group, self.marks_group)
            mark.set_position(score)


game_view = GameView()

# Test
if __name__ == '__main__':
    game_view.run()
