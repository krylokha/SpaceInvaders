from abc import ABC, abstractmethod
from typing import Protocol

class GameObject(Protocol):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def move(self, x: int, y: int):
        pass