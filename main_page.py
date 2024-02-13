import pygame

from source.pygame_manager.event_handler import Event_handler
from source.pygame_manager.element import Element
from source.pygame_manager.screen import Screen
from data.discord_manager import Discord_Manager

class Main_page(Element, Screen, Event_handler, Discord_Manager):
    
    def __init__(self):
        Screen.__init__(self)
        Element.__init__(self)
        Event_handler.__init__(self)
        Discord_Manager.__init__(self)
        pygame.init()

    def banner(self):
        self.rect_full(self.grey8, 645, 35, 1110, 70, 0)   

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
        self.rect_full(self.green, 220, 385, 260, 630, 0)
           
    def ThirdSection(self): 
        self.rect_full(self.blue, 775, 385, 850, 630, 0)

    def DisplayAll(self): 
      
        self.FirstSection()
        self.SecondSection()
        self.ThirdSection()
        self.banner()
        # self.profil_hover()

    def event_main_page(self):
        main_page_running = True
        while main_page_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_page_running = False    

            self.DisplayAll() 
            self.update()

main_page = Main_page()
main_page = main_page.event_main_page()