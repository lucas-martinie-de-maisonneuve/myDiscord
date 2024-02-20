import pygame

from source.pygame_manager.event_handler import Event_handler
from source.pygame_manager.element import Element
from data.discord_manager import Discord_Manager

class Main_page(Element, Event_handler, Discord_Manager):
    
    def __init__(self, user):
        Element.__init__(self)
        Event_handler.__init__(self)
        Discord_Manager.__init__(self)
        self.main_page_running = False
        self.search_text = ""
        self.user = user
        print(user)

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
 
    def ThirdSection(self):
        self.rect_full(self.grey10, 795, 385, 775, 610, 10)
        self.rect_full(self.grey1, 795, 650, 650, 60, 10)

    def DisplayAll(self): 
        self.background() 
        self.banner()
        self.FirstSection()
        self.SecondSection()
        self.ThirdSection()            

    def event_main_page(self):
        while self.main_page_running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.main_page_running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print("Recherche: " + self.search_text)
                        # Faites quelque chose avec le texte saisi, par exemple une recherche en ligne
                        self.search_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        self.search_text = self.search_text[:-1]
                    else:
                        self.search_text += event.unicode

            self.DisplayAll()
            self.update()

# main_page = Main_page()
# main_page.event_main_page()