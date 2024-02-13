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
        self.rect_full(self.pink, 645, 35, 1110, 70, 0)

    def FirstSection(self):
        self.rect_full(self.red, 45, 350, 90, 700, 0)

    def SecondSection(self):
        self.rect_full(self.green, 220, 385, 260, 630, 0)

    def ThirdSection(self):
        self.rect_full(self.blue, 775, 385, 850, 630, 0)

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