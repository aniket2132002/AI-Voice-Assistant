import tkinter as tk
from tkinter import messagebox, simpledialog
import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
import webbrowser
import threading

# Initialize the voice engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    with open("Alarmtext.txt", "a") as timehere:
        timehere.write(query)
    os.startfile("alarm.py")

def validate_password():
    password = password_entry.get()
    with open("password.txt", "r") as pw_file:
        pw = pw_file.read().strip()

    if password == pw:
        messagebox.showinfo("Jarvis", "WELCOME SIR! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        password_window.destroy()  # Close the password window
        main_program()
    else:
        messagebox.showerror("Error", "Incorrect Password, Try Again!")
        password_entry.delete(0, tk.END)

def execute_command(query):
    query = query.lower()
    if "wake up" in query:
        from GreetMe import greetMe
        greetMe()

        while True:
            query = takeCommand().lower()
            if "go to sleep" in query:
                speak("Ok sir, You can call me anytime")
                break
            elif "change password" in query:
                speak("What's the new password")
                new_pw = simpledialog.askstring("Password", "Enter the new password:")
                with open("password.txt", "w") as new_password:
                    new_password.write(new_pw)
                speak("Done sir")
                speak(f"Your new password is {new_pw}")

            elif "play a game" in query:
                from game import game_play
                game_play()

            elif "screenshot" in query:
                im = pyautogui.screenshot()
                im.save("ss.jpg")

            elif "click my photo" in query:
                pyautogui.press("super")
                pyautogui.typewrite("camera")
                pyautogui.press("enter")
                pyautogui.sleep(2)
                speak("SMILE")
                pyautogui.press("enter")

            elif "translate" in query:
                from Translator import translategl
                query = query.replace("jarvis", "").replace("translate", "")
                translategl(query)

            elif "hello" in query:
                speak("Hello sir, how are you?")
            elif "i am fine" in query:
                speak("That's great, sir")
            elif "how are you" in query:
                speak("Perfect, sir")
            elif "thank" in query:
                speak("You are welcome, sir")

            elif "tired" in query:
                speak("Playing your favourite songs, sir")
                a = (1, 2, 3)
                b = random.choice(a)
                if b == 1:
                    webbrowser.open("https://www.youtube.com/results?search_query=hamari+adhuri+kahani+song")

            elif "pause" in query:
                pyautogui.press("k")
                speak("Video paused")
            elif "play" in query:
                pyautogui.press("k")
                speak("Video played")
            elif "mute" in query:
                pyautogui.press("m")
                speak("Video muted")

            elif "volume up" in query:
                from keyboard import volumeup
                speak("Turning volume up, sir")
                volumeup()
            elif "volume down" in query:
                from keyboard import volumedown
                speak("Turning volume down, sir")
                volumedown()

            elif "open" in query:
                from Dictapp import openappweb
                openappweb(query)
            elif "close" in query:
                from Dictapp import closeappweb
                closeappweb(query)

            elif "google" in query:
                from SearchNow import searchGoogle
                searchGoogle(query)
            elif "youtube" in query:
                from SearchNow import searchYoutube
                searchYoutube(query)
            elif "wikipedia" in query:
                from SearchNow import searchWikipedia
                searchWikipedia(query)

            elif "news" in query:
                from NewsRead import latestnews
                latestnews()

            elif "calculate" in query:
                from Calculatenumbers import Calc
                query = query.replace("calculate", "").replace("jarvis", "")
                Calc(query)

            elif "temperature" in query or "weather" in query:
                search = "temperature in pune"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"Current {search} is {temp}")

            elif "set alarm" in query:
                speak("Set the time")
                a = simpledialog.askstring("Alarm", "Please tell the time (e.g., 10 and 10 and 10):")
                alarm(a)
                speak("Done, sir")

            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M")
                speak(f"Sir, the time is {strTime}")

            elif "finally sleep" in query:
                speak("ok, Going to sleep, sir")
                exit()

            elif "remember that" in query:
                rememberMessage = query.replace("remember that", "").replace("jarvis", "")
                speak("You told me to remember that " + rememberMessage)
                with open("Remember.txt", "a") as remember:
                    remember.write(rememberMessage + "\n")
            elif "what do you remember" in query:
                with open("Remember.txt", "r") as remember:
                    speak("You told me to remember that " + remember.read())

def main_program():
    def on_send():
        query = search_bar.get()
        search_bar.delete(0, tk.END)
        execute_command(query)

    def listen_for_commands():
        while True:
            query = takeCommand()
            if query:
                execute_command(query)

    main_window = tk.Tk()
    main_window.title("Jarvis")
    main_window.configure(bg='black')

    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    main_window.geometry(f"{screen_width}x{screen_height}")

    search_bar = tk.Entry(main_window, font=("Helvetica", 14), bg="white", fg="black")
    search_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    send_button = tk.Button(main_window, text="Voice", font=("Helvetica", 14), command=on_send)
    send_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    threading.Thread(target=listen_for_commands, daemon=True).start()

    main_window.mainloop()

password_window = tk.Tk()
password_window.title("Jarvis Password")
password_window.configure(bg='black')
password_window.geometry("1300x640")

password_label = tk.Label(password_window, text="Enter Password:", font=("Helvetica", 14), bg='black', fg='white')
password_label.pack(pady=10)

password_entry = tk.Entry(password_window, font=("Helvetica", 14), show='*')
password_entry.pack(pady=10)

submit_button = tk.Button(password_window, text="Submit", font=("Helvetica", 14), command=validate_password)
submit_button.pack(pady=10)

password_window.mainloop()
