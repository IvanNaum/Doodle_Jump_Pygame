import random

import pygame

from Platform import PlatformSprite
from constants import *
from doodler import Doodler


class App:
    def __init__(self):
        # ----- настройка окна ----- #
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Doodle Jump')
        icon = pygame.image.load('data/img/doodler/right.png')
        pygame.display.set_icon(icon)
        # /----- настройка окна ----- #

    def run(self):
        clock = pygame.time.Clock()
        main_group = pygame.sprite.Group()
        doodler_group = pygame.sprite.Group()
        Doodler(doodler_group, main_group)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill('white')
            doodler_group.update()
            main_group.draw(self.screen)
            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()

    def run_test(self):
        clock = pygame.time.Clock()
        main_group = pygame.sprite.Group()
        doodler_group = pygame.sprite.Group()
        platform_group = pygame.sprite.Group()
        for i in range(10):
            pl = PlatformSprite(platform_group, main_group)
            pl.move((random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))
        Doodler(doodler_group, main_group)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill('white')
            doodler_group.update(platform_group)
            main_group.draw(self.screen)
            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()


app = App()
if __name__ == '__main__':
    app.run_test()
