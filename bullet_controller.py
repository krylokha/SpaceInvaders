from __future__ import annotations
from controller import Controller
import screen as sc
from bullet import Bullet


class BulletController(Controller):
    def __init__(self, screen: sc.Screen):
        self.bullets = []
        self.screen = screen

    def create_bullet(self, x, y):
        bullet = Bullet(x, y)
        self.bullets.append(bullet)

    def handle_input(self, event: "Python event"):
        pass

    def process(self, delta_time):
        for bullet in self.bullets:
            bullet.move(bullet.x, bullet.y + (-1 * bullet.speed * delta_time))
            for game_obj in self.screen.game_objects:
                if game_obj.get_x() == bullet.x and game_obj.get_y() == bullet.y and game_obj is not bullet: # см класс game_object
                    self.screen.banish(bullet) # добавить в banish удаление из контроллера
                    self.bullets.remove(bullet)
                    self.screen.banish(game_obj)

