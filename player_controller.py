from __future__ import annotations
from controller import Controller
import screen as sc
from spaceship import Spaceship
import pygame
from game_object import GameObject


class PlayerController(Controller):
    spaceship: Spaceship

    START_X = 0
    EDGE_X = 800  

    def __init__(self, screen: sc.Screen) -> None:
        self.spaceship = Spaceship()
        self.screen = screen
        self.screen.spawn(self.spaceship)

    def handle_input(self, event: "Pygame event"):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.spaceship.move_right()
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.spaceship.move_left()
            elif event.key == pygame.K_SPACE:
                self.spaceship.fire(self.screen)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.spaceship.stop()

    def process(self, delta_time: int):
        if self.spaceship.get_x() + self.spaceship.WIDTH == self.EDGE_X or self.spaceship.get_x() == 0:
            self.spaceship.move(self.spaceship.get_x() - self.spaceship.get_direction() * self.spaceship.get_speed() * delta_time,
                            self.spaceship.get_y())
        else:
            self.spaceship.move(self.spaceship.get_x() + self.spaceship.get_direction() * self.spaceship.get_speed() * delta_time,
                            self.spaceship.get_y())
        
# создаем пулю, спавним, пихаем в массив пуль. буллет_контроллер на то и рассчитан