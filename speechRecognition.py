import speech_recognition as sr
import datetime
import webbrowser
from speak import Speak

r = sr.Recognizer()
speak = Speak(audio_lang='en')


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak.play_sound(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak.play_sound('Sorry, I did not get that')
        except sr.RequestError:
            speak.play_sound('Speech service is down')
        return voice_data


def respond(voice_data):
    if 'what is your name' in voice_data:
        speak.play_sound('My name is speech app.')
    if 'what time is it' in voice_data:
        current_time = datetime.datetime.now()
        speak.play_sound(current_time.strftime("%I:%M:%S %p"))
    if 'search' in voice_data:
        # figure out what is going on with this line
        search = record_audio("What do you want to search for?")
        url = 'http://google.com/search?q=' + search
        speak.play_sound(url)
        webbrowser.get().open(url)
        speak.play_sound('Here is what I found for ' + search)
    if 'find location' in voice_data:
        # figure out what is going on with this line
        location = record_audio("What is the location")
        url = 'http://google.nl/maps/place/' + location
        speak.play_sound(url)
        webbrowser.get().open(url)
        speak.play_sound('Here is the location ' + location)
    if 'exit' in voice_data:
        exit()