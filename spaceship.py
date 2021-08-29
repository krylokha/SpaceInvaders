from __future__ import annotations
from game_object import GameObject
import pygame
from bullet import Bullet
import screen


class Spaceship(GameObject):
    COLOR = (255, 255, 255)
    HEIGHT = 20
    WIDTH = 20

    def __init__(self) -> None:
        self.x = 400
        self.y = 550
        self.x_direction = 0
        self.speed = 0.5
        self.bullet_appeared = False

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

    def move_right(self):
        self.x_direction = 1

    def move_left(self):
        self.x_direction = -1

    def fire(self, game_screen: screen.Screen):
        bullet = Bullet(self.x, self.y)
        game_screen.spawn(bullet)
        game_screen.add_bullet(bullet)
        # self.bullet_appeared = True

    def render(self, surface):
        pygame.draw.rect(surface, Spaceship.COLOR, pygame.Rect(self.x, self.y, Spaceship.HEIGHT, Spaceship.WIDTH))
