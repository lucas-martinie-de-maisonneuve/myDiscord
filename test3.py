import pygame
import pygame.freetype

pygame.init()

# Définir les constantes pour les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Définir les dimensions de la fenêtre
LARGEUR = 800
HAUTEUR = 600

# Définir les dimensions du rectangle blanc
RECTANGLE_LARGEUR = 400
RECTANGLE_HAUTEUR = 300

# Longueur maximale de la ligne de texte avant découpe
LONGUEUR_MAX = 20
texte_entre = ""
# Créer la fenêtre
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

# Créer une police
police = pygame.freetype.SysFont("Arial", 30)

# Boucle principale
en_cours = True
while en_cours:
    # Événements
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False

        elif evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_ESCAPE:
                en_cours = False
            elif evenement.key == pygame.K_RETURN:
                print("Texte saisi : ", texte_entre)
            elif evenement.key == pygame.K_BACKSPACE:
                texte_entre = texte_entre[:-1]
            else:
                texte_entre += evenement.unicode

    # Découper le texte en lignes de longueur maximale en tenant compte des mots individuels
    texte_decoupe = []
    ligne_actuelle = ""
    mots = texte_entre.split(" ")
    for mot in mots:
        if len(ligne_actuelle) + len(mot) < LONGUEUR_MAX:
            ligne_actuelle += mot + " "
        else:
            texte_decoupe.append(ligne_actuelle.strip())
            ligne_actuelle = mot + " "
    texte_decoupe.append(ligne_actuelle.strip())

    # Afficher un rectangle blanc
    fenetre.fill(BLANC)

    # Afficher les lignes de texte
    for i, ligne in enumerate(texte_decoupe):
        police.render_to(fenetre, (LARGEUR // 2 - RECTANGLE_LARGEUR // 2, HAUTEUR // 2 - RECTANGLE_HAUTEUR // 2 + i * 30), ligne, NOIR)

    # Actualiser l'écran
    pygame.display.flip()

pygame.quit()
