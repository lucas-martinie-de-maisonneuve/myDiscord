import pygame

class Screen:
    def __init__(self):
        pygame.init()
        self.W = 1200
        self.H = 700
        self.Window = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("MyDiscord")
        self.clock = pygame.time.Clock()

    def update(self):
        pygame.display.flip()
        pygame.display.update()
        # self.clock.tick(60)
        # self.Window.fill((0, 0, 0))

    def screen_color(self, color): 
        self.Window.fill(color)