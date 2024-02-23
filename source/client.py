from data.DiscordManager import DiscordManager
from hashlib import sha256

class Client(DiscordManager):
    def __init__(self):
        self.user_email = ""
        self.user_password = ""
        self.connected = False
        self.user_info = (0, '', '', '', '', '', 0, 0)
        super().__init__()

    def login_user(self):
        hashed_password = sha256(self.user_password.encode()).hexdigest()

        if self.check_credentials(self.user_email, hashed_password):
            self.connected = True
            self.user_info = self.get_user(self.user_email, hashed_password)
            print("Connexion réussie !")
            return self.user_info
        else:
            print("Erreur. Connexion échouée.")

    def _update_user_info(self, user_info):
        self.user_info = user_info

    def update_user(self, user):
        self._update_user_info(user)
        return self.user_info
