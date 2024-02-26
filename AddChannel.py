import pygame
from data.DiscordManager import DiscordManager
from source.pygame_manager.Gui import Gui

class AddChannel(Gui, DiscordManager):

    def __init__(self):
        Gui.__init__(self)
        DiscordManager.__init__(self)
        self.add_channel_running = True
        self.new_name_channel = ""
        self.entry_new_name = 0
        self.status = None
        self.communication = None
        self.category = None

    def background(self): 
        self.img_background_blur('Background', 600, 350, 1200, 800, 'main_page/main_page8', blur_radius=10)

    def second_section(self):
        # Rectangle de fond
        self.rect_full(self.grey10, 600, 400, 500, 510, 10)
        
        self.text_center(self.font1, 31, "ADD CHANNEL", self.grey1, 600, 200)
        
        self.text_center(self.font2, 21, "Name Channel", self.grey1, 600, 270)
        self.rect_full(self.grey9, 600, 320, 300, 30, 10)
        
        # Choice category
        self.text_center(self.font2, 21, "Category", self.grey1, 600, 370)

        # Button Bachelor IT category
        if self.category==2:
            self.but_bachelor = self.button_hover("bachelor it button",540, 405, 100, 30, 10,self.grey1,self.grey2,self.grey2,"Bachelor IT",self.font2,self.white,16,2,10)
        else: 
            self.but_bachelor = self.button_hover("bachelor it button",540, 405, 100, 30, 10,self.grey2,self.grey2,self.grey2,"Bachelor IT",self.font2,self.white,16,0,10)

        # Button Talk TAlk category
        if self.category == 3:
            self.but_talk = self.button_hover("talk talk button",650, 405, 100, 30, 10,self.grey2,self.white,self.grey9,"Talk Talk",self.font2,self.white,16,0,10)
        else:
            self.but_talk = self.button_hover("talk talk button",650, 405, 100, 30, 10,self.grey2,self.grey9,self.grey9,"Talk Talk",self.font2,self.white,16,0,10)

        # Choice communication
        self.text_center(self.font2, 21, "Communication", self.grey1, 600, 465)

        # Button text communication
        if self.communication == 0:
            self.but_text = self.button_hover("text button",537, 500, 100, 30, 10,self.grey9,self.grey9,self.grey9,"Text",self.font2,self.white,16,2,10)
        else:
            self.but_text = self.button_hover("text button",537, 500, 100, 30, 10,self.grey9,self.grey9,self.grey9,"Text",self.font2,self.white,16,0,10)
            
        #Button vocal communication
        if self.communication == 1:
            self.but_voval = self.button_hover("vocal button",655, 500, 100, 30, 10,self.grey9,self.grey9,self.grey9,"Vocal",self.font2,self.white,16,0,10)
        else: 
            self.but_voval = self.button_hover("vocal button",655, 500, 100, 30, 10,self.grey9,self.grey9,self.grey9,"Vocal",self.font2,self.white,16,0,10)
            
        # Choice status
        self.text_center(self.font2, 21, "Status", self.grey1, 600, 550)
        
        # Button private status
        if self.status == 1:
            self.but_private = self.button_hover("private button",535, 580, 100, 30, 10,self.grey9,self.grey9,self.grey9,"Private",self.font2,self.white,16,0,10)
        else:
            self.but_private = self.button_hover("private button",535, 580, 100, 30, 10,self.grey9,self.grey9,self.grey9,"Private",self.font2,self.white,16,0,10)
            
        # Button public
        if self.status == 0:
            self.but_public = self.button_hover("public button",655, 580, 100, 30, 10,self.grey9,self.grey9,self.grey9,"Public",self.font2,self.white,16,0,10)
        else:
            self.but_public = self.button_hover("public button",655, 580, 100, 30, 10,self.grey9,self.grey9,self.grey9,"Public",self.font2,self.white,16,0,10)

        # logo choice category
        self.img_center("bachelor it", 725, 405, 35, 35,"profile/logo_talk")
        self.img_center("Hashtags logiciel", 465, 405, 35, 35,"profile/logo_bachelor") 
        
        # logo choice status
        self.img_center("Private logiciel", 725, 580, 35, 35,"main_page/main_page11")
        self.img_center("Hashtags logiciel", 465, 580, 35, 35,"profile/logo_public") 
        
        # logo choice communication
        self.img_center("Volume logiciel", 725, 498, 35, 35,"main_page/main_page10")
        self.img_center("Hashtags logiciel", 465, 499, 30, 30,"profile/logo_text") 
        
        # Neon light blue
        self.img_center("Neon light", 600, 170, 240, 90,"main_page/main_page7")
        self.img_center("Neon light", 600, 225, 240, 90,"main_page/main_page7")

    def addChannel_run(self):
        while self.add_channel_running :
            self.background()
            self.second_section()
            self.update()
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
                                              
                    if self.but_private.collidepoint(event.pos):
                        self.status = 1
                    elif self.but_public.collidepoint(event.pos):
                        self.status = 0
                        

                        
test = AddChannel()
test.addChannel_run()