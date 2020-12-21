import pygame


class App:
    WIDTH = 400
    HEIGHT = 650

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Doodle Jump')
        icon = pygame.image.load('data/img/doodler/right.png')
        pygame.display.set_icon(icon)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill('white')
            pygame.display.flip()
        pygame.quit()


if __name__ == '__main__':
    App().run()
