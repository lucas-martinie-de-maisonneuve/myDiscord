import pygame
from source.pygame.element import Element
from source.pygame.screen import Screen
from data.request import Discord_Manager

class Inscription(Element, Screen):
    def __init__(self):
        Screen.__init__(self)
        Element.__init__(self)
        self.inscription_running = True
        self.manager = Discord_Manager()
        self.username = "Username"
        self.email = "Email address"
        self.surname = "Surname"
        self.name = "Name"
        self.password = "Password"
        self.entry = 0
        self.photo = 0
        self.profil_hovered = None
        pygame.init()

    def form(self):
        # Display rectangles
        self.Window.fill(self.white)
        self.rect_full(self.grey3, 600, 355, 600, 580, 10)
        self.rect_border(self.grey2, 600, 355, 600, 580, 2, 10)

        # username
        self.username_rect = self.rect_full(self.grey2, 600, 240, 400, 40, 5) 
        self.button_hover("username", 600, 240, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.username, self.font2, self.white, 15, 4, 5)

        # Email
        self.email_rect = self.rect_full(self.grey2, 600, 300, 400, 40, 5)
        self.button_hover("email", 600, 300, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.email, self.font2, self.white, 15, 4, 5)

        # Surname
        self.surname_rect = self.rect_full(self.grey2, 600, 360, 400, 40, 5)
        self.button_hover("name", 600, 360, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.surname, self.font2, self.white, 15, 4, 5)

        # Name
        self.name_rect = self.rect_full(self.grey2, 600, 420, 400, 40, 5)
        self.button_hover("name", 600, 420, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.name, self.font2, self.white, 15, 4, 5)

        # Password
        self.password_rect = self.rect_full(self.grey2, 600, 480, 400, 40, 5)
        self.button_hover("password", 600, 480, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.password, self.font2, self.white, 15, 4, 5)
        
        # Button Sign Up
        self.sign_up = self.rect_full(self.blue, 600, 560, 350, 50,5)
        self.button_hover("connexion", 600, 560, 350, 50, self.blue, self.blue, self.blue1, self.blue1,"Sign Up", self.font1, self.white, 15, 4, 5)
        
        # Text Or
        self.text_center(self.font1, 12,"OR", self.blue, 600, 600)

        # White lines
        pygame.draw.line(self.Window, self.grey1, (630, 600), (770, 600), 1)
        pygame.draw.line(self.Window, self.grey1, (430, 600), (564, 600), 1)
        
        # Text hover Log In
        sign = (pygame.Rect(580, 620, 45, 13))    
        if self.is_mouse_over_button(sign):
            self.text_center(self.font1, 13, "Log In", self.white, 600, 625)          
        else:
            self.text_center(self.font1, 12, "Log In ", self.white, 600, 625)
            
    def profil_screen(self):
        # Profile pictures
        self.img_center("profil1",380,140,90,65,"new_profil/profil1")
        self.img_center("profil2",530,140,100,80,"new_profil/profil2")
        self.img_center("profil3",680,140,80,60,"new_profil/profil3")
        self.img_center("profil4",830,140,100,90,"new_profil/profil4")
        
    def profil_hover(self):
         # Cercle profile
        self.profil1_cercle = pygame.draw.circle(self.Window, self.black, (380, 140), 50)
        self.profil2_cercle = pygame.draw.circle(self.Window, self.black, (530, 140), 50)
        self.profil3_cercle = pygame.draw.circle(self.Window, self.black, (680, 140), 50)
        self.profil4_cercle = pygame.draw.circle(self.Window, self.black, (830, 140), 50)

        # Hover cercle profile
        self.p_profil1 = self.profil1_cercle
        if self.is_mouse_over_button(self.p_profil1):
            self.profil1_cercle = pygame.draw.circle(self.Window, self.black, (380, 140), 50)
            self.hover_profil1_cercle = pygame.draw.circle(self.Window, self.grey1, (380, 140), 50, width=2) 
        else:
            self.profil1_cercle = pygame.draw.circle(self.Window, self.black, (380, 140), 50)
            self.hover_profil1_cercle = pygame.draw.circle(self.Window, self.grey2, (380, 140), 50, width=2) 
            
        self.p_profil2 = self.profil2_cercle
        if self.is_mouse_over_button(self.p_profil2):
            self.profil2_cercle = pygame.draw.circle(self.Window, self.black, (530, 140), 50)
            self.hover_profil2_cercle = pygame.draw.circle(self.Window, self.grey1, (530, 140), 50, width=2)   
        else:
            self.profil2_cercle = pygame.draw.circle(self.Window, self.black, (530, 140), 50)
            self.hover_profil2_cercle = pygame.draw.circle(self.Window, self.grey2, (530, 140), 50, width=2) 

        self.p_profil3 = self.profil3_cercle
        if self.is_mouse_over_button(self.p_profil3):
            self.profil3_cercle = pygame.draw.circle(self.Window, self.black, (680, 140), 50)
            self.hover_profil3_cercle = pygame.draw.circle(self.Window, self.grey1, (680, 140), 50, width=2)
        else:
            self.profil3_cercle = pygame.draw.circle(self.Window, self.black, (680, 140), 50)
            self.hover_profil3_cercle = pygame.draw.circle(self.Window, self.grey2, (680, 140), 50, width=2)

        self.p_profil4 = self.profil4_cercle
        if self.is_mouse_over_button(self.p_profil4):
            self.profil4_cercle = pygame.draw.circle(self.Window, self.black, (830, 140), 50)
            self.hover_profil4_cercle= pygame.draw.circle(self.Window, self.grey1, (830, 140), 50, width=2) 
        else:
            self.profil4_cercle = pygame.draw.circle(self.Window, self.black, (830, 140), 50)
            self.hover_profil4_cercle= pygame.draw.circle(self.Window, self.grey2, (830, 140), 50, width=2)

    def inscription_run(self):  # sourcery skip: merge-else-if-into-elif
        self.inscription_running = True
        while self.inscription_running:
            self.form()
            self.profil_hover()
            self.profil_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.inscription_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.profil1_cercle.collidepoint(event.pos):
                        self.photo = 1
                        self.profil_hovered = self.profil1_cercle

                    elif self.profil2_cercle.collidepoint(event.pos):
                        self.photo = 2
                        self.profil_hovered = self.profil2_cercle

                    elif self.profil3_cercle.collidepoint(event.pos):
                        self.photo = 3
                        self.profil_hovered = self.profil3_cercle

                    elif self.profil4_cercle.collidepoint(event.pos):
                        self.photo = 4
                        self.profil_hovered = self.profil4_cercle

                    elif self.username_rect.collidepoint(event.pos):
                        self.username = ""
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

                    elif self.sign_up.collidepoint(event.pos):
                        if self.username!="Username" and self.email!="Email address" and self.surname != "Surname" and self.name != "Name" and self.password != "Password" and self.photo != 0:
                            self.manager.add_user(self.surname,self.name,self.username,self.email,self.password,self.photo,2)
                            print("ajouter")
                            
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if self.entry ==1:
                            self.username = self.username[:-1]
                        elif self.entry == 2:
                            self.email = self.email[:-1]
                        elif self.entry == 3:
                            self.surname = self.surname[:-1]
                        elif self.entry == 4:
                            self.name = self.name[:-1]
                        elif self.entry == 5:
                            self.password = self.password[:-1]

                    else:
                        if self.entry == 1:
                            if event.unicode.isalpha() or event.unicode.isdigit():
                                self.username += event.unicode
                            
                        elif self.entry == 2:
                            if event.unicode:
                                self.email = self.email + event.unicode

                        elif self.entry == 3:
                            if event.unicode.isalpha():
                                self.surname = self.surname + event.unicode
                                self.surname = self.surname.capitalize()

                        elif self.entry == 4:
                            if event.unicode.isalpha():
                                self.name = self.name + event.unicode
                                self.name = self.name.capitalize()

                        elif self.entry == 5:
                            if event.unicode:
                                self.password = self.password + event.unicode

            if self.profil_hovered:
                if self.profil_hovered == self.profil1_cercle:
                    self.hover_profil1_cercle = pygame.draw.circle(self.Window, self.blue, (380, 140), 50, width=2)
                    
                elif self.profil_hovered == self.profil2_cercle:
                    self.hover_profil2_cercle = pygame.draw.circle(self.Window, self.blue, (530, 140), 50, width=2)
                    
                elif self.profil_hovered == self.profil3_cercle:
                    self.hover_profil3_cercle = pygame.draw.circle(self.Window, self.blue, (680, 140), 50, width=2)
                    
                elif self.profil_hovered == self.profil4_cercle:
                    self.hover_profil4_cercle = pygame.draw.circle(self.Window, self.blue, (830, 140), 50, width=2)

            self.screen.update()

test = Inscription()
test.inscription_run()