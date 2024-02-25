##################################################
#                Projet myDiscord                #
#                   05/02/2024                   #
#                                                #
#  Lucas Martinie / Ines Lorquet / Vanny Lamorte #
##################################################

import pygame
from source.pygame_manager.Gui import Gui
from source.gui.Home import Home
from source.gui.Profile import Profile
from source.gui.Register import Register
from source.gui.MainPage import MainPage
class Display_test(Gui):
    def __init__(self):
        Gui.__init__(self)
        self.main_running = True
        self.main_page = MainPage()
        self.profile = Profile()
        self.register = Register()

    def test(self):
        while self.main_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.main_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.princi.collidepoint(event.pos):
                        self.main_page.main_page_running = True
                        self.main_page.mainPage_run()
                    elif self.inscri.collidepoint(event.pos):
                        self.register.register_running = True
                        self.register.register_run()
                    elif self.connec.collidepoint(event.pos):
                        self.connexion = Home()
                        self.connexion.home_running = True
                        self.connexion.home_run()

                    elif self.profi.collidepoint(event.pos):
                        self.profile.profile_running = True
                        self.profile.profile_run()

            if self.register.register_to_login or self.main_page.main_page_to_login or self.profile.profile_to_login or self.connexion.home_running:
                self.connexion.home_running = True
                self.connexion.home_run()
                self.register.register_to_login, self.main_page.main_page_to_login, self.profile.profile_to_login = False, False, False
            elif self.connexion.login_to_register or self.register.register_running:
                self.register.register_running = True
                self.register.register_run()
                self.connexion.login_to_register = False

            elif self.profile.profile_to_main_page or self.main_page.main_page_running or self.connexion.home_to_main_page:
                self.main_page.main_page_running = True
                self.main_page.mainPage_run()
                self.profile.profile_to_main_page, self.connexion.home_to_main_page = False, False

            elif self.main_page.main_page_to_profile or self.profile.profile_running:
                self.profile.profile_running = True
                self.profile.profile_run()
                self.main_page.main_page_to_profile = False

            else:
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