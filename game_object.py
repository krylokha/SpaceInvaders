from abc import ABC, abstractmethod
from typing import Protocol


class GameObject(Protocol):
    @abstractmethod
    def render(self, window):
        pass

    @abstractmethod
    def move(self, x: int, y: int):
        pass

    @abstractmethod
    def get_x(self):
        pass

    @abstractmethod
    def get_y(self):
        pass

    @abstractmethod
    def get_rect(self):
        pass

    def check_crossing(self, game_object):
        first_rect = self.get_rect()
        second_rect = game_object.get_rect()
        return first_rect.colliderect(second_rect)
