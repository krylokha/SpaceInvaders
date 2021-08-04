from controller import Controller
from game import Game
from game_object import GameObject

class Screen:
    game: Game
    game_objects: list[GameObject]
    controllers: list[Controller]

    def render(self):
        for game_object in self.game_objects:
            game_object.render()

    def handle_input(self):
        for controller in self.controllers:
            controller.handle_input()

    def spawn(self):
        pass