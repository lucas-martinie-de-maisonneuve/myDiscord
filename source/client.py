from source.User import User
class Client(User):
    def __init__(self):
        super().__init__()

    def page_manager(self):
        pass

    def connect(self):
        pass

    def send_audio(self): 
        pass

    def start_audio_con(self): 
        pass

    def mute(self): 
        self.mute = True

    def unmute(self): 
        self.mute = False


