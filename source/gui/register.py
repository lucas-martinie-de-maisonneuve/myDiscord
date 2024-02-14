import pygame
from source.pygame_manager.element import Element
from source.pygame_manager.screen import Screen
from data.discord_manager import Discord_Manager
from source.pygame_manager.event_handler import Event_handler
from source.pygame_manager.cursor import Cursor
from source.pygame_manager.animation import Animation

class Register(Element, Screen, Event_handler, Cursor, Animation):
    def __init__(self):
        Screen.__init__(self)
        Element.__init__(self)
        Cursor.__init__(self)
        Animation.__init__(self)
        
        self.register_running = False
        self.manager = Discord_Manager()
        self.username = ""
        self.email = ""
        self.surname = ""
        self.name = ""
        self.password = ""
        self.entry = 0
        self.photo = 0
        self.profil_hovered = None
        self.entry = 0
        pygame.init()

    def form(self):

        # Display rectangles
        self.img_background("Background", 600,350,1200,700,"register/background_register")
        self.logo_home(150, 127, 260, 140, 105)
        self.screen_alpha(self.alpha_grey2)
        self.rect_full(self.grey3, 600, 355, 600, 580, 10)
        self.rect_border(self.grey2, 600, 355, 600, 580, 2, 10)

        # Username, address Email, Surname, Name, Password
        # username
        self.username_rect = self.rect_full(self.grey2, 600, 240, 400, 40, 5)
        self.button_hover("username", 600, 240, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.username, self.font2, self.white, 15, 4, 5)
        if self.entry != 1 and self.username == "":
            self.text_center(self.font2, 15, "Username", self.white, 600, 240)

        # Email
        self.email_rect = self.rect_full(self.grey2, 600, 300, 400, 40, 5)
        self.button_hover("email", 600, 300, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.email, self.font2, self.white, 15, 4, 5)
        if self.entry != 2 and self.email == "":
            self.text_center(self.font2, 15, "Email address", self.white, 600, 300)

        # Surname
        self.surname_rect = self.rect_full(self.grey2, 600, 360, 400, 40, 5)
        self.button_hover("Surname", 600, 360, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.surname, self.font2, self.white, 15, 4, 5)
        if self.entry != 3 and self.surname == "":
            self.text_center(self.font2, 15, "Surname", self.white, 600, 360)

        # Name
        self.name_rect = self.rect_full(self.grey2, 600, 420, 400, 40, 5)
        self.button_hover("name", 600, 420, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.name, self.font2, self.white, 15, 4, 5)
        if self.entry != 4 and self.name == "":
            self.text_center(self.font2, 15, "Name", self.white, 600, 420)

        # Password
        self.password_rect = self.rect_full(self.grey2, 600, 480, 400, 40, 5)
        self.button_hover("password", 600, 480, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.password, self.font2, self.white, 15, 4, 5)
        if self.entry != 5 and self.password == "":
            self.text_center(self.font2, 15, "Password", self.white, 600, 480)
        
        # Button Sign Up
        self.sign_up = self.rect_full(self.blue, 600, 560, 350, 50,5)
        self.button_hover("connexion", 600, 560, 350, 50, self.blue, self.blue, self.blue1, self.blue1,"Sign Up", self.font1, self.white, 15, 4, 5)

        # Text Or
        self.text_center(self.font1, 12,"OR", self.blue, 600, 600)

        # White lines
        pygame.draw.line(self.Window, self.grey1, (630, 600), (770, 600), 1)
        pygame.draw.line(self.Window, self.grey1, (430, 600), (564, 600), 1)

        # Text hover Log In
        self.sign = (pygame.Rect(580, 620, 45, 13))
        if self.is_mouse_over_button(self.sign):
            self.text_center(self.font1, 13, "Log In", self.white, 600, 625)
        else:
            self.text_center(self.font1, 12, "Log In ", self.white, 600, 625)
            
    def profil_screen(self):

        # Profil pictures
        self.img_center("profil1",380,140,90,65,"profil/profil1")
        self.img_center("profil2",530,140,100,80,"profil/profil2")
        self.img_center("profil3",680,140,80,60,"profil/profil3")
        self.img_center("profil4",830,140,100,90,"profil/profil4")
        
    def profil_hover(self):
         # Cercle profil
        self.profil1_cercle = pygame.draw.circle(self.Window, self.black, (380, 140), 50)
        self.profil2_cercle = pygame.draw.circle(self.Window, self.black, (530, 140), 50)
        self.profil3_cercle = pygame.draw.circle(self.Window, self.black, (680, 140), 50)
        self.profil4_cercle = pygame.draw.circle(self.Window, self.black, (830, 140), 50)

        # Hover cercle profil
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

    def ProfilHovered(self): 
       # Display neon circle
       
       if self.profil_hovered:
                if self.profil_hovered == self.profil1_cercle:
                    self.img_center("neon circle", 380, 140, 140, 140,"main_page/main_page4")
                    
                elif self.profil_hovered == self.profil2_cercle:
                    self.img_center("neon circle", 530, 140, 140, 140,"main_page/main_page4")
                    
                elif self.profil_hovered == self.profil3_cercle:
                    self.img_center("neon circle", 680, 140, 140, 140,"main_page/main_page4")
                    
                elif self.profil_hovered == self.profil4_cercle:
                    self.img_center("neon circle", 830, 140, 140, 140,"main_page/main_page4")

    def register_run(self):
        while self.register_running:
            self.form()
            self.profil_hover()
            self.profil_screen()
            self.event_register()
            self.ProfilHovered()
            self.register_cursor()
            self.update()