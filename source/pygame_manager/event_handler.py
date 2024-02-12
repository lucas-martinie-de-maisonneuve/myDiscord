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
                if self.username_rect.collidepoint(event.pos):
                    self.size_username = 0
                    if not self.username_edit:
                        self.username_edit = True
                        self.email_edit, self.password_edit = False, False
                    else :
                        self.username_edit = False
                if self.email_rect.collidepoint(event.pos):
                    self.size_email = 0
                    if not self.email_edit:
                        self.email_edit = True
                        self.username_edit, self.password_edit = False, False
                    else:
                        self.email_edit = False
                if self.password_rect.collidepoint(event.pos):
                    self.size_password = 0
                    if not self.password_edit:
                        self.password_edit = True
                        self.email_edit, self.username_edit = False, False
                    else:
                        self.password_edit = False

            elif event.type == pygame.MOUSEBUTTONUP:
                if self.show.collidepoint(event.pos):
                     self.password_display = " *" * len(self.password)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if self.username_edit:
                        self.username = self.username[:-1]
                    if self.email_edit:
                        self.email = self.email[:-1]
                    if self.password_edit:
                        self.password = self.password[:-1]
                else:
                    if self.username_edit:
                        if event.unicode:
                            self.username += event.unicode
                    elif self.email_edit:
                            if event.unicode:
                                self.email += event.unicode
                    elif self.password_edit:
                            if event.unicode:
                                self.password += event.unicode