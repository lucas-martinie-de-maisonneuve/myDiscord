import pygame

class Event_handler():
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
                     
    def event_inscription(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.inscription_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.sign_up.collidepoint(event.pos):
                        self.inscription_running = False
                    elif self.profil1_cercle.collidepoint(event.pos):
                        self.photo = 1
                        self.profil_hovered = self.profil1_cercle

                    elif self.profil2_cercle.collidepoint(event.pos):
                        self.photo = 2
                        self.profil_hovered = self.profil2_cercle

                    elif self.profil3_cercle.collidepoint(event.pos):
                        self.photo = 3
                        self.profil_hovered = self.profil3_cercle

                    elif self.profil4_cercle.collidepoint(event.pos):
                        self.photo = 4
                        self.profil_hovered = self.profil4_cercle

                    elif self.username_rect.collidepoint(event.pos):
                        self.username = ""
                        self.entry = 1

                    elif self.email_rect.collidepoint(event.pos):
                        self.email = ""
                        self.entry = 2

                    elif self.surname_rect .collidepoint(event.pos):
                        self.surname = ""
                        self.entry = 3

                    elif self.name_rect.collidepoint(event.pos):
                        self.name = ""
                        self.entry = 4

                    elif self.password_rect.collidepoint(event.pos):
                        self.password = ""
                        self.entry = 5

                    elif self.sign_up.collidepoint(event.pos):
                        if self.username!="Username" and self.email!="Email address" and self.surname != "Surname" and self.name != "Name" and self.password != "Password" and self.photo != 0:
                            self.manager.add_user(self.surname,self.name,self.username,self.email,self.password,self.photo,2)
                            print("ajouter")
                            
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if self.entry ==1:
                            self.username = self.username[:-1]
                        elif self.entry == 2:
                            self.email = self.email[:-1]
                        elif self.entry == 3:
                            self.surname = self.surname[:-1]
                        elif self.entry == 4:
                            self.name = self.name[:-1]
                        elif self.entry == 5:
                            self.password = self.password[:-1]

                    else:
                        if self.entry == 1:
                            if event.unicode.isalpha() or event.unicode.isdigit():
                                self.username += event.unicode
                            
                        elif self.entry == 2:
                            if event.unicode:
                                self.email = self.email + event.unicode

                        elif self.entry == 3:
                            if event.unicode.isalpha():
                                self.surname = self.surname + event.unicode
                                self.surname = self.surname.capitalize()

                        elif self.entry == 4:
                            if event.unicode.isalpha():
                                self.name = self.name + event.unicode
                                self.name = self.name.capitalize()

                        elif self.entry == 5:
                            if event.unicode:
                                self.password = self.password + event.unicode
