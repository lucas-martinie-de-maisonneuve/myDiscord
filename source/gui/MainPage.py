import pygame
from datetime import datetime, timedelta
from data.DiscordManager import DiscordManager
from source.pygame_manager.Gui import Gui
from source.Client import Client

class MainPage(Gui, Client, DiscordManager):
    
    def __init__(self, user_info):
        Client.__init__(self)
        DiscordManager.__init__(self)  
        Gui.__init__(self)
        self.user_info = user_info
        self.last_login_date = ""
        self.input_search = "Search..."
        self.RECT_W = 600
        self.RECT_H= 60 
        self.L_MAX = 80
        self.link_is_clicked = True
        self.entry = 0
        self.scroll = 0
        self.channel_rects = []

        self.bell = pygame.Rect(1075, 15, 50, 50)
        self.poweroff_c = pygame.Rect(64-115/2, 635-115/2, 115, 115)
        self.settings_c = pygame.Rect( 64-115/2, 540-115/2, 115, 115)
        self.server_c =  pygame.Rect(64-115/2, 170-115/2, 115, 115)
        self.notification_c= pygame.Rect(1052, 25, 30, 30)
        
    def background(self): 
        self.img_background("Background", 600, 350, 1200, 800, "main_page/main_page8")
   
    def banner(self):
        # Rect Background 
        self.rect_full(self.grey10, 655, 40, 1055, 60, 10)

        # Logo Names
        self.image_not_center("Names", 155, 15, 200, 57,"main_page/main_page17") 
        self.image_not_center("Rectangle logo", 120, 1, 270, 75,"main_page/main_page18") 

        # Search bar
        self.input_search_rect = self.rect_full(self.grey2, 920, 40, 240, 35, 80)
        self.text_not_align(self.font2, 15, self.input_search, self.white, 810, 30.5)
        self.image_not_center("Search logo", 1000, 25, 30, 30,"main_page/main_page16")

        # Logo bell
        self.image_not_center("Bell logo", 1075, 15, 50, 50,"main_page/main_page19") 

        # Link to the LaPlateforme website  
        self.image_not_center("Question mark", 1120, 15, 50, 50,"main_page/main_page15")    
        self.link_logo_rect = pygame.Rect(1120, 15, 50, 50)
        self.url = "https://laplateforme.io/"

    def first_section(self):
        # First section background color
        self.rect_full(self.grey10, 65, 350, 90, 680, 10)

        # Main Logo    
        self.image_not_center("Logo principal", 20, 25, 95, 95,"main_page/main_page3")   

        # Hover server
        self.circle1 = pygame.draw.circle(self.Window, self.grey10, (64, 170), 35)     
        if self.is_mouse_over_button(self.circle1):      
            self.img_center("Logo principal", 64, 170, 70, 70,"main_page/main_page2")
            self.img_center("Neon circle", 64, 170, 115, 115,"main_page/main_page4")
        else:          
            self.img_center("Logo principal", 64, 170, 70, 70,"main_page/main_page2")
            self.img_center("Neon circle", 64, 170, 110, 110,"main_page/main_page4")
               
        # Hover settings
        self.circle2 = pygame.draw.circle(self.Window, self.grey10, (64, 540), 35)
        if self.is_mouse_over_button(self.circle2):           
            self.img_center("Neon server", 64, 540, 85, 85,"main_page/main_page5")
            self.img_center("Neon circle", 64, 540, 115, 115,"main_page/main_page4")   
        else:      
            self.img_center("Neon server", 64, 540, 85, 85,"main_page/main_page5")
            self.img_center("Neon circle", 64, 540, 110, 110,"main_page/main_page4") 

        # Hover Power Off
        self.circle3 = pygame.draw.circle(self.Window, self.grey10, (64, 635), 35)
        if self.is_mouse_over_button(self.circle3):     
            self.img_center("Power Off", 64, 635, 60, 60,"main_page/main_page9")
            self.img_center("Neon circle", 64, 635, 115, 115,"main_page/main_page4")   
        else:      
            self.img_center("Power Off", 64, 635, 60, 60,"main_page/main_page9")
            self.img_center("Neon circle", 64, 635, 110, 110,"main_page/main_page4") 
        
    def second_section(self):
        self.rect_full(self.grey10, 257, 385, 260, 610, 10)

        position_y = 50

        for category in self.categories:
            position_y += 60  
            self.text_not_align(self.font1, 18, category[1], self.grey1, 200, position_y)
            self.img_center("Neon light", 260, position_y - 20, 140, 105,"main_page/main_page7")
            for channel in self.channels:
                if channel[4] == category[0]:
                    position_y += 20
                    channel_rect = pygame.Rect(200, position_y, 150, 20)
                    self.channel_rects.append((channel[0], channel_rect))
                    if self.is_mouse_over_button(channel_rect):
                        self.text_not_align(self.font2, 17, channel[1], self.pink, 200, position_y)
                    else:
                        self.text_not_align(self.font2, 15, channel[1], self.grey1, 200, position_y)
                    if channel[4] == 1:
                        self.img_center("Book about us", 170, position_y + 10, 25, 25, "main_page/main_page12")
                    elif channel[3] == 1:
                        self.img_center("Volume logiciel", 170, position_y + 10, 25, 25, "main_page/main_page10")
                    else:
                        self.img_center("Hashtags logiciel", 170, position_y + 10, 15, 15, "main_page/main_page14")
    
    def third_section(self):
        self.rect_full(self.grey10, 795, 385, 775, 610, 10)
        self.display_text_chat()
        self.input_write_user()

    def split_string(self, string, length):
        result = []
        start_index = 0

        while start_index < len(string):
            end_index = start_index + length
            
            while end_index < len(string) and string[end_index] != ' ':
                end_index -= 1
            
            result.append(string[start_index:end_index])
            start_index = end_index + 1

        return result
    
    def display_text_chat(self):
        pos_y = 610
        
        for message in reversed(self.messages):
            if message[4] == self.actual_channel:
                message_content = str(message[3])
                message_name = message[1]
                message_time = message[2]
                self.message_picture = self.get_profile_picture(message_name)
                if self.message_picture:
                    self.str_picture = self.message_picture[0][0]

                chunked_strings = self.split_string(message_content, 101)
                rectangle_height = len(chunked_strings) * 30  
                pos_y -= rectangle_height + 40

                for j, chunk in enumerate(chunked_strings):
                    self.text_not_align(self.font2, 16, str(chunk), self.grey1, 480, ((30 * j) + pos_y + 20 + self.scroll))
                self.text_not_align(self.font1, 18, str(message_name), self.pink, 480, pos_y + 5 + self.scroll)
                self.text_not_align(self.font1, 10, str(message_time), self.grey1, 590, pos_y + 10 + self.scroll)
                self.img_center("bubble", 460, pos_y + 10 + self.scroll, 40, 40, "main_page/main_page4")
                self.img_center("ProfilePicture", 460, pos_y + 10 + self.scroll, 35, 35, f'profile/profile{self.str_picture}')
        self.img_center("Background",795, 40, 775, 80, "main_page/main_page20")
        self.img_center("Background",795, 660, 775, 80, "main_page/main_page21")
        self.entry_message = self.rect_full(self.grey10, 795, 650, 650, 60, 10)
        self.rect_border(self.grey4, 795, 650, 650, 60, 2, 10)
        self.send_button = self.hover_image("send_button", "Send_button", 1080, 650, 45, 45, "main_page/main_page22", "main_page/main_page22")
        
    def input_write_user(self): 

        split_text = []
        line = ""
        words = self.message.split(" ")
        for word in words:
            if len(line) + len(word) < self.L_MAX:
                line += word + " "
            else:
                split_text.append(line.strip())
                line = word + " "
        split_text.append(line.strip())

        for i, ligne in enumerate(split_text):
            self.text_not_align(self.font2, 17, ligne, self.grey1, 510, 625.5 + i * 15)

    def notification(self): 
        if self.last_login_date == "":
            self.last_login_date = self.load_info_last_message(self.user_info[0])

        # Save info when connect
            for message in self.messages: 
                
                if message[2] > self.last_login_date: 
                    self.new_message = self.new_message + 1

        self.text_center(self.font1, 20, str(self.new_message), self.pink1, 1067, 42)
        self.image_not_center("Circle notification",1052, 25, 30, 30,"main_page/main_page23")
        
    def mainPage_run(self):
        while self.main_page_running :
            self.update_message()
            self.background()
            self.first_section()
            self.second_section()
            self.third_section()
            self.banner() 
            self.event_main_page()
            self.main_page_cursor()

            self.notification()

            self.update()
