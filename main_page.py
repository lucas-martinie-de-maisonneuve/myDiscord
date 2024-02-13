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
        # First section background color
        self.rect_full(self.grey7, 45, 350, 90, 700, 0)

        # Main Logo    
        self.image_not_center("Logo prinicpal", 2, 0, 90, 90,"main_page/main_page3")       

        # Hover server
        self.cercle1 = pygame.draw.circle(self.Window, self.grey7, (44, 120), 35)     
        if self.is_mouse_over_button(self.cercle1):      
            self.img_center("Logo prinicpal", 44, 120, 75, 75,"main_page/main_page2")
            self.img_center("Logo prinicpal", 44, 120, 115, 115,"main_page/main_page4")
        else:          
            self.img_center("Logo prinicpal", 44, 120, 85, 85,"main_page/main_page2")
        
        # Hover settings
        self.cercle2 = pygame.draw.circle(self.Window, self.grey7, (45, 655), 35)
        if self.is_mouse_over_button(self.cercle2):           
            self.img_center("Logo prinicpal", 44, 640, 115, 115,"main_page/main_page4")   
            self.img_center("settings", 44, 635, 85, 85,"main_page/main_page5")
            self.img_center("settings", 55, 665, 30, 30,"main_page/main_page5")
        else:      
            self.img_center("settings", 44, 635, 90, 90,"main_page/main_page5")
            self.img_center("settings", 55, 665, 35, 35,"main_page/main_page5")

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
                        
        pygame.draw.line(self.Window, self.grey4, (100, 80), (300, 80), 3)
        pygame.draw.line(self.Window, self.grey4, (100, 270), (300, 270), 3)
        pygame.draw.line(self.Window, self.grey4, (100, 460), (300, 460), 3)

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