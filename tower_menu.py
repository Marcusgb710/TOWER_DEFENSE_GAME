from dataclasses import dataclass, field
import pygame, random, string
from pygame.draw import rect
pygame.font.init()


def create_id():
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    print(x)
    return x    

@dataclass
class TowerMenu:
    
    button_menu_names:list[str] = field(default_factory=list)
    button_width: int = 300
    button_height: int = 80
    button_x: int =4
    show: bool = False
    font: pygame.font.Font = pygame.font.SysFont('comicsans', 30)
    id: str = create_id()
    
    



    def draw(self, surface: pygame.Surface):
        starting_x: int = 4
        starting_y: int = 600
        
        for i in self.button_menu_names:
            menu_text: pygame.Surface = self.font.render(f"{i}", 0, (0,0,0))
            rect(surface, (100, 100, 100), (starting_x, starting_y,self.button_width, self.button_height))
            surface.blit(menu_text, ((starting_x+self.button_width//2)-menu_text.get_width()//2, (starting_y+self.button_height//2) - menu_text.get_height()//2))
            starting_x += 302