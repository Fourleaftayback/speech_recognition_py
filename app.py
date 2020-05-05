import time
from speechRecognition import respond, record_audio
from speak import Speak

speak = Speak(audio_lang='en')

time.sleep(1)
speak.play_sound('Whats up?')


while 1:
    data = record_audio()
    respond(data)

