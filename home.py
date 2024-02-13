import pygame

from source.pygame_manager.event_handler import Event_handler
from source.pygame_manager.element import Element
from source.pygame_manager.screen import Screen
from hashlib import sha256
from data.discord_manager import Discord_Manager

class Home(Element, Screen, Event_handler, Discord_Manager):
    
    def __init__(self):
        Screen.__init__(self)
        Element.__init__(self)
        Event_handler.__init__(self)
        Discord_Manager.__init__(self)
    
        self.input_email= "Email address"
        self.input_password= "Password"       

    def design(self): 
        self.screen_color(self.grey)

    # Intro section     

        self.image_not_center("Discord", 250, 380, 400, 79,"home/home2")
        self.text_not_align(self.font1,45,"Dive into", self.grey4,50, 413) 
        self.text_not_align(self.font1,45,"Where Ideas Collide", self.grey4,50, 460)          
        self.text_not_align(self.font2,20,"Discord is a versatile communication platform, voice,", self.grey4,80, 505)
        self.text_not_align(self.font2,20,"and video chat features, fostering real-time interaction", self.grey4,80, 530)
        self.text_not_align(self.font2,20,"and collaboration across diverse interests.", self.grey4,80, 555)

        # Images animated
        self.image_not_center("0wl", 170, 20, 370, 370,"home/home9") 
        self.image_not_center("Cheetah", 210, 50, 300, 300,"home/home8") 
        self.image_not_center("Lion", 170, 20, 370, 370,"home/home7") 
        self.image_not_center("Wolf", 160, 0, 370, 370,"home/home6") 
        self.image_not_center("Logo Discord", 270, 140, 170, 170,"home/home10")  

    # Connexion section       

        # Rec principal
        self.rect_full(self.grey3, 920, 355, 400, 580, 5)
        self.rect_border(self.grey2, 920, 355, 400, 580, 2, 5)

        # Discord image logo
        self.image_not_center("Discord", 840, 65, 170, 170,"home/home1") 

        # Rect email
        self.input_email_rect = self.rect_full(self.grey2, 920, 260, 350, 50, 5) 
        self.text_center(self.font2, 15, self.input_email, self.white, 920, 260)

        # Rect password
        self.input_password_rect= self.rect_full(self.grey2, 920, 320, 350, 50, 5)
        self.text_center(self.font2, 15, self.input_password, self.white,920,320)
        # self.text_center(self.font2, 15, self.password_text, self.white,920,320)

        # Rect log In
        self.button_hover("login", 920, 410, 350, 50, self.blue, self.blue, self.blue1, self.blue1,"Log In", self.font1, self.white, 15, 4, 5) 
        
        self.text_center(self.font2, 12,"Don't have an account ?", self.white, 900, 600)   
        self.text_center(self.font1, 12,"OR", self.blue, 920, 450)
      
        # Lines
        pygame.draw.line(self.Window, self.grey1, (950, 450), (1094, 450), 1)
        pygame.draw.line(self.Window, self.grey1, (746, 450), (890, 450), 1)
        pygame.draw.line(self.Window, self.grey1, (720, 575), (1119, 575), 1)

        # Social Media    
        self.text_center(self.font2, 12,"Sign In with", self.white, 925, 475)   
        self.hover_image("Facebook", "Facebook", 880, 520, 30, 30, "home/home3")    # Facebook
        self.hover_image("Instagram", "Instagram", 925, 520, 30, 30,"home/home4")   # Instagram
        self.hover_image("Google", "Google",  970, 520, 30, 30, "home/home5")       # Google  

    def HoverLostPassword(self): 
        # self.rect_full(self.green, 1045, 360, 105, 10, 5)
        forgot_p = (pygame.Rect(992, 355, 115, 15))    
        if self.is_mouse_over_button(forgot_p):
            self.text_center(self.font1, 12,"Forgot password", self.blue, 1045, 360)          
        else:
            self.text_center(self.font1, 11,"Forgot password", self.blue, 1045, 360)
    
    def HoverSign(self):
        sign = (pygame.Rect(967, 594, 45, 13))    
        if self.is_mouse_over_button(sign):
            self.text_center(self.font1, 12, "Sign Up", self.blue, 990, 600)          
        else:
            self.text_center(self.font1, 11, "Sign Up", self.blue, 990, 600) 

    def LoginUser (self): 
        email = self.input_email
        password = self.input_password

        hashed_password = sha256(password.encode()).hexdigest()

        if self.check_credentials(email, hashed_password):
            print("Connexion successful!")     
        else:
            print("Error. Connexion failed")

    def DisplayAll(self): 
        self.design()
        self.HoverLostPassword() 
        self.HoverSign()       
        
    def home_run(self):

        self.home_running = True
        while self.home_running :        
            self.event_home()    
            if self.is_mouse_over_button(pygame.Rect(920, 410, 350, 50)) and pygame.mouse.get_pressed()[0]:
                self.LoginUser()   

            self.DisplayAll()
            self.update()            

home = Home()
home.home_run()
