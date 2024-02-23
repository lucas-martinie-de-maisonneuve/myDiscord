import pygame
from source.pygame_manager.Element import Element

class LaplateformeContact(Element):
    
    def __init__(self):

        Element.__init__(self)
        self.laplateforme_contact_run = True    
        # self.laplateforme_contact_running = False
        
    def design(self):
   
        # Background
        self.img_background("Background", 600, 350, 1200, 700, "main_page/main_page8")
 
        # Left rectangle
        self.rect_full(self.grey5, 195, 350, 290, 620, 10) 

        # Right rectangle
        self.rect_full(self.grey5,750, 350, 800, 620, 10) 

        # Ines
        self.image_not_center("Creator Ines Lorquet ", 55, 60, 50, 50,"laplateforme_contact/laplateforme_contact1")
        self.text_not_align(self.font1, 13, "Ines Lorquet", self.grey6, 110, 87)
        self.image_not_center("LinkedIn ", 100, 110, 25, 25,"laplateforme_contact/laplateforme_contact4")
        self.text_not_align(self.font4, 13, "Ines Lorquet", self.grey6, 130, 120)
        self.image_not_center("Github", 100, 145, 25, 25,"laplateforme_contact/laplateforme_contact2")
        self.text_not_align(self.font4, 13, "ines-lorquet", self.grey6, 130, 155)
        self.image_not_center("Email", 100, 180, 25, 25,"laplateforme_contact/laplateforme_contact3")
        self.text_not_align(self.font4, 13,"ineslorquet@gmail.com", self.grey6, 130, 190)

        # Lucas
        self.image_not_center("Creator Lucas ", 55, 260, 50, 50,"laplateforme_contact/laplateforme_contact1")
        self.text_not_align(self.font1, 13, "Lucas Martinie de Maisonneuve", self.grey6, 110, 287)        
        self.image_not_center("LinkedIn ", 100, 310, 25, 25,"laplateforme_contact/laplateforme_contact4")
        self.text_not_align(self.font4, 13, "Lucas Martinie de Maisonneuve", self.grey6, 130, 320)
        self.image_not_center("Github", 100, 345, 25, 25,"laplateforme_contact/laplateforme_contact2")
        self.text_not_align(self.font4, 13, "lucas-martinie-de-maisonneuve", self.grey6, 130, 355)
        self.image_not_center("Email", 100, 380, 25, 25,"laplateforme_contact/laplateforme_contact3")
        self.text_not_align(self.font4, 13,"lucas.martinie@gmail.com", self.grey6, 130, 390)

        # Vanny
        self.image_not_center("Creator Vanny ", 55, 460, 50, 50,"laplateforme_contact/laplateforme_contact1")
        self.text_not_align(self.font1, 13, "Vanny Lamorte", self.grey6, 110, 487)        
        self.image_not_center("LinkedIn ", 100, 510, 25, 25,"laplateforme_contact/laplateforme_contact4")
        self.text_not_align(self.font4, 13, "Vanny Lamorte", self.grey6, 130, 520)
        self.image_not_center("Github", 100, 545, 25, 25,"laplateforme_contact/laplateforme_contact2")
        self.text_not_align(self.font4, 13, "vanny-laure-lamorte", self.grey6, 130, 555)
        self.image_not_center("Email", 100, 580, 25, 25,"laplateforme_contact/laplateforme_contact3")
        self.text_not_align(self.font4, 13,"vanny.lamorte@gmail.com", self.grey6, 130, 590)

        # Neon Lines
        self.image_not_center("Neon light", 120, 190, 140, 105,"main_page/main_page7")
        self.image_not_center("Neon light", 120, 390, 140, 105,"main_page/main_page7")

  
        # Profile logo

    def laplateforme_contact_running(self):
        
        while self.laplateforme_contact_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.design()
            self.update()

test = LaplateformeContact()
test.laplateforme_contact_running()
           
