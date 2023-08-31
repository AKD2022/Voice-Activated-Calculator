import os
import time
import pyaudio
from gtts import gTTS
import speech_recognition as sr
import playsound 

lang = 'en'


def textToAudio():
        said = ""
        mytext = said
        lang = 'en'
        myspeech = gTTS(text=mytext, lang=lang, slow=False)
        myspeech.save("response.wav")
        os.system("afplay response.wav")

def removeAudio():
        os.remove("response.wav")


while True: 
    def recordAudio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

            said = r.recognize_google(audio)
            print(said)    

            if said == "end program":
                exit()

            textToAudio()
            removeAudio()

            
    
    recordAudio()
