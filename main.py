import pygame
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

        self.clock = pygame.time.Clock()
        self.main_group = pygame.sprite.Group()
        self.doodler_group = pygame.sprite.Group()
        Doodler(self.doodler_group, self.main_group)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill('white')
            self.main_group.update()
            self.main_group.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()


app = App()
if __name__ == '__main__':
    app.run()
