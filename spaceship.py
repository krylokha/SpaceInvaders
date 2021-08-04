from game_object import GameObject
import pygame

class Spaceship(GameObject):
    def __init__(self, x: int, y: int, height: int, width: int, r: int, g: int, b: int) -> None:
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.border = 0
        self.color = (r, g, b)
        self.x_direction = 0
        self.speed = 0.5

    def move(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.x_direction = 1
            elif event.key == pygame.K_a:
                self.x_direction = -1


    def render(self):
        pass
