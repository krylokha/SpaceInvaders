from __future__ import annotations
from game import Game
from game_object import GameObject
import pygame
from bullet import Bullet
import screen
import time


class Spaceship(GameObject):
    COLOR = (200, 128, 0)
    HEIGHT = 20
    WIDTH = 20

    def __init__(self) -> None:
        self.x = 390
        self.y = 740
        self.x_direction = 0
        self.speed = 0.2
        self.time = time.time() - 1

    def move(self, x: int, y: int):
        self.x = x

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_rect(self):
        return pygame.Rect(self.x, self.y, Spaceship.HEIGHT, Spaceship.WIDTH)

    def get_speed(self):
        return self.speed

    def get_direction(self):
        return self.x_direction

    def stop(self):
        self.x_direction = 0

    def move_right(self):
        self.x_direction = 1

    def move_left(self):
        self.x_direction = -1

    def fire(self, game_screen: screen.MainScreen):
        if time.time() - self.time >= 1:
            bullet = Bullet(self.x + 1, self.y - 2)
            game_screen.spawn(bullet)
            game_screen.add_bullet(bullet)
            self.time = time.time()

    def render(self, surface):
        pygame.draw.rect(surface, Spaceship.COLOR, pygame.Rect(self.x, self.y, Spaceship.HEIGHT, Spaceship.WIDTH))
