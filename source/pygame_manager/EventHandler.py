import pygame
import webbrowser

class EventHandler():
    def event_profile(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.show.collidepoint(event.pos):
                    self.show_pass = True
                    self.password_display = str(self.profile_password[0])
                elif self.username_rect.collidepoint(event.pos):
                    if not self.username_edit:
                        self.username_edit = True
                        self.email_edit, self.password_edit = False, False
                    else :
                        self.username_edit = False
                elif self.email_rect.collidepoint(event.pos):
                    if not self.email_edit:
                        self.email_edit = True
                        self.username_edit, self.password_edit = False, False
                    else:
                        self.email_edit = False
                elif self.password_rect.collidepoint(event.pos):
                    if not self.password_edit:
                        self.password_edit = True
                        self.email_edit, self.username_edit = False, False
                    else:
                        self.password_edit = False
                elif self.status_rect.collidepoint(event.pos):
                    if not self.status_edit:
                        self.status_edit = True
                    else:
                        self.status_edit = False
                elif self.status_edit_rect.collidepoint(event.pos):
                    if self.status_edit:
                        if self.status == "Away":
                            self.status = "Online"
                        else:
                            self.status = "Away"
                        self.status_edit = False
                        self.status_edit_cursor = False
                        self.status_active_cursor = False
                            
                elif self.profile_pict.collidepoint(event.pos):
                    if not self.picture_edit:
                        self.picture_edit = True
                    else: 
                        self.picture_edit = False
                elif self.picture1.collidepoint(event.pos):
                    self.picture = self.pict[0]
                elif self.picture2.collidepoint(event.pos):
                    self.picture = self.pict[1]
                elif self.picture3.collidepoint(event.pos):
                    self.picture = self.pict[2]
                elif self.disconnect_button.collidepoint(event.pos):    
                    self.profile_to_login = True
                    self.profile_running = False
                elif self.contact_button.collidepoint(event.pos):
                    self.profile_to_contact = True
                    self.profile_running = False
                elif self.close_profile.collidepoint(event.pos):
                    self.profile_to_main_page = True
                    self.profile_running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                if self.show.collidepoint(event.pos):
                     self.show_pass = False
                     self.password_display = " *" * len(self.profile_password)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if self.username_edit:
                        self.username = self.username[:-1]
                    if self.email_edit:
                        self.email = self.email[:-1]
                    if self.password_edit:
                        self.profile_password = self.profile_password[:-1]
                else:
                    if self.username_edit:
                        if event.unicode:
                            self.username += event.unicode
                    elif self.email_edit:
                            if event.unicode:
                                self.email += event.unicode
                    elif self.password_edit:
                            if event.unicode:
                                self.profile_password += event.unicode
                          
    def event_home(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_email_rect.collidepoint(event.pos): 
                    self.entry = 1
                elif self.input_password_rect.collidepoint(event.pos): 
                    self.entry = 2
                else:
                    self.entry = 0
                if self.sign.collidepoint(event.pos):
                    self.login_to_register = True
                    self.home_running = False

                if self.show_pass_rect.collidepoint(event.pos):
                    self.show_pass = True                  

            elif event.type == pygame.MOUSEBUTTONUP:
                if self.show_pass_rect.collidepoint(event.pos):
                    self.show_pass = False

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

    def event_register(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.sign_up.collidepoint(event.pos):
                    self.inscription_running = False
                elif self.profile1_circle.collidepoint(event.pos):
                    self.photo = 1
                    self.profile_hovered = self.profile1_circle

                elif self.profile2_circle.collidepoint(event.pos):
                    self.photo = 2
                    self.profile_hovered = self.profile2_circle

                elif self.profile3_circle.collidepoint(event.pos):
                    self.photo = 3
                    self.profile_hovered = self.profile3_circle

                elif self.profile4_circle.collidepoint(event.pos):
                    self.photo = 4
                    self.profile_hovered = self.profile4_circle

                elif self.username_rect.collidepoint(event.pos):
                    self.entry = 1

                elif self.email_rect.collidepoint(event.pos):                    
                    self.entry = 2

                elif self.surname_rect .collidepoint(event.pos):                    
                    self.entry = 3

                elif self.name_rect.collidepoint(event.pos):                    
                    self.entry = 4

                elif self.password_rect.collidepoint(event.pos):
                    self.entry = 5

                elif self.sign_up.collidepoint(event.pos):
                    if self.username!="" and self.email!="" and self.surname != "" and self.name != "" and self.password != "" and self.photo != 0:
                        self.add_user(self.surname,self.name,self.username,self.email,self.password,self.photo,2)
                        print("ajouter")

                elif self.sign.collidepoint(event.pos):
                    self.register_to_login = True
                    self.register_running = False

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

    def event_main_page(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
               
                if event.key == pygame.K_RETURN:
                    pass

                elif event.key == pygame.K_BACKSPACE:
                    if self.entry == 1 :
                        self.message = self.message[:-1]
                    elif self.entry == 2: 
                        self.input_search = self.input_search[:-1]
                else:
                    if self.entry == 1 :
                        self.message += event.unicode  
                    elif self.entry == 2: 
                        self.input_search  += event.unicode 

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.scroll += 15
                elif event.button == 5 and self.scroll >0 :
                    self.scroll -= 15

                if self.entry_message.collidepoint(event.pos): 
                    self.entry = 1
                elif self.link_logo_rect.collidepoint(event.pos):
                    if self.link_is_clicked:
                        webbrowser.open(self.url)
                        self.link_is_clicked = False

                elif self.input_search_rect.collidepoint(event.pos):  
                    self.input_search = ""
                    self.entry = 2   

                elif self.circle2.collidepoint(event.pos):
                    self.main_page_to_profile = True
                    self.main_page_running = False

                elif self.circle3.collidepoint(event.pos):
                    self.main_page_to_login = True
                    self.main_page_running = False
                                             



            elif event.type == pygame.MOUSEBUTTONUP:
                 if self.link_logo_rect.collidepoint(event.pos):
                    self.link_is_clicked = True  

    def event_contact(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        for link_rect, url in self.link_data:
                            if link_rect.collidepoint(event.pos):
                                webbrowser.open(url)   