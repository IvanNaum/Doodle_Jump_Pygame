import pygame

from platforms import RegularPlatform
from constants import *
from doodler import Doodler
from camera import Camera


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
        for i in range(10):
            RegularPlatform(self.platform_group, self.main_group)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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

        pygame.quit()


app = App()
if __name__ == '__main__':
    app.run()
