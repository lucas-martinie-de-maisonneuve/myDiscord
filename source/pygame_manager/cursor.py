import pygame

class Cursor:
    def __init__(self):
        self.password_cursor = False
        self.pass_cursor = False
        self.picture_cursor = False
        self.username_cursor = False
        self.email_cursor = False
        self.role_cursor = False
        self.status_cursor = False
        self.surname_cursor = False
        self.name_cursor = False
        self.picture1_cursor = False
        self.picture2_cursor = False
        self.picture3_cursor = False
        self.disconnect_cursor = False
        self.status_edit_cursor = False
        self.status_active_cursor = False
        self.google_cursor = False
        self.facebook_cursor = False
        self.instagram_cursor = False
        self.forgot_p_cursor = False
        self.login_cursor = False
        self.sign_cursor = False
        self.profil1_cursor = False 
        self.profil2_cursor = False 
        self.profil3_cursor = False 
        self.profil4_cursor = False


    def set_cursor(self, rect, button):
        if self.is_mouse_over_button(rect):
            button = True
            self.hand_cursor()
        else:
            button = False

        if self.all_false():
            self.normal_cursor()

        return button

    def all_false(self):
        return not any([
            self.password_cursor, self.pass_cursor, self.picture_cursor,
            self.username_cursor, self.email_cursor, self.role_cursor,
            self.status_cursor, self.picture1_cursor, self.picture2_cursor,
            self.picture3_cursor, self.disconnect_cursor, self.status_edit_cursor,
            self.status_active_cursor, self.login_cursor, self.google_cursor,
            self.facebook_cursor, self.instagram_cursor, self.forgot_p_cursor, self.sign_cursor,
            self.profil1_cursor, self.profil2_cursor, self.profil3_cursor, self.profil4_cursor,
            self.surname_cursor, self.name_cursor
        ])

    def profil_page_cursor(self):
        self.username_cursor = self.set_cursor(self.username_rect, self.username_cursor)
        self.email_cursor = self.set_cursor(self.email_rect, self.email_cursor)
        self.pass_cursor = self.set_cursor(self.password_rect, self.pass_cursor)
        self.role_cursor = self.set_cursor(self.role_rect, self.role_cursor)
        self.status_cursor = self.set_cursor(self.status_rect, self.status_cursor)
        self.disconnect_cursor = self.set_cursor(self.disconnect_button, self.disconnect_cursor)
        self.picture_cursor = self.set_cursor(self.profile_pict, self.picture_cursor)
        self.status_edit_cursor = self.set_cursor(self.status_edit_rect, self.status_edit_cursor)
        self.status_active_cursor = self.set_cursor(self.status_active_rect, self.status_active_cursor)
        self.picture1_cursor = self.set_cursor(self.picture1, self.picture1_cursor)
        self.picture2_cursor = self.set_cursor(self.picture2, self.picture2_cursor)
        self.picture3_cursor = self.set_cursor(self.picture3, self.picture3_cursor)
        self.password_cursor = self.set_cursor(self.show, self.password_cursor)

    def home_page_cursor(self):
        self.login_cursor = self.set_cursor(self.login, self.login_cursor)
        self.facebook_cursor = self.set_cursor(self.facebook, self.facebook_cursor)
        self.instagram_cursor = self.set_cursor(self.instagram, self.instagram_cursor)
        self.google_cursor = self.set_cursor(self.google, self.google_cursor)
        self.sign_cursor = self.set_cursor(self.sign, self.sign_cursor)
        self.forgot_p_cursor = self.set_cursor(self.forgot_p, self.forgot_p_cursor)
        self.email_cursor = self.set_cursor(self.input_email_rect, self.email_cursor)
        self.password_cursor = self.set_cursor(self.input_password_rect, self.password_cursor)

    def register_cursor(self):
        self.profil1_cursor = self.set_cursor(self.p_profil1, self.profil1_cursor)
        self.profil2_cursor = self.set_cursor(self.p_profil2, self.profil2_cursor) 
        self.profil3_cursor = self.set_cursor(self.p_profil3, self.profil3_cursor) 
        self.profil4_cursor = self.set_cursor(self.p_profil4, self.profil4_cursor)
        self.login_cursor = self.set_cursor(self.sign_up, self.login_cursor)
        self.sign_cursor = self.set_cursor(self.sign, self.sign_cursor)
        self.username_cursor = self.set_cursor(self.username_rect, self.username_cursor)
        self.email_cursor = self.set_cursor(self.email_rect, self.email_cursor)
        self.surname_cursor = self.set_cursor(self.surname_rect, self.surname_cursor)
        self.name_cursor = self.set_cursor(self.name_rect, self.name_cursor)
        self.password_cursor = self.set_cursor(self.password_rect, self.password_cursor)
