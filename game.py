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
        self.previous_time = 0

    def run(self):
        self.is_running = True
        while self.is_running:
            self.handle_event()
            self.process()
            self.render()

    def change_screen(self, screen: Screen):
        self.screen = screen

    def stop(self):
        self.is_running = False

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
            else:
                self.screen.handle_input(event)

    def process(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.previous_time
        self.previous_time = current_time
        self.screen.process(delta_time)

    def render(self):
        """А как же флип и филл?"""
        self.screen.render(self.window)


if __name__ == "__main__":
    game = Game()
    game.run()
