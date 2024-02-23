from source.pygame_manager.Element import Element
from data.DiscordManager import DiscordManager
import pygame
from PIL import Image, ImageFilter
from io import BytesIO
class AddChannel(Element, DiscordManager):

    def __init__(self):
        Element.__init__(self)
        DiscordManager.__init__(self)
        self.add_channel_running = True
        self.new_name_channel = ""
        self.entry_new_name = 0

    def background(self): 
        self.img_background1('Background', 600, 350, 1200, 800, 'main_page/main_page8', blur_radius=10)
        
    def img_background_blur(self, name, x, y, width, height, image_name, blur_radius=5):
        name = pygame.image.load(f'assets/image/{image_name}.png').convert_alpha()
        name = pygame.transform.scale(name, (width, height))
        self.Window.blit(name, (x - name.get_width()//2, y - name.get_height()//2))

        image_bytes = BytesIO()
        pygame.image.save(name, image_bytes)
        image_bytes.seek(0)
        pillow_image = Image.open(image_bytes)
        blurred_pillow_image = pillow_image.filter(ImageFilter.GaussianBlur(radius=blur_radius))
        blurred_image = pygame.image.fromstring(
            blurred_pillow_image.tobytes(), 
            blurred_pillow_image.size, 
            blurred_pillow_image.mode
        )
        self.Window.blit(blurred_image, (x - width // 2, y - height // 2))

    def second_section(self):
        # Rectangle de fond
        self.rect_full(self.grey10, 600, 400, 500, 510, 10)
        
        self.text_center(self.font1, 31, "ADD CHANNEL", self.grey1, 600, 200)
        
        self.text_center(self.font2, 21, "Name Channel", self.grey1, 600, 270)
        self.rect_full(self.grey9, 600, 320, 300, 30, 10)
        
        self.text_center(self.font2, 21, "Category", self.grey1, 600, 370)
        
        self.rect_full(self.grey9, 540, 405, 100, 30, 10)
        self.text_center(self.font2, 16, "Bachelor IT", self.grey1, 540, 405)
        
        self.rect_full(self.grey9, 650, 405, 100, 30, 10)
        self.text_center(self.font2, 16, "Talk Talk", self.grey1, 650, 405)
        
        self.text_center(self.font2, 21, "Communication", self.grey1, 600, 465)
        
        self.rect_full(self.grey9, 537, 500, 100, 30, 10)
        self.text_center(self.font2, 16, "Text", self.grey1, 537, 500)
        
        self.rect_full(self.grey9, 655, 500, 100, 30, 10)
        self.text_center(self.font2, 16, "Vocal", self.grey1, 655, 500)

        self.text_center(self.font2, 21, "Status", self.grey1, 600, 550)
        
        self.rect_full(self.grey9, 535, 580, 100, 30, 10)
        self.text_center(self.font2, 16, "Private", self.grey1, 535, 580)
        
        self.rect_full(self.grey9, 655, 580, 100, 30, 10)
        self.text_center(self.font2, 16, "Public", self.grey1, 655, 580)
                # logo choix
        self.img_center("Volume logiciel", 465, 499, 35, 35,"main_page/main_page10")
        self.img_center("Hashtags logiciel", 725, 498, 25, 25,"main_page/main_page14") 
        # Neon light blue
        self.img_center("Neon light", 600, 170, 240, 90,"main_page/main_page7")
        self.img_center("Neon light", 600, 225, 240, 90,"main_page/main_page7")
       # self.rect_full(self.grey9, 600, 320, 300, 30, 10)

        

        
        
        
        
        

        # # Rectangle de fond
        
        
        # # Check Bachelor IT 
        # # self.img_center("Check NO", 470, 420, 25, 25,"profile/check1")
        # # self.img_center("Check YES", 470, 420, 35, 34,"profile/check2")
        # # self.img_center("Check YES", 470, 420, 136, 134,"profile/check2")
        
        
        # # Check Talk Talk
        # # self.img_center("Check NO", 730, 420, 45, 40,"profile/check1")
        # # self.img_center("Check YES", 730, 420, 45, 40,"profile/check2")
        

        

        # # self.img_center("Neon Light", 260, 630, 140, 105,"main_page/main_page7") 
    def addChannel_run(self):
        while self.add_channel_running :
            self.background()
            self.second_section()
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.add_channel_running = False 
                
test = AddChannel()
test.addChannel_run()