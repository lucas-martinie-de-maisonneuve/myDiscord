import pygame
from source.pygame.element import Element
from source.pygame.screen import Screen

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

        # Connexion 920, 290, 350, 50, 5
        self.button("connexion", 920, 420, 350, 50, self.blue, self.blue, self.blue1, self.blue1,"Log In", self.font1, self.white, 15, 4, 5)

        # Nouveau compte
        self.text_center(self.font2, 12,"Don't have an account ?", self.white, 900, 600)   
        
        # Hoover 
        # self.image_not_center("Discord", 770, 140, 300, 56,"home/home1")        

        # Texte accueil
        self.text_not_align(self.font1,60,"Your Place to Talk", self.grey3,50, 170)        
        self.text_not_align(self.font1,20,"imagine a place where friendship is not a request.", self.blue,100, 240)
        self.text_not_align(self.font1,20,"It Just sorta hapens", self.blue,100, 270)

        # Ligne
        pygame.draw.line(self.Window, self.grey1, (930, 400), (930, 400), 10)
        pygame.draw.line(self.Window, self.grey1, (930, 450), (930, 450), 10)
        pygame.draw.line(self.Window, self.grey1, (720, 575), (1119, 575), 1)

        # self.image_not_center("Discord", 770, 140, 300, 56,"home/home2")          

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
