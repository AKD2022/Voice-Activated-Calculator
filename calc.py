import os 
import pyaudio
import playsound
from gtts import gTTS
import speech_recognition as sr


def rec():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:

        try:
            audio = r.listen(source)
            said = ""
            said = r.recognize_google(audio)
            print(said)
        except Exception:
            print("No Audio Recorded, try again.")
    return said

def solve_problem():
    solve_problem = rec()

    result = eval(solve_problem)
    print(result)
    

while True:
    rec()
    solve_problem()