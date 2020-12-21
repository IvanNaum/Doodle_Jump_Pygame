import pygame


class Doodler(pygame.sprite.Sprite):
    right_image = pygame.image.load('data/img/doodler/right.png')
    left_image = pygame.image.load('data/img/doodler/left.png')

    def __init__(self, *groups):
        super(Doodler, self).__init__(*groups)

        self.image = self.right_image
        self.rect = self.image.get_rect()

        self.y_speed = 10

    def update(self, height, width):
        if self.rect.bottom >= height:
            self.y_speed = -10

        self.y_speed += 15 / 60

        self.rect.top += self.y_speed
        if self.rect.left >= width:
            self.rect.left = 0
        if self.rect.right <= 0:
            self.rect.right = width

    def step_right(self, speed: int):
        self.rect.left += speed + 16
        self.image = self.right_image

    def step_left(self, speed: int):
        self.rect.left -= speed + 16
        self.image = self.left_image
