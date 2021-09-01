from __future__ import annotations
import pygame
from controller import Controller
import screen as sc
from monster import Monster
from game_object import GameObject


class AIController(Controller):
    START_X = 50  # координата х, с которой монстр начинает движение
    EDGE_X = 800  # координата х, достигая которую монстры увеличивают координату у (переходят на другой ряд, ближе к игроку)
    EDGE_Y = 600  # координата у, достигая которую игрок умирает (если я правильно поняла суть игры)
    DELTA = 50  # на сколько увеличивается координата у при переходе монстра на другой ряд
    MONSTERS_NUM = 25

    def __init__(self, screen: sc.Screen):
        self.monsters = []
        self.screen = screen
        self.create_monsters()

    def create_monsters(self):
        x = 50
        y = 50
        for i in range(5):
            for j in range(AIController.MONSTERS_NUM // 5):
                new_monster = Monster(x, y)
                self.monsters.append(new_monster)
                self.screen.spawn(new_monster)
                x += 50
            x = 50
            y += 50

    def handle_input(self, event: "Python event"):
        pass

    def process(self, delta_time):
        flag = False
        for monster in self.monsters:
            monster.move(monster.get_x() + (monster.x_direction * monster.speed * delta_time), monster.get_y())
            if monster.get_x() + monster.WIDTH >= self.EDGE_X:
                # monster.x_direction = -1
                flag = True
                # monster.move(monster.get_x() + (monster.x_direction * monster.speed * delta_time),
                #              monster.get_y() + self.DELTA)
            elif monster.get_x() < self.START_X:
                # monster.x_direction = 1
                flag = True
                # monster.move(monster.get_x() + (monster.x_direction * monster.speed * delta_time),
                #              monster.get_y() + self.DELTA)
            # else:
            #     monster.move(monster.get_x() + (monster.x_direction * monster.speed * delta_time), monster.get_y())
        if flag:
            for monster in self.monsters:
                monster.x_direction *= -1
                monster.move(monster.get_x() + (monster.x_direction * monster.speed * delta_time),
                             monster.get_y() + self.DELTA)

    def banish(self, game_object: GameObject):
        if game_object in self.monsters:
            self.monsters.remove(game_object)

    def get_monsters(self):
        return self.monsters

    def has_monsters(self):
        return len(self.monsters) != 0