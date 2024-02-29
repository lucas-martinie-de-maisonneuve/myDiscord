import pygame
import webbrowser

class EventHandler():
    # def main_event(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             self.home_running = False
    #             self.register_running = False
    #             self.main_page_running = False
    #             self.profile_running = False
    #             self.contact_running = False
    #             self.main_running = False

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
                if self.profile1_circle.collidepoint(event.pos):
                    self.register_photo = 1
                    self.profile_hovered = self.profile1_circle

                elif self.profile2_circle.collidepoint(event.pos):
                    self.register_photo = 2
                    self.profile_hovered = self.profile2_circle

                elif self.profile3_circle.collidepoint(event.pos):
                    self.register_photo = 3
                    self.profile_hovered = self.profile3_circle

                elif self.profile4_circle.collidepoint(event.pos):
                    self.register_photo = 4
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
                    if self.register_username!="" and self.register_email!="" and self.register_surname != "" and self.register_name != "" and self.register_password != "" and self.register_photo != 0:
                        self.user_info = self.register_user()
                        self.register_to_main_page = True
                        self.registered = True
                        self.register_running = False
                        
                elif self.sign.collidepoint(event.pos):
                    self.register_to_login = True
                    self.register_running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if self.entry ==1:
                        self.register_username = self.register_username[:-1]
                    elif self.entry == 2:
                        self.register_email = self.register_email[:-1]
                    elif self.entry == 3:
                        self.register_surname = self.register_surname[:-1]
                    elif self.entry == 4:
                        self.register_name = self.register_name[:-1]
                    elif self.entry == 5:
                        self.register_password = self.register_password[:-1]
                else:
                    if self.entry == 1:
                        if event.unicode.isalpha() or event.unicode.isdigit():
                            self.register_username += event.unicode
                        
                    elif self.entry == 2:
                        if event.unicode:
                            self.register_email = self.register_email + event.unicode
                    elif self.entry == 3:
                        if event.unicode.isalpha():
                            self.register_surname = self.register_surname + event.unicode
                            self.register_surname = self.register_surname.capitalize()

                    elif self.entry == 4:
                        if event.unicode.isalpha():
                            self.register_name = self.register_name + event.unicode
                            self.register_name = self.register_name.capitalize()

                    elif self.entry == 5:
                        if event.unicode:
                            self.register_password = self.register_password + event.unicode

    def event_main_page(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
               
                if event.key == pygame.K_RETURN:
                    if self.entry == 1 and self.message != "":
                        self.add_message()
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
                # Event Emoji
                if self.emoji_logo.collidepoint(event.pos):
                    self.emoji_choice = True
                    
                if self.emoji_choice:
                    for id_message,rect1, rect2, rect3, rect4 in self.emoji_list:      
                        print(self.emoji_list) 
                        if rect1.collidepoint(event.pos):
                            self.add_emoji(1,id_message)
                            self.emoji_choice = False
                            
                        elif rect2.collidepoint(event.pos):
                            self.add_emoji(2,id_message)
                            self.emoji_choice = False
                            
                        elif rect3.collidepoint(event.pos):
                            self.add_emoji(3,id_message)
                            self.emoji_choice = False
                            
                        elif rect4.collidepoint(event.pos):
                            self.add_emoji(4,id_message)
                            self.emoji_choice = False

                if event.button == 4:
                    self.scroll += 15
                elif event.button == 5 and self.scroll >0 :
                    self.scroll -= 15
                elif event.button == 1:
                    for channel_id, rect in self.channel_rects:
                        if rect.collidepoint(event.pos):
                            self.actual_channel = channel_id
                            self.scroll = 0

                if self.send_button.collidepoint(event.pos):
                    self.add_message()
                elif self.entry_message.collidepoint(event.pos): 
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

                elif self.circle4.collidepoint(event.pos):
                    self.main_page_to_add_channel = True
                    self.add_channel_running = True
                    self.main_page_running = False
                    

                
            elif event.type == pygame.MOUSEBUTTONUP:
                 if self.link_logo_rect.collidepoint(event.pos):
                    self.link_is_clicked = True  

    def event_add(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.add_channel_running = False 
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.but_bachelor.collidepoint(event.pos):
                        self.category = 2
                    elif self.but_talk.collidepoint(event.pos):
                        self.category = 3

                    if self.but_text.collidepoint(event.pos):
                        self.communication = 0
                    elif self.but_voval.collidepoint(event.pos):
                        self.communication = 1
                                              
                    if self.but_public.collidepoint(event.pos):
                        self.status = 0
                    elif self.but_private.collidepoint(event.pos):
                        self.status = 1
                        
                    elif self.but_name.collidepoint(event.pos):
                        self.entry_new_name = 1

                    elif self.close_add.collidepoint(event.pos):
                        self.add_channel_to_main_page = True
                        self.add_channel_running = False   

                    elif self.but_add.collidepoint(event.pos):
                        if self.new_name_channel != "" and self.status != None and self.communication != None and self.category != None:
                            self.add_chan = self.add_channel_client()
                            self.add = False

                if self.entry_new_name != 0 and self.status != None and self.communication != None and self.category != None:
                    self.add=True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if self.entry_new_name==1:
                            self.new_name_channel = self.new_name_channel[:-1]
                    else:
                        if self.entry_new_name==1:
                            if event.unicode.isalpha():
                                self.new_name_channel += event.unicode
    def event_contact(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.close_about_us.collidepoint(event.pos):
                        self.contact_to_profile = True
                        self.contact_running = False 
                        
                    elif event.button == 1: 
                        for link_rect, url in self.link_data:
                            if link_rect.collidepoint(event.pos):
                                webbrowser.open(url)  

