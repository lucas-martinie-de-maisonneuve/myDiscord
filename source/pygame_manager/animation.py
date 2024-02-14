class Animation():
    def __init__(self):

        self.img_growth = True
        self.img_shrink = False
        self.change_img = 1

        self.anim_y = 0

# Animated pictures on home page
    def logo_home(self):
        if self.img_growth: # Growing image
            if self.anim_y < 370:
                self.anim_y += 10
            elif self.anim_y == 370:
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
            self.img_center("0wl", 355, 180, 370, self.anim_y,"home/home9")
        elif self.change_img == 2:
            self.img_center("Wolf", 355, 180, 370, self.anim_y,"home/home6")         
        elif self.change_img == 3:
            self.img_center("Cheetah", 355, 180, 370, self.anim_y,"home/home8") 
        elif self.change_img == 4:
            self.img_center("Lion", 355, 180, 370, self.anim_y,"home/home7") 
        
        self.img_center("Logo Discord", 355, 200, 150, 150,"home/home10")