import pygame
from source.pygame_manager.element import Element
from source.pygame_manager.screen import Screen

class Profil(Element, Screen):
    
    def __init__(self):
        Screen.__init__(self)
        Element.__init__(self)
        pygame.init()
        self.profil_running = True
        self.picture = 3
        self.theme_color = self.dark_purple
        self.username = "Lucasssa"
        self.email = "lucas.leplusfort@gmail.com"
        self.password = "bananaaaaa"
        self.password_display = "*" * len(self.password)

    def design(self):
        # Profil main rectangle
        self.img_background("background", 600, 350, 1200, 584, "main/main1")
        self.rect_radius_top(self.theme_color, 750, 90, 800, 100, 10)
        self.rect_radius_bot(self.grey5, 750, 400, 800, 520, 10)

        # Status circle
        self.circle(self.grey5, 500, 230, 15)
        self.circle(self.green, 500, 230, 9)

        # Username
        self.text_not_align(self.font1, 20, f"{self.username}", self.white, 550,180)
        
        # Profile info rectangle
        self.rect_full(self.grey2, 750, 445, 700, 350, 10)
        self.text_not_align(self.font1, 16, "Username",self.grey6,430, 300)
        self.text_not_align(self.font2, 16, f"{self.username}",self.white,440, 320)
        self.text_not_align(self.font1, 16, "E-mail",self.grey6,430, 360)
        self.text_not_align(self.font2, 16, f"{self.email}",self.white,440, 380)
        self.text_not_align(self.font1, 16, "password",self.grey6,430, 420)
        self.text_not_align(self.font2, 16, self.password_display,self.white,480, 440)


    def hover_profile_picture(self):
        self.circle(self.grey5, 450, 180, 70)

        profile_pict = pygame.draw.circle(self.screen.Window, self.theme_color, (450,180), 65)
        if self.is_mouse_over_button(profile_pict):
            self.img_center("profile_picture", 450,180,100,100,f"profil{self.picture}")
            self.circle_alpha(self.alpha_grey, 450, 180, 65)
            self.img_center("logo edit", 450,180,50,50,"logo_edit")

        else:
            self.circle(self.theme_color, 450, 180, 65)
            self.img_center("profile_picture", 450,180,100,100,f"profil{self.picture}")

    def password_show(self):
        self.show = pygame.Rect(440,445,35,15)
        if self.is_mouse_over_button(self.show):
            self.text_not_align(self.font2, 16, f"show",self.white,440, 440)
        else:
            self.text_not_align(self.font2, 16, f"show",self.grey1,440, 440)

    def pygame_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    self.profil_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.show.collidepoint(event.pos):
                    self.password_display = self.password
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.show.collidepoint(event.pos):
                     self.password_display = "*" * len(self.password)


    def profil_run(self):
        while self.profil_running :
            self.pygame_event()
            self.design()
            self.hover_profile_picture()
            self.password_show()
            self.update()
            
pro = Profil()
pro.profil_run()