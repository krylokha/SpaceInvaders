from __future__ import annotations
from abc_screen import Screen
from ai_controller import AIController
from game import Game
import pygame


class EndScreen(Screen):
    game: Game

    def __init__(self, game: Game):
        self.controller = AIController(self)
        self.game = game
        self.main_text = pygame.font.Font('Bungee-Regular.ttf', 36)
        self.text = pygame.font.Font('Bungee-Regular.ttf', 28)
        self.textSurfaceObj = self.text.render('GAME OVER', True, (200, 128, 0))

    def handle_input(self, event: "Pygame event"):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.stop_game()

    def lose(self) -> str:
        textMessage = self.main_text.render('you lost', True, (200, 128, 0))
        return textMessage

    def win(self) -> str:
        textMessage = self.main_text.render('you won', True, (200, 128, 0))
        return textMessage

    def render(self, surface):
        surface.blit(self.textSurfaceObj, (310, 450))
        if self.controller.has_monsters():
            surface.blit(self.win(), (305, 350))
        else:
            surface.blit(self.lose(), (305, 350))

    def process(self, delta_time):
        pass

    def spawn(self, object):
        pass