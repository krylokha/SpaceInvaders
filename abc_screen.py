from __future__ import annotations
from abc import ABC, abstractmethod

class Screen(ABC):
    @abstractmethod
    def handle_input(self, event: "Pygame event"):
        pass