import os
import re
import math
from gtts import gTTS
import speech_recognition as sr
import sympy as sp
from word2number import w2n

def rec():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        try:
            audio = r.listen(source)
            said = r.recognize_google(audio)
            print(said)
        except Exception:
            print("No Audio Recorded, try again.")

        if said == "end program":
            exit()

    return said

def extract_math_expression(user_input):
    # Use regular expressions to extract mathematical expressions
    pattern = r'(?i)what is (.*)'
    match = re.search(pattern, user_input)
    if match:
        return match.group(1)
    else:
        return user_input

def solve_problem(user_input):
    try:
        # Replace common words with their mathematical symbols or functions
        user_input = user_input.replace("pi", str(math.pi))
        user_input = user_input.replace("plus", "+")
        user_input = user_input.replace("minus", "-")
        user_input = user_input.replace("times", "*")
        user_input = user_input.replace("divided by", "/")
        
        # Handle square roots
        user_input = user_input.replace("square root", "sqrt")
        
        # Use sympy to evaluate the user's input as a symbolic expression
        expr = sp.sympify(user_input)
        result = sp.simplify(expr)
        print(result)
        return result
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def answerAudio(user_input):
    language = 'en'
    math_expression = extract_math_expression(user_input)
    result = solve_problem(math_expression)
    
    if result is not None:
        response = gTTS(text=f"The result is {result}", lang=language, slow=False)
        response.save("answer.wav")
        os.system("afplay answer.wav")

while True:
    user_input = rec()
    if user_input == "end program":
        os.remove("answer.wav")
        break
    answerAudio(user_input)
