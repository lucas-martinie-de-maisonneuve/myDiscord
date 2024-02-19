##################################################
#                Projet myDiscord                #
#                   05/02/2024                   #
#                                                #
#  Lucas Martinie / Ines Lorquet / Vanny Lamorte #
##################################################

import pygame
from source.pygame_manager.element import Element
from source.pygame_manager.screen import Screen
from source.gui.home import Home
from source.gui.profil import Profil
from source.gui.register import Register
from source.gui.main_page import Main_page

class Display_test(Element, Screen):
    def __init__(self):
        Element.__init__(self)
        Screen.__init__(self)
        self.main_running = True
        self.main_page = Main_page((2, 'None', 'Martinie', 'Lucassa', 'lucas.martinie@laplateforme.io', 'LucasMartinie2412!', 2, 2))
        self.connexion = Home()
        self.profil = Profil()
        self.register = Register()
        self.connexion.home_running = False
        self.profil.profil_running = False
        self.register.register_running = False
        self.main_page.main_page_running = False

    def test(self):
        while self.main_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.main_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.princi.collidepoint(event.pos):
                        self.main_page.main_page_running = True
                        self.main_page.event_main_page()
                    elif self.inscri.collidepoint(event.pos):
                        self.register.register_running = True
                        self.register.register_run()
                    elif self.connec.collidepoint(event.pos):
                        self.connexion.home_running = True
                        self.connexion.home_run()
                    elif self.profi.collidepoint(event.pos):
                        self.profil.profil_running = True
                        self.profil.profil_run()
                    
            self.princi = self.rect_full(self.white, self.W//3, self. H//3, 300, 70, 10)
            self.text_center(self.font1, 25, "Principal", self.black, self.W//3, self. H//3)

            self.inscri = self.rect_full(self.white, 2 * (self.W//3), self. H//3, 300, 70, 10)
            self.text_center(self.font1, 25, "Inscription", self.black, 2 * (self.W//3), self. H//3)

            self.connec = self.rect_full(self.white, self.W//3, 2 * (self. H//3), 300, 70, 10)
            self.text_center(self.font1, 25, "Connexion", self.black, self.W//3, 2 * (self. H//3))

            self.profi = self.rect_full(self.white, 2 * (self.W//3), 2 * (self. H//3), 300, 70, 10)
            self.text_center(self.font1, 25, "Profil", self.black, 2 * (self.W//3), 2 * (self. H//3))

            self.update()

display = Display_test()
display.test()