import pygame
from source.pygame_manager.event_handler import Event_handler
from source.pygame_manager.element import Element
from source.pygame_manager.screen import Screen
class Profil(Element, Screen, Event_handler):
    
    def __init__(self):
        Event_handler.__init__(self)
        Screen.__init__(self)
        Element.__init__(self)
        self.profil_running = True
        self.password_cursor, self.picture_cursor = False, False
        # Info a recuperer de la classe User
        self.picture = 1#
        self.theme_color = self.dark_purple
        self.username = "Lucasssa"#
        self.email = "lucas.leplusfort@gmail.com"#
        self.password = "bananaaa"#
        self.password_display = " *" * len(self.password)
        self.role = "Admin"#
        self.status = "Away"
        self.status_color = self.green

    def design(self):
        if not self.password_cursor and not self.picture_cursor:
            self.normal_cursor()
        # Profil main rectangle
        self.img_background("background", 600, 350, 1200, 700, "main/main1")
        self.rect_radius_top(self.theme_color, 750, 90, 800, 100, 10)
        self.rect_radius_bot(self.grey5, 750, 400, 800, 520, 10)

        # Username
        self.text_not_align(self.font1, 20, f"{self.username}", self.white, 550,180)
        
        # Profile info rectangle
        self.rect_full(self.grey2, 750, 445, 700, 350, 10)
        self.text_not_align(self.font1, 16, "Username",self.grey6,430, 300)
        self.text_not_align(self.font2, 16, f"{self.username}",self.white,440, 320)
        self.text_not_align(self.font1, 16, "E-mail",self.grey6,430, 360)
        self.text_not_align(self.font2, 16, f"{self.email}",self.white,440, 380)
        self.text_not_align(self.font1, 16, "password",self.grey6,430, 420)
        self.text_not_align(self.font2, 16, self.password_display,self.white,440, 440)
        self.text_not_align(self.font1, 16, "Role",self.grey6,430, 480)
        self.text_not_align(self.font2, 16, self.role,self.white,440, 500)
        self.text_not_align(self.font1, 16, "Status",self.grey6,430, 540)
        self.text_not_align(self.font2, 16, self.status,self.white,440, 560)

    def hover_profile_picture(self):
        self.circle(self.grey5, 450, 180, 70)

        # Profile picture
        profile_pict = pygame.draw.circle(self.screen.Window, self.theme_color, (450,180), 65)
        if self.is_mouse_over_button(profile_pict):
            self.picture_cursor = True
            self.hand_cursor()
            self.img_center("profile_picture", 450,180,100,100,f"new_profil/profil{self.picture}")
            self.circle_alpha(self.alpha_grey, 450, 180, 65)
            self.img_center("logo edit", 450,180,50,50,"logo_edit")

        else:
            self.picture_cursor = False
            self.circle(self.theme_color, 450, 180, 65)
            self.img_center("profile_picture", 450,180,100,100,f"new_profil/profil{self.picture}")

        # Status circle
        if self.status == "Online":
            self.status_color = self.green
        elif self.status == "Away":
            self.status_color = self.orange

        self.circle(self.grey5, 500, 230, 15)
        self.circle(self.status_color, 500, 230, 9)

    def password_show(self):
        self.show = pygame.Rect(450 + 10 * len(self.password),443,35,15)
        if self.is_mouse_over_button(self.show):
            self.password_cursor = True
            self.hand_cursor()
            self.text_not_align(self.font2, 16, f"show",self.blue1,450 + 10 * len(self.password), 437)
        else:
            self.password_cursor = False
            self.text_not_align(self.font2, 14, f"show",self.grey1,450 + 10 * len(self.password), 438)

    def button_edit(self):
        self.button_hover("Username", 1000,315, 80, 30, self.grey4, self.grey4, self.grey6, self.grey6, "Edit", self.font2, self.white, 17, 0, 4)
        self.button_hover("email", 1000,375, 80, 30, self.grey4, self.grey4, self.grey6, self.grey6, "Edit", self.font2, self.white, 17, 0, 4)
        self.button_hover("password", 1000,435, 80, 30, self.grey4, self.grey4, self.grey6, self.grey6, "Edit", self.font2, self.white, 17, 0, 4)
        self.button_hover("role", 1000,495, 80, 30, self.grey4, self.grey4, self.grey6, self.grey6, "Edit", self.font2, self.white, 17, 0, 4)
        self.button_hover("status", 1000,555, 80, 30, self.grey4, self.grey4, self.grey6, self.grey6, "Edit", self.font2, self.white, 17, 0, 4)

    def profil_run(self):
        while self.profil_running :
            self.event_profil()
            self.design()
            self.hover_profile_picture()
            self.password_show()
            self.button_edit()
            self.update()
            
pro = Profil()
pro.profil_run()