import pygame


SCREEN_WIDTH = 400  # px
SCREEN_HEIGHT = 650  # px
FPS = 60  # 1 / s
SCREEN_HALF_WIDTH = SCREEN_WIDTH // 2  # px
SCREEN_HALF_HEIGHT = SCREEN_HEIGHT // 2  # px

DOODLER_VELOCITY_X = 7  # скорость дудлера по оси X, px * FPS
GRAVITATION_ACCELERATION = 0.4  # ускорение свободного падения, px * FPS / s
JUMP_START_VELOCITY = -13  # скорость дудлера на начало прыжка, px / s
JUMP_HEIGHT = 230  # высота обычного прыжка дудлера, px

# ----- константы событий ----- #
PLAY_BUTTON_PRESSED = pygame.USEREVENT + 1
# /----- константы событий ----- #
