import bcrypt

# Fonction pour hacher un mot de passe
def hasher_mot_de_passe(mot_de_passe):
    # Génération d'un sel (salt) aléatoire
    sel = bcrypt.gensalt()
    # Hachage du mot de passe avec le sel
    mot_de_passe_hashe = bcrypt.hashpw(mot_de_passe.encode('utf-8'), sel)
    return mot_de_passe_hashe

# Fonction pour vérifier un mot de passe haché
def verifier_mot_de_passe(mot_de_passe, mot_de_passe_hashe):
    # Vérification du mot de passe avec le mot de passe haché
    return bcrypt.checkpw(mot_de_passe.encode('utf-8'), mot_de_passe_hashe)

# Exemple d'utilisation
mot_de_passe = "MotDePasseSecret123"
mot_de_passe_hashe = hasher_mot_de_passe(mot_de_passe)
print("Mot de passe haché:", mot_de_passe_hashe)

# Simuler la récupération du mot de passe haché de la base de données
# et vérifier un mot de passe entré par l'utilisateur
mot_de_passe_entre = "MotDePasseSecret123"
if verifier_mot_de_passe(mot_de_passe_entre, mot_de_passe_hashe):
    print("Mot de passe correct !")
else:
    print("Mot de passe incorrect.")
