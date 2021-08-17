from controller import Controller
from screen import Screen


class BulletController(Controller):
    def __init__(self, bullets: list, screen: Screen):
        self.bullets = bullets
        self.screen = screen

    def handle_input(self, event):
        pass

    def process(self, delta_time):
        for bullet in self.bullets:
            bullet.move(bullet.x, bullet.y + (-1 * bullet.speed * delta_time))
            for game_obj in self.screen.game_objects:
                if game_obj.get_x() == bullet.x and game_obj.get_y() == bullet.y:
                    self.screen.remove(bullet)
                    self.bullets.remove(bullet)
                    self.screen.remove(game_obj)
