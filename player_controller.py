from controller import Controller
from screen import Screen
from spaceship import Spaceship
import pygame

class PlayerController(Controller):
    spaceship: Spaceship

    def __init__(self, screen: Screen) -> None:
        self.spaceship = Spaceship()
        self.screen = screen
        """Уточни, верно ли поняла"""
        self.screen.spawn(self.spaceship)
    
    def handle_input(self, event: "Pygame event"):
        if event.type == pygame.KEYDOWN:
            if pygame.KEYDOWN == (pygame.K_RIGHT or pygame.K_d):
                return 1
            elif pygame.KEYDOWN == (pygame.K_LEFT or pygame.K_a):
                return 2
        return 0

    def process(self, delta_time: int, event):
        if self.handle_input(event) == 1:
            direction = self.spaceship.move_right()
        elif self.handle_input(event) == 2:
            direction = self.spaceship.move_left()
        self.spaceship.x += direction * self.spaceship.speed * delta_time """Или self.spaceship.get_x(), запуталась, спроси"""