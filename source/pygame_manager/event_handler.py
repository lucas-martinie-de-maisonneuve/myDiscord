import pygame

class Event_handler:
    def __init__(self):
        pygame.init()

    def event_profil(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    self.profil_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.show.collidepoint(event.pos):
                    self.password_display = self.password
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.show.collidepoint(event.pos):
                     self.password_display = " *" * len(self.password)