from data.DiscordManager import DiscordManager
from hashlib import sha256
class User(DiscordManager):
    def __init__(self, email, password):
        self.user_email = email
        self.user_password = password
        self.connected = False
        super().__init__()

    def loginUser(self):
        hashed_password = sha256(self.user_password.encode()).hexdigest()

        if self.check_credentials(self.user_email, hashed_password):
            self.connected = True
            user = self.get_user(self.user_email, hashed_password)
            print("Connexion successfull !")
            return(user)
        else:
            print("Erreur. Connexion échouée.")

    # Infos user 
    # Authentification
    # Création de compte
    # Déconnexion
    # envoi vers le serveur