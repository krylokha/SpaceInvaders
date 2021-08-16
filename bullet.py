import pygame
from game_object import GameObject


class Bullet(GameObject):
    speed = 0.7
    R = 0
    G = 0
    B = 0
    COLOR = (R, G, B)
    HEIGHT = 7
    WIDTH = 5
    is_died = False

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render(self, window):
        pygame.draw.rect(window, self.COLOR, (self.x - 0.5 * self.WIDTH, self.y - 0.5 * self.HEIGHT, self.x + 0.5 * self.WIDTH, self.y + 0.5 * self.HEIGHT))

    def move(self, x, y):
        self.x = x
        self.y = y
        #self.y += -1 * self.speed * delta_time

    def die(self):
        if self.is_died:
            return True
        else:
            return False
