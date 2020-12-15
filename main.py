import pygame

SIZE_WINDOW = 300, 500


def main():
    pygame.init()

    screen = pygame.display.set_mode(SIZE_WINDOW)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # do someone
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
