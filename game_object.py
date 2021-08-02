from abc import ABC, abstractmethod
from typing import Protocol

class GameObject(Protocol):
    @abstractmethod
    def render(self):
        pass