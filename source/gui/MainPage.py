import pygame

from source.pygame_manager.EventHandler import EventHandler
from source.pygame_manager.Element import Element
from data.DiscordManager import DiscordManager
from source.gui.Profile import Profile

class MainPage(Element, EventHandler, DiscordManager):
    
    def __init__(self, user):
        Element.__init__(self)
        DiscordManager.__init__(self)
        EventHandler.__init__(self)
        self.user = user
        self.profile = Profile(self.user)
        self.main_page_running = False
        self.input_search = "Search..."
        self.message = ""
        self.RECT_W = 600
        self.RECT_H= 60 
        self.L_MAX = 80
        self.link_is_clicked = True
        self.entry = 0

        self.categories = self.display_category()
        self.channels = self.display_channel()
        self.messages = self.display_message()
        self.actual_channel = 7

    def background(self): 
        self.img_background("Background", 600, 350, 1200, 800, "main_page/main_page8")
   
    def banner(self):

        # Rect Background 
        self.rect_full(self.grey10, 655, 40, 1055, 60, 10)

        # Logo Names
        self.image_not_center("Names", 155, 15, 200, 57,"main_page/main_page17") 
        self.image_not_center("Rectangle logo", 120, 12, 270, 55,"main_page/main_page18") 

        # Search bar
        self.input_search_rect = self.rect_full(self.grey2, 920, 40, 240, 35, 80)
        self.text_not_align(self.font2, 15, self.input_search, self.white, 810, 30.5)
        self.image_not_center("Search logo", 1000, 25, 30, 30,"main_page/main_page16")

        # Logo bell
        self.image_not_center("Bell logo", 1060, 15, 50, 50,"main_page/main_page19") 

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
            self.img_center("Logo principal", 64, 170, 115, 115,"main_page/main_page4")
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
        if self.is_mouse_over_button(self.circle2):           
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
                    self.text_not_align(self.font2, 15, channel[1], self.grey1, 200, position_y)
                    if channel[4] == 1:
                        self.img_center("Book about us", 170, position_y + 5, 25, 25, "main_page/main_page12")
                    elif channel[3] == 1:
                        self.img_center("Volume logiciel", 170, position_y + 5, 25, 25, "main_page/main_page10")
                    else:
                        self.img_center("Hashtags logiciel", 170, position_y + 5, 15, 15, "main_page/main_page14")
  
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
        self.entry_message = self.rect_full(self.grey1, 795, 650, 650, 60, 10)
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
                    self.text_not_align(self.font2, 16, str(chunk), self.grey1, 480, ((30 * j) + pos_y + 20))
                self.text_not_align(self.font1, 18, str(message_name), self.pink, 480, (pos_y + 5))
                self.text_not_align(self.font1, 10, str(message_time), self.grey1, 590, (pos_y+10))
                self.img_center("bubble", 460, (pos_y + 10), 40, 40, "main_page/main_page4")
                self.img_center("ProfilePicture", 460, (pos_y + 10), 35, 35, f'profile/profile{self.str_picture}')

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
            self.text_not_align(self.font2, 17, ligne, self.black, 510, 620 + i * 15)

    def mainPage_run(self):
        while self.main_page_running :
            if not self.profile.profile_running:                
                self.background()
                self.first_section()
                self.second_section()
                self.third_section()
                self.banner() 
                self.event_main_page()
                self.update()
