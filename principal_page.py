
import pygame
from source.pygame_manager.element import Element
from source.pygame_manager.screen import Screen
# from data.discord_manager import Discord_Manager

class Home(Element, Screen):

    def __init__(self):
        Screen.__init__(self)
        Element.__init__(self)
        pygame.init()
        self.principal_page_run = True

    def serveur_page(self):
        pass

    def channel_page(self):
        pass

    def chat_page(self):
        pass

    def principal_page_run(self):
        self.principal_page_run = True
        while self.principal_page_run :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.principal_page_run = False
