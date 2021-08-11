from game_object import GameObject
import pygame

class Spaceship(GameObject):
    def __init__(self, r: int, g: int, b: int) -> None:
        self.x = 400
        self.y = 550
        self.height = 20
        self.width = 30
        self.border = 0
        self.color = (r, g, b)
        self.x_direction = 0
        self.speed = 0.5

    def move(self, x: int, y: int):
        # всё (кнопки) это в контроллере прописываем
        # if pygame.KEYDOWN == pygame.K_d:
        #     self.x_direction = 1
        # elif pygame.KEYDOWN == pygame.K_a:
        #     self.x_direction = -1
        self.x += self.x_direction * self.speed * delta_time

    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.x, self.y, self.height, self.width, self.border)
