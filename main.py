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
        self.connexion = Home()
        self.register = Register()
        self.main_page = MainPage(None)
        self.profile = Profile(None)
        self.connexion.home_running = True
    
    def test(self):
        while True:
            if self.register.register_to_login or self.main_page.main_page_to_login or self.profile.profile_to_login or self.connexion.home_running:
                if not self.connexion.home_running:
                    self.connexion = Home()
                    self.connexion.home_running = True
                else:
                    self.register.register_to_login, self.main_page.main_page_to_login, self.profile.profile_to_login = False, False, False
                    self.connexion.home_run()

            elif self.connexion.login_to_register or self.register.register_running:
                self.register.register_running = True
                self.connexion.home_running = False
                self.login_to_register = False
                self.register.register_run()

            elif self.profile.profile_to_main_page or self.main_page.main_page_running or self.connexion.home_to_main_page:
                if not self.main_page.main_page_running:
                    self.main_page = MainPage(self.connexion.user_info)
                    self.main_page.main_page_running = True
                else:
                    self.profile.profile_to_main_page, self.connexion.home_to_main_page = False, False
                    self.main_page.mainPage_run()


            elif self.main_page.main_page_to_profile or self.profile.profile_running:
                if not self.profile.profile_running:
                    self.profile = Profile(self.main_page.user_info)
                    self.profile.profile_running = True
                else:
                    self.main_page.main_page_to_profile = False
                    self.profile.profile_run()
            self.update()

display = Display_test()
display.test()