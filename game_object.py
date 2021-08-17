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
