import pygame
import webbrowser

# Initialisation de Pygame
pygame.init()

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Création de la fenêtre
screen_width = 400
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Lien Pygame")

# Police de texte
font = pygame.font.Font(None, 36)

# Texte à afficher
text = font.render("link", True, WHITE)
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))

# Lien URL
url = "https://www.example.com"

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifie si le clic de souris est sur le texte
            if text_rect.collidepoint(event.pos):
                webbrowser.open(url)  # Ouvre le lien dans le navigateur

    # Efface l'écran
    screen.fill(BLACK)

    # Affiche le texte
    screen.blit(text, text_rect)

    # Rafraîchit l'écran
    pygame.display.flip()

# Quitte Pygame
pygame.quit()
