import pygame

from constants import *


class Doodler(pygame.sprite.Sprite):
    right_image = pygame.image.load('data/img/doodler/right.png')
    left_image = pygame.image.load('data/img/doodler/left.png')

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = self.right_image
        self.rect = self.image.get_rect()

        # текущая скорость по оси Y
        self.cur_vy = JUMP_START_VELOCITY
        self.rect.center = SCREEN_HALF_WIDTH, SCREEN_HEIGHT  # начальное положение

        self.fall = False

    def update(self, platform_group) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.step_left()
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.step_right()

        if self.cur_vy >= 0:
            sprite = self.collide_any(platform_group)
            if sprite:
                # небольшая регулировка положения дудлера,
                # если он оказывается чуть ниже платформы
                self.rect.bottom = sprite.rect.top
                self.jump()

        self.cur_vy += GRAVITATION_ACCELERATION / FPS
        self.rect.top += self.cur_vy

    def collide_any(self, *groups) -> pygame.sprite.Sprite:
        """
        Проверяет пересечение дудлера с группами спрайтов
        :param groups: группы спрайтов
        :return: pygame.sprite.Sprite or None
        """
        # проверяет пересечение дудлера с группами спрайтов без учёта носа
        rect = pygame.Rect(
            (self.rect.left + self.rect.width // 4,
             self.rect.top + self.rect.height // 6 * 5),
            (self.rect.width // 4 * 2, self.rect.height // 6 * 2)
        )
        for group in groups:
            for sprite in group:
                if rect.colliderect(sprite.rect):
                    return sprite  # возвращаем спрайт, с которым было пересечение

    def check_fall(self) -> bool:
        if self.rect.bottom >= SCREEN_HEIGHT and self.cur_vy > 0 and not self.fall:
            self.fall = True
            return True
        return False

    def jump(self) -> None:
        self.cur_vy = JUMP_START_VELOCITY
        # загрузка музыки
        pygame.mixer.music.load('data/sounds/jump.mp3')
        # воспроизведение
        pygame.mixer.music.play()

    def step_right(self) -> None:
        self.rect.left += DOODLER_VELOCITY_X
        if self.rect.left >= SCREEN_WIDTH:
            self.rect.left = 0
        self.image = self.right_image

    def step_left(self) -> None:
        self.rect.left -= DOODLER_VELOCITY_X
        if self.rect.right <= 0:
            self.rect.right = SCREEN_WIDTH
        self.image = self.left_image
