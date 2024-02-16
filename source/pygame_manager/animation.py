class Animation():
    def __init__(self):

        self.img_growth = True
        self.img_shrink = False
        self.change_img = 1

        self.anim_y = 0

# Animated pictures on home page
    def logo_home(self, x, y, size, logo_y, logo_size):
        if self.img_growth: # Growing image
            if self.anim_y < size:
                self.anim_y += 10
            elif self.anim_y == size:
                self.img_shrink = True
                self.img_growth = False

        if self.img_shrink: #Shrinking image
            if self.anim_y > 0:
                self.anim_y -= 10
            elif self.anim_y == 0:
                if self.change_img < 4: 
                    self.change_img += 1
                else:
                    self.change_img = 1
                self.img_growth = True
                self.img_shrink = False

        if self.change_img == 1:
            self.img_center("0wl", x, y, size, self.anim_y,"home/home9")
        elif self.change_img == 2:
            self.img_center("Wolf", x, y, size, self.anim_y,"home/home6")         
        elif self.change_img == 3:
            self.img_center("Cheetah", x, y, size, self.anim_y,"home/home8") 
        elif self.change_img == 4:
            self.img_center("Lion", x, y, size, self.anim_y,"home/home7") 
        
        self.img_center("Logo Discord", x, logo_y, logo_size, logo_size,"home/home10")