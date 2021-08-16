import pygame
from game_object import GameObject
from bullet import Bullet


class Monster(GameObject):
    R = 0
    G = 0
    B = 0
    COLOR = (R, G, B)
    RADIUS = 10
    speed = 0.5

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.x_direction = 1

    def move(self, x, y):
        self.x = x
        self.y = y

    def die(self, bullet: Bullet):
        if bullet.x == self.x and bullet.y == self.y:
            bullet.is_died = True
            return True
        else:
            return False

    def render(self, window):
        pygame.draw.circle(window, self.COLOR, (self.x, self.y), self.RADIUS)
