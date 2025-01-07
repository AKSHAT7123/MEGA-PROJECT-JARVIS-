import speech_recognition as sr
import webbrowser
import pyttsx3
import MusicLibrary
import requests
import pygame
from gtts import gTTS
import google.generativeai as genai
import os

recongnizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi ="77d17805783343e3a647572ae3fa0290"
def speak_old(text):
    engine.say(text)
    engine.runAndWait()
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")
def AiProcess(command):
    genai.configure(api_key="AIzaSyAx75B1ohkguToQ31n5jFGCaxom1QjAMjw")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"{command} Respond with a shorter answer")
    speak(response.text)
    # return completion.choices[0].message.content
def ProcessCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song =c.lower().split(" ")[1]
        link = MusicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code==200:
            # Parse the JSON response
            data = r.json()
            # Extract the Articles
            articles = data.get("articles",[])
            # Print the Headlines
            for article in articles:
                speak(article["title"])
    else:
        #Let OpenAI handle the request
        output = AiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # Listen for the wake word "Jarvis"
        # Obtain audi from the microphone
        r=sr.Recognizer()
        # Reciignize speech using Sphinx
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    ProcessCommand(command)

        except Exception as e:
            print("error; {0}".format(e))

