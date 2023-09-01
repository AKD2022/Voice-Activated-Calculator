import os
import time
import pyaudio
from gtts import gTTS
import speech_recognition as sr
import playsound 

lang = 'en'
        

def removeAudio():
        os.remove("response.wav")


while True: 
    def recordAudio():
        said = ""
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try: 
                audio = r.listen(source)
                said = r.recognize_google(audio)
            except Exception:
                 print("Could translate, try again")
            
            try: 
                # Text To Audio
                mytext = said 
                if said == "2+2":
                     mytext = "four"   
                lang = 'en'
                myspeech = gTTS(text=mytext, lang=lang, slow=False)
                myspeech.save("response.wav")
                os.system("afplay response.wav")
                removeAudio()

            except Exception:
                print("You did not say anything, try again")
                

            if said == "end program":
                exit()

            
    
    recordAudio()

