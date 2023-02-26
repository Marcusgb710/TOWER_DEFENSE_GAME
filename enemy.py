from dataclasses import dataclass
from pygame import Surface
from pygame.draw import rect, circle
from movement.vector2d import Vector


@dataclass
class Enemy:
    position: Vector
    name: str = 'Default tower'
    health: int = 10
    width:int = 16
    radius: int = 16
    velocity: Vector = Vector(1, 0)
    starting_position: int = 0
    
    def damage(self, amount: int = 3):
        self.health -= amount

    def draw(self, surface: Surface):
        rect(surface, (0, 0, 255), (self.position.x, self.position.y, self.width, self.width))
        rect(surface, (0, 255, 155), (self.position.x, self.position.y, self.width, self.width), 1)
        circle(surface, (255, 255, 0), (self.position.x + self.width //2, self.position.y + self.width //2), 16, 1)
    
    def find_direction(self, path_points: list[tuple[int]]):
        #finds direction from the value of elements in a list
        x1, y1 = self.position.as_tup()
        if self.starting_position < len(path_points)-1:
            x2 ,y2 = path_points[self.starting_position]
        else:
            x2 ,y2 = path_points[len(path_points) -1]
        
        direction: str = ""
        if x2 > x1 and y2 == y1:
            direction = 'r'
            self.starting_position += 1
            return direction
        if x2 < x1 and y2 == y1:
            direction = 'l'
            self.starting_position += 1
            return direction
        if y2 > y1 and x2 == x1:
            direction = 'd'
            self.starting_position += 1
            return direction
        if y2 < y1 and x2 == x1:
            direction = 'u'
            self.starting_position += 1
            return direction
        return direction

    def move(self, path_points: list[tuple[int]]):
        #moves enemy
        direction = self.find_direction(path_points)
        
        match direction:
            case 'u':
                self.velocity = Vector(0, -1)
            
            case 'd':
                self.velocity = Vector(0, 1)
            
            case 'l':
                self.velocity = Vector(-1, 0)
            
            case 'r':
                self.velocity = Vector(1, 0)
        self.position += self.velocity

    def update(self, enemies):
        if self.health <= 0:
            enemies.remove(self)
        
            