import pygame

from platforms import RegularPlatform
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

        self.background = pygame.transform.scale(
            pygame.image.load('data/img/background.png'), (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

    def run(self):
        clock = pygame.time.Clock()
        main_group = pygame.sprite.Group()
        doodler_group = pygame.sprite.Group()
        platform_group = pygame.sprite.Group()
        for i in range(10):
            RegularPlatform(platform_group, main_group)
        Doodler(doodler_group, main_group)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.background, (0, 0))
            doodler_group.update(platform_group)
            main_group.draw(self.screen)
            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()


app = App()
if __name__ == '__main__':
    app.run()