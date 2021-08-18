from controller import Controller
from game import Game
from game_object import GameObject

class Screen:
    game: Game
    game_objects: list[GameObject]
    controllers: list[Controller]

    def __init__(self, game: Game):
        self.game_objects = []
        # self.controllers = [пишем вручную контроллеры (3 шт)]
        self.game = game

    def render(self):
        for game_object in self.game_objects:
            game_object.render()

    def handle_input(self): 
        # принять и передать event
        for controller in self.controllers:
            controller.handle_input()

    def spawn(self, game_object: GameObject):
        self.game_objects.append(game_object)

    def banish(self):
        pass

    def process(self, delta_time: int):
        # у контроллеров вызываем process