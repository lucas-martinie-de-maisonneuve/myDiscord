import pygame
class Cursor:
    def __init__(self):
        # Profile page __init__
        self.username_rect = pygame.Rect(960, 300, 80, 30)
        self.email_rect = pygame.Rect(960, 360, 80, 30)
        self.password_rect = pygame.Rect(960, 420, 80, 30)
        self.role_rect = pygame.Rect(960, 480, 80, 30)
        self.status_rect = pygame.Rect(960, 540, 80, 30)
        self.picture1 = pygame.Rect(0, 0, 0, 0)
        self.picture2 = pygame.Rect(0, 0, 0, 0)
        self.picture3 = pygame.Rect(0, 0, 0, 0)

        self.password_cursor, self.pass_cursor, self.picture_cursor, self.username_cursor, self.email_cursor, self.role_cursor, self.status_cursor, self.picture1_cursor, self.picture2_cursor, self.picture3_cursor, self.disconnect_cursor, self.status_edit_cursor, self.status_active_cursor = False, False, False, False, False, False, False, False, False, False, False, False, False



    def profil_page_cursor(self):

        if not (self.password_cursor or self.picture_cursor or self.username_cursor or self.email_cursor or self.pass_cursor or self.role_cursor or self.status_cursor or self.picture1_cursor or self.picture2_cursor or self.picture3_cursor or self.disconnect_cursor or self.status_edit_cursor or self.status_active_cursor):
            self.normal_cursor()

# Cursor for disconnect button
        self.disconnect_button = pygame.Rect(95, 590, 200, 57)
        if self.is_mouse_over_button(self.disconnect_button):
            self.disconnect_cursor = True
            self.hand_cursor()
            self.img_center("disconnect", 195, 620, 220, 63, "profil/disconnect_hover")
        else:
            self.img_center("disconnect", 195, 620, 200, 57, "profil/disconnect")
            self.disconnect_cursor = False

# Cursor for profile picture
        self.profile_pict = pygame.draw.circle(self.screen.Window, self.theme_color, (450,180), 65)
        if self.is_mouse_over_button(self.profile_pict):
            self.picture_cursor = True
            self.hand_cursor()
        else:
            self.picture_cursor = False

# Cursor for status rect edition
        self.status_edit_rect = pygame.Rect(540, 570, 80, 20)
        self.status_active_rect = pygame.Rect(440, 570, 80, 20)
        if self.status_edit:
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

# Cursor for profile pictures edition
        self.picture1 = pygame.draw.circle(self.screen.Window, self.theme_color, (570,170), 45)
        if self.size_profile_picture > 170:
            if self.is_mouse_over_button(self.picture1):
                self.picture1_cursor = True
                self.hand_cursor()
            else:
                self.picture1_cursor = False

        self.picture2 = pygame.draw.circle(self.screen.Window, self.theme_color, (670,170), 45)
        if self.size_profile_picture > 270:
            if self.is_mouse_over_button(self.picture2):
                self.picture2_cursor = True
                self.hand_cursor()
            else:
                self.picture2_cursor = False

        self.picture3 = pygame.draw.circle(self.screen.Window, self.theme_color, (770,170), 45)
        if self.size_profile_picture > 370:
            if self.is_mouse_over_button(self.picture3):
                self.picture3_cursor = True
                self.hand_cursor()
            else:
                self.picture3_cursor = False

# Cursor on show button to display password
        self.show = pygame.Rect(450 + 10 * len(self.password),443,35,15)
        if not self.password_edit:
            if self.is_mouse_over_button(self.show):
                self.password_cursor = True
                self.hand_cursor()
            else:
                self.password_cursor = False

# Cursor on edit buttons (profil page)
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

