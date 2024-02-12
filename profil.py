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
        self.edit = 0

        self.password_cursor, self.pass_cursor, self.picture_cursor, self.username_cursor, self.email_cursor, self.role_cursor, self.status_cursor = False, False, False, False, False, False, False

        self.password_edit, self.username_edit, self.email_edit = False, False, False
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
        self.size_username, self.size_email ,self.size_password= 0, 0, 0

        self.username_rect = pygame.Rect(960, 300, 80, 30)
        self.email_rect = pygame.Rect(960, 360, 80, 30)
        self.password_rect = pygame.Rect(960, 420, 80, 30)
        self.role_rect = pygame.Rect(960, 480, 80, 30)
        self.status_rect = pygame.Rect(960, 540, 80, 30)

    def design(self):
        if not (self.password_cursor or self.picture_cursor or self.username_cursor or self.email_cursor or self.pass_cursor or self.role_cursor or self.status_cursor):
            self.normal_cursor()
        # Profil main rectangle
        self.img_background("background", 600, 350, 1200, 700, "main/main1")
        self.rect_radius_top(self.theme_color, 750, 90, 800, 100, 10)
        self.rect_radius_bot(self.grey5, 750, 400, 800, 520, 10)

        # Username
        self.text_not_align(self.font1, 20, f"{self.username}", self.white, 550,180)
        
        # Profile info rectangle
        self.rect_full(self.grey2, 750, 445, 700, 350, 10)
        
        #Info profil
        self.info_profil("Username", self.username, 300)
        self.info_profil("E-mail", self.email, 360)
        self.info_profil("Password", self.password_display, 420)
        self.info_profil("Role", self.role, 480)
        self.info_profil("Status", self.role, 540)

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

    def status_circle(self):
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

    def info_profil(self, title, text_info, y):
        self.text_not_align(self.font1, 16, title, self.grey6, 430, y)
        self.button_hover(title, 1000, y + 15, 80, 30, self.grey4, self.grey4, self.grey6, self.grey6, "Edit", self.font2, self.white, 17, 0, 4)
        self.info_profil_cursor(title)

# White rectangle when 'Edit' is pressed
    def info_profil_edit(self):
        if self.username_edit:
            self.rect_full_not_centered(self.white, 420, 320, 0 + self.size_username, 20, 10)
            if self.size_username < 250:
                self.size_username += 8
            self.text_not_align(self.font2, 16, self.username, self.black, 440, 320)
        else: 
            self.text_not_align(self.font2, 16, self.username, self.white, 440, 320)

        if self.email_edit:
            self.rect_full_not_centered(self.white, 420, 380, 0 + self.size_email, 20, 10)
            if self.size_email < 250:
                self.size_email += 8
            self.text_not_align(self.font2, 16, self.email, self.black, 440, 380)
        else: 
            self.text_not_align(self.font2, 16, self.email, self.white, 440, 380)

        if self.password_edit:
            self.rect_full_not_centered(self.white, 420, 440, 0 + self.size_password, 20, 10)
            if self.size_password < 250:
                self.size_password += 8
            self.text_not_align(self.font2, 16, self.password, self.black, 440, 440)
        else: 
            self.text_not_align(self.font2, 16, self.password_display, self.white, 440, 440)
            self.password_display = " *" * len(self.password)

    def info_profil_cursor(self, title):
        if title == "Username":
            self.username_cursor = self.is_mouse_over_button(self.username_rect)
        elif title == "E-mail":
            self.email_cursor = self.is_mouse_over_button(self.email_rect)
        elif title == "Password":
            self.pass_cursor = self.is_mouse_over_button(self.password_rect)
        elif title == "Role":
            self.role_cursor = self.is_mouse_over_button(self.role_rect)
        elif title == "Status":
            self.status_cursor = self.is_mouse_over_button(self.status_rect)
        if self.username_cursor or self.email_cursor or self.pass_cursor or self.role_cursor or self.status_cursor:
            self.hand_cursor()

    def profil_run(self):
        while self.profil_running :
            self.event_profil()
            self.design()
            self.hover_profile_picture()
            self.password_show()
            self.status_circle()
            self.info_profil_edit()
            self.update()
            
pro = Profil()
pro.profil_run()