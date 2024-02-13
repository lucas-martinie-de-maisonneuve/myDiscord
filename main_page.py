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
        self.rect_full(self.pink, 645, 35, 1110, 70, 0)

    
    def profil_hover(self):

        # Position hover
        self.cercle1 = pygame.draw.circle(self.Window, self.black, (45, 120), 35)
        self.cercle2 = pygame.draw.circle(self.Window, self.black, (45, 655), 35)

        # Hover cercle     
        if self.is_mouse_over_button(self.cercle1):
            pygame.draw.circle(self.Window, self.grey8, (45, 120), 35)
            pygame.draw.circle(self.Window, self.red, (45, 120), 35, width=2)  
            # self.image_not_center("Logo prinicpal", 0, 60, 90, 90,"main_page/main_page3")
        else:
            pygame.draw.circle(self.Window, self.grey8, (45, 120), 35)
            pygame.draw.circle(self.Window, self.grey8, (45, 120), 35, width=2)
            # self.image_not_center("Logo prinicpal", 0, 60, 90, 90,"main_page/main_page3")
        
        if self.is_mouse_over_button(self.cercle2):
            pygame.draw.circle(self.Window, self.grey8, (45, 655), 35)
            pygame.draw.circle(self.Window, self.red, (45, 655), 35, width=2) 
            self.image_not_center("Logo prinicpal", 0, 120, 90, 90,"main_page/main_page3") 
        else:
            pygame.draw.circle(self.Window, self.grey8, (45, 655), 35)
            pygame.draw.circle(self.Window, self.grey8, (45, 655), 35, width=2)
            self.image_not_center("Logo prinicpal", 12, 615, 70, 70,"main_page/main_page3")


    
    def FirstSection(self): 
        self.image_not_center("Logo prinicpal", 5, 4, 80, 80,"main_page/main_page1")
       

        # Images
        



    def SecondSection(self): 
        self.rect_full(self.green, 220, 385, 260, 630, 0)
           
    def ThirdSection(self): 
        self.rect_full(self.blue, 775, 385, 850, 630, 0)

    def DisplayAll(self): 
      
        self.FirstSection()
        self.SecondSection()
        self.ThirdSection()
        self.banner()
        self.profil_hover()

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