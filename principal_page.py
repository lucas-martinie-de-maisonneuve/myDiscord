import pygame
from source.pygame_manager.element import Element
from source.pygame_manager.screen import Screen
from data.discord_manager import Discord_Manager

class Main_page(Element, Screen,Discord_Manager):
    def __init__(self):
        Screen.__init__(self)
        Element.__init__(self)
        Discord_Manager.__init__(self)
        pygame.init()
        
    def banner(self):
        self.rect_full(self.grey4, 645, 35, 1110, 70, 0)

    def FirstSection(self):
        self.rect_full(self.grey8, 45, 350, 90, 700, 0)

    def SecondSection(self):
        self.rect_full(self.grey7, 220, 385, 260, 630, 0)

        self.nb_category = self.count_category()
        self.nb_category = self.nb_category[0]

        for a in range(self.nb_category):
            self.nb_channels = self.count_channel(a+1)
            self.nb_channels = self.nb_channels[0]

            self.name_category1 = self.name_category()
            self.str_name2 = self.name_category1[a][0]
            self.name_category1 = f'{self.str_name2} '
            self.text_center(self.font1, 18, self.name_category1, self.grey1, 170, (190*a) +100)

            for i in range(self.nb_channels):
                self.name_channel1 = self.name_channel(a+1)
                self.str_name3 = self.name_channel1[i][0]
                self.name_channel1 = f'{self.str_name3} '
                
                for _ in range(self.nb_channels):
                    if a==0:
                        self.text_center(self.font2, 15, self.name_channel1, self.grey1, 200, (20*i)+120)
                    elif a==1:
                        self.text_center(self.font2, 15, self.name_channel1, self.grey1, 200, (20*i)+320)
                    elif a==2:
                        self.text_center(self.font2, 15, self.name_channel1, self.grey1, 200, (20*i)+520)
                
        # nb_categories = self.count_category()[0]

        # for a in range(nb_categories):
        #     nb_channels = self.count_channel(a + 1)[0]

        #     name_category_item = f'{self.name_category()[a][0]} '
        #     self.text_center(self.font1, 18, name_category_item, self.grey1, 170, (190 * a) + 100)

        #     for i in range(nb_channels):
        #         name_channel_item = f'{self.name_channel(a + 1)[i][0]} '
        #         position = (20 * i) + (120 if a == 0 else 320 if a == 1 else 520)
        #         self.text_center(self.font1, 15, name_channel_item, self.grey1, 200, position)

    def ThirdSection(self):
        self.rect_full(self.grey6, 775, 385, 850, 630, 0)

    def DisplayAll(self): 
        self.FirstSection()
        self.SecondSection()
        self.ThirdSection()
        self.banner()

    def event_main_page(self):
        self.main_page_running = True
        while self.main_page_running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.main_page_running = False

            self.DisplayAll()
            self.update()

main_page = Main_page()
main_page.event_main_page()