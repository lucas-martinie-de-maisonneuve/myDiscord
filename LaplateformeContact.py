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
        (pygame.Rect(100, 110, 25, 25), "https://www.linkedin.com/in/ines-lorquet-35b90128b/"),
        (pygame.Rect(100, 135, 25, 25), "https://github.com/ines-lorquet"),
        (pygame.Rect(100, 170, 25, 25), " https://mail.google.com/"),
        (pygame.Rect(100, 310, 25, 25), "https://www.linkedin.com/in/lucas-martinie-de-maisonneuve-2349892b3/"),
        (pygame.Rect(100, 335, 25, 25),"https://github.com/lucas-martinie-de-maisonneuve"),
        (pygame.Rect(100, 370, 25, 25), " https://mail.google.com/"),
        (pygame.Rect(100, 510, 25, 25), "https://www.linkedin.com/in/vanny-lamorte-b4262b129/"),
        (pygame.Rect(100, 535, 25, 25),"https://github.com/vanny-laure-lamorte"),
        (pygame.Rect(100, 570, 25, 25), "https://mail.google.com/"),


        # Link LaPlateforme - A revoir
        (pygame.Rect(650, 370, 40, 40), "https://www.facebook.com/LaPlateformeIO"),
        (pygame.Rect(700, 370, 40, 40), "https://www.linkedin.com/school/laplateformeio/"),
        (pygame.Rect(750, 370, 40, 40),"https://twitter.com/i/flow/login?redirect_after_login=%2FLaPlateformeIO"),
        (pygame.Rect(800, 370, 40, 40), "https://www.instagram.com/LaPlateformeIO/"),
        (pygame.Rect(850, 370, 45, 45), "https://www.youtube.com/c/LaPlateformeIO"),

        # Link Brochure
        (pygame.Rect(750, 430, 240, 40), "https://laplateforme.io/telechargement-brochure/"),
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

    
    def design(self):
   
        # self.img_background_blur("Background",600, 350, 1200, 700, "main_page/main_page8", blur_radius=5)

        # Background
        self.img_background("Background", 600, 350, 1200, 700, "main_page/main_page8")
 
        # Left rectangle
        self.rect_full(self.grey5, 195, 350, 290, 620, 10) 

        # Right rectangle
        self.rect_full(self.grey5,750, 350, 800, 620, 10) 
        self.image_not_center("Logo LaPlateforme", 540, 45, 400, 66,"laplateforme_contact/contact5")
        self.text_not_align(self.font3, 18,"La grande école du numérique pour tous", self.grey1, 560, 115)

        # Rect 1
        self.rect_full(self.grey6, 750, 230, 740, 150, 10) 
        self.rect_border(self.white, 750, 230, 740, 150, 3, 10)
        self.text_not_align(self.font1, 15,"INFORMATIONS ", self.grey7, 400, 185)
        self.text_not_align(self.font1, 14,"• Par email : ", self.grey7, 400, 215)
        self.text_not_align(self.font4, 15,"contact@laplateforme.io" , self.grey7, 490, 210)
        self.text_not_align(self.font1, 14,"• Par téléphone : ", self.grey7, 400, 235)
        self.text_not_align(self.font4, 15,"04.84.89.43.69 " , self.grey7, 525, 230)
        self.text_not_align(self.font1, 14,"• Horaire : ", self.grey7, 400, 260)
        self.text_not_align(self.font4, 15," ouvert du lundi au vendredi de 9h à 17h" , self.grey7, 475, 255)

        # Rect 2
        self.rect_full(self.grey6, 750, 395, 740, 150, 10) 
        self.rect_border(self.white, 750, 395, 740, 150, 3, 10)
        self.hover_image("Facebook","Facebook", 650, 370, 40, 40,"laplateforme_contact/contact6")
        self.hover_image("LinkedIn","LinkedIn", 700, 370, 40, 40,"laplateforme_contact/contact7")
        self.hover_image("Twitter","Twitter", 750, 370, 40, 40,"laplateforme_contact/contact8")
        self.hover_image("Instagram","Instagram", 800, 370, 40, 40,"laplateforme_contact/contact9")
        self.hover_image("Youtube","Youtube", 850, 370, 45, 45,"laplateforme_contact/contact10")

        self.rect_full(self.grey1, 750, 430, 240, 40, 5) 
        self.button_hover("Social media", 750, 430, 240, 40, self.grey6, self.white, self.white, self.white,"download the brochure", self.font1, self.grey7,14, 2, 5)

        # self.text_not_align(self.font1, 14,"download the brochure", self.grey7, 665, 425)

        

        # Rect 3
        self.rect_full(self.grey6, 750, 560, 740, 150, 10) 
        self.rect_border(self.white, 750, 560, 740, 150, 3, 10)

     

        # Ines
        self.creator_contact("Creator Ines", "Ines Lorquet", "Ines Lorquet","ines-lorquet","ineslorquet@gmail.com", 87, 60, 125, 115)  

        # Lucas
        self.creator_contact("Creator Lucas", "Lucas Martinie de Maisonneuve", "Lucas Martinie de Maisonneuve ","lucas-martinie-de-maisonneuve","lucas.martinie@gmail.com", 287, 260, 325, 315)

        # Vanny
        self.creator_contact("Creator Vanny", "Vanny Lamorte", "Vanny Lamorte","vanny-laure-lamorte","vannylamorte@gmail.com", 487, 460, 525, 515)

        # Neon Lines
        self.image_not_center("Neon light", 120, 190, 140, 105,"main_page/main_page7")
        self.image_not_center("Neon light", 120, 390, 140, 105,"main_page/main_page7")

    def laplateforme_contact_running(self):
        
        while self.laplateforme_contact_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                self.handle_clicks(event)
            self.draw_links()              
            
            self.design()
            self.update()

test = LaplateformeContact()
test.laplateforme_contact_running()