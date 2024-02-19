from source.user import User
class Client(User):
    def __init__(self):
        super().__init__()

    def page_manager(self):
        pass

    def connect(self):
        pass

    def send_audio(self): 
        pass

    def StartAudioCon(self): 
        pass

    def Mute(self): 
        self.mute = True

    def Unmute(self): 
        self.mute = False


