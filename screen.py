import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# экран используется как глобальный объект проекта, поэтому вынесен в отдельный модуль
