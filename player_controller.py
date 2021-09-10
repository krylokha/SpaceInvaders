from __future__ import annotations
from controller import Controller
import screen as mainsc
from spaceship import Spaceship
from ai_controller import AIController
import pygame


class PlayerController(Controller):
    spaceship: Spaceship

    START_X = 0
    EDGE_X = 800

    def __init__(self, screen: mainsc.MainScreen) -> None:
        self.spaceship = Spaceship()
        self.screen = screen
        self.screen.spawn(self.spaceship)

    def handle_input(self, event: "Pygame event"):
        if event.type == pygame.KEYDOWN:
            if not self.check_edges():
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
        for game_object in self.screen.game_objects:
            if self.spaceship.check_crossing(game_object):
                pass
        self.check_edges()
        self.spaceship.move(
            self.spaceship.get_x() + self.spaceship.get_direction() * self.spaceship.get_speed() * delta_time,
            self.spaceship.get_y())

    def check_edges(self):
<<<<<<< HEAD
        return self.spaceship.get_x() + self.spaceship.WIDTH == PlayerController.EDGE_X or self.spaceship.get_x() == PlayerController.START_X
=======
        if (self.spaceship.get_x() + self.spaceship.WIDTH >= PlayerController.EDGE_X and self.spaceship.x_direction == 1) or (self.spaceship.get_x() <= PlayerController.START_X and self.spaceship.x_direction == -1):
            self.spaceship.stop()
            return True
        return False
>>>>>>> 45d7088cb61c5c1299a907d5a5acad91a9d1eb36
