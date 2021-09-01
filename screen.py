from __future__ import annotations
from abc_screen import Screen
from end_screen import EndScreen
from controller import Controller
from ai_controller import AIController
from player_controller import PlayerController
from bullet_controller import BulletController
from game import Game
from game_object import GameObject
from bullet import Bullet


class MainScreen(Screen):
    game: Game
    game_objects: list[GameObject]
    controllers: list[Controller]

    def __init__(self, game: Game):
        self.game_objects = []
        self.controllers = [AIController(self), PlayerController(self), BulletController(self)]
        self.game = game

    def render(self, window):
        for game_object in self.game_objects:
            game_object.render(window)

    def handle_input(self, event):
        for controller in self.controllers:
            controller.handle_input(event)

    def spawn(self, game_object: GameObject):
        self.game_objects.append(game_object)

    def add_bullet(self, bullet: Bullet):
        self.controllers[2].bullets.append(bullet)

    def banish(self, game_object: GameObject):
        if game_object in self.game_objects:
            self.game_objects.remove(game_object)
        if game_object in self.controllers[0].monsters:
            self.controllers[0].banish(game_object)

    def process(self, delta_time: int):
        for controller in self.controllers:
            controller.process(delta_time)
        if not self.controllers[0].has_monsters():
            self.game.change_screen(EndScreen(self.game))