import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
# from openai import OpenAI
# from gtts import gTTS
# import pygame
# import os

# pip install pocketsphinx
# pip install pyttsx3
# pip install SpeechRecognition
# pip install pyaudio
# pip install requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "08b7d42373da408286dd333fc19371d1"


def speak(text):
    engine.say(text)
    engine.runAndWait()

# def speak_old(text):
#     tts = gTTS(text)
#     tts.save("temp.mp3")
    
#     # Initialize Pygame mixer
#     pygame.mixer.init()

#     # Load the MP3 file
#     pygame.mixer.music.load('temp.mp3')

#     # Play the MP3 file
#     pygame.mixer.music.play()

#     # Keep the program running until the music stops playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)

#     # Clean up
#     pygame.mixer.music.unload()
#     os.remove("temp.mp3")


# def aiProcess(command):
#     client = OpenAI(api_key="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",)

# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
#         {"role": "user","content": command}
#     ]
# )

# print(completion.choices[0].message.content)


def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "Open Facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com/")
    elif "Open Instagram" in c.lower():
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com/")
    elif "Open LinkedIn" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com/in/somen-pradhan-154741298/")
    elif "open YouTube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)


    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response 
            data = r.json()

            # Extract the articles
            articles = data.get('articles',[])

            # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        # Let OpenAI handle the request
        # output = aiProcess(c)
        # speak(output)
        pass
            
        



if __name__ == "__main__":
    speak("Initializing Jarvis......")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone

        r = sr.Recognizer()
        
    
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)



        except Exception as e:
             print("Error; {0}".format(e))