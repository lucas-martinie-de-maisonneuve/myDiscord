import pygame
import webbrowser
from source.pygame_manager.Element import Element


class LaplateformeContact(Element):
    
    def __init__(self):

        Element.__init__(self)
        self.laplateforme_contact_run = True    
        # self.laplateforme_contact_running = False
        self.link_is_clicked = True        

        self.link_data = [

        # Links creators
        (pygame.Rect(110-13, 125-13, 25, 25), "https://www.linkedin.com/in/ines-lorquet-35b90128b/"),
        (pygame.Rect(110-13, 160-13, 25, 25), "https://github.com/ines-lorquet"),
        (pygame.Rect(110-13, 195-13, 25, 25), " https://mail.google.com/"),

        (pygame.Rect(110-13, 325-13, 25, 25), "https://www.linkedin.com/in/lucas-martinie-de-maisonneuve-2349892b3/"),
        (pygame.Rect(110-13, 360-13, 25, 25),"https://github.com/lucas-martinie-de-maisonneuve"),
        (pygame.Rect(110-13, 395-13, 25, 25), " https://mail.google.com/"),

        (pygame.Rect(110-13, 525-13, 25, 25), "https://www.linkedin.com/in/vanny-lamorte-b4262b129/"),
        (pygame.Rect(110-13, 560-13, 25, 25),"https://github.com/vanny-laure-lamorte"),
        (pygame.Rect(110-13, 595-13, 25, 25), "https://mail.google.com/"),

        (pygame.Rect(450-20, 460-20, 40, 40), "https://www.facebook.com/LaPlateformeIO"),
        (pygame.Rect(500-20, 460-20, 40, 40), "https://www.linkedin.com/school/laplateformeio/"),
        (pygame.Rect(550-20, 460-20, 40, 40),"https://twitter.com/i/flow/login?redirect_after_login=%2FLaPlateformeIO"),
        (pygame.Rect(600-22, 460-22, 43, 43), "https://www.instagram.com/LaPlateformeIO/"),
        (pygame.Rect(650-23, 460-23, 45, 45), "https://www.youtube.com/c/LaPlateformeIO"),
        # Link Brochure
        (pygame.Rect(550-120, 590-20, 240, 40), "https://laplateforme.io/telechargement-brochure/"),
    ]

    def draw_links(self):
        for link_rect, url in self.link_data:
            pygame.draw.rect(self.Window, (0, 0, 255), link_rect)            

    def handle_clicks(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                for link_rect, url in self.link_data:
                    if link_rect.collidepoint(event.pos):
                        webbrowser.open(url)   
    
    def creator_contact(self, creator_name, name, linkedin, github, email, y_name, y_neon, y_logo, y_text): 
        self.text_not_align(self.font1, 13, name, self.grey6, 110, y_name)
        self.image_not_center(creator_name, 55, y_neon, 50, 50,"laplateforme_contact/contact1")
        self.hover_image("LinkedIn", "LinkedIn", 110, y_logo, 25, 25,"laplateforme_contact/contact4")
        self.text_not_align(self.font4, 13, linkedin, self.grey6, 130, y_text)      
        self.hover_image("Github", "Github", 110, y_logo+35, 25, 25,"laplateforme_contact/contact2")
        self.text_not_align(self.font4, 13, github, self.grey6, 130, y_text + 35)
        self.hover_image("Github", "Github", 110, y_logo+70, 25, 25,"laplateforme_contact/contact3")
        self.text_not_align(self.font4, 13, email, self.grey6, 130, y_text + 70)   

    def address(self, name_rect, x, y, addr, addr_x, addr_y ):  
        name_rect = pygame.Rect(x, y, 25, 25)
        if self.is_mouse_over_button(name_rect): 
            self.text_not_align(self.font4, 14, addr, self.pink, addr_x, addr_y)   
        else:
            self.text_not_align(self.font4, 15, addr, self.grey7, addr_x, addr_y)  
    
    def design(self):
        
        #--- Background ---#
        # self.img_background_blur("Background",600, 350, 1200, 700, "main_page/main_page8", blur_radius=5)
        self.img_background("Background", 600, 350, 1200, 700, "main_page/main_page8")

        # --- Left rectangle ---#
        
        self.rect_full(self.grey5, 195, 350, 290, 620, 10)        
        self.creator_contact("Creator Ines", "Ines Lorquet", "Ines Lorquet","ines-lorquet","ineslorquet@gmail.com", 87, 60, 125, 115) # Ines
        self.creator_contact("Creator Lucas", "Lucas Martinie de Maisonneuve", "Lucas Martinie de Maisonneuve ","lucas-martinie-de-maisonneuve","lucas.martinie@gmail.com", 287, 260, 325, 315) # Lucas
        self.creator_contact("Creator Vanny", "Vanny Lamorte", "Vanny Lamorte","vanny-laure-lamorte","vannylamorte@gmail.com", 487, 460, 525, 515) # Vanny
        self.image_not_center("Neon light", 120, 190, 140, 105,"main_page/main_page7") # Neon Lines top
        self.image_not_center("Neon light", 120, 390, 140, 105,"main_page/main_page7") # Neon Lines bottom

        #--- Right rectangle ---#

        self.rect_full(self.grey5,750, 350, 800, 620, 10) 
        self.image_not_center("Logo LaPlateforme", 540, 45, 400, 66,"laplateforme_contact/contact5")
        self.text_not_align(self.font3, 18,"La grande école du numérique pour tous", self.grey1, 560, 115)

        # Information section
        self.rect_full(self.grey6, 555, 230, 350, 140, 10) 
        self.rect_border(self.white, 555, 230, 350, 140, 3, 10)
        self.text_not_align(self.font1, 15,"INFORMATIONS ", self.grey7, 400, 185)
        self.text_not_align(self.font1, 14,"• Par email : ", self.grey7, 400, 225)
        self.text_not_align(self.font4, 15,"contact@laplateforme.io" , self.grey7, 490, 220)
        self.text_not_align(self.font1, 14,"• Par téléphone : ", self.grey7, 400, 245)
        self.text_not_align(self.font4, 15,"04.84.89.43.69 " , self.grey7, 525, 240)
        self.text_not_align(self.font1, 14,"• Horaire : ", self.grey7, 400, 270)
        self.text_not_align(self.font4, 15,"lundi au venddredi de 9h à 17h" , self.grey7, 480, 265)

        # Our locations section
        self.rect_full(self.grey6, 555, 395, 350, 140, 10) 
        self.rect_border(self.white, 555, 395, 350, 140, 3, 10)
        self.text_not_align(self.font1, 15,"OUR LOCATIONS", self.grey7, 400, 345)
        self.text_not_align(self.font1, 14,"• Marseille : " , self.grey7, 400, 385)
        self.address("Marseille", 990-13, 470-13,"8 rue d’Hozier, 13002 Marseille", 495, 380)
        self.text_not_align(self.font1, 14,"• Martigues : ", self.grey7, 400, 405)
        self.address("Matigues", 980-13, 465-13,"Place du 8 mai 1945, 13500 Martigues", 495, 400)
        self.text_not_align(self.font1, 14,"• Toulon : ", self.grey7, 400, 425)
        self.address("Toulon", 1020-12, 480-12,"131 Av. Franklin Roosevelt, 83100 Toulon",  470, 420)
        self.text_not_align(self.font1, 14,"• Cannes : ", self.grey7, 400, 445)
        self.address("Cannes", 1045-12, 465-12,"1 Chemin de l’École, 06150 Cannes", 475, 440)
            
        # Social Media section
        self.rect_full(self.grey6, 555, 565, 350, 140, 10) 
        self.rect_border(self.white, 555, 565, 350, 140, 3, 10)
        self.hover_image("Facebook","Facebook", 450, 530, 40, 40,"laplateforme_contact/contact6") # Facebook
        self.hover_image("LinkedIn","LinkedIn", 500, 530, 40, 40,"laplateforme_contact/contact7") # LinkedIn
        self.hover_image("Twitter","Twitter", 550, 530, 40, 40,"laplateforme_contact/contact8") # Twitter
        self.hover_image("Instagram","Instagram", 600, 530, 43, 43,"laplateforme_contact/contact9") # Instagram
        self.hover_image("Youtube","Youtube", 650, 530, 45, 45,"laplateforme_contact/contact10") # Youtube

        # Brochure section
        self.button_hover("Brochure", 550, 590, 240, 40, self.grey6, self.white, self.white, self.white,"download the brochure", self.font1, self.grey7,14, 2, 5)

        # Maps section
        self.rect_full(self.grey6, 940, 395, 365, 475, 10)
        self.rect_border(self.white, 940, 395, 365, 475, 3, 10)
        self.text_not_align(self.font1, 20,"LaPlateforme Locations" , self.grey4, 810, 185) # Title maps
        self.image_not_center("Maps", 750, 190, 380, 380,"laplateforme_contact/contact11") # Maps  

        # Pin section
        self.hover_image("Cannes","Cannes", 1045, 465, 25, 25,"laplateforme_contact/contact12") # Cannes
        self.hover_image("Toulon","Toulon", 1020, 480, 25, 25,"laplateforme_contact/contact12") # Toulon
        self.hover_image("Marseille", "Marseille", 990, 470, 25, 25,"laplateforme_contact/contact12") # Marseille  
        self.hover_image("Martigues","Martigues", 980, 465, 25, 25,"laplateforme_contact/contact12")  # Martigues

               
       


   



 
    
            

       
            
    def laplateforme_contact_running(self):        
        while self.laplateforme_contact_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                self.handle_clicks(event)

            self.draw_links()            
            self.design()
            # self.address()
            self.update()

test = LaplateformeContact()
test.laplateforme_contact_running()