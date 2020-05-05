import playsound
import os
import random
from gtts import gTTS


class Speak:
    def __init__(self, audio_lang='en'):
        self.audio_lang = audio_lang
        print(self.audio_lang)

    def play_sound(self, audio_string):
        tts = gTTS(audio_string, lang=self.audio_lang)
        random_string = random.randint(1, 1000000)
        audio_file = 'audio-' + str(random_string) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(audio_string)
        os.remove(audio_file)
