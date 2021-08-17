import pygame
from controller import Controller
from screen import Screen
from monster import Monster


class AIController(Controller):
    START_X = 100  # координата х, с которой монстр начинает движение
    EDGE_X = 800  # координата х, достигая которую монстры увеличивают координату у (переходят на другой ряд, ближе к игроку)
    EDGE_Y = 600  # координата у, достигая которую игрок умирает (если я правильно поняла суть игры)
    DELTA = 50  # на сколько увеличивается координата у при переходе монстра на другой ряд
    MONSTERS_NUM = 30

    def __init__(self, monsters: list, screen: Screen):
        self.monsters = monsters
        self.screen = screen

    def create_monsters(self):
        x = 0
        y = 0
        for i in range(self.MONSTERS_NUM):
            new_monster = Monster(x, y)
            self.monsters.append(new_monster)
            self.screen.spawn(new_monster)

    def handle_input(self):
        pass

    def process(self, delta_time):
        for monster in self.monsters:
            if monster.x + monster.RADIUS >= self.EDGE_X:
                monster.x_direction = -1
                monster.move(monster.x, monster.y + self.DELTA)
            elif monster.x - monster.RADIUS <= self.START_X:
                monster.x_direction = 1
                monster.move(monster.x, monster.y + self.DELTA)
            else:
                monster.move(monster.x + (monster.x_direction * monster.speed), monster.y)

    def die(self):
        pass
