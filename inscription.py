import pygame
from source.pygame.element import Element
from source.pygame.screen import Screen

class Inscription(Element,Screen):
    def __init__(self):
        Screen.__init__(self)
        Element.__init__(self)
        self.inscription_running = True
        pygame.init() 
        
    def form(self):
        self.Window.fill(self.white)
        self.rect_full(self.grey3, 600, 355, 600, 580, 5)
        self.rect_border(self.grey2, 600, 355, 600, 580, 2, 5)
    
    def inscription_run(self):
        running = True
        while running:
            self.form()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.update()

test = Inscription()
test.inscription_run()
