import speech_recognition as sr
import pyttsx3 
import webbrowser
import os
import requests
import pyjokes
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand.")
            return ""
        except sr.RequestError:
            print("Request error.")
            return ""

def perform_task(command):
    if 'open browser' in command:
        speak("Opening browser.")
        webbrowser.open("https://www.google.com")
    elif 'i am fine' in command:
        speak("Great to hear that sir")
    elif 'open notepad' in command:
        speak("Opening Notepad.")
        os.system('notepad')
    elif 'time' in command:
        from datetime import datetime
        current_time = datetime.now().strftime('%H:%M')
        speak(f"The current time is {current_time}.")
    elif 'open calculator' in command:
        speak("Opening Calculator.")
        os.system('calc')
    elif 'open youtube' in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif 'tell me a joke' in command:
        joke = pyjokes.get_joke()
        speak(joke)
    else:
        speak("I don't understand that command.")

if __name__ == "__main__":
    speak("Hello pawan, I am your personal , how may i assist you.")
    while True:
        command = listen()
        if 'exit' in command:
            speak("Goodbye pawan!")
            break
        else:
            perform_task(command)
