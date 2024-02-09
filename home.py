import pygame
from source.pygame_manager.element import Element
from source.pygame_manager.screen import Screen

class Home(Element, Screen):
    
    def __init__(self):
        Screen.__init__(self)
        Element.__init__(self)
        pygame.init()

    def design(self): 
        self.screen_color(self.grey)

        # Rectangles principal de connexion
        self.rect_full(self.grey3, 920, 355, 400, 580, 5)
        self.rect_border(self.grey2, 920, 355, 400, 580, 2, 5)
        # self.rect_full(self.white, 820, 350, 410, 450, 5)
        # self.rect_border(self.grey, 820, 350, 410, 450, 1, 5)

        # Rect email
        self.rect_full(self.grey2, 920, 260, 350, 50, 5) 
        self.text_center(self.font2, 15,"Email address", self.white, 920, 260)

        # Rect password
        self.rect_full(self.grey2, 920, 320, 350, 50, 5)
        self.text_center(self.font2, 15, "Password", self.white,920,320)

        # Section intro
        self.image_not_center("Discord", 840, 65, 170, 170,"home/home1") # Discord logo

        self.button("connexion", 920, 410, 350, 50, self.blue, self.blue, self.blue1, self.blue1,"Log In", self.font1, self.white, 15, 4, 5)
        self.text_center(self.font2, 12,"Don't have an account ?", self.white, 900, 600)   
        self.text_center(self.font1, 12,"OR", self.blue, 920, 450)
        self.text_not_align(self.font1,45,"Dive into", self.grey4,50, 203) 
        self.image_not_center("Discord", 225, 0, 470, 470,"home/home2")   

        self.text_not_align(self.font1,45,"Where Ideas Collide", self.grey4,50, 250)          
        self.text_not_align(self.font2,20,"Discord is a versatile communication platform, voice,", self.grey4,80, 295)
        self.text_not_align(self.font2,20,"and video chat features, fostering real-time interaction", self.grey4,80, 320)
        self.text_not_align(self.font2,20,"and collaboration across diverse interests.", self.grey4,80, 345)

        # Lines
        pygame.draw.line(self.Window, self.grey1, (950, 450), (1094, 450), 1)
        pygame.draw.line(self.Window, self.grey1, (746, 450), (890, 450), 1)
        pygame.draw.line(self.Window, self.grey1, (720, 575), (1119, 575), 1)


        # Social Media     
      
        self.text_center(self.font2, 12,"Sign In with", self.white, 925, 475) 
        self.image_not_center("Discord", 860, 500, 30, 30,"home/home3") # Facebook
        self.image_not_center("Discord", 910, 500, 30, 30,"home/home4") # Instagram
        self.image_not_center("Discord", 960, 500, 30, 30,"home/home5") # Google
    
         

    def HoverSign(self): 
        # self.rect_full(self.green, 1045, 360, 105, 10, 5)
        sign = (pygame.Rect(992, 355, 115, 15))    
        if self.is_mouse_over_button(sign):
            self.text_center(self.font1, 12,"Forgot password", self.blue, 1045, 360)          
        else:
            self.text_center(self.font1, 11,"Forgot password", self.blue, 1045, 360)
    
    def HoverLostPassword(self):
        sign = (pygame.Rect(967, 594, 45, 13))    
        if self.is_mouse_over_button(sign):
            self.text_center(self.font1, 12, "Sign Up", self.blue, 990, 600)          
        else:
            self.text_center(self.font1, 11, "Sign Up", self.blue, 990, 600)   



        
    def home_run(self):
        home_run = True
        while home_run :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        home_run = False

            self.design()
            self.HoverSign()
            self.HoverLostPassword()
            self.update()
            

home = Home()
home.home_run()
