import pygame
from source.pygame_manager.event_handler import Event_handler
from source.pygame_manager.element import Element
from source.pygame_manager.screen import Screen
from source.pygame_manager.cursor import Cursor
class Profil(Element, Screen, Event_handler, Cursor):
    
    def __init__(self):
        Event_handler.__init__(self)
        Screen.__init__(self)
        Element.__init__(self)
        Cursor.__init__(self)
        self.profil_running = False
        self.edit = 0

        self.password_edit, self.username_edit, self.email_edit, self.picture_edit, self.status_edit = False, False, False, False, False
        # Info a recuperer de la classe User
        self.picture = 1#
        self.theme_color = self.dark_purple
        self.username = "Lucasssa"#
        self.email = "lucas.leplusfort@gmail.com"#
        self.password = "bananaaa"#
        self.password_display = " *" * len(self.password)
        self.show_pass = False
        self.role = "Admin"#
        self.status = "Online"
        self.status_color = self.green
        self.size_username, self.size_email ,self.size_password, self.size_profile_picture= 0, 0, 0, 0
        self.pict = []

    def design(self):
        # Profil main rectangle
        self.img_background("background", 600, 350, 1200, 700, "main_page/main1")
        self.rect_radius_top(self.theme_color, 750, 90, 800, 100, 10)
        self.rect_radius_bot(self.grey5, 750, 400, 800, 520, 10)
        
        # Left rectangle and disconnect
        self.rect_full(self.grey5, 195, 305, 290, 530, 10) 
        self.rect_full(self.grey5, 195, 620, 290, 80, 10) 
        
        # Username
        if self.size_profile_picture < 100:
            self.text_not_align(self.font1, 20, f"{self.username}", self.white, 550,180 + self.size_profile_picture // 2)
        else:
            self.text_not_align(self.font1, 20, f"{self.username}", self.white, 550,230)
        
        # Profile info rectangle
        self.rect_full(self.grey2, 750, 445, 700, 350, 10)
        
        #Info profil
        self.info_profil("Username", self.username, 300)
        self.info_profil("E-mail", self.email, 360)
        self.info_profil("Password", self.password_display, 420)
        self.info_profil("Role", self.role, 480)
        self.info_profil("Status", self.role, 540)

        #Disconnect button
        self.disconnect_button = pygame.Rect(95, 590, 200, 57)
        if self.is_mouse_over_button(self.disconnect_button):
            self.img_center("disconnect", 195, 620, 220, 63, "profil/disconnect_hover")
        else:
            self.img_center("disconnect", 195, 620, 200, 57, "profil/disconnect")

    def hover_profile_picture(self):
        self.circle(self.grey5, 450, 180, 70)

        # Profile picture
        self.profile_pict = pygame.draw.circle(self.screen.Window, self.theme_color, (450,180), 65)
        if self.is_mouse_over_button(self.profile_pict):
            self.img_center("profile_picture", 450,180,100,100,f"profil/profil{self.picture}")
            self.circle_alpha(self.alpha_grey, 450, 180, 65)
            self.img_center("logo edit", 450,180,50,50,"logo_edit")

        else:
            self.picture_cursor = False
            self.circle(self.theme_color, 450, 180, 65)
            self.img_center("profile_picture", 450,180,100,100,f"profil/profil{self.picture}")

    def status_display(self, x, y, texte, texte2, color, color2):
        self.status_edit_rect = pygame.Rect(540, 570, 80, 20)
        self.status_active_rect = pygame.Rect(440, 570, 80, 20)
        self.status_change = self.rect_full(self.grey6, x + 25, y, 80, 20, 8)
        self.text_center(self.font2, 15, texte, self.black, x + 35, y)
        self.circle(color, x, y, 8)

        if self.status_edit:
            self.status_change = self.rect_full(self.grey6, x + 125, y, 80, 20, 8)
            self.text_center(self.font2, 15, texte2, self.black, x + 135, y)
            self.circle(color2, x +100, y, 8)

    def status_circle(self):
        if self.status == "Online":
            self.status_display(455, 580, "Online", "Away", self.green, self.orange)
            self.status_color = self.green

        elif self.status == "Away":
            self.status_display(455, 580, "Away", "Online", self.orange, self.green)
            self.status_color = self.orange

        self.circle(self.grey5, 500, 230, 15)
        self.circle(self.status_color, 500, 230, 9)

    def profile_picture_edit(self):
        if self.picture == 1: 
            self.pict = [2, 3, 4]
        elif self.picture == 2:
            self.pict = [1, 3, 4]
        elif self.picture == 3:
            self.pict = [1, 2, 4]
        elif self.picture == 4:
            self.pict = [1, 2, 3]
        if self.picture_edit:
            if self.size_profile_picture < 400:
                self.size_profile_picture += 10
        else:
            if self.size_profile_picture > 0:
                self.size_profile_picture -=10
        self.rect_full_not_centered(self.grey3, 450, 120, 0 + self.size_profile_picture, 100, 50)
        if self.size_profile_picture > 170:
            self.picture1 = pygame.draw.circle(self.screen.Window, self.theme_color, (570,170), 45)
            self.image_not_center("image1", 540, 140, 60, 60, f"profil/profil{self.pict[0]}")
            if self.is_mouse_over_button(self.picture1):
                self.hover_profil1 = pygame.draw.circle(self.Window, self.yellow, (570, 170), 45, 4, True, False, True, False) 
                self.hover_profil1 = pygame.draw.circle(self.Window, self.pink, (570, 170), 45, 4, False, True, False, True) 

        if self.size_profile_picture > 270:
            self.picture2 = pygame.draw.circle(self.screen.Window, self.theme_color, (670,170), 45)
            self.image_not_center("image1", 640, 140, 60, 60, f"profil/profil{self.pict[1]}")
            if self.is_mouse_over_button(self.picture2):
                self.hover_profil2 = pygame.draw.circle(self.Window, self.yellow, (670, 170), 45, 4, True, False, True, False) 
                self.hover_profil2 = pygame.draw.circle(self.Window, self.pink, (670, 170), 45, 4, False, True, False, True) 


        if self.size_profile_picture > 370:
            self.picture3 = pygame.draw.circle(self.screen.Window, self.theme_color, (770,170), 45)
            self.image_not_center("image1", 740, 140, 60, 60, f"profil/profil{self.pict[2]}")
            if self.is_mouse_over_button(self.picture3):
                self.hover_profil3 = pygame.draw.circle(self.Window, self.yellow, (770, 170), 45, 4, True, False, True, False) 
                self.hover_profil3 = pygame.draw.circle(self.Window, self.pink, (770, 170), 45, 4, False, True, False, True) 

        self.hover_profile_picture()
        self.status_circle()

    def password_show(self):
        if not self.password_edit:
            self.show = pygame.Rect(450 + 10 * len(self.password),443,35,15)
            if self.is_mouse_over_button(self.show):
                self.text_not_align(self.font2, 16, f"show",self.blue1,450 + 10 * len(self.password), 437)
            else:
                self.text_not_align(self.font2, 14, f"show",self.grey1,450 + 10 * len(self.password), 438)

    def info_profil(self, title, text_info, y):
        self.text_not_align(self.font1, 16, title, self.grey6, 430, y)
        self.button_hover(title, 1000, y + 15, 80, 30, self.pink, self.pink, self.purple2, self.purple2, "Edit", self.font5, self.white, 17, 0, 4)
        self.info_profil_cursor(title)

# White rectangle when 'Edit' is pressed
    def info_profil_edit(self):
        # Username info 
        self.rect_full_not_centered(self.white, 420, 322, 0 + self.size_username, 20, 12)
        if self.username_edit:
            if self.size_username < 240:
                self.size_username += 15
            self.text_not_align(self.font2, 16, self.username, self.black, 440, 322)
        else:
            if self.size_username < 15:
                self.size_username = 0
            if self.size_username > 0:
                self.text_not_align(self.font2, 16, self.username, self.black, 440, 322)
                self.size_username -= 20
            else: 
                self.text_not_align(self.font2, 16, self.username, self.white, 440, 322)

        # Email info 
        self.rect_full_not_centered(self.white, 420, 382, 0 + self.size_email, 20, 12)
        if self.email_edit:
            if self.size_email < 240:
                self.size_email += 15
            self.text_not_align(self.font2, 16, self.email, self.black, 440, 382)
        else:
            if self.size_email < 15:
                self.size_email = 0
            if self.size_email > 0:
                self.text_not_align(self.font2, 16, self.email, self.black, 440, 382)
                self.size_email -= 20
            else: 
                self.text_not_align(self.font2, 16, self.email, self.white, 440, 382)

        # Password info 
        self.rect_full_not_centered(self.white, 420, 442, 0 + self.size_password, 20, 12)
        if self.password_edit:
            if self.size_password < 240:
                self.size_password += 15
            self.text_not_align(self.font2, 16, self.password, self.black, 440, 442)
        else:
            if self.size_password < 15:
                self.size_password = 0
            elif self.size_password > 0:
                self.size_password -= 20
            if self.size_password < 100:
                if self.show_pass:
                    self.text_not_align(self.font2, 16, self.password, self.white, 440, 442)
                else:
                    self.password_display = " *" * len(self.password)
                    self.text_not_align(self.font2, 16, self.password_display, self.white, 440, 442)
            else:
                self.text_not_align(self.font2, 16, self.password, self.black, 440, 442)

    def profil_run(self):
        while self.profil_running :
            self.profil_page_cursor()
            self.event_profil()
            self.design()
            self.info_profil_edit()
            self.password_show()
            self.profile_picture_edit()
            self.update()
            