from source.pygame_manager.Gui import Gui
from source.Client import Client
from data.DiscordManager import DiscordManager
class AddChannel(Gui,Client,DiscordManager):

    def __init__(self):
        Gui.__init__(self)
        Client.__init__(self)
        DiscordManager.__init__(self)
        self.entry_new_name = 0

    def background(self): 
        self.img_background("Background", 600, 350, 1200, 800, "main_page/main_page8")

    def add_section(self):
        # Background Rectangle
        self.rect_full(self.grey10, 600, 400, 500, 510, 10)
        
        self.text_center(self.font1, 31, "ADD CHANNEL", self.grey1, 600, 200)
        
        self.text_center(self.font2, 21, "Name Channel", self.grey1, 600, 270)
        self.but_name = self.rect_full(self.grey2, 600, 310, 300, 30, 10)
        self.text_center(self.font2,15,self.new_name_channel,self.grey1,600,310)
        
        # Choice category
        self.text_center(self.font2, 21, "Category", self.grey1, 600, 370)

        # Button Bachelor IT category
        if self.category==2:
            self.but_bachelor = self.button_hover("Bachelor IT button",540, 405, 100, 30, 10,self.grey2,self.grey2,self.grey2,"Bachelor IT",self.font2,self.white,16,2,10)
            self.img_center("bachelor it", 465, 405, 45, 45,"profile/logo_bachelor")
        else: 
            self.but_bachelor = self.button_hover("Bachelor it button",540, 405, 100, 30, 10,self.grey2,self.grey2,self.grey2,"Bachelor IT",self.font2,self.white,16,0,10)
            self.img_center("bachelor it", 465, 405, 35, 35,"profile/logo_bachelor") 

        # Button Talk TAlk category
        if self.category == 3:
            self.but_talk = self.button_hover("talk talk button",650, 405, 100, 30, 10,self.grey2,self.grey2,self.grey2,"Talk Talk",self.font2,self.white,16,2,10)
            self.img_center("talk talk", 725, 405, 45, 45,"profile/logo_talk")
        else:
            self.but_talk = self.button_hover("talk talk button",650, 405, 100, 30, 10,self.grey2,self.grey2,self.grey2,"Talk Talk",self.font2,self.white,16,0,10)
            self.img_center("talk talk", 725, 405, 35, 35,"profile/logo_talk")

        # Choice communication
        self.text_center(self.font2, 21, "Communication", self.grey1, 600, 460)

        # Button text communication
        if self.communication == 0:
            self.but_text = self.button_hover("text button",537, 495, 100, 30, 10,self.grey2,self.grey2,self.grey2,"Text",self.font2,self.white,16,2,10)
            self.img_center("Hashtags logiciel", 465, 495, 40, 40,"profile/logo_text") 
        else:
            self.but_text = self.button_hover("text button",537, 500, 100, 30, 10,self.grey2,self.grey2,self.grey2,"Text",self.font2,self.white,16,0,10)
            self.img_center("Hashtags logiciel", 465, 495, 30, 30,"profile/logo_text") 
            
        # Button vocal communication
        if self.communication == 1:
            self.but_voval = self.button_hover("vocal button",655, 495, 100, 30, 10,self.grey2,self.grey2,self.grey2,"Vocal",self.font2,self.white,16,2,10)
            self.img_center("Volume logiciel", 725, 495, 45, 45,"main_page/main_page10")
        else: 
            self.but_voval = self.button_hover("vocal button",655, 495, 100, 30, 10,self.grey2,self.grey2,self.grey2,"Vocal",self.font2,self.white,16,0,10)
            self.img_center("Volume logiciel", 725, 495, 35, 35,"main_page/main_page10")
            
        # Choice status
        self.text_center(self.font2, 21, "Status", self.grey1, 600, 550)
        
        # Button private status
        if self.status == 1:
            self.but_private = self.button_hover("private button",535, 580, 100, 30, 10,self.grey2,self.grey2,self.grey2,"Private",self.font2,self.white,16,2,10)
            self.img_center("Private", 465, 580, 45, 45,"main_page/main_page11")
        else:
            self.but_private = self.button_hover("private button",535, 580, 100, 30, 10,self.grey2,self.grey2,self.grey2,"Private",self.font2,self.white,16,0,10)
            self.img_center("Private", 465, 580, 35, 35,"main_page/main_page11")
            
        # Button public
        if self.status == 0:
            self.but_public = self.button_hover("public button",655, 580, 100, 30, 10,self.grey2,self.grey2,self.grey2,"Public",self.font2,self.white,16,2,10)
            self.img_center("Public ", 725, 580, 45, 45,"profile/logo_public") 
        else:
            self.but_public = self.button_hover("public button",655, 580, 100, 30, 10,self.grey2,self.grey2,self.grey2,"Public",self.font2,self.white,16,0,10)
            self.img_center("Public ", 725, 580, 35, 35,"profile/logo_public") 
            
        # Button Add Channel
        if self.add:
            self.but_add = self.button_hover("Button add channel",600, 630, 190, 30, 10,self.grey2,self.grey2,self.grey2,"ADD CHANNEL",self.font2,self.white,16,0,10)
        else:
            self.but_add = self.button_hover("Button add channel",600, 630, 190, 30, 10,self.grey9,self.grey9,self.grey9,"ADD CHANNEL",self.font2,self.white,16,0,10)

        # Neon light blue
        self.img_center("Neon light", 600, 170, 240, 90,"main_page/main_page7")
        self.img_center("Neon light", 600, 225, 240, 90,"main_page/main_page7")
        
        # Cross quit
        self.close_add = self.hover_image("Quit", "Quit", 815, 180, 50, 50, "profile/profile11", "profile/profile8")

        self.img_center("Neon light", 600, 530, 150, 90,"main_page/main_page7")
        self.img_center("Neon light", 600, 440, 150, 90,"main_page/main_page7")
        self.img_center("Neon light", 600, 350, 150, 90,"main_page/main_page7")
        
    def addChannel_run(self):
        if self.add_channel_running :
            self.background()
            self.event_add()
            self.add_section()            
