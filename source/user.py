from data.discord_manager import Discord_Manager

class User(Discord_Manager):
    def __init__(self, email, password):
        self.user_email = email
        self.user_password = password
        self.connected = False
        super().__init__()

    def loginUser(self):
        if self.check_credentials(self.user_email, self.user_password):
            self.connected = True
            user = self.get_user(self.user_email, self.user_password)
            print("Connexion successfull !")
            return(user)
        else:
            print("Erreur. Connexion échouée.")

    # Infos user 
    # Authentification
    # Création de compte
    # Déconnexion
    # envoi vers le serveur