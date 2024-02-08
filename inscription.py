import pygame
from source.pygame.element import Element
from source.pygame.screen import Screen

class Inscription(Element,Screen):
    def __init__(self):
        Screen.__init__(self)
        Element.__init__(self)
        self.inscription_running = True
        self.pseudo = "Pseudo"
        self.email = "Email address"
        self.surname = "Surname"
        self.name = "Name"
        self.password = "Password"
        self.entry = 0
        self.photo = 0
        pygame.init() 
        
    def form(self):
        self.Window.fill(self.white)
        self.rect_full(self.grey3, 600, 355, 600, 580, 5)
        self.rect_border(self.grey2, 600, 355, 600, 580, 2, 5)
        # Pseudo
        self.pseudo_rect = self.rect_full(self.grey2, 600, 260, 400, 40, 5) 
        self.button("pseudo", 600, 260, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.pseudo, self.font2, self.white, 15, 4, 5)
        
        # Email
        self.email_rect = self.rect_full(self.grey2, 600, 320, 400, 40, 5)
        self.button("email", 600, 320, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.email, self.font2, self.white, 15, 4, 5)
        
         # Prenom
        self.surname_rect = self.rect_full(self.grey2, 600, 380, 400, 40, 5)
        self.button("name", 600, 380, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.surname, self.font2, self.white, 15, 4, 5)
        
        # Nom
        self.name_rect = self.rect_full(self.grey2, 600, 440, 400, 40, 5)
        self.button("name", 600, 440, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.name, self.font2, self.white, 15, 4, 5)
        
        # Mot De Passe
        self.password_rect = self.rect_full(self.grey2, 600, 500, 400, 40, 5)
        self.button("password", 600, 500, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.password, self.font2, self.white, 15, 4, 5)
        
        self.button("connexion", 600, 580, 350, 50, self.blue, self.blue, self.blue1, self.blue1,"Sign In", self.font1, self.white, 15, 4, 5)
    def profil_screen(self):
        self.img_center("profil1",380,150,90,65,"new_profil/profil1")
        self.img_center("profil2",530,150,100,80,"new_profil/profil2")
        self.img_center("profil3",680,150,80,60,"new_profil/profil3")
        self.img_center("profil4",830,150,100,90,"new_profil/profil4")
    
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
            self.profil_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.profil1_cercle.collidepoint(event.pos):
                        self.photo = 1
                    elif self.profil2_cercle.collidepoint(event.pos):
                        self.photo = 2
                    elif self.profil3_cerclecollidepoint(event.pos):
                        self.photo = 3
                    elif self.profil4_cercle.collidepoint(event.pos):
                        self.photo = 4
                    
                    elif self.pseudo_rect.collidepoint(event.pos):
                        self.pseudo = ""
                        self.entry = 1
                        
                    elif self.email_rect.collidepoint(event.pos):
                        self.email = ""
                        self.entry = 2
                        
                    elif self.surname_rect .collidepoint(event.pos):
                        self.surname = ""
                        self.entry = 3
                        
                    elif self.name_rect.collidepoint(event.pos):
                        self.name = ""
                        self.entry = 4
                        
                    elif self.password_rect.collidepoint(event.pos):
                        self.password = ""
                        self.entry = 5

            self.screen.update()

test = Inscription()
test.inscription_run()