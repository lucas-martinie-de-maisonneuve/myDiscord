import pyaudio, datetime
import pygame
import wave
import os
import time


class Recorder():
    
    def __init__(self):
        pygame.init()  

    def record_audio (self, duration=1, chunk=1024, channels=1, rate= 44100):
        audio = pyaudio.PyAudio()

        stream = audio.open(format=pyaudio.paInt16,
                            channels=channels,
                            rate=rate,
                            input=True,
                            frames_per_buffer=chunk)
        print("Recording...")

        frames = []

        for i in range(0, int(rate / chunk * duration)):
            data = stream.read(chunk)
            frames.append(data)

        print("Finished recording.")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        with wave.open("audio_liv.wav", 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(rate)
            wf.writeframes(b''.join(frames))


    def play_audio(filename):
        pygame.mixer.init()
        pygame.mixer.music.load("audio_liv.wav")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

  
    def audio_list_window(self):
        audio_list = True
        audio_list_surface = pygame.Surface((300, 100))
        audio_list_surface.fill((10, 61, 98))
        audio_list_font = pygame.font.SysFont(None, 24)
        audio_index = 1
        
        for message in self.mess.get_message_by_id_chanel(self.curent_chanel):
            type = self.mess.get_type_by_message(message[0])
            if type[0][0] == 'audio':
                audio_button = audio_list_font.render(f"Audio {audio_index}", True, (255, 255, 255))
                audio_list_surface.blit(audio_button, (10, (audio_index - 1) * 30))
                audio_index += 1
        
        while audio_list:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    audio_list = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        if 10 <= pos[0] <= 90 and 10 <= pos[1] <= 30:
                            self.lire_audio(self.mess.get_id_by_message(message[0]))
            self.window.fill((255, 255, 255))
            self.window.blit(audio_list_surface, (0, 0))
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()


     
        # self.window = pygame.display.set_mode((300, 100))
        # pygame.display.set_caption("Audio list")
        # self.clock = pygame.time.Clock()
    
    # def lire_audio(self, message_id):
    #     audio_blob = self.mess.get_message_by_id(message_id[0][0])
    #     if audio_blob != []:
    #         audio_file = f"temp_audio_{message_id}.wav"
    #         with open(audio_file, 'wb') as f:
    #             f.write(audio_blob[0][0])
    #         pygame.mixer.music.load(audio_file)
    #         pygame.mixer.music.play()
    #         while pygame.mixer.music.get_busy():
    #             self.clock.tick(10)
    #         pygame.mixer.quit()
    #         os.remove(audio_file)
    #     else:
    #         print("You have finished recording") 
