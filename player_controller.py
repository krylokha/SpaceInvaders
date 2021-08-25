from __future__ import annotations
from controller import Controller
import screen as sc
from spaceship import Spaceship
import pygame


class PlayerController(Controller):
    spaceship: Spaceship

    def __init__(self, screen: sc.Screen) -> None:
        self.spaceship = Spaceship()
        self.screen = screen
        self.screen.spawn(self.spaceship)

    def handle_input(self, event: "Pygame event"):
        if event.type == pygame.KEYDOWN:
            if pygame.KEYDOWN == (pygame.K_RIGHT or pygame.K_d):
                self.spaceship.move_right()
            elif pygame.KEYDOWN == (pygame.K_LEFT or pygame.K_a):
                self.spaceship.move_left()
            elif pygame.KEYDOWN == pygame.K_SPACE:
                self.spaceship.fire_the_bullet()

    def process(self, delta_time: int):
        self.spaceship.move(self.spaceship.get_x() + self.spaceship.get_direction() * self.spaceship.get_speed() * delta_time,
                            self.spaceship.get_y())
