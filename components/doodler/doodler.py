from pathlib import Path
import pygame

from constants import (
    GRAVITATION_ACCELERATION, JUMP_START_VELOCITY, SCREEN_HALF_WIDTH, SCREEN_HEIGHT,
    DOODLER_VELOCITY_X, SCREEN_WIDTH
)

dir_path = Path(__file__).parent.absolute()


class Doodler(pygame.sprite.Sprite):
    right_image = pygame.image.load(str(dir_path / 'images/right.png'))
    left_image = pygame.image.load(str(dir_path / 'images/left.png'))

    def __init__(self, *groups):
        super().__init__(*groups)
        self.cur_vy = None

        self.image = self.right_image
        self.rect = self.image.get_rect()

        self.reset()

    def update(self, platform_group, listen_key=True) -> None:
        if listen_key:
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

        self.cur_vy += GRAVITATION_ACCELERATION
        self.rect.top += self.cur_vy

    def reset(self):
        # текущая скорость по оси Y
        self.cur_vy = JUMP_START_VELOCITY
        self.rect.center = SCREEN_HALF_WIDTH, SCREEN_HEIGHT  # начальное положение

    def collide_any(self, *groups) -> pygame.sprite.Sprite:
        """
        Проверяет пересечение дудлера с группами спрайтов
        :param groups: группы спрайтов
        :return: pygame.sprite.Sprite or None
        """
        # проверяет пересечение дудлера с группами спрайтов без учёта носа
        rect = pygame.Rect(
            self.rect.left + self.rect.width // 4,
            self.rect.top + self.rect.height * 5 // 6,
            self.rect.width * 2 // 4,
            self.rect.height * 2 // 6
        )
        for group in groups:
            for sprite in group:
                if rect.colliderect(sprite.rect):
                    return sprite  # возвращаем спрайт, с которым было пересечение

    def jump(self):
        self.cur_vy = JUMP_START_VELOCITY

    def step_right(self) -> None:
        self.rect.left += DOODLER_VELOCITY_X
        self.rect.left %= SCREEN_WIDTH
        self.image = self.right_image

    def step_left(self) -> None:
        self.rect.left -= DOODLER_VELOCITY_X
        self.rect.left %= SCREEN_WIDTH
        self.image = self.left_image

    def fell(self):
        return self.rect.top >= SCREEN_HEIGHT
