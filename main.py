##################################################
#                Projet myDiscord                #
#                   05/02/2024                   #
#                                                #
#  Lucas Martinie / Ines Lorquet / Vanny Lamorte #
##################################################

from source.gui.Home import Home
from source.gui.Profile import Profile
from source.gui.Register import Register
from source.gui.MainPage import MainPage
from source.gui.Contact import Contact
from source.gui.AddChannel import AddChannel
from source.pygame_manager.Gui import Gui

class Display_test(Gui):
    def __init__(self):
        Gui.__init__(self)
        self.connexion = Home()
        self.register = Register()
        self.main_page = MainPage(None)
        self.profile = Profile(None)
        self.contact = Contact()
        self.add_channel = AddChannel()
        self.connexion.home_running = True

    def discord_run(self):
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
                self.connexion.login_to_register = False
                self.register.register_run()

            elif self.profile.profile_to_main_page or self.main_page.main_page_running or self.connexion.home_to_main_page or self.add_channel.add_channel_to_main_page or self.connexion.home_to_main_page:
                if not self.main_page.main_page_running:
                    self.normal_cursor()
                    if self.register.registered:
                        self.main_page = MainPage(self.register.user_info)
                        self.main_page.main_page_running = True
                        self.register.register_running = False
                    else:
                        self.main_page = MainPage(self.connexion.user_info)
                        self.main_page.main_page_running = True
                else:
                    self.profile.profile_to_main_page, self.connexion.home_to_main_page, self.register.registered, self.register.register_to_main_page,self.add_channel.add_channel_to_main_page = False, False, False, False,False
                    self.main_page.mainPage_run()

            elif self.main_page.main_page_to_profile or self.contact.contact_to_profile or self.profile.profile_running:
                if not self.profile.profile_running:
                    self.profile = Profile(self.main_page.user_info)
                    self.profile.profile_running = True
                else:
                    self.main_page.main_page_to_profile = False
                    self.contact.contact_to_profile = False
                    self.profile.profile_run()

            elif self.main_page.main_page_to_add_channel or self.add_channel.add_channel_running:
                    self.add_channel.add_channel_running = True
                    self.add_channel.addChannel_run()
                    self.main_page.main_page_to_add_channel = False

            elif self.profile.profile_to_contact or self.contact.contact_running:
                self.contact.contact_running = True
                self.contact.contact_run()
                self.contact.profile_to_contact = False

            self.update()
            
display = Display_test()
display.discord_run()