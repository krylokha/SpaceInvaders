from __future__ import annotations
from abc import ABC, abstractmethod
from game import Game

class Screen(ABC):
    game: Game

    def __init__(self, game: Game) -> None:
        self.game = game

    @abstractmethod
    def handle_input(self, event: "Pygame event"):
        pass

    def stop_game(self):
        self.game.stop()

    def change_screen(self, screen):
        self.game.change_screen(screen)