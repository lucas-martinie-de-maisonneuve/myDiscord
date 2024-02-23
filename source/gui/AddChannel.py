import pygame

from pygame_manager.EventHandler import EventHandler
from pygame_manager.Element import Element
from data.DiscordManager import DiscordManager

class AddChannel(Element, EventHandler, DiscordManager):

    def __init__(self, user):
        Element.__init__(self)
        DiscordManager.__init__(self)
        EventHandler.__init__(self)
        self.user = user
        self.add_channel_running = True
        self.new_name_channel = ""
        self.entry_new_name = 0

    def background(self): 
        self.img_background("Background", 600, 350, 1200, 800, "main_page/main_page8")
        
    def second_section(self):
        self.rect_full(self.grey10, 257, 385, 260, 610, 10)

        self.text_not_align(self.font1, 18, self.name_category1, self.grey1, 200, (190*a) +100)

        self.text_not_align(self.font2, 15, self.name_channel1, self.grey1, 200, (20*i)+120)
        self.img_center("Book about us", 170, (20*i)+125, 25, 25,"main_page/main_page12")

        self.img_center("Volume logiciel", 170,(20*i)+530, 25, 25,"main_page/main_page10")
        self.img_center("Hashtags logiciel", 170, (20*i)+530, 15, 15,"main_page/main_page14") 
    
        # Neon light blue
        self.img_center("Neon light", 260, 230, 140, 105,"main_page/main_page7")
        self.img_center("Neon light", 260, 430, 140, 105,"main_page/main_page7")
        self.img_center("Neon Light", 260, 630, 140, 105,"main_page/main_page7")    

    def addChannel_run(self):
        while self.add_channel_running :
            if not self.profile.add_channel_running:                
                self.background()
                self.second_section()
                self.event_main_page()
                self.update()

test = AddChannel()
test.addChannel_run()