import pygame
from enemy import Enemy
from tower import Tower
import os
from movement.vector2d import Vector
import random

from tower_menu import TowerMenu

pygame.font.init()

WIN_DIM = 1216, 688


WIN = pygame.display.set_mode((WIN_DIM))
pygame.display.set_caption("BTD Clone")

BG = pygame.image.load(os.path.join("assets", "map.png"))

CLOCK = pygame.time.Clock()
FPS: int = 60

FONT = pygame.font.SysFont('comicsans', 10)




# path_points = {
# (242, 333): 'r',
# (242, 189): 'u',
# (457, 189): 'r',
# (457, 354): 'd',
# (741, 354): 'r',
# (741, 242): 'u',
# (949, 242): 'r',
# (949, 409): 'd',
# (1193, 409): 'r'}

path_points = [
    (242, 333),
(242, 189),
(457, 189),
(457, 354),
(741, 354),
(741, 242),
(949, 242),
(949, 409),
(1193, 409),
(1248 + 16, 409)
]
# e = Enemy(Vector(0,333))
towers = []
def spawn_ememies(amount: int = 3):
    return[Enemy(Vector(-50*_, 333)) for _ in range(amount)]

def record_click(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        path_points.append(event.pos)
        print(event.pos)

def can_place_tower(mouse_pos = tuple[int]):
        for _tower in towers:
            tower: Tower = _tower
            if tower.check_collision(mouse_pos, tower.radius):
                return False
        return True

def place_tower(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if can_place_tower(event.pos):
            tower :Tower = Tower(Vector(event.pos[0], event.pos[1]), TowerMenu(["1", "2", "3", "4"]))

            towers.append(tower)


enemies = spawn_ememies(9)

def update():
    global enemies
    if len(enemies) == 0:
        enemies = spawn_ememies(9)


def redraw():
    WIN.blit(BG, (0, 0))

    text = FONT.render(f'FPS: {CLOCK.get_fps()}', 1, (0,0,0))
    WIN.blit(text, (WIN.get_size()[0] - 50, 30))
    for enemy in enemies:
        enemy.draw(WIN)
        enemy.move(path_points)
        enemy.update(enemies)
        

    for tower in towers:
        tower.draw(WIN)
        tower.shoot(enemies)
        tower.update(WIN, enemies)

    pygame.display.update()

def main():
    run = True
    menu_opened: bool = False
    
    while run:
        CLOCK.tick(FPS)
        
        
        redraw()
        update()
        for event in pygame.event.get():

            for tower in towers:
                tower.on_click(event, menu_opened)

            place_tower(event)

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
        
        
                

main()