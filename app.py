import pygame

from views.start_view import start_view


class App:
    def __init__(self):
        pygame.display.set_caption('Doodle Jump')
        icon = pygame.image.load('icon.png')
        pygame.display.set_icon(icon)

    @staticmethod
    def run():
        start_view.run()


if __name__ == '__main__':
    App().run()
