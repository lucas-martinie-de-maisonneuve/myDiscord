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

    def play_audio_in_channel(self, id_channel):
        if  id_channel == 4:  
            audio_filename = "output1.wav"
        elif id_channel == 6:  
            audio_filename = "output2.wav"
        elif id_channel == 9:  
            audio_filename = "output3.wav"

        pygame.mixer.init()
        pygame.mixer.music.load(audio_filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
