from controller import Controller
from game import Game
from spaceship import Spaceship
import pygame

class PlayerController(Controller):
    spaceship: Spaceship

    def __init__(self) -> None:
        self.spaceship = Spaceship()
    
    def handle_input(self):
        pass

    def process(self, delta_time: int):
        if pygame.KEYDOWN == pygame.K_d or pygame.KEYDOWN == pygame.K_RIGHT:
           self.spaceship.x_direction = 1
        elif pygame.KEYDOWN == pygame.K_a or pygame.KEYDOWN == pygame.K_LEFT:
            self.spaceship.x_direction = -1
        self.spaceship.x += self.spaceship.x_direction * self.spaceship.speed * delta_time
        return self.spaceship.x
        # delta_time !!! ask