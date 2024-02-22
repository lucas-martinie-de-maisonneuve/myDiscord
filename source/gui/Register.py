import pygame
from source.pygame_manager.Element import Element
from source.pygame_manager.EventHandler import EventHandler
from source.pygame_manager.Cursor import Cursor
from source.pygame_manager.Animation import Animation
from data.DiscordManager import DiscordManager

class Register(Element, EventHandler, Cursor, Animation,DiscordManager):
    def __init__(self):
        Element.__init__(self)
        Cursor.__init__(self)
        Animation.__init__(self)
        
        self.register_running = False
        self.username = ""
        self.email = ""
        self.surname = ""
        self.name = ""
        self.password = ""
        self.entry = 0
        self.photo = 0
        self.profile_hovered = None
        self.entry = 0

    def background(self):
        self.img_background("Background", 600,350,1200,700,"register/background_register")
        self.logo_home(150, 127, 260, 140, 105)
        self.screen_alpha(self.alpha_grey2)

    def form(self):

        # Display rectangles
        self.rect_full(self.grey3, 600, 355, 600, 580, 10)
        self.rect_border(self.grey2, 600, 355, 600, 580, 2, 10)

        # Username, Email address, Surname, Name, Password
        # Username
        self.username_rect = self.rect_full(self.grey2, 600, 240, 400, 40, 5)
        self.button_hover("username", 600, 240, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.username, self.font2, self.white, 15, 4, 5)
        self.text_input(self.username_rect, self.username, "Username", 600, 240, 400, 40, id="username")

        # Email
        self.email_rect = self.rect_full(self.grey2, 600, 300, 400, 40, 5)
        self.button_hover("email", 600, 300, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.email, self.font2, self.white, 15, 4, 5)
        self.text_input(self.email_rect, self.email, "Email address", 600, 300, 400, 40, id="email")

        # Surname
        self.surname_rect = self.rect_full(self.grey2, 600, 360, 400, 40, 5)
        self.button_hover("Surname", 600, 360, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.surname, self.font2, self.white, 15, 4, 5)
        self.text_input(self.surname_rect, self.surname, "Surname", 600, 360, 400, 40, id="surname")

        # Name
        self.name_rect = self.rect_full(self.grey2, 600, 420, 400, 40, 5)
        self.button_hover("Name", 600, 420, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.name, self.font2, self.white, 15, 4, 5)
        self.text_input(self.name_rect, self.name, "Name", 600, 420, 400, 40, id="name")

        # Password
        self.password_rect = self.rect_full(self.grey2, 600, 480, 400, 40, 5)
        self.button_hover("Password", 600, 480, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.password, self.font2, self.white, 15, 4, 5)
        self.text_input(self.password_rect, self.password, "Password", 600, 480, 400, 40, id="password")

        # Button Sign Up
        self.sign_up = self.rect_full(self.blue, 600, 560, 350, 50,5)
        self.button_hover("Connexion", 600, 560, 350, 50, self.blue, self.blue, self.blue1, self.blue1,"Sign Up", self.font1, self.white, 15, 4, 5)

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
            
    def profile_screen(self):

        # Profile pictures
        self.img_center("profile1",380,140,100,100,"profile/profile1")
        self.img_center("profile2",530,140,100,100,"profile/profile2")
        self.img_center("profile3",680,140,100,100,"profile/profile3")
        self.img_center("profile4",830,140,100,100,"profile/profile4")
        
    def profile_hover(self):
         # Circle profile
        self.profile1_circle = pygame.draw.circle(self.Window, self.black, (380, 140), 50)
        self.profile2_circle = pygame.draw.circle(self.Window, self.black, (530, 140), 50)
        self.profile3_circle = pygame.draw.circle(self.Window, self.black, (680, 140), 50)
        self.profile4_circle = pygame.draw.circle(self.Window, self.black, (830, 140), 50)

        # Hover circle profile
        self.p_profile1 = self.profile1_circle
        if self.is_mouse_over_button(self.p_profile1):
            self.profile1_circle = pygame.draw.circle(self.Window, self.black, (380, 140), 50)
            self.img_center("profile1",380,140,140,140,"register/register1")
        else:
            self.profile1_circle = pygame.draw.circle(self.Window, self.black, (380, 140), 50)
            self.hover_profile1_circle = pygame.draw.circle(self.Window, self.grey2, (380, 140), 50, width=2) 
            
        self.p_profile2 = self.profile2_circle
        if self.is_mouse_over_button(self.p_profile2):
            self.profile2_circle = pygame.draw.circle(self.Window, self.black, (530, 140), 50)
            self.img_center("profile2",530,140,140,140,"register/register1")
        else:
            self.profile2_circle = pygame.draw.circle(self.Window, self.black, (530, 140), 50)
            self.hover_profile2_circle = pygame.draw.circle(self.Window, self.grey2, (530, 140), 50, width=2) 

        self.p_profile3 = self.profile3_circle
        if self.is_mouse_over_button(self.p_profile3):
            self.profile3_circle = pygame.draw.circle(self.Window, self.black, (680, 140), 50)
            self.img_center("profile3",680,140,140,140,"register/register1")
        else:
            self.profile3_circle = pygame.draw.circle(self.Window, self.black, (680, 140), 50)
            self.hover_profile3_circle = pygame.draw.circle(self.Window, self.grey2, (680, 140), 50, width=2)

        self.p_profile4 = self.profile4_circle
        if self.is_mouse_over_button(self.p_profile4):
            self.profile4_circle = pygame.draw.circle(self.Window, self.black, (830, 140), 50)
            self.img_center("profile4",830,140,140,140,"register/register1")
        else:
            self.profile4_circle = pygame.draw.circle(self.Window, self.black, (830, 140), 50)
            self.hover_profile4_circle= pygame.draw.circle(self.Window, self.grey2, (830, 140), 50, width=2)

    def profile_picture_hovered(self): 
       
       if self.profile_hovered:
                if self.profile_hovered == self.profile1_circle:
                    self.img_center("neon circle", 380, 140, 140, 140,"main_page/main_page4")
                    
                elif self.profile_hovered == self.profile2_circle:
                    self.img_center("neon circle", 530, 140, 140, 140,"main_page/main_page4")
                    
                elif self.profile_hovered == self.profile3_circle:
                    self.img_center("neon circle", 680, 140, 140, 140,"main_page/main_page4")
                    
                elif self.profile_hovered == self.profile4_circle:
                    self.img_center("neon circle", 830, 140, 140, 140,"main_page/main_page4")

    def register_run(self):
        while self.register_running:
            self.background()
            self.form()
            self.profile_hover()
            self.profile_screen()
            self.event_register()
            self.profile_picture_hovered()
            self.register_cursor()
            self.update()
