from game_object import GameObject
import pygame

class Spaceship(GameObject):
    # дополнительный метод, который (... пропуск)
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
        # player_controller - экземпляр
        # self.x = PlayerController.process(Game.process()) убери вообще
        self.x = x

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def move_right(self):
        self.x_direction = 1
        return self.x_direction

    def move_left(self):
        self.x_direction = -1
        return self.x_direction

    def render(self, surface):
        pygame.draw.rect(surface, self.COLOR, self.x, self.y, self.HEIGHT, self.WIDTH, self.BORDER)
