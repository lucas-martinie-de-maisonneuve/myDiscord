import pygame

from source.pygame_manager.EventHandler import EventHandler
from source.pygame_manager.Element import Element
from data.DiscordManager import DiscordManager
from source.gui.Profil import Profil

class MainPage(Element, EventHandler, DiscordManager):
    
    def __init__(self, user):
        Element.__init__(self)
        DiscordManager.__init__(self)
        EventHandler.__init__(self)
        self.user = user
        self.profil = Profil(self.user)
        self.main_page_running = False
        self.input_search = "Search..."
        self.message = ""
        self.RECTANGLE_LARGEUR = 600
        self.RECTANGLE_HAUTEUR = 60 
        self.LONGUEUR_MAX = 80
        self.police = pygame.freetype.SysFont(self.font5,18)
        self.link_is_clicked = True   

    def background(self): 
        self.img_background("background", 600, 350, 1200, 800, "main_page/main_page8")
   
    def banner(self):

        # Link to the LaPlateforme website
        self.rect_full(self.grey10, 655, 40, 1055, 60, 10)
        self.image_not_center("Question mark", 1120, 15, 50, 50,"main_page/main_page15")    
        self.link_logo_rect = pygame.Rect(1120, 15, 50, 50)
        self.url = "https://laplateforme.io/"

        # Search bar
        self.input_search_rect = self.rect_full(self.grey2, 970, 40, 240, 35, 80)
        self.text_not_align(self.font2, 15, self.input_search, self.white, 860, 30.5)
        self.image_not_center("Search logo", 1050, 25, 30, 30,"main_page/main_page16")  

    def FirstSection(self):

        # First section background color
        self.rect_full(self.grey10, 65, 350, 90, 680, 10)

        # Main Logo    
        self.image_not_center("Logo prinicpal", 20, 25, 95, 95,"main_page/main_page3")   

        # Hover server
        self.cercle1 = pygame.draw.circle(self.Window, self.grey10, (64, 170), 35)     
        if self.is_mouse_over_button(self.cercle1):      
            self.img_center("Logo prinicpal", 64, 170, 70, 70,"main_page/main_page2")
            self.img_center("Logo prinicpal", 64, 170, 115, 115,"main_page/main_page4")
        else:          
            self.img_center("Logo prinicpal", 64, 170, 70, 70,"main_page/main_page2")
            self.img_center("neon cercle", 64, 170, 110, 110,"main_page/main_page4")
               
        # Hover settings
        self.cercle2 = pygame.draw.circle(self.Window, self.grey10, (64, 540), 35)
        if self.is_mouse_over_button(self.cercle2):           
            self.img_center("neon server", 64, 540, 85, 85,"main_page/main_page5")
            self.img_center("neon circle", 64, 540, 115, 115,"main_page/main_page4")   
        else:      
            self.img_center("neon server", 64, 540, 85, 85,"main_page/main_page5")
            self.img_center("neon circle", 64, 540, 110, 110,"main_page/main_page4") 

        # Hover Power Off
        self.cercle3 = pygame.draw.circle(self.Window, self.grey10, (64, 635), 35)
        if self.is_mouse_over_button(self.cercle2):           
            self.img_center("Power Off", 64, 635, 60, 60,"main_page/main_page9")
            self.img_center("neon circle", 64, 635, 115, 115,"main_page/main_page4")   
        else:      
            self.img_center("Power Off", 64, 635, 60, 60,"main_page/main_page9")
            self.img_center("neon circle", 64, 635, 110, 110,"main_page/main_page4") 
   
     
    def SecondSection(self):
        self.rect_full(self.grey10, 257, 385, 260, 610, 10)

        self.nb_category = self.count_category()
        self.nb_category = self.nb_category[0]

        for a in range(self.nb_category):
            self.nb_channels = self.count_channel(a+1)
            self.nb_channels = self.nb_channels[0]

            self.name_category1 = self.name_category()
            self.str_name2 = self.name_category1[a][0]
            self.name_category1 = f'{self.str_name2} '
            self.text_not_align(self.font1, 18, self.name_category1, self.grey1, 200, (190*a) +100)

            for i in range(self.nb_channels):
                self.name_channel1 = self.name_channel(a+1)                
                self.str_name3 = self.name_channel1[i][0]
                self.name_channel1 = f'{self.str_name3} '
                
                for _ in range(self.nb_channels):
                    
                    if a==0:
                        self.text_not_align(self.font2, 15, self.name_channel1, self.grey1, 200, (20*i)+120)
                        self.img_center("Book about us", 170, (20*i)+125, 25, 25,"main_page/main_page12")
                        
                    elif a == 1:
                        self.text_not_align(self.font2, 15, self.name_channel1, self.grey1, 200, (20*i)+320)
                        
                        self.communication = self.communication_channel(a+1)
                        self.str_communication1= self.communication[i][0]
                        self.communication = f'{self.str_communication1}'

                        if self.communication == "0":
                            self.img_center("Volume logiciel", 170,(20*i)+310, 25, 25,"main_page/main_page10")
                            
                        if self.communication == "1": 
                            self.img_center("Hashtags logiciel", 170, (20*i)+350, 15, 15,"main_page/main_page14") 
                        
                    elif a==2:
                        self.communication = self.communication_channel(a+1)
                        self.text_not_align(self.font2, 15, self.name_channel1, self.grey1, 200, (20*i)+520)
                        self.communication = self.communication_channel(a+1)
                        self.str_communication1= self.communication[i][0]                        
                        self.communication = f'{self.str_communication1}'

                        if self.communication == "0":
                            self.img_center("Volume logiciel", 170,(20*i)+530, 25, 25,"main_page/main_page10")
                            print(i,"volume")
                            
                        if self.communication == "1": 
                            self.img_center("Hashtags logiciel", 170, (20*i)+530, 15, 15,"main_page/main_page14") 
                            print(i,"hashtag")
                        
                        
                # for _ in range(self.nb_channels):
                #     if a==0:
                #         self.text_not_align(self.font2, 15, self.name_channel1, self.grey1, 200, (20*i)+120)
                #         self.img_center("Book about us", 170, (20*i)+125, 25, 25,"main_page/main_page12")

                #     elif a == 1:
                #         self.communication = self.communication_channel(a+1)
                #         print(self.communication)
                #         self.str_communication1= self.communication[0][0]
                #         self.communication = f'{self.str_communication1}'
                #         if self.communication == "0":
                #             # print (self.communication)                        
                #             self.img_center("Volume logiciel", 170,(20*i)+330, 25, 25,"main_page/main_page10")
                #         elif self.communication == "1": 
                #             # print (self.communication) 
                #             self.img_center("Hashtags logiciel", 170, 350, 15, 15,"main_page/main_page14") 

                #         self.text_not_align(self.font2, 15, self.name_channel1, self.grey1, 200, (20*i)+320)
                        
                #     elif a==2:

                #         self.communication = self.communication_channel(a+1)
                #         self.text_not_align(self.font2, 15, self.name_channel1, self.grey1, 200, (20*i)+520)
                    
                    # True = 0 =  son
                    # False = 1 = Message
                        
        # def communication_channel(self):
        # sql = "SELECT communication FROM channel"
        # self.cursor.execute(sql)
        # self.channels = self.cursor.fetchall()
        # return self.channels 
    
        # Neon light blue
        self.img_center("Neon light", 260, 230, 140, 105,"main_page/main_page7")
        self.img_center("Neon light", 260, 430, 140, 105,"main_page/main_page7")
        self.img_center("Neon Light", 260, 630, 140, 105,"main_page/main_page7")    


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
        self.entry_message = self.rect_full(self.grey1, 795, 650, 650, 60, 10)

        self.nb_message = self.count_message(3)
        self.nb_message = self.nb_message[0]
        self.nb =  self.nb_message
        print(self.nb)
        long_string = "Une phrase tres  tres tres long pour tester que ca marche super bien et que ines est la plus intelligentetres tres long pour tester que ca marche super bien et que ines est la plus intelligente"
        # chunked_strings = self.split_string(long_string,50)

        max_line_length =  755
        pos_y = 610
            
        for i in range(self.nb):
            self.message_1 = self.message_message(3)
            self.str_name2 = self.message_1[i][0]
            self.message_1 = f'{self.str_name2} '

            self.message_name = self.name_message(3)
            self.str_name1 = self.message_name[i][0]
            self.message_name = f'{self.str_name1} '
            
            self.message_time1 = self.time_message(3)
            self.str_name3 = self.message_time1[i][0]
            self.message_time1 = f'{self.str_name3} '

            index_message_suivant = i + 1

            # Vérifier s'il y a un message suivant avant de le récupérer
            if index_message_suivant < self.nb:  # self.nb étant le nombre total de messages
                print(i)
                # Obtenez les données du message suivant en utilisant des fonctions similaires à celles que vous utilisez actuellement
                next_message_1 = self.message_message(3)
                next_str_name2 = next_message_1[index_message_suivant][0]
                next_message_1_content = f'{next_str_name2} '

                next_message_name = self.name_message(3)
                next_str_name1 = next_message_name[index_message_suivant][0]
                next_message_name_content = f'{next_str_name1} '

                next_message_time = self.time_message(3)
                next_str_name3 = next_message_time[index_message_suivant][0]
                next_message_time_content = f'{next_str_name3} '

                next_chunked_strings = self.split_string(next_message_1_content, 105)
                next_rectangle_height = len(next_chunked_strings) * 40
          
            chunked_strings = self.split_string(self.message_1, 105)
            rectangle_height = len(chunked_strings) * 40  
            pos_y -= rectangle_height + 10 


# Ajuster la position verticale en fonction de la hauteur du prochain message
            pos_y -= next_rectangle_height + 10
            
            self.rect_full_not_centered(self.grey10, 795, pos_y, 20 + max_line_length, rectangle_height , 2)

            for j, chunk in enumerate(chunked_strings):
                self.text_not_align(self.font2, 16, chunk, self.grey1, 435, ((30 * j) + pos_y + 20))
            self.text_not_align(self.font1, 18, self.message_name, self.pink, 435, (pos_y + 5))
            self.text_not_align(self.font1, 10, self.message_time1, self.grey1, 580, (pos_y + 10))
        texte_decoupe = []
        ligne_actuelle = ""
        mots = self.message.split(" ")
        for mot in mots:
            if len(ligne_actuelle) + len(mot) < self.LONGUEUR_MAX:
                ligne_actuelle += mot + " "
            else:
                texte_decoupe.append(ligne_actuelle.strip())
                ligne_actuelle = mot + " "
        texte_decoupe.append(ligne_actuelle.strip())

        for i, ligne in enumerate(texte_decoupe):
            self.text_not_align(self.font2, 17, ligne, self.black, 510, 620 + i * 15)

    def mainPage_run(self):
        while self.main_page_running :
            if not self.profil.profil_running:
                
                self.background()
                self.FirstSection()
                self.SecondSection()
                self.ThirdSection()
                self.banner() 
                self.event_main_page()
                self.update()
