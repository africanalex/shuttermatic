#!/usr/bin/python

from Tkinter import *
import tkFont
import time, os, subprocess

win = Tk()

myFont = tkFont.Font(family = "Helvetica", size = 36, weight = "bold")

def buttonClicked():
    print("button was clicked")
    takePhoto(4)

def takePhoto(snap):
    if snap > 0:
        countdown(3)
        win.after(10000, takePhoto, snap-1)
    else:
        label["text"] = "Please wait..."
        win.after(100, assAndPrint)

def countdown(count):
    label["text"] = count
    if count > 0:
        win.after(1000, countdown, count-1)
    else:
        label["text"] = ""
        win.after(100, callCamera)

def callCamera():
    subprocess.call("sudo /home/pi/scripts/boothcamera.sh", shell=True)

def assAndPrint():
    subprocess.call("sudo /home/pi/scripts/assemble_and_print", shell=True)
    label["text"] = "Thanks!"
    exitButton.pack(side = BOTTOM)

def exitProgram():
    win.destroy()

win.title("Photobooth")
win.attributes("-fullscreen", True)
label = Label(win, font = myFont)
label.place(relx=0.5, rely=0.5, anchor=CENTER)
label["bg"] = "yellow"
win["bg"] = "yellow"
exitButton = Button(win, text = "Exit", font = myFont, command = exitProgram, height = 2, width = 6)

startButton = Button(win, text = "Start", font = myFont, command = buttonClicked, height = 2, width = 8)
startButton.pack()

mainloop()
    
