import pygame
import pywebview

def main():
    # Initialisation de Pygame
    pygame.init()

    # Création de la fenêtre Pygame
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Google Maps in Pygame")

    # Initialisation de pywebview
    pywebview.create_window("Google Maps", "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d")

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
