from controller import Controller
from screen import Screen
from spaceship import Spaceship
import pygame
from game_object import GameObject


class PlayerController(Controller):
    spaceship: Spaceship

    def __init__(self, screen: Screen) -> None:
        self.spaceship = Spaceship()
        self.screen = screen
        self.screen.spawn(self.spaceship)

    def handle_input(self, event: "Pygame event"):
        if event.type == pygame.KEYDOWN:
            if pygame.KEYDOWN == (pygame.K_RIGHT or pygame.K_d):
                self.spaceship.move_right()
            elif pygame.KEYDOWN == (pygame.K_LEFT or pygame.K_a):
                self.spaceship.move_left()

    def process(self, delta_time: int):
        self.spaceship.move(self.spaceship.get_x() + self.spaceship.get_direction() * self.spaceship.get_speed() * delta_time,
                            self.spaceship.get_y())

