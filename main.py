import speech_recognition as sr
import webbrowser
import pyttsx3
import ggtsx
import musicLibrary
import requests
import pygame
import os
from openai import OpenAI #Open ai API is paid


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "Use your news api key"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    client = OpenAI(api_key="use your api key open ai")

    completion = client.chat.completions.create(
    model= "chatgpt-4o-latest",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks."},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")

    elif "open linkdin" in c.lower():
        webbrowser.open("https://linkdin.com")

    elif "open github" in c.lower():
        webbrowser.open("https://github.com")

    elif c.lower().startswith("play"):
        
         song = c.lower().split(" ")[1]
         link = musicLibrary.music[song]
         webbrowser.open(link)
    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()

            articles = data.get('articles', [])

            for article in articles:
                speak(article['title'])

    else:
        output = aiprocess(c)
        speak(output)

if __name__ == "__main__" :
    speak("Initializing jarvis...")
    while True:

        #Listen for the wake word Morgen
        #obtain audio from microphone
        r = sr.Recognizer()
        
        print("Recognizing...")
        try:
            audio = None
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))

            #Code is completed
