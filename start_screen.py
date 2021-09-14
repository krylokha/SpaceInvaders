from __future__ import annotations
from abc_screen import Screen
import screen as mainsc
from game import Game
import pygame

class StartScreen(Screen):
    game: Game

    def __init__(self, game: Game):
        self.game = game
        self.main_text = pygame.font.Font('Bungee-Regular.ttf', 36)
        self.text = pygame.font.Font('Bungee-Regular.ttf', 18)
        self.textSurfaceObj1 = self.main_text.render('SPACE INVADERS GAME', True, (200, 128, 0))
        self.textSurfaceObj2 = self.text.render('press enter to start', True, (200, 128, 0))

    def handle_input(self, event: "Pygame event"):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.change_screen(mainsc.MainScreen(self.game))

    def render(self, surface):
        surface.blit(self.textSurfaceObj1, (200, 360))
        surface.blit(self.textSurfaceObj2, (300, 440))

    def process(self, delta_time):
        pass