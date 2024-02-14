import pygame
from source.pygame_manager.screen import Screen
class Element:

    def __init__(self):
        self.screen = Screen()

        # Color
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.darkgrey = (100,100,100)
        self.grey = (255, 255, 255) # backhome
        self.grey1 = (240, 242, 245)   
        self.grey2 = (53, 53, 53)    
        self.grey3 = (25, 25, 25)
        self.grey4 = (146, 151, 153)
        self.grey5 = (34, 31, 37)
        self.grey6 = (176, 186, 181)
        self.grey7 = (30, 33, 35) # First section principal page
        self.grey8 = (51, 55, 62) # Banner principal page
        self.grey9 = (45, 49, 53) # 2 section principal page
        self.grey10 = (29,30,33)

        self.green = (66, 183, 42)
        self.dark_green = (43, 147, 72) #connected bubble

        self.blue = (0, 151, 254) # login
        self.blue1 = (0, 140, 234) # login  
        self.purple1 = (202, 8, 255) #linehome

        self.pink = (222, 50, 79)
        self.dark_purple = (67, 47, 104)
        self.dark_grey = (34, 31, 37)
        self.yellow = (233, 164, 41)   

        self.darkgreen = (97, 155, 138)
    
        self.darkgreenblue = (37, 50, 55)
        self.darkblue = (67, 97, 238)
        self.lightblue = (189, 224, 254)
        self.greyblue = (92, 103, 125)
        self.darkbluesea = (0, 40, 85)
        self.lightbluesea = (39, 76, 119)

        self.yellow = (255, 183, 3)
        self.lightyellow = (244, 226, 133)
        self.orange = (251, 133, 0)

        self.red = (242, 106, 141)
        self.darkred = (221, 45, 74)
        self.brown = (75, 67, 67)

        self.alpha_grey =(50,50,50,100)
        self.alpha_none =(0,0,0,0)

        self.font1 = "Uni Sans Heavy.otf"
        self.font2 = "gg sans Regular.ttf"
        self.font3 = "Uni Sans Thin.otf"
      
# Def text          

    def text_center(self, font, text_size, text_content, color, x, y):
        pygame.font.init()
        text = pygame.font.Font(f"source/pygame_manager/{font}", text_size).render(text_content, True,color)
        text_rect = text.get_rect(center=(x, y))
        self.screen.Window.blit(text, text_rect)
    
    def text_not_align(self, font, text_size, text_content, color, x, y):
        text = pygame.font.Font(f"source/pygame_manager/{font}", text_size).render(text_content, True, color)
        text_rect = text.get_rect(topleft=(x, y))
        self.screen.Window.blit(text, text_rect)

# Def image
        
    def img_center(self, name, x, y, width, height, image_name):
        name = pygame.image.load(f'image/{image_name}.png')
        name = pygame.transform.scale(name, (width, height))
        self.screen.Window.blit(name, (x - name.get_width()//2, y - name.get_height()//2))

    def image_not_center(self, name, x, y, width, height, image_name):
        name = pygame.image.load(f'image/{image_name}.png').convert_alpha()
        name = pygame.transform.scale(name,(width,height))
        self.screen.Window.blit(name, (x,y))
        
    def img_background(self, name, x, y, width, height, image_name):
        name = pygame.image.load(f'image/{image_name}.png').convert()
        name = pygame.transform.scale(name, (width, height))
        self.screen.Window.blit(name, (x - name.get_width()//2, y - name.get_height()//2))
 
# Def rectangle  
             
    def rect_full(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.screen.Window, color, pygame.Rect(x - width//2, y - height//2, width, height),0, radius)
        return button

    def rect_border(self, color, x, y, width, height, thickness, radius):
        button = pygame.draw.rect(self.screen.Window, color, pygame.Rect(x - width //2, y - height //2, width, height),  thickness, radius)
        return button
    #Rect border only on top  
    def rect_radius_top(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.screen.Window, color, pygame.Rect(x - width //2, y - height //2, width, height),False,0, radius, radius)
        return button

    #Rect border only on bottom
    def rect_radius_bot(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.screen.Window, color, pygame.Rect(x - width //2, y - height //2, width, height),False ,0,0,0, radius, radius)
        return button

# Def Circle
    def circle(self, color, x, y, radius):
        pygame.draw.circle(self.screen.Window, color, (x,y), radius)

    def circle_alpha(self, alpha_color, x, y, radius):
        circle_surface = pygame.Surface((self.screen.W,self.screen.H), pygame.SRCALPHA)
        pygame.draw.circle(circle_surface,alpha_color,(x,y),radius)
        self.screen.Window.blit(circle_surface, (0,0))

    def circle_hover(self, name, color,alpha_color, x, y, radius): 
        name = pygame.draw.circle(self.screen.Window, color, (x,y), radius)

        if self.is_mouse_over_button(name):
            self.circle_alpha(alpha_color, x, y, radius)
        else:
            self.circle(color, x, y, radius)

# Def Hoover
    
    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)  

    def button_hover(self, name, x, y, width, height, color_full, color_border, color_hoover, color_border_hoover, text, font, text_color,text_size, thickness, radius): 

        name = pygame.Rect((x - width//2), (y - height//2), width, height)

        if self.is_mouse_over_button(name):
            self.rect_full(color_hoover, x, y, width + 5, height + 5, radius)
            self.rect_border(color_border_hoover, x, y, width + 5, height + 5, thickness, radius)  
            self.text_center(font, text_size, text, text_color,  x, y)
        else:
            self.rect_full(color_full, x, y, width, height, radius)
            self.rect_border(color_border, x, y, width, height, thickness, radius)
            self.text_center(font, text_size, text,text_color, x, y)

    def hover_image(self, name_rect, name, x, y, width, height, image_name): 
        name_rect = pygame.Rect( x - width//2, y - height//2, width, height)        
        if self.is_mouse_over_button(name_rect):
            self.img_center(name, x, y, width+5, height+5, image_name)     
        else:
            self.img_center(name, x, y, width, height, image_name)
          

    def normal_cursor(self):
        pygame.mouse.set_cursor(pygame.cursors.arrow)

    def hand_cursor(self):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    # Hover texte
    # def hover(self):
    #     sign = (pygame.Rect(967, 594, 45, 13))    
    #     if self.is_mouse_over_button(sign):
    #         self.text_center(self.font1, 13, "Sign Up", self.blue, 990, 600)          
    #     else:
    #         self.text_center(self.font1, 12, "Sign Up", self.blue, 990, 600)
        
