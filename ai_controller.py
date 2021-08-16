import pygame
from controller import Controller


class AIController(Controller):
    START_X = 100  # координата х, с которой монстр начинает движение
    EDGE_X = 800  # координата х, достигая которую монстры увеличивают координату у (переходят на другой ряд, ближе к игроку)
    EDGE_Y = 600  # координата у, достигая которую игрок умирает (если я правильно поняла суть игры)
    DELTA = 50  # на сколько увеличивается координата у при переходе монстра на другой ряд

    def __init__(self, monsters: list):
        self.monsters = monsters
        self.previous_time = 0

    def handle_input(self):
        pass

    def process(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.previous_time
        self.previous_time = current_time
        self.move()

    def move(self):
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
