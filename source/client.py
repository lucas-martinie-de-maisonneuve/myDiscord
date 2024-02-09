import socket 
import pyaudio

class Client:
    def __init(self, server): 
        self.server_ip = 
        self.server_port = 
        self.server_connection = (socket.AF_INET, socket.SOCK_STREAM)    

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


HOST = '192.168.243.1'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

