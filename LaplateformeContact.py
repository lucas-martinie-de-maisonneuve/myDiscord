import pygame
import pywebview
from source.pygame_manager.Element import Element


class LaplateformeContact(Element):
    
    def __init__(self):

        Element.__init__(self)
        self.laplateforme_contact_run = True    
        # self.laplateforme_contact_running = False
    
    def creator_contact(self, creator_name, name, linkedin, github, email, y_name, y_neon, y_logo, y_text): 
        self.text_not_align(self.font1, 13, name, self.grey6, 110, y_name)
        self.image_not_center(creator_name, 55, y_neon, 50, 50,"laplateforme_contact/laplateforme_contact1")
        self.image_not_center("LinkedIn ", 100, y_logo, 25, 25,"laplateforme_contact/laplateforme_contact4")
        self.text_not_align(self.font4, 13, linkedin, self.grey6, 130, y_text)
        self.image_not_center("Github", 100, y_logo + 35, 25, 25,"laplateforme_contact/laplateforme_contact2")
        self.text_not_align(self.font4, 13, github, self.grey6, 130, y_text + 35)
        self.image_not_center("Email", 100, y_logo + 70, 25, 25,"laplateforme_contact/laplateforme_contact3")
        self.text_not_align(self.font4, 13, email, self.grey6, 130, y_text + 70)        

    def design(self):
   
        # Background
        self.img_background("Background", 600, 350, 1200, 700, "main_page/main_page8")
 
        # Left rectangle
        self.rect_full(self.grey5, 195, 350, 290, 620, 10) 

        # Right rectangle
        self.rect_full(self.grey5,750, 350, 800, 620, 10) 
        self.image_not_center("Logo LaPlateforme", 560, 55, 400, 66,"laplateforme_contact/laplateforme_contact5")

        # Rect 1
        self.rect_full(self.grey6, 750, 230, 740, 150, 10) 
        self.rect_border(self.white, 750, 230, 740, 150, 3, 10)

        # Rect 2
        self.rect_full(self.grey6, 750, 395, 740, 150, 10) 
        self.rect_border(self.white, 750, 395, 740, 150, 3, 10)

        # Rect 3
        self.rect_full(self.grey6, 750, 560, 740, 150, 10) 
        self.rect_border(self.white, 750, 560, 740, 150, 3, 10)

        # Ines
        self.creator_contact("Creator Ines", "Ines Lorquet", "Ines Lorquet","ines-lorquet","ineslorquet@gmail.com",87, 60, 110, 115)

        # Lucas
        self.creator_contact("Creator Lucas", "Lucas Martinie de Maisonneuve", "Lucas Martinie de Maisonneuve ","lucas-martinie-de-maisonneuve","lucas.martinie@gmail.com", 287, 260, 310, 315)

        # Vanny
        self.creator_contact("Creator Vanny", "Vanny Lamorte", "Vanny Lamorte","vanny-laure-lamorte","vannylamorte@gmail.com", 487, 460, 510, 515)

        # Neon Lines
        self.image_not_center("Neon light", 120, 190, 140, 105,"main_page/main_page7")
        self.image_not_center("Neon light", 120, 390, 140, 105,"main_page/main_page7")

        # Rect Maps
        self.rect_full(self.grey5, 195, 350, 290, 620, 10)
     

    def laplateforme_contact_running(self):
        pygame.init()
      
        
        while self.laplateforme_contact_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.design()
            self.update()

        pygame.quit()


test = LaplateformeContact()
test.laplateforme_contact_running()
           
