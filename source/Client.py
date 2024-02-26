from data.DiscordManager import DiscordManager
from hashlib import sha256

class Client(DiscordManager):
    def __init__(self):
        self.home_running = False
        self.user_email = ""
        self.connected = False
        self.user_password = ""
        self.user_info = (0, '', '', '', '', '', 0, 0)
        super().__init__()
        self.register_to_login = False 
        self.main_page_to_login = False
        self.profile_to_login = False

        self.login_to_register = False
        self.register_running = False

        self.profile_to_main_page = False
        self.home_to_main_page = False
        self.main_page_running = False
        
        self.main_page_to_profile = False
        self.creator_to_profile = False
        self.profile_running = False

        self.profile_to_contact = False
        self.contact_running = False

    def login_user(self):
        print(self.user_email, self.user_password)
        hashed_password = sha256(self.user_password.encode()).hexdigest()

        if self.check_credentials(self.user_email, hashed_password):
            self.user_info = self.get_user(self.user_email, hashed_password)
            self.connected = True
            print("Connexion réussie !")
            print(self.user_info)
            return self.user_info
        else:
            print("Erreur. Connexion échouée.")
            print(self.user_info)