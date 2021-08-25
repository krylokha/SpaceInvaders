from __future__ import annotations
from abc import ABC, abstractmethod

class Controller(ABC):
    @abstractmethod
    def handle_input(self, event):
        pass

    @abstractmethod
    def process(self, delta_time):
        pass