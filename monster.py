import pygame
from game_object import GameObject


class Monster(GameObject):
    R = 0
    G = 255
    B = 0
    COLOR = (R, G, B)
    # RADIUS = 10
    speed = 0.5
    WIDTH = 15
    HEIGHT = 15

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.x_direction = 1

    def move(self, x, y):
        self.x = x
        self.y = y

    def render(self, window):
        # pygame.draw.circle(window, self.COLOR, (self.x, self.y), self.RADIUS)  # лучше сделать прямоугольниками
        rect = self.get_rect()
        pygame.draw.rect(window, self.COLOR, rect)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.HEIGHT, self.WIDTH)
