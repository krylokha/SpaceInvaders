from player_controller import PlayerController
import pygame
from screen import Screen

class Game:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800

    screen: Screen

    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))
        self.is_running = False

    def run(self):
        pass

    def change_screen(self):
        pass

    def stop(self):
        pass

    def handle_events(self):
        pass

    def process(self):
        pass

if __name__ == "__main__":
    game = Game()
    game.run()    