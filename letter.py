import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotation de lettres")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Police de caractères
font = pygame.font.SysFont(None, 100)

# Texte à afficher
text = "ABC"

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Effacement de l'écran
    SCREEN.fill(WHITE)

    # Rendu du texte
    text_surface = font.render(text, True, BLACK)

    # Récupération du rectangle entourant le texte
    text_rect = text_surface.get_rect()

    # Positionnement du texte au centre de l'écran
    text_rect.center = (WIDTH // 2, HEIGHT // 2)

    # Rotation du texte autour de son centre
    rotated_text = pygame.transform.rotate(text_surface, 90)

    # Obtention du rectangle entourant le texte rotatif
    rotated_text_rect = rotated_text.get_rect(center=text_rect.center)

    # Affichage du texte rotatif sur l'écran
    SCREEN.blit(rotated_text, rotated_text_rect)

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Pause de 1 seconde avant de faire la rotation suivante
    pygame.time.delay(1000)

pygame.quit()
sys.exit()
