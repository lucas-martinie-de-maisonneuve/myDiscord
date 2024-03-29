import pygame

class Element():
    def __init__(self):

        # Color
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        self.darkgrey = (100,100,100)
        self.grey = (250, 250, 250) # Backgroud Home
        self.grey1 = (240, 242, 245)   
        self.grey2 = (53, 53, 53) # Info profile rectangle 
        self.grey3 = (25, 25, 25)
        self.grey4 = (146, 151, 153)
        self.grey5 = (34, 31, 37)
        self.grey6 = (176, 186, 181)
        self.grey7 = (30, 33, 35) # First section principal page
        self.grey8 = (51, 55, 62) # Banner principal page
        self.grey9 = (17, 18, 20) # Second section principal page
        self.grey10 = (29,30,33) # Rect principal page
        self.grey11 = (155,155,155)
        self.dark_grey = (34, 31, 37)

        self.dark_green = (43, 147, 72)

        self.blue = (0, 151, 254) # Login
        self.blue1 = (0, 140, 234) # Login  
        self.blue2 = (33, 6, 84) # Theme color pink
        self.blue3 = (27, 38, 59) # Theme color orange
        self.blue4 = (20, 236, 232) # Flashy blue #14ece8
        self.darkblue = (65, 90, 119) 
        self.lightblue = (189, 224, 254)

        self.alpha_white =(150,150,150, 200) # Alpha profil picture on profil page
        self.alpha_grey =(50,50,50,100) # Alpha profil picture on profil page
        self.alpha_grey2 =(50,50,50,200) # Alpha background register
        self.alpha_none =(0,0,0,0)

        self.pink = (222, 50, 79)
        self.pink1 = (254, 0, 135) # Notif number
      
        self.yellow = (233, 164, 41)   

        self.green = (66, 183, 42) # Connected bubble
        self.green2 = (39, 78, 19)
        self.darkgreen = (97, 155, 138)

        self.purple1 = (202, 8, 255) # Linehome
        self.purple2 = (125, 85, 196)
        self.purple3 = (60, 9, 108)  # Theme color blue
        self.purple4 = (67, 47, 104) # Theme color green
        self.dark_purple = (67, 47, 104)

        self.darkgreenblue = (37, 50, 55)
     
        self.greyblue = (92, 103, 125)
        self.darkbluesea = (0, 40, 85)
        self.lightbluesea = (39, 76, 119)

        self.yellow = (233, 164, 41)   
        self.lightyellow = (244, 226, 133)
        self.orange = (251, 133, 0)
        self.orange2 = (255, 103, 2) 

        self.red = (242, 106, 141)
        self.darkred = (221, 45, 74)
        self.brown = (75, 67, 67)
   
        self.font1 = "assets/font/Uni Sans Heavy.otf"
        self.font2 = "assets/font/gg sans Regular.ttf"
        self.font3 = "assets/font/Uni Sans Thin.otf"
        self.font4 = "assets/font/gg sans Semibold.ttf"
        self.font5 = "assets/font/gg sans Bold.ttf"

# Def text          

    def text_center(self, font, text_size, text_content, color, x, y):
        pygame.font.init()
        text = pygame.font.Font(f"{font}", text_size).render(text_content, True,color)
        text_rect = text.get_rect(center=(x, y))
        self.Window.blit(text, text_rect)
    
    def text_not_align(self, font, text_size, text_content, color, x, y):
        text = pygame.font.Font(f"{font}", text_size).render(text_content, True, color)
        text_rect = text.get_rect(topleft=(x, y))
        self.Window.blit(text, text_rect)

    def text_center_italic(self, font, text_size, text_content, color, x, y):
        pygame.font.init()
        font_obj = pygame.font.Font(f"{font}", text_size)
        text = font_obj.render(text_content, True, color)
        text_rect = text.get_rect(center=(x, y))
        self.Window.blit(text, text_rect)

# Def image

    def img_center(self, name, x, y, width, height, image_name):
        name = pygame.image.load(f'assets/image/{image_name}.png')
        name = pygame.transform.scale(name, (width, height))
        self.Window.blit(name, (x - name.get_width()//2, y - name.get_height()//2))
        return name

    def image_not_center(self, name, x, y, width, height, image_name):
        name = pygame.image.load(f'assets/image/{image_name}.png').convert_alpha()
        name = pygame.transform.scale(name,(width,height))
        self.Window.blit(name, (x,y))
        return name
        
    def img_background(self, name, x, y, width, height, image_name):
        name = pygame.image.load(f'assets/image/{image_name}.png').convert_alpha()
        name = pygame.transform.scale(name, (width, height))
        self.Window.blit(name, (x - name.get_width()//2, y - name.get_height()//2))

    def hover_image(self, name_rect, name, x, y, width, height, image_name, image_name_hover): 
        name_rect = pygame.Rect( x - width//2, y - height//2, width, height)        
        if self.is_mouse_over_button(name_rect):
            self.img_center(name, x, y, width+5, height+5, image_name_hover)     
        else:
            self.img_center(name, x, y, width, height, image_name)
        return name_rect
 
# Def rectangle  
    def rect_full(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x - width//2, y - height//2, width, height),0, radius)
        return button
    
    def rect_full_not_centered(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x, y, width, height),0, radius)
        return button

    def rect_border(self, color, x, y, width, height, thickness, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x - width //2, y - height //2, width, height),  thickness, radius)
        return button
    
    # Rect border only on top  
    def rect_radius_top(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x - width //2, y - height //2, width, height),False,0, radius, radius)
        return button

    # Rect border only on bottom
    def rect_radius_bot(self, color, x, y, width, height, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x - width //2, y - height //2, width, height),False ,0,0,0, radius, radius)
        return button

# Def Circle
    def circle(self, color, x, y, radius):
        pygame.draw.circle(self.Window, color, (x,y), radius)

    def circle_alpha(self, alpha_color, x, y, radius):
        circle_surface = pygame.Surface((self.W,self.H), pygame.SRCALPHA)
        pygame.draw.circle(circle_surface,alpha_color,(x,y),radius)
        self.Window.blit(circle_surface, (0,0))

    def circle_hover(self, name, color,alpha_color, x, y, radius): 
        name = pygame.draw.circle(self.Window, color, (x,y), radius)

        if self.is_mouse_over_button(name):
            self.circle_alpha(alpha_color, x, y, radius)
        else:
            self.circle(color, x, y, radius)

# Def Hover
    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)
    
    def button_hover(self, name, x, y, width, height, color_full, color_border, color_hover, color_border_hover, text, font, text_color,text_size, thickness, radius): 

        name = pygame.Rect((x - width//2), (y - height//2), width, height)

        if self.is_mouse_over_button(name):
            self.rect_full(color_hover, x, y, width + 5, height + 5, radius)
            self.rect_border(color_border_hover, x, y, width + 5, height + 5, thickness, radius)
        else:
            self.rect_full(color_full, x, y, width, height, radius)
            self.rect_border(color_border, x, y, width, height, thickness, radius)
        self.text_center(font, text_size, text, text_color,  x, y)

        return name    
# Def Cursor 
    def normal_cursor(self):
        pygame.mouse.set_cursor(pygame.cursors.arrow)

    def hand_cursor(self):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

# Def BackgroundAlpha
    def screen_alpha(self, color):
        self.alpha_window = pygame.Surface((self.W, self.H), pygame.SRCALPHA)
        pygame.draw.rect(self.alpha_window, color, pygame.Rect(0,0, self.W, self.H))
        self.Window.blit(self.alpha_window, (0,0))
