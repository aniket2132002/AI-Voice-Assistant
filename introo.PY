from tkinter import * #pip install tkinter
from PIL import Image,ImageTk,ImageSequence #pip install Pillow
import time
import pygame  #pip install pygame
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("1440x700")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("D:\Aj2.O\jarvis-iron-man.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("D:\Aj2.O\jarvis_plug_in.mp3")
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1440,700))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.10)
    root.destroy()

play_gif()
root.mainloop()

