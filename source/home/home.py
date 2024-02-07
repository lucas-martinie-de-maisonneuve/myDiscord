import pygame
from source.pygame.element import Element

class Home():
    
    def __init__(Element):
        self.element = Element()

        pygame.init()

        fenetre = pygame.display.set_mode((640, 480))
    

        home_run = True
        while home_run :
            for event in pygame.event.get():
                if event.type == QUIT:
                        home_run = False

            

            pygame.quit()
