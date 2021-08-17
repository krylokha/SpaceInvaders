from abc import ABC, abstractmethod

class Controller(ABC):
    @abstractmethod
    def handle_input(self):
        pass

    @abstractmethod
    def process(self, delta_time):
        pass