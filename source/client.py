from data.DiscordManager import DiscordManager
from hashlib import sha256

class Client(DiscordManager):
    def __init__(self):
        self.user_email = ""
        self.user_password = ""
        self.connected = False
        self.user_info = (0, '', '', '', '', '', 0, 0)
        super().__init__()
        self.register_to_login = False 
        self.main_page_to_login = False
        self.profile_to_login = False
        self.home_running = False

        self.login_to_register = False
        self.register_running = False

        self.profile_to_main_page = False
        self.main_page_running = False
        self.home_to_main_page = False
        
        self.main_page_to_profile = False
        self.profile_running = False

    def login_user(self):
        hashed_password = sha256(self.user_password.encode()).hexdigest()

        if self.check_credentials(self.user_email, hashed_password):
            self.connected = True
            self.user_info = self.get_user(self.user_email, hashed_password)
            print("Connexion réussie !")
            return self.user_info
        else:
            print("Erreur. Connexion échouée.")
    
    def run(self):
        while True:
            if self.register_to_login or self.main_page_to_login or self.profile_to_login or self.home_running:
                self.home_running = True
                self.register_to_login, self.main_page_to_login, self.profile_to_login = False, False, False

            elif self.login_to_register or self.register_running:
                self.register_running = True
                self.login_to_register = False

            elif self.profile_to_main_page or self.main_page_running or self.home_to_main_page:
                self.main_page_running = True
                self.profile_to_main_page, self.home_to_main_page = False, False

            elif self.main_page_to_profile or self.profile_running:
                self.profile_running = True
                self.main_page_to_profile = False
