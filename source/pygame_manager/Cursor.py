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
        self.profile1_cursor = False 
        self.profile2_cursor = False 
        self.profile3_cursor = False 
        self.profile4_cursor = False

        self.linkedinI_cursor = False
        self.githubI_cursor = False
        self.mailI_cursor = False
        self.linkedinL_cursor = False
        self.githubL_cursor = False
        self.mailL_cursor =  False
        self.linkedinV_cursor = False
        self.githubV_cursor = False
        self.mailV_cursor = False
        self.FacebookP_cursor = False 
        self.linkedinP_cursor = False
        self.twitterP_cursor = False
        self.instagramP_cursor = False 
        self.youtubeP_cursor = False 
        self.brochureP_cursor = False 
        self.cannes_cursor = False
        self.toulon_cursor = False
        self.marseille_cursor = False
        self.martigues_cursor = False

        self.bell_cursor = False
        self.link_logo_rect_cursor = False
        self.server_c_cursor = False
        self.settings_c_cursor = False
        self.poweroff_c_cursor = False
        self.input_search_rect_cursor = False
        self.notification_c_cursor = False
    
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
            self.profile1_cursor, self.profile2_cursor, self.profile3_cursor, self.profile4_cursor,
            self.surname_cursor, self.name_cursor, self.linkedinI_cursor, self.linkedinI_cursor, self.githubI_cursor, self.mailI_cursor, self.linkedinL_cursor, self.githubL_cursor, self.mailL_cursor, self.linkedinV_cursor, self.githubV_cursor, self.mailV_cursor, self.FacebookP_cursor, self.linkedinP_cursor, self.twitterP_cursor, self.instagramP_cursor, self.youtubeP_cursor, self.brochureP_cursor, self.cannes_cursor, self.toulon_cursor, self.marseille_cursor, self.martigues_cursor, self.bell_cursor,   self.link_logo_rect_cursor, self.server_c_cursor, self.settings_c_cursor, self.poweroff_c_cursor, self.input_search_rect_cursor, self.notification_c_cursor
        ])

    def profile_page_cursor(self):
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

    def  main_page_cursor(self):
        self.bell_cursor = self.set_cursor(self.bell, self.bell_cursor)
        self.link_logo_rect_cursor = self.set_cursor(self.link_logo_rect, self.link_logo_rect_cursor)
        self.server_c_cursor = self.set_cursor(self.server_c, self.server_c_cursor)
        self.settings_c_cursor = self.set_cursor(self.settings_c, self.settings_c_cursor)
        self.poweroff_c_cursor = self.set_cursor(self.poweroff_c, self.poweroff_c_cursor)
        self.input_search_rect_cursor = self.set_cursor(self.input_search_rect, self.input_search_rect_cursor)
        self.notification_c_cursor = self.set_cursor(self.notification_c, self.notification_c_cursor)

    def register_cursor(self):
        self.profile1_cursor = self.set_cursor(self.p_profile1, self.profile1_cursor)
        self.profile2_cursor = self.set_cursor(self.p_profile2, self.profile2_cursor) 
        self.profile3_cursor = self.set_cursor(self.p_profile3, self.profile3_cursor) 
        self.profile4_cursor = self.set_cursor(self.p_profile4, self.profile4_cursor)
        self.login_cursor = self.set_cursor(self.sign_up, self.login_cursor)
        self.sign_cursor = self.set_cursor(self.sign, self.sign_cursor)
        self.username_cursor = self.set_cursor(self.username_rect, self.username_cursor)
        self.email_cursor = self.set_cursor(self.email_rect, self.email_cursor)
        self.surname_cursor = self.set_cursor(self.surname_rect, self.surname_cursor)
        self.name_cursor = self.set_cursor(self.name_rect, self.name_cursor)
        self.password_cursor = self.set_cursor(self.password_rect, self.password_cursor)

    def contact_cursor(self):
     
        self.linkedinI_cursor = self.set_cursor(self.linkedinI, self.linkedinI_cursor)
        self.githubI_cursor = self.set_cursor(self.githubI, self.linkedinI_cursor)
        self.mailI_cursor = self.set_cursor(self.mailI, self.mailI_cursor )
        self.linkedinL_cursor = self.set_cursor( self.linkedinL, self.linkedinL_cursor)
        self.githubL_cursor = self.set_cursor(self.githubL, self.githubL_cursor )
        self.mailL_cursor =  self.set_cursor (self.mailL, self.mailL_cursor)
        self.linkedinV_cursor = self.set_cursor( self.linkedinV,  self.linkedinV_cursor)
        self.githubV_cursor = self.set_cursor(self.githubV, self.githubV_cursor)
        self.mailV_cursor = self.set_cursor(self.mailV, self.mailV_cursor)
        self.FacebookP_cursor = self.set_cursor(self.FacebookP, self.FacebookP_cursor)
        self.linkedinP_cursor = self.set_cursor(self.linkedinP, self.linkedinP_cursor)
        self.twitterP_cursor = self.set_cursor(self.twitterP, self.twitterP_cursor)
        self.instagramP_cursor = self.set_cursor(self.instagramP, self.instagramP_cursor)
        self.youtubeP_cursor = self.set_cursor(self.youtubeP, self.youtubeP_cursor ) 
        self.brochureP_cursor = self.set_cursor(self.brochureP, self.brochureP_cursor)
        self.cannes_cursor = self.set_cursor(self.cannes, self.cannes_cursor)
        self.toulon_cursor = self.set_cursor(self.toulon, self.toulon_cursor)
        self.marseille_cursor = self.set_cursor( self.marseille,  self.marseille_cursor)
        self.martigues_cursor = self.set_cursor(self.martigues, self.martigues_cursor)

    
    
