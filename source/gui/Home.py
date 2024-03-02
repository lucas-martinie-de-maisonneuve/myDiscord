import pygame
from source.pygame_manager.Gui import Gui
from source.Client import Client

class Home(Gui, Client):
    
    def __init__(self):
        Gui.__init__(self)
        Client.__init__(self)
        
        self.input_email = ""
        self.input_password = ""
        self.password_display = " *" * len(self.input_password)
        self.show_pass = False
        self.entry = 0
        self.anim_pass = False 
        self.anim_email = False

    def design(self): 
        self.screen_color(self.grey)

    # Intro section     

        self.image_not_center("Discord", 250, 380, 400, 79,"home/home2")
        self.text_not_align(self.font1,45,"Dive into", self.grey4,50, 413) 
        self.text_not_align(self.font1,45,"Where Ideas Collide", self.grey4,50, 460)          
        self.text_not_align(self.font2,20,"Discord is a versatile communication platform, voice,", self.grey4,80, 505)
        self.text_not_align(self.font2,20,"and video chat features, fostering real-time interaction", self.grey4,80, 530)
        self.text_not_align(self.font2,20,"and collaboration across diverse interests.", self.grey4,80, 555)

    # Connexion section       

        # Rect principal
        self.rect_full(self.grey3, 920, 355, 400, 580, 5)
        self.rect_border(self.grey2, 920, 355, 400, 580, 2, 5)

        # Discord image logo
        self.image_not_center("Discord", 840, 55, 170, 170,"home/home1") 

        # Rect email
        self.input_email_rect = self.button_hover("Email", 920, 250, 350, 50, self.grey2, self.grey2, self.grey2, self.grey2,self.input_email, self.font2, self.white, 15, 4, 5)
        self.text_input(self.input_email_rect, self.input_email, "Email address", 920, 250, 350, 50, id="email_login")

        self.input_password_rect = self.button_hover("Password", 920, 320, 350, 50, self.grey2, self.grey2, self.grey2, self.grey2,self.password_display, self.font2, self.white, 15, 4, 5)
        self.text_input(self.input_password_rect, self.password_display, "Password", 920, 320, 350, 50, id="password_login")

        # Eye to show password
        self.image_not_center("Eye", 1050, 305, 30,30,"home/home11")
        self.show_pass_rect = pygame.Rect(1050, 305,30,30)
              
        # Rect password
        if self.show_pass:
           self.password_display = self.input_password
        else:
            self.password_display = " *" * len(self.input_password)

        # Rect log In
        self.login = self.button_hover("Login", 920, 410, 350, 50, self.blue, self.blue, self.blue1, self.blue1,"Log In", self.font1, self.white, 15, 4, 5) 
        
        self.text_center(self.font2, 12,"Don't have an account ?", self.white, 900, 600)   
        self.text_center(self.font1, 12,"OR", self.blue, 920, 450)
      
        # Lines
        pygame.draw.line(self.Window, self.grey1, (950, 450), (1094, 450), 1)
        pygame.draw.line(self.Window, self.grey1, (746, 450), (890, 450), 1)
        pygame.draw.line(self.Window, self.grey1, (720, 575), (1119, 575), 1)

        # Social Media    
        self.text_center(self.font2, 12,"Sign In with", self.white, 925, 475)   
        self.facebook = self.hover_image("Facebook", "Facebook", 880, 520, 30, 30, "home/home3", "home/home3")    # Facebook
        self.instagram = self.hover_image("Instagram", "Instagram", 925, 520, 30, 30,"home/home4", "home/home4")   # Instagram
        self.google = self.hover_image("Google", "Google",  970, 520, 30, 30, "home/home5", "home/home5")       # Google   
   
    def hover_lost_password(self): 
        self.forgot_p = (pygame.Rect(992, 355, 115, 15))    
        if self.is_mouse_over_button(self.forgot_p):
            self.text_center(self.font1, 12,"Forgot password", self.blue, 1045, 360)          
        else:
            self.text_center(self.font1, 11,"Forgot password", self.blue, 1045, 360)

    def hover_sign(self):
        self.sign = (pygame.Rect(967, 594, 45, 13))    
        if self.is_mouse_over_button(self.sign):
            self.text_center(self.font1, 12, "Sign Up", self.blue, 990, 600)          
        else:
            self.text_center(self.font1, 11, "Sign Up", self.blue, 990, 600)

    def display_all(self):
        self.design()
        self.hover_lost_password() 
        self.hover_sign()       
        self.logo_home(355, 180, 370, 200, 150)
        self.connexion()

    def connexion(self):
        if self.is_mouse_over_button(pygame.Rect(745, 385, 350, 50)) and pygame.mouse.get_pressed()[0]:
            self.user_email = self.input_email
            self.user_password = self.input_password
            self.user_info = self.login_user()
        if self.connected:
            self.home_to_main_page = True
            self.home_running = False
        if self.user_info is None:
            self.text_center(self.font1, 11, "Wrong password or Email", self.darkred, 825, 360)
        
    def home_run(self):
        if self.home_running:
            self.display_all()
            self.event_home()
            self.home_page_cursor()
