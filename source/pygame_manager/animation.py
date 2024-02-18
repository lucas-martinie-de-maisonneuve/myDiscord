class Animation():
    def __init__(self):

        self.img_growth = True
        self.img_shrink = False
        self.change_img = 1
        self.anim_y = 0

        self.anim_field = {
            "email": {"new_y": 0, "new_x": 0, "new_height": 0, "new_width": 0, "text_size": 0},
            "password": { "new_y": 0, "new_x": 0, "new_height": 0, "new_width": 0, "text_size": 0},
            "name": { "new_y": 0, "new_x": 0, "new_height": 0, "new_width": 0, "text_size": 0},
            "surname": { "new_y": 0, "new_x": 0, "new_height": 0, "new_width": 0, "text_size": 0},
            "username": { "new_y": 0, "new_x": 0, "new_height": 0, "new_width": 0, "text_size": 0}
        }
        
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
            self.img_center("Butterfly", x, y, size, self.anim_y,"home/home6")         
        elif self.change_img == 3:
            self.img_center("Bat", x, y, size, self.anim_y,"home/home7") 
        elif self.change_img == 4:
            self.img_center("Manta Ray", x, y, size, self.anim_y,"home/home8") 
        
        self.img_center("Logo Discord", x, logo_y, logo_size, logo_size,"home/home10")

    def text_input(self, rect, input, text, x, y, width, height, id):
        if self.is_mouse_over_button(rect) or input != "":
            if self.anim_field[id]["new_y"] < height / 2:
                self.anim_field[id]["new_x"] += ((width * 70 / 100 ) / 10)
                self.anim_field[id]["new_y"] +=  height / 10
                self.anim_field[id]["new_width"] += width / 7
                self.anim_field[id]["new_height"] += height / 10
                self.anim_field[id]["text_size"] += 1
            self.rect_full(self.grey2, (x - self.anim_field[id]["new_x"]), y - self.anim_field[id]["new_y"], width - self.anim_field[id]["new_width"], height - self.anim_field[id]["new_height"], 5)
            self.rect_border(self.black, (x - self.anim_field[id]["new_x"]), y - self.anim_field[id]["new_y"], width - self.anim_field[id]["new_width"], height - self.anim_field[id]["new_height"], 2, 5)
            self.text_center(self.font2, 15 - self.anim_field[id]["text_size"], text, self.white, (x - self.anim_field[id]["new_x"]), y - self.anim_field[id]["new_y"])
        else:
            if self.anim_field[id]["new_y"] > 0:
                self.anim_field[id]["new_x"] -= ((width * 70 / 100 ) / 10)
                self.anim_field[id]["new_y"] -= height / 10
                self.anim_field[id]["new_width"] -= width / 7
                self.anim_field[id]["new_height"] -= height / 10
                self.anim_field[id]["text_size"] -= 1
                self.rect_border(self.black, (x - self.anim_field[id]["new_x"]), y - self.anim_field[id]["new_y"], width - self.anim_field[id]["new_width"], height - self.anim_field[id]["new_height"], 2, 5)
            self.rect_full(self.grey2,(x - self.anim_field[id]["new_x"]), y - self.anim_field[id]["new_y"], width - self.anim_field[id]["new_width"], height - self.anim_field[id]["new_height"], 5)
            self.text_center(self.font2, 15 - self.anim_field[id]["text_size"], text, self.white,(x - self.anim_field[id]["new_x"]), y - self.anim_field[id]["new_y"])


