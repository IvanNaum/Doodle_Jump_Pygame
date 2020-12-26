import pygame
from constants import *


class Doodler(pygame.sprite.Sprite):
    right_image = pygame.image.load('data/img/doodler/right.png')
    left_image = pygame.image.load('data/img/doodler/left.png')
    VY0 = -15  # начальная скорость по оси Y при отскоке, px/s
    AY = 25  # ускорение по оси Y, px/s²
    VX = 5  # постоянная скорость по оси X, px/s

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = self.right_image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.cur_vy = self.VY0  # текущая скорость по оси Y

        # Начальный вылет
        self.rect.topleft = SCREEN_HALF_WIDTH - self.rect.centerx, SCREEN_HEIGHT

    def update(self, platform_group):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.step_left()
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.step_right()

        if self.cur_vy >= 0:
            sprite = self.collide_any(platform_group)
            if sprite:
                self.cur_vy = self.VY0
                # небольшая регулировка положения дудлера,
                # если он оказывается чуть ниже платформы
                self.rect.bottom = sprite.rect.top

        self.cur_vy += self.AY / FPS
        self.rect.top += self.cur_vy

    def collide_any(self, *groups):
        """
        Проверяет пересечение дудлера с группами спрайтов
        :param groups: группы спрайтов
        :return: pygame.sprite.Sprite or None
        """
        # Проверяет пересечение дудлера с группами спрайтов без учёта носа
        rect = pygame.Rect(
            (self.rect.left + self.rect.width // 4,
             self.rect.top + self.rect.height // 6 * 5),
            (self.rect.width // 4 * 2, self.rect.height // 6 * 2)
        )
        for group in groups:
            for sprite in group:
                if rect.colliderect(sprite.rect):
                    return sprite  # возвращаем спрайт, с которым было пересечение

    def step_right(self):
        self.rect.left += self.VX
        if self.rect.left >= SCREEN_WIDTH:
            self.rect.left = 0
        self.image = self.right_image

    def step_left(self):
        self.rect.left -= self.VX
        if self.rect.right <= 0:
            self.rect.right = SCREEN_WIDTH
        self.image = self.left_image
