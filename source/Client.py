import time
from data.DiscordManager import DiscordManager
from hashlib import sha256
from source.pyaudio.Recorder import Recorder

class Client(DiscordManager, Recorder):
    def __init__(self):
        super().__init__()
        
        self.connected = False
        self.profile_password = ""
        self.home_running = False
        self.user_email = ""
        self.user_password = ""
        self.user_info = (0, '', '', '', '', '', 0, 0)
        self.user = (0, '', '', '', '', '', 0, 0)   

        self.register_username = ""
        self.register_email = ""
        self.register_surname = ""
        self.register_name = ""
        self.register_password = ""
        self.register_photo = 0
        self.registered = False
        self.username, self.email, self.picture, self.hashed_password = "", "", 0, ""

        self.new_name_channel = ""
        self.status = None
        self.communication = None
        self.category = None
        self.add = False        
        
        self.register_to_login = False 
        self.main_page_to_login = False
        self.profile_to_login = False

        self.login_to_register = False
        self.register_running = False

        self.profile_modified = False
        self.register_to_main_page = False
        self.profile_to_main_page = False
        self.home_to_main_page = False
        self.main_page_running = False
        
        self.main_page_to_profile = False
        self.contact_to_profile = False
        self.profile_running = False

        self.profile_to_contact = False
        self.contact_running = False
        self.contact_to_profile = False
        self.add_channel_running = False
        self.main_page_to_add_channel = False
        self.add_channel_to_main_page = False

        self.actual_channel = 1
        self.message = ""
        
        self.categories = self.display_category()
        self.channels = self.display_channel()
        self.messages = self.get_message(self.actual_channel)
        self.community_list = self.display_user()  
        self.request = self.display_admin_request()
        # self.emoji_display = self.emoji_react()

        # Notification
        self.new_message = 0                
        
    def login_user(self):
        hashed_password = sha256(self.user_password.encode()).hexdigest()

        if self.check_credentials(self.user_email, hashed_password):
            self.user_info = self.get_user(self.user_email, hashed_password)
            self.connected = True
            return self.user_info
        
    def abc_password(self, user_id): 
        self.profile_password = self.get_password(user_id)
        return self.profile_password[0][0]

    def register_user(self):
            hashed_password = sha256(self.register_password.encode()).hexdigest()
            self.add_user(self.register_surname, self.register_name, self.register_username, self.register_email, hashed_password, self.register_photo, 2)
            self.user_info = self.get_user(self.register_email, hashed_password)
            self.add_abc_password(self.register_password, self.user_info[0])
            return self.user_info
        
    def add_channel_client(self):
        self.add_channel(self.new_name_channel,self.status,self.communication,self.category)
        
    def update_message(self):
        self.messages = self.get_message(self.actual_channel)

    def add_message(self):
        if self.message != "":
            self.save_message(self.user_info[3], self.message, self.actual_channel)
            self.messages = self.get_message(self.actual_channel)
            self.message = ""

    def modify_user(self, pseudo, email, password,photo, id, user):

        hashed_password = sha256(password.encode()).hexdigest()

        self.update_user(pseudo, email, hashed_password, photo, id)
        self.update_message_author(pseudo, user)
        self.update_abc_password(password, id)
        self.user = self.get_user(self.email, hashed_password)
        return self.user
        
        # Notification
    def load_info_last_message(self, user): 
        self.last_login_date = self.get_last_message_time(user)
        return self.last_login_date
    
    def reset_new_message_counter(self):
        self.new_message = 0

        # Audio
    def audio_table(self): 

        # filename = f"{id_channel}_{datetime.now().strftime('%Y%m%d%H%M%S')}.wav"

        self.create_and_save(self.user_info[3], self.message1, self.actual_channel)


    def change_role_request(self):
        self.update_role_request(self.email)
        self.user = self.get_user(self.email, self.hashed_password)
        return self.user
    
    def change_role_validate(self, user_id):
        self.upgrade_role(user_id)
        self.request = self.display_admin_request()
        return self.request

    def change_role_denyed(self, user_id):
        self.deny_upgrade_role(user_id)
        self.request = self.display_admin_request()
        return self.request
    
    def channel_deleted(self, id_channel):
        self.delete_channel_message(id_channel)
        self.delete_channel(id_channel)
        self.channels = self.display_channel()
        return self.channels
    
    def channel_private(self, id_channel):
        user_role = self.get_user_role(self.user_info[0])
        channel_status = self.get_channel_status(id_channel)
        user = user_role[0][0]
        status = channel_status[0][0]
        if user == 2 and status == 1:
            return False
        else:
            return True