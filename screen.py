from controller import Controller
from game import Game
from game_object import GameObject


class Screen:
    game: Game
    game_objects: list[GameObject]
    controllers: list[Controller]

    def __init__(self, game: Game):
        self.game_objects = []
        self.controllers = []
        self.game = game

    def render(self):
        for game_object in self.game_objects:
            game_object.render()

    def handle_input(self):
        for controller in self.controllers:
            controller.handle_input()

    def spawn(self, game_object: GameObject):
        self.game_objects.append(game_object)

    def remove(self, game_object: GameObject):
        pass

    def process(self, delta_time: int):
        for controller in self.controllers:
            controller.process(delta_time)
