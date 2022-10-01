
from pygame import mixer
from tkinter import *
import os

#Function

def playsong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()

root = Tk()
root.title("Давайка паслухаеМ")

mixer.init()
songstatus = StringVar()
songstatus.set("choosing")

#playlist----------------------

playlist = Listbox(root, selectmode=SINGLE, bg="red", fg="white", font=("Calibri", 15), width=40)
playlist.grid(columnspan=5)

os.chdir(r'C:\Users\DELL\Music')
songs = os.listdir()
for i in songs:
    playlist.insert(END, i)

#battons

playbtn = Button(root, text="play", command=playsong)
playbtn.config(font=("Calibri", 20), bg="DodgerBlue1", fg="white", padx=7, pady=7)
playbtn.grid(row=1, column=0)

pausebtn = Button(root, text="pause", command=pausesong)
pausebtn.config(font=("Calibri", 20), bg="DodgerBlue1", fg="white", padx=7, pady=7)
pausebtn.grid(row=1, column=1)

stopbtn = Button(root, text="stop", command=stopsong)
stopbtn.config(font=("Calibri", 20), bg="DodgerBlue1", fg="white", padx=7, pady=7)
stopbtn.grid(row=1, column=2)

Resumebtn = Button(root, text="Resume", command=resumesong)
Resumebtn.config(font=("Calibri", 20), bg="DodgerBlue1", fg="white", padx=7, pady=7)
Resumebtn.grid(row=1, column=3)


mainloop()
