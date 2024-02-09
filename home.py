import pygame

from source.pygame_manager.element import Element
from source.pygame_manager.screen import Screen
# from data.discord_manager import Discord_Manager

class Home(Element, Screen):
    
    def __init__(self):
        Screen.__init__(self)
        Element.__init__(self)
        # Discord_Manager.__init__(self)
    
        pygame.init()
        self.input_email= "Email address"
        self.input_password= "Password"       

    def design(self): 
        self.screen_color(self.grey)

    # Intro section     

        self.image_not_center("Discord", 83, 35, 215, 115,"home/home2")
        self.text_not_align(self.font1,45,"Dive into", self.grey4,50, 203) 
        self.text_not_align(self.font1,45,"Where Ideas Collide", self.grey4,50, 250)          
        self.text_not_align(self.font2,20,"Discord is a versatile communication platform, voice,", self.grey4,80, 295)
        self.text_not_align(self.font2,20,"and video chat features, fostering real-time interaction", self.grey4,80, 320)
        self.text_not_align(self.font2,20,"and collaboration across diverse interests.", self.grey4,80, 345)

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

    def DisplayAll(self): 
        self.design()
        self.HoverLostPassword() 
        self.HoverSign()       
        
    def home_run(self):

        home_run = True
        while home_run :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        home_run = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_email_rect.collidepoint(event.pos): 
                        self.input_email = ""
                        self.entry = 1
                    elif self.input_password_rect.collidepoint(event.pos): 
                        self.input_password = ""
                        self.entry = 2

                    #  920, 410, 350, 50
                    elif self.is_mouse_over_button(pygame.Rect(745, 385, 350, 50)): 
                        
                        print("ok")
                   

                elif event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_BACKSPACE:
                            if self.entry == 1: 
                                self.input_email = self.input_email[:-1]
                            elif self.entry == 2: 
                                self.input_password = self.input_password[:-1]                        
                    else:
                        if self.entry == 1:
                            if event.unicode:
                                self.input_email= self.input_email + event.unicode             
                     
                        elif self.entry == 2:
                            if event.unicode:
                                self.input_password= self.input_password + event.unicode

            

                        
                      
            self.DisplayAll()
            self.update()
            

home = Home()
home.home_run()
