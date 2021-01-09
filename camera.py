import pygame

from constants import SCREEN_HEIGHT


class Camera:
    def __init__(self):
        """
        Инициализация начального сдвига
        """
        self.dy = 0

    def apply(self, group: pygame.sprite.Group) -> None:
        """
        Сдвигает спрайты в группе
        :param group: pygame.sprite.Group
        :return: None
        """
        for sprite in group:
            sprite.rect.y += self.dy

    def update(self, target: pygame.sprite.Sprite) -> None:
        """
        Позиционирует камеру на объекте target
        :param target: pygame.sprite.Sprite
        :return: None
        """
        target_center_y = target.rect.centery
        if target_center_y < SCREEN_HEIGHT // 2:
            self.dy = SCREEN_HEIGHT // 2 - target_center_y
        else:
            self.dy = 0
