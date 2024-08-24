import tkinter as tk
import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import os
import pyautogui
import random
import webbrowser
import datetime

from Calculatenumbers import WolfRamAlpha

# Initialize pyttsx3 engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
        return query
    except Exception as e:
        print("Say that again")
        return "None"

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis. How may I help you?")

def searchGoogle(query):
    query = query.replace("jarvis", "")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def searchYoutube(query):
    query = query.replace("jarvis", "")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def searchWikipedia(query):
    query = query.replace("jarvis", "")
    webbrowser.open(f"https://en.wikipedia.org/wiki/{query}")

def latestnews():
    url = "https://news.google.com/news/rss"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features='xml')
    news_list = soup.findAll('item')
    speak("Here are some top news from the world")
    for news in news_list:
        print(news.title.text)
        speak(news.title.text)

def Calc(query):
    app_id = "Wolframalpha app_id"  # Get your own API key from Wolframalpha
    client = WolfRamAlpha.Client(app_id)

    res = client.query(query)
    answer = next(res.results).text
    speak(f"The answer is {answer}")

def sendMessage():
    speak("Opening Whatsapp...")
    webbrowser.open("https://web.whatsapp.com/")

def openappweb(query):
    apps = {
        "chrome": "https://www.google.com/",
        "firefox": "https://www.mozilla.org/en-US/firefox/new/",
        "notepad": "notepad.exe",
        # Add more apps and their URLs here
    }
    app_name = query.split("open", 1)[1].strip()
    if app_name in apps:
        speak(f"Opening {app_name}")
        webbrowser.open_new(apps[app_name])
    else:
        speak("Sorry, I couldn't find that app.")

def closeappweb(query):
    apps = {
        "chrome": "chrome",
        "firefox": "firefox",
        "notepad": "notepad",
        # Add more apps here
    }
    app_name = query.split("close", 1)[1].strip()
    if app_name in apps:
        speak(f"Closing {app_name}")
        os.system(f"TASKKILL /F /IM {apps[app_name]}.exe")
    else:
        speak("Sorry, I couldn't find that app.")

def volumeup():
    pyautogui.press("volumeup")

def volumedown():
    pyautogui.press("volumedown")

# Create the main window
root = tk.Tk()
root.title("AI Voice Assistant")
root.geometry("400x400")
root.configure(bg="#2c3e50")  # Set background color

# Create text area with a dark theme
text_area = tk.Text(root, font=("Helvetica", 12), bg="#34495e", fg="white", insertbackground="white", bd=0)
text_area.pack(fill="both", expand=True, padx=20, pady=10)

# Create entry field with a dark theme
input_field = tk.Entry(root, font=("Helvetica", 12), bg="#34495e", fg="white", insertbackground="white", bd=0)
input_field.pack(pady=10, padx=20, fill="x")

def speakButtonClicked():
    query = input_field.get()
    text_area.insert(tk.END, f"You Said: {query}\n")
    speak(query)

def textButtonClicked():
    query = takeCommand().lower()
    text_area.insert(tk.END, f"You Said: {query}\n")
    speak("Processing...")
    if "wake up" in query:
        greetMe()
    elif "change password" in query:
        speak("What's the new password?")
        new_pw = input("Enter the new password\n")
        new_password = open("password.txt","w")
        new_password.write(new_pw)
        new_password.close()
        speak("Done sir")
        speak(f"Your new password is {new_pw}")
    elif "hello" in query:
        speak("Hello sir, how are you?")
    elif "i am fine" in query:
        speak("That's great, sir")
    elif "how are you" in query:
        speak("Perfect, sir")
    elif "thank" in query:
        speak("You are welcome, sir")
    elif "tired" in query:
        speak("Playing your favorite songs, sir")
        a = (1,2,3)
        b = random.choice(a)
        if b == 1:
            webbrowser.open("https://www.youtube.com/results?search_query=hamari+adhuri+kahani+song")
    elif "pause" in query:
        pyautogui.press("k")
        speak("video paused")
    elif "play" in query:
        pyautogui.press("k")
        speak("video played")
    elif "mute" in query:
        pyautogui.press("m")
        speak("video muted")
    elif "volume up" in query:
        volumeup()
        speak("Volume increased, sir")
    elif "volume down" in query:
        volumedown()
        speak("Volume decreased, sir")
    elif "open" in query:
        openappweb(query)
    elif "close" in query:
        closeappweb(query)
    elif "google" in query:
        searchGoogle(query)
    elif "youtube" in query:
        searchYoutube(query)
    elif "wikipedia" in query:
        searchWikipedia(query)
    elif "news" in query:
        latestnews()
    elif "calculate" in query:
        Calc(query)
    elif "whatsapp" in query:
        sendMessage()
    elif "temperature" in query:
        search = "temperature in pune"
        url = f"https://www.google.com/search?q={search}"
        r  = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div", class_ = "BNeawe").text
        speak(f"current{search} is {temp}")
    elif "weather" in query:
        search = "temperature in pune"
        url = f"https://www.google.com/search?q={search}"
        r  = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div", class_ = "BNeawe").text
        speak(f"current{search} is {temp}")
    elif "set alarm" in query:
        speak("Please provide the time for the alarm (format: HH:MM)")
        a = input("Please tell the time (format: HH:MM): ")
        alarm(a)
        speak("Alarm set successfully")
    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M")    
        speak(f"Sir, the time is {strTime}")
    elif "finally sleep" in query:
        speak("Ok, Going to sleep, sir")
        exit()
    elif "remember that" in query:
        rememberMessage = query.replace("remember that", "")
        rememberMessage = query.replace("jarvis", "")
        speak("You told me to remember that " + rememberMessage)
        remember = open("Remember.txt", "a")
        remember.write(rememberMessage)
        remember.close()
    elif "what do you remember" in query:
        remember = open("Remember.txt", "r")
        speak("You told me to remember that " + remember.read())

# Create speak button with a futuristic style
speak_button = tk.Button(root, text="Speak", font=("Helvetica", 12), bg="#2980b9", fg="white", command=speakButtonClicked)
speak_button.pack(pady=5)

# Create text button with a futuristic style
text_button = tk.Button(root, text="Text", font=("Helvetica", 12), bg="#2980b9", fg="white", command=textButtonClicked)
text_button.pack(pady=5)

# Run the GUI loop
root.mainloop()
