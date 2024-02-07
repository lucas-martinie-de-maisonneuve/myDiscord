import pygame
from source.pygame.screen import Screen
class Element:

    def __init__(self):
        self.screen = Screen()

        # Color
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.pink = (222, 50, 79)
        self.dark_purple = (67, 47, 104)
        self.dark_grey = (34, 31, 37)
        self.yellow = (233, 164, 41)
       


        self.green = (161, 193, 129)
        self.darkgreen = (97, 155, 138)

        self.blue = (72, 149, 239)
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

        self.grey = (139, 140, 137)
        self.darkgrey = (100,100,100)
        self.lightgrey = (160, 160, 160)
   
# Def text          
    
    def text_center(self, text_size, text_content, color, x, y):
        pygame.font.init()
        text = pygame.font.Font(None, text_size).render(text_content, True, color)
        text_rect = text.get_rect(center=(x, y))
        self.screen.Window.blit(text, text_rect)
    
    def text_not_align(self, text_size, text_content, color, x, y):
        text = pygame.font.Font(None, text_size).render(text_content, True, color)
        text_rect = text.get_rect(topleft=(x, y))
        self.screen.Window.blit(text, text_rect)

# Def image
        
    def img_center(self, name, x, y, width, height, image_name):
        name = pygame.image.load(f'image/{image_name}.png')
        name = pygame.transform.scale(name, (width, height))
        self.screen.Window.blit(name, (x - name.get_width()//2, y - name.get_height()//2))

    def image_not_center(self, name, x, y, width, height, image_name):
        name = pygame.image.load(f'image/{image_name}.png').convert_alpha()
        name = pygame.transform.scale(name,width,height)
        self.screen.Window.blit(name, (x,y))
        
    def img_background(self, name, x, y, width, height, image_name):
        name = pygame.image.load(f'image/{image_name}.png').convert()
        name = pygame.transform.scale(name, (width, height))
        self.screen.Window.blit(name, (x - name.get_width()//2, y - name.get_height()//2))

    
# Def rectangle  
             
    def rect_full(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.screen, color, pygame.Rect(x - width//2, y - height//2, width, height),0, radius)
        return button

    def rect_border(self, color, x, y, width, height, thickness, radius):
        button = pygame.draw.rect(self.screen, color, pygame.Rect(x - width //2, y - height //2, width, height),  thickness, radius)
        return button

# Def Hoover
    
    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)

    def button(self, x, y, width, height, color_full, color_border, color_hoover, color_border_hoover, text, text_color,text_size, thickness, radius): 

        name = pygame.Rect(x, y, width, height)

        if self.is_mouse_over_button(name):
            self.rect_full(color_hoover, x, y, width + 5, height + 5, thickness, radius)
            self.rect_border(color_border_hoover, x, y, width + 5, height + 5, thickness, radius)  
            self.text_center(text_size, text_color, text, x, y)
        else:
            self.rect_full(color_full, x, y, width, height, radius)
            self.rect_border(color_border, x, y, width, height, thickness, radius)
            self.text_center(text_size, text_color,text, x, y)
