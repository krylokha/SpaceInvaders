from abc import ABC, abstractmethod

class Controller(ABC):
    @abstractmethod
    def handle_event(self):
        pass

    @abstractmethod
    def process(self):
        pass