from dataclasses import dataclass
from movement.vector2d import Vector
from pygame.draw import circle
import pygame

@dataclass
class Bullet:
    position: Vector
    velocity: Vector
    speed: int = 8

    def draw(self, surface: pygame.Surface):
        circle(surface, (155, 155, 155), (self.position.as_tup()), 8)

    
    def update(self):
        self.position += self.velocity//self.speed