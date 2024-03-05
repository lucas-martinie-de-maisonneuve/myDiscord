import pygame
from source.pygame_manager.Gui import Gui
from source.Client import Client

class Register(Gui, Client):
    def __init__(self):
        Gui.__init__(self)
        Client.__init__(self)
        self.entry = 0
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
        self.button_hover("username", 600, 240, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.register_username, self.font2, self.white, 15, 4, 5)
        self.text_input(self.username_rect, self.register_username, "Username", 600, 240, 400, 40, id="username")
        if self.register_username != "":
            self.img_center("Validate", 865, 240, 30, 30, "profile/profile16")
        else:
            self.img_center("Not", 865, 240, 30, 30, "profile/profile17")

        # Email
        self.email_rect = self.rect_full(self.grey2, 600, 300, 400, 40, 5)
        self.button_hover("email", 600, 300, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.register_email, self.font2, self.white, 15, 4, 5)
        self.text_input(self.email_rect, self.register_email, "Email address", 600, 300, 400, 40, id="email")
        if "@" in self.register_email and "." in self.register_email:
            self.img_center("Validate", 865, 300, 30, 30, "profile/profile16")
        else:
            self.img_center("Not", 865, 300, 30, 30, "profile/profile17")

        # Surname
        self.surname_rect = self.rect_full(self.grey2, 600, 360, 400, 40, 5)
        self.button_hover("Surname", 600, 360, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.register_surname, self.font2, self.white, 15, 4, 5)
        self.text_input(self.surname_rect, self.register_surname, "Surname", 600, 360, 400, 40, id="surname")
        if self.register_surname != "":
            self.img_center("Validate", 865, 360, 30, 30, "profile/profile16")
        else:
            self.img_center("Not", 865, 360, 30, 30, "profile/profile17")
       
        # Name
        self.name_rect = self.rect_full(self.grey2, 600, 420, 400, 40, 5)
        self.button_hover("Name", 600, 420, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.register_name, self.font2, self.white, 15, 4, 5)
        self.text_input(self.name_rect, self.register_name, "Name", 600, 420, 400, 40, id="name")
        if self.register_name != "":
            self.img_center("Validate", 865, 420, 30, 30, "profile/profile16")
        else:
            self.img_center("Not", 865, 420, 30, 30, "profile/profile17")

        # Password
        self.password_rect = self.rect_full(self.grey2, 600, 480, 400, 40, 5)
        self.button_hover("Password", 600, 480, 400, 40, self.grey2, self.grey2, self.grey2, self.grey2,self.register_password, self.font2, self.white, 15, 4, 5)
        self.text_input(self.password_rect, self.register_password, "Password", 600, 480, 400, 40, id="password")
        if len(self.register_password) >= 8 and any(char.isdigit() for char in self.register_password) and any(char.isupper() for char in self.register_password) and any(char.islower() for char in self.register_password) and any(char in "_^*%/+.:;=" for char in self.register_password):
            self.img_center("Validate", 865, 480, 30, 30, "profile/profile16")
        else:
            self.img_center("Not", 865, 480, 30, 30, "profile/profile17")

        if self.entry == 5:
            self.rect_full(self.grey11, 990, 480, 170, 120, 4)

            self.text_not_align(self.font2, 12, "At least 1 Uppercase", self.grey7, 925, 432)
            if any(char.isupper() for char in self.register_password):
                self.img_center("Validate", 915, 440, 16, 16, "profile/profile15")

            self.text_not_align(self.font2, 12, "At least 1 Lowercase", self.grey7, 925, 452)
            if any(char.islower() for char in self.register_password):
                self.img_center("Validate", 915, 460, 16, 16, "profile/profile15")
                
            self.text_not_align(self.font2, 12, "At least 8 Characters", self.grey7, 925, 472)
            if len(self.register_password) >= 8:
                self.img_center("Validate", 915, 480, 16, 16, "profile/profile15")

            self.text_not_align(self.font2, 12, "At least 1 Special (_^*%/+.:;=)", self.grey7, 925, 492)
            if any(char in "_^*%/+.:;=" for char in self.register_password):
                self.img_center("Validate", 915, 500, 16, 16, "profile/profile15")

            self.text_not_align(self.font2, 12, "At least 1 Digit", self.grey7, 925, 512)
            if any(char.isdigit() for char in self.register_password):
                self.img_center("Validate", 915, 520, 16, 16, "profile/profile15")           

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
        self.img_center("profile1",425,140,100,100,"profile/profile1")
        self.img_center("profile2",545,140,100,100,"profile/profile2")
        self.img_center("profile3",665,140,100,100,"profile/profile3")
        self.img_center("profile4",785,140,100,100,"profile/profile4")
        
    def profile_hover(self):
         # Circle profile
        self.profile1_circle = pygame.draw.circle(self.Window, self.black, (425, 140), 50)
        self.profile2_circle = pygame.draw.circle(self.Window, self.black, (545, 140), 50)
        self.profile3_circle = pygame.draw.circle(self.Window, self.black, (665, 140), 50)
        self.profile4_circle = pygame.draw.circle(self.Window, self.black, (785, 140), 50)

        # Hover circle profile
        self.p_profile1 = self.profile1_circle
        if self.is_mouse_over_button(self.p_profile1):
            self.profile1_circle = pygame.draw.circle(self.Window, self.black, (425, 140), 50)
            self.img_center("profile1",425,140,140,140,"register/register1")
        else:
            self.profile1_circle = pygame.draw.circle(self.Window, self.black, (425, 140), 50)
            self.hover_profile1_circle = pygame.draw.circle(self.Window, self.grey2, (425, 140), 50, width=2) 
            
        self.p_profile2 = self.profile2_circle
        if self.is_mouse_over_button(self.p_profile2):
            self.profile2_circle = pygame.draw.circle(self.Window, self.black, (545, 140), 50)
            self.img_center("profile2",545,140,140,140,"register/register1")
        else:
            self.profile2_circle = pygame.draw.circle(self.Window, self.black, (545, 140), 50)
            self.hover_profile2_circle = pygame.draw.circle(self.Window, self.grey2, (545, 140), 50, width=2) 

        self.p_profile3 = self.profile3_circle
        if self.is_mouse_over_button(self.p_profile3):
            self.profile3_circle = pygame.draw.circle(self.Window, self.black, (665, 140), 50)
            self.img_center("profile3",665,140,140,140,"register/register1")
        else:
            self.profile3_circle = pygame.draw.circle(self.Window, self.black, (665, 140), 50)
            self.hover_profile3_circle = pygame.draw.circle(self.Window, self.grey2, (665, 140), 50, width=2)

        self.p_profile4 = self.profile4_circle
        if self.is_mouse_over_button(self.p_profile4):
            self.profile4_circle = pygame.draw.circle(self.Window, self.black, (785, 140), 50)
            self.img_center("profile4",785,140,140,140,"register/register1")
        else:
            self.profile4_circle = pygame.draw.circle(self.Window, self.black, (785, 140), 50)
            self.hover_profile4_circle= pygame.draw.circle(self.Window, self.grey2, (785, 140), 50, width=2)

        if self.register_photo != 0:
            self.img_center("Validate", 865, 140, 30, 30, "profile/profile16")
        else:
            self.img_center("Not", 865, 140, 30, 30, "profile/profile17")

    def profile_picture_hovered(self): 
       
       if self.profile_hovered:
                if self.profile_hovered == self.profile1_circle:
                    self.img_center("neon circle", 425, 140, 140, 140,"main_page/main_page4")
                    
                elif self.profile_hovered == self.profile2_circle:
                    self.img_center("neon circle", 545, 140, 140, 140,"main_page/main_page4")
                    
                elif self.profile_hovered == self.profile3_circle:
                    self.img_center("neon circle", 665, 140, 140, 140,"main_page/main_page4")
                    
                elif self.profile_hovered == self.profile4_circle:
                    self.img_center("neon circle", 785, 140, 140, 140,"main_page/main_page4")

    def register_run(self):
        if self.register_running:
            self.background()
            self.form()
            self.profile_hover()
            self.profile_screen()
            self.event_register()
            self.profile_picture_hovered()
            self.register_cursor()
