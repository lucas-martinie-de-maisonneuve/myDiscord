import pygame
from source.pygame_manager.element import Element
from source.pygame_manager.screen import Screen
from data.discord_manager import Discord_Manager
from source.pygame_manager.event_handler import Event_handler

class Test2(Element, Screen, Event_handler):
    def __init__(self):
        Screen.__init__(self)
        Element.__init__(self)
        self.inscription_running = True
        self.manager = Discord_Manager()
        pygame.init()
        
    def split_string(self,string, length):
        result = []
        start_index = 0

        while start_index < len(string):
            end_index = start_index + length
            
            while end_index < len(string) and string[end_index] != ' ':
                end_index -= 1
            
            result.append(string[start_index:end_index])
            start_index = end_index + 1

        return result
    
    def ThirdSection(self):
        self.rect_full(self.grey10, 795, 385, 775, 610, 10)
        self.rect_full(self.grey1, 795, 650, 650, 60, 10)
        # self.nb_message = self.manager.count_message()
        # self.nb_message = self.nb_message[0]
        # self.nb =  self.nb_message
        # print(self.nb_message)
        
        for i in range(1):
            self.message_name = self.manager.name_message()
            self.str_name1 = self.message_name[i][0]
            self.message_name = f'{self.str_name1} '

            self.message_1 = self.manager.message_message()
            self.str_name2 = self.message_1[i][0]
            self.message_1 = f'{self.str_name2} '

            self.message_time1 = self.manager.time_message()
            self.str_name3 = self.message_time1[i][0]
            self.message_time1 = f'{self.str_name3} '

            long_string = "Une phrase tres  tres tres long pour tester que ca marche super bien et que ines est la plus intelligentetres tres long pour tester que ca marche super bien et que ines est la plus intelligente"
            chunked_strings = self.split_string(self.message_1,105)
            # chunked_strings = self.split_string(long_string,50)

            max_line_length =  758
            rectangle_height = len(chunked_strings) * 40
            pos_x = 408
            pos_y = 610 - rectangle_height
            
            if i==0:
                # Avoir la longueur du second message 
                self.message_1 = self.manager.message_message()
                self.str_name = self.message_1[i+1][0]
                self.message_2 = f'{self.str_name} '
                chunked_strings2 = self.split_string(self.message_2,105)
                rectangle_height2 = len(chunked_strings) * 20
                
                self.rect_full_not_centered(self.blue, pos_x, pos_y-rectangle_height2, 20 + max_line_length, rectangle_height , 2)

                for i, chunk in enumerate(chunked_strings):
                    self.text_not_align(self.font2, 16, chunk, self.grey1, pos_x + 12, ((30 * i) + pos_y + 20)-rectangle_height2)
                self.text_not_align(self.font1, 18, self.message_name, self.black, pos_x + 12, (pos_y + 5)-rectangle_height2)
                self.text_not_align(self.font1, 10, self.message_time1, self.grey1, pos_x + 142, (pos_y + 10)-rectangle_height2)
                
            if i!=0:            
                self.rect_full_not_centered(self.blue, pos_x, pos_y, 20 + max_line_length, rectangle_height , 2)

                for i, chunk in enumerate(chunked_strings):
                    self.text_not_align(self.font2, 16, chunk, self.grey1, pos_x + 12, ((30 * i) + pos_y + 20))
                self.text_not_align(self.font1, 18, self.message_name, self.black, pos_x + 12, (pos_y + 5))
                self.text_not_align(self.font1, 10, self.message_time1, self.grey1, pos_x + 142, (pos_y + 10))

    def register_run(self):
        self.inscription_running = True
        while self.inscription_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.inscription_running = False
            self.ThirdSection()
            # self.event_register()
            self.update()

test = Test2()
test.register_run()
