from game_object import GameObject
from player_controller import PlayerController
from game import Game
import pygame

class Spaceship(GameObject):
    COLOR = (255, 255, 255)
    BORDER = 0
    HEIGHT = 20
    WIDTH =20
    
    def __init__(self) -> None:
        self.x = 400
        self.y = 550
        self.x_direction = 0
        self.speed = 0.5

    def move(self, x: int, y: int):
        self.x = PlayerController.process(Game.process())

    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.x, self.y, self.height, self.width, self.border)
