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

        self.password_cursor, self.pass_cursor, self.picture_cursor, self.username_cursor, self.email_cursor, self.role_cursor, self.status_cursor, self.picture1_cursor, self.picture2_cursor, self.picture3_cursor, self.disconnect_cursor, self.status_edit_cursor, self.status_active_cursor = False, False, False, False, False, False, False, False, False, False, False, False, False

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
        self.username_rect = pygame.Rect(960, 300, 80, 30)
        self.email_rect = pygame.Rect(960, 360, 80, 30)
        self.password_rect = pygame.Rect(960, 420, 80, 30)
        self.role_rect = pygame.Rect(960, 480, 80, 30)
        self.status_rect = pygame.Rect(960, 540, 80, 30)
        self.picture1 = pygame.Rect(0, 0, 0, 0)
        self.picture2 = pygame.Rect(0, 0, 0, 0)
        self.picture3 = pygame.Rect(0, 0, 0, 0)

    def design(self):
        if not (self.password_cursor or self.picture_cursor or self.username_cursor or self.email_cursor or self.pass_cursor or self.role_cursor or self.status_cursor or self.picture1_cursor or self.picture2_cursor or self.picture3_cursor or self.disconnect_cursor or self.status_edit_cursor or self.status_active_cursor):
            self.normal_cursor()

        # Profil main rectangle
        self.img_background("background", 600, 350, 1200, 700, "main/main1")
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
        disconnect_button = pygame.Rect(95, 590, 200, 57)
        if self.is_mouse_over_button(disconnect_button):
            self.disconnect_cursor = True
            self.hand_cursor()
            self.img_center("disconnect", 195, 620, 220, 63, "profil/disconnect_hover")
        else:
            self.img_center("disconnect", 195, 620, 200, 57, "profil/disconnect")
            self.disconnect_cursor = False

    def hover_profile_picture(self):
        self.circle(self.grey5, 450, 180, 70)

        # Profile picture
        self.profile_pict = pygame.draw.circle(self.screen.Window, self.theme_color, (450,180), 65)
        if self.is_mouse_over_button(self.profile_pict):
            self.picture_cursor = True
            self.hand_cursor()
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

            if self.is_mouse_over_button(self.status_edit_rect):
                self.status_edit_cursor = True
                self.hand_cursor()
            else:
                self.status_edit_cursor = False
            if self.is_mouse_over_button(self.status_active_rect):
                self.status_active_cursor = True
                self.hand_cursor()
            else:
                self.status_active_cursor = False

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
                self.picture1_cursor = True
                self.hover_profil1 = pygame.draw.circle(self.Window, self.yellow, (570, 170), 45, 4, True, False, True, False) 
                self.hover_profil1 = pygame.draw.circle(self.Window, self.pink, (570, 170), 45, 4, False, True, False, True) 
                self.hand_cursor()
            else:
                self.picture1_cursor = False

        if self.size_profile_picture > 270:
            self.picture2 = pygame.draw.circle(self.screen.Window, self.theme_color, (670,170), 45)
            self.image_not_center("image1", 640, 140, 60, 60, f"profil/profil{self.pict[1]}")
            if self.is_mouse_over_button(self.picture2):
                self.picture2_cursor = True
                self.hover_profil2 = pygame.draw.circle(self.Window, self.yellow, (670, 170), 45, 4, True, False, True, False) 
                self.hover_profil2 = pygame.draw.circle(self.Window, self.pink, (670, 170), 45, 4, False, True, False, True) 
                self.hand_cursor()
            else:
                self.picture2_cursor = False

        if self.size_profile_picture > 370:
            self.picture3 = pygame.draw.circle(self.screen.Window, self.theme_color, (770,170), 45)
            self.image_not_center("image1", 740, 140, 60, 60, f"profil/profil{self.pict[2]}")
            if self.is_mouse_over_button(self.picture3):
                self.picture3_cursor = True
                self.hover_profil3 = pygame.draw.circle(self.Window, self.yellow, (770, 170), 45, 4, True, False, True, False) 
                self.hover_profil3 = pygame.draw.circle(self.Window, self.pink, (770, 170), 45, 4, False, True, False, True) 
                self.hand_cursor()
            else:
                self.picture3_cursor = False
        self.hover_profile_picture()
        self.status_circle()

    def password_show(self):
        if not self.password_edit:
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
        self.button_hover(title, 1000, y + 15, 80, 30, self.pink, self.pink, self.purple2, self.purple2, "Edit", self.font5, self.white, 17, 0, 4)
        self.info_profil_cursor(title)

# White rectangle when 'Edit' is pressed
    def info_profil_edit(self):
        # Username info 
        self.rect_full_not_centered(self.white, 420, 320, 0 + self.size_username, 20, 10)
        if self.username_edit:
            if self.size_username < 240:
                self.size_username += 15
            self.text_not_align(self.font2, 16, self.username, self.black, 440, 320)
        else:
            if self.size_username < 15:
                self.size_username = 0
            if self.size_username > 0:
                self.text_not_align(self.font2, 16, self.username, self.black, 440, 320)
                self.size_username -= 20
            else: 
                self.text_not_align(self.font2, 16, self.username, self.white, 440, 320)

        # Email info 
        self.rect_full_not_centered(self.white, 420, 380, 0 + self.size_email, 20, 10)
        if self.email_edit:
            if self.size_email < 240:
                self.size_email += 15
            self.text_not_align(self.font2, 16, self.email, self.black, 440, 380)
        else:
            if self.size_email < 15:
                self.size_email = 0
            if self.size_email > 0:
                self.text_not_align(self.font2, 16, self.email, self.black, 440, 380)
                self.size_email -= 20
            else: 
                self.text_not_align(self.font2, 16, self.email, self.white, 440, 380)

        # Password info 
        self.rect_full_not_centered(self.white, 420, 440, 0 + self.size_password, 20, 10)
        if self.password_edit:
            if self.size_password < 240:
                self.size_password += 15
            self.text_not_align(self.font2, 16, self.password, self.black, 440, 440)
        else:
            if self.size_password < 15:
                self.size_password = 0
            elif self.size_password > 0:
                self.size_password -= 20
            if self.size_password < 100:
                if self.show_pass:
                    self.text_not_align(self.font2, 16, self.password, self.white, 440, 440)
                else:
                    self.password_display = " *" * len(self.password)
                    self.text_not_align(self.font2, 16, self.password_display, self.white, 440, 440)
            else:
                self.text_not_align(self.font2, 16, self.password, self.black, 440, 440)

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
            self.info_profil_edit()
            self.password_show()
            self.profile_picture_edit()
            self.update()
            
pro = Profil()
pro.profil_run()