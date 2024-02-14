import pygame
from source.pygame_manager.element import Element
from source.pygame_manager.screen import Screen
from data.discord_manager import Discord_Manager
from source.pygame_manager.event_handler import Event_handler

class Inscription(Element, Screen,Event_handler):
    def __init__(self):
        Screen.__init__(self)
        Element.__init__(self)
        self.inscription_running = True
        self.manager = Discord_Manager()
        self.username = "Username"
        self.email = "Email address"
        self.surname = "Surname"
        self.name = "Name"
        self.password = "Password"
        self.entry = 0
        self.photo = 0
        self.profil_hovered = None
        pygame.init()

    def form(self):
        self.rect_full(self.grey10, 500, 300, 500, 100, 10)

        self.message_name = self.manager.name_message()
        self.str_name1 = self.message_name[0][0]
        self.message_name = f'{self.str_name1} '
        self.text_not_align(self.font1, 18, self.message_name, self.grey1, 500, 300)
        
        self.message_1 = self.manager.message_message()
        self.str_name2 = self.message_1[0][0]
        self.message_1 = f'{self.str_name2} '
        self.text_not_align(self.font1, 12, self.message_1, self.grey1, 500, 300)
            
    def profil_screen(self):
        pass
        
    def profil_hover(self):
        pass
    def inscription_run(self):
        self.inscription_running = True
        while self.inscription_running:
            self.form()
            self.profil_hover()
            self.profil_screen()
            self.event_inscription()

            self.screen.update()

test = Inscription()
test.inscription_run()