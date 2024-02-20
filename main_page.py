import pygame

from source.pygame_manager.event_handler import Event_handler
from source.pygame_manager.element import Element
from data.discord_manager import Discord_Manager
# from test2 import Test2
class Main_page(Element,Event_handler, Discord_Manager):

    def __init__(self):
        Element.__init__(self)
        Event_handler.__init__(self)
        Discord_Manager.__init__(self)
        self.message = ""
        self.message = ""
        # self.test2 = Test2()
        self.RECTANGLE_LARGEUR = 600
        self.RECTANGLE_HAUTEUR = 60 
        self.LONGUEUR_MAX = 80
        self.police = pygame.freetype.SysFont(self.font5,18)
        pygame.init()

    def background(self): 
        self.img_background("background", 600, 350, 1200, 800, "main_page/main_page8")
        
    def banner(self):
        self.rect_full(self.grey10, 655, 40, 1055, 60, 10)

        # self.text_not_align(self.font2, 40, "self.search_text", self.white, 10, 5)

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
        self.cercle2 = pygame.draw.circle(self.Window, self.grey10, (64, 635), 35)
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

                    elif a ==1:
                        self.communication = self.communication_channel(a+1)
                        self.str_communication1= self.communication[0][0]
                        self.communication = f'{self.str_communication1}'
                        if self.communication == "0": 
                            self.img_center("Volume logiciel", 170,(20*i)+330, 25, 25,"main_page/main_page10")
                        elif self.communication == "1": 
                            self.img_center("Hashtags logiciel", 170, 350, 15, 15,"main_page/main_page14") 

                        self.text_not_align(self.font2, 15, self.name_channel1, self.grey1, 200, (20*i)+320)
                        
                    elif a==2:
                        self.communication = self.communication_channel(a+1)
                        self.text_not_align(self.font2, 15, self.name_channel1, self.grey1, 200, (20*i)+520)
                    
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

        # Logo hashtags, volume and book
        # self.img_center("Book about us", 170, 125, 25, 25,"main_page/main_page12")
        # self.img_center("Book Rules", 170, 150, 25, 25,"main_page/main_page12")
        # self.img_center("Book News", 170, 175, 25, 25,"main_page/main_page12")

        # self.img_center("Volume logiciel", 170, 330, 25, 25,"main_page/main_page10")
        # self.img_center("Hashtags logiciel", 170, 350, 15, 15,"main_page/main_page14")
        
        # self.img_center("Volume ia", 170, 370, 25, 25,"main_page/main_page10")
        # self.img_center("Hashtags ia", 170, 390, 15, 15,"main_page/main_page14")

        # self.img_center("Dark Side Lock logo", 170, 530, 25, 25,"main_page/main_page11")
        # self.img_center("Volume logo ia", 170, 550, 25, 25,"main_page/main_page10")
        # self.img_center("Hashtags ia", 170, 570, 15, 15,"main_page/main_page14")

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
        #         # self.text_center()
        # for i in range(2):
        #     # self.message_name = self.name_message()
        #     # self.str_name1 = self.message_name[i][0]
        #     # self.message_name = f'{self.str_name1} '

        #     # self.message_1 = self.message_message()
        #     # self.str_name2 = self.message_1[i][0]
        #     # self.message_1 = f'{self.str_name2} '

        #     # self.message_time1 = self.time_message()
        #     # self.str_name3 = self.message_time1[i][0]
        #     # self.message_time1 = f'{self.str_name3} '

        #     long_string = "Une phrase tres  tres tres long pour tester que ca marche super bien et que ines est la plus intelligentetres tres long pour tester que ca marche super bien et que ines est la plus intelligente"
        #     chunked_strings = self.split_string(long_string,50)

        #     max_line_length =  758
        #     rectangle_height = len(chunked_strings) * 40
        #     pos_x = 408
        #     pos_y =  200 + rectangle_height
        #     # self.rect_full_not_centered(self.blue, pos_x, pos_y, 20 + max_line_length, rectangle_height, 2)

        #     # for i, chunk in enumerate(chunked_strings):
        #     #     self.text_not_align(self.font2, 16, chunk, self.grey1, pos_x + 12, (30 * i) + pos_y + 20)
        #     # self.text_not_align(self.font1, 18, self.message_name, self.black, pos_x + 12, pos_y + 5)
        #     # self.text_not_align(self.font1, 10, self.message_time1, self.grey1, pos_x + 82, pos_y + 10)
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

    def DisplayAll(self):
        self.main_page_running = True
        while self.main_page_running :
            self.background()
            self.banner()
            self.FirstSection()
            self.SecondSection()
            self.ThirdSection()
            self.event_main_page()
            self.update()

# main_page = Main_page()
# main_page.event_main_page()
