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


    def event_home(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.home_running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_email_rect.collidepoint(event.pos): 
                    self.input_email = ""
                    self.entry = 1
                elif self.input_password_rect.collidepoint(event.pos): 
                    self.input_password = ""
                    self.entry = 2

                # elif self.is_mouse_over_button(pygame.Rect(745, 385, 350, 50)):                         
                #     if self.input_email != "" and self.input_password != "":                  
                #         self.login(self.input_email, self.input_password)

            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_BACKSPACE:
                        if self.entry == 1: 
                            self.input_email = self.input_email[:-1]
                        elif self.entry == 2: 
                            self.input_password = self.input_password[:-1]                        
                else:
                    if self.entry == 1:
                        if event.unicode:
                            self.input_email= self.input_email + event.unicode             
                    
                    elif self.entry == 2:
                        if event.unicode:
                            self.input_password= self.input_password + event.unicode

        