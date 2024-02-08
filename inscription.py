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
    def profil_hoover(self):
        self.profil1_cercle = pygame.draw.circle(self.Window, self.black, (380, 150), 50)
        self.profil2_cercle = pygame.draw.circle(self.Window, self.black, (530, 150), 50)
        self.profil3_cercle = pygame.draw.circle(self.Window, self.black, (680, 150), 50)
        self.profil4_cercle = pygame.draw.circle(self.Window, self.black, (830, 150), 50)
        self.p_profil2 = self.profil2_cercle
        if self.is_mouse_over_button(self.p_profil2):
            self.profil2_cercle = pygame.draw.circle(self.Window, self.black, (530, 150), 50)
            self.hoover_profil2_cercle = pygame.draw.circle(self.Window, self.grey1, (530, 150), 50, width=2) 
        else:
            self.profil2_cercle = pygame.draw.circle(self.Window, self.black, (530, 150), 50)
            self.hoover_profil2_cercle = pygame.draw.circle(self.Window, self.grey2, (530, 150), 50, width=2) 
        
        self.p_profil3 = self.profil3_cercle
        if self.is_mouse_over_button(self.p_profil3):
            self.profil3_cercle = pygame.draw.circle(self.Window, self.black, (680, 150), 50)
            self.hoover_profil3_cercle = pygame.draw.circle(self.Window, self.grey1, (680, 150), 50, width=2)
        else:
            self.profil3_cercle = pygame.draw.circle(self.Window, self.black, (680, 150), 50)
            self.hoover_profil3_cercle = pygame.draw.circle(self.Window, self.grey2, (680, 150), 50, width=2)

        self.p_profil4 = self.profil4_cercle
        if self.is_mouse_over_button(self.p_profil4):
            self.profil4_cercle = pygame.draw.circle(self.Window, self.black, (830, 150), 50)
            self.hoover_profil4_cercle= pygame.draw.circle(self.Window, self.grey1, (830, 150), 50, width=2) 
        else:
            self.profil4_cercle = pygame.draw.circle(self.Window, self.black, (830, 150), 50)
            self.hoover_profil4_cercle= pygame.draw.circle(self.Window, self.grey2, (830, 150), 50, width=2) 

        self.p_profil1 = self.profil1_cercle
        if self.is_mouse_over_button(self.p_profil1):
            self.profil1_cercle = pygame.draw.circle(self.Window, self.black, (380, 150), 50)
            self.hoover_profil1_cercle = pygame.draw.circle(self.Window, self.grey1, (380, 150), 50, width=2) 
        else:
            self.profil1_cercle = pygame.draw.circle(self.Window, self.black, (380, 150), 50)
            self.hoover_profil1_cercle = pygame.draw.circle(self.Window, self.grey2, (380, 150), 50, width=2) 
    def inscription_run(self):
        running = True
        while running:
            self.form()
            self.profil_hoover()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.update()

test = Inscription()
test.inscription_run()
