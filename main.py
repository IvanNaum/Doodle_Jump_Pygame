import sys

import pygame

from camera import Camera
from constants import *
from doodler import Doodler
from platforms import RegularPlatform


def terminate():
    pygame.quit()
    sys.exit()


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

    # Функция для рисования текста на self.screen
    def draw_text(self, text, pos: tuple = (0, 0), color=(0, 0, 0), size: int = 50,
                  border: bool = False, center: bool = False,
                  border_color=(0, 0, 0), border_width=3,
                  margin_left=5, margin_top=5) -> pygame.Rect:
        font = pygame.font.Font(None, size)

        text_x, text_y = pos
        text = font.render(text, True, color)

        text_h = text.get_height()
        text_w = text.get_width()
        if center:
            text_x, text_y = text_x - text.get_width() // 2, text_y - text.get_height()

        self.screen.blit(text, (text_x, text_y))

        if center:
            rect = pygame.Rect(
                (pos[0] - margin_left - text_w // 2, pos[1] - margin_top - text_h),
                (text_w + margin_left * 2, text_h + margin_top * 2))
        else:
            rect = pygame.Rect((pos[0] - margin_left, pos[1] - margin_top),
                               (text_w + margin_left * 2, text_h + margin_top * 2))

        if border:
            pygame.draw.rect(self.screen, border_color, rect, border_width)

        return rect

    def start_screen(self):
        while True:
            self.screen.blit(self.background, (0, 0))
            start_btn = self.draw_text('Старт', pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                                       border=True, center=True, border_width=2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_btn.collidepoint(*event.pos):
                        return

            pygame.display.flip()

    def end_screen(self):
        while True:
            self.screen.blit(self.background, (0, 0))
            start_btn = self.draw_text('Заново',
                                       pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                                       border=True, center=True, border_width=2, size=40)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_btn.collidepoint(*event.pos):
                        return

            pygame.display.flip()

    def run(self):
        # show start screen
        self.start_screen()

        # основной цикл
        while True:

            # ---- генерация платформ ----
            rect = pygame.Rect((0, 0), RegularPlatform.image.get_size())
            rect.centerx = SCREEN_HALF_WIDTH
            rect.bottom = SCREEN_HEIGHT - 50
            RegularPlatform(
                rect, self.platform_group, self.main_group
            )

            rect2 = rect.copy()
            rect2.top -= JUMP_HEIGHT
            RegularPlatform(
                rect2, self.platform_group, self.main_group
            )
            # ----------------------------

            running = True
            SCORE = 0
            self.doodler.reset()
            while running:  # цикл игры
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()

                if self.doodler.check_fall():
                    pygame.mixer.music.load('data/sounds/fall_down.mp3')
                    pygame.mixer.music.play()

                if self.doodler.rect.top >= SCREEN_HEIGHT:
                    running = False

                self.screen.blit(self.background, (0, 0))

                self.doodler.update(self.platform_group)
                self.platform_group.update()

                self.main_group.draw(self.screen)
                self.doodler_group.draw(self.screen)  # перемещаем дудлера на передний план

                self.camera.update(self.doodler)
                self.camera.apply(self.main_group)

                SCORE += self.camera.dy
                self.draw_text(str(SCORE), (10, 10), size=30)

                pygame.display.flip()
                self.clock.tick(FPS)



            # kill all platform
            [i.kill() for i in self.platform_group]

            # show end screen
            self.end_screen()

        terminate()


if __name__ == '__main__':
    app = App()
    app.run()
