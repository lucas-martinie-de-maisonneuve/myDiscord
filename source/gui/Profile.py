import pygame
from source.pygame_manager.Gui import Gui
from source.Client import Client

class Profile( Gui, Client):
    
    def __init__(self, user_info):
        Gui.__init__(self)
        Client.__init__(self)

        self.community_list = self.display_user()  
        self.user = user_info   
        self.edit = 0
        self.password_edit, self.username_edit, self.email_edit, self.picture_edit, self.status_edit = False, False, False, False, False
        self.theme_color = self.purple4

        self.show_pass = False
        self.status = "Online"
        self.status_color = self.green
        self.size_username, self.size_email ,self.size_password, self.size_profile_picture= 0, 0, 0, 0
        self.pict = []
        self.picture1 = pygame.Rect(0, 0, 0, 0)
        self.picture2 = pygame.Rect(0, 0, 0, 0)
        self.picture3 = pygame.Rect(0, 0, 0, 0)
        self.username_rect = pygame.Rect(960, 300, 80, 30)
        self.email_rect = pygame.Rect(960, 360, 80, 30)
        self.password_rect = pygame.Rect(960, 420, 80, 30)
        self.role_rect = pygame.Rect(960, 480, 80, 30)
        self.status_rect = pygame.Rect(960, 540, 80, 30)

    def display_user_community(self):
        self.rect_full(self.grey2, 195, 250, 250, 380, 10)
        self.rect_border(self.grey4, 195, 250, 250, 380, 1, 10)
        self.text_not_align(self.font1, 18,"People You May Know..." , self.white, 90, 85)

        pos_y = 0  
        for i, user_community in enumerate(self.community_list[:10]): 
            pos_y = pos_y + 30
            self.text_not_align(self.font2, 20,str(user_community[3]), self.white, 150, 95 + pos_y)  
            self.image_not_center("ProfilePicture", 90, pos_y + 90, 35, 35, f'profile/profile{user_community[6]}')

    def design(self):
        # Profile main rectangle
        self.img_background("Background", 600, 350, 1200, 700, "main_page/main_page8")
        self.rect_radius_top(self.theme_color, 750, 90, 800, 100, 10)
        self.rect_radius_bot(self.grey5, 750, 400, 800, 520, 10)
        
        # Left rectangle
        self.rect_full(self.grey5, 195, 350, 290, 620, 10) 
        
        # Username
        if self.size_profile_picture < 100:
            self.text_not_align(self.font1, 20, f"{self.username}", self.white, 550,180 + self.size_profile_picture // 2)
        else:
            self.text_not_align(self.font1, 20, f"{self.username}", self.white, 550,230)
        
        # Profile info rectangle
        self.rect_full(self.grey2, 750, 445, 700, 350, 10)
        self.rect_border(self.grey4, 750, 445, 700, 350, 1, 10)
        
        # Info profile
        self.info_profile("Username", self.username, 300)
        self.info_profile("E-mail", self.email, 360)
        self.info_profile("Password", self.password_display, 420)
        self.info_profile("Role", self.role, 480)
        self.info_profile("Status", self.role, 540)
     
        # Creators button
        self.contact_button = self.lateral_menu_display(475, "profile/profile6", "profile9", "profile9")        

        # Disconnect button
        self.disconnect_button = self.lateral_menu_display(575, "main_page/main_page9", "disconnect_hover", "disconnect")

    def lateral_menu_display(self, y, logo, image_neon_hover, image_neon):
        button = pygame.Rect(55, y, 300, 60)
        if self.is_mouse_over_button(button):
            self.img_center("Logo principal", 100, y + 30, 50, 50, f"{logo}")
            self.img_center("Neon circle", 100, y + 30, 100, 100, "main_page/main_page4")
            self.img_center("Logo inside circle", 242, y + 30, 210, 59, f"profile/{image_neon_hover}")
        else:
            self.img_center("Logo principal", 100, y + 30, 50, 50, f"{logo}")
            self.img_center("Neon circle", 100, y + 30, 95, 95, "main_page/main_page4")
            self.img_center("Logo inside circle", 240, y + 30, 200, 57, f"profile/{image_neon}")
        return button  

    def hover_profile_picture(self):
        self.circle(self.grey5, 450, 180, 70)
        self.img_center("bubble", 450, 180, 130, 130, f"register/register1")
        # Profile picture
        self.profile_pict = pygame.draw.circle(self.Window, self.theme_color, (450,180), 65)
        if self.is_mouse_over_button(self.profile_pict):
            self.img_center("profile_picture", 450,180,130,130,f"profile/profile{self.picture}")
            self.circle_alpha(self.alpha_grey, 450, 180, 65)
            self.img_center("logo edit", 450,180,50,50,"profile/logo_edit")
            self.img_center("bubble", 450, 180, 175, 175, f"main_page/main_page4")

        else:
            self.picture_cursor = False
            self.circle(self.theme_color, 450, 180, 65)
            self.img_center("profile_picture", 450,180,130,130,f"profile/profile{self.picture}")
        # Status color 
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
            self.theme_color = self.purple3
        elif self.picture == 2:
            self.pict = [1, 3, 4]
            self.theme_color = self.blue2
        elif self.picture == 3:
            self.pict = [1, 2, 4]
            self.theme_color = self.purple4
        elif self.picture == 4:
            self.pict = [1, 2, 3]
            self.theme_color = self.blue3
        if self.picture_edit:
            if self.size_profile_picture < 400:
                self.size_profile_picture += 10
        else:
            if self.size_profile_picture > 0:
                self.size_profile_picture -=10
        self.rect_full_not_centered(self.grey3, 440, 120, 0 + self.size_profile_picture, 100, 50)
        if self.size_profile_picture > 170:
            self.picture1 = pygame.draw.circle(self.Window, self.theme_color, (570,170), 45)
            self.image_not_center("image1", 525, 125, 90, 90, f"profile/profile{self.pict[0]}")
            if self.is_mouse_over_button(self.picture1):
                self.image_not_center("bubble", 510, 110, 120, 120, f"main_page/main_page4")

        if self.size_profile_picture > 270:
            self.picture2 = pygame.draw.circle(self.Window, self.theme_color, (670,170), 45)
            self.image_not_center("image1", 625, 125, 90, 90, f"profile/profile{self.pict[1]}")
            if self.is_mouse_over_button(self.picture2):
                self.image_not_center("bubble", 610, 110, 120, 120, f"main_page/main_page4")

        if self.size_profile_picture > 370:
            self.picture3 = pygame.draw.circle(self.Window, self.theme_color, (770,170), 45)
            self.image_not_center("image1", 725, 125, 90, 90, f"profile/profile{self.pict[2]}")
            if self.is_mouse_over_button(self.picture3):
                self.image_not_center("bubble", 710, 110, 120, 120, f"main_page/main_page4")

        self.hover_profile_picture()
        self.status_circle()

    def password_show(self):
        if not self.password_edit:
            self.show = pygame.Rect(450 + 10 * len(self.profile_password),443,35,15)
            if self.is_mouse_over_button(self.show):
                self.text_not_align(self.font2, 16, f"show",self.blue1,450 + 10 * len(self.profile_password), 437)
            else:
                self.text_not_align(self.font2, 14, f"show",self.grey1,450 + 10 * len(self.profile_password), 438)

    def info_profile(self, title, text_info, y):
        self.text_not_align(self.font1, 16, title, self.grey6, 430, y)
        self.button_hover(title, 1000, y + 15, 80, 30, self.pink, self.pink, self.purple2, self.purple2, "Edit", self.font5, self.white, 17, 0, 4)

    # White rectangle when 'Edit' is pressed
    def info_profile_edit(self):
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
            self.text_not_align(self.font2, 16, self.profile_password, self.black, 440, 442)
        else:
            if self.size_password < 15:
                self.size_password = 0
            elif self.size_password > 0:
                self.size_password -= 20
            if self.size_password < 100:
                if self.show_pass:                    
        
                    self.text_not_align(self.font2, 16, self.profile_password, self.white, 440, 442)
                else:
                    self.password_display = " *" * len(self.profile_password)
                    self.text_not_align(self.font2, 16, self.password_display, self.white, 440, 442)
            else:
                self.text_not_align(self.font2, 16, self.profile_password, self.black, 440, 442)

        # Quit
            self.close_profile = self.hover_image("Quit", "Quit", 1120, 70, 50, 50, "profile/profile11", "profile/profile8")

    def profile_run(self):
        if self.profile_password == "":
            user_id = self.user[0]
            self.profile_password = self.abc_password(user_id) 
            
        self.username, self.email, self.picture, self.role = self.user[3], self.user[4], self.user[6], self.user[7]
        self.password_display = " *" * len(self.profile_password)

        if self.profile_running :
            self.design()
            self.display_user_community()
            self.profile_picture_edit()
            self.info_profile_edit()
            self.password_show()
            self.event_profile()
            self.profile_page_cursor()