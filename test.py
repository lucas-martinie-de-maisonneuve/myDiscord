# import pygame
# from source.pygame_manager.element import Element
# from source.pygame_manager.screen import Screen
# from data.discord_manager import Discord_Manager
# from source.pygame_manager.event_handler import Event_handler

# class Inscription(Element, Screen,Event_handler):
#     def __init__(self):
#         Screen.__init__(self)
#         Element.__init__(self)
#         self.inscription_running = True
#         self.manager = Discord_Manager()
#         self.username = "Username"
#         self.email = "Email address"
#         self.surname = "Surname"
#         self.name = "Name"
#         self.password = "Password"
#         self.entry = 0
#         self.photo = 0
#         self.profil_hovered = None
#         pygame.init()
#     def split_string(self, string, length):
#         result = []
#         start_index = 0

#         while start_index < len(string):
#             end_index = start_index + length
            
#             # Si le prochain caractère à la fin de la sous-chaîne n'est pas un espace, recule jusqu'à trouver un espace
#             while end_index < len(string) and string[end_index] != ' ':
#                 end_index -= 1
            
#             # Ajoute la sous-chaîne au résultat
#             result.append(string[start_index:end_index])
            
#             # Met à jour l'index de début pour la prochaine sous-chaîne
#             start_index = end_index + 1

#         return result
        
#     def form(self):
#         self.rect_full(self.grey10, 500, 300, 775, 610, 10)
#         self.rect_full(self.red, 500, 350, 775, 160, 10)
        
#         self.message_name = self.manager.name_message()
#         self.str_name1 = self.message_name[0][0]
#         self.message_name = f'{self.str_name1} '
#         self.text_not_align(self.font1, 18, self.message_name, self.blue, 220, 270)
        
#         self.message_1 = self.manager.message_message()
#         self.str_name2 = self.message_1[0][0]
#         self.message_1 = f'{self.str_name2} '
#         # self.text_not_align(self.font1, 12, self.message_1, self.grey1, 500, 300)
        
#         # self.message_1 = self.manager.message_message()
#         # self.str_name2 = self.message_1[0][0]
#         # self.message_1 = f'{self.str_name2} '
#         # self.text_not_align(self.font1, 12, self.message_1, self.grey1, 500, 300)
        
#         self.message_time1 = self.manager.time_message()
#         self.str_name3 = self.message_time1[0][0]
#         self.message_time1 = f'{self.str_name3} '
#         self.text_not_align(self.font1, 8, self.message_time1, self.grey1, 290, 270)
        
#         long_string = "Une phrase tres tres tres long pour tester que ca marche super bien et que ines est la plus intelligente"
#         chunked_strings = self.split_string(long_string, 50)
        
#         for i,chunk in enumerate(chunked_strings):
#             self.text_not_align(self.font2, 16, chunk, self.grey1, 220, (20*i)+300)
            
#     def profil_screen(self):
#         pass
        
#     def profil_hover(self):
#         pass
#     def register_run(self):
#         self.inscription_running = True
#         while self.inscription_running:
#             self.form()
#             self.profil_hover()
#             self.profil_screen()
#             self.event_register()

#             self.screen.update()

# test = Inscription()
# test.register_run()
import pygame
from source.pygame_manager.element import Element
from source.pygame_manager.screen import Screen
from data.discord_manager import Discord_Manager
from source.pygame_manager.event_handler import Event_handler

class Inscription(Element, Screen, Event_handler):
    def __init__(self):
        Screen.__init__(self)
        Element.__init__(self)
        self.inscription_running = True
        self.manager = Discord_Manager()
        self.username = "Username"
        self.email = "Email address"
        self.surname = "Surname"
        self.name = "Name"
        self.password = "Password"
        self.entry = 0
        self.photo = 0
        self.profil_hovered = None
        pygame.init()

    def split_string(self, string, length):
        result = []
        start_index = 0

        while start_index < len(string):
            end_index = start_index + length
            
            while end_index < len(string) and string[end_index] != ' ':
                end_index -= 1
            
            result.append(string[start_index:end_index])
            start_index = end_index + 1

        return result
        
    def form(self):
        self.rect_full(self.grey10, 500, 300, 775, 610, 10)
        self.rect_full(self.red, 500, 350, 775, 160, 10)
        
        self.message_name = self.manager.name_message()
        self.str_name1 = self.message_name[0][0]
        self.message_name = f'{self.str_name1} '
        
        self.message_1 = self.manager.message_message()
        self.str_name2 = self.message_1[0][0]
        self.message_1 = f'{self.str_name2} '
        
        self.message_time1 = self.manager.time_message()
        self.str_name3 = self.message_time1[0][0]
        self.message_time1 = f'{self.str_name3} '
        
        long_string = "Une phrase tres  tres tres long pour tester que ca marche super bien et que ines est la plus intelligentetres tres long pour tester que ca marche super bien et que ines est la plus intelligente"
        chunked_strings = self.split_string(long_string, 50)
        
        max_line_length =  758
        rectangle_height = len(chunked_strings) * 40
        self.rect_full_not_centered(self.blue, 112, 335, 20 + max_line_length, rectangle_height, 2)

        for i, chunk in enumerate(chunked_strings):
            self.text_not_align(self.font2, 16, chunk, self.grey1, 220, (30 * i) + 355)
        self.text_not_align(self.font1, 18, self.message_name, self.black, 220, 340)
        self.text_not_align(self.font1, 10, self.message_time1, self.grey1, 290, 345)

    def register_run(self):
        self.inscription_running = True
        while self.inscription_running:
            self.form()
            self.event_register()
            self.screen.update()

test = Inscription()
test.register_run()
