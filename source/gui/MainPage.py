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

        self.nb_category = self.count_category()
        self.nb_category = self.nb_category[0]

        for a in range(self.nb_category):
            self.nb_channels = self.count_channel(a+1)
            self.nb_channels = self.nb_channels[0]

            self.name_category1 = self.name_category()
            self.str_name2 = self.name_category1[a][0]
            self.name_category1 = f'{self.str_name2} '
            self.text_not_align(self.font1, 18, self.name_category1, self.grey1, 200, (190*a) +100)

            for i in range(self.nb_channels):
                self.name_channel1 = self.name_channel(a+1)                
                self.str_name3 = self.name_channel1[i][0]
                self.name_channel1 = f'{self.str_name3} '

                for _ in range(self.nb_channels):

                    if a==0:
                        self.text_not_align(self.font2, 15, self.name_channel1, self.grey1, 200, (20*i)+120)
                        self.img_center("Book about us", 170, (20*i)+125, 25, 25,"main_page/main_page12")

                    elif a == 1:
                        self.text_not_align(self.font2, 15, self.name_channel1, self.grey1, 200, (20*i)+320)

                        self.communication = self.communication_channel(a+1)
                        self.str_communication1= self.communication[i][0]
                        self.communication = f'{self.str_communication1}'

                        if self.communication == "0":
                            self.img_center("Volume logiciel", 170,(20*i)+310, 25, 25,"main_page/main_page10")
                        elif self.communication == "1": 
                            self.img_center("Hashtags logiciel", 170, (20*i)+350, 15, 15,"main_page/main_page14") 

                    elif a==2:
                        self.communication = self.communication_channel(a+1)
                        self.text_not_align(self.font2, 15, self.name_channel1, self.grey1, 200, (20*i)+520)
                        self.communication = self.communication_channel(a+1)
                        self.str_communication1= self.communication[i][0]                        
                        self.communication = f'{self.str_communication1}'

                        if self.communication == "0":
                            self.img_center("Volume logiciel", 170,(20*i)+530, 25, 25,"main_page/main_page10")
                        elif self.communication == "1":                             
                            self.img_center("Hashtags logiciel", 170, (20*i)+530, 15, 15,"main_page/main_page14") 
     
        # Neon light blue
        self.img_center("Neon light", 260, 230, 140, 105,"main_page/main_page7")
        self.img_center("Neon light", 260, 430, 140, 105,"main_page/main_page7")
        self.img_center("Neon Light", 260, 630, 140, 105,"main_page/main_page7")    

    def third_section(self):
        self.rect_full(self.grey10, 795, 385, 775, 610, 10)
        self.display_text_chat(3)
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
    
    def display_text_chat(self, id_channel): 
        
        self.entry_message = self.rect_full(self.grey1, 795, 650, 650, 60, 10)

        self.nb_message = self.count_message(id_channel)
        self.nb_message = self.nb_message[0]
        self.nb =  self.nb_message
    
        pos_y = 610
            
        for i in reversed(range(self.nb)):
            self.message_1 = self.message_message(id_channel)
            self.str_name2 = self.message_1[i][0]
            self.message_1 = f'{self.str_name2} '

            self.message_name = self.name_message(id_channel)
            self.str_name1 = self.message_name[i][0]
            self.message_name = f'{self.str_name1} '
            
            self.message_time1 = self.time_message(id_channel)
            self.str_name3 = self.message_time1[i][0]
            self.message_time1 = f'{self.str_name3} '
          
            chunked_strings = self.split_string(self.message_1, 101)
            rectangle_height = len(chunked_strings) * 30  
            pos_y -= rectangle_height + 40 

            for j, chunk in enumerate(chunked_strings):
                self.text_not_align(self.font2, 16, chunk, self.grey1, 480, ((30 * j) + pos_y + 20))
            self.text_not_align(self.font1, 18, self.message_name, self.pink, 480, (pos_y + 5))
            self.text_not_align(self.font1, 10, self.message_time1, self.grey1, 590, (pos_y+10))

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
