from dataclasses import dataclass, field
import pygame, random, string
from pygame.draw import rect, circle, line
from movement.vector2d import Vector
from bullet import Bullet
from enemy import Enemy
from enum import Enum, auto

from tower_menu import TowerMenu


class Level(Enum):
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()

def create_id():
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    print(x)
    return x 

@dataclass
class Tower:
    position: Vector
    menu: TowerMenu
    radius: int = 16
    damage: int = 1
    range: int = round(radius*2/0.5)
    bullets: list[Bullet] = field(default_factory=list)
    target: str = "first"
    target_index: int = 0
    shot_count: int = 0
    level: Level = Level.ONE
    id: str = create_id()


    def check_collision(self, pos: tuple[int], radius, enemy:Enemy = None):
        if enemy != None:
            return abs((self.position.x-enemy.position.x)**2 + (self.position.y-enemy.position.y)**2) < (self.range+enemy.radius) **2
        posx, posy = pos
        return abs((self.position.x-posx)**2 + (self.position.y-posy)**2) < (self.radius+radius) **2

    def select_target(self):
        match self.target:
            case "first":
                self.target_index = 0
            
            case "last":
                self.target_index = -1

    def shoot(self, enemies):
        try:
            _enemies = []
            enemy = enemies[self.target_index]
            for enemy in enemies:
                if self.check_collision((0,0), 0, enemy=enemy) and self.shot_count == 0:
                    self.shot_count += 1
                    self.bullets.append(Bullet(Vector(self.position.x, self.position.y), Vector(((enemy.position.x + 16 //2) - self.position.x), ((enemy.position.y + 16 //2) - self.position.y)), 10))
                
        except IndexError:
            self.bullets = []
        except ValueError:
            self.bullets = []
            print(_enemies)
        # for enemy in enemies:
        
    def draw(self, surface: pygame.Surface):
        
        circle(surface, (0, 255, 0), (self.position.as_tup()), self.radius)
        circle(surface, (0, 255, 255), (self.position.as_tup()), self.range, 1)
        for bullet in self.bullets:
            bullet.draw(surface)
        
        if self.menu.show:
            self.menu.draw(surface)

    def update(self, win: pygame.Surface, enemies):

        # print(self.bullets)
        try:
            enemy: Enemy = enemies[self.target_index]
            for bullet in self.bullets:
                if bullet.position.x + 8 > win.get_size()[0] or bullet.position.x - 8 < 0 or bullet.position.y + 8 > win.get_size()[1] or bullet.position.y - 8 < 0:
                    self.bullets.remove(bullet)
                    self.shot_count -= 1
                
                if bullet.position.x + 8 > enemy.position.x and bullet.position.x < enemy.position.x + enemy.width and bullet.position.y + 8 > enemy.position.y and bullet.position.y < enemy.position.y + enemy.width:
                    self.bullets.remove(bullet)
                    enemy.damage(self.damage)
                    self.shot_count -= 1
                bullet.update()        
        except IndexError:
            self.bullets = []

    def on_click(self, event: pygame.event.Event, menu_shown):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.check_collision(event.pos, self.radius):
                # menu: TowerMenu = self.menu(["1", "2", "3", "4"])
                # print("hi")
                # print(self, id(self.menu))
                self.menu.show = not self.menu.show

