from __future__ import annotations
from abc_screen import Screen
from game import Game
import pygame


class EndScreen(Screen):
    game: Game

    def __init__(self, game: Game):
        self.text = pygame.font.Font('Bungee-Regular.ttf', 36)
        self.textSurfaceObj = self.text.render('GAME OVER', True, (128, 128, 0))
        # super().__init__(game)

    def handle_input(self, event: "Pygame event"):
        pass

    def render(self, surface):
        surface.blit(self.textSurfaceObj, (300, 400))

    def process(self, delta_time):
        pass
