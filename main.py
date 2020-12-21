import pygame
from constants import *
from Doodler import Doodler


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Doodle Jump')
        icon = pygame.image.load('data/img/doodler/right.png')
        pygame.display.set_icon(icon)

    def run(self):
        doodler_group = pygame.sprite.Group()
        doodler = Doodler(doodler_group)

        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT]:
                        doodler.step_left()
                    if keys[pygame.K_RIGHT]:
                        doodler.step_right()

            self.screen.fill('white')
            doodler_group.draw(self.screen)
            doodler_group.update()
            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()


if __name__ == '__main__':
    App().run()
